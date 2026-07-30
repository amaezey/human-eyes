# Paul Graham on "delve" (April 2024)

## Metadata

- **URL:** https://x.com/paulg/status/1777030573220933716; follow-up: https://x.com/paulg/status/1777035484826349575
- **Author / owner:** Paul Graham
- **Publisher / platform:** X for the two direct posts; secondary reporting from Benzinga, Cryptopolitan, Entrepreneur, Guardian TechScape as quoted by Simon Willison, and Business Insider as syndicated by AOL
- **Published:** 2024-04-07
- **Retrieved:** 2026-07-14
- **Extracted:** 2026-07-15
- **Source type:** practitioner social-media posts with journalism amplification
- **Evidence tier:** Practitioner / teacher / editor essays
- **Review mode:** update
- **Stable identifier:** X post 1777030573220933716; follow-up X post 1777035484826349575
- **Version / revision:** current preserved snapshot retrieved 2026-07-14 and candidate contract update extracted 2026-07-15; previous pre-contract extraction dated 2026-07-14
- **Full-text status:** complete
- **Snapshot:** `snapshots/graham-delve-post.md`
- **Extraction method:** existing snapshot compiled from X page titles surfaced in web search and cross-checked against Benzinga, Cryptopolitan, Entrepreneur, Business Insider via AOL, and Simon Willison quoting Guardian TechScape; no refetch in this contract update
- **Snapshot SHA-256:** `9fa2c196cbdc98a0c28ee0ada68997debe94ebba3e1f8f55538ff9839817c53f`
- **Model / corpus scope:** ChatGPT circa April 2024; one cold-email anecdote; later reporting about academic publishing, Nigerian and other postcolonial Englishes, and founder-email register; English; no controlled sample from Graham
- **Access limitations:** x.com blocked anonymous access; post wording comes from indexed X page titles and secondary corroboration rather than direct page retrieval; the attached chart image and the exact URLs for the secondary articles were not preserved, so the chart contents and all inherited measurements remain indirect; no other known omissions from the preserved material

## Summary

Paul Graham's two April 2024 X posts turned one occurrence of "delve" in a cold email into a public shorthand for ChatGPT-written prose. The preserved record also captures the immediate dialect objection, later frequency claims, and an RLHF-origin hypothesis through secondary coverage. For human-eyes, the source is useful as historical and practitioner evidence about salience, register, and the risks of single-word authorship claims. It does not supply a controlled comparison, threshold, or severity basis. Separate academic records for excess vocabulary remain in the Juzek and Ward and Kobak source cards.

## Main insights

- Graham treated one occurrence of "delve" in one cold email as enough to infer ChatGPT authorship, but supplied no method, comparison group, or error analysis.
- Reported comments expanded the concern to written-only formal vocabulary such as "burgeoning" and described unedited model output as an inauthentic register.
- Graham later said AI should be used "in the right way", qualifying the object-code and inauthenticity criticism as an objection to unedited or register-inappropriate use rather than all AI use.
- Nigerian and other postcolonial English speakers were reported as human look-alikes, while other commenters pointed to historical use predating ChatGPT: "delve" can be ordinary formal vocabulary, so a single-word rule risks penalising dialect and register.
- Quantitative claims in the preserved record come from journalism, Philip Shapira's chart, PubMed reporting, and AI Phrase Finder, not from Graham's anecdote.
- The proposed Nigerian RLHF-annotator mechanism is a reported hypothesis, not an established causal result in this source.
- The source is model- and date-sensitive. It concerns public reactions to ChatGPT in 2024 and cannot establish that the word's presence or absence has the same meaning for later models.

## Evidence and claims to extract

- **Direct source reviewed:** preserved text for X posts 1777030573220933716 and 1777035484826349575, reconstructed from indexed X page titles and corroborated quotations, plus the secondary reports preserved in `snapshots/graham-delve-post.md`.
- **Method and sample:** two short practitioner posts prompted by one cold email, plus secondary news and commentary published from April 2024 to 2025; ChatGPT circa April 2024; English; cold-email, academic-publication, and founder-email contexts; no controlled human comparison or sample size beyond the one reported email.
- **Direct versus cited evidence:** C01 comes from the preserved wording of Graham's two posts. C02 and C03 are Graham comments reported by secondary outlets, including his later qualification that AI should be used "in the right way"; Benzinga's disclosure concern is the outlet's interpretation rather than a preserved Graham claim. C04 records reported public counterexamples from Nigerian and other postcolonial English speakers, reported historical use predating ChatGPT, and dictionary senses quoted by Entrepreneur. C05 inherits quantitative claims and a legitimate-use qualification from reporting on Shapira's chart, PubMed, and AI Phrase Finder. C06 is a hypothesis preserved through Simon Willison's quotation of Guardian TechScape and a reported Tony Zador post. C07 is a scope inference from the source dates and later coverage, not a measured source result.
- **Important limits and counterexamples:** x.com was not directly accessible; the chart image and exact secondary article URLs were not preserved; the quantitative, dialect, and causal claims are indirect; Graham gives no threshold, corpus, comparison, or validation; Nigerian and other postcolonial English use and historical usage predating ChatGPT are explicit human look-alikes; no claim supports an individual-document authorship verdict.

## Matched patterns / rules

- Pattern B1, `no-ai-vocabulary-clustering`: `delve` is in `AI_VOCABULARY`. The live registered check masks the quoted word in Graham's exact cold-email sentence and passes with `Max AI words per paragraph: 0 (0 total in text)`; a bare `delve` control passes with `Max AI words per paragraph: 1 (1 total in text)`. The focused `delve` plus `burgeoning` example also passes with one local listed word because `burgeoning` is not in `AI_VOCABULARY`. The three-local-term control, `delve`, `intricate`, and `vibrant`, fails with `Worst paragraph has 3 AI words`.
- `overall-signal-stacking`: `delve` and `burgeoning` occur in `kobak-excess-words.csv`, but the aggregate requires much broader vocabulary evidence or structural co-occurrence. The one-word and two-word focused examples each pass at 0/4. The three-local-term control passes at 1/4 because vocabulary contributes one point and no structural component fires.
- `STRATEGY.md`: human-eyes examines catalogue patterns and does not determine authorship.
- `human-eyes/references/patterns.md`: vocabulary is density and clustering evidence, not one-word proof.
- H1, H3, H9, H24, and H25 in `dev/hypotheses.md`: register calibration, non-detector framing, look-alike disambiguation, register-specific vocabulary density, and model-specific drift.
- `liang-detector-bias.md`, `juzek-ward-delve.md`, `kobak-llm-excess-vocabulary.md`, and `gptzero-ai-vocabulary.md`: direct cards for detector-bias caution, measured excess-vocabulary evidence, and separately scoped vendor vocabulary evidence.

## Associated hypotheses

- H1: continuous calibrated register-distance score per pattern.
- H3: drop detection framing entirely.
- H9: similar-species disambiguation field per pattern.
- H24: register-specific vocabulary density.
- H25: model-family versus generic-AI residue.
