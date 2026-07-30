# Sussman and Carter: AI-mediated communication, complexity, and sentiment

## Metadata

- **URL:** https://doi.org/10.1145/3701716.3717543
- **Author / owner:** Kristen Sussman and Daniel Carter
- **Published:** 2025-04-28 on arXiv; 2025-05-08 in the Companion Proceedings of the ACM Web Conference 2025
- **Retrieved:** 2026-07-17
- **Extracted:** 2026-07-17
- **Source type:** Peer-reviewed conference companion empirical study
- **Evidence tier:** Peer-reviewed / academic empirical
- **Review mode:** update
- **Stable identifier:** DOI 10.1145/3701716.3717543; arXiv:2504.19556v1
- **Version / revision:** Current review: arXiv v1, five-page ACM-formatted proceedings paper; prior record: same paper revision in the 2026-07-14 snapshot
- **Full-text status:** complete
- **Snapshot:** `snapshots/sussman-carter-ai-mediated-communication.md`
- **Extraction method:** Official arXiv v1 PDF preserved; complete embedded text layer converted with Poppler `pdftotext -layout`; PDF structure checked with `pdfinfo`; pages 1, 2, 3, and 5 rendered with `pdftoppm` and compared visually; arXiv API and Crossref metadata checked
- **Snapshot SHA-256:** `143cabe08e9fa50201050114fc172ff31ad08b6ca7d48bd8e89dcaa203cb7dfc`
- **Model / corpus scope:** X/Twitter posts mentioning Donald Trump from 2020 (`n = 970,919`, Kaggle) and 2024 (`n = 20,000`, Meltwater), each covering October 15-November 8 around a US presidential election; corpus language and any language filter are not reported; two 2020 posts rewritten with a system called `ChatGPT-4`, with exact model build, access date, generation parameters, run count, and selection procedure not reported
- **Access limitations:** No substantive source material is missing. The Markdown extraction does not encode figure pixels or red font colour; the complete five-page PDF, including all three figures and the section 2.4 highlighting, is preserved at `snapshots/attachments/sussman-carter-ai-mediated-communication-arxiv-2504.19556v1.pdf`. The arXiv experimental HTML route returned 404 and a later abstract-page request returned 429, but the official PDF and arXiv API were available.

## Summary

This five-page conference companion paper compares unequal corpora of Donald Trump-related X/Twitter posts from matched election-season windows in 2020 and 2024, reports Flesch-Kincaid grade-level, word-length, sentence-variance, and VADER polarity differences, and shows two posts rewritten after a clarity-and-engagement prompt to `ChatGPT-4`. It directly supports a bounded source-versus-rewrite concern: both displayed rewrites add political prescriptions or future-oriented calls to action, while at least one response to an attempted political rewrite was refused; the distinct post count, attempt count, and relation of that refusal to the two displayed pairs are not reported. It also supplies aggregate, time- and genre-specific measurement candidates. It does not label AI use in either corpus, isolate AI from political, audience, sampling, or platform change, validate a document-level detector, or justify the prior card's mappings to A4 promotional language and E4 generic positive conclusions. The paper itself contains inconsistent sentiment percentages, a Figure 1 caption/content mismatch, mismatched references, and an ambiguous readability conclusion that must remain visible.

## Main insights

