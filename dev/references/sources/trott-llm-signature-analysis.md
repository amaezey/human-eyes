# Identifying signatures of LLM-generated text

## Metadata

- **URL:** https://seantrott.substack.com/p/identifying-signatures-of-llm-generated
- **Author / owner:** Sean Trott
- **Published:** 2025-04-18T20:41:44.443Z
- **Retrieved:** 2026-07-17
- **Extracted:** 2026-07-17
- **Source type:** Practitioner empirical analysis and research commentary
- **Evidence tier:** Practitioner / teacher / editor essays
- **Review mode:** update
- **Stable identifier:** Substack post ID 161487215
- **Version / revision:** API `updated_at` 2025-04-18T20:42:54.109Z; previous legacy Jina capture retrieved 2026-05-05
- **Full-text status:** complete
- **Snapshot:** `snapshots/trott-llm-signature-analysis.md`
- **Extraction method:** First-party Substack post API fetched with `curl -L`; complete `body_html` converted to Markdown with Python 3 `html2text`; rendered canonical HTML compared at the beginning, middle, and end; two original 14,000 × 5,500 source figures downloaded and visually inspected
- **Snapshot SHA-256:** `f01f9ea152a46efa4d02991428974004a3ff53cf36e628eddf5cd7bd24c80800`
- **Model / corpus scope:** A 2023 third-party dataset of mostly high-school-student argumentative essays and browser-produced ChatGPT-3 and ChatGPT-4 essays on a constrained set of topics reported as N = 90, prompted with approximately 200 words; English; Trott scores the passages with Pythia-14M, Pythia-70M, Pythia-160M, and Pythia-410M. Exact ChatGPT builds, sampling settings, passage counts by condition, Pythia checkpoints/seeds, and analysis code are not supplied.
- **Access limitations:** No public article-body omissions. The post supplies prose, two figures, captions, and high-level results but not the dataset itself, analysis code, exact model builds/checkpoints, sampling settings, regression tables, coefficients, uncertainty intervals, p-values, multiple-comparison handling, cross-validation folds, or split grouping. Claims attributed to cited papers remain indirect unless separately reviewed.

## Summary

Sean Trott reports a small, constrained analysis of whether interpretable metrics from four open Pythia models distinguish mostly high-school-student argumentative essays from browser-generated ChatGPT-3 and ChatGPT-4 essays. The direct results are lower mean token surprisal for both ChatGPT conditions, a qualified and model-size-dependent reduction in surprisal variability, a cosine-distance result that washes out or reverses, higher student intrinsic dimensionality especially in later layers of larger Pythia models, and high three-class cross-validated accuracy within this dataset. The plotted group distributions still overlap, so their ordering is not document-level separation. The source is useful as bounded research evidence and as a strong calibration warning. It does not validate a surface phrase tell, a current-model threshold, or a document-level authorship verdict.

## Main insights

- The source's strongest direct result is distributional: words in the sampled human essays had higher average surprisal than words in either sampled ChatGPT condition across all four Pythia evaluators.
- Variability is qualified rather than universal. Human surprisal standard deviation exceeded ChatGPT-3, while the ChatGPT-4 comparison only trended overall and was significant for larger but not smaller Pythia models.
- Average cosine distance is a direct null and counterexample: different Pythia evaluators disagree, and ChatGPT-4 sometimes exceeds students, so the aggregate result is a wash.
- Student passages show higher Two-NN intrinsic-dimensionality scores, especially with larger Pythia evaluators; the student versus ChatGPT-4 gap is larger in later layers.
- Mean surprisal alone yields reported three-class accuracies of about 73%, 86%, 85%, and 84% for Pythia-14M, 70M, 160M, and 410M. Combining predictability features within each evaluator raises all four to at least 94%, with about 97% for 160M and 410M, on this same constrained sample; the post does not enumerate the exact feature combinations.
- Figures 1 and 2 visibly retain overlap among student, ChatGPT-3, and ChatGPT-4 distributions, especially for surprisal variability and intrinsic dimensionality. This is reviewer observation from the preserved figures, not a quantified author-reported overlap estimate.
- The post does not report a result for every named metric. Entropy is described as measured, but no entropy estimate or null is presented.
- The classifier result is not deployment evidence. The source repeatedly limits the conclusion to these two outdated browser-labelled ChatGPT versions, these student essays, this genre, and these topics, and warns that false positives can harm students.
- The broader homogenisation claim is explicitly conditional author interpretation, not a longitudinal language-change result.
- Several literature claims in the post, including DetectGPT, persistent-homology detection, human ratings of the source essays, and newer-model interaction results, are cited context rather than evidence produced by Trott's analysis.

