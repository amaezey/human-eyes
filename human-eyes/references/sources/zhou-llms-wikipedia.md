# Zhou, Cho, and Terveen: LLMs in Wikipedia

## Metadata

- **URL:** https://arxiv.org/abs/2509.07819
- **Authors:** Moyan Zhou, Soobin Cho, and Loren Terveen
- **Published:** 2025-09-09
- **Extracted:** 2026-07-14
- **Source type:** Qualitative empirical study of Wikipedia editors
- **Evidence tier:** Academic preprint / semi-structured interviews
- **Extraction status:** reviewed from complete saved PDF text
- **Full text snapshot:** `snapshots/zhou-llms-wikipedia.md`

## Study design

- Semi-structured interviews with 16 Wikipedia editors who had used LLMs during editing.
- Includes newcomers and experienced editors with different contribution volumes and editing frequencies.
- Every participant listed ChatGPT; several also listed Gemini, Grok, Claude, Perplexity, Microsoft Copilot, or other tools.
- The study examines content contribution, conformity to community norms, and other editors' responses.

## Direct prose and sourcing observations

- Editors observed overly positive and promotional output, including `it's one of the best` and `there are so many possibilities`.
- Editors reported unreliable commercial sources, missing sources, hallucinated facts, and fabricated references.
- Participants described neutralising tone, heavily editing output, repairing wikitext and links, and checking every word for verifiability.
- The paper names three recurring editorial strategies: **evaluation, verification, and modification**.
- Newcomers sometimes use LLMs to draft whole articles or fill knowledge gaps before they have developed the editorial judgment needed to filter the output.
- Experienced editors more often adapt or reject suggestions using accumulated knowledge of policies, genre, and context.

## Direct workflow and design recommendations

The authors recommend three forms of support:

1. **Scaffold participation through incremental guidance:** break complex article creation into source finding, summarising, and structuring rather than returning a complete draft immediately.
2. **Teach community norms through interaction:** highlight problematic passages, provide acceptable and unacceptable examples, and ask questions that require editors to evaluate the output.
3. **Adapt to user expertise:** give newcomers more guided, stepwise assistance while allowing experienced editors more direct control.

## Project incorporation

- **#4 promotional language — adds direct evidence and examples:** editors observed overly positive language, `it's one of the best`, `there are so many possibilities`, and unsupported `puffery peacock terms`.
- **#5/#41 source review — expands the Wikipedia branch:** check for no source, click-driven commercial sources presented as reliable evidence, invented facts, invented references, and citations that do not support the claim.
- **#41 Wikipedia formatting — adds a new genre-specific failure group:** check mistranslated or broken wikilinks, references, and wikitext. This is what `source/markup failure` means here; it is concrete Wikipedia formatting and citation damage, not an abstract authorship signal.
- **Audit/rewrite process — guidance, not a tell:** `evaluate, verify, modify` means judge whether the suggestion improves the writing, check every factual claim and source, and then repair tone, text, links, references, and wikitext. It should not be presented as evidence that a text is human.
- **Interaction-design context — future guidance, not a prose check:** incremental help and different support for newcomers and experienced editors may matter if human-eyes later develops a guided Wikipedia workflow.
- This paper does **not** establish the formulaic Wikipedia discussion replies or boilerplate Wikipedia user profiles catalogued on Wikipedia's own guidance pages. Those observations must not be attributed to Zhou et al.

## Recommendations for human-eyes

1. Add the direct promotional examples and `puffery peacock terms` to #4's evidence/examples.
2. Expand #41's Wikipedia branch with missing, unreliable, fabricated, and non-supporting sources and references.
3. Add broken or mistranslated wikilinks, references, and wikitext as Wikipedia-specific formatting failures.
4. Record evaluate–verify–modify as possible audit/rewrite process guidance, not as a writing tell.
5. Preserve the three design recommendations for any future guided-workflow work.
6. Preserve the 16-editor sampling frame and participant tool table when discussing model usage.

These are recommendations from the direct source. No checker, assessment registry, process file, or fixture was changed as part of this source-card work.

## Matched patterns / rules

- #4 promotional language
- #5 vague/unreliable attribution context
- #19 context and workflow residue
- #37 neutrality / positive-tone correction
- #41 genre-specific provenance and citation review

## Associated hypotheses

- H9 similar-species and process disambiguation
- H12 genre-aware threshold calibration
- H25 model-family and workflow context