- The 2020 and 2024 corpora differ in size and acquisition route. Their shared platform, Donald Trump topic, and approximately 3.5-week election window improve comparability, but there are no post-level AI-use labels and no matched-author or matched-post design.
- Mean Flesch-Kincaid grade level changed from 10.24 to 10.04. The difference is statistically significant but practically modest (`0.20` grade levels); the paper places more interpretive weight on compressed extreme scores in 2024.
- Mean polarity rose from `0.044` to `0.115` (`163.4%`, Cohen's `d = 0.281`). Average word length fell `6.6%` (`d = -0.182`), and sentence variance fell `3.6%` (`d = -0.022`). The last effect is near zero even though the paper groups all changes as statistically significant.
- The abstract and results disagree on neutral and positive shares. The abstract reports neutral `54.8%` to `39.8%` and positive `28.6%` to `45.9%`; section 2.3.2 reports neutral `62.9%` to `49.4%`, strongly positive `4.4%` to `8.1%`, and strongly negative `2.1%` to `1.7%`.
- Both shown rewrites add a prescriptive next step absent from the source post. One adds “choose leaders who put people first”; the other adds “unity and leadership that puts America first.” The rewrites also change hashtags and add flag or ballot emoji, so the transformation is not limited to clarity.
- The two original/rewrite cosine similarities are `0.376` and `0.398` (`M = 0.387`, `SD = 0.015`, `n = 2`). The paper interprets one minus each cosine value as “approximately 60-63%” modification while preserving intent, but it gives no similarity implementation and has only two selected pairs; cosine distance is not a validated percentage of content changed and does not by itself prove that meaning or stance was preserved.
- At least one prompt was refused as political persuasion. The paper does not state how many posts were attempted, how the two successful pairs were selected, or which exact ChatGPT build and policy state produced the outputs, so refusal frequency and rewrite availability are unknown.
- The direct examples add a more prescriptive stance rather than moving toward neutrality. Their unity and leadership language may read as positive-framed, but the paper reports no pair-level sentiment score. The prescriptions therefore challenge treating H7 neutrality collapse as the only possible stance change: source-bound review must detect stance addition, erasure, reversal, or reframing.
- The authors explicitly acknowledge platform, topic/person, political-climate, and audience-behaviour confounds and call for replication. The data cannot establish that AI caused the temporal shifts or quantify AI-MC prevalence.
- Predictable-writing, smart-reply-positivity, and emotional-clarification statements are indirect claims attributed to references 6-8, not measured findings of this study. Other literature-framed statements are unsupported or miscited here: detector F1 is pointed to reference 4, a Brookings political-polarization article; the AI-authorship readability statement points to reference 11, Flesch's 1948 readability paper; and concealed-origin susceptibility is the authors' untested interpretation rather than a measured or clearly cited result.

## Evidence and claims to extract

- **Direct source reviewed:** Complete five-page arXiv v1 PDF of *Detecting Effects of AI-Mediated Communication on Language Complexity and Sentiment*, DOI 10.1145/3701716.3717543, including the abstract, all sections, three figures, two displayed original/rewrite pairs, limitations, conclusion, and 13 references.
- **Method and sample:** A Kaggle 2020 corpus of 970,919 posts and a Meltwater 2024 corpus of 20,000 X/Twitter posts mentioning Donald Trump from October 15 through November 8 around US presidential elections. The paper reports preprocessing, Flesch-Kincaid Grade Level, an independent-samples t-test, TextBlob and VADER naming with VADER application, polarity distributions, word length, sentence variance, effect sizes, two qualitative rewrite pairs, and cosine similarities. Exact sampling from the 2024 retrieval pool, bot/retweet handling, corpus language and language filtering, post-length controls, cosine implementation, uncertainty calculations, multiple-comparison handling, code, data, and complete prompt-response inventory are not reported.
- **Direct versus cited evidence:** C01-C16 and C18-C20 concern the paper's data, examples, interpretation, limits, or internal reporting. C17 separates indirect claims attributed to references 6-8 from detector-F1 and AI-readability assertions whose citation pointers are mismatched, plus a concealed-origin assertion that is author interpretation rather than a measured or clearly cited result. None of the indirect upstream results was re-ingested here; the unsupported or miscited assertions cannot be treated as inherited evidence without correction and direct source identification.
- **Important limits and counterexamples:** The corpora have no AI-use labels, are unequal, use different collection sources, and cover different elections and audiences. The two rewrites are selected examples rather than a reported sample; at least one response to an attempted political rewrite was refused, but distinct post count, attempt count, and relation to the two displayed pairs are unknown. The paper's sentiment percentages conflict between abstract and body; Figure 1 contains both Flesch-Kincaid and polarity panels although its caption names only Flesch-Kincaid; detector, readability, and Meltwater citation pointers are mismatched; the text says “Hohenstein & Jung, 2020” while reference 7 is their 2018 paper; TextBlob's role is unclear; the stated readability maxima are outside the displayed Figure 1 x-axis; and the conclusion says readability scores increased even though reported Flesch-Kincaid grade level fell from 10.24 to 10.04. Aggregate associations do not determine who or what wrote one post.

## Matched patterns / rules

- `human-eyes/references/process.md`, “Preserve meaning,” and `human-eyes/references/voice.md`, “Preserve the source”: direct guidance coverage for preserving argument, stance, facts, point of view, genre, uncertainty, and source-closed material; neither supplies an automated paired comparator.
- H7 `neutrality_collapse` and `human-eyes/scripts/judgement.json` `neutrality_collapse`: adjacent source-bound stance concern, but the live assessment reads one document and only flags hedging or flattening. The two direct rewrites add prescriptions rather than neutralising the source, so they challenge the one-way frame.
- A4 `no-promotional-language` and E4 `no-generic-conclusions`: the four exact source fragments produced zero candidates and clear outcomes in focused surface-only runs. The prior mappings are retired.
- G4 `no-unicode-flair`: the ballot emoji in the first rewrite was recognised as one candidate but remained below the aggregate finding threshold; the flag emoji in the second was not recognised. These are quoted social-media examples and not evidence for a general formatting rule.
- H10 `genre_specific`: relevant process coverage for verifying academic citations, DOI, figures, data consistency, and evidentiary support; it does not measure the paper's temporal effects.
- G9 `sentence-length-variance`: conceptually adjacent but not equivalent. It computes within-document sentence-word-count standard deviation for prose of 100+ words; the paper reports an aggregate, unspecified sentence-variance measure across tweet corpora.
- B5 `vocabulary-diversity`: not coverage for average word length or Flesch-Kincaid grade level; it computes type-token ratio on documents of 150+ words.

## Associated hypotheses

- H2 comparison-engine product reframe: relevant possible home for source-versus-rewrite divergence, but no live comparator exists.
- H12 genre-aware threshold calibration: relevant to political social media, post length, platform, topic, and time controls.
- H25 model-family versus generic-AI residue: relevant because `ChatGPT-4` is not a reproducible build identifier and policy behaviour changes over time.
- H20 severity calibration of agent-judgement items: relevant to testing whether H7 can accurately describe source-bound stance changes rather than standalone balance.
