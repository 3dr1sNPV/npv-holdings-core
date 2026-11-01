# NPV HOLDINGS — Copilot Portfolio and Engineering Handover

**Snapshot:** 2026-11-02  
**Repository:** `3dr1sNPV/npv-holdings-core` (public)  
**Default branch at inspection:** `main`  
**Handover branch:** `copilot/ai-handover-2026-11-02`  
**Purpose:** Bring GitHub Copilot up to date on NPV Holdings, its known ventures, current repository artifacts, cross-project architecture and unresolved portfolio recovery.

> This is a source-backed handover snapshot, not proof that every past ChatGPT discussion, archive, subsidiary sub-branch or naming rule has been recovered. Do not invent missing details.

## 1. Organizational identity and authority

NPV Holdings is the parent/organizational root for the portfolio. Each venture has its own domain, product logic, data boundaries, operational records and roadmap. The user's stated ownership rule is that NPV Holdings owns 100% of each company. Git records are intended to be authoritative for company types and relationship types once the complete hierarchy is reconciled.

NPV Holdings combines:
- strategic holding, capital allocation, R&D and intellectual property;
- digital businesses and e-commerce;
- aviation, logistics and telemetry;
- automotive, marine and industrial engineering;
- luxury design, fragrance and audio;
- software, automation, infrastructure, fintech and security.

The long-term financial concept is a cash-flow flywheel: scalable digital/software businesses can fund more capital-intensive engineering, R&D and physical product ventures. This is a strategic model, not evidence that the ventures currently generate revenue or that automated capital transfers are implemented.

## 2. Critical organizational version distinction

The repository contains two materially different organization-chart generations. Preserve both. Do not merge them, silently rename entities, or assume a one-to-one mapping until historical records, naming rules and ownership/relationship evidence are reconciled.

### Generation A — seven broader operating groups

Source: `docs/processed/npv_org_chart.md`.

1. **House EDRIS** — fashion and luxury.
   - EDRIS Atelier / TUX GEN (bespoke tailoring)
   - The Masked Rabbit crest
   - EDRIS fragrance
   - Digital and physical ecosystem (shop, passport, assets)
2. **Obsidian Motors** — automotive engineering.
   - Project Loki
   - Project Snow White 2.0
3. **Aero Logistics Systems** — aviation and technology.
   - Civil aviation research and controls
   - Electronic baggage tags (UHF/RAIN RFID, UWB telemetry)
4. **Abyss Marine** — marine systems and advanced fluids.
   - Submersible buoyancy systems and pressure vessels
5. **Kryon Thermal & Patents** — HVAC and IP commercialization.
   - HVAC R&D and productization
   - Patent portfolio and licensing
6. **Nocturne Audio Works** — music and entertainment.
   - Music production and composition
   - Studio infrastructure and hardware
7. **Kepler Technologies** — D2C and software.
   - Direct-to-consumer retail (DaddysKiosk and shops)
   - Digital infrastructure, software repositories and automation

This chart is a distinct historical generation, not automatically the current legal subsidiary list.

### Generation B — twelve subsidiary blueprint

Sources: `AGENTS.md`, `CONGLOMERATE_CONTEXT.md`, `CONGLOMERATE_MASTER_SPEC.md`.

1. **Daddyskiosk Global** — e-commerce, print-on-demand and digital assets.
2. **House EDRIS** — luxury fashion, design and architecture.
3. **Project Avi** — aviation baggage tracking and telemetry.
4. **Project Loki** — automotive engineering and restomods.
5. **NPV Patents & R&D** — IP, hardware and engineering R&D.
6. **EDRIS Acoustics** — audio engineering, amplifiers and DSP.
7. **NPV Digital Infrastructure** — cloud infrastructure, automation and DevOps.
8. **Aero Logistics Ventures** — air cargo and commercial logistics.
9. **NPV Global Properties** — international real estate.
10. **EDRIS Bespoke Fragrance** — perfumery and fragrance manufacturing.
11. **NPV Fintech Systems** — treasury, financial systems and multi-currency operations.
12. **NPV Security Ventures** — hardware encryption and physical security.

The 12-entity blueprint contains descriptions and proposed technology/workflows. It does not prove that each venture is incorporated, staffed, funded, deployed or commercially operating. Verify legal status separately.

## 3. Naming, hierarchy and ownership — unresolved recovery work

The owner has stated that the venture branches contain deeper sub-branches and that a naming algorithm, naming rules, codes, prefixes and hierarchy conventions were developed in prior ChatGPT work. The complete rules have not yet been recovered into this snapshot.

Required recovery:
- search prior ChatGPT exports/history and the repository's archive material;
- inspect the large AI archive parts `AI.7z.001` and `AI.7z.002`;
- inspect `docs/raw`, `docs/processed`, `docs/text`, chunk collections, ledgers and project records;
- inspect the 146-page `Elden Ring Run Discussion - Google Gemini` export in the Aether repository, whose later sections reportedly contain SNAKE/Big Boss central-AI and project-sector discussion;
- inspect other Gemini/ChatGPT exports, including `EDRIS_MASTER_CONTEXT_FOR_GEMINI`, but separate EDRIS product context from Holdings legal/organizational records;
- recover all subsidiary sub-branches and project naming algorithms without guessing.

