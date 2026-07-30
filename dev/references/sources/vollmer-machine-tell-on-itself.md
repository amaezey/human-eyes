# Matthew Vollmer: I Asked the Machine to Tell on Itself

## Metadata

- **URL:** https://matthewvollmer.substack.com/p/i-asked-the-machine-to-tell-on-itself
- **Author / owner:** Matthew Vollmer
- **Published:** 2026-04-24T19:43:23.647Z; Substack metadata says updated 2026-04-24T19:49:27.140Z
- **Retrieved:** 2026-07-17
- **Extracted:** 2026-07-17
- **Source type:** practitioner / teacher essay containing an LLM-generated catalogue and author commentary
- **Evidence tier:** Conduit / catalogue sources
- **Review mode:** update
- **Stable identifier:** Substack post ID 195382258; publication ID 3707068
- **Version / revision:** published post updated 2026-04-24T19:49:27.140Z; prior reviewed Jina capture extracted 2026-05-05
- **Full-text status:** complete
- **Snapshot:** `snapshots/vollmer-machine-tell-on-itself.md`
- **Extraction method:** direct Substack HTML fetched with `curl -L --compressed`; embedded `window._preloads` JSON used for identity, version, and complete `body_html`; body checked against current Jina Reader Markdown and archived prior Jina capture
- **Snapshot SHA-256:** `69661f83a7e0eb998d0a3f55174efb1e1238d02118023c98ce3626799571b6a4`
- **Model / corpus scope:** English-language public Substack post; Vollmer supplied one prompt to Claude and published its 6,185-word field guide, which mixes cited empirical research, journalism, vendor material, practitioner observations, and uncited synthesis; model family is Claude, but the source gives no model name, version, date, settings, system prompt, source-retrieval log, or reproducible generation transcript beyond Vollmer's displayed user prompt
- **Access limitations:** none for the complete public post; the student poem, allegation evidence, Claude conversation metadata, source-retrieval trace, and full bibliographic verification behind the generated field guide are not supplied; one hero image remains linked at the full source URL rather than copied as a binary attachment

## Summary

Vollmer introduces an anecdote about a prize-winning student poem, explicitly says he does not know whether AI use can be proved, and then publishes a Claude-generated field guide requested with one displayed prompt. The guide inventories lexical, syntactic, rhetorical, tonal, formatting, genre, model-fingerprint, computational, detector-limit, cultural, and teaching claims. It is valuable as a discovery map and as a record of a writing teacher using an LLM to synthesize public discourse, but it is not a single empirical study: most evidence belongs to upstream sources of very different strength, several figures and mechanisms are asserted without a reproducible research trail, and the guide itself warns that individual features are human usages rather than proof. The live project already covers many surface families and genre questions, while the most important gaps are epistemic: evidence attribution, model/version drift, human look-alikes, quotation/context handling, and evaluation of the guide's exact three-or-more diagnostic cluster.

## Main insights

- Vollmer's direct contribution is the publication context, displayed prompt, classroom framing, pedagogical exercises, source selection, and coda. The long field guide is explicitly presented as Claude's response.
- The source begins with uncertainty: Vollmer had an intuition about one poem and later heard an allegation, but says he does not know whether anyone can prove AI use. The poem and allegation evidence are absent.
- The generated preamble calls the guide diagnostic rather than a tribunal. It says no single signal is proof, human writers use the named forms, and any signal lies in clustering, density, and texture.
- Stronger inherited evidence includes dated, register-bounded aggregate research such as Kobak's biomedical vocabulary analysis, Juzek and Ward's focal-word study, Walsh's poetry comparison, and Liang's detector-bias study. The guide also mixes in vendor pages, journalism, blogs, forum comments, and uncited model explanations.
- The surface catalogue covers vocabulary clusters; signposting and closing rituals; contrastive negation; triads; low sentence-length variation; vague sentence subjects; trailing participles; essay and section scaffolding; hedging; inflated importance; promotional prose; false concessions; aphoristic endings; vagueness; sycophancy; generic profundity; affective flatness; missing particulars; punctuation and formatting; and genre-specific cues.
- Genre branches include poetry, fiction, student essays, academic writing, journalism, and business email. These are review prompts, not validated universal thresholds.
- The model-fingerprint section is explicitly unstable: it gives ChatGPT, Claude, Gemini, Copilot, DeepSeek, and Perplexity tendencies, then says fingerprints drift and some earlier patterns have already shrunk or disappeared.
- The computational section distinguishes corpus-level or classifier features from individual-document proof, but it also repeats broad detector-mechanism and Turnitin-baseline claims that are not established by this source itself.
- The limits section is material evidence, not an appendix: it covers non-native-English false positives, claimed neurodivergent and tool-user false positives, detector unreliability, weak human performance, mixed human/LLM writing, evasion, and the ethics of accusation.
- The 12-item closing checklist proposes three or more cues within a few hundred words and then makes a near-90% practiced-reader claim. The source does not supply a validation sample, annotation protocol, decision rule, or uncertainty for that exact checklist, so the threshold and accuracy claim must not be adopted.

