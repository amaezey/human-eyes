# Wang et al.: Is Human-Like Text Liked by Humans?

## Metadata

- **URL:** https://aclanthology.org/2026.acl-long.639/
- **Author / owner:** ACL Anthology HTML lists Yuxia Wang, Rui Xing, Jonibek Mansurov, Giovanni Puccetti, Zhuohan Xie, Minh Ngoc Ta, Jiahui Geng, Jinyan Su, Mervat Abassy, Saadeldine Eletter, Kareem Elozeiri, Nurkhan Laiyk, Maiya Goloburda, Tarek Mahmoud, Raj Vardhan Tomar, Alexander Aziz, Ryuto Koike, Masahiro Kaneko, Artem Shelmanov, Ekaterina Artemova, Vladislav Mikhailov, Akim Tsvigun, Alham Fikri Aji, Nizar Habash, Iryna Gurevych, and Preslav Nakov
- **Author identity note:** The authoritative proceedings PDF author block renders `Saad El Dine Ahmed` in the corresponding author-list position (affiliation 14), while the ACL Anthology HTML renders `Saadeldine Eletter`. This record preserves both source identities rather than silently treating either rendering as canonical.
- **Published:** 2026-07
- **Retrieved:** 2026-07-14
- **Extracted:** 2026-07-14
- **Source type:** peer-reviewed conference study
- **Evidence tier:** Peer-reviewed / academic empirical
- **Review mode:** new
- **Stable identifier:** DOI 10.18653/v1/2026.acl-long.639; ACL Anthology ID 2026.acl-long.639
- **Version / revision:** ACL 2026 proceedings version, pages 14043-14076
- **Full-text status:** complete
- **Snapshot:** `snapshots/wang-et-al-human-like-text-liked-by-humans.md`
- **Extraction method:** official ACL PDF downloaded and preserved; all 34 pages extracted with Poppler `pdftotext -layout`; page structure checked with `pdfinfo`, `pdfimages -list`, and rendered-PDF inspection
- **Snapshot SHA-256:** `9d18a13990356a2536b21afe1103a56a8ae52ce1539fcb7e3c6983e9e1264f35`
- **Model / corpus scope:** 8,778 human-detection instances from 16 datasets, 9 languages, 9 domains, 11 LLMs, 19 unique native-speaker expert annotators, and 30 annotation settings; additional prompting experiments covered 4,730 examples across 13 datasets, plus automatic evaluation of 17,017 original-prompt and 32,487 improved-prompt generations with 26 detector approaches; preference labeling covered about 5,000 choices from ten annotators across six Arabic, Chinese, and Russian datasets. Languages were Arabic, Chinese, English, Hindi, Italian, Japanese, Kazakh, Russian, and Vietnamese. Reported generators include GPT-4o (including `GPT-4o-2024-08-06` and, in the automatic-evaluation data, `GPT-4o-2024-05-13`), GPT-4o-mini, GPT-4/GPT-4-Turbo, `claude-3.5-sonnet-20240620`, Qwen-turbo, Qwen2/Qwen2-7.5B, Qwen2.5-72B, AceGPT, ChatGLM4/GLM-4-9B-Chat, ChatGLM3-6B, Baichuan2-13B-Chat, Anita, `Llama-3.1-405b-instruct`, and `Vikhrmodels/Vikhr-Nemo-12B-Instruct-R-21-09-24`. Domains included news, community QA, tweets, summaries, Wikipedia, student essays, government reports, academic summaries, and peer-review meta-reviews.
- **Access limitations:** none. The authoritative 34-page PDF is preserved at `snapshots/attachments/wang-et-al-human-like-text-liked-by-humans.pdf` with SHA-256 `521ee263f9bd13efed4f84604d240bdc580d8fcf659add1bffa2539ccda44740`. The Markdown snapshot preserves all extracted text. Figures are not separately rasterized in its body: captions, axes/tick labels recoverable from the text layer, and the authors' prose interpretations are present, but Figure 6's visual heatmap and color encoding are not represented in Markdown. The preserved PDF contains the complete figure, including its content-bearing vertical color scale on PDF page 30.

## Summary

