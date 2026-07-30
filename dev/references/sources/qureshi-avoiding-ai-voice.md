# @hosseeb: How to avoid AI voice

## Metadata

- **URL:** https://x.com/hosseeb/status/1969157336100192663
- **Author / owner:** Haseeb Qureshi (@hosseeb)
- **Publisher:** X
- **Published:** 2025-09-19
- **Retrieved:** 2026-07-14
- **Extracted:** 2026-07-14
- **Source type:** X post containing practitioner observations and writing-process advice
- **Evidence tier:** Practitioner / teacher / editor essays
- **Review mode:** update
- **Stable identifier:** X post ID 1969157336100192663
- **Version / revision:** single post published 2025-09-19; source bytes unchanged from the pre-contract 2026-07-14 extraction; card upgraded to the current contract on 2026-07-15
- **Full-text status:** complete
- **Snapshot:** `snapshots/qureshi-avoiding-ai-voice.md`
- **Extraction method:** fxtwitter mirror API JSON transcription of the complete single-post body from https://api.fxtwitter.com/hosseeb/status/1969157336100192663; publication time cross-checked by decoding the X post ID snowflake
- **Snapshot SHA-256:** `f6b48ad3c639baaab3e524864b5ba293851e04ee2822d8b00c05b99b5cc07a70`
- **Model / corpus scope:** one English X post of about 340 words, published in September 2025; it discusses unspecified AI writing tools, names Claude Projects and Pangram, does not identify a target writing genre, and supplies no model version, corpus, comparison sample, frequency estimate, or threshold
- **Access limitations:** x.com blocked anonymous retrieval, so the complete post body was obtained through the fxtwitter mirror API. The post is a single long post rather than a thread. Author replies, if any, were not retrieved and are outside the reviewed single-post scope. The source supplies no link for its claimed University of Chicago study.

## Summary

This September 2025 X post gives practitioner advice for avoiding a recognisable AI voice. Qureshi says AI voice sounds hollow and cheap to most readers, says one-shot drafting guarantees that voice, recommends local editing and writer-controlled revision, names four surface tells, and proposes Pangram as a pre-publication perception proxy. The post contributes dated practitioner corroboration and a clear no-authorship qualification, but it contains no measured comparison, threshold, model version, or direct detector evidence. Its Pangram accuracy claim is inherited from an unidentified study, while its low-entropy and human-signature claims are direct but uncited assertions.

## Main insights

- Qureshi frames AI voice as a reader-perception and craft problem rather than proof of authorship.
- He says one-shot generation guarantees AI voice and recommends supplying the writer's own material and style context when whole-draft generation is used.
- He recommends using AI for local editing, beginning whole-piece work with critique, discussing alternatives, and accepting only edits the writer endorses.
- He names the U+2014 em dash, `delve`, `intricate`, and `not just X, but Y` as common AI-associated forms.
- The post explicitly says those forms do not guarantee AI authorship. Its concern is that readers may assume AI use when they see them.
- The Pangram accuracy, detector-comparison, low-entropy, and human-signature claims are not supported by a linked study in the post.

## Evidence and claims to extract

- **Direct source reviewed:** the complete body of X post ID 1969157336100192663, published 2025-09-19 and preserved verbatim in the snapshot.
- **Method and sample:** one English practitioner post of about 340 words. It provides recommendations and examples from the author's experience, not a corpus, experiment, comparison group, model evaluation, reader study, or writing-quality study.
- **Direct versus cited evidence:** C01, C02, and C04 to C11 are direct statements or recommendations made by Qureshi, supported only by practitioner observation. Within C03, the detector comparison and 99%+ precision-and-recall figure are attributed to an unnamed University of Chicago study whose underlying evidence was not supplied. The low-entropy mechanism and categorical human-signature claims are Qureshi's direct but uncited assertions.
- **Important limits and counterexamples:** the tell list is expressly non-exhaustive; none of the four forms receives a frequency estimate from this source; the post says their presence does not prove AI authorship, leaving legitimate human usage as an explicit possibility and a counterexample to authorship inference. The source does not support its claims about most readers or universal AI use, test whether one-shot drafting guarantees a recognisable register, test whether local editing preserves voice, establish that readers and Pangram agree, or measure its prediction that readers will improve at identifying AI voice. It does not identify a target writing genre or establish whether the advice generalises beyond the unspecified writing context of one English X post in September 2025.

## Matched patterns / rules

- `STRATEGY.md` partly covers the craft framing and fully covers the boundary against authorship classification; it does not make the post's universal-use or majority-reader claims.
- `human-eyes/references/process.md` partly covers writer control, voice preservation, planned editing, and validation, but not Qureshi's one-shot, local-editor, critique-first, or top-edits sequence.
- `no-em-dashes` / pattern C7 in `human-eyes/scripts/grade.py`, `human-eyes/scripts/patterns.json`, and `human-eyes/references/patterns.md` detects every U+2014 occurrence. Its current implementation fails a single occurrence at Balanced and All depth.
- `no-ai-vocabulary-clustering` / pattern B1 recognises `delve` and `intricate`, but the deterministic check passes one or two listed words in a paragraph and fails at three or more.
- `no-negative-parallelisms` / pattern B3 directly detects `not just X, but Y`, reports occurrence count, and states that a match is not proof of authorship.
- `pangram-classifier.md` (with `spero-emi-pangram-classifier.md` retired 2026-07-17 as its duplicate) and the detector-caution rows in `pattern-opportunities.md` cover Pangram as evaluation context rather than prose-pattern evidence. They do not verify the post's 99%+ claim.
- No live agent-assessment record in `human-eyes/scripts/judgement.json` covers one-shot drafting, editor-versus-ghostwriter workflow, selective acceptance, or agreement between detector output and reader perception.

## Associated hypotheses

- H3, drop detection framing entirely.
- H7, five-check gating grader plus advisory catalogue.
- H9, field-guide disambiguation for legitimate human look-alikes.
- H11, manufactured insight as a deliberate human rhetorical move that still requires matched-register calibration.
- H24, register-specific vocabulary density rather than flat one-word blacklists.
- H25, model-family, model-version, prompt-style, and public-tell drift.