For every recovered hierarchy item, record: exact original name; parent; entity type; relationship type; source document/chat; source date/version; confidence; current/historical status; and any conflicts. Keep verbatim source evidence where possible. Distinguish source fact, owner decision, inference and unresolved question.

## 4. Group-wide AI and Aether boundary

**NPV Intelligence / Holdings Intelligence is group-wide infrastructure.** It is intended to serve the entire portfolio, with each venture using it differently for its own authorized data and workflows.

**Aether is the connectivity venture/platform**, not the group-wide intelligence system. It can expose authorized portfolio hierarchy and roadmap context, but must not become the parent namespace or gain unrestricted access to every subsidiary's data.

Owner-defined strategic sequence:
1. Complete Aether to a sufficiently capable and reliable state.
2. Use Aether as a platform to develop and deploy NPV autonomous intelligence.
3. Once NPV autonomous intelligence is mature, replace Aether's initial AI layer with NPV autonomous AI.

Architecture requirements:
- NPV Holdings remains the organizational root.
- Keep identity, tenancy, namespaces, permissions, data classification, secrets and business logic separated by venture.
- Shared AI services should be multi-tenant by design, with explicit data access and provenance.
- No cross-venture data access merely because ventures share an owner.
- Aether customer identities/configurations/subscriptions must never collide with Holdings corporate identities, financial ledgers or subsidiary records.
- Preserve independent venture ownership and domain boundaries while enabling authorized shared services.

## 5. Current repository contents — present, not yet exhaustively audited

The `main` branch contains:
- `AGENTS.md` — 12-subsidiary operating context and agent guidance.
- `CONGLOMERATE_CONTEXT.md` — 12-subsidiary overview and cash-flow model.
- `CONGLOMERATE_MASTER_SPEC.md` — detailed 12-subsidiary operational blueprint.
- `docs/processed/npv_org_chart.md` — seven-group hierarchy generation.
- `AI.7z.001` and `AI.7z.002` — split AI archive parts.
- `docs/raw`, `docs/processed`, `docs/text` and knowledge/chunk directories — imported project and chat material.
- `ledger/global_revenue_state.json` — a version-controlled revenue-state record; inspect schema, provenance and update semantics before any write.
- `npv-core/modules/pod-pipeline/live_master_catalog.json`.
- `npv_master_orchestrator.py` and `npv_theme_generator.py`.
- `runners/ingest_and_index.py`.
- `‎Gemini - direct access to Google AI.docx` and associated exported text/PDF material.

The presence of a script, archive, manifest or ledger does not establish that it is reliable, current, secure, complete or deployed. Audit entry points, dependencies, workflows, data lineage, permissions and tests before modifying or operationalizing them.

## 6. Existing documents and their authority

Read these before portfolio changes:
1. `AGENTS.md`
2. `CONGLOMERATE_CONTEXT.md`
3. `CONGLOMERATE_MASTER_SPEC.md`
4. `docs/processed/npv_org_chart.md`
5. Relevant source exports under `docs/raw` and `docs/text`
6. Relevant ledgers and source manifests
7. Aether repository's `docs/COPILOT_HANDOVER_2026-11-02.md` when cross-project architecture or the Aether/NPV Intelligence boundary matters.

If sources conflict, preserve both and create a conflict record. Do not silently rewrite old source files to match a newer interpretation. Use a new dated/versioned decision record.

## 7. Portfolio-level roadmap

### P0 — Recover and normalize the enterprise map
- Recover all seven-group and 12-subsidiary source generations and determine their chronology.
- Recover all sub-branches, projects, naming algorithms, prefixes, codes and relationship types.
- Reconcile exact legal entity names, trade names, product names, project names and internal platform names.
- Produce a canonical machine-readable organization registry only after source-backed reconciliation.
- Record 100% ownership relationships as owner-stated policy, then verify legal-entity records before representing them as registered facts.
- Keep a versioned decision log and migration map from old names to new names; never silently discard history.

### P1 — Holdings Intelligence architecture
- Define group-wide identity, access control, venture namespaces, data classifications, provenance and audit.
- Separate shared intelligence services from venture-specific domain services.
- Build retrieval over approved records and repositories with source citations, version tracking and retention controls.
- Design shared task orchestration and specialist routing without sharing private hidden reasoning or secrets.
- Integrate with Aether only through explicit versioned APIs and authorized context contracts.
- Ensure each venture can use shared intelligence without seeing another venture's restricted data.