This ACL 2026 long paper tests an upper bound on human recognition of machine-generated text rather than population-average detection. Nineteen native-speaker NLP researchers and practitioners judged 8,778 instances from 16 datasets spanning nine languages, nine domains, and 11 LLMs. Their simple mean accuracy was 87.6%, but results ranged from near chance to 100% and depended on domain, language, model, comparison setup, and prior examples. The paper's expert annotations identify recurring cross-language differences in concreteness, cultural knowledge, structural and emotional diversity, formatting, and language mixing. Prompt revisions that named those differences reduced mean human detection accuracy from 87.6% to 72.5% and reduced 19 of 26 automatic detectors' accuracy, while a separate preference study found that human authorship and reader preference can diverge. For human-eyes, the paper is strong comparative evidence for several existing contextual pattern families and for adversarial, multilingual, genre-aware evaluation, but it does not justify authorship verdicts, universal thresholds, or treating expert intuitions as stable automatic features.

## Main insights

- C01: Selected native-speaker LLM experts can perform far above chance in some multilingual detection settings: the paper reports 87.6% mean accuracy over 8,778 instances, with individual dataset/settings ranging from 50.1% to 100%.
- C02: Detectability is conditional rather than a single human capability. Wikipedia, short dialect tweets, and summaries were harder; news, QA, essays, government reports, and peer-review meta-reviews were often easier. Pairwise comparison and few-shot examples generally helped, and generator choice sometimes changed results sharply. These comparisons are not a fully crossed experiment: some tasks permit non-corresponding texts, Table 5 marks some generated sets as non-parallel, and paired items can be topic-unmatched. The source also reports Japanese news accuracy as 86.4% in Tables 3 and 7 but 62% in Appendix D.6, and several appendix task-setting labels conflict internally with Table 2.
- C03: Across the annotators' qualitative summaries, human text was usually more concrete and informative, including names, dates, places, numbers, URLs, and specific institutions, while machine text more often made generic claims with little support. The prompting follow-up is an important negative result: requesting specificity also produced repetitive names and news outlets, potentially incorrect but persuasive-looking details, and hallucinated Vietnamese event timestamps.
- C04: Human text more often carried regional, cultural, religious, idiomatic, and platform-specific knowledge. These distinctions were especially important in Arabic, Japanese, Hindi, Kazakh, and Chinese, and remained difficult to add through prompts.
- C05: Human text varied more in length, structure, style, emotion, and topic movement. Machine outputs were more formulaic and more consistently neutral or positive, although the exact cues varied by language, domain, and model.
- C06: Machine outputs more often used bullet points, segmentation, Markdown, and polished formatting, while collected human texts more often contained blocks of plain text, typos, grammar errors, hashtags, or platform residue. The authors explicitly note that collection and conversion may partly explain the formatting gap.
- C07: Some non-English generations, particularly from less capable models, mixed English or another language into the response. The annotators described this as rare in the corresponding human data.
- C08: Explicit prompts targeting the observed gaps fully or partly helped in about half of the fill-the-gap survey cases. Across 13 datasets, the same experts' mean detection accuracy fell from 87.6% to 72.5%; 19 of 26 automatic detector approaches also lost accuracy on improved-prompt generations. Cultural nuance, length/structure diversity, phrasing diversity, and situation-appropriate sentiment remained difficult, while specificity instructions introduced repetitive names/outlets, plausible-looking incorrect detail, and Vietnamese timestamp hallucinations.
- C09: Human-like output was not synonymous with preferred output. The direct result is that, across ten annotators and six preference datasets, human text was selected in about half of the cases, with dataset- and annotator-specific distributions. The further claim that machine text is favored when annotators are uncertain which source is human is the authors' interpretation of preference patterns alongside detection accuracy, not an experimentally isolated causal result.
- C10: In the Chinese essay comparison, annotators favored human essays for coherence, sincerity, connected narrative, precise language, and room for reflection. They described machine essays as sometimes verbose but shallow, reliant on abstractions and rhetorical flourishes, weak at connecting multiple stories under one theme, and inclined toward a lecture-like tone.
- C11: Preference was personal and domain-sensitive. Emotion-rich Chinese QA was often judged more favorably when machine-generated because some human answers were biased or mean-spirited; Russian and Arabic preference distributions also differed by annotator.
- C12: The study is an expert upper-bound case study, not a population estimate. No lay annotators participated; many datasets had only one annotator; some repeated sets had three to five; fill-the-gap judgments varied between individuals; no automatic linguistic feature analysis validated the experts' named cues; and the paper's preference conclusions cover only selected Arabic, Chinese, and Russian datasets. Cross-condition comparisons are further limited by non-corresponding, non-parallel, or potentially topic-unmatched samples. Internal reporting inconsistencies include Japanese news at 86.4% in Tables 3 and 7 versus 62% in Appendix D.6, plus appendix labels such as `setting I` for paired Kazakh data, `setting III. Single-binary` for Russian summaries, and `setting I. Pair-binary` for Vietnamese data, which conflict with the definitions in Table 2.

