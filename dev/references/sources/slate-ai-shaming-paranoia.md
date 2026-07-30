# Laurie Clarke: ChatGPT Shaming Is Making Our Writing So Much Worse

## Metadata

- **URL:** https://slate.com/technology/2025/08/chatgpt-artificial-intelligence-shaming-paranoia-writing.html
- **Author / owner:** Laurie Clarke / Slate
- **Published:** 2025-08-20 at 10:30 AM; `article:published_time` and NewsArticle `datePublished` are 2025-08-20T14:30:00+00:00; conflicting Permutive `publishedTime` is 2025-08-19T04:26:58+00:00
- **Retrieved:** 2026-07-17
- **Extracted:** 2026-07-17
- **Source type:** journalism with first-person observation, reported interviews, linked examples, and cited research
- **Evidence tier:** Journalism / reported cases
- **Review mode:** update
- **Stable identifier:** Slate article component `slate.com/_components/article/instances/cmeisilvf0053r3m7oafbb0n4@published`
- **Version / revision:** current published component `cmeisilvf0053r3m7oafbb0n4`; previous legacy extraction SHA-256 `849a05903ab87f0270eecc5ee9c000f127f67100302367dbbe13559c5e5887eb`
- **Full-text status:** complete
- **Snapshot:** `snapshots/slate-ai-shaming-paranoia.md`
- **Extraction method:** direct Slate HTML fetched with `curl -L --compressed`, transcribed to Markdown, and checked against both Jina Reader renderings and the archived 2026-05-05 extraction; the full hero illustration was preserved separately
- **Snapshot SHA-256:** `406c6f78c1c9af10b780472acd86327fd90ef8f6d5daf7db72c3de426f5a62b4`
- **Model / corpus scope:** August 2025 English-language cultural journalism about public reactions to ChatGPT-associated prose across email, Medium, LinkedIn, online publishing, brands, SEO, and student writing; qualitative first-person and interview reporting, not a sampled model-output corpus or authorship study
- **Access limitations:** none for the Slate article: the canonical page returned HTTP 200 and exposed the complete headline, deck, byline/date, hero illustration/caption, and 21 body paragraphs. The article's linked posts and papers were not recursively ingested; their findings remain indirect unless separately reviewed.

## Summary

Clarke's 1,261-word Slate article combines her own reaction to accusations of AI-written prose with interviews, linked public examples, expert commentary, and summaries of academic work. It documents a social feedback loop in which writers remove em dashes, words, metaphors, formal conventions, or even corrections to avoid looking machine-written. For human-eyes it is strongest as dated journalism about false-positive harm, anti-AI camouflage, and public-tell drift. It supplies no representative sample, model comparison, detector evaluation, causal test, frequency estimate, or threshold, and its cited academic findings cannot become direct project evidence through this card.

## Main insights

- Clarke describes second-guessing punctuation, voice, polish, and whether to correct a typo because polished prose can attract AI accusations.
- The article reports people purging em dashes, words associated with ChatGPT, the `not just X, Y` construction, metaphors, and formal writing conventions despite claiming human authorship.
- Gallagher's mistaken suspicion of a 2019 paper is a concrete false-positive anecdote; it does not measure a false-positive rate.
- Smith and McCarty report leaving or recommending small errors as authenticity cues, while brands reportedly request em-dash removal because they fear search-ranking penalties.
- Clarke treats triads, transitions such as `however`, metaphors, and polished grammar as legitimate writing practices that can be degraded by indiscriminate tell removal.
- The student-writing, workplace-stigma, and spoken-vocabulary findings are summaries of linked research, not findings established by Clarke's reporting method.
- Ippolito says public tells are transient because training-data recipes change; the claim supports time/version metadata and caution, not a timetable or model-wide rule.
- The article preserves countervailing possibilities: more personalised prose may be welcome, and reviewing a habitual device can improve word choice when the goal is craft rather than camouflage.

## Evidence and claims to extract

- **Direct source reviewed:** The complete current Slate page at published component `cmeisilvf0053r3m7oafbb0n4`, including headline, deck, Laurie Clarke byline, displayed/structured publication time, hero illustration and caption, 21 body paragraphs, and 13 inline source links. The direct HTML, two Jina renderings, and archived legacy extraction were compared.
- **Method and sample:** Qualitative cultural journalism in English. Evidence consists of Clarke's first-person account; interviews with Thomas Smith, Larissa McCarty, Jessica Reif, and Daphne Ippolito; attributed material from John Gallagher and Jack McNamara; linked public examples; and summaries of external papers. The article supplies no interview count beyond the named people, sampling frame, model/version test, comparison group, output corpus, or quantitative analysis.
- **Direct versus cited evidence:** C01, C04-C06, C10-C12 draw on Clarke's observations, analysis, or direct interviews. C02-C03 mix Clarke's synthesis with linked posts and attributed examples. C07-C09 report external research and remain indirect; Reif's interview in C08 explains the reported Duke result but does not turn the study result into this article's own measurement.
- **Important limits and counterexamples:** The article's claims are dated to the public discourse of August 2025. It does not establish that any named feature is unique to AI, that avoiding a feature changes detector or SEO outcomes, or that bylined published prose proves a no-AI production history. Gallagher's 2019 false positive, the article's own six em dashes and triads, Smith's refusal to abandon em dashes, Clarke's decision to correct her typo, and the possibility of useful introspection all counter simple feature-to-authorship or always-remove rules.

## Matched patterns / rules

- `human-eyes/scripts/patterns.json` and `human-eyes/scripts/grade.py`: B1 `no-ai-vocabulary-clustering`, B3 `no-negative-parallelisms`, B4 `no-forced-triads`, G2 `generic_metaphors` in `human-eyes/scripts/judgement.json`, G3 `no-excessive-lists`, H10 `genre_specific`, C7 `no-em-dashes`, and `overall-signal-stacking`.
- `human-eyes/references/process.md`: preserve argument, stance, genre, factual qualifications, quotations, and deliberate devices; do not make authorship statements.
- `dev/hypotheses.md`: H3 drop detection framing, H24 register-specific vocabulary density, and H25 model-family versus generic-AI residue.
- Focused deterministic evidence on the 21 body paragraphs: C7 flagged six em dashes; B1 was below threshold at two watched terms in the worst paragraph and three in the article; B4 surfaced two candidates while the then-separate #10a density check (retired 2026-07-25 via DR-19G) stayed below its four-candidate threshold; B3 surfaced one candidate (`promises to improve, not everyone is fearful of the future`); sentence-length variance and paragraph-length uniformity were clear. The exact illustrative sentence `It’s not just X, it’s Y.` separately triggered B3. These are surface-only results, not a complete Audit and not authorship evidence.

## Associated hypotheses

- H3: Drop detection framing entirely.
- H24: Register-specific vocabulary density.
- H25: Model-family versus generic-AI residue.
