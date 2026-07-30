# Karolina Rudnicka: Each AI Chatbot Has Its Own Distinctive Writing Style—Just as Humans Do

## Metadata

- **URL:** https://www.scientificamerican.com/article/chatgpt-and-gemini-ai-have-uniquely-different-writing-styles/
- **Author / owner:** Karolina Rudnicka; edited by Madhusree Mukerjee; published by Scientific American
- **Published:** 2025-07-09
- **Retrieved:** 2026-07-17
- **Extracted:** 2026-07-17
- **Source type:** first-person science journalism reporting an author-run exploratory stylometric comparison
- **Evidence tier:** Journalism / reported cases
- **Review mode:** update
- **Stable identifier:** Scientific American article ID 1309411; Contentful ID `3MPLDwXrQZYNJY9I2LsWUB`
- **Version / revision:** canonical article record updated 2025-07-10T17:52:31.284000+00:00; prior pre-contract Jina capture retrieved 2026-05-05
- **Full-text status:** complete
- **Snapshot:** `snapshots/rudnicka-chatbot-writing-style.md`
- **Extraction method:** canonical HTML downloaded with `curl --compressed`, preserved losslessly with `gzip -n`, and parsed from the original bytes; rendered `<article>` and embedded structured article data parsed with Python 3 and Beautiful Soup; complete body cross-checked against two Jina Reader routes; original chart and lead image downloaded and visually inspected; cited Zenodo dataset metadata and complete ZIP inspected for scope and literal-count verification
- **Snapshot SHA-256:** `0e2085da539e84d9e8cd891c970027b2259f8e794f670746730d405f441e9337`
- **Model / corpus scope:** product labels ChatGPT and Gemini, model versions and generation settings unspecified; 205 nonempty diabetes texts per product from cited dataset files timestamped January 2024, primarily 590-601 whitespace-separated words; English medical-topic explanatory prose; model-versus-model comparison only; no human comparison
- **Access limitations:** no substantive article material is missing. The page does not provide the Delta/trigram analysis code, random seed, selected 10 percent sample identifiers, preprocessing/tokenization rules, model versions, prompts, settings, human baseline, uncertainty, repeated-split results, or full ranked top-20 trigram lists. The cited dataset is indirect evidence and was inspected, not recursively ingested as a separate source card.

## Summary

Rudnicka reports an exploratory comparison of ChatGPT- and Gemini-labelled diabetes texts from a cited Zenodo dataset. She applies Burrows's Delta to one random 10 percent sample from each product group, reports lower within-product than cross-product distances, and compares frequent trigrams and word choices. The article's useful contribution is model-specific, topic- and date-bound style evidence: the ChatGPT group is more formal and clinical in the published examples, while the Gemini group is more conversational. It does not establish a generic AI voice, a human-versus-AI threshold, a validated model-attribution system, or a causal mechanism. The complete source record also exposes a prose/chart discrepancy, missing generation provenance, an unspecified random split, and no human control.

## Main insights

- The direct analysis compares two product-labelled model corpora with one topic and similar lengths; it does not compare model text with human writing.
- Reported Delta distances are 0.92 from a ChatGPT sample to the ChatGPT dataset versus 1.49 to Gemini, and 0.84 from a Gemini sample to Gemini versus 1.45 to ChatGPT. The article does not say whether sampled texts were excluded from their reference datasets or whether the result repeats across splits.
- The published phrase contrast is specific to diabetes prose: ChatGPT is described as more formal, clinical, and academic; Gemini as more conversational and explanatory.
- The chart and cited dataset support exact large differences for `blood glucose levels` and `high blood sugar`, but no matched human frequency shows that either side is an AI-versus-human tell.
- The prose says `the cascade of`; the chart says `a cascade of`. The cited dataset contains the chart form and no literal instance of the prose form.
- The principle-of-least-effort, self-priming, and emergent-ability explanations are alternatives proposed by the author, not tested mechanisms.
- The article explicitly says model idiolects may change across updates or versions. Missing model build identifiers make the reported January 2024 product labels non-portable to current systems.
- The article's possible authorship/model-identification application is interpretation, not evaluated detection evidence. No threshold, held-out human control, error rate, confidence interval, or mixed/editing test is reported.

## Evidence and claims to extract