## Evidence and claims to extract

- **Direct source reviewed:** complete public Substack post at stable post ID 195382258, current direct HTML with embedded full `body_html`, current Jina Markdown, and the exact archived 2026-05-05 Jina snapshot. The current Jina body and prior snapshot differed only in the reader's `http` versus `https` URL header; the direct Substack metadata reports the same published version and no substantive body change.
- **Method and sample:** one displayed user prompt asked Claude to deploy research to identify AI tells while acknowledging that LLM authorship cannot be definitively identified. Vollmer published the response with his own opening anecdote and closing framing. The source supplies no model version, reproducible retrieval trace, citation-check protocol, generated comparison corpus, human control corpus, or independent validation of its taxonomy.
- **Direct versus cited evidence:** C01, C27, and C28 include Vollmer's direct anecdote, cultural selection, pedagogy, and closing interpretation. C02 and C29 are claims made by the generated guide about its own use and aggregate cluster. C03-C26 are predominantly Claude's synthesis of named or unnamed upstream sources plus uncited interpretation. Existing direct source cards and `dev/research/vollmer.md` were used to preserve known attribution corrections, but no inherited claim is promoted as direct evidence merely because it appears here.
- **Important limits and counterexamples:** the student poem and allegation are unavailable; no individual feature proves authorship; human writers deliberately use every named device; fields, genres, prompts, models, and dates differ; model fingerprints drift; the source mixes evidence tiers; the exact checklist is unvalidated; commercial and human detection can fail; non-native, neurodivergent, precise, tool-assisted, and deliberately rhetorical human prose can look similar; mixed authorship is not resolved; and the article's own body triggers many live checks because it quotes or inventories their target forms.

## Matched patterns / rules

- Programmatic overlap inspected in `human-eyes/scripts/grade.py`, not only the rendered catalogue: A1 `no-significance-inflation`; A3 `no-superficial-ing`; A4 `no-promotional-language`; A5 `no-vague-attributions`; B1 `no-ai-vocabulary-clustering`; B2 `no-copula-avoidance`; B3 `no-negative-parallelisms`; B4 triad recognition and density; C1 `no-boldface-overuse`; C2 `no-inline-header-lists`; C5 `no-curly-quotes`; D1 and folded D3 `no-collaborative-artifacts`; E1 `no-filler-phrases`; E2 and E3 hedging and false concession; E4 and G8 conclusion checks; G3 and G4 list and Unicode checks; H2 paragraph endings and uniformity; H4 orphaned demonstratives; G6 section scaffolding; H8 placeholder residue; H9 rubric echoing; H11 corporate register; C7 em dashes; E8 formulaic openers; G9 sentence-length variance; B5 vocabulary diversity; and `overall-signal-stacking`.
- Agent-assessment overlap inspected in `human-eyes/scripts/judgement.json`: tonal uniformity, faux specificity, neutrality collapse, generic metaphors, structural monotony, formulaic parallelism, underspecified language, context leakage, and the polymorphic H10 genre branches for academic, student essay, poetry, fiction, journalism, and marketing email.
- A deterministic body-only audit was run as `python3 human-eyes/scripts/grade.py audit tmp/vollmer/body.md --surface-only --format json`. It reported `coverage_mode: surface_only`, `audit_status: incomplete`, 20 flagged programmatic checks, and aggregate signal stacking 16/4. This proves executable recognition only. The article quotes target phrases and is organized as a catalogue, so the output is not a complete Audit, source-validity test, or authorship result.
- The body-only scan found 82 em dashes; a 19-item worst-paragraph vocabulary cluster; seven negative-parallelism candidates; nine triads; 141 list items across 22 blocks; 98 bold spans; six Unicode candidates; two placeholder examples; and current low-TTR and signal-stacking findings. These are exact runtime results on the source text, not validation of Vollmer's prevalence, causal, or threshold claims.

## Associated hypotheses

- H3: drop detection framing entirely.
- H9: per-pattern disambiguation and human look-alikes.
- H11: manufactured insight is register-coded in long-form essay.
- H12: genre-aware threshold calibration.
- H21: low information density and wrong sentence subject.
- H22: long-tail compression and grammatical standardisation.
- H24: register-specific vocabulary density.
- H25: model-family versus generic-AI residue.
- H26: vague-change intros separate from contrastive negation.
- H27: performative profundity and aphoristic closure.
