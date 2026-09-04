#!/usr/bin/env python3
"""Deterministic Detection data for every pattern (owner ruling 2026-08-24).

One rule, one rendering: behaviour shared between checks is emitted by one
family generator, so identical logic always reads identically on every
page. Hand input is limited to the irreducible per-check fragments (what
the counted thing is). The output is consumed by the app build, the
and the copy gates: every surface renders from this
module and nothing else.

Line syntax, resolved downstream:
  {setting}          a named number from CHECK_THRESHOLDS; the build fails
                     on a name the table does not hold
  `literal`          text the check matches literally; rendered as a chip
  @trigger-phrases   the named set on the page; rendered as a chip-styled
                     link reading "trigger phrase"
  @source[slug]      a chip-styled link straight to the named evidence
                     card's page, reading as the card's short title
                     ("Kobak et al."); the slug must be one of that
                     pattern's card references
  @list[NAME]        a word list extracted from grade.py (MANIFEST), spelled
                     out in full as sorted chips at build time; NAME must be
                     a constant grade.py defines
  pattern ids        A3, G7, S1 and the like render as links to their
                     pattern pages

Conditions follow the spec grammar: quantity, subject, qualifiers. An
`unless` list binds to its condition, never to the check. In an all-of
check a check-wide carve-out is a negated condition row, not an unless.

Definitions never sit inline in a condition line (owner rulings
2026-08-24): each check carries a top-level `definitions` list, one
"term = definition" row per term, rendered as a Definitions block at the
top of the card's Detection section; defined terms in condition lines
render as links to it, the way trigger phrases do. Definitions hold
definitions only — anything negatively phrased or exemption-shaped is an
`unless` row on its condition, in the plus-expansion. The condition line
itself stays quantity + subject + scope.
"""

import json
import re
from pathlib import Path

SCRIPTS_DIR = Path(__file__).resolve().parent
GRADE_PATH = SCRIPTS_DIR / "grade.py"
PATTERNS_PATH = SCRIPTS_DIR / "patterns.json"

# Fixed wordings for shapes many checks share. Never restate these inline;
# shared shapes are constructed only by the family generators below, keeping
# their wording canonical across every registry entry that uses them.
#
# The comparator lexicon — one rendering per comparison, everywhere:
#   at or above N   ->  "{key}+" / "`N+`"      (never "or more", "at least")
#   below N         ->  "under {key}"           (never "less than")
#   at or below N   ->  "{key} or under"      (never "at most", "up to")
# Recurring scopes: "in one sentence", "in one paragraph", "sentences in a
# row" (never "consecutive"). No scope phrase means the whole text — the
# fillers "across the document", "anywhere in the text", and "repeats
# counted" are banned as redundant (owner ruling 2026-08-24): a count
# always counts every occurrence, and a line says "different" or "word
# families counting as one" in the rare cases distinctness matters.
GATE_TEXT_WORDS = "text of {minimum_words}+ words"
GATE_SENTENCES = "{minimum_sentences}+ sentences"
RATE_UNIT = "per `1,000` words"

SKIP_LABELS = ("front matter", "code", "web addresses", "quoted text")

AGENT_CONDITION = "the reviewing agent judges the pattern present · no fixed rule"


# --------------------------------------------------------------------------
# Families. A family is a function from a spec entry to the condition list
# and mode. Same family, same skeleton, always.

def _family_biber_rate(entry):
    first = {"line": "{minimum_candidates}+ " + entry["subject"]}
    if "unless" in entry:
        first["unless"] = entry["unless"]
    article = entry.get("article", "a")
    return {
        "mode": "all",
        "conditions": [
            first,
            {
                "line": (
                    article + " " + entry["subject_short"] + " rate of "
                    "{maximum_rate_per_1000}+ " + RATE_UNIT
                )
            },
            {"line": GATE_TEXT_WORDS},
        ],
    }


def _family_document_count(entry):
    # N or more matches, whole text (the default scope), every occurrence
    # counted (the default counting rule).
    return {
        "mode": "any",
        "conditions": [
            {
                "line": "{minimum_candidates}+ " + entry["subject"],
                **({"unless": entry["unless"]} if "unless" in entry else {}),
            },
        ],
    }


def _family_list_match(entry):
    # The check fails on the first match from its own phrase list. One
    # shape, one wording, for every such check.
    return {"mode": "any", "conditions": [{"line": "`1+` @trigger-phrases"}]}


def _family_bespoke(entry):
    return {"mode": entry["mode"], "conditions": entry["conditions"]}


FAMILIES = {
    "biber_rate": _family_biber_rate,
    "document_count": _family_document_count,
    "list_match": _family_list_match,
    "bespoke": _family_bespoke,
}


