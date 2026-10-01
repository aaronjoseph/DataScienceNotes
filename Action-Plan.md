---
note_type: career_plan
role_target: Senior / Staff Machine Learning Engineer
market_scope: India and remote India
reviewed: 2026-10-01
tags:
  - career
  - ai-engineering
---

# Senior and Staff ML Engineering Career Plan

## Goal

Target **Senior Machine Learning Engineer** and selectively **Staff Machine Learning Engineer** positions at companies building and operating their own products. Prioritise search, relevance, ranking, recommendations, and ML infrastructure where they match your experience. Use [[Search Engineering]], [[Learning to Rank]], and [[System_Design/Design a Personalized Search Recommendation System for Rapido|search system design]] as the technical foundation.

Use the next 12 weeks to assemble convincing evidence of product impact, modelling judgment, experimentation, reliable production systems, and technical leadership. Apply as soon as the relevant evidence is ready. Completing all 104 study cards is not an application prerequisite, and a portfolio alone cannot demonstrate sustained Staff-level organisational impact.

> [!note] Personal evidence still needs an audit
> The vault suggests a strong search and production-engineering focus. Your years of experience, independently owned launches, measured outcomes, and cross-team influence have not been established here. Treat Senior as the primary preparation track and Staff as a selective track to validate against your actual work, not an automatic level assessment.

## Product-company role review

**Reviewed 1 October 2026:** six publicly accessible LinkedIn descriptions from product employers, selected for relevance to ML engineering. Five are India listings; one US listing is a skills benchmark. This replaces the earlier Cognizant/Luxoft examples as the basis for the plan. It is a targeted sample, not a representative hiring-market survey.

### Roles and requirements observed

| Employer and advertised role | Location | Experience stated |
|---|---|---|
| Apple — Senior ML Engineer / Senior Applied Scientist, Search & AI[^apple] | Bengaluru | 8+ years |
| Bloomreach — Staff ML Engineer, Search Quality team[^bloomreach] | India | 8+ years |
| Intuit — Staff ML Engineer, Network Intelligence Science[^intuit] | Bengaluru | 7+ years |
| project44 — Staff ML Engineer[^project44] | Bengaluru | 8–10+ years |
| Adobe — Senior ML Engineer 5[^adobe] | Bengaluru East | 9+ years |
| Atlassian — Senior ML Engineer, Search & Intelligence[^atlassian] | San Francisco, US | 5+ years |

The experience figures belong to these specific descriptions, not a universal Senior/Staff ladder. Location comes from the role itself, not LinkedIn's surrounding search page. The details below are paraphrases of the postings; fit and study priorities are this plan's interpretation.

- **Apple — close domain match:** query understanding, retrieval/ranking, ML model development, and component/end-to-end evaluation. The description includes fine-tuning and reinforcement learning; RAG appears among preferred qualifications. Prepare to explain model choices and experimental results as well as serving architecture.[^apple]
- **Bloomreach — close Staff benchmark:** search relevance across queries, catalogues, and user behaviour; production Python/backend engineering; scalable low-latency systems; evaluation frameworks; roadmap ownership and mentoring. Its search role combines ML and LLM approaches with quality, latency, and cost trade-offs.[^bloomreach]
- **Intuit — leadership benchmark with a distinct specialism:** production ownership across data, training, evaluation, and serving; shared infrastructure, data contracts, rollback, and standards adopted by others. This particular team also requires forecasting, optimisation/control, and related decision-making expertise. Do not generalise that specialism to every Staff ML role.[^intuit]
- **project44 — product and platform ownership:** predictive ML for logistics alongside GenAI, reusable feature/experimentation/deployment capabilities, messy-data diagnosis, and business-linked evaluation. The posting explicitly requires three office days weekly; it is not a remote-India lead.[^project44]
- **Adobe — research-heavy exception:** novel models and learning methods for agentic intelligence, rigorous experimentation, and publications or impactful original research. It asks for an MS/PhD and 9+ years. A tool-orchestration demo is insufficient preparation for this particular role; pursue it only if your research evidence fits.[^adobe]
- **Atlassian — Senior scope benchmark:** complete ML lifecycle ownership, Python/SQL, scalable data processing, offline/online experiments, architecture, product collaboration, and mentoring. Its description also values influence beyond the immediate team. The US listing does not establish India eligibility, despite the company's flexible-work language.[^atlassian]

**Access and freshness:** these six descriptions were opened and read. LinkedIn pages may be cached, reposted, or later closed; their relative posting ages and applicant counts are not used as evidence of availability. Some additional search results redirected or could not be opened and were excluded from this comparison. Before applying, verify the exact requisition on the employer's careers site, current requirements, location, work authorisation, and office expectations. No remote-India vacancy is confirmed by this review.

