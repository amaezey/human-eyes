# Abdulhai et al.: How LLMs Distort Our Written Language

## Metadata

- **URL:** https://arxiv.org/abs/2603.18161
- **Author / owner:** Marwa Abdulhai, Isadora White, Yanming Wan, Ibrahim Qureshi, Joel Leibo, Max Kleiman-Weiner, and Natasha Jaques
- **Published:** 2026-03-18
- **Retrieved:** 2026-07-15
- **Extracted:** 2026-07-15
- **Source type:** Academic empirical preprint
- **Evidence tier:** Academic empirical preprint; not peer-reviewed in this record
- **Review mode:** update
- **Stable identifier:** arXiv:2603.18161v1; DOI 10.48550/arXiv.2603.18161
- **Version / revision:** arXiv v1, submitted 2026-03-18; replaces the prior abstract-only extraction of the same version
- **Full-text status:** complete
- **Snapshot:** `snapshots/abdulhai-llms-distort-written-language.md`
- **Extraction method:** Complete 96-page arXiv v1 PDF preserved and converted from its embedded text layer with Poppler `pdftotext -layout`; main-paper pages 1-16 and PDF pages 47, 48, and 96 rendered with `pdftoppm` and visually compared
- **Snapshot SHA-256:** `aa42d0be3ed8808624a69398eeae1cedf772a2ba9933fcad0ffaf0659cb5c750`
- **Model / corpus scope:** Three English-language settings: a randomized access study with 100 US-resident native-English-speaking Prolific participants writing one money-and-happiness essay using no LLM or embedded `gpt-4o-mini`; 86 2021 university-student self-driving-car essays from ArgRewrite-v2 revised by humans and by `gpt-5-mini`, `gemini-2.5-flash`, and inconsistently named Claude Haiku versions across five edit prompts with and without expert feedback; and 18,000 ICLR 2026 reviews for 9,000 LLM-topic papers, paired by paper after Pangram classification
- **Access limitations:** None for the paper. The preserved PDF contains all figure geometry and colour. The Markdown snapshot preserves all 96 pages of extracted text, captions, prompts, examples, appendices, and references, but does not reproduce figure pixels. The linked code repository, project page, ArgRewrite-v2 data, ICLR review data, Pangram classifier, and cited sources were not separately ingested in this one-source run.

## Summary

This preprint combines a 100-person randomized LLM-access study, a counterfactual comparison of human and LLM revisions to 86 pre-ChatGPT student essays, and an observational analysis of 18,000 ICLR 2026 reviews classified as fully human or fully LLM-generated. Across the paired revisions and randomized-access writing study, it supplies direct evidence that heavy text generation and LLM revision can change stance, vocabulary, grammar, emotion, and source voice even under minimal or grammar-only instructions. Figure 10 separately reports analytic and argument-style differences, but its body and panel labels cross-assign the user-study and ArgRewrite-v2 samples, so those results cannot be presented as secure paired-rewrite evidence. The paper also supplies important counterevidence: participants who used the LLM only for information or advice looked similar to the no-LLM group on the reported measures, heavy users remained equally satisfied, and the paper cannot support individual-document authorship inference. The full text exposes material reporting and provenance limits hidden by the abstract, including inconsistent Claude version labels, conflicting stance-test values, an abstract claim of a full-point review-score increase where the body reports 4.43 versus 4.13, a body description of those means as 10% rather than about 7.3% higher, and a body claim of 84% more scalability commentary for both strengths and weaknesses where Figure 11 and Table 1 report +50% and +111% respectively.

## Main insights

- The most actionable result is source-bound rewrite fidelity, not a standalone detector: the paper compares initial human drafts with human and LLM revisions and shows that even grammar and minimal prompts can change conclusions and introduce a shared semantic direction.
- Heavy generative use and lighter information-seeking use are materially different in the user study. The latter subgroup resembled the human control on reported voice, creativity, satisfaction, struggle, stance distribution, and embedding location, although this subgroup was defined by observed use after random assignment to LLM access.
- The paper provides direct distributional evidence for pronoun depletion, noun and adjective increases, lexical replacement, and emotional-language shifts. Figure 10 also reports more analytic, statistical, and expert-opinion language, but its cross-labelled samples prevent assigning those comparisons confidently to the paired revision corpus versus the randomized-access user study. None of these aggregate shifts supplies a safe document-level threshold.
- The appendices preserve unusually strong qualitative controls: complete human, LLM-influenced, and LLM-generated money-and-happiness examples, plus original, human-edited, and multi-model rewrites of six ArgRewrite essays.
- Side-by-side examples show two distinct risks: LLM edits can remove source-specific anecdotes, colloquialisms, uncertainty, and positions, and generative revisions can add extensive factual, policy, safety, and causal claims absent from the source draft.
- Expert feedback reduces some measured shifts but does not eliminate them. Effects vary by model and revision mode; `gpt-5-mini` generally shifts most and the Claude condition least in the authors' analyses.
- The ICLR analysis is observational and detector-conditioned. It compares paired reviews of the same papers, but the labels come from Pangram and the paper explicitly concedes possible errors and introduced correlations.
- Several statements conflict within the paper. These conflicts must remain visible rather than selecting a preferred version: Figure 10's section body assigns panel 10a to the user study and panel 10b to ArgRewrite-v2, while the panel subcaptions and full caption make the opposite assignments—10a to ArgRewrite-v2 and 10b to the user study; stance testing is `p = 0.017` in Figure 6 and `p < 0.036` in the body; the abstract's “a full point higher” conflicts with 4.43 versus 4.13 in the body; the body's “10% higher” is about 7.3% from those means; Figure 11's clarity caption gives `z = 11.00` while the body and Table 1 give about 14.37; the body's 84% scalability increase “for both strengths and weaknesses” conflicts with Figure 11 and Table 1's +50% strength and +111% weakness changes; and the category-reduction prompt caps each list at 15 even though Table 1 contains 17 strength categories.

