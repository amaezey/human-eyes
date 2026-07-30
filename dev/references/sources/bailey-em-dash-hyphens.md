# Jonathan Bailey: Em Dashes, Hyphens and Spotting AI Writing

## Metadata

- **URL:** https://www.plagiarismtoday.com/2025/06/26/em-dashes-hyphens-and-spotting-ai-writing/
- **Author / owner:** Jonathan Bailey
- **Published:** 2025-06-26
- **Retrieved:** 2026-05-05
- **Extracted:** 2026-05-05
- **Contract updated:** 2026-07-15; the preserved extraction was brought into the source-ingest contract without a fresh article scrape
- **Source type:** practitioner journalism and plagiarism commentary
- **Evidence tier:** Practitioner / teacher / editor essays
- **Review mode:** update
- **Stable identifier:** none found
- **Version / revision:** article as published 2025-06-26 and captured 2026-05-05; previous record was the same preserved article body before source-ingest contract framing
- **Full-text status:** complete
- **Snapshot:** `snapshots/bailey-em-dash-hyphens.md`
- **Extraction method:** preserved Jina Reader URL-to-Markdown extraction; no fresh scrape
- **Snapshot SHA-256:** `60125940ad10b7fc73e9dc51f1fb1fe1aa13dd6cebe7016ee34aabafcf17b5e8`
- **Model / corpus scope:** one output from each of six free or basic services, named ChatGPT, Microsoft Copilot, DeepSeek, Claude, Gemini, and Meta.ai, generated before the article's 2025-06-26 publication from one English journalism prompt about the H3H3 lawsuit; reported lengths range from 261 to 948 words; exact model versions, dates, settings, sessions, temperatures, repetitions, and human comparison texts are not supplied
- **Access limitations:** none for the preserved article body; the linked Google Doc containing the six raw generated articles was not preserved or reviewed, the generic hero image was not saved, and the article supplies no model build identifiers, repeated trials, human comparison corpus, annotation protocol, statistical test, or reproducible record of the factual-error verification

## Summary

Bailey reports a one-prompt, six-service spot check of em-dash use, then uses the sharply different output counts to reject em dashes as a standalone authorship shortcut. The article's strongest contribution is its own limitation case: three services reportedly used eight or nine em dashes, one used two, and two used none; humans also use the punctuation deliberately; the glyph is easy to replace; and the model-specific pattern can drift. Bailey found concrete factual mistakes more useful than punctuation, but the linked raw outputs were not preserved, so the counts and error examples remain author-reported practitioner observations rather than independently reproducible evidence. The article supports a deeper-review cue and product restraint, not a threshold, hard failure, generic model claim, or authorship verdict.

## Main insights

- The six reported outputs vary from zero to nine em dashes despite one shared prompt, directly challenging a generic claim that every AI-generated text contains them.
- Bailey explicitly says the sample is far too small for statistical significance, reports no human comparison, and names only free or basic product surfaces rather than model versions.
- Bailey says Claude's two em-dash glyphs occurred in one highlighted section, but that clustering detail remains author-reported and cannot be checked without the linked raw output.
- Human writers use em and en dashes, sometimes as a long-standing personal style; Bailey therefore rejects the absence or presence of one glyph as proof.
- Replacing em dashes with hyphens is trivial, while services and users can adapt, so a public surface cue can decay quickly.
- The phrase "ChatGPT hyphen" conflates a hyphen with the em dash under discussion. Bailey's rhetorical questions about hyphens and parentheses do not establish either as an AI pattern.
- Bailey's three factual-error examples point toward source and claim verification, but they are not independently reproducible from the preserved record because the linked model outputs were not captured.
- Bailey parenthetically relays a linked allegation that DeepSeek is "based on ChatGPT." This article does not establish that lineage or show that it explains DeepSeek's dash count, so the allegation remains indirect, unresolved, and non-promoted.
- The article's statement that eight or nine em dashes are beyond what almost any human would use is an unsupported interpretation that sits uneasily with its own account of heavy human use and lacks a human baseline.

## Evidence and claims to extract

- **Direct source reviewed:** Complete preserved article titled "Em Dashes, Hyphens and Spotting AI Writing," including the punctuation background, six-system test and counts, limitation discussion, bottom line, three factual-error examples, inline links, and reuse footer, retrieved 2026-05-05.
- **Method and sample:** One unconstrained prompt, "Write an article about the H3H3 lawsuit against reaction streamers," was submitted to six free or basic AI services. Bailey reports one output per service, word counts, em-dash counts, and en-dash counts for two outputs. No repetition, randomisation, model version, generation date, decoding settings, blinded coding, human control, or inferential analysis is reported.
- **Direct versus cited evidence:** C05-C07 and C12 are direct author-reported observations from Bailey's own test, although the raw outputs needed to reproduce them are not preserved. C01, C08-C11, C13, and C15 are Bailey's interpretations or conclusions. C02-C04 and C09 draw partly on linked public comments, dictionaries, style guides, and earlier Plagiarism Today articles rather than evidence generated in this article. C17 is Bailey's indirect relay of a linked Gizmodo allegation about DeepSeek and ChatGPT; the linked source was not reviewed in this work unit. C14 identifies an internal overreach in Bailey's interpretation. C16 is this review's provenance assessment, not a source claim.
- **Important limits and counterexamples:** One output per service cannot establish prevalence or a threshold. Product names are not model versions. Bailey reports that Claude's two em dashes occurred in one highlighted section, but the missing raw output prevents verification of that clustering qualification. Gemini and Meta.ai are direct counterexamples to any universal em-dash claim in this sample, while deliberate and habitual human use is an explicit false-positive case. Easy substitution creates evasion and drift. The raw model text and factual checks were not preserved, so the reported counts and errors are attributable to Bailey but cannot be independently recomputed here. The linked DeepSeek-lineage allegation is also unresolved and cannot explain the observed counts.

## Matched patterns / rules

- C7 `no-em-dashes`; root pattern table row 49; catalogue em-dash tolerance note; focused `grade.ALL_CHECKS["no-em-dashes"]` results
- C6 `no-compound-modifier-density` only as a distinct hyphenated-modifier check, not coverage of Bailey's rhetorical question about generic hyphen substitution
- H10 `genre_specific` journalism and academic source-verification branches
- Product boundary in root `README.md` and `human-eyes/references/process.md`: pattern review does not infer authorship
- H7 advisory catalogue, H9 similar-species disambiguation, H12 genre-aware threshold calibration, and H25 model-family versus generic-AI residue
- `pattern-opportunities.md` mappings for source-grounding, deliberate punctuation, and source date/model metadata

## Associated hypotheses

- H7: Five-check gating grader plus advisory catalogue
- H9: Field-guide voice with similar-species disambiguation per pattern
- H12: Genre-aware threshold calibration
- H25: Model-family versus generic-AI residue
