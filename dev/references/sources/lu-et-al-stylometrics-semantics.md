# Synergizing Stylometrics with Semantics: Dual-Path Framework for LLM Detection and Attribution

## Metadata

- **URL:** https://aclanthology.org/2026.findings-acl.1855/
- **Author / owner:** Xingyu Lu, Yumeng Ma, Xiang Zhou, Shengli Gan, Guiying Deng, Yang Wen, and Yanbing Liu
- **Published:** 2026-07; proceedings dates July 2-7, 2026
- **Retrieved:** 2026-07-15
- **Extracted:** 2026-07-15
- **Source type:** peer-reviewed empirical research
- **Evidence tier:** Peer-reviewed / academic empirical
- **Review mode:** new
- **Stable identifier:** DOI 10.18653/v1/2026.findings-acl.1855; ACL Anthology ID 2026.findings-acl.1855
- **Version / revision:** Findings of ACL 2026 proceedings version; ACL Anthology landing page commit 717fd3cc0c5b0c9b4c55108aae362c2f8dc47bd0
- **Full-text status:** complete
- **Snapshot:** `snapshots/lu-et-al-stylometrics-semantics.md`
- **Extraction method:** Official ACL paper and checklist PDFs downloaded directly; all pages converted with Poppler `pdftotext -layout`; page counts checked with `pdfinfo`; paper pages 1, 8, and 14 plus both checklist pages rendered and visually compared with the extraction.
- **Snapshot SHA-256:** `91f46741086676a1a1f97fdc2902396ee5545beb590e18c31d33b6d712e4cf47`
- **Model / corpus scope:** English MGTBench Essay, Reuters, and Wikipedia datasets containing human text and text from six LLMs for seven-way closed-set attribution and binary human-versus-machine detection. The paper names ChatGPT, Claude, and LLaMA as examples but does not enumerate all six source models or report their exact versions. DeepSeek-V3 is the default rewriting probe, with Gemini-1.5-Flash as an alternate. A separate XSum persona-steering test uses GPT-4o, DeepSeek-V3, Gemini-1.5-Flash, and GLM-4. Training subsets range from 839 to 8,397 samples.
- **Access limitations:** No pages or supplements were inaccessible. The six main benchmark generators and their exact versions are not fully enumerated in the paper text, code and trained artifacts are not linked from the ACL record, and most reported results do not state repeated-run variance. PDF column layout, tables, formulas, and figure labels were transformed through the embedded text layer, with selected rendered pages checked visually.

## Summary

This Findings of ACL 2026 paper proposes Stylometric-Semantic LLM Attribution, or SSLA, a supervised dual-path classifier that combines handcrafted lexical, syntactic, structural, and rewrite-based features with RoBERTa embeddings. It evaluates seven-way source attribution and binary detection on three English MGTBench domains, plus short-text, low-data, cross-domain, alternate-probe, and persona-steering conditions. The paper provides useful evidence that model-specific style signals can complement semantic representations, but it does not validate any one feature as a universal AI-writing tell or an individual-document authorship rule. The user queue title, "Synergizing Stylometrics with Semantics", is incomplete; the authoritative title at the supplied URL adds the subtitle "Dual-Path Framework for LLM Detection and Attribution".

## Main insights