### What changes in this plan

The recurring signal in the engineering-oriented roles is ownership from product problem through data, models, evaluation, and production. The Staff examples add shared capabilities and technical direction; Senior roles can also require mentoring and architectural influence.[^bloomreach][^intuit][^project44][^atlassian]

**Planning decision:** prioritise ML fundamentals, data quality, learning to rank, experimental reasoning, Python/SQL, and production reliability. Keep generative AI as a role-dependent extension. For postings that explicitly require shipped LLM systems, record that as a real gap; an optional learning module does not make the requirement optional. Do not pursue every framework or specialised research area mentioned by one employer.

## Target role and positioning

### Best-fit role families

- **Primary:** Senior ML Engineer in Search/Relevance, Ranking, Recommendations, Personalisation, or Applied ML.
- **Selective Staff:** Staff ML Engineer / Staff Software Engineer, ML, where you can substantiate technical direction, multi-team delivery, shared infrastructure, and outcomes sustained beyond one launch.
- **Adjacent:** ML Platform, Inference, or Applied AI roles when their modelling/serving expectations match your evidence. Check GPU, distributed-training, or LLM-production requirements individually.
- **Separate research track:** research scientist and research-heavy engineering roles requiring original methods and research output. The Adobe example illustrates why the title alone is insufficient.

### Senior versus Staff: evidence to prepare

This is a working preparation rubric inferred from the reviewed descriptions, not an official company levelling framework. Calibrate it with each employer.

| Dimension | Senior evidence | Additional Staff evidence |
|---|---|---|
| Ownership | Take an ambiguous product feature through launch and operation | Set direction across connected systems or teams |
| ML judgment | Choose labels, models, metrics, and defensible experiments | Establish reusable evaluation and modelling standards |
| Systems | Explain scale, quality, latency, cost, failures, and rollback | Resolve shared architectural constraints and migration trade-offs |
| Product impact | Connect a measured result to a user or business outcome | Prioritise investments and demonstrate impact across initiatives |
| Leadership | Partner with product/data teams; mentor engineers | Gain adoption, align stakeholders, and raise others' effectiveness |

For example, improving a ranking service is useful Senior evidence when you can explain your decisions and measured results. Staff evidence might additionally show that multiple teams adopted an evaluation or serving approach you led, why they agreed, and how you measured its ongoing benefit. These are illustrative examples, not claims about your work.

### Evidence audit and career narrative

Mark each area **demonstrated**, **needs practice**, or **missing**, with an actual project/story reference. All remain **TODO: unassessed** until that evidence is supplied.

- **Product:** problem, affected users, baseline, success metric, guardrails, and measured outcome.
- **Models and data:** labels/features, leakage prevention, baselines, model choice, ablations, and failure slices.
- **Experiments:** offline evaluation, uncertainty, online-test design or execution, and the decision supported.
- **Production:** serving/data architecture, performance, costs, incident response, rollout, and rollback.
- **Leadership:** your decisions, stakeholder disagreements, mentoring, adoption, and sustained results.

Use a truthful version of: “I build and improve production search and ML systems, connecting retrieval and ranking quality to product outcomes and reliable serving.” Add a Staff positioning statement only when supported by examples of technical direction and adoption across teams. Keep production achievements, prototype results, and proposed designs clearly distinguished; do not invent metrics or claim shipped LLM experience.

## Start here: the study board

Open [[Job Interviews/Interview Study Board|Interview Study Board]] for daily execution. It contains **104 study cards**: NeetCode’s Blind 75 and all **29 chapters** from Alex Xu’s *System Design Interview*, Volumes 1 and 2. This note holds the career strategy, workflow, and evidence milestones; the board holds each study item’s current status.

**First session:** the proposed starting queue contains Contains Duplicate, Valid Anagram, Two Sum, and Volume 1 Chapter 1. These are planned tasks, not recorded accomplishments. No previous completion history has been inferred.

### Can Obsidian work like sticky notes?

Yes. There are three relevant options, checked on **1 October 2026**:

| Option | Best use | This vault |
|---|---|---|
| Existing Kanban plugin | Task cards moved through status columns | Enabled; version 2.0.51. Use now. |
| Canvas | Freely positioned cards, groups, and connecting lines | Core plugin currently disabled. Optional for visual planning. |
| Bases Kanban | Note files grouped by a status property | Requires Obsidian 1.14+; running app is 1.13.7. Revisit later. |

