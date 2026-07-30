# Robin Sloan: Writing with the machine

## Metadata

- **URL:** https://www.robinsloan.com/notes/writing-with-the-machine/
- **Author / owner:** Robin Sloan
- **Published:** May 2016
- **Retrieved:** 2026-07-17
- **Extracted:** 2026-07-17
- **Source type:** practitioner essay and first-party software demonstration
- **Evidence tier:** Practitioner / teacher / editor essays
- **Review mode:** update
- **Stable identifier:** none found
- **Version / revision:** live first-party HTML retrieved 2026-07-17, with HTTP `Last-Modified: Mon, 13 Jul 2026 15:54:04 GMT`; previous Jina-derived snapshot retrieved 2026-05-05; no page-specific revision ID
- **Full-text status:** complete
- **Snapshot:** `snapshots/sloan-human-ai-writing.md`
- **Extraction method:** direct first-party HTML downloaded with `curl`, complete `<main>` converted to Markdown and checked through a rendered-reader view; three first-party images downloaded and inspected; cited GitHub implementation READMEs and May 2016 commit histories checked for implementation identity and context, but not used as claim evidence
- **Snapshot SHA-256:** `c822ab3c187af1a43deb4cfad11301a0bba94fdd6a4a5599a0bbe6404f3cc38b`
- **Model / corpus scope:** an unspecified recurrent neural network used through `torch-rnn-server` and the Atom `rnn-writer` plugin in May 2016; trained on Sloan's lightly processed approximately 150 MB, 149,326,361-character corpus derived from *Galaxy* and *IF Magazine* scans in the Internet Archive Pulp Magazine Archive; English science-fiction text containing OCR errors and advertisements, normalized into one text file with no line breaks; no model architecture/configuration, sampling settings, prompt log, repeated trials, comparison corpus, or human baseline reported
- **Access limitations:** none for the essay, its three images, or the cited implementation READMEs. The page has no stable revision history; the HTTP `Last-Modified` value is a server-supplied page timestamp, not a content revision ID. The linked code repositories and corpus are contextual external works, not separately ingested evidence records.

## Summary

Robin Sloan's May 2016 first-person essay describes a two-part, on-demand writing tool: an Atom plugin requests inline continuations from a character-level RNN server trained on old science fiction. The direct evidence is a practitioner build report, two selected animated demonstrations, and Sloan's reflection on using the tool. Its useful contribution to human-eyes is bounded process framing: deliberate human control, augmentation rather than outsourcing, and creative difference rather than surface polish. It is not a study of AI-writing tells, modern transformer models, writing quality, authorship, prevalence, or detection, and its strongest result is negative: the shared tools had not yet produced effects worth their effort.

## Main insights

- Sloan describes a user-initiated call-and-response workflow: the writer presses `tab` to request a suggestion and can work with the RNN's output inside the editor. Exact accept/reject key mappings appear only in the separately accessed current `rnn-writer` README and are not claim evidence here.
- The two GIFs are selected demonstrations rather than a sample. They show locally coherent and strange science-fiction continuations, but provide no output log, rejected-output inventory, rate, comparison, or evaluation criterion.
- Sloan reports an initially deflating first hour and a later, qualified improvement in his view of the tool. He immediately generalises the disappointment as “an unavoidable emotional waystation in any project, and possibly a crucial one”; this is author interpretation from one experience, not a measured usability, quality, or project-development result.
- He rejects the goal of an editor that “writes for you” and instead names augmentation, partnership, and call and response. His goal is harder and different writing, including stranger effects, rather than easier or generically better text.
- He states that the tools do not achieve that goal because their effects do not yet compensate for the effort required. His forward-looking claim that they could get there is explicitly speculative.
- In this experiment, Sloan says corpus collection and processing mattered more than RNN design and training. The corpus was large, genre-specific, lightly normalized into one text file with no line breaks, and noisy with OCR errors and advertisements; he also says the RNN “seems to thrive on that,” a subjective observation with no metric or ablation.
- Sloan's praise of a clear-explanation culture is partly inherited: the causal importance claim belongs to an unnamed friend, and Sloan calls it reasonable based on his experience. The linked Karpathy essay, Udacity course, and Goodwin essay are examples he found useful, not evidence reviewed here for a human-eyes rule.

## Evidence and claims to extract

- **Direct source reviewed:** complete first-party live HTML of “Writing with the machine,” retrieved 2026-07-17; all 33 article `p` elements, three `h2` sections, two lists with five items, and three images were preserved or represented in the snapshot. The current first-party body is text-equivalent to the archived 2026-05-05 Jina capture after packaging and HTML layout normalization.
- **Method and sample:** first-person practitioner account of one 2016 tool build and the author's use of it; two selected animated demonstrations; unspecified RNN configuration; English science-fiction corpus of approximately 150 MB and 149,326,361 characters; no controlled prompt set, repetitions, blind assessment, human comparison, quantitative outcome, or present-day model.
- **Direct versus cited evidence:** C01-C06 are Sloan's direct implementation descriptions, selected examples, observations and interpretation, goals, negative result, and corpus report. C07 combines Sloan's direct assessment with an unnamed friend's causal claim and three linked resources; the causal part is indirect and unresolved. The separately accessed current GitHub READMEs corroborate the two-part tool identity and expose additional interaction details, and their APIs expose contemporaneous May 2016 commits. Those live repository pages were not version-pinned or preserved, so none of their added details is used as claim evidence.
- **Important limits and counterexamples:** the initial disappointment, the explicit failure to reach the stated goal, the effort-cost qualification, and the noisy corpus all constrain positive process claims. The GIFs are cherry-picked demonstrations. No claim supports a surface tell, severity, threshold, model-general tendency, quality score, authorship inference, or requirement that assisted writing be harder or stranger.

## Matched patterns / rules

- `human-eyes/references/voice.md`, “Preserve the source” and “Preserve deliberate form”: partly covers C04 by retaining distinctive choices, unusual phrases, form, and images.
- `human-eyes/references/process.md`, “Plan the edit” and “Preserve meaning”: partly covers C04 by protecting stance, genre, point of view, and deliberate devices.
- `human-eyes/scripts/judgement.json`, `genre_specific.fiction`: adjacent only; it asks about surprise, revision depth, voice differentiation, and fidelity that misses a source author's oddities, but it does not evaluate collaborative process and Sloan does not validate that assessment.
- `dev/references/sources/pattern-opportunities.md`, “Audience, intent, and choice as positive voice criteria” and “Pure framing essays as pattern evidence”: directly records the process-guidance and non-promotion boundaries, but its Sloan mapping needs the claim IDs added by this refresh.
- No entry in `human-eyes/scripts/patterns.json` or generated `human-eyes/references/patterns.md` implements Sloan's process framing, and this source does not justify adding one.

## Associated hypotheses

- None directly supported. The previous card's H3 and H8 mappings were too broad: Sloan offers optional creative-process framing, not evidence that detector positioning should be dropped (H3) or that audit and rewrite invocation surfaces need separate voices (H8).
