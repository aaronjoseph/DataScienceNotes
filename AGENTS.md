# Agent Instructions: Knowledge Repository & Research Workflows

## Purpose and priorities

Act as a knowledge assistant and curator for this Obsidian vault. Make notes accurate, clear, useful for revision, and connected to related knowledge. Preserve the author's insights and examples while improving their explanation; correct factual errors rather than preserving them because they are already written down.

When guidance competes, apply this order:

1. The user's explicit request and scope.
2. Factual accuracy.
3. Preservation of the author's unique content, links, embeds, and metadata.
4. The conventions in this file.
5. The existing style of the note being edited.

Stay within the requested scope: improving one note does not authorise reorganising the vault, bulk metadata edits, or unrelated cleanup. If a request is ambiguous and a wrong guess would be costly to undo, ask first; otherwise choose the most useful interpretation and state it in the final summary.

## Vault layout

- Most root notes cover statistics, mathematics, machine learning, NLP, deep learning, MLOps, programming, and data engineering.
- Topic folders include `SQL/`, `GCP/`, `AWS/`, `DevOps/`, `Finance/`, `Vim/`, `Research_Paper/`, `System_Design/`, `Job Interviews/`, `MGT_8803/`, and `ISYE_6501/`.
- Notes range from link-only stubs and `TODO:` items to derivations, command tables, study plans, and long explanations. Match the structure to the note's purpose.
- Obsidian creates new notes at the vault root and stores new attachments in `Attachements/`; preserve that exact spelling. Older attachments also occur in nested folders.
- Excalidraw drawings occur in `Excalidraw/` and `System_Design/`. Identify them by `excalidraw-plugin` frontmatter or drawing payload, not by the `.md` extension or folder alone.
- Filenames contain abbreviations, inconsistent capitalisation, and occasional misspellings. Search before creating a similarly named note, and link to existing paths as they are.
- Leave `.obsidian/`, `.idea/`, and other application settings unchanged unless the task concerns them.
- The working tree may contain uncommitted, in-progress edits. Never discard, revert, or overwrite changes you did not make.

## Search-engineering focus

The owner is a search engineer strengthening fundamentals. `Search Engineering.md` is the learning map and defines the controlled vocabulary for search metadata. Connect theory to query understanding, indexing, retrieval, ranking, evaluation, and reliable serving where the connection is real; do not force unrelated subjects into a search framing.

- Add `search-eng` to the YAML `tags` list of notes directly relevant to search or its selected prerequisites. The tag signals relevance, not factual review.
- On central search notes and substantively revised search concept notes, set the `note_type` and `search_stage` text properties using values defined in `Search Engineering.md`. Do not bulk-add them to every `search-eng` prerequisite, and add a new stage only when the map is deliberately extended.
- Keep retrieval coverage, ranking quality, online outcomes, and serving performance distinct. State evaluation units, cutoffs, relevance-label conventions, and missing-data handling.
- Include a concrete example, assumptions, common failure modes, and a short exercise when they aid understanding. Define prerequisites before advanced terminology.
- For broad improvement requests, inventory the vault first, then work through connected topics. Record what was substantively reviewed versus only tagged or linked, and keep unresolved review work visible in the learning map.

## Data-science foundations tag

`ds-foundations` marks notes on core data-science fundamentals: statistics and probability, the calculus and linear algebra behind model training, classical machine-learning algorithms and ensembles, deep-learning fundamentals (optimisers, activations, initialisation, automatic differentiation, and basic architectures such as CNNs), introductory reinforcement learning such as MDPs, time series, basic text and data representations, and everyday data tooling such as pandas and regular expressions.

- Add it to the YAML `tags` list of notes you create or substantively revise in these areas, alongside `search-eng` when both apply. Like `search-eng`, it signals scope, not factual review.
- Do not bulk-tag the vault; add it as notes are revised, or during an explicitly requested tag migration.
- It replaced the ambiguous `oan` tag on 27 September 2026, and absorbed the `dl` and `DL` tags the same day. Do not reintroduce `oan`, `dl` or `DL`, or create near-synonyms such as `ds-basics`, `dl-foundations` or `fundamentals`.
- This tag alone does not justify `note_type` or `search_stage`; those properties remain reserved for search notes as described above.
- Topic tags can sit alongside it. Use `clustering` for clustering algorithms, clustering evaluation, and segmentation notes built on clustering, such as `K Means.md`, `DBSCAN.md`, and `RFM.md`. Reuse an existing topic tag before creating a new one.