**Kanban** provides the structured card wall needed here and stores its board in Markdown.[^kanban] **Canvas** is closer to an unrestricted sticky-note whiteboard: text cards can exist without separate note files, and notes can be arranged spatially.[^canvas] **Bases Kanban** supports moving note cards between groups by updating a property; it is a future option if each task needs its own detailed note and table view.[^bases]

The existing [[MLE Study Prep]] and [[Job Interviews/Preparation|Preparation]] are Kanban boards. [[Action Plan.base|Action Plan base]] is different: its current filter lists `search-eng` notes, and its views organise search metadata. It does not track this study backlog. Keep it as the search-note catalogue.

**Decision:** use the already-enabled Kanban plugin. Keep the new board separate from the long action plan, so prose headings do not become board columns. A Markdown comparison table is not a draggable board. No new plugin, application upgrade, or settings change is needed for this setup. The plugin’s repository currently requests maintainers; keep the Markdown board portable and reassess Bases when an upgrade is otherwise useful.[^kanban]

### Board columns and movement

The daily columns come first; the two large backlogs sit to their right.

| Column | Meaning | Rule |
|---|---|---|
| This Week | Small queue selected from either backlog | Start with 3 coding problems and 1 chapter. |
| In Progress | Work being actively attempted | At most 2 cards total. |
| Review | First attempt finished; recall or explanation still needs checking | Add a review date and the specific gap. |
| Done | Completion criteria below demonstrated | Keep cards visible for progress counts. |
| Coding Backlog | Remaining Blind 75 problems | Ordered by pattern; difficulty stays on the card. |
| System Design Backlog | Remaining chapters from both books | Volume and chapter identify every card. |

Move the **same card**, rather than copying it: backlog → This Week → In Progress → Review → Done. If a later check fails, move it back to Review. Checkbox state is not the progress measure; column placement is. Do not archive completed cards while using board counts as the dashboard.

For example, after attempting **LC 1 — Two Sum**, record whether a hint was needed and why a hash map helps. Move it to Review, add a date for a fresh attempt, and only move it to Done once you can solve and explain it without the solution open. Review dates are a manual convention, not scheduled reminders.

For blockers, keep the card in its current column and add `Blocked: ...; next action: ...`. At the weekly review, return unstarted overflow to its original backlog. Do not keep accumulating commitments.

### Card detail and completion criteria

Keep the visible card short: identifier, topic, difficulty where applicable, and a useful note link. Add `Last attempt: YYYY-MM-DD; review: YYYY-MM-DD; gap: ...` after an attempt. Create or link a substantive solution note only when there is something to preserve; do not create 104 empty notes.

- **Coding — Review:** make a serious attempt, inspect the explanation if needed, and identify the missed idea. **Done:** solve again independently, explain the invariant or recurrence, justify time/space complexity, and check relevant edge cases. An accepted submission after copying a solution is not enough.
- **System-design case study — Review:** read, draw the main flow, and record uncertainties. **Done:** explain requirements, scale assumptions, API/data model, bottleneck, at least two trade-offs, and a failure/recovery path from a blank page. Keep a diagram or concise summary as evidence.
- **Foundational or closing chapter — Done:** produce the appropriate output instead of forcing a case-study template: a capacity estimate, an interview outline, or a next-learning list. Volume 1 Chapters 1–3 and 16 use this criterion.

These are proposed learning checks, not claims that a fixed number of solved questions guarantees interview readiness.

## Coding track: Blind 75

“NeetCode 75” is interpreted here as **Blind 75 on NeetCode**, not NeetCode 150 or LeetCode 75, which are different lists.[^blind75] The board includes all 75 entries selected by the `blind75` flag in NeetCode’s public problem data, checked on 1 October 2026.[^problem-data]

Each card links to its entry in [[Job Interviews/Coding Practice Index|Coding Practice Index]], where the original problem URL is kept. This index is a launch list, not another completion tracker. Names, identifiers, patterns, and difficulty labels come from the source snapshot; URLs were taken from its slugs, but individual problem pages and account access were not all checked.

Study by pattern: arrays/hashing → pointers/windows → stack/binary search → linked lists/trees → tries/heaps/backtracking/graphs → dynamic programming → greedy/intervals/matrices/bits. This is a suggested sequence; move a prerequisite forward when a problem exposes a gap. Use [[Big O]] for complexity and [[LeetCode/Binary Search/Binary Search|Binary Search]] for the existing binary-search foundation.

Keep separate evidence for first attempts and independent re-solves. Work on the same pattern across a few problems, then mix older patterns into review so the category name does not become a hint. Use NeetCode’s practice list for available explanations and practice options if the linked platform does not expose a problem to your account.

