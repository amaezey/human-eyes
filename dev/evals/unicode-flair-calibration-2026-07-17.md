# G4 unicode-flair threshold calibration, 2026-07-17

Calibration record for DR-116 (Merrill/WaPo emoji prevalence, `merrill-wapo-chatgpt-clues:C02`). Decision: the calibration was approved 2026-07-17; the proposal was an evaluation with matched genre controls, not a threshold change.

## Question

`no-unicode-flair` fails at 2+ decorative symbols/shortcodes (`minimum_candidates: 2`). The WaPo chart reports that by July 2025, 70 percent of sampled GPT-4o public-share messages contained at least one emoji. Does that figure, plus matched genre controls, justify moving the threshold to 1 or 3?

## Corpus measurement

Candidate counts across the essay corpora (`dev/evals/samples/human-sourced`, n=55; `generated-ai`, n=38):

| Group | any candidates | counts observed |
|---|---|---|
| Human essays | 1 of 55 (2%) | one marketing essay with 4 |
| Generated essays | 2 of 38 (5%) | 11 and 4 |

Emoji are essentially absent from essay prose on both sides. Every nonzero text fires at any threshold from 1 to 4, so the corpus cannot discriminate between thresholds 1, 2, and 3.

## Genre controls

Constructed fixtures in `dev/evals/samples/unicode-flair-controls/`, per the card's required control list (chat, professional prose, UI, checklist, quotation, social):

| Fixture | Genre legitimacy | Candidates | Fires at 1 | at 2 (current) | at 3 |
|---|---|---|---|---|---|
| professional-email | human-legitimate (one 🙂) | 1 | yes | no | no |
| social-post | human-legitimate | 2 | yes | yes | no |
| chat-thread | human-legitimate | 3 | yes | yes | yes |
| ui-copy | legitimate format | 4 | yes | yes | yes |
| quoted-ai-output | human prose quoting AI | 4 | yes | yes | yes |
| checklist | legitimate format | 5 | yes | yes | yes |
| ai-decorated-email | AI-decorated style | 6 | yes | yes | yes |
| ai-decorated-answer | AI-decorated style | 11 | yes | yes | yes |

## Findings

- Threshold 1 adds exactly one new catch across all fixtures and corpora: the single-emoji professional email, a legitimate human use. Strictly worse.
- Threshold 3 spares only the two-emoji social post; both corpora and both AI-decorated fixtures are unchanged. No detection gain, small tolerance gain in a genre the audit does not target.
- The WaPo 70 percent figure measures chat-message prevalence for one model with no human chat baseline, no genre split, and no uncertainty; it cannot anchor a prose-document threshold at any value.
- Chat, checklist, and UI fixtures fire at every threshold from 2 up. That is genre exposure, not threshold error; the audit's input genre is prose documents, and no genre carve-out is proposed here (a context gate would be a separate decision).

## Outcome

This calibration could not test the threshold question. Emoji occur in chat and social text; the library's corpora are essays, which contain almost none of the phenomenon on either side, and the genre fixtures were constructed for this session rather than sampled, so essay-vs-essay comparison was not like-for-like and the fixture table shows mechanics, not rates. Ruling 2026-07-17: threshold stays at `minimum_candidates: 2`, unchanged, as the no-evidence default. A like-for-like answer would need a provenance-labelled social/chat corpus (for example pre-2022 archived human posts against AI posts generated to matched briefs); no such work is currently queued.

## Limits

Genre controls are constructed fixtures, not sampled texts; the essay corpora carry almost no emoji; no chat corpus with known human/AI provenance was available. Re-run if a provenance-labelled chat or social corpus is added to the library.