## Workflow

### 1. Inspect before editing

1. Read the target note and relevant linked or neighbouring notes. Search filenames and content for synonyms, abbreviations, and overlapping topics.
2. Classify the material: concept note, practical guide, paper summary, interview exercise, study plan, comparison, or drawing.
3. Note existing frontmatter, tags, aliases, embeds, block identifiers, equations, code, references, and unfinished work. Separate content to preserve from claims to verify.
4. Prefer updating an existing note over creating a duplicate. Put a new note in an established topic folder when it clearly fits; otherwise use the root. Do not introduce a new taxonomy without a task-specific reason.

### 2. Refine structure and substance

- Obsidian shows the filename as the inline title, so do not open the body with a `#` heading that repeats it; start with a concise lead or the first meaningful `##` section. Keep a body `#` heading only when it adds a distinct title. Before removing a duplicate heading from an existing note, check that no links target it.
- Use meaningful `##` and `###` headings for new or substantially rewritten notes. Small edits need not reformat the whole file.
- Lead with a plain-language explanation, then develop intuition, mechanics, examples, assumptions, and limitations as appropriate.
- Expand acronyms on first use where helpful, and distinguish related concepts instead of treating similar names as interchangeable.
- Preserve useful examples, personal context, and learning goals. Never invent personal experiences, interview answers, achievements, or financial holdings.
- Remove repetition within the edited scope. Do not pad short notes with empty sections or generic introductions; short definitions may stay short.
- Keep unfinished tasks until they are addressed. Record remaining gaps as `TODO:` or a specific open question; do not make an incomplete note look complete.

### 3. Verify claims and research

- Research substantive factual additions and explicit research requests. Pure formatting or link maintenance does not need new research.
- Prefer original papers, official documentation, standards, and authoritative educational material. Use tutorials as supporting explanations, not as proof of universal claims.
- Open and read a source before attributing a claim to it. Never invent URLs, citations, quotations, paper findings, or verification results. If a source is inaccessible, state what remains unverified.
- Distinguish established facts, intuition, the author's interpretation, and source-specific results. Do not turn heuristics into universal rules.
- Check current documentation for changing APIs, cloud services, product availability, and pricing; record the version or verification date when it materially affects the note.
- **Mathematics and statistics:** Define notation and assumptions; check denominators, dimensions, and edge cases.
- **ML metrics and algorithms:** Explain when they apply and where they fail; state the dataset, evaluation setup, or assumptions behind performance comparisons.
- **SQL and code:** Name the dialect or environment when relevant; distinguish logical query processing from physical execution; verify performance advice against the engine and context. Use language-labelled fences such as `python`, `sql`, or `bash`, make examples self-contained where practical, label pseudocode, and claim execution or testing only when actually performed.
- **Finance:** State jurisdiction and time period when relevant; separate educational examples from current facts or personal recommendations.

### 4. Connect notes

- Link with `[[Note Title]]` using the exact existing filename stem. Use a vault-relative path when names are ambiguous, for example `[[SQL/Ranking|SQL ranking]]`.
- Use display aliases for natural prose, written without spaces around the pipe: `[[Go Language|Go]]`, `[[Data - MLOPs|data lifecycle]]`. Treat the spaced form `[[Go Language | Go]]` as the same intent. Escape the pipe as `\|` inside Markdown tables.
- Use section links such as `[[Go Language#Core Principles|Go design principles]]` only after confirming the heading exists.
- Link meaningful prerequisites, related methods, contrasting ideas, and applications, usually at the first useful occurrence rather than every repetition. Do not add generic hub links that serve no purpose in this vault.
- Prefer existing notes. Prospective links to useful missing topics are allowed when listed under a TODO or open question; do not create empty files solely to resolve links.
- Preserve `![[...]]` embeds, block identifiers, and headings that other notes link to.
- Add `## Related Notes` only when useful connections are not already clear from the body.

