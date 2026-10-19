# This repo contains raw AI export files and is prepared for ingestion into structured text artifacts.

This repository includes raw PDF/DOCX/PNG assets under `docs/raw/chat-history/AI`.

The ingestion pipeline turns those raw files into structured outputs:

- `docs/text/` — cleaned plain-text per source
- `docs/chunks/` — chunked JSONL text for downstream indexing
- `docs/metadata.json` — metadata manifest describing every source file
- `docs/embeddings/` — optional vector embeddings (generated only when `OPENAI_API_KEY` is configured)

How to run locally

1. Create a virtual environment
   ```bash
   python -m venv .venv
   source .venv/bin/activate   # Windows: .venv\Scripts\activate
   pip install -r requirements.txt