### P2 — Enterprise operations and financial records
- Audit orchestrator, runners, workflows, ledgers and catalogs.
- Determine whether any recurring jobs are active, safe, idempotent and monitored.
- Define ledger schemas, reconciliation, approvals, audit and backup/restore.
- Do not automate money movement, financial postings, external orders, legal filings or destructive operations without explicit owner authorization and deterministic safeguards.
- Never infer actual revenue, orders, legal ownership or business activity from a placeholder or stale JSON manifest.

### P3 — Venture execution
- Create a project index with one authoritative page per venture and its subprojects.
- Track each venture's purpose, product scope, current artifacts, dependencies, status, risks, owner decisions and next milestones.
- Keep engineering repositories separate where appropriate; cross-link them instead of duplicating entire codebases.
- Use shared standards for security, contracts, CI, release provenance and documentation while respecting each venture's stack.

### P4 — Governance and commercialization
- Reconcile intellectual-property ownership, licensing, contributor rights, trademarks, data protection and jurisdictional requirements.
- The existing commercial/IP document in Aether is a strategy draft; it is not a legal agreement or an adopted licence.
- Do not publish or change licences, CLAs, prices, contracts, trademarks or legal claims without explicit owner approval and qualified legal review.

## 8. Important project-specific context to preserve

- **House EDRIS:** luxury house, design and product ecosystem. EDRIS is a venture/brand domain; TUX GEN is its internal bespoke design/atelier system, not a public sub-brand. Consult the EDRIS master catalogue and execution master for product decisions.
- **Project Avi / electronic baggage tags:** aviation telemetry and baggage tracking; preserve distinction between aviation research, hardware tags and logistics ventures until organizational mapping is reconciled.
- **Project Loki:** automotive engineering/restomod project; distinguish it from the broader Obsidian Motors group generation.
- **EDRIS Acoustics / Nocturne Audio Works:** preserve the 12-subsidiary and seven-group names as different versions until reconciled.
- **NPV Digital Infrastructure:** shared infrastructure/DevOps capability; do not assume it is identical to NPV Intelligence.
- **NPV Fintech Systems:** financial/treasury domain; financial data is restricted and must not be casually passed to external models.
- **NPV Security Ventures:** security hardware and access domain; apply restricted handling to cryptographic material.
- Other ventures in the 12-entity list must receive their own project records; do not fill missing sub-branches with invented detail.

## 9. Privacy and information classification

Do not indiscriminately feed every imported personal chat export into Copilot or external model providers.
- Public: approved public descriptions, public code and published material.
- Internal: non-sensitive architecture, plans and operational docs.
- Confidential: business strategy, unpublished IP, supplier/commercial terms and internal financial analysis.
- Restricted: credentials, private keys, customer personal data, personal identity/health details, private subscription links/configs, financial account access and security-sensitive designs.

Keep personal EDRIS fitting/body measurement records and other personal profile material out of general NPV Holdings instructions. Load only the minimum relevant information for a specifically authorized EDRIS task, and never send sensitive records to an external provider without an explicit approved data policy. Never commit secrets or customer data.

## 10. Copilot execution protocol

For every task:
1. Identify repository, branch, base SHA and working tree state.
2. Read relevant project docs and source evidence.
3. Classify data and task risk.
4. State what is known, inferred, proposed and unresolved.
5. Make the smallest coherent change on an assigned feature branch.
6. Add tests and validation for behavior changes.
7. Inspect diffs for secrets, personal data, generated files, unrelated edits and weakened controls.
8. Report exact changed paths, commit, tests, CI results, limitations and next steps.
9. Do not merge, deploy, spend, alter financial/customer state, delete records, rewrite history or change legal/licensing terms without explicit owner authorization.

Use dated decision records rather than rewriting source history. Prefer versioned machine-readable registries for canonical entities and relationships once the hierarchy is proven. Keep provenance for every imported/recovered fact.

## 11. Immediate next actions

1. Inspect current branch and confirm this handover branch is checked out.
2. Audit `AGENTS.md`, context/spec files and seven-group chart; record contradictions.
3. Inventory every file under archive, raw, processed, text, chunks, ledger and `npv-core` without executing untrusted archives or scripts.
4. Recover and document the naming algorithm and full sub-branch hierarchy from source exports.
5. Build a source-linked conflict register for seven-group versus 12-subsidiary generations.
6. Audit orchestrator, runners, workflows and ledger semantics; distinguish code present from active/verified operations.
7. Define Holdings Intelligence requirements and the Aether integration boundary before implementing cross-project services.
8. Keep the Aether build-first strategic sequence intact.

## 12. Status vocabulary

- **IMPLEMENTED:** code/document exists and relevant behavior is covered by tests.
- **VERIFIED:** tested on a named commit/environment with evidence.
- **PARTIAL:** some components exist; integrations or requirements remain.
- **PLANNED:** owner-approved direction not yet implemented.
- **PROPOSED:** idea needing a decision.
- **BLOCKED:** waiting on a named dependency or approval.
- **UNVERIFIED:** evidence missing, incomplete or stale.

Do not equate a document's claim of "complete" with deployed, legally established or operational reality.