- **Direct source reviewed:** Scientific American canonical article ID 1309411, updated 2025-07-10T17:52:31.284000+00:00, including display headline, standfirst, byline/editor, all 12 substantive body paragraphs, two substantive headings, one content-bearing chart, lead illustration, links, and structured asset metadata.
- **Method and sample:** Burrows's Delta over frequencies of common function and content words; one unspecified random 10 percent sample from each full product-labelled diabetes group; comparison against both complete product groups; top-20 trigram extraction for each group; published chart of ten selected phrase contrasts. The cited ZIP contains 205 nonempty texts per group, 15 additional empty ChatGPT placeholders, January 2024 file timestamps, and similar text lengths. Model versions, prompts, settings, generation route, random seed, sample IDs, tokenization, code, and human controls are absent.
- **Direct versus cited evidence:** C04-C10 are the article's direct dataset description, method, reported results, examples, chart, and interpretations, with the snapshot's mechanical dataset cross-check clearly marked as reviewer verification. C01-C03 report background claims inherited from cited studies. C11-C14 are author interpretations, limitations, or proposed applications rather than measured detector results. The Zenodo metadata and files are cited-source context, not a second ingestion.
- **Important limits and counterexamples:** one medical topic; one product-labelled corpus per side; undisclosed model versions and prompts; no humans; possible sample-to-reference overlap not resolved; one random split; no uncertainty, statistical test, replication, or held-out classifier; only ten of the stated top 20 trigrams per product are published as contrasts; no exact chart data table; `cascade` prose/chart conflict; lexical choice is interpreted as accessibility without a readability or reader study; causal explanations untested; later model drift acknowledged; model/document attribution unvalidated.

## Matched patterns / rules

- H25 `Model-family versus generic-AI residue`: fully covers the correct research framing but is an open hypothesis, not runtime behavior.
- H24 `Register-specific vocabulary density`: partly covers the need for dated, register-specific lexical comparison but does not implement product-family trigram profiles.
- H1 `Continuous calibrated register-distance score per pattern`: adjacent to the distance framing, but Rudnicka reports uncalibrated source-corpus Delta distances, not human-register z-scores or project reliability curves.
- H3 `Drop detection framing entirely`, `human-eyes/references/process.md`, and `dev/TESTING.md`: fully cover the no-authorship, matched-register, candidate-versus-threshold, provenance, and complete-Audit boundaries.
- B1 `no-ai-vocabulary-clustering`: partly recognizes the cited background list, not the direct diabetes result. Focused execution found `delve`, `underscore`, and `commendable` among the six cited examples, while bare `align`, `noteworthy`, and `versatile` were not B1 matches. Each of the ten direct diabetes phrases returned zero B1 candidates.
- H3 `tonal_uniformity`: not covered and not supported. Its agent assessment asks whether one whole text holds a register without breaks; Rudnicka compares aggregate phrase frequencies between corpora and supplies no within-document or human-register result.
- H13 `no-bland-critical-template`: not covered and explicitly not supported; the project already records Rudnicka only as model-specific context, not template evidence.

## Associated hypotheses

- H25 `Model-family versus generic-AI residue`: directly informed and materially bounded by missing model/version and prompt provenance.
- H24 `Register-specific vocabulary density`: directly informed by the diabetes-only phrase distributions and lack of human/register controls.
- H1 `Continuous calibrated register-distance score per pattern`: methodologically adjacent, but the source supplies no project calibration or human distribution.
- H3 `Drop detection framing entirely`: informed by the gap between a source-corpus distance result and the article's proposed authorship application.

## Prior-to-current comparison

- **Added:** complete current provenance; article and Contentful identifiers; editor and update timestamp; original HTML, chart, and lead-image attachments; exact prior archive and digest; beginning/middle/end structure checks; cited-dataset scope verification; 14 claim IDs; deterministic B1 checks; source-to-project coverage; recommendation states; decision history; and independent-review fields.
- **Corrected:** the current display headline differs from the old internal/Jina title; the direct corpus is 205 nonempty files per product, not only “hundreds”; the analysis is model-versus-model with no human control; model versions, prompts, random split, and code are unspecified; the article's `the cascade of` differs from its chart and cited data's `a cascade of`.
- **Removed:** the unrelated fundraising module and page chrome from the active snapshot. No substantive article claim was removed.
- **Unchanged:** canonical URL, author, publication date, direct article body, four Delta values, core diabetes phrase contrasts, model-update warning, rejection of H13 support, and the source's main use as model-specific rather than universal-AI context.