### 5. Curate references

- Put all external resource links in a final section titled exactly `## References & Useful Links`.
- When refining a note, consolidate bare URLs, inline web citations, HTML resource links, and scattered resource lists into that section, keeping their context and attribution.
- Use descriptive Markdown links, each followed by a short explanation of what it supports or teaches. Prefer a few relevant sources to a long undifferentiated list.
- For claim-level attribution, use Obsidian footnotes: `[^1]` in the body and `[^1]: [Source title](https://example.com) — Supporting context.` in the references section. Reuse an identifier for the same source and give each marker exactly one definition. Plain `[1]` markers are not footnotes.
- Keep local attachment embeds beside the explanation they illustrate; move links to externally hosted illustrations into the references section.
- URLs that are literal inputs in a code example are code data, not citations; leave them in place.
- Do not fabricate references to fill a template. If research is incomplete, record the gap explicitly.

## Obsidian conventions

### Frontmatter, tags, and properties

- Frontmatter sits at the very start of the file, followed by one blank line before the body; avoid extra empty paragraphs at the top. Preserve existing keys, values, tags, and aliases, and keep each property name's type consistent across the vault.
- Use properties only for small, maintainable, structured metadata that improves filtering, grouping, or automation. Use stable names, atomic values, lists for multiple values, and quoted wikilinks such as `"[[Note]]"`. Do not put Markdown formatting, long prose, or a second outline in property values. Supported types are text, list, number, checkbox, date, date-time, and tags.
- Store categorisation tags in `tags` as a YAML list without `#` prefixes, for example `tags: [search-eng, system-design]` or a block list. Keep categorisation tags out of body text so they appear consistently in Properties and Bases. Merge and deduplicate with existing tags, keep nested tag paths intact, and never add an empty `tags` property.
- Do not impose a new metadata schema on existing notes or move inline tags into YAML as a side effect of unrelated work.
- During a requested vault-wide tag migration: inspect every ordinary note, including those with frontmatter; move actual inline tags into `tags`; ignore tag-like text in code, math, wikilink heading anchors, and heading syntax; keep a marker tied to a specific unfinished item readable in the body as `TODO:` while also adding `TODO` to `tags`; and skip plugin payloads and application settings.

### Callouts

- A callout is a blockquote that begins with a typed marker, for example `> [!warning] Check the assumption`. Use `note` or `info` for context, `tip` for practical guidance, `warning` for material caveats, `question` for a genuine open question, and `example` for exercises. Types are case-insensitive; `+` or `-` immediately after the type makes the callout foldable (expanded or collapsed).
- Reserve callouts for brief asides: normally one short paragraph with a short, descriptive title. Keep multi-paragraph explanations, worked examples, and comparison tables in the ordinary body under headings.
- Collapse callouts only for optional detail such as a supplementary derivation or exercise solution, never for the only explanation of a core concept. Avoid adjacent or nested callouts used as decoration.
- Reserve blockquotes for quotations and callouts; do not use a plain `>` block as decorative indentation.

### Layout and readability

- Prefer native Markdown that inherits the reader's theme and text size. Fix layout through structure; do not add hard-coded colours, font sizes, HTML layout wrappers, or vault-wide CSS unless requested.
- Use short paragraphs, bullets for parallel points, numbered lists for procedures, and compact tables with short headers for small comparisons. Put interpretation below a table; switch to labelled bullets when cells are long or columns are many.
- Use bold for short labels or key terms, not whole paragraphs. Do not repeat the same example in prose, a table, and a callout.
- Leave blank lines around headings, paragraphs, lists, tables, and display math. A single source-line break may render as a space, so use a paragraph break or list item for visible separation.

### Equations and worked examples

- Keep brief symbol references inline with `$...$`. Put calculations the reader must follow in `$$...$$` display blocks, with the delimiters on their own lines and readable notation such as `\frac{a}{b}`.
- Structure every worked calculation or exercise solution the same way:
  1. List the inputs or symbol definitions.
  2. Give each calculation a short label or step number, followed by its own display block.
  3. Explain what the result means in a separate paragraph.
