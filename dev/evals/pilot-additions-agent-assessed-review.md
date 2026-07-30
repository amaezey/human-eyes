# Pilot additions: agent-assessed and deterministic review

Date: 2026-07-12

Scope: the ten pilot-addition genre pairs only, using the retained literal-first uncoached AI responses and their matched human sources. The current approved checker has 50 deterministic checks and 15 agent-assessment records. No equivalent established-corpus agent execution through the skill exists, so this report makes no cross-corpus agent-performance claim. Internal schema fields retain the existing `semantic_*` names; this report calls the stored judgments agent-assessed because an agent supplied them.

## Validation status

- 20 source-bound work bundles were rebound to the updated checker.
- 300/300 agent answers passed the current native schema and evidence-substring validation.
- Every resulting audit reports `coverage_mode: full` and `audit_status: complete`.
- Schema validity means the agent supplied an allowed answer with source-bound evidence. It does not establish that the judgment or explanation is correct.

## Aggregate result

The retained pilot-addition agent judgments flag 11/150 human answers and 14/150 AI answers. They are descriptive counts, not a validated performance result. The document-level review below is useful for identifying supported judgments, overcalls and likely false negatives, but there is no corresponding established-corpus agent run to compare them with.

| Agent-assessment record | Human flags | AI flags | Review |
|---|---:|---:|---|
| tonal_uniformity | 3 | 9 | Overused by the agent; most answers cite one sentence, which cannot demonstrate whole-document uniformity. Uniform register is also genre-appropriate in reports and professional email. |
| performed_candour | 1 | 0 | Human finding is supported by the explicit `Honestly` frame. |
| referential_clarity | 1 | 0 | Human finding is supported: `they` and `that` have loose competing referents. |
| semantic_redundancy | 1 | 1 | Both findings are supported, although repetition of key findings in a government report can be deliberate structure rather than misuse. |
| generic_metaphors | 2 | 0 | Human findings are arguable; zero AI findings is not credible after document review. |
| even_jargon_distribution | 1 | 1 | Both report findings are supportable but need comparison across multiple passages, not a single phrase. |
| underspecified_language | 1 | 2 | The cited criteria gaps are supported. |
| genre_specific | 1 | 1 | Genre taxonomy caused questionable mappings: memoir was treated as journalism and cultural criticism as academic because neither genre is available directly. |
| all other records | 0 | 0 | Several all-clear sets, especially faux specificity and formulaic parallelism, contain likely false negatives. |

## Systemic agent-treatment problems

1. **Single-sentence proof for document-level state.** Every tonal-uniformity flag cites one sentence. The record asks whether the whole text remains in one register, so one sentence is insufficient evidence.
2. **Uniformity treated as intrinsically bad.** The agent flags consistent register in professional email, government reporting, workplace updates and strategy reports even when consistency fits the genre.
3. **List-shaped agent checks are underused.** Across 20 documents the agent returned zero faux-specificity and zero formulaic-parallelism findings. Multiple AI texts contain invented scene detail, repeated balanced clauses and symmetrical paragraph construction.
4. **Genre options are incomplete.** The registry offers academic, student essay, poetry, fiction, journalism, marketing email and default. It lacks memoir, personal essay, workplace update, strategy report, government report and cultural criticism, forcing lossy classifications.
5. **Clear answers lack affirmative evidence.** The schema validates clear states without requiring a short reason or counterexample. This makes false negatives difficult to distinguish from careful review.

## Document review

### 01 Personal reflective essay

- **Human agent finding:** performed candour. Supported by `Honestly, I am much more afraid...`.
- **AI agent finding:** tonal uniformity. The conclusion may be plausible, but the single cited sentence does not prove it.
- **Likely AI omissions:** faux specificity in the unnamed neighbour/council narrative; formulaic parallelism in repeated `who...` clauses; generic metaphors such as unfairness arriving and a pattern having weight.
- **Deterministic treatment:** both sides trigger individual triads and cross the density threshold. The AI also triggers anaphora and negative parallelism; the human triggers performed candour and staccato sequences.

### 02 Lived-experience memoir

- **Human agent findings:** generic `journey` metaphor is supportable; journalism classification is a forced taxonomy choice for a memoir/article hybrid.
- **AI agent findings:** none.
- **Likely AI omissions:** faux specificity in the generic first-computer scene; formulaic three-beat action sequences; generic `map out of the wilderness` and `sealed object` metaphors.
- **Deterministic treatment:** both sides contain recognized triads; the AI also triggers paragraph-length uniformity and crosses the triad-density threshold.

### 03 Personal newsletter

- **Human agent findings:** none; reasonable.
- **AI agent finding:** tonal uniformity, supported only by one sentence.
- **Likely AI omissions:** balanced-concession scripting (`That is the point, and also the loss`) and tidy parallel construction around the changed travel plan.
- **Deterministic treatment:** neither side produces a triad finding after the grammar correction. The human triggers curly quotes; the AI is clear. The removed Markdown-heading indicator no longer penalises the AI title.