## System-design track: both Alex Xu volumes

Scope is **the books**, using Alex Xu’s published chapter lists: **Volume 1 Chapters 1–16** and **Volume 2 Chapters 1–13**.[^xu] All 29 appear on the board, including the foundational and closing chapters. Board labels are shortened topic descriptions; volume/chapter numbers preserve the mapping. The evolving online course may use different numbering or include additional material.

Start with Volume 1 Chapters 1–3. Continue in book order by default, using earlier concepts in each new design. Later, prioritise review of retrieval, storage, messaging, and monitoring designs when target interviews emphasise them; prioritisation does not remove the other chapters from the backlog.

Reuse these existing notes where they fit; they are supporting material, not substitutes for every book chapter:

- [[System Design]] and [[Primitives - System Design]] — requirements and reusable components.
- [[Horizontal & Vertical Scaling]] and [[Database Sharding]] — scaling and partitioning discussions.
- [[System_Design/File Storage System|File Storage System]] — Google Drive and object-storage practice.
- [[System_Design/Accommodation Booking System|Accommodation Booking System]] — hotel-reservation practice.
- [[Monitoring - MLOPS]] — monitoring connections, with ML-specific scope kept explicit.
- [[System_Design/Design a Personalized Search Recommendation System for Rapido|Rapido search design]] — an additional application of retrieval and ranking decisions.

## Time budget and milestones

The original portfolio plan assumed **6–8 hours per week**. Adding 75 coding questions, re-solves, and 29 chapters does not fit into that allowance automatically. These are planning scenarios to recalibrate after two weeks, not measured completion estimates:

| Weekly capacity | Suggested allocation | Expected planning approach |
|---|---|---|
| 6–8 hours total | 2–3 coding; 1–2 design; 2 project/evidence; 1 career/review | Extend the portfolio phases beyond 12 weeks. |
| 12–15 hours total | 4 coding; 3 design; 4–6 project/evidence; 1–2 career/review | Use week 12 as a portfolio checkpoint; study can continue. |

Start with **3 new coding problems and 1 chapter per week**, plus review. At that unchanged pace, first-pass coverage alone takes 25 weeks for coding and 29 for the books. Reviews, difficult chapters, and missed weeks can extend that; faster prior familiarity can shorten it. Do not add dates to every card before measuring your pace.

After two weeks, record actual session time, independent re-solves, and chapters you can explain. Then choose whether to increase weekly time, reduce portfolio scope, or extend the horizon. Do not silently drop review to preserve a deadline.

### Setup and first two weeks

1. Open [[Job Interviews/Interview Study Board|Interview Study Board]] in Obsidian. The board frontmatter selects the existing plugin. If it opens as text, use the note’s menu to open it as Kanban.
2. Start with the four cards in This Week. Move one into In Progress when beginning, then into Review after the first pass.
3. Follow a coding card into the index to launch its problem. Read design chapters in your own book or authorised course access; this setup imports a study inventory, not book content or solutions.
4. Record attempt notes and choose review dates. Add evidence links as you produce useful solutions or diagrams.
5. At the end of week one, review the queue and select the next small batch. At the end of week two, recalibrate the time budget.

**Setup acceptance:** 75 unique coding cards, 16 Volume 1 cards, 13 Volume 2 cards, no inferred completions, and one status location per study item. The board tracks progress locally; it does not sync completion with NeetCode, LeetCode, or ByteByteGo.

## Twelve-week roadmap

Use six two-week phases as a sequence for closing gaps and packaging evidence. The 12-week target depends on the time budget above; extend it at 6–8 hours total per week. Keep the coding and Alex Xu tracks running alongside it. Prefer a strong, permitted account of existing production work over rebuilding something solely for a portfolio. Use public data for a separate reproducible project when needed.

### Weeks 1–2: Select roles and audit your evidence

- Expand the reviewed sample into 15–20 relevant descriptions, prioritising India eligibility and direct product ownership. Separate must-haves, preferences, specialised requirements, and level scope.
- Complete the evidence audit. Select the two largest gaps that recur in roles you would actually accept.
- Draft a role-specific resume and 3–5 real stories: model/product decision, production incident, evaluation result, collaboration, and a difficult trade-off. For Staff, include an initiative adopted across teams.
- Choose one bounded project or case study with a user, measurable objective, data source, baseline, and scope limit. Default to **search quality and learning to rank**; add a grounded assistant only when target roles justify it.

**Deliverable:** role shortlist, evidence scorecard, resume draft, story inventory, and a one-page project brief. **Gate:** every achievement is attributable to your work; unknown results remain unknown.