# --------------------------------------------------------------------------
# The per-check table. Every check-owning record must appear here; the
# emitter fails on a missing or surplus id. Bespoke entries carry their
# whole condition set; family entries carry only their fragments.

DETECTION = {
    # ---- Biber / Xia feature rates (one family, six checks) -------------
    "no-nominalisation-rate": {
        "family": "biber_rate",
        "subject": "nominalisations",
        "subject_short": "nominalisation",
        "definitions": [
            "a nominalisation = a word with a stem of `4+` letters before "
            "one of the endings `tion`, `ment`, `ness`, `ity`, `ance`, or "
            "`ence`, singular or plural; `ness` in the singular only"
        ],
    },
    "no-that-relative-rate": {
        "family": "biber_rate",
        "subject": "subject relatives",
        "subject_short": "subject-relative",
        "definitions": [
            "a subject relative = a word plus `that`, the `that` "
            "standing as subject of the verb straight after it"
        ],
        "unless": [
            "the word before `that` is one of "
            "@list[REL_COMPLEMENT_HEADS]",
        ],
    },
    "no-participial-clause-rate": {
        "family": "biber_rate",
        "subject": "participial clauses",
        "subject_short": "participial-clause",
        "definitions": [
            "a participial clause = an `-ing` clause joined to a main "
            "sentence at its start with a comma after it, after a `,` or "
            "`;`, or after `while`, `when`, `before`, `after`, `since`, "
            "`by`, `through`, `without`, `despite`, `besides`, or `upon`",
        ],
        "unless": [
            "the `-ing` word is one of @list[PARTICIPIAL_STOPWORDS]",
        ],
    },
    "no-passive-voice-rate": {
        "family": "biber_rate",
        "subject": "passive verbs",
        "subject_short": "passive-verb",
        "definitions": [
            "a passive verb = a form of `be` plus a past participle",
        ],
        "unless": [
            "the participle is one of "
            "@list[PASSIVE_ADJECTIVE_EXCLUSIONS]",
        ],
    },
    "no-it-pronoun-rate": {
        "family": "biber_rate",
        "subject": "occurrences of the word `it`",
        "subject_short": "`it`",
        "article": "an",
    },
    "no-latinate-verb-rate": {
        "family": "biber_rate",
        "subject": "@trigger-phrases, in any form",
        "subject_short": "trigger-phrase",
    },

    # ---- First-match list checks (one family) ---------------------------
    "no-significance-inflation": {"family": "list_match"},
    "no-notability-claims": {"family": "list_match"},
    "no-promotional-language": {"family": "list_match"},
    "no-vague-attributions": {
        "family": "list_match",
        "shape_chips": ["some critics"],
    },
    "no-collaborative-artifacts": {"family": "list_match"},
    "no-knowledge-cutoff-disclaimers": {
        "family": "list_match",
        "shape_chips": ["specific details about X are limited"],
    },
    "no-formulaic-social-posts": {"family": "list_match"},
    "no-filler-phrases": {"family": "list_match"},
    "no-false-concession-hedges": {
        "family": "list_match",
        "shape_chips": ["while critics argue X, supporters maintain Y"],
    },
    "no-dramatic-transitions": {"family": "list_match"},
    "no-manufactured-insight": {"family": "list_match"},
    "no-placeholder-residue": {"family": "list_match"},
    "no-corporate-ai-speak": {"family": "list_match"},
    "no-nonliteral-land-surface": {
        "family": "list_match",
        "shape_chips": [
            "the argument landed on X",
            "where I landed on X",
            "the framework, as if it were a map",
        ],
    },
    "no-performed-candour": {"family": "list_match"},

    # ---- Document-wide list counts (one family) -------------------------
    "no-ghost-spectral-density": {
        "family": "document_count",
        "subject": "@trigger-phrases",
    },
    "no-quietness-obsession": {
        "family": "document_count",
        "subject": "@trigger-phrases",
    },
    "no-excessive-hedging": {
        "family": "document_count",
        "subject": "@trigger-phrases",
    },
    "no-rubric-echoing": {
        "family": "document_count",
        "subject": "@trigger-phrases",
    },
    "no-bland-critical-template": {
        "family": "document_count",
        "subject": "@trigger-phrases",
    },
    "no-orphaned-demonstratives": {
        "family": "document_count",
        "subject": (
            "`this`, `that`, `these`, or `those` followed straight by "
            "@trigger-phrases"
        ),
    },
    "no-unicode-flair": {
        "family": "document_count",
        "subject": (
            "decorative characters: any emoji, one of `✓` `✔` `✕` `✖` "
            "`×` `★` `☆` `◆` `◇` `→` `⇒` `➜` `➤` `•` `●` `○` `◦` `※` "
            "`✨` `⭐` `✅` `❌` `🔥` `🚀` `⚡` `➡` `♻`, a run of letters "
            "or digits from Unicode's styled alphabets, or a short name "
            "wrapped in `:` marks, all counted together"
        ),
    },

    # ---- Feature rates joining the biber_rate family --------------------
    "no-forced-triads": {
        "family": "biber_rate",
        "subject": (
            "three-part lists, each `3` matched items, phrases, or "
            "clauses joined by commas and a closing `and` or `or`, a "
            "clause plus a `which` clause split by `and` or `or` counting "
            "with them"
        ),
        "subject_short": "three-part-list",
        "shape_chips": ["when X, how Y, and what Z"],
    },
    "no-negation-density": {
        "family": "biber_rate",
        "subject": "@trigger-phrases",
        "subject_short": "trigger-phrase",
    },

    # ---- Bespoke shapes -------------------------------------------------
    "no-negative-parallelisms": {
        "family": "bespoke",
        "mode": "any",
        "shape_chips": [
            "is X, rather than Y",
            "a question of X, rather than Y",
            "beyond X, it is Y",
            "in reality, it is X",
            "it isn't about X. It's about Y",
            "it isn't just X; it's Y",
            "it isn't X; it's Y",
            "it isn't X, it's Y",
            "it isn't X. It's Y",
            "the team wasn't X. The team was Y",
            "the team wasn't X. It was Y",
            "we aren't X, we're Y",
            "the brand isn't just X, it's Y",
            "you're not X, you're Y",
            "it's not X, it's Y",
            "they aren't X, they're Y",
            "you aren't X, you're Y",
            "she wasn't X, she was Y",
            "he wasn't X, he was Y",
            "it wasn't X, it was Y",
            "the whole plan wasn't X. It was Y",
            "because the plan wasn't X, it was Y",
        ],
        "conditions": [
            {
                "line": "`1+` @trigger-phrases",
                "unless": ["the match overlaps one already counted"],
            },
        ],
    },
    "no-ai-vocabulary-clustering": {
        "family": "bespoke",
        "mode": "any",
        "conditions": [
            {
                "line": (
                    "{minimum_cluster_terms}+ @trigger-phrases in one "
                    "paragraph"
                )
            },
            {
                "line": (
                    "{minimum_term_families}+ different words among "
                    "`underscore` `delve` `showcase` `unveil` `intricate` "
                    "`meticulous` `pivotal` `heighten` `nuance` `bolster` "
                    "`foster` `interplay`, in any form"
                )
            },
        ],
    },
    "no-copula-avoidance": {
        "family": "bespoke",
        "mode": "any",
        "conditions": [
            {"line": "`1+` @trigger-phrases"},
            {
                "line": (
                    "a first sentence of the first paragraph starting with "
                    "`The` plus `term`, `phrase`, `name`, `concept`, "
                    "`expression`, or `designation`, or with a capitalised "
                    "name of `1` to `5` words, with `refers to` or "
                    "`refer to` straight after either start"
                )
            },
        ],
    },
    "vocabulary-diversity": {
        "family": "bespoke",
        "mode": "all",
        "definitions": [
            "vocabulary-diversity score = the share of distinct words "
            "inside a window of {window_words} words, the window "
            "shrinking to the text when the text is shorter, averaged as "
            "the window moves through the text; higher means fewer words "
            "repeat",
        ],
        "conditions": [
            {"line": "a vocabulary-diversity score of {minimum_mattr}+"},
            {"line": "text of {minimum_words}+ words"},
        ],
    },
    "no-mixed-spelling-conventions": {
        "family": "bespoke",
        "mode": "all",
        "shape_chips": [
            "apologize",
            "apologise",
            "color",
            "colour",
        ],
        "conditions": [
            {"line": "`1+` @trigger-phrases spelled the British way"},
            {"line": "`1+` @trigger-phrases spelled the American way"},
        ],
    },
    "word-length-average": {
        "family": "bespoke",
        "mode": "all",
        "conditions": [
            {
                "line": (
                    "an average word length of {maximum_mean_characters}+ "
                    "characters"
                )
            },
            {"line": "text of {minimum_words}+ words"},
        ],
    },
    "concreteness-average": {
        "family": "bespoke",
        "mode": "all",
        "definitions": [
            "average concreteness = the `1`-to-`5` rating of every word "
            "found in @source[brysbaert-concreteness-norms]'s published "
            "concreteness list, averaged; lower means the words stay "
            "abstract",
            "a small grammar word = an everyday connecting word, one of "
            "@list[CONCRETENESS_STOPWORDS]",
        ],
        "conditions": [
            {
                "line": (
                    "an average concreteness of "
                    "{maximum_mean_concreteness} or under"
                ),
                "unless": ["the word is a small grammar word"],
            },
            {"line": "text of {minimum_words}+ words"},
        ],
    },
    "no-boldface-overuse": {
        "family": "bespoke",
        "mode": "all",
        "definitions": [
            "a bold span = a stretch of text of "
            "{maximum_bold_span_characters} characters or under, wrapped "
            "in `**`",
        ],
        "conditions": [
            {
                "line": "{minimum_candidates}+ bold spans",
                "unless": [
                    "the span sits on a line starting with `-`, `*`, `+`, "
                    "or `•`, a number and `.`, or `#` marks",
                ],
            },
            {
                "line": (
                    "a bold-span rate of {maximum_rate_per_1000}+ "
                    + RATE_UNIT
                )
            },
        ],
    },
    "no-inline-header-lists": {
        "family": "bespoke",
        "mode": "any",
        "definitions": [
            "a bold label = a stretch of text of "
            "{maximum_label_characters} characters or under, wrapped in "
            "`**`, ending with `:` just inside or just after the closing "
            "`**`",
        ],
        "conditions": [
            {
                "line": (
                    "{minimum_candidates}+ bold labels on lines starting "
                    "with a bullet or a number, or on lines holding "
                    "{minimum_labels_per_line}+ bold labels"
                )
            },
        ],
    },
    "no-title-case-headings": {
        "family": "bespoke",
        "mode": "any",
        "conditions": [
            {
                "line": (
                    "`1+` headings marked with `#`, of "
                    "{minimum_heading_words}+ words, holding `1+` "
                    "@trigger-phrases that start with a capital letter "
                    "and sit between the heading's first and last words"
                ),
                "unless": ["the word just before it ends with `:`"],
            },
        ],
    },
    "no-curly-quotes": {
        "family": "bespoke",
        "mode": "any",
        "conditions": [
            {"line": "`1+` of the curly quote marks `“` `”` `‘` `’`"},
        ],
    },
    "no-compound-modifier-density": {
        "family": "bespoke",
        "mode": "any",
        "conditions": [
            {
                "line": (
                    "{minimum_per_sentence}+ @trigger-phrases in one "
                    "sentence holding a `-`"
                )
            },
        ],
    },
    "no-em-dashes": {
        "family": "bespoke",
        "mode": "any",
        "conditions": [
            {"line": "`1+` em dashes"},
        ],
    },
    "no-parenthetical-headings": {
        "family": "bespoke",
        "mode": "any",
        "conditions": [
            {
                "line": (
                    "`1+` headings marked with `#`, containing text in "
                    "parentheses"
                )
            },
            {
                "line": (
                    "`1+` headings underlined with a row of `=` or `-` "
                    "signs, containing text in parentheses"
                )
            },
        ],
    },
    "no-mixed-script-words": {
        "family": "bespoke",
        "mode": "any",
        "conditions": [
            {
                "line": (
                    "`1+` words holding both a Latin letter and a Cyrillic "
                    "or Greek letter shaped exactly like a Latin one"
                )
            },
        ],
    },
    "no-generic-conclusions": {
        "family": "bespoke",
        "mode": "any",
        "conditions": [
            {"line": "`1+` @trigger-phrases"},
            {
                "line": (
                    "a last sentence of the text ending with `!`, of "
                    "{maximum_final_sentence_words} words or under"
                ),
                "unless": [
                    (
                        "its first word is `i`, `we`, `you`, `it`, `this`, "
                        "`that`, `these`, `those`, `the`, `a`, `an`, "
                        "`there`, `what`, `how`, `my`, `our`, `your`, "
                        "`he`, `she`, or `they`"
                    ),
                ],
            },
        ],
    },
    "no-soft-scaffolding": {
        "family": "bespoke",
        "mode": "any",
        "definitions": [
            "a report-style entry = a paragraph starting with one of "
            "`5` shapes: `a` or `another`, then maybe `major`, `key`, or "
            "`important`, then `priority`, `area`, `theme`, or `focus`, "
            "then maybe `of work`, then `was` or `is` · `the`, then "
            "`body`, `organisation`, `organization`, `team`, "
            "`committee`, or `agency`, then `also`, then `considered`, "
            "`examined`, `reviewed`, or `focused on` · `regional`, "
            "`international`, `community`, or `industry`, then "
            "`participation remained` · `throughout the`, then `year`, "
            "`reporting period`, or `period`, then a `,` · `in`, then a "
            "four-digit year and a `,`, then `the` plus one of the same "
            "body words or `we`, then `will`",
        ],
        "shape_chips": ["first, we'll look at X"],
        "conditions": [
            {
                "line": (
                    "{minimum_candidates}+ @trigger-phrases, report-style "
                    "entries counting with them"
                ),
                "unless": [
                    "a report-style entry past the first in one paragraph",
                ],
            },
        ],
    },
    "no-formulaic-openers": {
        "family": "bespoke",
        "mode": "any",
        "conditions": [
            {
                "line": (
                    "`1+` @trigger-phrases at the start of a paragraph"
                )
            },
        ],
    },
    "no-modal-stacks": {
        "family": "bespoke",
        "mode": "any",
        "conditions": [
            {
                "line": (
                    "{minimum_per_sentence}+ @trigger-phrases in one "
                    "sentence, the lowercase word `may` counting with them"
                )
            },
        ],
    },
    "no-rhetorical-questions": {
        "family": "bespoke",
        "mode": "all",
        "definitions": [
            "a question word = `who` `whom` `whose` `what` `when` "
            "`where` `why` `how` `which`",
            "a helping verb = `am` `is` `are` `was` `were` `do` `does` "
            "`did` `have` `has` `had` `can` `could` `will` `would` "
            "`shall` `should` `may` `might` `must`, with or without "
            "`n't`",
        ],
        "conditions": [
            {
                "line": (
                    "{minimum_candidates}+ questions of "
                    "{maximum_prompt_words} words or under, a question "
                    "running from the text's start, a `.`, or a `!` to "
                    "the next `?`"
                )
            },
            {
                "line": (
                    "the question's first word is not a question word or "
                    "a helping verb, a leading `and`, `but`, or `so` "
                    "skipped first"
                )
            },
            {
                "line": (
                    "the sentence right after the `?` is of "
                    "{maximum_answer_words} words or under"
                )
            },
        ],
    },
    "no-excessive-lists": {
        "family": "bespoke",
        "mode": "any",
        "definitions": [
            "a list-item line = a line starting with `-`, `*`, or a "
            "number and `.`, then a space",
        ],
        "conditions": [
            {
                "line": (
                    "list-item lines making up {minimum_line_ratio}+ of "
                    "all lines, blank lines counted"
                ),
            },
            {
                "line": (
                    "{minimum_items}+ list-item lines spread over "
                    "{minimum_blocks}+ separate runs of list-item lines, "
                    "a run broken only where a line of ordinary text "
                    "comes between"
                )
            },
        ],
    },
    "no-section-scaffolding": {
        "family": "bespoke",
        "mode": "any",
        "conditions": [
            {
                "line": (
                    "{minimum_repeats}+ appearances of the same line of "
                    "under {maximum_label_characters} characters, matched "
                    "with capital letters and leading `#` marks ignored"
                ),
                "unless": [
                    "the line is nothing but punctuation or markdown marks",
                ],
            },
            {
                "line": (
                    "`1+` headings placed right after a line of `3+` `-`, "
                    "`*`, or `_` marks, with only blank lines between"
                )
            },
            {"line": "a first heading of `3+` leading `#` marks"},
            {
                "line": (
                    "`1+` headings with `2+` more leading `#` marks than "
                    "the heading before them"
                )
            },
        ],
    },
    "no-signposted-conclusions": {
        "family": "bespoke",
        "mode": "any",
        "conditions": [
            {
                "line": (
                    "`1+` @trigger-phrases at the start of a paragraph "
                    "or heading"
                )
            },
        ],
    },
    "sentence-length-variance": {
        "family": "bespoke",
        "mode": "all",
        "definitions": [
            "sentence-length variation = how widely the sentences' word "
            "counts spread around their average; lower means the "
            "sentences are more alike",
        ],
        "conditions": [
            {
                "line": (
                    "a sentence-length variation of {minimum_stdev} or under"
                )
            },
            {"line": GATE_SENTENCES},
            {"line": GATE_TEXT_WORDS},
        ],
    },
    "no-heading-one-liners": {
        "family": "bespoke",
        "mode": "any",
        "conditions": [
            {
                "line": (
                    "{minimum_candidates}+ headings each followed by a "
                    "paragraph of one line holding exactly one sentence"
                ),
                "unless": [
                    (
                        "the paragraph after the heading starts with a "
                        "`#` heading mark, a list mark, or a `>` quote "
                        "mark"
                    ),
                ],
            },
        ],
    },
    "no-symmetric-list-items": {
        "family": "bespoke",
        "mode": "all",
        "definitions": [
            "middle count = the count sitting in the middle when the "
            "items are sorted by length",
        ],
        "conditions": [
            {"line": "{minimum_items}+ items in one list"},
            {
                "line": (
                    "every item's word count within {maximum_deviation} "
                    "words of the list's middle count"
                )
            },
            {
                "line": (
                    "the same first word on every item in the list, or the "
                    "same last word on every item, matched with capital "
                    "letters and punctuation ignored"
                )
            },
        ],
    },
    "paragraph-length-uniformity": {
        "family": "bespoke",
        "mode": "all",
        "definitions": [
            "paragraph-length variation = the spread of paragraph word "
            "counts divided by their average, measured only over "
            "paragraphs of {minimum_paragraph_words}+ words; lower means "
            "the paragraphs are more alike",
        ],
        "conditions": [
            {
                "line": "a paragraph-length variation under {maximum_cv}",
            },
            {
                "line": (
                    "{minimum_paragraphs}+ paragraphs of "
                    "{minimum_paragraph_words}+ words each, headings not "
                    "counted"
                )
            },
        ],
    },
    "no-countdown-negation": {
        "family": "bespoke",
        "mode": "any",
        "definitions": [
            "a subject word = `you` `we` `they` `people`",
            "a negated verb = `can't` `won't` `don't` `shouldn't` "
            "`couldn't` `cannot` `will not` `do not` `should not` "
            "`could not`",
        ],
        "conditions": [
            {
                "line": (
                    "{minimum_negations}+ sentences in a row of `it`, "
                    "`this`, or `that` plus `wasn't`, `isn't`, `was not`, "
                    "or `is not`, then a sentence of `it`, `this`, or "
                    "`that` plus `was` or `is`"
                )
            },
            {
                "line": (
                    "{minimum_run}+ sentences in a row starting with the "
                    "same subject word plus a negated verb"
                )
            },
        ],
    },
    "no-tidy-paragraph-endings": {
        "family": "bespoke",
        "mode": "all",
        "conditions": [
            {
                "line": (
                    "{minimum_candidates}+ paragraphs whose last sentence "
                    "is any of"
                ),
                "any": [
                    {"line": "a sentence holding a @trigger-phrase"},
                    {
                        "line": (
                            "a sentence of {tidy_minimum_sentence_words} "
                            "to {tidy_maximum_abstract_sentence_words} "
                            "words starting with `the`, `this`, `that`, "
                            "`it`, `these`, or `those`, then within `4` "
                            "words a form of `be`, `become`, or `remain`, "
                            "then `already`, `itself`, `themselves`, "
                            "`in itself`, or `in themselves`, then within "
                            "`3` words an abstract noun: a word ending in "
                            "`tion`, `sion`, `ment`, `ness`, `ity`, "
                            "`ance`, `ence`, `ship`, or `ism`, or one of "
                            "`argument` `choice` `reading` `claim` "
                            "`lesson` `thesis` `verdict` `metaphor` "
                            "`symbol` `myth` `fiction` `proof` `warning` "
                            "`refinement`"
                        )
                    },
                    {
                        "line": (
                            "a sentence of {tidy_minimum_sentence_words} "
                            "to {tidy_maximum_balanced_sentence_words} "
                            "words split by `;` into two clauses of "
                            "{tidy_minimum_clause_words} to "
                            "{tidy_maximum_clause_words} words, each with "
                            "a subject of `1` to `5` words then a form of "
                            "`be`, `become`, `remain`, `seem`, `mean`, "
                            "`mark`, `sound`, `feel`, or `look`"
                        ),
                        "unless": [
                            (
                                "a `;` clause has `if`, `when`, "
                                "`because`, `while`, `although`, "
                                "`unless`, `where`, `after`, or `before` "
                                "before its verb"
                            ),
                        ],
                    },
                ],
            },
            {
                "line": (
                    "a matching-last-sentence rate of "
                    "{maximum_rate_per_1000}+ " + RATE_UNIT
                )
            },
        ],
    },
    "no-this-chains": {
        "family": "bespoke",
        "mode": "any",
        "conditions": [
            {
                "line": (
                    "{minimum_run}+ sentences in a row inside one "
                    "paragraph, each starting with `this` plus another "
                    "word"
                ),
                "unless": ["the word after `this` is `is`"],
            },
        ],
    },
    "no-anaphora": {
        "family": "bespoke",
        "mode": "any",
        "conditions": [
            {
                "line": (
                    "{minimum_run}+ sentences in a row starting with the "
                    "same word"
                ),
                "unless": [
                    "the shared word is `i`, `a`, `the`, `it's`, or `it`",
                ],
            },
        ],
    },
    "no-paragraph-anaphora": {
        "family": "bespoke",
        "mode": "any",
        "conditions": [
            {
                "line": (
                    "{minimum_run}+ paragraphs in a row starting with the "
                    "same word, counting only prose paragraphs, not "
                    "headings, list items, or quote lines"
                ),
                "unless": [
                    "the shared word is `i`, `a`, `the`, `it's`, or `it`",
                ],
            },
        ],
    },
    "overall-signal-stacking": {
        "family": "bespoke",
        "mode": "sum",
        "definitions": [
            "the AI vocabulary and GPTZero watch lists = the two lists "
            "behind B1's trigger phrases; the GPTZero watch list is the "
            "part taken from @source[gptzero-ai-vocabulary]'s published "
            "phrases",
            "Kobak style words = a fixed list of tone words that "
            "@source[kobak-llm-excess-vocabulary] found AI editing adds "
            "to paper abstracts",
            "the single-clause contrast test = a check for a form of "
            "`be` plus `more than just`, or for `goes beyond`",
        ],
        "conditions": [
            {
                "line": (
                    "`2` points when one paragraph holds `4+` words or "
                    "phrases from the AI vocabulary and GPTZero watch "
                    "lists, in any form"
                )
            },
            {
                "line": (
                    "`1` point when one paragraph holds `2` or `3` such "
                    "words or phrases"
                )
            },
            {
                "line": (
                    "`1` point when `2+` different GPTZero watch phrases "
                    "appear"
                )
            },
            {
                "line": (
                    "`2` points at a Kobak style-word rate of `35+` "
                    + RATE_UNIT + ", needing `1` different Kobak style "
                    "word per `12` words of text, that needed count "
                    "bounded `5` to `25`"
                )
            },
            {
                "line": (
                    "`1` point at a Kobak style-word rate of `20+` "
                    + RATE_UNIT + ", needing `1` different Kobak style "
                    "word per `25` words of text, that needed count "
                    "bounded `3` to `12`, when the `2`-point Kobak tier "
                    "does not fire"
                )
            },
            {
                "line": (
                    "capped at `4` points from all the vocabulary lines "
                    "combined"
                )
            },
            {
                "line": (
                    "`1` point when the single-clause contrast test "
                    "triggers"
                )
            },
            {"line": "`2` points when G7's check triggers"},
            {
                "line": (
                    "`2` points when B3's check triggers, `1` more for "
                    "each match past the first, capped at `4` points from it"
                )
            },
            {"line": "`1` point when E8's check triggers"},
            {"line": "`1` point when E6's check triggers"},
            {"line": "`1` point when G6's check triggers"},
            {"line": "`1` point when H2's check triggers"},
            {"line": "`2` points when G12's check triggers"},
            {"line": "`1` point when G3's check triggers"},
            {"line": "`2` points when D1's check triggers"},
            {"line": "`2` points when E4's check triggers"},
            {"line": "`1` point when H13's check triggers"},
            {"line": "`1` point when E3's check triggers"},
            {"line": "{minimum_points}+ points in total"},
        ],
    },
    "no-false-ranges": {
        "family": "bespoke",
        "mode": "all",
        "conditions": [
            {
                "line": (
                    "{minimum_pairs_per_sentence}+ pairs of `from` and "
                    "`to` in one sentence"
                )
            },
            {
                "line": (
                    "{maximum_pair_characters} characters or under stand "
                    "between each pair's `from` and `to`"
                )
            },
            {
                "line": (
                    "no `,` `.` `;` `:` `!` `?` stands between each "
                    "pair's `from` and `to`"
                )
            },
        ],
    },
    "no-superficial-ing": {
        "family": "bespoke",
        "mode": "any",
        "definitions": [
            "clause verbs = `is` `are` `was` `were` `has` `have` `had` "
            "`mean` `means` `meant` `feel` `feels` `felt` `depend` "
            "`depends` `should` `would` `could` `can` `will` `must` "
            "`come` `comes` `came` `do` `does` `did`",
        ],
        "conditions": [
            {
                "line": (
                    "`1+` sentences whose first word ends in `-ing`, with a "
                    "comma within {maximum_clause_characters} characters of "
                    "that word"
                ),
                "unless": [
                    "the first word is `according` or `during`",
                    "a clause verb stands between the `-ing` word and the "
                    "comma",
                    "a quote mark or apostrophe stands between the `-ing` "
                    "word and the comma",
                    "the word after the comma is `and`, `but`, `or`, "
                    "`nor`, `for`, `so`, `yet`, `even`, `not`, `because`, "
                    "`while`, `although`, or `though`",
                    "the first character after the comma is not a letter",
                ],
            },
            {"line": "`1+` @trigger-phrases"},
        ],
    },
    "no-staccato-sequences": {
        "family": "bespoke",
        "mode": "any",
        "conditions": [
            {
                "line": (
                    "{minimum_run}+ sentences in a row, each under "
                    "{run_short_sentence_words} words"
                )
            },
            {
                "line": (
                    "{minimum_repeated_opener_run}+ sentences in a row, each "
                    "under {run_short_sentence_words} words, all starting "
                    "with the same word"
                )
            },
            {
                "line": (
                    "`1+` @trigger-phrases standing as its own sentence "
                    "or fragment"
                )
            },
            {
                "line": (
                    "sentences of {rate_short_sentence_words} words or "
                    "under at a rate of {maximum_short_rate_per_1000}+ "
                    + RATE_UNIT
                    + ", in text of {rate_minimum_words}+ words"
                )
            },
            {
                "line": (
                    "an average sentence length under "
                    "{maximum_mean_sentence_words} words, across "
                    "{minimum_mean_sentences}+ sentences"
                )
            },
        ],
    },
}