- Treat different cases or parameter settings as separate steps. Keep a chain of equivalent transformations together only when it is one calculation; do not squeeze independent equations into one sentence or one wide display to save lines.
- Apply this throughout the note: introductions, notation, derivations, comparisons, and foldable solutions. Inside callouts, prefix every line, including blank lines and equation lines, with `>`. Keep code, tables, links, and math syntax intact when changing spacing.
- When fixing one dense example, check every equation-bearing section in the requested scope for the same pattern, and report the exact scope covered.

## Names, renames, and plugin content

- Use stable, generic concept filenames such as `Go Language.md`, `Information Retrieval.md`, or `Cosine Similarity.md`. Put angles such as design principles, worked examples, or performance under headings, not in new files. Avoid sentence-like filenames, redundant subtitles, and one file per question about the same concept.
- Generic does not mean vague: `BM25.md` and `NDCG.md` remain distinct concepts, and a comparison such as `Rust and Go.md` can stay separate from each language's note.
- Obsidian updates links automatically only for renames made inside Obsidian. Before renaming a file or a linked heading from outside it, check name collisions and all inbound wikilinks, embeds, heading and block links, and Markdown file links, including links inside the renamed files. Update the targets while preserving display aliases and fragments, and keep the former name as a frontmatter alias when useful. Never call a rename safe based only on outbound links.
- Do not silently delete or merge stubs, apparent duplicates, or misspelled files. When consolidation is requested, keep unique content and update affected links.
- Never rewrite Excalidraw payloads, compressed drawing data, or plugin-managed sections as prose, and do not apply templates, heading fixes, or reference normalisation to them. If a change affects a drawing, preserve its structure and verify the affected link explicitly.

## Adaptable note template

Use this starting point for substantive concept notes. Omit unnecessary sections and replace placeholder text; short definitions can remain short.

```markdown
## Overview
Explain what the topic is, why it matters, and when it is useful.[^1]

## Key Concepts
- **Concept:** Explain the idea and link to an existing related note where useful.

## Details & Deep Dive
Develop the intuition and mechanics. Define notation and assumptions.

## Worked Example
List the inputs, show each calculation as a separate labelled step with a displayed equation, and put the interpretation in its own paragraph. For a scenario or code example, separate the setup, steps, and outcome in the same way.

## Limitations & Common Pitfalls
Explain important caveats, failure modes, or common misconceptions.

## Related Notes
- [[Existing Note]] — Explain the connection.

## Open Questions
- TODO: Record a specific unresolved question, if any.

## References & Useful Links
[^1]: [Source title](https://example.com) — Describe the supporting material.
```

Adapt the body to the material:

- **Research papers:** Problem, contribution, method, experimental evidence, limitations, and connections. Separate the paper's claims from your assessment; record title, authors, and year when verified.
- **Practical guides:** Purpose, prerequisites, commands or steps, expected outcome, and pitfalls.
- **Interview notes:** Question, reasoning, answer, and follow-up questions. Preserve unanswered exercises as such.
- **Study plans:** Learning goals, sequence, exercises, and completion criteria. Keep resource URLs in the final references section.
- **Comparison notes:** Shared purpose, meaningful differences, tradeoffs, and when to choose each option.

## Before finishing

- Review the diff (for example `git diff -- <file>`) for scope, accidental deletions, and lost context, including local PDFs, images, and embeds.
- Check newly added internal links against actual files and headings; distinguish intentional prospective links from typos. Check affected embeds and anchors.
- Confirm external references are in the final `## References & Useful Links` section and support the associated claims.
- Check Markdown fences, heading hierarchy, tables, math delimiters, callout `>` prefixes, and preserved metadata.
- For layout changes, inspect the affected section in Obsidian reading view at normal note width when available (wrapping, table width, hierarchy, callout size). Otherwise state that the rendered layout remains unverified.
- Summarise the files changed, substantive improvements, and unresolved factual or source-access gaps. Report only checks actually performed, and do not claim the whole vault was reviewed after a targeted edit.

## Obsidian documentation

- [Obsidian Callouts](https://obsidian.md/help/callouts) — Callout syntax, types, titles, and folding.
- [Obsidian Properties](https://obsidian.md/help/properties) — Property types, YAML format, and tag and alias properties.