### Weeks 3–4: Build the data and modelling foundation

- Define query/item or query/document data, relevance labels, missing-judgment handling, and a train/validation/test split appropriate to the task. Check leakage across queries, users, and time where applicable. See [[Feature Engineering]], [[Learning to Rank]], and [[Click Bias]].
- Establish lexical and dense baselines, then test hybrid candidates and one justified reranker or learned ranking model. Use [[BM25]], [[Dense Retrieval]], [[Hybrid Retrieval]], and [[Cross-Encoder]]. Avoid adding model complexity without a baseline comparison.
- Make feature extraction, training where applicable, indexing, and evaluation reproducible. Record data/model/configuration versions in [[Experiment Tracking]]. Explain the loss, regularisation, and optimisation choices for any trained model.
- Practise SQL joins, windows, aggregations, and dataset-quality debugging alongside the project. Do not substitute algorithm questions for data work.

**Deliverable:** reproducible dataset path, baseline comparison, one model/feature ablation, and an error analysis. **Gate:** a reviewer can reproduce the comparison and explain why the split, labels, and model are appropriate.

### Weeks 5–6: Connect evaluation to product decisions

- Measure candidate coverage and ranking separately, using suitable Recall@k, MRR, or nDCG@k definitions and a stated evaluation unit. Compare the same held-out cases; inspect head/tail queries, new items, and other meaningful slices. See [[Search Evaluation]].
- Specify a user-facing objective and guardrails such as latency, errors, or harmful relevance regressions. Explain why offline improvement might not translate into the chosen product outcome. Use [[Product Metrics]].
- Design an A/B experiment: hypothesis, randomisation unit, primary metric, guardrails, sample-size/duration assumptions, uncertainty, and decision rule. Practise diagnosing selection bias, novelty effects, and mismatches between logged and intended exposure. See [[AB Testing]].
- If real traffic is unavailable, deliver an experiment proposal and label simulations as simulations. Do not report an offline metric increase as observed revenue, conversion, or user benefit.

**Deliverable:** evaluation report, versioned regression cases, failure slices, and experiment design. **Gate:** explain what improved, what regressed, how certain you are, and which product claim remains untested.

### Weeks 7–8: Operate the ML system reliably

- Expose a typed Python API, for example FastAPI, with validation, timeouts, bounded retries, and clear errors. Provide a container and repeatable local execution; deploy to a relevant cloud only when it adds useful evidence. Where your existing GCP experience fits, a small Cloud Run deployment can keep the scope manageable.
- Document training/serving consistency, feature freshness, data contracts, model/index versions, and retraining triggers. Link to [[ML Pipelines]] and [[Data Drift]] where helpful.
- Measure p50/p95 latency, throughput, errors, and resource or inference cost under a stated workload. Include concurrency and warm-up assumptions; track each retrieval/ranking stage with structured logs and traces.
- Demonstrate a safe rollout and rollback procedure, degraded behaviour, and incident diagnosis. Practise [[Shadow Deployment]] or [[Canary Deployment]] as appropriate. Test API contracts, data validation, and important failure paths.

**Deliverable:** runnable service, architecture diagram, workload report, runbook, and failure drill. **Gate:** explain the observed bottleneck and show what happens when a model, feature source, or downstream dependency fails.

### Weeks 9–10: Demonstrate technical leadership

- **Senior track:** write a concise design decision comparing plausible approaches, the selected trade-offs, a staged delivery plan, and how success will be measured. Present an actual collaboration or mentoring example separately from the portfolio.
- **Staff track:** prepare a real cross-team case study covering the original disagreement or systemic constraint, stakeholders, alternatives, alignment, adoption, migration, and sustained outcomes. Include what you changed after feedback.
- For a portfolio, propose one reusable capability—evaluation harness, feature contract, or rollout mechanism—and demonstrate it in a second small use case if useful. Mark adoption as hypothetical unless others actually used it; an RFC by itself is not organisational impact.
- Practise a short technical proposal and a product-facing explanation of investment versus benefit. Seek reviewer feedback; no automatic outreach is part of this plan.

**Deliverable:** design/RFC, leadership story, and critique log. **Gate:** distinguish your contribution from the team's work and demonstrate influence through evidence, not title or diagram size.

### Weeks 11–12: Interview and refine applications

