# Geng and Trotta: Is ChatGPT Transforming Academics' Writing Style?

## Metadata

- **URL:** https://arxiv.org/abs/2404.08627
- **Author / owner:** Mingmeng Geng and Roberto Trotta
- **Published:** 2024-04-12; v2 revised 2024-11-08
- **Retrieved:** 2026-07-15
- **Extracted:** 2026-07-15
- **Source type:** academic preprint; population-level corpus analysis with controlled simulated admixtures
- **Evidence tier:** Academic empirical preprint (no peer-reviewed publication identified); grouped under README.md's Peer-reviewed / academic empirical tier
- **Review mode:** update
- **Stable identifier:** arXiv:2404.08627v2
- **Version / revision:** current arXiv v2; prior library snapshot also contained v2
- **Full-text status:** complete
- **Snapshot:** `snapshots/geng-trotta-transforming-academic-style.md`
- **Extraction method:** official arXiv v2 PDF downloaded and converted with Poppler `pdftotext -layout`; rendered pages 1, 9, and 19 checked
- **Snapshot SHA-256:** `fc47635e58ce43bb5120f3b7f2ab301470951fd0780e5571818a2ce7bde39fad`
- **Model / corpus scope:** one million arXiv abstracts submitted May 2018-January 2024; the paper does not report a language filter; GPT-3.5 simulation model `gpt-3.5-turbo-1106`, temperature 0.7, seed 1106, top_p 0.2; four reported subject groups cover 70% of the corpus
- **Access limitations:** none; the authoritative 19-page PDF is preserved, and plain-text equation and multi-column layout is a best-effort transformation

## Summary

Geng and Trotta analyse word-frequency changes in one million arXiv abstracts and calibrate a population-level estimate of “ChatGPT impact” with GPT-3.5-modified pre-ChatGPT abstracts. The paper contributes direct, prompt- and discipline-scoped evidence that both rising and falling word frequencies can track simulated LLM revision, including decreases in `is` and `are`, but it does not validate a document-level detector, identify individual LLM users, or show that the live human-eyes copula-replacement constructions caused those decreases. The refresh preserves the complete 19-page v2 paper, narrows the inherited B2 mapping, and makes the source most useful to register-specific vocabulary-density and calibration work.

## Main insights

- The direct corpus observation is a post-release change in aggregate word frequencies, not proof that any abstract or author used an LLM.
- In real 2023 arXiv abstracts, `is` and `are` fell by more than 10% after being comparatively stable; the authors call these examples anecdotal before fitting their larger model.
- Under one GPT-3.5 revision prompt, Table 1 reports category-specific decreases in `is` and `are` and increases in `significant`; the size and even direction of a word-level signal cannot be generalized beyond the stated model, prompt, corpus, and category. Table 1's astrophysics `are` row is internally inconsistent: 1.39 to 1.25 is about a 10% decrease, while the printed change is -1%.
- The method selects words adaptively by category, including decreasing words, because research-topic drift, baseline frequency, noise, and prompt sensitivity can confound flat lists.
- Simulated and real word-frequency changes correlate weakly in 2021-2022 and strongly in 2022-2023, especially for computer-science abstracts, but the paper frames this as population-level consistency rather than authorship classification.
- The authors go beyond that correlation to speculate that ChatGPT may be the main reason for recent word-frequency change and describe computer scientists as the most enthusiastic adopters among the four groups. Those interpretations are not causal or user-count results and conflict with the paper's later statement that simulated data cannot accurately estimate how many people use LLMs.
- The approximately 35% computer-science result is a relative “LLM-style” density against one simple-prompt baseline, not a percentage of authors or papers known to use ChatGPT; the authors say the relative estimate can exceed 1 under different prompt effects.
- Same-prompt calibration and testing worked better than a changed-prompt test using “Please rewrite the following paragraph from an academic paper:”. Changed-prompt estimates remained close at lower admixture ratios but were usually high, which directly limits prompt transfer; normalization by the total abstracts in a period and by the total words in a period produced similar trends with detail differences. Figure 3's panel label identifies the second normalization as total words, while its shared caption describes normalization by abstracts, an apparent source inconsistency.
- Topic words such as `Covid-19`, `LLMs`, and `AI` supply a counterexample to treating every large frequency change as stylistic evidence.
- The authors distinguish LLM-like style from direct LLM use and allow indirect habit diffusion as an alternative explanation.
- Benefits for non-native English writers and risks from unsupervised full generation appear in the Discussion as author interpretation supported by citations, not as outcomes measured by this study.

## Evidence and claims to extract