## Evidence and claims to extract

- **Direct source reviewed:** The complete 96-page arXiv:2603.18161v1 PDF, including the 16-page paper, references, ethics and reproducibility statements, appendices A-I, Figures 1-40, Table 1, survey instruments, prompts, conversations, and full sample essays.
- **Method and sample:** Before the main human study, an `n = 8` pilot revealed two natural usage modes—abstention/peripheral information or critique versus extensive generation—and informed the pre-analysis subgroup rule. The main study randomly assigned 45 participants to no LLM and 55 to embedded `gpt-4o-mini`; 28 of the 55 were classified a priori as LLM-influenced after self-report and transcript cross-checking, with less than 40% generated text, leaving a heavy-use subgroup. ArgRewrite-v2 supplies 86 2021 university-student D1/D2 essay pairs and expert feedback; three production model families generated five revision types with and without that feedback. Metrics include sentence embeddings with PCA or t-SNE, unigram Jensen-Shannon divergence, POS distributions, NRC emotion lexicon counts, LIWC, and `gpt-4o` LLM-as-a-Judge classifications. The ICLR study selected 9,000 papers with one Pangram-classified fully human and one fully LLM review, for 18,000 reviews, and used LLM-generated strength/weakness categories plus two-proportion z-tests.
- **Direct versus cited evidence:** C01-C18, C20-C24, and C31 report the paper's studies, results, examples, nulls, methods, or a bounded direct visual observation. C25-C27 and C30 record direct limitations or internal provenance findings. C19, C28, and C32 are inherited or cited background rather than results established by this paper; none of their Pangram/Emi or other upstream sources was directly reviewed here. C29 is the authors' institutional interpretation. C17 and the G1/G2 direction assignments for Table 1-only categories in C22-C23 are explicitly reviewer inferences rather than author-labelled outcomes.
- **Important limits and counterexamples:** The heavy-use and LLM-influenced groups were behavioural subgroups after random assignment to access, not separately randomized treatments. The paper does not report human validation or reliability for the `gpt-4o` stance and argument labels, generation parameters or repeated stochastic runs, confidence intervals for most descriptive shifts, or a causal design for ICLR. Table 1 reports 32 separate category tests without stating a multiple-comparison correction, including several nominal p-values near 0.05. The RCT is one English essay prompt in one US-native-English sample with item-level demographic missingness; ArgRewrite is one English student-essay topic; the ICLR pair set is restricted to LLM-topic papers. Model-version labels conflict. Aggregate group differences do not identify the provenance of one document.

## Matched patterns / rules

- `human-eyes/scripts/judgement.json` `neutrality_collapse` is direct conceptual coverage for C05 and C10 but operates on one document without the original, so it cannot establish collapse.
- Pattern E3 and `no-false-concession-hedges` detect named false-balance phrases only. Focused runs on the paper's grammar-edit stance flip, a generated neutral opening, and a position-taking human passage all returned `passed: true`, confirming that this surface check does not measure the source's paired stance outcome.
- `human-eyes/references/process.md` and `human-eyes/references/voice.md` directly protect meaning, stance, factual qualification, point of view, distinctive choices, quotations, names, and source-closed facts. They cover the required editorial behaviour for C10, C16, and C17 but do not measure comparative semantic or distributional fidelity.
- Pattern H3 `tonal_uniformity` is adjacent to voice loss but tests within-document register lock, not source-versus-rewrite change.
- Pattern H6 `faux_specificity` can flag stock invented detail but does not check whether an edit removed the source author's actual anecdote or added unsupported specifics.
- Pattern H10's academic and student branches cover evidence, source support, draft history, polish-versus-reasoning, and agency. They are adjacent to C15-C17 and C22-C23, not implementations of the paper's quantitative features.
- Pattern B5 `vocabulary-diversity` computes low type-token ratio. C11 instead measures Jensen-Shannon divergence from a specific original draft and does not establish lower vocabulary diversity, so B5 is not coverage.
- H2, H12, H20, H23, H24, H25, and H28 are relevant open research homes for paired comparison, genre calibration, neutrality severity, noun-heavy style, register-specific lexical evidence, model/version scope, and higher-level originality/formality dimensions.

## Associated hypotheses

- H2, comparison-engine product reframe: C05-C18 directly support comparing a rewrite with its source rather than judging either in isolation.
- H12, genre-aware threshold calibration: the results are bounded to two English essay settings and LLM-topic ICLR reviews.
- H20, severity calibration of agent-judgement items: C05 supports evaluating `neutrality_collapse` on source/rewrite pairs, not assuming its current standalone strong-warning severity is calibrated.
- H23, nominalization and noun-heavy style: C12-C13 add paired noun, pronoun, adjective, determiner, and coordinating-conjunction measurements, but no document-level cutoff.
- H24, register-specific vocabulary density: C11 supplies paired lexical-distribution evidence, not support for low type-token ratio or a flat word list.
- H25, model-family versus generic-AI residue: C09, C11, C13, C14, C18, and C26 show model differences and a version-label problem.
- H28, originality, clarity, and formality as comparison dimensions: C02, C12-C16 provide direct paired and self-report context, while still not supporting authorship verdicts.
