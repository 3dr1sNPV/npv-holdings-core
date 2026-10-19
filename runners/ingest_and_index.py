import json
import os
import re
from pathlib import Path

import fitz  # PyMuPDF
import openai
from docx import Document
from PIL import Image
import pytesseract

ROOT = Path(__file__).resolve().parents[1]
RAW_DIR = ROOT / "docs" / "raw" / "chat-history" / "AI"
TEXT_DIR = ROOT / "docs" / "text"
CHUNKS_DIR = ROOT / "docs" / "chunks"
EMBEDDINGS_DIR = ROOT / "docs" / "embeddings"
METADATA_PATH = ROOT / "docs" / "metadata.json"

SUPPORTED_EXTS = {".pdf", ".docx", ".doc", ".png", ".jpg", ".jpeg", ".txt", ".md", ".html"}

def normalize_text(text: str) -> str:
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    text = re.sub(r"\n{3,}", "\n\n", text)
    text = re.sub(r"[ \t]+\n", "\n", text)
    text = re.sub(r"\n{2,}", "\n\n", text)
    return text.strip()

def read_txt(file_path: Path) -> str:
    try:
        return normalize_text(file_path.read_text(encoding="utf-8", errors="ignore"))
    except Exception:
        return normalize_text(file_path.read_text(encoding="latin-1", errors="ignore"))

def read_docx(file_path: Path) -> str:
    doc = Document(file_path)
    paragraphs = [p.text.strip() for p in doc.paragraphs if p.text.strip()]
    return normalize_text("\n\n".join(paragraphs))

def read_pdf(file_path: Path) -> str:
    pages = []
    with fitz.open(file_path) as doc:
        for page in doc:
            pages.append(page.get_text("text"))
    return normalize_text("\n\n".join(pages))

def ocr_image(file_path: Path) -> str:
    try:
        image = Image.open(file_path)
        text = pytesseract.image_to_string(image)
        return normalize_text(text)
    except Exception:
        return ""

def chunk_text(text: str, source_name: str):
    if not text:
        return []
    chunks = []
    paragraphs = re.split(r"\n\s*\n+", text)
    current = []
    current_len = 0
    for para in paragraphs:
        para = para.strip()
        if not para:
            continue
        para_len = len(para)
        if current_len + para_len > 2600 and current:
            chunks.append("\n\n".join(current))
            current = [para]
            current_len = para_len
        else:
            current.append(para)
            current_len += para_len
    if current:
        chunks.append("\n\n".join(current))

    results = []
    for i, chunk in enumerate(chunks, start=1):
        results.append({
            "chunk_id": f"{source_name}::chunk-{i}",
            "source": source_name,
            "text": chunk,
        })
    return results

def maybe_embed_texts(chunks, model_name: str = "text-embedding-3-large"):
    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:
        return []

    try:
        client = openai.OpenAI(api_key=api_key)
    except Exception:
        return []

    embeddings = []
    for chunk in chunks:
        if not chunk.get("text"):
            continue
        try:
            resp = client.embeddings.create(
                model=model_name,
                input=chunk["text"][:6000],
            )
            embeddings.append({
                "chunk_id": chunk["chunk_id"],
                "source": chunk["source"],
                "embedding": resp.data[0].embedding,
            })
        except Exception:
            continue
    return embeddings

def ensure_dirs():
    TEXT_DIR.mkdir(parents=True, exist_ok=True)
    CHUNKS_DIR.mkdir(parents=True, exist_ok=True)
    EMBEDDINGS_DIR.mkdir(parents=True, exist_ok=True)

def main():
    ensure_dirs()
    files = []
    for path in sorted(RAW_DIR.rglob("*")):
        if path.is_file() and path.suffix.lower() in SUPPORTED_EXTS:
            files.append(path)

    metadata = []
    all_chunks = []

    for file_path in files:
        rel = file_path.relative_to(ROOT)
        source_name = str(rel)
        print(f"Processing: {source_name}")

        if file_path.suffix.lower() == ".pdf":
            text = read_pdf(file_path)
        elif file_path.suffix.lower() == ".docx":
            text = read_docx(file_path)
        elif file_path.suffix.lower() in {".txt", ".md", ".html"}:
            text = read_txt(file_path)
        elif file_path.suffix.lower() in {".png", ".jpg", ".jpeg"}:
            text = ocr_image(file_path)
        else:
            text = ""

        out_text_path = TEXT_DIR / (file_path.stem + ".txt")
        out_text_path.write_text(text or "", encoding="utf-8")

        chunk_items = chunk_text(text, source_name)
        all_chunks.extend(chunk_items)

        chunk_path = CHUNKS_DIR / (file_path.stem + ".jsonl")
        with chunk_path.open("w", encoding="utf-8") as f:
            for item in chunk_items:
                f.write(json.dumps(item, ensure_ascii=False) + "\n")

        metadata.append({
            "source": source_name,
            "text_path": str(out_text_path.relative_to(ROOT)),
            "chunk_path": str(chunk_path.relative_to(ROOT)),
            "size_bytes": file_path.stat().st_size,
            "chars": len(text or ""),
            "extension": file_path.suffix.lower(),
        })

    METADATA_PATH.write_text(json.dumps(metadata, indent=2, ensure_ascii=False), encoding="utf-8")

    embeddings = maybe_embed_texts(all_chunks)
    if embeddings:
        embeddings_path = EMBEDDINGS_DIR / "embeddings.jsonl"
        with embeddings_path.open("w", encoding="utf-8") as f:
            for item in embeddings:
                f.write(json.dumps(item, ensure_ascii=False) + "\n")

    print(f"Processed {len(files)} files")
    print(f"Created {len(all_chunks)} chunks")
    if embeddings:
        print(f"Created {len(embeddings)} embeddings")

if __name__ == "__main__":
    main()