- **Direct source reviewed:** complete official arXiv v2 PDF, arXiv:2404.08627v2, submitted 2024-11-08; all 19 pages, seven numbered sections, References, appendices A-F, Tables 1-2, and Figures 1-8 were preserved and checked.
- **Method and sample:** Kaggle arXiv metadata snapshots version 161 and pre-ChatGPT version 105; one million abstracts submitted May 2018-January 2024, with no reported language filter; four detailed categories covering 70% of the corpus. Section 3.1 and Figure 1 divide the corpus into 100 consecutive periods of 10,000 abstracts. The discipline-level simulation and real-data model instead divide it into 20 article-count periods whose arXiv identifier bounds appear in Appendix A; period 20 ends in January 2024. Table 1's initial simulation processes 10,000 abstracts from period 14 with GPT-3.5. The later calibration pipeline, restricted to abstracts after the stated September 2021 training cutoff, separately uses 20,000 period-13 abstracts to estimate word-change rates, 10,000 period-12 abstracts for calibration, and 10,000 period-14 abstracts for testing; it sets `T0 = 10`, `m = 1`, and 11 simulated mixing ratios from 0 to 0.5. The 11 calibrated word sets may repeat, and word sets calibrated at the same admixture ratio generally estimate the matched test ratio better. Appendix E lists `1/qᵈ` threshold values of 10, 20, 30, 40, 50, 60, 70, 80, 100, 150, 200, and 500, and `r̂` candidate values of 0.1, 0.15, 0.2, `0,3`, 0.4, 0.5, 0.6, 0.7, and 0.8; selection applies less-than thresholds to `1/qᵈ` and to the transformed criterion `(r̂ + 1) / r̂²` using the corresponding candidate value. `0,3` is preserved as an apparent decimal-punctuation inconsistency, not silently corrected. Google Ngram English-word frequencies supply a reference and the calibration considers its 10,000 most frequent words; that reference does not establish a paper-level language filter.
- **Direct versus cited evidence:** C01-C13 and C15 describe the paper's data, simulations, model, results, controls, or stated limits. C14 preserves the Discussion's author interpretation and cited context; it is not a measured finding here. The broader detector, productivity, citation-error, and non-native-writer claims in the Introduction are cited background and are not used as direct project evidence.
- **Important limits and counterexamples:** population aggregates cannot classify a short document or identify users; `LLM style` may arise without direct use; the baseline is one GPT-3.5 version and simple prompt; other models and real prompts may differ; different-prompt tests are usually high, while calibration-driven word selection can introduce a new bias that neutralizes the original so estimates are not necessarily high; the counterfactual assumes selected-word frequencies would have stayed stable without LLMs and substitutes the pre-ChatGPT mean for an unobservable baseline; the paper assumes without evidence that other LLMs were less used through January 2024; the Eq. 18 high-bias result depends on Case 1 ignoring only impact's effect on `ξ` relative to other terms, with a zero-mean small-variance `δ(*)`, while retaining and differentiating `g(η)`; both processing-noise terms are separately assumed zero-mean Gaussian with variance proportional to frequency, and Case 2 adds Gaussian count variation while retaining those processing-noise assumptions; Figure 4 restricts high-change words to maximum counts above 500; Figure 6 restricts correlation plots to words occurring more than 0.1 times per abstract before processing; Appendix F's variance analysis uses the first 500,000 computer-science abstracts and 12 most frequent words, and its Gaussian approximation fits only a subset of tested words; four reported categories cover 70% and cross-posts use only the first category; no language filter is reported; hot-topic terms confound raw change; simulated data cannot accurately estimate user counts; extension from abstracts to full papers is proposed, not tested; Table 1's printed astrophysics `are` change conflicts with its displayed before/after values; Appendix E prints `0,3` in a decimal grid; Figure 3's normalization caption conflicts with panel (b).

## Matched patterns / rules

- B1 `no-ai-vocabulary-clustering`: partial conceptual overlap only; the paper supports population-level, category-specific frequency change, not the live fixed list or its paragraph threshold.
- B2 `no-copula-avoidance`: challenged evidence mapping; the paper measures fewer `is` and `are` tokens but does not measure `serves as`, `stands as`, `functions as`, `marks a`, `represents a`, `boasts`, or `features` as replacements.
- `overall-signal-stacking`: supports its non-authorship and aggregate-evidence posture, not its current component weights or threshold.
- H10 `genre_specific` academic branch: supports corpus- and genre-bound interpretation but does not itself validate the branch's citation/argument watchlist.
- No complete human-eyes Audit was run or needed for source-to-project coverage; implementation was inspected directly and existing deterministic tests define B2's actual behavior.

## Associated hypotheses

- H1 continuous calibrated register-distance score per pattern: supports population-level, register-specific calibration and uncertainty rather than binary authorship claims.
- H12 genre-aware threshold calibration: supports discipline/category-specific baselines and results.
- H24 register-specific vocabulary density: directly supports repeated, time-sensitive, register-specific increases and decreases rather than flat one-word blacklists.
- H25 model-family versus generic-AI residue: supports model-, prompt-, and version-specific source metadata and warns against generic-AI attribution.
