# Gmelius: Can Customers Tell an Email May Have Been Written Using Generative AI?

## Metadata

- **URL:** https://gmelius.com/blog/can-customers-tell-an-email-is-written-using-generative-ai
- **Author / owner:** Anwesha Roy / Gmelius
- **Published:** 2025-07-22
- **Retrieved:** 2026-07-15
- **Extracted:** 2026-07-15
- **Source type:** vendor email-writing guide and product marketing page
- **Evidence tier:** Vendor, first-party, and practitioner guides
- **Review mode:** update
- **Stable identifier:** Webflow page ID `6737568a4ac417efeb387e46`
- **Version / revision:** page metadata `dateModified` 2025-07-22; prior and current article-body bytes are identical
- **Full-text status:** complete
- **Snapshot:** `snapshots/gmelius-email-ai-isms.md`
- **Extraction method:** direct canonical HTML plus Jina Reader Markdown, verified against canonical HTML with Beautiful Soup
- **Snapshot SHA-256:** `b2e311e46b36141dbc5935fedd26b631d1b6fbf414c3c4229f6dfc4bd086891a`
- **Model / corpus scope:** unspecified versions of generative AI, ChatGPT, Gemini, and Gmelius; English email and customer-communication guidance; no collected corpus, sample, comparison group, prompt set, output lengths, model versions, or validation method reported
- **Access limitations:** none for the complete substantive article body; decorative hero and avatar images, navigation, signup chrome, recommendation cards, footer, and unrelated promotional video assets were omitted because they add no evidence needed to interpret the article

## Summary

This first-party Gmelius guide supplies a 20-item practitioner watchlist for English email, editing advice, two cited numerical claims, and product claims about Gmelius. It reports no collection method, model versions, sample, comparison group, frequency, error rate, or human baseline for the 20 signs. Its useful contribution is bounded email-review vocabulary, especially placeholders, missing personalization, generic subject lines, weak domain grounding, formatting excess, and formulaic greetings. It cannot establish prevalence, causality, model-general behavior, customer detection accuracy, or authorship. The 2026-07-15 source body is byte-identical to the prior 2026-05-05 Jina capture; this update deepens provenance, claim coverage, project comparison, decision states, and independent review rather than recording a substantive page revision.

## Main insights

- The directly reviewable contribution is a vendor-practitioner list, not a measured detection study.
- Empty placeholders, generic subject lines, fake or missing personalization, weak domain grounding, and unsupported jargon fit the project's existing marketing-email review better than a general prose detector.
- The article explicitly supplies important exceptions: a short reply can suit the situation; complex vocabulary is not unique to AI; title case and bold can be appropriate; technical or formal language can be required; and personalization depends on supplied context.
- Several claimed cues are absences, such as no semicolons, no humor, few pronouns, and little white space. The source gives no baseline, threshold, or comparison needed to operationalize them safely.
- The live deterministic layer exactly detects the placeholder example and the page's heavy bolding, but it does not detect the page's formulaic email greetings as D1 or E8, and its corporate-speak check does not cover the source's `optimization` and `efficiency` examples.
- The page repeats product and outcome claims, including lower cost and effort, high returns, exponentially stronger messages, weekly reinforcement, variation across outputs, context-aware automation, prevention of hallucination, trust and effectiveness effects, and one hour saved per day, without methods or direct evidence on this page.

## Evidence and claims to extract

- **Direct source reviewed:** complete canonical Gmelius article carrying page metadata `dateModified` 2025-07-22 and Webflow page ID `6737568a4ac417efeb387e46`, retrieved 2026-07-15 through canonical HTML and Jina Reader Markdown.
- **Method and sample:** the author provides 20 numbered observations, examples, editing suggestions, 10 FAQs, and Gmelius marketing claims. No source-generation method, sampled emails, model/version, prompt protocol, annotation procedure, comparison group, language beyond English, platform beyond email/customer communication, output-length range, uncertainty, or error analysis is reported.
- **Direct versus cited evidence:** C01 and C04-C34 describe the page's own taxonomy, examples, qualifications, advice, marketing assertions, and review inferences. C02 inherits Gartner's 64% customer-service preference result and the article's linked summary of wrong-answer and personalization concerns. C03 inherits a 9.44% versus 8.46% click-through result from an external 2024 experiment. C31 uses the FAQ's unspecified `Research shows` wording and remains indirect and unresolved. Neither linked work was directly ingested in this update.
- **Important limits and counterexamples:** the page does not test whether recipients can identify AI-written email and does not validate any sign. It concedes that short replies may fit, complex words are also human, formatting can be appropriate, prompting and training alter outputs, and targeted AI emails can work. A named byline does not reveal how the article was produced, so the page is not a verified human-authored control. The page itself contains many bold spans and repeated vocabulary but that consistency check is not authorship evidence.

## Matched patterns / rules

- C1 / `no-boldface-overuse`
- C3 / title case in headings, manual only
- C4 and G4 / `no-unicode-flair`
- E5 / `no-staccato-sequences`, only adjacent to short-email advice
- G3 / `no-excessive-lists`
- H3 / agent assessment `tonal_uniformity`
- H8 / `no-placeholder-residue`
- H10 / agent assessment `genre_specific`, marketing-email branch
- H11 / `no-corporate-ai-speak`, only partial lexical overlap
- E8 / `no-formulaic-openers`, not the article's greeting examples
- G9 / `sentence-length-variance`, not a long-sentence or comma check
- B5 / `vocabulary-diversity`
- Agent assessments `semantic_redundancy` and `even_jargon_distribution`
- Closed-source and source-grounding constraints in `human-eyes/references/process.md`

## Associated hypotheses

- H9, field-guide voice with similar-species disambiguation per pattern
- H12, genre-aware threshold calibration
- H13, sentence-length mean as a register-aware research candidate, adjacent only
- H24, register-specific vocabulary density
- H25, model-family versus generic-AI residue