### 04 Professional email

- **Human agent findings:** none; reasonable.
- **AI agent finding:** tonal uniformity. Consistent professional register is expected here, and one sentence does not show a defect.
- **Likely AI omissions:** formulaic list symmetry and underspecified claims such as `essential help` and `more reliable approach`.
- **Deterministic treatment:** both sides trigger individual triads, while only the AI crosses the density threshold. The human also triggers curly quotes. Headings and ordinary email structure are no longer counted as evidence.

### 05 Workplace project update

- **Human agent findings:** referential-clarity finding is supported; tonal-uniformity finding is not established by its single sentence and consistency fits the genre.
- **AI agent finding:** tonal uniformity, again based on one sentence and genre-appropriate consistency.
- **Likely AI omission:** highly regular issue/decision scaffolding and balanced list construction.
- **Deterministic treatment:** both sides trigger triads. The AI also triggers curly quotes; the human triggers anaphora and list density, which reflects the real update format rather than authorship.

### 06 Business strategy report

- **Human agent findings:** even jargon and underspecified `effective and fit-for-purpose` are supported; tonal uniformity is expected in a formal report and under-evidenced.
- **AI agent findings:** even jargon and three underspecified evaluations are supported; tonal uniformity is expected and under-evidenced.
- **Likely AI omissions:** repeated paragraph template (`area of work` → explanation → implication), redundant recap in the final paragraph and vacuous connective claims.
- **Deterministic treatment:** the human triggers six findings versus two for AI, driven partly by human punctuation, repeated `This` chains, anaphora and triad density. This pair requires careful per-check interpretation rather than aggregate scoring.

### 07 Marketing/customer communication

- **Human agent findings:** none.
- **AI agent findings:** underspecified speed/memory/smoothness claims are strongly supported; tonal uniformity is under-evidenced and appropriate to release communication.
- **Likely AI omission:** repeated feature-paragraph formula and balanced performance claims.
- **Deterministic treatment:** human formatting, copula avoidance, filler and list structure produce four findings versus one AI triad finding. The deterministic catalogue currently misses several unsupported performance claims that the agent-assessed layer catches.

### 08 Student academic essay

- **Human agent findings:** none.
- **AI agent finding:** tonal uniformity, based on one sentence.
- **Likely AI omissions:** faux autobiographical specificity, symmetrical contrast between formal/material access and personal/structural explanation, and generic metaphors such as a hidden curriculum.
- **Deterministic treatment:** both sides trigger triads. AI additionally triggers density, negative parallelism and em dashes; the human additionally triggers curly quotes and significance inflation.

### 09 Cultural criticism

- **Human agent finding:** `meaning peeled away` is a real metaphor but is grounded in a specific translation argument; treating it as generic is questionable.
- **AI agent findings:** tonal uniformity is under-evidenced; academic classification is a forced substitute for cultural criticism, making the uncited-claim watchlist finding questionable.
- **Likely AI omissions:** generic translation-as-vehicle metaphors, repeated balanced sentence structures and restatement of selection/translation/reception.
- **Deterministic treatment:** both sides trigger contrast and triad patterns; the AI additionally triggers copula avoidance and density.

### 10 Government report

- **Human agent findings:** semantic redundancy is factually supported but expected between key findings and body results; tonal uniformity is genre-appropriate and under-evidenced.
- **AI agent findings:** semantic redundancy is supported; tonal uniformity is genre-appropriate and under-evidenced.
- **Likely AI omissions:** underspecified phrases such as `well-connected care`, `more apparent`, and `practical points`, plus repeated report-paragraph templates.
- **Deterministic treatment:** human source formatting and vocabulary produce five findings versus three for AI. The AI now also crosses the triad-density threshold. Removing Markdown headings helps, but curly quotes, em dashes and generic-conclusion rules still favour the AI sample in this pair.

## Deterministic versus agent-assessed disagreement

- Triads are now surfaced on every document where the construction appears, regardless of author. Density is reported separately.
- Quoted triad candidates remain detectable and carry a `quoted` field in candidate evidence. Quotation changes interpretation, not recognition.
- Deterministic checks catch formatting, punctuation and repeated surface structures that sometimes occur more often in source-published human prose.
- Agent-assessed checks catch unsupported evaluative claims that deterministic matching cannot reliably assess, especially in the marketing and strategy pairs.
- The retained agent over-relies on tonal uniformity and under-reports faux specificity, formulaic parallelism and generic metaphor use in AI prose.

## Evaluation implication

The 20 pilot-addition audits are structurally complete, and their document review identifies genuine treatment problems. They cannot support a numeric comparison with the established corpus because no equivalent established agent execution exists. This run appears to undercall faux specificity and formulaic parallelism, while its single-sentence tonal-uniformity judgments remain under-evidenced. Any comparative run must preserve raw agent executions through the skill on both corpora, use the same instructions, and evaluate them against a separately reviewed reference set. Deterministic results remain independently reproducible and should be reported separately from agent judgments.