- Package the case study/project into a brief walkthrough: problem, data, model, experiment, architecture, launch/operations, measured results, and limitations. Include a short demo with a success and failure case where applicable.
- Practise five areas: coding/debugging, SQL/data reasoning, ML/statistics, ML system design, and behavioural/product leadership. Use mock feedback to set the next study queue; these are preparation areas, not a verified interview loop for every employer.
- Extend one Alex Xu design into an ML system discussion: labels/features, training, retrieval/ranking, offline/online evaluation, freshness, feedback, monitoring, and rollback. The books cover general system design and do not replace this ML-specific practice.
- Tailor the resume and stories to each role. Continue a manageable application cadence while interviewing and revising evidence.

**Deliverable:** evidence packet, role-specific resume/profile, and interview-gap log. **Gate:** explain the model and product reasoning as clearly as the infrastructure, including uncertain findings and the next experiment.

## Ongoing weekly cadence

- **Study:** pull a small batch into This Week; attempt independently and revisit Review before adding work.
- **Build evidence:** use the allocated project time for modelling, evaluation, or a concrete case-study gap. Avoid collecting tutorials without an output.
- **Evaluate:** inspect failures and keep a regression set; review results beyond a successful demo query.
- **Apply:** make a few carefully matched applications once the resume is ready, without waiting for all study cards.
- **Get feedback:** seek a useful technical critique or career conversation when possible.
- **Review:** record time spent, evidence produced, interview feedback, and next week's two most important gaps.

## Skill priorities

| Priority | Evidence area | Useful output |
|---|---|---|
| 1 | ML/statistics and modelling judgment | Baseline, loss/model explanation, ablation, error slices |
| 2 | Data, features, and Python/SQL | Reproducible dataset, leakage checks, reliable pipeline |
| 3 | Product measurement and experimentation | Offline report, business objective, defensible A/B design |
| 4 | ML systems and operations | Tested service, workload report, monitoring and rollback |
| 5 | Communication and leadership | Decision memo, collaboration story, demonstrated adoption |
| Role-dependent | LLMs, RAG, agents, specialised modelling | Evidence matching the actual posting |

Leadership is a parallel priority throughout the plan and central to Staff applications; row order is not a reason to postpone it. Use one relevant modelling stack deeply enough to train, debug, evaluate, and serve. Frameworks, clouds, and orchestration libraries are choices, not a universal checklist. Keep [[Probability Calibration]] and other foundations in the revision loop when a model or target role needs them.

## Application strategy

### Search for these titles

- Senior Machine Learning Engineer — Search, Ranking, Recommendations, Personalisation, Applied ML.
- Staff Machine Learning Engineer / Staff Software Engineer, Machine Learning — evaluate actual scope.
- Senior Search Relevance Engineer / ML Engineer, Retrieval — check whether the title matches the required level.
- Senior/Staff ML Platform or Inference Engineer — when the systems and model-serving requirements fit.
- Applied AI / Generative AI Engineer — selectively, with explicit production-ML ownership and appropriate seniority.

Run separate Senior and Staff searches on LinkedIn with India and suitable city filters. A useful starting query is `("machine learning" OR "search relevance") AND (senior OR staff)`; refine with ranking, recommendations, or ML platform. Treat title synonyms as discovery aids and inspect the actual description.

### Screen for product-company fit

1. **Employer and product:** confirm direct employment with a company operating its own product or platform, and identify the team/product. Exclude consulting delivery, client-staffing, and service-provider placements from this target list. An agency repost or company brand alone does not establish the employing entity.
2. **Ownership:** look for ongoing roadmap, data/model decisions, customer or business metrics, deployment, experimentation, and operation after launch. Check whether the job is actually implementation support or a customer-specific delivery engagement.
3. **Level and specialism:** compare the must-have experience, modelling depth, and leadership scope with your evidence. Staff years alone are insufficient; research-heavy and optimisation-heavy roles need their own assessment.
4. **Location and work model:** confirm India eligibility, office cadence, time zones, and work authorisation. “Remote” or “virtual first” does not mean hire-from-anywhere.
5. **Current requisition:** use the employer's careers site or recruiter to verify status before tailoring. Record the check date; keep expired descriptions only as labelled preparation references.

Start the domain-fit shortlist with Apple search and Bloomreach search, then assess other product ML teams individually. Intuit/project44 provide useful ownership benchmarks but have additional domain demands. Atlassian's reviewed US role is a benchmark only; Adobe's reviewed role belongs to the research track. These are preparation priorities, not confirmed eligibility or recommendations to apply to every listed job.

For each candidate role, record: employer/team, title and requisition ID, source and verification date, location/work model, must-haves versus preferences, your evidence and gaps, contact/referral if any, application stage, and next action. Keep any saved external URLs in this note's references section if recording them here. No application or message has been sent as part of this review.

## Progress dashboard

