Title: Onur Solmaz: kill-ai-smell skill and ai-smell stylometric corpus
URL Source: https://github.com/osolmaz/tools/tree/main/agents/skills/kill-ai-smell and https://github.com/osolmaz/ai-smell

Markdown Content:

Fetched 2026-07-14 from raw.githubusercontent.com at branch main. Tree of osolmaz/tools path agents/skills/kill-ai-smell per GitHub contents API: SKILL.md (21096 bytes), check.py (11375 bytes), evidence.md (6910 bytes). The ai-smell corpus repository README is appended; the corpus texts, scripts, results.json, and autoresearch journal live in that repository and are not copied here.

===== osolmaz/tools: agents/skills/kill-ai-smell/SKILL.md =====

---
name: kill-ai-smell
description: Remove AI writing tells from prose, headings, openings, and page structure. Use when writing or editing anything meant to read as human-written, including blog posts, site copy, documentation, README text, reports, PR descriptions, and emails. Trigger when the user mentions AI smell, AI tells, slop, em dashes, or prose sounding AI-written.
---

# Kill AI smell

AI-written text has recognizable tells, and readers who spot them discount
the whole document. The tells run deeper than word choice. They show up in
punctuation, in sentence shape, in how a document opens, in what headings
look like, and in the layout of a page. This skill covers each level in
turn, from the smallest unit to the whole document. Apply the rules to
everything you write or edit, and sweep for violations before finishing
any writing task.

One principle governs all of it: write for a reader who is following a
thought from beginning to end. Slop mentions things; writing explains
them. When a passage lists facts without saying why the reader should
care, or compresses context into fragments the reader must decode, the
fix is to rewrite it as sentences that carry the reader forward. Every
rule below is a special case of this.

Knowing these rules is no defense against violating them. The patterns
are how models write by default, so they appear even in text about the
patterns, including rewrites produced to fix an earlier sweep. Sweep
your own output mechanically after every revision; do not trust your
ear, and do not let a violation stand because you can articulate a
stylistic justification for it after the fact.

Most rules below carry a Bad/Good pair. Study the shape of the rewrite,
not just the banned pattern: the fix is always restructuring, never
swapping the banned pattern for a neighboring one.

## Punctuation

**Em dashes.** At most one set per 1000 words. Restructure with commas,
parentheses, or separate sentences instead. This is the most widely known
tell, and readers now flinch at a single one.

- Bad: "The data plane — SSH, rsync, and command execution — goes
  directly to the runner."
- Good: "The data plane (SSH, rsync, and command execution) goes directly
  to the runner."

**Colon pivots.** Do not compensate for the em-dash rule with "X: Y"
constructions. Colons are for genuine lists and quoted examples. The
short punch ("The fix is simple: stop guessing.") is the obvious case,
but the longer pivot, a claim followed by a colon and its elaboration,
is the same crutch, and stamping it into paragraph after paragraph is a
tell even though each instance looks defensible alone. Human prose uses
the occasional colon; it does not hinge every paragraph on one. If more
than a couple of paragraphs in a row pivot on a colon, rewrite most of
them as two sentences or fold the elaboration in with a comma.
Semicolons should be rare.

- Bad: "The fix is simple: stop guessing."
- Good: "The fix is to stop guessing."
- Bad: "The groups overlap: the Requests README out-fragments three of
  the AI pages."
- Good: "The groups overlap. The Requests README out-fragments three of
  the AI pages."

**Semicolon chains.** Do not string an enumeration across one sentence
with semicolons. Break it into sentences, each of which says something
about its step.

- Bad: "It leases a machine; syncs your files; runs the command; streams
  output; records evidence."
- Good: "It leases a machine and syncs your files to it. The command then
  runs remotely while output streams back, and the run is recorded."

## Sentence patterns

**Contrast rhetoric.** "It is not X, it is Y", "X, not Y", "not X, but Y"
and all variants are banned. The construction forces the reader to hold a
clause (X) that the sentence immediately throws away. Say Y directly.

- Bad: "It is not a benchmark predictor. It is a roofline."
- Good: "It is a roofline."
- Bad: "This changes the packaging, not the position."
- Good: "The position stays the same."
- Bad: "Queries hit the disk, not GitHub."
- Good: "Queries hit the local database, so no GitHub quota is spent."

A plain negation is fine when the negation is the content: a genuine
non-equivalence ("fitting in memory does not imply serving usefully"), a
disambiguation between two real quantities, or a warning about a real
misconception. Use it once, plainly, without the paired "it is Y" reveal.

**"Not just X" escalation.** "It isn't just X, it's Y" and similar
intensifier patterns are banned for the same reason.

- Bad: "It's not just a linter, it's a full review pipeline."
- Good: "It runs a full review pipeline, from mapping the repo to
  validating each fix."

**Rule of three.** Lists of exactly three parallel items, sentence after
sentence, are a strong tell. In measured corpora, AI copy produces these
at several times the human rate. Vary list length, or use fewer lists.

- Bad: "It is fast, simple, and reliable. Setup takes minutes, works
  everywhere, and survives upgrades. You get speed, safety, and control."
- Good: "It is fast and needs no setup. In three months of daily use it
  has not broken once."

**Anaphora chains.** Three or more parallel negations or repetitions in a
row read as ad copy. One plain sentence saying the same thing is stronger.

- Bad: "No client ID, no redirect URI, no developer dashboard."
- Good: "You skip the developer-dashboard registration entirely."

**Fragment rhythm.** AI copy alternates verbless two-to-four word punches
with thirty-word feature enumerations. Human short sentences are full
clauses with a subject and a verb. If a paragraph swings between
fragments and freight trains, rewrite it into sentences of ordinary,
varied length.

- Bad: "Actively developed. Ships weekly."
- Good: "Development is active, with releases most weeks."

**Sentence flow.** Let main clauses run. The strongest rhythm tell in the
study corpus is that AI copy breaks nearly every sentence with a comma,
colon, dash, or parenthesis before ten words pass, while human prose
keeps producing sentences that contain one long unbroken run of words,
whatever the register. Do not chop a flowing clause into punctuated
pieces; if every sentence in a paragraph pauses by word eight, merge the
pieces back into clauses that carry through.

