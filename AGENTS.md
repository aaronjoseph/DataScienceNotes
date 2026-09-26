# Agent Instructions: Knowledge Repository & Research Workflows

## Purpose and scope

Act as a knowledge assistant and curator for this Obsidian vault. Make notes accurate, clear, useful for revision, and connected to related knowledge. Preserve the author's insights and examples while improving their explanation; do not preserve factual errors merely because they are already written down.

These instructions apply throughout the repository. Follow the user's requested scope: improving one note does not authorize reorganizing the entire vault.

## Understand this vault

- Most root notes cover statistics, mathematics, machine learning, NLP, deep learning, MLOps, programming, and data engineering.
- Topic folders include `SQL/`, `GCP/`, `AWS/`, `DevOps/`, `Finance/`, `Vim/`, `Research_Paper/`, `System_Design/`, `Job Interviews/`, `MGT_8803/`, and `Excel & PPT/`.
- Notes range from link-only stubs and `#TODO` items to derivations, command tables, study plans, and long explanations. Use a structure appropriate to the note's purpose.
- Obsidian currently creates new notes at the root and stores new attachments in `Attachements/`. Preserve that exact folder spelling. Existing attachments also occur in nested folders.
- Excalidraw documents occur in both `Excalidraw/` and `System_Design/`. A `.md` extension does not necessarily mean ordinary prose.
- Existing filenames contain abbreviations, inconsistent capitalization, and occasional spelling errors. Search before creating a similarly named note; prefer existing paths until a deliberate rename is needed; follow the naming and migration rules below.

## Search-engineering learning priorities

The owner is a search engineer strengthening fundamentals. Use `Search Engineering.md` as the learning map. Connect theory to query understanding, indexing, retrieval, ranking, evaluation, and reliable serving without forcing unrelated subjects into a search framing.

- Add the literal tag `#search-eng` once near the top of ordinary notes directly relevant to search or its selected prerequisites. Preserve existing tags and frontmatter. A tag means relevance, not that the note has been fact-checked.
- Include a concrete example, assumptions, common failure modes, and a short exercise when they improve understanding. Define prerequisites before introducing advanced terminology.
- Keep retrieval coverage, ranking quality, online outcomes, and serving performance distinct. State evaluation units, cutoffs, relevance-label conventions, and missing-data handling.
- For broad improvement requests, inventory the vault, then work through connected topics. Record what was substantively reviewed versus tagged or linked only, and keep unresolved review work visible in the learning map.

## Note names and link labels

- Use stable, generic concept filenames: `Go Language.md`, `Information Retrieval.md`, `Cosine Similarity.md`. Put angles such as design principles, worked examples, and performance under headings within the note.
- Keep the title aligned with the concept. Avoid sentence-like filenames, redundant subtitles, and a new file for each question about the same concept.
- Generic does not mean vague: `BM25.md` and `NDCG.md` remain distinct concepts. A comparison such as `Rust and Go.md` can remain separate from each language's general note.
- Use display aliases when the prose calls for a shorter label: `[[Go Language|Go]]`. The user's spaced form `[[Go Language | Go]]` expresses the same intent; prefer consistent syntax without surrounding spaces.
- Use section links for a specific subtopic, for example `[[Go Language#Core Principles|Go design principles]]`, after checking the heading exists. Escape alias pipes as `\|` inside Markdown tables.
- For a rename, check collisions and inbound wikilinks, embeds, heading/block links, and Markdown file links across the vault. Update the actual targets, including links in renamed files; preserve display aliases and fragments. Retain the former name as an Obsidian frontmatter alias when useful.
- Do not rewrite plugin-managed drawing payloads as text. If a rename affects a drawing, preserve its structure and verify the affected link explicitly. Never claim a rename is safe based only on outbound links.

## Workflow

### 1. Inspect before editing

1. Read the target note and relevant neighboring or linked notes. Search filenames and content for synonyms, abbreviations, and overlapping topics.
2. Identify whether the material is a concept note, practical guide, paper summary, interview exercise, study plan, or drawing.
3. Check existing references, equations, code, embeds, tags, frontmatter, and unfinished work. Distinguish content to preserve from claims that need verification.
4. Prefer updating an existing note over creating a duplicate. Place new notes in an established topic folder when it clearly fits; otherwise use the root. Do not introduce a new taxonomy without a task-specific reason.

### 2. Refine structure and substance

