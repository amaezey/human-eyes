# Liang et al.: GPT detectors are biased against non-native English writers

## Metadata

- **URL:** https://www.cell.com/patterns/fulltext/S2666-3899(23)00130-7
- **Author / owner:** Weixin Liang, Mert Yuksekgonul, Yining Mao, Eric Wu, and James Zou
- **Published:** 2023-07-10 online; Patterns volume 4 issue 7 dated 2023-07-14
- **Retrieved:** 2026-07-16
- **Extracted:** 2026-07-16
- **Source type:** Peer-reviewed empirical opinion article with supporting preprint, code, data, and detector outputs
- **Evidence tier:** Peer-reviewed / academic empirical
- **Review mode:** update
- **Stable identifier:** DOI 10.1016/j.patter.2023.100779; PMID 37521038; PMCID PMC10382961; arXiv:2304.02819v3; Zenodo 10.5281/zenodo.7893958 (v1.0.0)
- **Version / revision:** Published Patterns article plus final arXiv v3 methods version and cited Zenodo v1.0.0 code/data record; previous source record was a 2026-05-05 Jina capture without a recorded stable identifier or digest
- **Full-text status:** complete
- **Snapshot:** `snapshots/liang-detector-bias.md`
- **Extraction method:** Complete published JATS XML from Europe PMC converted to Markdown; complete nine-page arXiv v3 PDF extracted with Poppler and pages 1, 5, and 9 rendered and checked; complete Zenodo v1.0.0 ZIP and API metadata preserved, checksummed, inventoried, and its five Python files inspected
- **Snapshot SHA-256:** `3061a0517316608f70b302713c978bfb4bcd9b6da70f1da2096c1d3d324a75ba`
- **Model / corpus scope:** Seven named public detectors as accessed 2023-03-15; GPT-2 XL for the paper's perplexity analysis; March 14, 2023 ChatGPT 3.5 for 31 college essays and 145 CS224N abstracts plus their self-edits; GPT-4, exact build/date unstated, for 91 TOEFL vocabulary enhancements and 88 Hewlett eighth-grade simplifications; English text from 91 TOEFL essays collected from a Chinese forum through 2020, 88 Hewlett ASAP essays, 70 published college essays, 145 Stanford CS224N Winter 2021 abstracts, and 1,574 ICLR 2023 accepted-paper abstracts
- **Access limitations:** No substantive source material is missing. Cell's PDF route returned HTTP 403 and the current PMC PDF route returned an interstitial/404, so the published version is preserved as complete PMC JATS XML; the arXiv PDF preserves figures and full methods. The detector services are proprietary and version/build identifiers, thresholds, and training data are mostly undisclosed. The Zenodo release preserves data and detector outputs but not an executable end-to-end analysis: `extract_scores.py` imports absent modules, contains an undefined `foler` name, and no figure-generation script is present.

## Summary

Liang et al. compare seven March 2023 GPT detectors on 91 TOEFL essays used as a non-native-English group and 88 US eighth-grade essays used as a native-English comparison, then intervene on vocabulary and test prompt-based evasion on 31 college essays and 145 scientific abstracts. The headline false-positive disparity is large, but the source is a small English-language pilot with dataset-level proxies for language background, proprietary detector versions, and incomplete reproduction code. Its strongest contribution to human-eyes is a direct warning against treating predictability, limited lexical range, or any detector-like surface signal as individual authorship evidence. It does not validate a prose pattern, a human-eyes threshold, or a document-level origin verdict.

## Main insights