## Evidence and claims to extract

- **Direct source reviewed:** ACL 2026 proceedings PDF for DOI 10.18653/v1/2026.acl-long.639, all 34 pages including the main paper, limitations, ethical statement, broader impact, references, and Appendices A-G.
- **Method and sample:** Human detection used 8,778 instances, 16 datasets, nine languages, nine domains, 11 LLMs, 19 unique native-speaker NLP experts, and four task formulations: single-binary, pair-binary, triplet-three-class, and pair-four-class, in zero- or few-shot settings. Prompt improvement covered 4,730 examples across 13 datasets, using the same annotators and nominal task settings, plus 26 automatic detector approaches on 17,017 original and 32,487 improved generations. Preference labeling used ten annotators and six Arabic, Chinese, and Russian datasets selected to span high, medium, and low detection accuracy.
- **Direct versus cited evidence:** C01-C12 are measured results, author-reported qualitative synthesis, or stated limitations from this paper. The introduction and Appendix A summarize earlier random-chance or moderate human-detection studies; those inherited results are not used as new project evidence here. The paper's interpretation that model memorization explains Wikipedia similarity is plausible but not directly isolated experimentally, so it is not promoted as a causal claim.
- **Important limits and counterexamples:** Mean accuracy hides a 50.1%-100% range. Expert-only results cannot be transferred to ordinary users. Pairwise comparison is easier than single-text judgment, and some comparisons use non-corresponding, non-parallel, or topic-unmatched samples. Short text and memorized/training-heavy domains reduce opportunity for cues. Formatting differences may reflect collection pipelines. Prompting can erase many observed cues but can also manufacture repetitive or false specificity. Human preference can favor machine text, and individual preference distributions can reverse each other. Preference counts do not establish that uncertainty about source identity causes machine preference. Japanese accuracy and appendix task-label inconsistencies remain unresolved in the paper. The study did not use computational linguistic analysis to test whether the experts' qualitative cues form stable classifier features.

## Matched patterns / rules

- Overall stance in `STRATEGY.md`: human-eyes examines writing patterns and does not determine authorship.
- `tonal_uniformity` and `structural_monotony` in `human-eyes/scripts/judgement.json`.
- `faux_specificity` in `human-eyes/scripts/judgement.json`, plus H6 in `human-eyes/scripts/patterns.json`.
- `genre_specific` student, academic, and journalism branches in `human-eyes/scripts/judgement.json`.
- G3 excessive lists, C2 inline-header lists, H2 `paragraph-length-uniformity`, and G9 `sentence-length-variance` in `human-eyes/scripts/patterns.json` and `human-eyes/scripts/grade.py`.
- H10 student essay review, G7 manufactured insight, and H21 low information density.
- H3 drop detection framing, H12 genre-aware threshold calibration, H22 long-tail compression, H25 model-family versus generic-AI residue, and H28 originality/clarity/formality as comparison dimensions.
- `dev/TESTING.md` rules for matched lengths, packaging normalization, complete Audits, genre/register breadth, and keeping coached or humanized generations outside the main comparison corpus.
- Related evidence cards: `russell-karpinska-iyyer-detectors.md`, `waltzer-teachers-detect-ai-essays.md`, `zaitsu-stylometry.md`, `liang-detector-bias.md`, and `dhillon-mfa-students-llms-fiction.md`.

## Associated hypotheses

- H3: Drop detection framing entirely.
- H12: Genre-aware threshold calibration.
- H21: Low information density and wrong sentence subject.
- H22: Long-tail compression and grammatical standardisation.
- H25: Model-family versus generic-AI residue.
- H28: Originality, clarity, and formality as comparison dimensions.
- Proposed follow-up only: multilingual cultural/platform fit and code-mixing should be evaluated as comparison dimensions before any catalogue promotion.