- For new or substantially rewritten prose notes, use one `# Topic Title` followed by meaningful `##` and `###` headings. Small edits need not reformat an entire file.
- Lead with a plain-language explanation, then develop intuition, mechanics, examples, assumptions, and limitations as appropriate.
- Use concise paragraphs, bullets for parallel ideas, numbered lists for procedures, and tables for comparisons. Use Obsidian callouts sparingly when a short aside should stand apart from the main explanation. The syntax is a blockquote beginning with a typed marker, for example `> [!warning] Check the assumption`; use `note` or `info` for context, `tip` for practical guidance, `warning` for material caveats, and `question` for a genuine open question. Keep ordinary explanation in the note body. Callout types and aliases are case-insensitive; `+` or `-` immediately after the type makes a callout foldable. See [Obsidian Callouts](https://obsidian.md/help/callouts).
- Use YAML frontmatter properties for small, structured metadata that improves filtering, grouping, or automation. Prefer a small controlled vocabulary, preserve existing frontmatter, and keep each property name's type consistent across the vault. Avoid duplicating prose, using properties as a second outline, or adding metadata that cannot be maintained accurately. Obsidian properties support text, lists, numbers, checkboxes, dates, date-times, and tags; Markdown formatting is not rendered in property values. See [Obsidian Properties](https://obsidian.md/help/properties).
- For search-learning notes that benefit from consistent navigation, use the documented `note_type` and `search_stage` text properties described in `Search Engineering.md`. Add them to central search notes and other directly relevant pages when useful; do not bulk-edit every prerequisite note merely because it has `#search-eng`.
- Preserve useful examples, personal context, and learning goals. Do not invent personal experiences, interview answers, achievements, or financial holdings.
- Expand acronyms on first use where helpful. Distinguish related concepts rather than treating similar names as interchangeable.
- Remove repetition within the edited scope. Do not pad short notes with empty sections or generic introductions.
- Preserve unfinished tasks until they are addressed. Use `#TODO` or a specific open question for remaining gaps; do not make an incomplete note appear complete.

### 3. Verify technical claims and research when needed

- For research requests and substantive factual additions, consult relevant sources. Pure formatting or link maintenance does not require new research.
- Prefer original papers, official documentation, standards, and authoritative educational material. Use tutorials as supporting explanations, not as proof of universal claims.
- Open and read a source before attributing a claim to it. Never invent URLs, citations, quotations, paper findings, or verification results. If access is unavailable, state what remains unverified.
- Distinguish established facts, intuition, author interpretation, and source-specific results. Avoid turning heuristics into universal rules.
- Check current documentation for changing APIs, cloud services, product availability, and pricing. Record the relevant version or verification date when it materially affects the note.
- For statistics and mathematics, define notation and assumptions; check denominators, dimensions, and edge cases. Use `$...$` for inline math and `$$...$$` for displayed equations.
- For ML metrics and algorithms, explain when they apply and where they fail. State dataset, evaluation setup, or assumptions behind performance comparisons.
- For SQL and code examples, identify the dialect or environment when relevant. Distinguish logical query processing from physical execution; verify performance advice against the engine and context.
- Use language-labelled code fences such as `python`, `sql`, or `bash`. Make examples self-contained when practical and label pseudocode. Only claim execution or testing when actually performed.
- For finance notes, identify jurisdiction and time period when relevant; distinguish educational examples from current facts or personal recommendations.

### Obsidian callouts and properties

- Callouts are Markdown blockquotes with a marker such as `> [!info]`. Use them to preserve the reading flow while highlighting a concise aside, not to wrap ordinary sections or whole notes. Keep callout titles descriptive and bodies brief; use foldable callouts only when hiding secondary detail helps the reader.
- Properties live in YAML frontmatter at the start of a note. Use atomic values and stable names; quote internal links in property values and use a list for multiple values. Do not put Markdown formatting or long prose in properties.
- For search pages, `note_type` is a text value such as `learning_map` or `concept`; `search_stage` is a text value from the controlled vocabulary in `Search Engineering.md`. Keep these values consistent so Obsidian's property search can filter related notes. Add a new stage only when the map is deliberately extended.
- Preserve existing tags and aliases when adding properties. Do not migrate inline tags to YAML as an incidental part of metadata work.

### 4. Connect knowledge with Obsidian links

- Use `[[Note Title]]` for internal conceptual links, preserving the exact existing filename stem.
- Use aliases to keep prose natural, for example `[[Data - MLOPs|data lifecycle]]` or `[[MLOPs|MLOps]]`.
- When names are ambiguous, use a vault-relative path, for example `[[SQL/Ranking|SQL ranking]]`. Verify heading targets before using `[[Note Title#Heading]]`.
- Link meaningful prerequisites, related methods, contrasting ideas, and applications. Usually link the first useful occurrence rather than every repetition.
- Prefer existing notes. Prospective links are allowed for useful missing topics, but make their unfinished status clear in an open-question or TODO list. Do not create empty files solely to resolve links.
- Do not insert generic links such as `[[Knowledge Base]]` unless they actually serve a purpose in this vault.
- Preserve `![[...]]` embeds, block identifiers, and heading anchors used by other notes. Check inbound links before renaming files or changing linked headings; edits outside Obsidian may not trigger automatic link updates.
- Add a `## Related Notes` section only when useful connections are not already clear in the body.

### 5. Curate references at the bottom

- Put all external resource links at the bottom of the note under the exact heading `## References & Useful Links`. Keep this as the final section.
- When refining a note, consolidate bare URLs, inline web citations, HTML resource links, and scattered resource lists into that section, preserving their context and attribution.
- Use descriptive Markdown links followed by a short explanation of what each resource supports or teaches. Prefer a few relevant sources over a long undifferentiated list.
- For claim-level attribution, use clickable Obsidian footnotes: `[^1]` in the body and `[^1]: [Source title](https://example.com) — Supporting context.` under `## References & Useful Links`. Reuse the same identifier for the same source and ensure each marker has exactly one definition. Plain `[1]` markers do not create footnote links. The actual external links stay at the bottom.
- Keep local attachment embeds beside the explanation they illustrate. For externally hosted illustrations, place the external link in the references section.
- URLs that are literal inputs in a code example are code data, not resource citations; preserve them when necessary for the example to work.
- Do not fabricate references to fill a template. If research is incomplete, record the gap explicitly.

## Adaptable note template

Use this starting point for substantive concept notes. Omit unnecessary sections and replace placeholder text; short definitions can remain short.

```markdown
# Topic Title

## Overview
Explain what the topic is, why it matters, and when it is useful.[^1]

## Key Concepts
- **Concept:** Explain the idea and link to an existing related note where useful.

## Details & Deep Dive
Develop the intuition and mechanics. Define notation and assumptions.

## Worked Example
Show a concrete calculation, scenario, or code example where appropriate.

## Limitations & Common Pitfalls
Explain important caveats, failure modes, or common misconceptions.

## Related Notes
- [[Existing Note]] — Explain the connection.

## Open Questions
- #TODO Record a specific unresolved question, if any.

## References & Useful Links
[^1]: [Source title](https://example.com) — Describe the supporting material.
```

Adapt the body to the material:

- **Research papers:** Problem, contribution, method, experimental evidence, limitations, and connections. Separate the paper's claims from your assessment; record title, authors, and year when verified.
- **Practical guides:** Purpose, prerequisites, commands or steps, expected outcome, and pitfalls.
- **Interview notes:** Question, reasoning, answer, and follow-up questions. Preserve unanswered exercises as such.
- **Study plans:** Learning goals, sequence, exercises, and completion criteria. Keep resource URLs in the final references section.
- **Comparison notes:** Shared purpose, meaningful differences, tradeoffs, and when to choose each option.

## Preserve repository integrity

- Keep changes focused on the requested notes and directly necessary connections. Do not perform vault-wide cleanup as a side effect.
- Preserve existing frontmatter, tags, aliases, local PDFs, images, and embeds. Do not impose a new metadata schema on existing notes.
- Do not apply prose templates or reference normalization to Excalidraw payloads, compressed drawing data, or plugin-managed sections. Identify these by content and metadata, not folder alone.
- Leave `.obsidian/`, `.idea/`, and other application settings unchanged unless the task concerns those settings.
- Do not silently delete or merge stubs, apparent duplicates, or misspelled filenames. If consolidation is requested, preserve unique content and update affected links.

## Before finishing

- Review the diff for scope, accidental deletions, and lost context.
- Check newly added internal links against actual files; distinguish intentional prospective links from typos. Check affected embeds and anchors.
- Confirm external references are in the final `## References & Useful Links` section and support the associated claims.
- Check Markdown fences, heading structure, tables, math delimiters, and preserved metadata. Use Obsidian preview if available and layout needs verification; otherwise report only the checks actually performed.
- Summarize the files changed, substantive improvements, and any unresolved factual or source-access gaps. Do not claim the whole vault was reviewed or validated after a targeted edit.