Update this table once a week. Count study items from board columns, not from a second checklist. **Attempted/read** counts unique items that have had a first pass, wherever they now sit. **Done** counts items currently meeting the completion criteria; it can decrease after a failed review. Session/review counts are activity, not additional unique completions.

| Week ending | Coding attempted /75 | Coding Done /75 | Chapters read /29 | Chapters Done /29 | Next adjustment |
|---|---|---|---|---|---|
|  |  |  |  |  |  |

Record project, leadership, and career outcomes separately so reading progress is not mistaken for shipped engineering evidence.

| Week ending | Model/product/leadership evidence | Applications | Conversations/referrals | Interview feedback |
|---|---|---|---|---|
|  |  |  |  |  |

## Optional project extension

### Role-dependent RAG and LLM track

Retain the original **search-grounded assistant over a bounded document collection** when it addresses a target-role gap. Use public product documentation, policies, or technical guides. Follow [[Retrieval-Augmented Generation]]: reproducible ingestion, parsing/chunking, metadata, re-indexing, and a manually reviewed query/passage set. Reuse the core lexical/dense/hybrid comparison before adding generation.

Substitute this work for a lower-priority gap, or extend the schedule; do not silently add another project to the same time budget. For roles requiring LLM experience, include model/prompt versions, provider failure handling, token/cost accounting, latency, and sensitive-data handling. Use [[Decoder-Only Model (Transformers)#Serving and the KV Cache|prefill, decoding, and the KV cache]] to explain generation-serving trade-offs.

### Grounded generation and evaluation

- Generate answers from retrieved evidence, with citations that point to source documents or chunks.
- Define answer-level checks: answer relevance, faithfulness to retrieved evidence, citation correctness, refusal behavior, and “not enough evidence” handling. See [[LLM Evaluation]] for metric definitions.
- Build a versioned evaluation set with representative, ambiguous, unanswerable, and adversarial queries.
- Compare at least two model/configuration choices if access and budget permit. Record model/version, prompt, retrieval settings, and date so results can be reproduced.
- Keep model-graded metrics as a diagnostic signal; inspect a sample manually and report the judging method and its limitations.

**Deliverables**

- An evaluation command that produces retrieval and answer-quality results separately.
- A small regression set that runs whenever retrieval, prompt, or model settings change.
- A failure report with examples of unsupported answers, missed evidence, bad citations, and appropriate abstentions.

**Quality check:** You can show what improved, on which cases, and what regressed. “The answers look good” is not an evaluation result.

### One bounded tool workflow

- Add one deterministic tool that improves the chosen use case, such as a metadata filter, calculator, or lookup API. Use a bounded workflow with explicit tool schemas and validation; see [[Tool Calling]].
- Define when the system may call the tool, what inputs it accepts, and what happens on failure. Do not add [[Multi-Agent Systems|multi-agent orchestration]] unless the problem genuinely needs multiple independent roles.
- Test prompt injection in user input and retrieved documents, unauthorized tool requests, malformed tool outputs, and attempts to expose secrets. See [[Prompt Injection]].
- Add a simple policy for citations, abstention, and escalation to a human or a safe fallback.
- Document known limitations and data handling. Keep credentials out of the repository and avoid collecting unnecessary user data.

**Deliverables**

- A short architecture decision note that explains why the tool workflow is appropriate and what simpler alternative you considered.
- An adversarial test set and a visible summary of pass/fail outcomes.

**Quality check:** The tool can only perform its declared operation, and the system behaves safely when evidence or tools are unavailable.

### Further stretch work

- Compare query rewriting or an additional reranker on the same held-out cases.
- Compare a hosted model with a smaller/local model only with a fair quality, latency, and cost workload.
- Add asynchronous ingestion or a queue if the use case needs it.
- Learn [[Tool Calling#Model Context Protocol (MCP)|Model Context Protocol (MCP)]] when the workflow or target role needs standardised tool/context integration.
- Study fine-tuning, [[Multi-Agent Systems|multi-agent systems]], Kubernetes, or distributed training when the selected roles require them. Do not infer that assembling a RAG application demonstrates original ML research.

## Study Notes for This Plan

Revise notes in response to the evidence audit and interview feedback. Start with the core ML/product topics, then use the LLM material for relevant roles.

- **ML, data, and product:** [[Learning to Rank]], [[Feature Engineering]], [[Evaluation Metrics]], [[Search Evaluation]], [[Probability Calibration]], [[AB Testing]], and [[Product Metrics]].
- **ML delivery:** [[ML Pipelines]], [[Experiment Tracking]], [[Data Drift]], [[Canary Deployment]], and [[Shadow Deployment]].
- **Model foundations:** [[Transformers]] → [[Encoder-Only Model (Transformers)|encoder-only]], [[Decoder-Only Model (Transformers)|decoder-only]], and [[Encoder-Decoder Model (Transformers)|encoder–decoder]] models → [[BERT]] and [[RoBERTa]] → [[Language Model|language models]]. Supporting pieces: [[Tokenization#Subword Tokenizers for Transformers|subword tokenizers]], [[Layer Normalization]], and [[Softmax Function|softmax]].
- **Retrieval for RAG:** [[Retrieval-Augmented Generation]], [[Hybrid Retrieval]], [[Dense Retrieval]], [[Cross-Encoder]], and [[Search Evaluation]].
- **Quality and safety:** [[LLM Evaluation]], [[Prompt Injection]], and [[Tool Calling]].
- **Serving:** [[Decoder-Only Model (Transformers)#Serving and the KV Cache|KV caching]], [[Latency vs Throughput]], and [[Tail Latency]].
- **Reading list:** [[Transformer Papers]].

## References & Useful Links

Job descriptions below were opened and read on **1 October 2026**. Titles identify the role text reviewed; availability, repost dates, and India-remote eligibility were not independently confirmed with the employers.

[^apple]: [Apple — Senior ML Engineer / Senior Applied Scientist, Search & AI](https://in.linkedin.com/jobs/view/senior-machine-learning-engineer-senior-applied-scientist-search-ai-at-apple-4434323124) — LinkedIn description, Bengaluru; search modelling, evaluation, and production depth. Apple role number 200670460-0321.
[^bloomreach]: [Bloomreach — Staff Machine Learning Engineer](https://in.linkedin.com/jobs/view/staff-machine-learning-engineer-at-bloomreach-4472060414) — LinkedIn description, India, Search Quality; relevance engineering, roadmap, evaluation, and production systems.
[^intuit]: [Intuit — Staff Machine Learning Engineer](https://in.linkedin.com/jobs/view/staff-machine-learning-engineer-at-intuit-4456204545) — LinkedIn description, Bengaluru, Network Intelligence Science; cross-system leadership, shared ML infrastructure, and optimisation specialism.
[^project44]: [project44 — Staff Machine Learning Engineer](https://in.linkedin.com/jobs/view/staff-machine-learning-engineer-at-project44-4428256823) — LinkedIn description, Bengaluru; predictive ML, reusable platform capabilities, GenAI, product outcomes, and office requirement.
[^adobe]: [Adobe — Senior Machine Learning Engineer 5](https://in.linkedin.com/jobs/view/senior-machine-learning-engineer-5-at-adobe-4452715684) — LinkedIn description, Bengaluru East; research-intensive agentic intelligence role and research qualifications.
[^atlassian]: [Atlassian — Senior Machine Learning Engineer, Search & Intelligence](https://www.linkedin.com/jobs/view/senior-machine-learning-engineer-search-intelligence-at-atlassian-4467433923) — LinkedIn description, San Francisco; full ML lifecycle and Senior technical leadership. US benchmark, not a verified India vacancy.

[^kanban]: [Obsidian Kanban — repository and README](https://github.com/community-archive/obsidian-kanban) — Markdown-backed board format and maintainer status; checked 1 October 2026. Local plugin enablement/version and existing boards were inspected separately.
[^canvas]: [Obsidian Help — Canvas](https://obsidian.md/help/plugins/canvas) — Freeform text/file cards, grouping, and connections; checked 1 October 2026.
[^bases]: [Obsidian Help — Kanban view for Bases](https://obsidian.md/help/bases/views/kanban) — Property-based columns and the Obsidian 1.14+ requirement, currently documented as early access; checked 1 October 2026.
[^blind75]: [NeetCode — Blind 75](https://neetcode.io/practice/practice/blind75) — The 75-problem practice list and category totals; checked 1 October 2026.
[^problem-data]: [NeetCode — public problem data](https://github.com/neetcode-gh/leetcode/blob/main/.problemSiteData.json) — Source for the 75 `blind75` entries, problem identifiers, categories, difficulty labels, and URL slugs; checked 1 October 2026. The study index includes source attribution and its MIT notice.
[^xu]: [Alex Xu — System Design Interview Books: Volume 1 vs Volume 2](https://blog.bytebytego.com/p/system-design-interview-books-volume) — Author’s 15 April 2022 chapter inventory, checked 1 October 2026: 16 chapters in Volume 1 and 13 in Volume 2. Chapter contents were not re-reviewed for this board setup.