## Evidence and claims to extract

- **Direct source reviewed:** Complete public article body for Substack post 161487215, API revision `updated_at` 2025-04-18T20:42:54.109Z, including four article headings, 55 API paragraph nodes, three block quotations, one two-item list, two original-resolution figures and captions, 50 links, and 12 numbered notes.
- **Method and sample:** Trott reuses a 2023 paper's English argumentative-essay dataset, described as mostly high-school students and ChatGPT-3/ChatGPT-4 browser outputs on a constrained set of topics reported as N = 90. The prompt is “Write an essay with about 200 words on ‘[topic]’”. Four open Pythia evaluators from 14M to 410M parameters produce predictability and embedding-geometry features. Pairwise condition differences are assessed with regressions across Pythia evaluators; separate random forests use individual and combined predictability features in cross-validation for three evenly distributed labels. The post does not state item counts by condition, exact ChatGPT builds, temperatures, Pythia checkpoints or seeds used, the complete feature list, regression specification, or split grouping.
- **Direct versus cited evidence:** C01-C02 and C06, C08-C18 are the source's framing, direct method/results, explicit limits, or author interpretation. C03-C05 and C07 are literature or source-dataset claims reported from cited work and remain indirect here. The newer-model interactive-pass and curvature observations within C08 are also cited, not measured by Trott.
- **Important limits and counterexamples:** C11 contains a small-evaluator null for human versus ChatGPT-4 surprisal variability; C12 records an unreported entropy result; C13 is a cosine-distance wash with direction reversals; C08 and C17 restrict generalisation across time, models, humans, topics, and registers; C18 records missing reproducibility details. No result establishes a current generic-AI signal, a surface tell, a false-positive rate, a deployment threshold, or authorship for one document.

## Matched patterns / rules

- `sentence-length-variance` / pattern G9 is adjacent only in the broad idea of variation. Its implementation computes standard deviation of sentence word counts and is not token surprisal variability.
- `vocabulary-diversity` / pattern B5 computes type-token ratio and is not mean surprisal, entropy, or token-probability variance.
- `paragraph-length-uniformity` and `overall-signal-stacking` are structural and lexical aggregate checks; neither implements a Trott metric or classifier.
- `human-eyes/references/patterns.md` states that clusters are signals rather than authorship proof.
- `dev/TESTING.md` requires matched provenance, genre/register variation, false-positive reporting, separate candidate versus threshold accounting, complete Audits for project comparisons, and an explicit statement that human-eyes does not classify authorship.
- No record in `human-eyes/scripts/judgement.json` assesses token predictability, embedding geometry, classifier confidence, or synthetic-text provenance.

## Associated hypotheses

- H1, continuous calibrated register-distance score per pattern: adjacent to continuous distributional evidence, but Trott does not validate current project patterns or a transferable register-specific score.
- H3, drop detection framing entirely: supported as a product-framing caution by C01-C02 and C17, not as a new performance estimate.
- H12, genre-aware threshold calibration: supported by the source's narrow argumentative-essay boundary and generalisation warning.
- H22, long-tail compression and grammatical standardisation: C10-C13 provide adjacent token-probability and variability evidence, but not the syntactic measures proposed by H22.
- H25, model-family versus generic-AI residue: supported by the explicit ChatGPT-3/ChatGPT-4, 2023, browser, Pythia-evaluator, and moving-target boundaries.