- The authors report model-dependent lexical, syntactic, and semantic-intention differences under matched prompts, but the exploratory sample size and feature-direction statistics are not reported.
- SSLA's explicit feature path contains type-token ratio, sentence length, noun and verb ratios, average dependency depth and distance, syntax-semantic n-grams, and six similarities between an input and an LLM rewrite.
- The main strength comes from the semantic path and learned fusion. The combined static-plus-rewrite Feature variant, rewrite-only variant, and SN-Gram-only variant perform much worse than RoBERTa or the complete system. Adding the Feature block directly to RoBERTa also reduces average F1, so the study does not justify promoting isolated surface metrics as rules.
- In-domain seven-way attribution is strong, with Macro-F1 values of 0.945 on Essay, 0.966 on Reuters, and 0.956 on Wikipedia, but OTB-D is slightly higher on Essay at 0.949. These are classifier results on a closed benchmark and are outside human-eyes' product objective.
- Short-text, low-data, cross-domain, and persona-steering tests support separate robustness evaluation. They do not establish a universal feature threshold.
- The data-efficiency prose calls the plotted result accuracy, while Figure 3 labels the vertical axis Macro-F1 Score. The metric is internally inconsistent and should not be reported as either one without qualification.
- The cross-domain result, 0.7083 Macro-F1 from Reuters training to Essay testing, is materially below the in-domain results even though it exceeds the compared baselines.
- Replacing DeepSeek-V3 with Gemini-1.5-Flash changes individual dataset results while leaving the reported average close, so rewrite-based rigidity is not fully probe-free.
- A human case is misclassified after the semantic path overpowers a correct style-path decision, while a ChatGLM case needs the semantic path to correct a style-path ChatGPT label. These cases show that familiar constructions and summary metrics remain ambiguous.
- The paper is limited to English, high-quality parsing, offline closed-set attribution, and known source classes. Unknown models remain untested.
- The official checklist reports limited AI assistance for grammar, clarity, wording, and submission procedure, with no role claimed in the ideas, method, findings, or substantive content. It also states that the paper has no dedicated downstream-risk discussion.

## Evidence and claims to extract

- **Direct source reviewed:** The 14-page Findings of ACL 2026 proceedings PDF, DOI 10.18653/v1/2026.findings-acl.1855, and its official two-page Responsible NLP Checklist, both retrieved from ACL Anthology on 2026-07-15.
- **Method and sample:** SSLA is trained for seven-way attribution over human text and six LLM sources in English MGTBench Essay, Reuters, and Wikipedia data. It uses a 140-dimensional style vector comprising six static linguistic metrics, six rewrite-comparison metrics, and 128 selected syntax-semantic n-gram features, plus a RoBERTa-base semantic path. The paper reports binary detection, dataset subsets from 839 to 8,397 samples, Reuters-to-Essay transfer, length strata including fewer than 50 tokens, alternate rewriting probes, and a four-model XSum persona-steering test.
- **Direct versus cited evidence:** C01 through C13 distinguish the paper's own methods, tables, ablations, case studies, limitations, and checklist responses from cited background. The general claim that LLM style fingerprints persist across prompted styles is also attributed to Bitton et al. 2025. Claims about prior detectors, literary attribution, RLHF bias, and earlier stylometric methods remain indirect and are not promoted here.
- **Important limits and counterexamples:** The work is English-only, closed-set, parser-dependent, computationally heavier than a semantic classifier, and evaluated on public benchmark data. Exact versions for the six main generators are not reported. The paper supplies no open-world result, no deployment-risk analysis, no direct human-subject study, no universal direction or threshold for its individual linguistic features, and a qualitative case where fusion turns a correct style-path human label into an error. Figure 3 conflicts with its surrounding prose about whether it reports accuracy or Macro-F1, and SSLA does not lead every dataset-level comparison in Tables 1, 3, or 5.

## Matched patterns / rules

- `vocabulary-diversity` and pattern B5: partial overlap with type-token ratio only.
- `sentence-length-variance` and H13: related length features, but the paper uses sentence length and length strata rather than the current within-document standard-deviation rule.
- `overall-signal-stacking`: conceptual overlap with combining weak signals, but not implementation equivalence to supervised attention fusion.
- `genre_specific`, H12, H22, H23, and H25: domain, grammar-feature, and model-family context.
- `STRATEGY.md`: the paper's classifier objective remains outside human-eyes' non-authorship product boundary.
- `dev/TESTING.md`: matched samples, provenance, weak and reversed cases, and separate handling of coached or adversarial samples.

## Associated hypotheses

- H1: Continuous calibrated register-distance score per pattern.
- H3: Drop detection framing entirely.
- H12: Genre-aware threshold calibration.
- H13: Sentence-length mean as a grader check.
- H22: Long-tail compression and grammatical standardisation.
- H23: Nominalization and noun-heavy style.
- H25: Model-family versus generic-AI residue.
