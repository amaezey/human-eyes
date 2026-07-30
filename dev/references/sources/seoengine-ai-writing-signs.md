# SEO Engine / VRID: Signs of AI Writing

## Metadata

- **URL:** https://vrid.ai/blog/signs-of-ai-writing
- **Author / owner:** VRID, formerly SEOEngine.ai; no individual byline found
- **Published:** 2026-02-11
- **Retrieved:** 2026-07-17
- **Extracted:** 2026-07-17
- **Source type:** vendor/practitioner SEO and writing guide
- **Evidence tier:** Vendor / detector pages
- **Review mode:** update
- **Stable identifier:** none found
- **Version / revision:** current living page after SEOEngine.ai-to-VRID migration, compared with the 2026-05-05 SEOEngine.ai capture
- **Full-text status:** complete
- **Snapshot:** `snapshots/seoengine-ai-writing-signs.md`
- **Extraction method:** HTTP redirect and access check with `curl`; complete Jina Reader Markdown compared across the original SEOEngine URL and current VRID HTTP/HTTPS URLs; current rendered page independently inspected to recover the Jina-omitted Fix 4 heading
- **Snapshot SHA-256:** `6211d8d2a7bfde093dda7944261940862fd0bf9c9fc4174659b2d1cedebb1ea4`
- **Model / corpus scope:** uncited or indirectly cited claims about ChatGPT, Claude, Gemini, GPT-4o, and GPT-5.1 in English web, marketing, academic, formal, technical, and fiction prose; no disclosed article-specific corpus, prompts, model versions, sampling, coding method, comparison group, or validation
- **Access limitations:** direct VRID HTML returned Cloudflare 403 after the original URL redirected there; three Jina routes returned the same article body but omitted the rendered `Fix 4: Kill the Meta-Commentary` heading while retaining its prose. Independent rendered-page inspection supplied that heading. Page chrome and a decorative hero image were omitted.

## Summary

This is a 2026 vendor guide and product-marketing page that asserts 27 surface and higher-level AI-writing signs, gives two comparison tables, makes detector and SEO/AEO claims, and supplies ten editing moves. Its complete retained article body is 5,485 whitespace-delimited words and substantively unchanged after the SEOEngine.ai-to-VRID migration. The sign inventory and examples are useful as dated practitioner candidates and editing prompts, especially where human-eyes can test exact constructions. The page supplies no disclosed primary study of its own, and many frequency, threshold, causal, detector, model, prevalence, ranking, fixability, and product-performance claims are uncited, point to intermediary pages, or exceed what the linked source is described as showing. It cannot establish authorship, severity, a universal threshold, current model behaviour, ranking impact, or whether a pattern can be repaired only through lived experience.

## Main insights

- The article's 27-item inventory spans punctuation and vocabulary, paragraph and list templates, stance and rhythm, vague or repetitive meaning, sensory and personal grounding, citation/provenance failures, assistant/model residue, and formatting leakage.
- Several exact candidates overlap live human-eyes checks, but the article frequently turns a candidate into a universal rule or causal story without a disclosed sample, human baseline, coding definition, or uncertainty.
- The page contains its own counterevidence: clean human writing can be accused of AI use, detector features overlap human academic, technical, and formal prose, most current content may be mixed human/AI work, and model tells change over time.
- Its ten fixes often align with human-eyes editing goals, but blanket word bans, deliberate error injection, invented personal experience, false confidence, and “edit until it passes as human” are not acceptable consequences. Meaning, honest uncertainty, quotations, deliberate rhetoric, and source-grounded facts must survive.
- The model table, 80%/99% detector framing, false-positive rates, prevalence estimates, traffic/citation figures, ranking claims, and VRID performance claims remain indirect or unsupported here and should not be promoted as project evidence.

## Evidence and claims to extract

- **Direct source reviewed:** complete living article at the current VRID URL, retrieved through three Jina Reader routes after the original SEOEngine.ai URL returned an HTTP 301; prior exact 2026-05-05 capture also compared.
- **Method and sample:** vendor checklist and sales article based on asserted “academic research,” editorial experience, and pattern analysis across unspecified “millions” of documents. No article-specific data, instrument, annotation protocol, prompt, sample accounting, model build, release date beyond a few prose references, human comparator, statistical test, or error analysis is disclosed.
- **Direct versus cited evidence:** C01-C38 and C45-C47 are the page's own practitioner assertions, examples, taxonomies, advice, table ratings, and methodology framing; some point to Wikipedia, WHYY, arXiv, Google, Reddit, and vendor pages but do not reproduce primary methods. C39-C44 are detector, search, prevalence, market, and commercial claims that are indirect, self-reported, or unsupported on the page. Focused upstream checks established that arXiv `2502.00000` is invalid, arXiv `2406.07016` is a biomedical-abstract excess-vocabulary study rather than a document blacklist, WHYY reports the 12,000-text Reinhart design and model drift but not all claims inherited here, and the GEO-16 abstract is an observational English B2B SaaS citation study. No claim is a direct empirical result produced by this article.
- **Important limits and counterexamples:** pattern drift, model and register variation, human use of every named surface form, the quoted clean-writing false-positive complaint, detector overlap with non-native, academic, technical, and formal prose, mixed human/AI workflows, missing raw examples, and the Jina/prior-capture omission of the rendered Fix 4 heading all limit transfer. Aggregate or anecdotal claims do not support a document-level authorship verdict.

## Matched patterns / rules

- Deterministic implementations inspected in `human-eyes/scripts/grade.py`: `no-ai-vocabulary-clustering` (B1), `no-forced-triads` (B4), `no-inline-header-lists` (C2), `no-collaborative-artifacts` (D1, folded D3), `no-filler-phrases` (E1), `no-excessive-hedging` (E2), `no-false-concession-hedges` (E3), `no-excessive-lists` (G3), `no-unicode-flair` (G4), `no-section-scaffolding` (G6), `no-placeholder-residue` (H8), `no-signposted-conclusions` (G8), `no-em-dashes` (C7), `no-formulaic-openers` (E8), `no-anaphora` (H14), `sentence-length-variance` (G9), and `vocabulary-diversity` (B5).
- Catalogue/manual patterns inspected: formulaic challenges sections (#6), false ranges (A6), promotional language (A4), generic positive conclusions (E4), forced synesthesia (F3), generic/ungrounded metaphors (G2), tonal uniformity (H3), faux specificity (H6), neutrality collapse (H7), genre-specific manual checks (H10), and manufactured insight (G7).
- Agent-assessment implementations inspected in `human-eyes/scripts/judgement.json`: `structural_monotony`, `tonal_uniformity`, `faux_specificity`, `neutrality_collapse`, `forced_synesthesia`, `generic_metaphors`, `formulaic_parallelism`, `semantic_redundancy`, `underspecified_language`, `vacuous_connection`, and `genre_specific`.
- Process boundary inspected in `human-eyes/references/process.md`: preserve facts, quotations, qualifications, stance, genre, and deliberate choices; do not invent personal detail or certainty; an Audit reports patterns and does not infer authorship.

## Associated hypotheses

- H7 five-check gating plus advisory catalogue: relevant because most claims here are candidates, not validated gates.
- H9 similar-species disambiguation and H12 genre-aware thresholds: required for clean human prose, academic/formal writing, deliberate rhetoric, quotations, and other look-alikes.
- H21 low information density and wrong sentence subject: adjacent to C12 and C22, but still open.
- H24 register-specific vocabulary density and H25 model-family versus generic-AI residue: directly constrain C02, C10, C16, C38, and C43.
- H27 performative profundity and aphoristic closure: already cites this source, but remains advisory and unvalidated.