- The published article reports a 61.3% average false-positive rate across seven detectors on 91 human TOEFL essays; 18/91 were flagged by all seven and 89/91 by at least one. The arXiv methods version gives 61.22%, 19.78%, and 97.80%.
- The 18 unanimously flagged TOEFL essays had lower GPT-2 XL perplexity than the others, but lower perplexity is an association and the limited-expression mechanism is an author interpretation, not an individual authorship rule.
- GPT-4 vocabulary enhancement moved the average TOEFL false-positive rate from 61.22% to 11.77%, a 49.45 percentage-point decrease, while the reverse simplification intervention moved the 88 Hewlett essays from 5.19% to 56.65%.
- In 1,574 ICLR 2023 abstracts, country of the first author's institution was used as a language-background proxy; the lower-perplexity difference remained after controlling for review ratings. This is an ecological comparison, not individually reported native-language data.
- Second-round style prompts reduced maximum reported detector rates from up to 100% to up to 13% for 31 college essays and from up to 68% to up to 28% for 145 scientific abstracts. These are detector-specific maxima, not a universal average or proof that every detector was bypassed.
- The study is date-, detector-, threshold-, genre-, language-, model-, and sample-specific. It does not establish transfer to present detectors, languages other than English, longer texts, or other populations.
- The authors caution against detector use in evaluative and educational settings, ask for heterogeneous and domain-specific evaluation with risk communication, and suggest only a potential low-risk educational self-check use. The educational-aid proposal was not evaluated.
- The preserved Zenodo artifact supports inspection but not exact end-to-end reproduction. It also labels GPT-edited human datasets as `AI-Generated` and labels one `CS224N_gpt3PromptEng` folder's model as `GPT4` despite the paper describing March 14 ChatGPT 3.5, so those metadata labels cannot be treated as ground-truth provenance without resolution.

## Evidence and claims to extract

- **Direct source reviewed:** Complete published Patterns article, DOI 10.1016/j.patter.2023.100779, through the complete PMC JATS record; complete final arXiv:2304.02819v3 nine-page PDF with figures, 36 references, Materials and Methods, prompts, data descriptions, statistical method, and detector inventory; complete cited Zenodo v1.0.0 archive, DOI 10.5281/zenodo.7893958, containing 98 files and ten data/result folders.
- **Method and sample:** Seven detector services were accessed on 2023-03-15. The source compares 91 TOEFL essays collected through 2020 from a Chinese forum with 88 Hewlett ASAP eighth-grade essays; applies paired GPT-4 word-choice interventions; uses GPT-2 XL log probability/perplexity and one-sided paired t-tests; compares 1,574 ICLR 2023 abstracts with a country-of-affiliation language proxy and rating residualisation; and tests March 14 ChatGPT 3.5 college-essay and CS224N-abstract generations before and after self-edit prompts. Exact detector thresholds/builds and the GPT-4 build are unstated.
- **Direct versus cited evidence:** C01-C08 and C15 are direct experiments or reported results/methods; C09 is the authors' direct limitations section; C10-C13 are author interpretation or recommendations grounded in those experiments, not measured downstream outcomes; C14 is direct artifact inspection. Claims that humans struggle to detect AI, that non-native writers generally have lower lexical/syntactic/grammatical complexity, and that second-order or watermarking methods may perform better are inherited from cited sources and are not promoted as direct results here.
- **Important limits and counterexamples:** TOEFL and Hewlett membership proxy individual native-language status; the paper does not give individual proficiency, demographic, socioeconomic, or consent metadata; samples are small and English-only; detector versions and thresholds are largely absent; the paper reports a one-sided paired t-test but does not explain pairing for every cross-group comparison; the ICLR analysis uses affiliation-country rather than writer language; proprietary services prevent exact replay; published numbers are rounded relative to arXiv v3; and human-edited-by-GPT records are not clean binary-authorship controls. Low perplexity and limited lexical range are demonstrated human look-alikes, not positive AI evidence.

## Matched patterns / rules

- `human-eyes/SKILL.md` Keep the product boundary: never classify authorship.
- `human-eyes/references/process.md` Product boundary and no score/confidence/authorship report.
- `human-eyes/scripts/patterns.json` and `human-eyes/references/patterns.md`: evidence preamble, B5 `vocabulary-diversity`, H10 genre-specific student/academic review, and `overall-signal-stacking`.
- `dev/TESTING.md`: complete-Audit requirement, matched genre/register/length controls, packaging normalization, false-positive reporting, and separate labeling for coached or humanized generations.
- H3 drop detection framing, H9 similar-species disambiguation, H12 genre-aware threshold calibration, H19 bootstrap confidence intervals, H24 register-specific vocabulary density, and H25 model-family versus generic-AI residue.

## Associated hypotheses

- H3: Drop detection framing entirely.
- H9: Field-guide voice with similar-species disambiguation per pattern.
- H12: Genre-aware threshold calibration.
- H19: Bootstrap confidence intervals on corpus claims.
- H24: Register-specific vocabulary density.
- H25: Model-family versus generic-AI residue.
