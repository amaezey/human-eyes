# Anthropic: Claude system-prompt release notes

## Metadata

- **URL:** https://platform.claude.com/docs/en/release-notes/system-prompts
- **Author / owner:** Anthropic
- **Published:** living release-notes page; reviewed entries are dated 2024-07-12 through 2026-06-09
- **Retrieved:** 2026-07-15
- **Extracted:** 2026-07-15
- **Source type:** first-party model documentation
- **Evidence tier:** First-party model docs
- **Review mode:** update
- **Stable identifier:** none found; living page capture retrieved 2026-07-15
- **Version / revision:** complete first-party Markdown capture through Claude Fable 5 dated 2026-06-09; supersedes the partial 2026-05-05 capture
- **Full-text status:** complete
- **Snapshot:** `snapshots/anthropic-sonnet-prompts.md`
- **Extraction method:** direct first-party `.md` documentation endpoint; checked against raw rendered HTML, a fully expanded 64-page browser PDF, and PDF text extraction
- **Snapshot SHA-256:** `b7a5544d3d32e3e8599885cdf13f9f9b65a5a698ba577734d33c8a4dd5fe2be3`
- **Model / corpus scope:** 16 Claude model headings and 28 dated prompt entries spanning Fable 5, Opus 4.8 through Opus 3, Sonnet 4.6 through Sonnet 3.5, and Haiku 4.5 through Haiku 3; Claude web, iOS, and Android system prompts only, not the Claude API; English prompt text with some entries instructing multilingual response behaviour; no model-output corpus, human comparison, compliance measure, prevalence estimate, or prose-length sample
- **Access limitations:** none for the accessible first-party page. The browser PDF retains page chrome and is supporting rendered verification; the direct Markdown snapshot is the authoritative complete text.

## Summary

Anthropic's complete living release-notes page preserves 28 dated web/mobile system prompts across 16 model headings. It directly documents prompt instructions about concision, lists, headings, bolding, Markdown, tone, response openings, follow-up questions, apologies, knowledge-cutoff disclosures, system-prompt leakage, repetition, metaphors, poetry, emoji, and user style controls. This is instruction-level evidence, not measured model behaviour: it cannot establish compliance, frequency, causality, a human comparison, or authorship. The full source changes the earlier partial record substantially because some instructions provide plausible provenance for candidate residue while others explicitly tell named versions not to produce patterns commonly attributed to AI.

## Main insights

- Prompt instructions change materially by model and date; a cue cannot be attributed generically to Claude from this page.
- Many 4.5-and-later entries instruct minimal formatting and restrict lists, headers, and bolding, which is direct counterevidence to a model-general claim that Claude is prompted to over-format.
- Sonnet 3.5 prompts instruct concise answers and offers to elaborate, but also explicitly forbid filler affirmations such as `Certainly!`, `Of course!`, `Absolutely!`, `Great!`, and `Sure!`.
- Entries constrain openings and turn-taking in both directions: newer prompts limit questions, praise, continued-engagement solicitation, directness preambles, and excessive apology, while Sonnet 3.7, Haiku 3.5, and Sonnet 3.5 entries dated 2024-09-09 (both text-only and text-and-images variants) and 2024-07-12 require a post-code explanation question; Sonnet 3.5 also asks for offers to elaborate or piecemeal continuation with feedback.
- Seven Opus/Sonnet 4.x entries prohibit opening by praising a question, idea, or observation as good, great, fascinating, profound, or excellent; three newer 4.x prompts also prohibit `genuinely`, `honestly`, and either `actually` or `straightforward`. These are direct negative instructions relevant to D1/D3 and B1/H15, not evidence of compliance.
- Older Sonnet 3.5 prompts tell the model to vary repeated wording; this is a direct alternative prompt-level mechanism relevant to synonym cycling, but the page supplies no output evidence that the instruction causes that pattern. Synonym cycling was removed from the catalogue on 2026-07-25 through DR-156, so the mechanism question has no product surface left to attach to.
- Knowledge-cutoff and current-date disclosures are conditionally prompted, which supplies model/version-specific provenance context for D2 without showing that such disclaimers are frequent or inappropriate in every genre.
- User requests, preferences, and style settings can override default tone and formatting, so the same model snapshot does not imply one fixed surface style.

## Evidence and claims to extract

- **Direct source reviewed:** Complete first-party Markdown response from `https://platform.claude.com/docs/en/release-notes/system-prompts.md`, retrieved 2026-07-15, with 16 model sections and 28 dated Accordion entries. The source was checked against the rendered canonical page, raw HTML, a 64-page expanded PDF, and extracted PDF text at the beginning, middle, and end.
- **Method and sample:** First-party living documentation, not a study. The sample is the complete accessible prompt archive for named Claude web/mobile releases from 2024-07-12 to 2026-06-09. It contains prompt instructions but no outputs, users, documents, comparison group, ratings, error bars, compliance tests, or human-authored prose.
- **Direct versus cited evidence:** C01-C24 are direct statements, prompt instructions, or direct comparisons among the preserved dated entries. No cited source is used to establish a project conclusion. References inside the prompts to product documentation, support pages, or external facts are not separately reviewed here.
- **Important limits and counterexamples:** A system instruction is not a behavioural result. The page cannot show whether a model follows an instruction, how often a surface feature appears, whether an instruction caused it, or whether humans use the same feature differently. User requests and style settings are explicit modifiers. Bold markup for multi-entry models marks documentation changes, while bold inside single-entry prompts may be literal prompt emphasis; neither is model-output evidence.

## Matched patterns / rules

- C1 `no-boldface-overuse`, G3 `no-excessive-lists`, and G6 `no-section-scaffolding`: relevant as instructed-against formatting in many recent prompts, not as observed behaviour.
- C4/G4 `no-unicode-flair`: several dated prompts instruct against unrequested emoji; the instruction does not prove output compliance.
- D1/D3 `no-collaborative-artifacts`: exact anti-affirmation wording appears in Sonnet 3.5, seven Opus/Sonnet 4.x entries prohibit opening praise, and older entries positively instruct offers to elaborate, piecemeal continuation/feedback, or a post-code explanation question. The post-code instruction appears in Sonnet 3.7, Haiku 3.5, and Sonnet 3.5 entries dated 2024-09-09 (both variants) and 2024-07-12.
- D2 `no-knowledge-cutoff-disclaimers`: several prompts conditionally require cutoff or current-information disclosures.
- B1 AI vocabulary and H15 `no-performed-candour`: Sonnet 3.5 and Haiku 3.5 explicitly forbid directness/honesty preambles, including examples beginning `I aim to` and `I need to be`; Opus 4.8, Sonnet 4.6, and Opus 4.6 prohibit `genuinely`, `honestly`, and either `actually` or `straightforward`.
- Synonym cycling (former #11, removed 2026-07-25 via DR-156): Sonnet 3.5 directs lexical variation, but supplies no output or causal test.
- G2 generic metaphors and H10 poetry review: prompts allow explanatory metaphors while Sonnet 3.7 and Haiku 3.5 instruct against hackneyed poetry imagery and predictable rhyme.
- H25 `Model-family versus generic-AI residue`: the primary project home for the prompt archive's model/date/surface boundaries.

## Associated hypotheses

- H25: Model-family versus generic-AI residue — directly supported as a provenance requirement because prompt instructions vary by model, date, product surface, and user style control; not supported as a behavioural or authorship result.