# --------------------------------------------------------------------------
# Skips derivation. Lexical checks carry the full mask; the quote-aware
# lexical check keeps quoted text; everything else is scanned for the
# front-matter strip in its own source (directly or through the helpers
# that strip on the check's behalf).

_STRIP_HELPERS = (
    "strip_front_matter",
    "prose_paragraphs",
    "_biber_rate_check",
)


def _grade_source():
    return GRADE_PATH.read_text()


def _function_sources(source):
    """Map function name -> body text for every top-level def in grade.py."""
    bodies = {}
    matches = list(re.finditer(r"^def ([a-zA-Z0-9_]+)\(", source, re.M))
    for i, m in enumerate(matches):
        end = matches[i + 1].start() if i + 1 < len(matches) else len(source)
        bodies[m.group(1)] = source[m.start():end]
    return bodies


def _registry_map(source):
    """Map check id -> function name from the ALL_CHECKS literal."""
    block = re.search(r"^ALL_CHECKS = \{(.*?)^\}", source, re.M | re.S)
    if not block:
        raise AssertionError("detection_spec: ALL_CHECKS literal not found")
    return dict(re.findall(r'"([a-z0-9-]+)":\s*(check_[a-z0-9_]+)', block.group(1)))


def _lexical_sets(source):
    def read(name):
        block = re.search(name + r"\s*=\s*\{(.*?)\}", source, re.S)
        return set(re.findall(r'"([a-z0-9-]+)"', block.group(1)))
    return read("LEXICAL_CHECKS"), read("QUOTE_AWARE_LEXICAL_CHECKS")