- Bad: "The parser, once configured, rejects unknown fields, quietly, and
  logs them."
- Good: "Once configured, the parser quietly rejects unknown fields and
  logs each one it drops."

**Hedging boilerplate.** Cut "it's worth noting that", "it's important to
remember", and similar throat-clearing.

- Bad: "It's worth noting that the cache is process-local."
- Good: "The cache is process-local."

**Overwrought transitions.** Cut "moreover", "furthermore", "in
conclusion", and summary paragraphs that restate what was just said.

- Bad: "Moreover, the parser rejects unknown fields. In conclusion,
  strict validation prevents drift."
- Good: "The parser also rejects unknown fields."

**Inflated vocabulary.** Use the plain word. "Delve", "landscape",
"testament to", "tapestry", "crucial", and "leverage" as a verb all mark
generated text.

- Bad: "It leverages a robust caching landscape."
- Good: "It uses a cache."

## Paragraph and argument shape

Sentence-level fixes are not enough. A paragraph can pass every rule
above and still read as generated, because the tell is in its shape:
generated prose argues completely and evenly, and human prose does not.

**Cut content, not just words.** Do not fill every slot of an argument.
A paragraph whose skeleton runs limitation, objection, fix, result,
caveat, confidence, with one sentence per slot and every rebuttal
pre-answered, smells no matter how good the sentences are. Merge points,
drop the weakest one, and leave an inferential step to the reader. When
a passage still smells after sentence-level fixes, the remaining fix is
deletion. A detail that already appears elsewhere in the document (a
date, a definition, a second supporting number) does not need to appear
again.

- Bad: a ten-sentence paragraph covering the limitation, the objection,
  the fix, both results, the future test, and the final confidence.
- Good: the same ground in six sentences, with the objection folded into
  the fix and one number carrying the conclusion.

**Ground abstractions in named things.** A paragraph written entirely in
the document's own coinages, with no file, person, or number in it, runs
at the concept layer where generated prose lives. Reach for the concrete
instance.

- Bad: "The structural gaps survived that control untouched."
- Good: "Triads and labeled bullets kept separating the groups after the
  READMEs went in."

**No drama vocabulary for methodology.** Findings do not "survive",
metrics do not "collapse", baselines are not "adversarial", and the next
step is not an "escalation". Say what happened in plain verbs.

- Bad: "Two metrics collapsed under the adversarial baseline."
- Good: "Two metrics stopped separating the groups once the READMEs went
  in."

**No aphorism closers.** Do not end a paragraph by promoting its
specific point into a universal principle. If the story implies the
principle, the closing slogan adds nothing; delete it.

- Bad: "That is the argument for keeping the baselines adversarial."
- Good: (nothing; the previous sentence already made the point)

**Keep the subject next to its verb.** Do not stuff a list or a chain of
qualifications between a subject and its verb. Split the sentence.

- Bad: "The sizes of the surviving gaps, three-fold at the closest edge
  and roughly twenty-fold on average with no overlap, make me
  confident."
- Good: "The closest gap is three-fold and the average is around
  twenty-fold. That margin is enough for me."

**Hold one register.** Stiff formality and bolted-on casualness in the
same passage is an uncanny mixture that neither a formal nor a casual
human writer produces. Pick the register the venue calls for and hold
it through the document.

- Bad: "I would not call this a validated classifier. A stricter test
  would need a pile of landing pages."
- Good: "I wouldn't promise these thresholds hold beyond this corpus. A
  stricter test would need human-written landing pages from after 2022."

## Openings

Say what the thing is before saying what it does. GPT-flavored copy
describes behavior and dodges identity, so the reader has to assemble
what kind of thing they are looking at. State the category in the first
sentence and the practical job in the second.

- Bad: "LocalPerf benchmarks local LLM inference servers and keeps the
  evidence in one portable run artifact."
- Good: "LocalPerf is a local LLM inference benchmark CLI. It runs
  benchmark plans against local inference servers and stores the
  evidence in one portable run artifact."

The identity sentence has degraded forms that do not count:

- The headless fragment: "A local-first GitHub triage tool for
  maintainers." Category information with no subject and no verb.
- The buried identity: opening with an imperative benefit ("Keep your
  editor and git workflow.") and stating what the tool is three screens
  down.
- Pseudo-identity: "is designed to be the layer between X and Y" states
  purpose, and "root() is the product" is a meta-remark. Neither names a
  category.

The same rule scales up: a section or report should open with sentences
that orient the reader (what this is, what was done, what follows), never
with a compressed context dump. See "Page structure" below.

## Headings

Make headings labels, not sentences. A heading names the topic of its
section as a noun phrase ("Capacity limit", "Crash testing", "Worked
examples") so the reader can scan the structure. Specific heading tells:

**Slogan headings.** A full subject-verb heading pre-empts the section
and reads as a pitch.

- Bad: "Capacity Caps the Batch"
- Good: "Capacity limit"

**Comma couplets.** The parallel two-beat slogan is among the strongest
title-level tells and appears almost exclusively in generated copy.

- Bad: "Local loop, remote box" / "Two jobs, one binary" / "Many
  providers, one loop"
- Good: "Remote execution model" / "Scope" / "Supported providers"

**Imperative slogans.** These sell the section instead of naming it.

- Bad: "Pick your path" / "Try it" / "Reuse what's warm"
- Good: "Reading guide" / "First run" / "Warm-box reuse"

**Rhetorical frames.** A run of "Why X" / "How Y" / "What you get"
headings down one outline is a smell, and so is any one template stamped
across siblings ("I want to try it / I want to wire up an agent / I want
the full reference").

- Bad: "Why spogo" / "What you get" / "Where to next"
- Good: "Design rationale" / "Feature overview" / "Further reading"

**Casing and articles.** Use sentence case. Capitalize the first word,
proper nouns, and coined terms; lowercase the rest. Keep acronyms
uppercase. Do not make "The" a reflexive prefix; drop it from noun-phrase
labels and keep it only where a full clause needs it.

- Bad: "The Memory-Fit Batch"
- Good: "Memory-fit batch"

The exception is a deliberate major statement. A heading may be a full
sentence when that sentence is a load-bearing claim the section exists to
defend, such as a named law or a thesis. Use it rarely; in a document
whose headings are otherwise noun phrases, a sentence heading should earn
its emphasis, and two in a row almost never do.

After drafting, read the headings as a flat list and check that they are
the same kind of thing: labels with labels, one register, one casing.

## Page structure

**Subtitles where intros belong.** A section that opens with compressed
context fragments has skipped the introduction. The reader gets metadata
before they know what the document is about. Write an intro in full
sentences that says what this is, what was done, and what the reader will
find, in that order. Details the reader cannot use yet belong later, next
to where they matter.

- Bad: "Six pages against three baselines. Code blocks stripped; rates
  per 1,000 words."
- Good: "This report compares six project pages against three
  human-written baselines. Before measuring, the script strips code
  blocks, and every rate is normalized per 1,000 words so the two groups
  are comparable."

**Labeled-bullet walls.** The bullet shaped "Label — one-sentence
elaboration" (or "Label. Elaboration.") is the signature layout unit of
AI landing copy; measured pages are 50 to 95 percent this one shape,
while human docs almost never use it. A run of them is a wall of parallel
fragments, and none of them explains anything. Convert runs into prose
paragraphs that connect the items, and keep bullets for genuinely
enumerable things. Vary their shape when you do use them.

- Bad: "- Zero-config discovery. Reads your editor config automatically.
  - Typed clients. Emits interfaces for every tool.
  - OAuth ergonomics. Caches and refreshes tokens."
- Good: "It discovers servers from your editor config, so there is
  nothing to set up. From that config it can emit typed interfaces for
  every tool, and it handles OAuth caching and refresh on its own."

**Formula and fact dumps.** No section may become a list of statements
one after another, whether formulas, definitions, or feature claims.
Introduce each item with prose that says why it appears, and follow
substantial items with prose that interprets them. Long derivations or
arguments must be broken into stages with the goal stated between stages.
The reader should be able to follow the conceptual path from the
surrounding paragraphs alone.

**Template stamping.** The same skeleton shipped across documents ("Why
X", "Pick your path", "Status", "Out of scope", a "five minutes"
time-to-value promise) marks a house style produced by one prompt. Any
single page looks fine; side by side they are unmistakable. Let each
document's structure follow its content.

**Word diarrhea.** Do not pad with exhaustive feature taxonomies,
implementation internals, long option catalogs, or process history the
reader does not need for the task at hand. Being comprehensive about the
wrong things is a tell of its own.

**Emoji feature grids.** The grid of emoji-headed feature cards is the
most recognizable generated landing-page layout. Do not use emojis as
section markers or bullets at all.

**Manual heading numbers.** Do not number Markdown headings by hand. Let
the renderer or publication system number sections when numbering is
needed.

- Bad: "## 1. Overview"
- Good: "## Overview"

## Repetition and word choice

Generated text avoids repeating itself: each mention of a thing gets a
fresh synonym, which pushes lexical variety above the human range. Human
writers repeat deliberately. They reuse the established term for a
concept instead of rotating synonyms, and they repeat a phrase for
emphasis when hammering a point. Keep one name per concept through a
document, and let purposeful repetition stand.

- Bad: "The tool syncs issues locally. The utility then clusters them,
  and the binary ships a TUI for browsing."
- Good: "The tool syncs issues locally, clusters them, and ships a TUI
  for browsing them."

The same applies to sentence shape in reverse: humans vary rhythm
naturally, while generated text stamps one shape (or one bullet template)
many times. Uniform novelty in words plus uniform sameness in structure
is the combination to break up.

## Final sweep

Before finishing any writing task, check the draft against this list:

- Em dashes within budget; no "X: Y" punch lines; no semicolon chains.
- No contrast rhetoric or "not just X" anywhere.
- No run of exactly-three lists; no anaphora chains.
- No verbless fragments doing a sentence's job.
- No paragraph that fills every argumentative slot; something was cut.
- Every paragraph contains at least one named thing (a file, a person,
  a number), and no drama verbs narrate the methodology.
- No aphorism closing a paragraph; no list wedged between a subject and
  its verb; one register throughout.
- The document says what its subject is before what it does.
- Sections open with orienting sentences, never context-dump fragments.
- Headings are sentence-case noun-phrase labels; no slogans, comma
  couplets, imperatives, or repeated rhetorical frames.
- No labeled-bullet walls; bullets vary in shape and are genuinely lists.
- No hedging, inflated vocabulary, or restating summaries.
- One name per concept; repetition only where it serves emphasis.

When editing existing text, fix a smell by restructuring the sentence or
the section. Swapping one banned pattern for another (an em dash for a
punchy colon, a triad for an anaphora chain) changes nothing.

## Mechanical check

This skill ships `check.py`, a stdlib-only script that runs the
measurable subset of the rules above. Rewrites reintroduce the patterns,
so run it on the draft after every revision:

```
python3 check.py draft.md
```

It prints findings with line numbers at two severities and exits nonzero
when any violation remains:

- A `VIOLATION` is a banned pattern or a rate over budget: em dashes
  beyond one per thousand words, semicolon chains, "not just X",
  hedging phrases, anaphora chains, exactly-three lists past the
  detector threshold, labeled bullets past 30% of all bullets, and
  manually numbered headings. Fix all of these by restructuring, then
  rerun until the file is clean.
- A `REVIEW` needs judgment. "X, not Y" is allowed when the negation is
  the content; a colon before a list is fine; a heading with a comma may
  be a legitimate title. Read each flagged line and decide; do not
  mechanically rewrite them.

Two document-level `REVIEW` stats come from the stylometric study rather
than from a single line. Sentence flow reports when the mean longest
unbroken run of words per sentence falls under 10, which in the study
corpus happens to every AI page and no human text; the fix is to let
main clauses run instead of chopping them with punctuation. MTLD
lexical diversity reports when synonym rotation pushes the score past
110, where every AI page in the corpus sits; the fix is to reuse the
established word for a thing.

The script cannot see paragraph shape, register, or aphorism closers,
so a clean run does not replace the checklist above. Human baselines in
the study corpus average under one violation per document while the AI
pages average more than three. A draft that reports several violations
needs restructured sections rather than patched sentences.

## Where the rules come from

Every threshold in this skill was measured, not asserted. The rules
derive from a stylometric study of ten AI-written landing pages
against eight provably pre-LLM human texts, plus 42 in-the-wild tweet
samples, maintained in the
[ai-smell repository](https://github.com/osolmaz/ai-smell) and written
up at [solmaz.io/ai-de-smeller](https://solmaz.io/ai-de-smeller). For
the per-rule evidence, including which tells separate the corpus with
no overlap, which are one-directional, which collapsed into register
signals, and how to test a new tell candidate, see
[evidence.md](evidence.md) in this skill's folder.


===== osolmaz/tools: agents/skills/kill-ai-smell/check.py =====

#!/usr/bin/env python3
"""Mechanical sweep for AI writing tells.

Usage: python3 check.py FILE [FILE...]

Checks Markdown or plain-text prose against the kill-ai-smell rules and
prints findings with line numbers. Code blocks, inline code, URLs, and
YAML frontmatter are ignored. Two severities:

  VIOLATION  banned pattern or rate over budget; restructure until clean
  REVIEW     needs judgment (for example, a negation that may be content)

Exit code is 1 when any VIOLATION is found, else 0. Rate thresholds come
from the stylometric study in https://github.com/osolmaz/ai-smell.
"""
import re
import sys
from pathlib import Path

HEDGING = [
    "it's worth noting", "it is worth noting", "it's important to note",
    "it is important to note", "it's important to remember",
    "keep in mind that", "needless to say",
]
TRANSITIONS = ["moreover", "furthermore", "in conclusion", "in summary"]
INFLATED = [
    "delve", "delves", "delving", "tapestry", "testament to", "landscape",
    "crucial", "leverage", "leverages", "leveraged", "leveraging",
    "robust", "seamless", "seamlessly", "supercharge", "game-changer",
]
CONTRAST_BANNED = [
    (r"\bnot\s+(?:just|only|merely)\b", '"not just X" escalation'),
    (r"\bit\s+is\s+not\s+[^.;]{1,40}[,.;]\s*it\s+is\b", '"it is not X, it is Y"'),
    (r"\bisn't\s+[^.;]{1,40}[,.;]\s*it's\b", '"isn\'t X, it\'s Y"'),
]
CONTRAST_REVIEW = [
    (r",\s*not\s+[a-z]", '"X, not Y" contrast (allowed only as real content)'),
    (r"\bnot\s+[^.;:]{1,30},\s*but\b", '"not X, but Y"'),
    (r"\brather than\b", '"rather than" contrast frame'),
]


def strip_prose(raw):
    """Return (lines, in_prose_mask): code fences and frontmatter blanked."""
    lines = raw.splitlines()
    out = []
    in_code = False
    in_front = False
    for i, line in enumerate(lines):
        s = line.strip()
        if i == 0 and s == "---":
            in_front = True
            out.append("")
            continue
        if in_front:
            out.append("")
            if s == "---":
                in_front = False
            continue
        if s.startswith("```"):
            in_code = not in_code
            out.append("")
            continue
        if in_code:
            out.append("")
            continue
        line = re.sub(r"<!--.*?-->", "", line)
        line = re.sub(r"`[^`]+`", "CODE", line)
        line = re.sub(r"\]\([^)]+\)", "]", line)   # markdown link targets
        line = re.sub(r"https?://\S+", "URL", line)
        out.append(line)
    return out


def sentences(text):
    for abbr in ("e.g.", "i.e.", "vs.", "etc."):
        text = text.replace(abbr, abbr.replace(".", "\u0000"))
    text = re.sub(r"(\d)\.(\d)", "\\1\u0000\\2", text)
    parts = re.split(r"(?<=[.!?])\s+", text)
    return [p.replace("\u0000", ".") for p in parts if p.strip()]


def check(path):
    lines = strip_prose(Path(path).read_text())
    findings = []  # (severity, line_no or None, message)

    headings, bullets, body = [], [], []
    for n, line in enumerate(lines, 1):
        if re.match(r"\s*#{1,6}\s", line):
            headings.append((n, re.sub(r"^\s*#{1,6}\s+", "", line).strip()))
        elif re.match(r"\s*([-*+]|\d+\.)\s", line):
            bullets.append((n, line))
            body.append((n, re.sub(r"^\s*([-*+]|\d+\.)\s+", "", line)))
        elif line.strip():
            body.append((n, line))

    text = " ".join(l for _, l in body)
    words = re.findall(r"[A-Za-z0-9'’-]+", text)
    n_words = max(len(words), 1)
    per_1k = lambda count: round(count * 1000.0 / n_words, 1)

    # --- punctuation ---
    def dashes(line):
        if re.match(r"^\s*\|?[\s|:-]+\|?\s*$", line):   # table separator / hrule
            return []
        return re.findall(r"—|(?<!-)--(?!-)| - ", line)

    dash_lines = [n for n, l in body for _ in dashes(l)]
    budget = max(1, n_words // 1000)
    if len(dash_lines) > budget:
        findings.append(("VIOLATION", None,
                         f"{len(dash_lines)} em dashes for {n_words} words "
                         f"(budget {budget}); lines {sorted(set(dash_lines))}"))

    for n, l in body:
        if l.count(";") >= 2:
            findings.append(("VIOLATION", n, "semicolon chain"))
    semis = sum(l.count(";") for _, l in body)
    if per_1k(semis) > 3:
        findings.append(("REVIEW", None,
                         f"semicolons at {per_1k(semis)}/1k words (humans stay under 3)"))

    # Mid-sentence prose colons. A colon that ends the line introduces a
    # list or block quote and is fine; a colon with prose flowing on is
    # usually the pivot crutch. Each one gets a REVIEW, and a streak of
    # three consecutive paragraphs hinging on one is a VIOLATION.
    pivot_lines = []
    for n, l in body:
        for m in re.finditer(r"[a-z\"\u201d)](?<!\d):(?!\d)\s+(\S[^.!?]{0,80})", l):
            findings.append(("REVIEW", n,
                             f'colon pivot: "...: {m.group(1).strip()[:60]}"'))
            pivot_lines.append(n)
    para_lines = [n for n, _ in body]
    streak, prev = [], None
    for n in para_lines:
        if n in pivot_lines:
            streak.append(n)
            if len(streak) >= 3:
                findings.append(("VIOLATION", n,
                                 f"3+ consecutive paragraphs pivot on a colon "
                                 f"(lines {streak[-3:]})"))
                streak = []
        else:
            streak = []

    # --- sentence patterns ---
    for n, l in body:
        low = l.lower()
        for pat, name in CONTRAST_BANNED:
            if re.search(pat, low):
                findings.append(("VIOLATION", n, name))
        for pat, name in CONTRAST_REVIEW:
            if re.search(pat, low):
                findings.append(("REVIEW", n, name))
        for phrase in HEDGING:
            if phrase in low:
                findings.append(("VIOLATION", n, f'hedging: "{phrase}"'))
        for word in TRANSITIONS:
            if re.search(r"\b" + word + r"\b", low):
                findings.append(("VIOLATION", n, f'overwrought transition: "{word}"'))
        for word in INFLATED:
            if re.search(r"\b" + re.escape(word) + r"\b", low):
                findings.append(("REVIEW", n, f'inflated vocabulary: "{word}"'))
        if re.search(r"\bno\s+[\w-]+(?:\s+[\w-]+)?,\s*no\s+[\w-]+", low):
            findings.append(("VIOLATION", n, "anaphora chain (no X, no Y, ...)"))

    triads = len(re.findall(r"\b[\w'’-]+,\s+[\w'’-]+,\s+and\s+[\w'’-]+\b", text))
    if per_1k(triads) > 3:
        findings.append(("VIOLATION", None,
                         f"exactly-three lists at {per_1k(triads)}/1k words "
                         "(detector threshold is 3)"))
    elif triads >= 2:
        findings.append(("REVIEW", None,
                         f"{triads} exactly-three lists; fine if they enumerate "
                         "real items, a tell if rhetorical"))

    sents = sentences(text)
    frags = [s for s in sents if len(re.findall(r"[\w'’-]+", s)) <= 4]
    if sents and len(frags) / len(sents) > 0.15:
        findings.append(("REVIEW", None,
                         f"{len(frags)} of {len(sents)} sentences are fragments "
                         f"of 4 words or fewer ({100 * len(frags) // len(sents)}%)"))

    # Sentence flow: the longest run of words in each sentence with no
    # punctuation break. Human prose keeps producing sentences with one
    # run of 10+ words; AI copy breaks nearly every sentence first. In
    # the study corpus the AI pages average 4.9-8.8 words per longest
    # run and every human text 10.0 or more.
    runs = []
    for s in sents:
        pieces = re.split(r"[,;:—()]|\s--?\s", s)
        lens = [len(re.findall(r"[\w'’-]+", p)) for p in pieces]
        lens = [l for l in lens if l]
        if lens:
            runs.append(max(lens))
    if len(runs) >= 15:
        mean_run = sum(runs) / len(runs)
        if mean_run < 10:
            findings.append(("REVIEW", None,
                             f"sentence flow: mean longest unbroken run is "
                             f"{mean_run:.1f} words (AI pages 4.9-8.8, human "
                             f"texts 10.0+); let main clauses run without a "
                             f"punctuation break"))

    # Synonym rotation, measured as MTLD lexical diversity (bidirectional,
    # threshold 0.72). Every AI page in the study scores above 111 while
    # seven of eight human texts stay under 106.
    def mtld_pass(tokens, threshold=0.72):
        factors, types, count = 0.0, set(), 0
        for t in tokens:
            count += 1
            types.add(t)
            if len(types) / count <= threshold:
                factors += 1
                types, count = set(), 0
        if count:
            factors += (1 - len(types) / count) / (1 - threshold)
        return len(tokens) / factors if factors else 0.0

    tokens = [w.lower() for w in re.findall(r"[A-Za-z'’-]+", text)]
    if len(tokens) >= 300:
        mtld = (mtld_pass(tokens) + mtld_pass(tokens[::-1])) / 2
        if mtld > 110:
            findings.append(("REVIEW", None,
                             f"MTLD lexical diversity is {mtld:.0f} (AI pages "
                             f"score 111+, humans mostly under 106); reuse the "
                             f"established word instead of rotating synonyms"))

    # --- bullets ---
    labeled = []
    for n, b in bullets:
        m = re.match(r"\s*[-*+]\s+(?:\*\*)?([^—:.]{1,60}?)(?:\*\*)?\s*(?:[—:.])\s+\S", b)
        if m and len(m.group(1).split()) <= 5:
            labeled.append(n)
    if bullets and len(labeled) / len(bullets) > 0.3:
        findings.append(("VIOLATION", None,
                         f"labeled bullets are {100 * len(labeled) // len(bullets)}% "
                         f"of {len(bullets)} bullets (threshold 30%); "
                         f"lines {labeled}"))

    # --- headings ---
    for n, h in headings:
        h_words = h.split()
        if re.match(r"^\d+[.)]\s", h):
            findings.append(("VIOLATION", n, f'manually numbered heading: "{h}"'))
        if h.count(",") == 1 and len(h_words) <= 6 and not h.endswith("?"):
            findings.append(("REVIEW", n, f'possible comma-couplet heading: "{h}"'))
        caps = [w for w in h_words[1:] if re.match(r"^[A-Z][a-z]", w)]
        if len(h_words) >= 3 and len(caps) >= len(h_words) / 2:
            findings.append(("REVIEW", n, f'Title Case heading: "{h}"'))
        if re.match(r"^(why|what|how|where)\b", h, re.I) and not h.endswith("?"):
            findings.append(("REVIEW", n, f'rhetorical-frame heading: "{h}"'))

    return findings, n_words


def main(argv):
    if len(argv) < 2:
        print(__doc__.strip())
        return 2
    exit_code = 0
    for path in argv[1:]:
        findings, n_words = check(path)
        violations = [f for f in findings if f[0] == "VIOLATION"]
        if violations:
            exit_code = 1
        print(f"== {path} ({n_words} words): "
              f"{len(violations)} violations, "
              f"{len(findings) - len(violations)} to review")
        for sev, line, msg in sorted(findings, key=lambda f: (f[0] != "VIOLATION", f[1] or 0)):
            loc = f"line {line}" if line else "document"
            print(f"  {sev:9s} {loc}: {msg}")
    return exit_code


if __name__ == "__main__":
    sys.exit(main(sys.argv))


===== osolmaz/tools: agents/skills/kill-ai-smell/evidence.md =====

# Evidence behind the kill-ai-smell rules

This file carries the measurements that justify the rules in SKILL.md,
so the rules can stay short. Read it when you need to know how strong a
rule is, when someone challenges a rule, or when you want to extend the
study. Everything here is reproducible from the
[ai-smell repository](https://github.com/osolmaz/ai-smell), and the
write-up is the blog post
[Building an AI de-smeller](https://solmaz.io/ai-de-smeller).

## The corpus

The ground truth is 18 documents. The AI side is ten OpenClaw project
landing pages written by GPT 5.5 (4,853 words after stripping code).
The human side is eight texts frozen before language models existed
(15,317 words): the SQLite testing docs, essays by Spolsky (2000),
antirez (2018), Graham (2009), and Evans (2019), and the ripgrep,
Redis, and Requests READMEs at 2016-2017 git tags. The READMEs matter
because they sell tools the way landing pages do, which controls for
register. Two register-sensitive metrics (first person, type-token
ratio) looked like tells against essays alone and collapsed once the
READMEs entered the corpus. Treat any new tell with suspicion until it
survives a register-matched baseline.

There are also 42 long-form tweet samples with no ground truth, used
only to see how the thresholds transfer to the feed, and the blog post
itself, archived as a known-AI, skill-compliant control.

All rates are per 1,000 words. One AI model, one register, 18
documents: these are demonstrations with wide margins, not a validated
classifier.

## Strength of each rule

Ranked by the evidence, strongest first.

**Exactly-three lists (triads).** AI 6.3-15.9 per 1k, human 0.0-2.0.
No overlap. Every AI page is at least 3x every human text, and the
corpus averages differ about 19x. One of the two detector rules (threshold 3
per 1k). This is the strongest punctuation-level tell.

**Labeled bullets.** Share of bullets that open with a short label,
then a separator, then elaboration: AI 53-100%, human 0-11%, and five
of eight human texts never use the shape. The other detector rule
(threshold 30%). More diagnostic than any punctuation rate.

**Sentence flow.** Longest unbroken run of words per sentence, ranked
against a pooled corpus and averaged (the Mann-Whitney statistic of
the document's runs against the pool): AI 0.19-0.41, human 0.49-0.73,
no overlap, leave-one-out 18/18. In raw words, AI pages average a
4.9-8.8-word longest run, human texts 10.0-18.3. Found by an
autoresearch-style search (about fifty logged experiments, preserved
in the repo's `autoresearch/` directory). The negative result matters:
every order-only statistic (alternation, turning points,
autocorrelation, permutation-normalized jaggedness) failed to
separate the groups, so the tell is the level of the runs, never the
order they come in.

**Word choice, measured properly.** MTLD lexical diversity: all ten AI
pages above 111, seven of eight human texts under 106. Mean Zipf word
frequency: every AI page 5.30 or below, every human text 5.28 or
above. Each axis has one crossover (Requests on diversity, ripgrep on
frequency) but no document fails both, so the pair classifies the
corpus. The mechanism is connective tissue rather than fancy words:
human text is nearly half made of the commonest English words because
full sentences run on articles and prepositions, while telegraphic
noun piles need none. Raw type-token ratio does not work, because it is a
register signal (the punchy Requests README scores AI-high).

**Em dashes.** Corpus averages differ about 18x, and the heaviest AI
page lands one every 16 words. But the tell is one-directional: three
of ten AI pages use fewer em dashes than the 2016 ripgrep README and
one uses none. Bulk convicts, and absence proves nothing. That is why the
skill budgets em dashes but the detector dropped them.

**Heading register.** About a third of AI headings are slogans,
imperatives, or rhetorical frames versus one in ten for humans (mostly
mild FAQ questions). The comma couplet ("Two jobs, one binary")
appeared 11 times across five of ten AI sites and once in the human
set, as a deliberate essay title. Title Case turned out to be a human
convention of an era, so the skill flags rhetoric rather than casing.

**Identity deferral.** All three pre-LLM READMEs state what the tool
is in their opening lines, and one of ten AI pages does. The raw
action-to-identity predicate ratio does not separate groups (all body
prose is verb-led); the position of the identity claim does.

**Fragments.** AI pages run 3.6-41.9% verbless sentences of four words
or fewer, humans 1.4-17.4%. The ranges overlap (Requests out-fragments
three AI pages), so fragments corroborate rather than convict.

**Template phrasing across documents.** "Pick your path" on six of ten
AI sites, a "five minutes" promise on seven, "Status" on eight, the
exact closer "Released under the MIT license." on six. Only visible
across a set, since each page looks fine alone. No per-document threshold.

**First person.** Dead as a tell. Essays are saturated with it, but
the pre-LLM READMEs have almost none, exactly like the AI pages. It
tracks register, kept in the skill only as a reminder that some
signals are register.

## Tells that fire on their own author

The study's most instructive event: the agent that had just measured
contrast rhetoric as a top tell titled its own report callout "The
strongest tells are structural, not lexical". Knowing the rules is no
defense, because the patterns are the model's defaults. This is why
the skill demands a mechanical sweep of your own output, and why
`check.py` exists. The blog post that documents the study is archived
in the corpus as `corpus/self/` and clears every detector, which shows
the tells are defaults rather than fingerprints, and an instructed
model stops producing them.

## Interpreting check.py numbers

Human baselines average under one violation per document, and the AI
pages average more than three. A draft with several violations needs
restructured sections, not patched sentences, because patching swaps
one pattern for another (the em dash becomes a punchy colon, the triad
becomes an anaphora chain) and the rates stay high. The document-level
stats have known clean ranges: mean longest run of 10+ words and MTLD
under 110 put a draft with the human baselines on both axes.

## Extending the study

New tell candidates should be tested against the archived corpus, not
against intuition. Clone the ai-smell repository, add a counter to
`analyze.py` or a scorer in the style of `analyze_flow.py`, and demand
separation against the register-matched baselines before believing it.
For open-ended searches, the repo's `autoresearch/` directory shows
the loop that found the flow metric (frozen harness, one editable
feature file, a journal of every run); the same method is available as
the `autoresearch-loop` skill.


===== osolmaz/ai-smell: README.md =====

# ai-smell

This repository is a stylometric study of AI writing tells: the corpus,
scripts, results, and figures behind the blog post
[Building an AI de-smeller](https://solmaz.io/ai-de-smeller) and the
[kill-ai-smell](https://github.com/osolmaz/tools/blob/main/agents/skills/kill-ai-smell/SKILL.md)
agent skill. The starting point was an observation that several OpenClaw
project landing pages read as AI-written. Instead of cleaning them up, we
kept them as specimens and asked whether the tells could be measured, and
which ones separate generated copy from human writing most cleanly. The
study was later expanded from 9 to 18 ground-truth documents to control
for register, plus 42 in-the-wild tweet samples.

The AI side of the corpus is the landing and docs copy of ten OpenClaw
project sites (crabbox.sh, mcporter.sh, gitcrawl.sh, clawpatch.ai,
fs-safe.io, spogo.sh, imsg.sh, wacli.sh, gogcli.sh, goplaces.sh), 4,853
words of prose after stripping code blocks. The human side is eight texts
that are provably human because they were frozen before language models
existed, 15,317 words in total. Five are essays and documentation: the
SQLite testing documentation, Joel Spolsky's 2000 essay on rewrites, a
2018 antirez blog post, Paul Graham's 2009 "Maker's Schedule, Manager's
Schedule", and Julia Evans' 2019 brag-documents post. Three are READMEs
captured at old git tags, whose commit history proves their date and whose
register matches the AI pages: ripgrep at 0.4.0 (2016), Redis at 3.2.0
(2016), and Requests at v2.13.0 (2017). All rates below are normalized per
1,000 words so the corpora are comparable.

## What was measured

The main script (`analyze.py`) strips code blocks and inline code, then
measures each document for punctuation rates (em dashes, semicolons,
colons), sentence-length distribution and fragment share, bullet-line
share and labeled bullets (a bullet that opens with a label of at most
five words, then a period, colon, or dash, then elaboration, reported
as a share of all bullets), contrast rhetoric, exactly-three lists,
anaphora chains, first- and second-person rates, type-token ratio,
sentence openers, and template phrases shared across the AI sites. Two
follow-up scripts test claims from existing writing guidance.
`analyze_ontology.py` tests the identity-deferral claim from the solmaz.io
post "Good READMEs say what tools are" and the write-readme skill.
`analyze_headings.py` classifies every heading against the write-monograph
title rules. Full numbers land in `results.json`.

## Headline numbers

The table gives the range across documents in each group.

| Metric | AI set (10 docs) | Human set (8 docs) |
| --- | --- | --- |
| Em dashes /1k | 0.0–61.3 | 0.0–4.7 |
| Exactly-three lists /1k | 6.3–15.9 | 0.0–2.0 |
| Labeled bullets, % of bullets | 53–100% | 0–11% |
| Fragment sentences (≤4 words) | 3.6–41.9% | 1.4–17.4% |
| First person /1k | 0.0–2.1 | 0.0–50.9 |
| Type-token ratio (first 280 words) | 0.59–0.69 | 0.53–0.67 |
| Sentence flow (mean run percentile) | 0.19–0.41 | 0.49–0.73 |

The triad and labeled-bullet gaps have no overlap between groups. The
notorious AI vocabulary ("delve", "landscape") barely appears in either
corpus, so on this evidence the strongest tells are structural.

## Findings

**1. Labeled bullets are the signature layout unit.** Between 53% and 100%
of bullets on the AI pages follow one shape, a short noun-phrase label
followed by a separator and one sentence of elaboration ("Zero-config
discovery. Reads your home config..."). The human baselines top out at 11%
(the 2016 Redis README), and five of the eight never write the shape at
all. This one feature separates the corpora more cleanly than em dashes.

**2. Sentence rhythm is bimodal.** AI copy alternates verbless punches of
two to four words ("Actively developed.") with feature enumerations of 25
words or more. Human prose keeps a steadier band. Joel Spolsky also writes
short sentences, but his are full clauses with subjects and verbs.

**3. Enumeration comes in threes, or goes maximal.** Exactly-three lists
run 6 to 16 per 1,000 words in the AI set against 0 to 2 in the baselines,
about nineteen-fold on the corpus averages with no overlap at the edges.
When AI copy exceeds three items it chains five to seven verb phrases with
semicolons, which makes wacli and crabbox the semicolon outliers at 11 to
16 per 1,000 words while every human text stays under 3.

**4. The em dash is a one-directional tell.** The corpus averages differ
roughly eighteen-fold, and the heaviest page (clawpatch) lands one em dash
every sixteen words. But three AI pages use fewer em dashes than the 2016
ripgrep README and gogcli uses none, so a page drowning in dashes is
almost certainly generated while a page without them proves nothing.

**5. First person and lexical diversity are register signals.** Against
essays alone both looked like strong tells: the whole AI set contains a
single first-person word while every essay has a narrator. The pre-LLM
READMEs broke both metrics. The Requests README has zero first person and
scores a type-token ratio right among the AI pages. What survives is the
qualitative human tendency to repeat deliberately for emphasis (Joel opens
three consecutive paragraphs with "You are throwing away..."), while
generated copy swaps in a fresh synonym at every mention.

**6. One skeleton ships across the ten sites.** "Pick your path" appears
on six sites, a "five minutes" time-to-value promise on seven, a "Status"
section on eight, and the exact closer "Released under the MIT license."
on six. Each page looks fine alone. Side by side they reveal a house style
produced by one prompt.

**7. Openings defer identity.** The solmaz.io claim holds with a nuance.
All three pre-LLM READMEs establish identity in their opening lines
("ripgrep is a line oriented search tool...", "Requests is the only
Non-GMO HTTP library...", Redis's first section heading is literally
"What is Redis?"). Among the ten AI pages exactly one (clawpatch) opens
with a copula. Four open with headless noun-phrase fragments that carry
category information with no subject and no verb (gitcrawl, spogo, wacli,
goplaces), and the remaining five open with imperative benefits or setup
instructions. Counting sentences where the tool name is the grammatical
subject, action predicates outnumber identity predicates 26 to 5 across
the AI set. The raw ratio alone does not separate the groups, because
body prose about a known subject is naturally verb-led (SQLite runs 18 to
2). The tell is positional.

**8. Heading style inverts the expected offense.** Classifying all 94 AI
headings and 80 human headings against the write-monograph title rules
produced an inversion. Title Case belongs to the humans here, appearing in
8 of 39 SQLite headings ("Boundary Value Tests") as a convention of its
era, while the AI pages already write sentence case. The AI headings fail
differently. About a third are rhetoric rather than labels, against one in
ten for the humans, and the human flags are mostly mild FAQ questions
("Why should I use ripgrep?"). The comma couplet, a parallel two-beat
slogan ("Local loop, remote box", "Two jobs, one binary", "Small surface,
clear split"), appears eleven times across five AI sites and once in the
human set, as the deliberate title "Maker's Schedule, Manager's Schedule".
Imperative slogans ("Pick your path", "Reuse what's warm") and wh-frames
("Why spogo", "What you get") fill out the rest, and gitcrawl stamps one
frame four times in a row ("I want to try it / wire up an agent / triage
a busy repo").

**9. Sentence flow separates the corpus without tuned constants.** Split
each sentence at its punctuation and keep the longest piece, the longest
run of words with no pause. Rank that run against every run in the pooled
corpus and average the percentiles per document (`analyze_flow.py`). This
is the Mann-Whitney rank statistic of the document's runs against the
corpus, and it separates the groups completely: AI pages score 0.19 to
0.41, human texts 0.49 to 0.73, with leave-one-out at 18/18. Human prose
keeps producing sentences with one long unbroken run; the AI pages break
nearly every sentence before a run develops. The metric came out of an
autoresearch-style search (`autoresearch/`, about fifty logged
experiments). The negative results matter as much: every statistic of
pure order (alternation, turning points, autocorrelation) fails, and a
sliding-window generalization that multiplies consecutive percentiles
collapses back to the plain mean once its scale is normalized. The run
lengths carry the whole signal.

## Long-form tweets in the wild

A third corpus group (`corpus/tweets/`, built by `sample_tweets.py` from
the private xtap-store archive) holds one sample per account: every
original long-form tweet (>280 chars), date-sorted, for the 42 accounts
with at least 2,000 words of such text. There is no ground truth for
these. Applying the page detector unchanged, seven of the 42 accounts
trip it: four cross the triad line (topped by 5.4 per 1,000 words) and
three cross the labeled-bullet line (topped by a 78% share), and none
crosses both, unlike the landing pages where every document sat far past
both thresholds at once. The bullet share rests on smaller counts in the
feed, since threads carry far fewer bullets than landing pages, and one
flagged account crosses on just two labeled bullets, so the thresholds
transfer but the confidence does not. The motivating account (analogalok)
is one of the three past the bullet line, with 41 labeled bullets out of
90 (46%) while its dash and triad rates sit mid-field. Its long posts
also share a hook template ("Let me explain", "It's not X. It's Y.")
that these counters do not measure.

## A minimal detector

Two thresholds each classify all eighteen documents correctly on their
own: exactly-three lists above 3 per 1,000 words, or labeled-bullet share
above 30% of bullets. The em dash dropped out of the detector because its
absence clears nothing (see finding 4), and first person dropped out as a
register signal (finding 5). With eighteen documents these numbers are
still hypotheses rather than a validated classifier. The register
objection is partially addressed by the three pre-LLM READMEs, which sell
tools the way the AI pages do; the natural next escalation is a large
sample of post-LLM, human-written landing pages.

## Contents and reproduction

The corpus lives in `corpus/ai/` (the ten site pages, fetched 2026-07-13),
`corpus/human/` (the eight baselines; the essays were fetched by
`fetch_human.py` or by hand, the READMEs from raw.githubusercontent.com at
their tags), `corpus/tweets/` (the 42 account samples, built by
`sample_tweets.py` from a private tweet archive), and `corpus/self/` (the
blog post itself, archived as measured).

To reproduce the numbers, run `python3 analyze.py`, which writes
`results.json` and prints the per-document table. `analyze_ontology.py`
covers finding 7, `analyze_headings.py` covers finding 8, and
`analyze_lexical.py` (run via `uv run --with wordfreq python3
analyze_lexical.py`) writes `results_lexical.json` with MTLD lexical
diversity, word length, syllable, readability, and Zipf word-frequency
metrics. `analyze_flow.py` covers finding 9 and writes
`results_flow.json`; the search that produced the metric, with its frozen
harness, feature files, and experiment journal, is preserved under
`autoresearch/`. `export_web_data.py` writes `figures/data.json`, the compact
per-document dataset behind the blog post's interactive Chart.js
figures, and `render_figures.py` renders the blog figures into
`figures/` (it needs matplotlib and adjustText, for example via `uv run
--with matplotlib --with adjustText python3 render_figures.py`). All
scripts resolve the corpus relative to the repository root.

## License

[MIT](LICENSE)