def skips_for(check_id, source, fn_bodies, registry, lexical, quote_aware):
    if check_id in quote_aware:
        return ["front matter", "code", "web addresses"]
    if check_id in lexical:
        return list(SKIP_LABELS)
    body = fn_bodies.get(registry.get(check_id, ""), "")
    if any(helper in body for helper in _STRIP_HELPERS):
        return ["front matter"]
    return []


# --------------------------------------------------------------------------
# Emitter.

def emit_all():
    """Return {pattern_number: detection} for all 79 records."""
    source = _grade_source()
    fn_bodies = _function_sources(source)
    registry = _registry_map(source)
    lexical, quote_aware = _lexical_sets(source)
    data = json.loads(PATTERNS_PATH.read_text())

    record_ids = {key for key in data if not key.startswith("_")}
    missing = sorted(record_ids - DETECTION.keys())
    surplus = sorted(DETECTION.keys() - record_ids)
    if missing or surplus:
        problems = []
        if missing:
            problems.append("missing structured entries: " + ", ".join(missing))
        if surplus:
            problems.append("unknown entries: " + ", ".join(surplus))
        raise AssertionError("detection_spec registry mismatch: " + "; ".join(problems))

    out = {}
    checked_by = {}
    for key, record in data.items():
        if key == "_extra_entries":
            continue
        if key.startswith("_"):
            continue
        number = record["pattern_number"]
        spec = DETECTION[key]
        family = FAMILIES[spec["family"]]
        built = family(spec)
        out[number] = {
            "kind": "check",
            "mode": built["mode"],
            "definitions": spec.get("definitions", []),
            # Sentence shapes the check matches, as owner-approved chip
            # wordings; X and Y stand for the free parts. They join the
            # Trigger phrases chips.
            "shape_chips": spec.get("shape_chips", []),
            "conditions": built["conditions"],
            "skips": skips_for(
                key, source, fn_bodies, registry, lexical, quote_aware
            ),
        }
    for extra in data.get("_extra_entries", []):
        number = extra["pattern_number"]
        if extra.get("kind") == "agent":
            out[number] = {
                "kind": "agent",
                "mode": None,
                "conditions": [{"line": AGENT_CONDITION}],
                "skips": [],
            }
        elif extra.get("kind") == "programmatic":
            checked_by[number] = extra.get("check_id")
    # Programmatic extra entries name their check by id; resolve the pattern
    # that owns it from the check-owning records so the reference can never
    # dangle.
    check_owner = {}
    for key, record in data.items():
        if not key.startswith("_"):
            check_owner[key] = record["pattern_number"]
    for number, check_id in checked_by.items():
        owner = check_owner.get(check_id)
        if owner is None:
            raise AssertionError(
                f"detection_spec: extra entry {number} references unknown "
                f"check {check_id}"
            )
        out[number] = {
            "kind": "check",
            "mode": "any",
            "conditions": [
                {"line": f"{owner}'s check triggers · this pattern is checked by it"}
            ],
            "skips": [],
        }
    return out


def main():
    print(json.dumps(emit_all(), indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
