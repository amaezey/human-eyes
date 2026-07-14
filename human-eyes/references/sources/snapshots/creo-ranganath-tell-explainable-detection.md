# Show, Don't TELL: Explainable AI-Generated Text Detection

- **Canonical URL:** https://arxiv.org/abs/2605.27921
- **Alternate access URLs:**
  - https://ar5iv.labs.arxiv.org/html/2605.27921
  - https://arxiv.org/pdf/2605.27921
- **Author / owner:** Aldan Creo and Suraj Ranganath
- **Publisher:** arXiv
- **Published:** 2026-05-27
- **Retrieved:** 2026-07-15
- **Stable identifier:** arXiv:2605.27921v1; DOI 10.48550/arXiv.2605.27921
- **Version / revision:** v1, submitted 2026-05-27
- **Extraction method:** Official arXiv v1 PDF downloaded and converted from its embedded text layer with Poppler `pdftotext -layout`; ar5iv HTML used as an alternate reading and structure check
- **Full-text status:** complete
- **Access and transformation notes:** The arXiv HTML endpoint returned 404. The ar5iv HTML rendering was accessible but duplicated some mathematical values and lost layout in complex figures, so the official 30-page PDF is authoritative. The text below preserves the complete PDF text layer. Multi-column reading order and complex figure layout are mechanically transformed; the preserved PDF retains the authoritative visual structure.

## Full text

```text
                                                                             Show, Don’t TELL:
                                                                   Explainable AI-Generated Text Detection

                                                                         Aldan Creo and Suraj Ranganath
                                                                  School of Computing, Information and Data Sciences
                                                                          University of California, San Diego
                                                                              United States of America
                                                                                 Correspondence: research@acmc.fyi



                                                               Abstract                                      Imagine a professor who submits a student’s es-
                                                                                                          say and receives the verdict: “95% AI”. She might




arXiv:2605.27921v1 [cs.AI] 27 May 2026
                                             Research on AI-generated text detection has                  promptly accuse the student of cheating, having
                                             presented a number of approaches to discern                  used a detector that claims to use “comprehen-
                                             human from AI prose, some of which achiev-
                                                                                                          sive deep learning methodology, trained on exten-
                                             ing high in-distribution performance. However,
                                             real-world applicability has stalled because                 sive text collections” (ZeroGPT, 2026). But when
                                             their outputs are misaligned with the needs of               asked, she cannot explain her reasoning or defend
                                             users, such as professors, who are presented                 it at a hearing; the detector gave her a number, but
                                             with a numeric score that has no attached ex-                no insight.
                                             planation. We tackle this issue with a novel                    The research community has largely focused on
                                             architecture, TELL, that bakes explainability                chasing higher accuracy. Every major detector to-
                                             from the ground-up. While our system still of-
                                                                                                          day outputs a score as a verdict (Figure 1), and
                                             fers a numerical score like other detectors for
                                             comparability, TELL takes a fundamentally dif-               the literature is saturated with models claiming to
                                             ferent approach where we aim to show the user                surpass existing ones. So if accuracy is the answer,
                                             the “tells” by which the model believes a text               why does public trust in detectors remain fragile?
                                             is AI or human-written, to empower the user to
                                             decide who wrote a text using their own judg-                1.1   A “crisis of trust” in detectors
                                             ment and understanding of the context of the                 When reading the literature on AI-generated text
                                             writing and its alleged author. We train TELL                detection, it is possible to find a vast number of pa-
                                             on a custom SFT dataset of domain-specific
                                                                                                          pers reporting near-perfect results on their test sets,
                                             authorship annotations, and further refine the
                                             system using GRPO with curriculum learning                   with a field saturated with new models and tech-
                                             to improve performance. We achieve competi-                  niques claiming to surpass existing ones (Adam
                                             tive performance with state-of-the-art detectors             et al., 2026; Emi and Spero, 2024; Hans et al., 2024;
                                             (AUROC 0.927) while natively providing anno-                 Mitchell et al., 2023; Koike et al., 2023; Hu et al.,
                                             tations that explain the basis for the detector’s            2023; Li et al., 2023; Zhan et al., 2023; Liu et al.,
                                             decision. We further evaluate the quality of our             2023; Hou et al., 2023; Solaiman et al., 2019, inter
                                             explanations using a dataset of human annota-
                                                                                                          alia).
                                             tions and report a high (mean 72.3%) win-rate
                                             on annotation concreteness, falsifiability, co-                  One might naturally assume that detecting AI-
                                             herence, plausibility and grounding, allowing                generated text is “a solved problem”, and democ-
                                             users to critically think and decide for them-               ratizing detectors is enough to respond to the con-
                                             selves. Our work thus reframes the problem of                cerns of, for instance, 76% of Americans who say
                                             AI-generated text detection in a human-centric               it is “extremely or very important to be able to tell
                                             perspective and paves the way for a new family               if pictures, videos, and text were made by AI or
                                             of detectors that focus on native explainability.            people” (Kennedy et al., 2025), 90.4% of people in
                                                                                                          the UK who are concerned about deepfakes (Sippy
                                         1   Introduction
                                                                                                          et al., 2024), or the 87% of EU27 citizens “moder-
                                                  The purpose of computing is insight, not numbers.       ately or highly worried” about fake content created
                                                                                                          by AI (European Parliament, 2026).
                                                                                 Richard Hamming
                                                                                                              However, performance reported by the original
                                           What does “insight” mean when the output of a                  articles does not always stand the test of time and
                                         detector is a single percentage?                                 community scrutiny. For example, while the origi-

                                                                                                      1
         (a) ZeroGPT                     (b) Pangram




                                                                                         (e) TELL
         (c) QuillBot                   (d) Grammarly

Figure 1: Existing AI-generated text detectors (e.g., 1a-1d) only give users a prediction in a binary scale. In contrast,
TELL (1e) provides readable explanations for each decision, so users can understand them and make their own call.

→ For instance, the example above (from Wang et al. (2024), written by BLOOMZ) might pass off as human-written
at first glance. But it says that “NFS [. . . ] uses two servers [. . . ] with one acting as both the server and the other as
the client” — a clear contradiction (and a signal of AI generation). TELL is the only detector that can point out this
kind of specific evidence and let the user judge it themselves.


nal Fast-DetectGPT (Bao et al., 2024) paper reports              dasaini, 2024; Weber-Wulff et al., 2023; Sadasivan
a 0.9887 AUROC, Tufts et al. (2024) report a lower               et al., 2023, inter alia). In fact, a part of the student
0.8405, Wu et al. (2024) 0.5533, and Chen et al.                 body has grown increasingly worried of being mis-
(2025b) 0.4632. This might be due to a multitude                 takenly accused of academic integrity violations
of reasons, such as selective reporting, dataset cu-             — with some talking about a “witch hunt” in the
ration or other methodological choices that inflate              educational system — and thus try to, among other
results, datasets turning increasingly challenging               things, add typos to their work, “dumb down” their
over time, generator models progressively reduc-                 writing, or use online “AI humanizers” that claim
ing the human-AI language modeling gap, or other                 to make AI-generated text appear more human-like
“perverse incentives” that can shape the publication             (even if their text was human to begin with) (Waters,
dynamics of a “hot” research community (Ioanni-                  2026; Kingkade, 2026; Friedman, 2026; Scibilia,
dis, 2005).                                                      2025).
                                                                    We are not claiming that all detectors are inac-
   In fact, recent public incidents show how AI-
                                                                 curate, but rather that even the best ones can fail in
text detectors fail in real settings, including false
                                                                 practice. For instance, back in 2023, several news
accusations and inconsistent results across tools
                                                                 outlets reported that detectors were incorrectly flag-
(Chen, 2026; Mingay, 2026; University of San
                                                                 ging the US Constitution as AI-generated (Univer-
Diego Legal Research Center, 2025; NPR, 2025;
                                                                 sity of San Diego Legal Research Center, 2025;
Mathewson, 2025; Weinberg, 2025; Ardito, 2023;
                                                                 Wood, 2024; Naprys, 2024; Jiang, 2023; Edwards,
Scarfe et al., 2024; Fowler, 2023, inter alia), as
                                                                 2023, inter alia). This was fixed by subsequent
detectors tend to struggle with out-of-distribution
                                                                 work, but the damage was already done; currently,
examples such as unseen domains, obfuscated or
                                                                 a substantial part of the public is skeptical about
paraphrased texts, or texts produced by newer mod-
                                                                 the reliability of detectors or simply avoids using
els (Pudasaini et al., 2026; Shekhar et al., 2026;
                                                                 them altogether (Shepherd, 2025; Roe et al., 2024;
Ranganath and Ramesh, 2026; David and Gervais,
                                                                 Geng and Poibeau, 2025).
2025; Ayoobi et al., 2024; Burger et al., 2025;
Huang et al., 2024; Dugan et al., 2024; Creo and Pu-                We call this a “crisis of trust” in AI-generated

                                                             2
text detection: one visible failure can damage trust              text detection.
far more than many correct predictions can rebuild
it. And the mistrust is aggravated when the only               • TELL is trained on a custom SFT dataset of
output of the model is a numeric score and users                 domain-specific authorship annotations, and
can’t understand why a model misclassified a text                further refined using GRPO with curriculum
— in the case of the US Constitution example, users              learning to improve performance.
could arguably have been more forgiving if the de-             • TELL achieves state-of-the-art performance
tector had explained that “I know this text” and thus            (Section 3.1) — but most importantly,
an AI could have memorized it. Instead of “this                  TELL gives users high-quality, explained ev-
detector doesn’t work”, users might think, “this is              idence (Section 3.2) that allows them to un-
an edge case, so it’s normal that the detector got               derstand the reasons behind the verdict, and
it wrong”. And yet, even though public discourse                 gives them the ability to judge on their own.
and the scientific literature have repeatedly pointed
out that explainability is a “major issue” (Thom-              • TELL may serve as a didactic tool to train
son et al., 2025; Anlen and Wojciak, 2025; Saha                  users in AI-generated text detection, as prior
and Feizi, 2025; Ji et al., 2024), to the best of our            research has shown that after training, humans
knowledge, existing work has failed to frame AI-                 may be accurate detectors themselves.
generated text detection around explainability as
its core design goal.                                          • We openly release our code, data and weights
                                                                 (https://github.com/ACMCMC/TELL) to fa-
1.2   Building trust with explainability                         cilitate research in explainable AI-generated
                                                                 text detection, as well as an interface (https:
With TELL, our goal is not to claim near-perfect
                                                                 //ai-tells.tech) to make it accessible.
detection, since (1) all detectors can fail and need
human oversight; (2) many need retraining as new
models are released; (3) we find that related work          1.3   Related work
claims high performance that does not replicate in          To the best of our knowledge, no existing work
our experiments or (arguably) the real world; and           explicitly frames AI-generated text detection as an
most importantly, (4) focusing on accuracy alone            explainability problem, but there are some works
misses the point of why people use AI detectors,            related to this view.
i.e., to make decisions in the real world. Instead,
we design an architecture that returns a verdict            Reasoning in LLMs. The shift from direct gen-
together with specific evidence, so users can see           eration to reasoning-based responses in LLMs mir-
why the model made that decision and check it               rors what we propose. Reasoning models were mo-
themselves.                                                 tivated (among other factors) by the desire to make
   In fact, we believe that the utility of TELL goes        them more interpretable by showing how they ar-
beyond just being a more explainable detector.              rive at their conclusions (OpenAI et al., 2026; Guo
While several authors have reported that humans             et al., 2025; Wei et al., 2023). We take inspiration
are not accurate AI detectors (Fiedler and Döpke,           from that shift, moving from a direct classification
2025; Cooke et al., 2025; Cheng et al., 2025; Frank         to one based on interpretable evidence.
et al., 2023), this assumption has been challenged          Prompt inversion. Chen et al. (2025a) proposed
(Russell et al., 2025; Milička et al., 2025). Recent       a method to detect AI-generated text by inverting
work has shown that humans that undergo some                the prompt and checking if the model can recon-
kind of (possibly informal) training process can            struct the original input. However, we argue that
show high degrees of accuracy. In this context,             (1) this method is not designed to provide explain-
TELL can help users learn, since it gives detailed          ability to users, and (2) it may mislead them by
explanations that allow them to generate their own          “finding a generating prompt” even when the text
mental model of what AI-generated text looks like,          is human-generated — which “primes” them into
and thus become better detectors themselves.                believing whatever the model outputted.
   Therefore, our contributions are as follows:
                                                            Attribution. Some works have explored attribu-
   • We propose a novel architecture, TELL, that            tion methods to find which parts of a text are most
     puts explainability at the core of AI-generated        indicative of AI generation. For example, prior

                                                        3
            AI                          Human
          This is a                          This is a
          sentence.                          sentnece.




                                                                                                   “Compare these two documents
                      GPT-5.5                                                                      and annotate the differences.”
                                                                                                                                                                                                                                                      Curriculum
       <text>This is a
       <span>sentnece<annotation
       type="human" why="typo; AI is
       unlikely to produce it because it                                                                                                                                                             Compute                                          Compute
       breaks tokenization" score="0.85"                                                                                                                 GRPO update
       /></span>.<verdict type="human"                                                                                                                                                              advantages                                        rewards
       why="This is a short sentence, but
       the typo gives it away." score="0.85"
       /></text>




                                                                                                                                                                “Annotate this document
              GPT-OSS-120B (OpenAI, 2025)                                                                                                                       following the format. . . ”


                                                                                                                                                 n>n ?
                                                                                                                                                                                                         Tag token types
                                                                                                                      0   . 9 1 "/ > < / s p a           0.91
                                                                                                            o" score="
                                                                      no t a t i o   n type="human" why="typ
                                                             an>am<an                                                                                                                                                               why annots.
                                        his prose AI or hu<sp
                                                                                                                                                                                                Is this prose AI or hu
                                 Is t

                             Is thi
                                    s prose <span>AI or huamn<annotat
                                                                     io n t y p e = " h u
                                                                                            man" why="atypical" score="0.72"/></span>?
                                                                                                                                                         0.72           Fix format
                                                                                                                                                                                                <span>am<annotation
                                                                                                                                                                                                                                                  Grok-4.1 (fast)
       Is this text            Is this prose <span>AI or human<annotation type="AI" why="ambiguity" score="0.50"/></span>?
                            Is th                                                                                                                        0.50    human → huamn                  type="human" why="typo"
       AI or huamn?           <sp
                                 is <span><span>prose<annotatio
                                                                 n type="AI
                                                                           " why="formal" score="0.31"/></s
                                 an>I
                                     s<ann
                                          otation type="AI" why
                                                                ="capita
                                                                                                           pan> AI or huamn?
                                                                                                                                                         0.37    <span><span> → <span>          score="0.91" /></span>n?
                                                                        lized" s
                                                                                core="0.71"/></span> this p
                                                                                                            rose AI or
                                                                                                                       huamn?
                                                                                                                                                         0.14                                                                                     “How credible is
                                                                                                                                                                                              • doc • struct • type • why • score
                                                                                                                                                                                                                                                  this annotation?”


Figure 2: Our approach. We start by generating a dataset of annotation examples that we use to fine-tune
a pretrained LM. That intermediate model is not able to reliably identify AI-generated text (AUROC 0.638,
TPR@1%FPR 0.0), but has learned the general task setup. We further refine it with reinforcement learning (GRPO)
till convergence. The resulting model is reasonably accurate (AUROC 0.927, TPR@1%FPR 0.638) — but most
importantly, explainable by design.


work used SHAP (Najjar et al., 2025), while Yan                                                                                                                                      SFT data. We first train our model on the task
et al. (2025) used Layer Integrated Gradients to                                                                                                                                     mechanics with SFT on annotated span examples.
measure neuron contributions via gradient attribu-                                                                                                                                   To the best of our knowledge, no dataset exists
tion. But all these methods are post-hoc: the model                                                                                                                                  that provides AI/human annotated text with span-
produces a score first, and then attribution tries to                                                                                                                                level annotations and natural language explana-
explain it after the fact, which is non-trivial and can                                                                                                                              tions. Therefore, we built our own dataset on top
easily lead to unfaithful explanations. In contrast,                                                                                                                                 of the EditLens (Thai et al., 2025) dataset, which
we build explainability from the ground up; it’s                                                                                                                                     pairs human text with AI-edited variants. We use
inherent to our model. NOTAI.AI (Breneur et al.,                                                                                                                                     GPT-5.5 to compare each pair and generate span-
2026) provides a similar approach by integrating                                                                                                                                     level annotations, for both the human and the AI-
curvature-based signals with neural and stylomet-                                                                                                                                    edited document. We limit this to 2000 examples,
ric features for explainability, though this is done                                                                                                                                 partly because generation is expensive, but mostly
through XGBoost and SHAP attribution given to an                                                                                                                                     because the goal of this stage is just to teach the
LLM to write the explanations a posteriori. Simi-                                                                                                                                    model the tell-annotation format, not to build an
larly, Yuan et al. (2025) proposed EMMM, a frame-                                                                                                                                    accurate detector yet. Additionally, we combine it
work where they use Faith-SHAP to select salient                                                                                                                                     with the dataset by Russell et al. (2025). It contains
tokens and convert them into natural language us-                                                                                                                                    300 documents of human annotators indicating not
ing templates. However, their work focuses on                                                                                                                                        only whether they think a text is human or AI-
customer service chatbot interactions, and the ex-                                                                                                                                   generated, but also their natural text commentary.
planations are also post-hoc.                                                                                                                                                        We take 100 elements from it to generate additional
                                                                                                                                                                                     SFT examples with GPT-5.5 and GPT-5.4, using
2     Methods                                                                                                                                                                        a prompt where we ask the model to annotate the
                                                                                                                                                                                     document based on the final commentary (since
In this section, we describe how we collect data                                                                                                                                     the dataset doesn’t contain annotated spans, which
and train and evaluate TELL.                                                                                                                                                         is a key motivation for our work). Each example
                                                                                                                                                                                     contains the verdict of 5 annotators, but we filter
2.1    Datasets                                                                                                                                                                      the commentaries that are shorter than 50 words
We use two sources of data at different stages:                                                                                                                                      to ensure that the model has enough information


                                                                                                                                                                               4
   Source                                     License          Primary role in corpus                               Rows
   RAID (Dugan et al., 2024)                  MIT              Multi-domain and adversarial benchmark            7,654,920
   COLING 2025 (Alam et al., 2025)            Apache-2.0       Multi-domain (aggregates Li et al. (2023); Guo      872,525
                                                               et al. (2023); Wang et al. (2024))
   OpenLLMText (Chen et al., 2023b)           cb 4.0           Web text with human/AI labels                      344,530
   AuTexTification (Sarvazyan et al., 2023)   cbna 4.0         Multi-domain detection data across social, re-     107,868
                                                               view, news, legal, and how-to domains
   OUTFOX (Koike et al., 2023)                Apache-2.0       Student essays with LLM generations and ad-         63,600
                                                               versarially generated attacks
  Pangram EditLens (Thai et al., 2025)        cbna 4.0         Human-written and AI-generated corpus               51,115
  (human_written and ai_generated
  rows)
  DAIGT-v2 (Kłeczek, 2023)                    MIT              Student-essay style human/AI texts                  44,864
  AI-and-Human-Generated                      MIT              Academic abstracts                                  28,662
  Text (Theocharopoulos et al., 2024)
  Ghostbuster Essay (Verma et al., 2023)      cb 3.0           Human and AI-written essays                           7000
  ArguGPT (Liu et al., 2023)                  cb 4.0           GPT-generated argumentative essays                    4038
   Total                                                       Our RL corpus                                     9,179,122

                  Table 1: Source datasets in our training corpus after filtering and normalization.


to generate annotations from. This results in 316                Detector               AUROC (95% CI)          TPR@1%FPR
additional SFT examples. We include the prompts                  TELL (ours)            0.927 [0.919, 0.935]           63.8
in Appendix B.                                                   MAGE                   0.913 [0.904, 0.922]            4.2
                                                                 Pangram-EditLens       0.911 [0.903, 0.919]           58.3
                                                                 Fast-DetectGPT         0.861 [0.850, 0.872]           59.0
                                                                 ArguGPT                0.828 [0.816, 0.840]           43.3
Reinforcement learning (RL) and test data.                       T5Sentinel             0.802 [0.790, 0.814]           17.5
                                                                 DetectLLM-NPR          0.782 [0.769, 0.795]           32.0
We build a unified dataset aggregating 10 public                 OpenAI RoBERTa         0.777 [0.764, 0.789]           33.1
sources spanning 15 domains (e.g., academic ab-                  AIGC MPU               0.774 [0.761, 0.787]           11.6
stracts, creative writing, news, student essays. . . )           DetectLLM-LRR          0.763 [0.749, 0.776]           27.2
                                                                 LogRank                0.757 [0.744, 0.771]           23.2
for a total of 9.2M rows (Table 1). However, our                 RADAR                  0.744 [0.730, 0.758]            1.3
source datasets have very different sizes, so if we              ChatGPT-D              0.697 [0.682, 0.711]           16.6
were to sample uniformly, our model would learn                  Binoculars             0.616 [0.601, 0.632]            1.4
                                                                 DNA-GPT                0.581 [0.566, 0.595]            0.0
to exploit the features in e.g. RAID rather than                 PHD RoBERTa            0.521 [0.505, 0.537]            4.6
generalizing. So instead of drawing proportionally
or equally (ignoring dataset size), we (1) define               Table 2:    Comparison of detection methods.
strata based on the combination of dataset and do-              TELL achieves the best scores (metrics: higher
main,   and (2) allocate examples per stratum by                is better).
√
  stratum size as the geometric mean of the two.
We generate three splits with the same policy on
                                                                2.2     Model architecture and training.
scale, and ensure a 50/50 balance of AI/human
examples.                                                       2.2.1    Supervised fine-tuning
   The validation and test sets contain 5,000 exam-            We used the examples generated (Section 2.1)
ples. We chose this number based on statistical                for the supervised fine-tuning (SFT) step on
power: when collecting data, we assumed approxi-               GPT-OSS-120B (see Appendix C for details). We
mately 10 detectors in our comparison, for a total            also include the real human comments by Russell
of 102 = 45 pairwise comparisons. Using the De-
                                                               et al. (2025).
Long variance formula and Benjamini–Hochberg                      Additionally, we include an extra CE loss on
FDR correction at q = 0.05, this gives 86–99%                  “hint” following: during the RL stage, we artifi-
power to detect a ∆ = 0.04 AUROC gap, the small-               cially inject the document label in some of the
est difference we consider practically meaningful              rollouts, so that the model has signal on what the
for a deployed detector. We do this to achieve a bal-          correct annotation should be. Otherwise, the vari-
ance between minimizing computational costs and                ance of the reward might be too small and the
ensuring that we have sufficient statistical power to          model might collapse, e.g. if the model is strongly
assess model performance.                                      confident on a wrong label. For that, we train on

                                                           5
dual pairs of examples of text where there is a hint          batch size without additional expensive decoding.
(“Text origin is AI/human”) in the reasoning sec-
                                                              Format collapse. We found that the model can
tion, and the only token that is optimized is the
                                                              sometimes collapse to a degenerate behavior, where
final verdict token (either “AI” or “human”). This
                                                              it, for example, “corrects” grammatical errors in the
way, the model learns to associate the hint with the
                                                              input by generating the corrected version instead,
correct label, and we leverage this during the RL
                                                              or simply repeats structural tokens, or hallucinates
stage to provide a stronger learning signal.
                                                              a false output. To address this, we implemented
2.2.2   RL training                                           a format-fixing pipeline that detects and corrects
After SFT, we further refine the model with GRPO              wrong-format rollout (up to a 10% difference), and
(Shao et al., 2024), where we aim to progress                 we use the format-fixed version for GRPO updates,
from a model that is familiar with the task for-              and we then apply an additional cross-entropy loss
mat, though not accurate, to one that can reliably            gradient up to the corrected version’s doc-copy
identify AI-generated text and provide high-quality           and structural tokens (the annotations are zeroed
annotations. We describe our main methodolog-                 out), so that the model is reinforced to produce
ical choices (which substantially deviate from a              correctly-formatted text. Initial experiments where
standard GRPO implementation) in the following                we applied the reward directly with a reward of 0
paragraphs.                                                   for wrong-format rollouts led to a complete col-
                                                              lapse, since differences are frequently small (e.g.,
Curriculum. Not all training documents are                    a missing comma), and GRPO was negatively rein-
equally informative at every stage of training. Doc-          forcing all tokens in those wrong rollouts when the
uments where the model always fails or succeeds               culprit was only a small fraction of them.
have no group variance (thus give zero GRPO gradi-
ent). We therefore implement a curriculum (Bengio             Per-Token Advantage Decomposition. In our
et al., 2009) that dynamically prioritizes the strata         output, tokens perform different roles depending
where documents show the maximum reward vari-                 on their position. For instance, in
ance, in line with the approach by Emi and Spero                   <text>This   <span>is<annotation
(2024), who showed it can be highly effective to                   type="human"        why="reason"
maximize model learning in developing the Pan-                     score="0.12" /></span> an. . .
gram detector.
                                                              the first token <text> is structural — it always ap-
   Our training data is heterogeneous, spanning
                                                              pears at the beginning. Then, TELL should start
multiple datasets and domains (see Section 2.1), so
                                                              copying the original document text — either writ-
we first partition documents into strata by dataset
                                                              ing the same token as in the original document
and domain. For each stratum, we maintain an
                                                              (This), or choosing to open a span (<span>). Af-
EMA of the classification reward as a proxy for
                                                              ter opening a span and copying the tokens inside,
difficulty. We then sample strata using a Gaussian
                                                              <annotation type=" is a structural token again,
curriculum window centered at a target difficulty τ ,
                                                              but then the model needs to write the annotation
which linearly ramps from τstart = 0.35 to τend =
                                                              type (human or AI), another structural token, and a
0.70 over the first 50 training steps; the model starts
                                                              potentially long explanation (reason), etc.
training on moderately hard strata and as training
                                                                 If we were to apply a single scalar advantage
progresses, it is given harder examples. Within
                                                              across all tokens, the model would receive the same
each selected stratum, we use a UCB exploration
                                                              learning signal for all of them, which in practice
term to also ensure that we have coverage of less-
                                                              leads to format collapse. In all rollouts, better and
visited strata (to avoid local optima).
                                                              worse, the model should still reproduce the origi-
Replay. We additionally maintain a cache of suc-              nal document text — and if we were to negatively
cessful rollouts (up to 6000 entries), from which             reward in some rollouts, then it would get a contra-
we sample a growing fraction of each batch (start-            dictory signal (“you should only write the original
ing at 35%, ramping to 50% by step 80). This                  document when you’re correct”). The same rea-
way, we stabilize the gradient signal by mixing               soning applies to structural tokens and annotation
fresh rollouts with those where reward variance               tokens. The “tasks” performed by different tokens
was maximized (i.e., the model had the most learn-            are different, and thus they require different learn-
ing potential), and we also increase the effective            ing signals.

                                                          6
   Therefore, we assign each token an advantage                                      Judge                                                     Win rate (%) [95% CI]
based on its structural role, using independent
reward pools per token type. We always give                                          Panel mean                                                                         72.3 [68.3, 76.2]
document-copy tokens zero advantage: the model                                       GPT-5.4-mini                                                                       78.3 [73.9, 82.4]
should reproduce the original text regardless of out-                                Gemma 4 26B                                                                        67.5 [62.6, 72.1]
put quality, and rewarding or penalizing this would                                  DeepSeek V4 Flash                                                                  75.3 [70.8, 79.5]
introduce contradictory signal1 . We also give struc-                                Nemotron Super                                                                     66.3 [61.5, 70.8]
tural tokens a small fixed positive advantage to                                     GPT-OSS 120B                                                                       74.1 [69.5, 78.4]
reinforce the adherence to our format.
                                                                      Table 3: Win rate vs. human experts.                                                                                                     95% CIs:
Reward functions. We only optimize rollouts                           document-level bootstrap (B = 10,000).
with a valid format, and we assign independent
rewards to each token type (Section 2.2.2). For                                       0.3                                                                                                                              AI why
                                                                                                                                                                                                                       human why
type tokens, we model the reward as the product                                       0.2

of the rubric credibility and the label alignment:                                                 opener starts

                                                                                                         starts broad              even when
                                                                                                                                                                formatting tell       next sentence

                                                                                                                                                                                       strong formatting
                                                                                                                                                                                                               missing space

                                                                                      0.1                                                                                                                      space after

c · (+1) if the annotation type matches the docu-                                                                  very common
                                                                                                                      very clean
                                                                                                                                                   which common


                                                                                                                                                             trying make
                                                                                                                                                                        comma before
                                                                                                                                                                                             formatting slip

                                                                                                                                       person writing                                  small formatting
                                                                                                                                                                      strong tell

ment label, and c · (−1) + 1 if it does not. This                                     0.0
                                                                                                                                         old fashioned                     model usually




                                                                       component 2
                                                                                                                                                                                           makes text
                                                                                                                                                                  model trying


way, a high-credibility but of the label opposite to                                 −0.1
                                                                                                                                   very specific
                                                                                                                                                        rather than     which makes
                                                                                                                                                                         than model




the document (i.e., the model identified high qual-                                  −0.2

ity evidence that happens to contradict the over-                                    −0.3

all label) receives only a small penalty, while a
                                                                                     −0.4
low-credibility wrong-type annotation receives the
                                                                                     −0.5
strongest negative signal. For the annotation and
                                                                                            −0.4               −0.2                             0.0                                   0.2                                0.4
verdict explanation tokens, the reward is the prod-                                                                                          component 1


uct of the rubric credibility and a quality gate based
                                                                      Figure 3: What TELL writes. There is human/AI sep-
on length and repetition across annotations. We
                                                                      aration, with specific “attributes” relating to each (e.g.,
get the credibility score from a frozen LLM judge,                    “very common”, “formatting slip”, “very specific”).
Grok-4.1-Fast (see prompt in Appendix B). For
the score tokens, we reward as 1 − |ŝ − c|, where
ŝ is the model’s written score and c is the rubric                   detectors on 5000 samples not present in the train-
credibility; this teaches the model to calibrate its                  ing data (Section 2.1). For comprehensiveness, our
confidence to match the judge’s. We use these re-                     baselines include fine-tuned neural classifiers, ro-
wards on GRPO normalization with separate pools                       bust neural detectors, likelihood/log-rank methods,
for each token type, e.g., a rollout can receive a                    and curvature-based zero-shot methods (Li et al.,
strong positive signal on its type token and also                     2023; Hu et al., 2023; Su et al., 2023; Bao et al.,
receive a negative signal on its why tokens, so that                  2024; Thai et al., 2025; Emi and Spero, 2024; So-
the model can learn classification and explanation                    laiman et al., 2019; Liu et al., 2023; Guo et al.,
quality at the same time.                                             2023; Tulchinskii et al., 2023; Hans et al., 2024;
                                                                      Ippolito et al., 2020; Chen et al., 2023a; Tian et al.,
3       Results and discussion                                        2023). We exclude closed-source detectors due
                                                                      to their lack of transparency (no public code or
In this section, we present our experimental results
                                                                      models available) and reproducibility (results could
and provide deeper model analysis.
                                                                      change any time), as well as their cost and accessi-
                                                                      bility issues.
3.1      How accurate is TELL?
                                                                         Table 2 shows that which baseline performs best
While accuracy is not our primary design target,                      depends on the operating regime. We utilize boot-
since we argue it should only be seen as a pre-                       strap resampling (10000 resamples) to estimate the
requisite, for completeness, we provide a standard                    95% confidence intervals. TELL (AUROC 0.927)
comparison to other existing architectures in the                     slightly outperforms MAGE (0.913), but when an-
literature. We thus benchmark standard AI-text                        alyzing the true positive rate at 1% false positive
    1
    We also experimented with a small fixed advantage, but            rate, it recovers a significantly higher proportion of
found it to be of no benefit as we already apply format fixing.       AI documents (63.8 % instead of 4.2 %). Pangram-

                                                                  7
         I (91%)    think (92%)   this (99%)    is (81%)     AI (96%)             . (66%)      The (95%)    first (76%)   two (67%) sentences (99%)
        This (3%)    get (3%)      AI (1%)     sounds (7%)    the (1%)         because (24%)    It (4%)     text (10%) sentence (32%)    lines (1%)
        The (3%)    guess (2%)    the (0%)     looks (7%)    likely (1%)         -ish (5%)      I (1%)     opening (8%)   part (0%)      facts (0%)
         the (2%)    feel (1%)     I (0%)      reads (4%) machine (1%)              , (2%)     Most (0%)    main (3%)     line (0%)     clauses (0%)
        this (2%)    see (1%)      a (0%)       has (2%)     more (0%)         -looking (2%)     (0%)      passage (3%)   three (0%)     parts (0%)

                Figure 4: Decoding tree of the verdict’s why="..." on the NFS example from Figure 1.


EditLens and Fast-DetectGPT have lower AUROC                                    and reduce their dimensionality with PCA (we only
(0.911 and 0.861) but much better conservative re-                              show 5000 on the figure for clarity). We remove
call, with 58.3 % and 59.0 % of AI documents at                                 stopwords and annotate the 25 most frequent 2-
the same budget. Other detectors have significantly                             grams at the mean location of the spans containing
lower scores, which can be due to the difficulty of                             each. We show the results in Figure 3.
some of the documents in our test set2 . We also re-                               Additionally, we also explore the decoding pro-
port bootstrap ranking stability as a non-parametric                            cess to understand how TELL generates its anno-
argument for ranking robustness in Appendix E                                   tations. Figure 4 shows a greedy decoding process
alongside further details.                                                      in the verdict “why="..."” section, with the top-5
                                                                                most likely tokens shown at each step (probability
3.2    What’s the quality of the annotations?                                   mass renormalized), where we observe branching
In order to evaluate the quality of TELL’s anno-                                on certain key tokens where the model decides,
tations, we use the human expert comments from                                  for instance, whether to comment on the text in
Russell et al. (2025). We take the 200 documents                                general, the opening, the first sentences, or other
that we didn’t use for SFT, each being annotated by                             specific aspects.
five experts for a total of 1000 comments. We gen-
erate one annotation sampled from the TELL policy                               4      Conclusion
for each of those documents, and we compare it                                 In this work, we proposed a new approach to AI-
to the human comments in a blind ranked evalua-                                generated text detection that moves away from the
tion (in random order). To reduce bias, we use five                            traditional focus on accuracy and instead acknowl-
different LLM judges (Table 3).                                                edges that no detector can be perfect, and that it is
   TELL wins 72.3 % of the comparisons against                                 instead more important to empower users to make
the human comments. We observe that, in gen-                                   their own judgments. We do this by designing
eral, our annotations are competitive with human                               TELL, a novel architecture that produces human-
experts based on concreteness, falsifiability, co-                             auditable evidence on why it predicts that a text is
herence, plausibility and grounding; they tend to                              AI-generated or human-written. We train TELL on
be more detailed and provide more context than                                 a custom SFT dataset of domain-specific author-
human counterparts (mean 357.4 characters, SD                                  ship annotations, and refine it using GRPO with
204.3 for human; mean 443.8, SD 157.1 for TELL).                               curriculum learning to improve performance. We
We report additional details in Appendix F along                               evaluate TELL on a comprehensive test set span-
with an example that illustrates how TELL’s anno-                              ning multiple domains and original datasets, and
tations can be better than an average expert.                                  show that it outperforms existing detectors (AU-
                                                                               ROC 0.927), while also providing high-quality ex-
3.3    What types of annotations does
                                                                               planations (win-rate 72.3 % in average compared to
       TELL generate?
                                                                               human experts) — which no other detector can do
To better offer an intuition of the types of annota-                           — that can serve to build trust organically, identify
tions that TELL generates, we analyze all 16,651                               failed predictions, and train users to be better detec-
annotations generated on the test set to find which                            tors themselves. Overall, TELL sets the stage for a
are the learned patterns the model tends to produce.                           new line of work that is better aligned with human
We embed them with BAAI/bge-small-en-v1.5,                                     needs on AI-generated text detection, and we hope
   2
     While this is not a definitive statement about the difficulty             that our open code, data and model weights will
of the test set, we manually inspected a random subsample                      facilitate further research.
and found it subjectively challenging (at times, impossible) to
distinguish human from AI ourselves.


                                                                           8
Limitations                                                Ethical considerations
While we think that TELL is a step forward, it has         Any AI-generated text detector is subject to the risk
some limitations on which we hope future work              of false predictions, and this can have serious con-
can build. We want to be transparent about them:           sequences in the real world if trusted blindly. We
                                                           believe that our design is inherently better than ex-
Anchoring bias. While we’re confident that pro-            isting detectors in this regard, focusing on empow-
viding explanations is crucial for building trust in       ering users to make their own judgments, but there
detectors, this trust can be double-sided: research        is always a risk that certain users might overtrust
has shown that providing explanations can “anchor”         the model. We believe it’s essential to highlight
users to the model’s output, even when it’s wrong          this risk and strongly encourage users to critically
(Fok and Weld, 2023; Vasconcelos et al., 2023;             think about their own assessment of the evidence.
Nourani et al., 2021; Buçinca et al., 2021; Bansal
et al., 2020). To address this, we centered our ef-        Acknowledgements
forts on making explanations evidence-focused (in          Generative AI assistance. We used AI coding
SFT data generation and the judge rubric), so users        assistants to help write and debug the implementa-
can judge on their own. We also shaped our re-             tion, and produce data visualizations and figures.
wards to promote having a balance of human and             We also used them to refine the writing of this pa-
AI annotations in the same text.                           per and write the details in Appendices C, E, and F;
                                                           all ideas and claims are our own.
Multilingualism. We have designed TELL on
English text, and while informal testing suggests an
impressive ability to generalize to other languages,       References
this is testing we leave for future work.                  George Adam, Alexander Cui, Edwin Thomas, E. R.
                                                             Napier, Nazar Shmatko, Jacob Schnell, Jacob-Junqi
Unexplainable cases. We manually inspected                   Tian, Alekhya Dronavalli, Edward Tian, and Dong-
some failed examples, and in many cases, found it            won Lee. 2026. GPTZero: Robust Detection of LLM-
impossible to identify specific tells of AI/human            Generated Texts. ArXiv, abs/2602.13042.
generation. We believe that the task of identifying        Firoj Alam, Preslav Nakov, Nizar Habash, Iryna
AI-generated text can at times be “impossible”, at            Gurevych, Shammur Chowdhury, Artem Shelmanov,
least when it comes to completing it in a way that            Yuxia Wang, Ekaterina Artemova, Mucahid Kutlu,
                                                              and George Mikros, editors. 2025. Proceedings of the
humans can understand and verify. We believe that            1stWorkshop on GenAI Content Detection (GenAIDe-
future work might explore where the frontiers of              tect). International Conference on Computational
human capabilities lie, and how to design detectors           Linguistics, Abu Dhabi, UAE.
that align with them.
                                                           Shirin Anlen and Zuzanna Wojciak. 2025. TRIED:
                                                             Truly Innovative and Effective AI Detection
Mixed authorship. To be comparable to other                  Benchmark, developed by WITNESS.       ArXiv,
detectors, we have focused on the binary classifi-           abs/2504.21489.
cation of fully human vs fully AI-generated text.
                                                           C. G. Ardito. 2023. Contra generative AI detec-
However, we believe that a more realistic setting            tion in higher education assessments.  ArXiv,
could also include mixed-authorship documents,               abs/2312.05241.
and we hope future work can explore this more
                                                           Navid Ayoobi, Lily Knab, Wen Cheng, David Pantoja,
complex setting.                                             Hamidreza Alikhani, Sylvain Flamant, Jin Kim, and
                                                             Arjun Mukherjee. 2024. ESPERANTO: Evaluating
Human evaluation. Finally, our “quality of ex-               Synthesized Phrases to Enhance Robustness in AI De-
planations” evaluation (Section 3.2) is based on             tection for Text Origination. Proceedings of the 36th
LLMs. We used 5 different model families to max-             ACM Conference on Hypertext and Social Media.
imize the diversity of perspectives, but to further        Gagan Bansal, Tongshuang Sherry Wu, Joyce Zhou,
strengthen our claim that TELL produces convinc-             Raymond Fok, Besmira Nushi, Ece Kamar,
ing explanations, human evaluation would be ideal.           Marco Tulio Ribeiro, and Daniel S. Weld. 2020.
                                                             Does the Whole Exceed its Parts? The Effect of AI
However, we were unable to run it due to bud-                Explanations on Complementary Team Performance.
get constraints, and we hope future research can             Proceedings of the 2021 CHI Conference on Human
deepen experimental validation with human judges.            Factors in Computing Systems.


                                                       9
Guangsheng Bao, Yanbin Zhao, Zhiyang Teng, Linyi                 to accurately identify different forms of AI-generated
  Yang, and Yue Zhang. 2024. Fast-DetectGPT: Ef-                 written content. Advances in Simulation, 10(1):66.
  ficient Zero-Shot Detection of Machine-Generated
  Text via Conditional Probability Curvature.                  Di Cooke, Abigail Edwards, Sophia Barkoff, and
                                                                 Kathryn Kelly. 2025. As Good as a Coin Toss: Hu-
Yoshua Bengio, Jérôme Louradour, Ronan Collobert,                man Detection of AI-Generated Content. Communi-
  and Jason Weston. 2009. Curriculum learning. In                cations of the ACM, 68(10):100–109.
  Proceedings of the 26th Annual International Confer-
  ence on Machine Learning, pages 41–48, Montreal              Aldan Creo and Shushanta Pudasaini. 2024. SilverS-
  Quebec Canada. ACM.                                            peak: Evading AI-Generated Text Detectors using
                                                                 Homoglyphs. In COLING Workshops.
Yonatan Bitton, Hritik Bansal, Jack Hessel, Rulin
  Shao, Wanrong Zhu, Anas Awadalla, Josh Gardner,              Isaac David and Arthur Gervais. 2025. AuthorMist:
  Rohan Taori, and Ludwig Schmidt. 2023. VisIT-                   Evading AI Text Detectors with Reinforcement
  Bench: A Benchmark for Vision-Language Instruc-                 Learning. ArXiv, abs/2503.08716.
  tion Following Inspired by Real-World Use. Preprint,
  arXiv:2308.06595.                                            Liam Dugan, Alyssa Hwang, Filip Trhlik, Josh Mag-
                                                                 nus Ludan, Andrew Zhu, Hainiu Xu, Daphne
Oleksandr Marchenko Breneur, Adelaide Danilov,                   Ippolito, and Christopher Callison-Burch. 2024.
  Aria Nourbakhsh, and Salima Lamsiyah. 2026.                    RAID: A Shared Benchmark for Robust Evalua-
  NOTAI.AI: Explainable Detection of Machine-                    tion of Machine-Generated Text Detectors. ArXiv,
  Generated Text via Curvature and Feature Attribution.          abs/2405.07940.
  Preprint, arXiv:2603.05617.
                                                               Benj Edwards. 2023. Why AI writing detectors don’t
Zana Buçinca, Maja Barbara Malaya, and Krzysztof Z.              work. Ars Technica.
  Gajos. 2021. To Trust or to Think: Cognitive Forcing
  Functions Can Reduce Overreliance on AI in AI-               Bradley Emi and Max Spero. 2024. Technical Report
  assisted Decision-making. Proceedings of the ACM               on the Pangram AI-Generated Text Classifier.
  on Human-Computer Interaction, 5(CSCW1):1–21.
                                                               European Parliament. 2026. Parlemeter: EP Autumn
Christopher Burger, Karmece Talley, and C. Trotter.              2025 Survey. Eurobarometer Survey EB049EP, Eu-
  2025. Can AI Recognize Its Own Reflection? Self-               ropean Parliament, Directorate-General for Commu-
  Detection Performance of LLMs in Computing Edu-                nication.
  cation. ArXiv, abs/2512.23587.
                                                               Alexandra Fiedler and Jörg Döpke. 2025. Do humans
Te-Ping Chen. 2026. Writers Are Going to Extremes to
                                                                 identify AI-generated text better than machines? Evi-
  Prove They Didn’t Use AI. The Wall Street Journal.
                                                                 dence based on excerpts from German theses. Inter-
Yutian Chen, Hao Kang, Vivian Jiaying Zhai, Liangze              national Review of Economics Education, 49:100321.
  Li, Rita Singh, and Bhiksha Raj. 2023a. Token Pre-
  diction as Implicit Classification to Identify LLM-          Raymond Fok and Daniel S. Weld. 2023. In Search of
  Generated Text. In Conference on Empirical Meth-               Verifiability: Explanations Rarely Enable Comple-
  ods in Natural Language Processing.                            mentary Performance in AI-Advised Decision Mak-
                                                                 ing. AI Mag., 45:317–332.
Yutian Chen, Hao Kang, Yiyan Zhai, Liangze Li, Rita
  Singh, and Bhiksha Raj. 2023b. OpenLLMText                   Geoffrey A. Fowler. 2023. We tested a new ChatGPT-
  Dataset.                                                       detector for teachers. It flagged an innocent student.
                                                                 The Washington Post.
Zheng Chen, Yushi Feng, Jisheng Dang, Yue Deng,
  Changyang He, Hongxi Pu, Haoxuan Li, and Bo Li.              Joel Frank, Franziska Herbert, Jonas Ricker, Lea Schön-
  2025a. IPAD: Inverse Prompt for AI Detection - A                herr, Thorsten Eisenhofer, Asja Fischer, Markus Dür-
  Robust and Interpretable LLM-Generated Text De-                 muth, and Thorsten Holz. 2023. A Representative
  tector. In Unknown.                                             Study on Human Detection of Artificially Generated
                                                                  Media Across Countries.
Zhihui Chen, Kai He, Yucheng Huang, Yunxiao Zhu,
  and Mengling Feng. 2025b. DivScore: Zero-Shot                Jane Friedman. 2026. AI detection and authors’ fear of
  Detection of LLM-Generated Text in Specialized Do-             witch hunts. Jane Friedman.
  mains. In Proceedings of the 2025 Conference on
  Empirical Methods in Natural Language Processing,            Mingmeng Geng and T. Poibeau. 2025. On the De-
  pages 19242–19264, Suzhou, China. Association for              tectability of LLM-Generated Text: What Exactly Is
  Computational Linguistics.                                     LLM-Generated Text? ArXiv, abs/2510.20810.

Adam Cheng, Yiqun Lin, Gabriel Reedy, Christine                Biyang Guo, Xin Zhang, Ziyuan Wang, Minqi Jiang, Jin-
  Joseph, Samantha Wirkowski, Viviane Mallette,                  ran Nie, Yuxuan Ding, Jianwei Yue, and Yupeng Wu.
  Vikhashni Nagesh, David Krieser, and Aaron Cal-                2023. How Close is ChatGPT to Human Experts?
  houn. 2025. Ability of AI detection tools and humans           Comparison Corpus, Evaluation, and Detection.


                                                          10
Daya Guo, Dejian Yang, Haowei Zhang, Junxiao Song,             Ryuto Koike, Masahiro Kaneko, and Naoaki Okazaki.
  Peiyi Wang, Qihao Zhu, Runxin Xu, Ruoyu Zhang,                 2023. OUTFOX: LLM-generated Essay Detection
  Shirong Ma, Xiao Bi, Xiaokang Zhang, Xingkai                   through In-context Learning with Adversarially Gen-
  Yu, Yu Wu, Z. F. Wu, Zhibin Gou, Zhihong Shao,                 erated Examples. In AAAI Conference on Artificial
  Zhuoshu Li, Ziyi Gao, Aixin Liu, and 175 oth-                  Intelligence.
  ers. 2025. DeepSeek-R1 incentivizes reasoning
  in LLMs through reinforcement learning. Nature,              Ryan Koo, Minhwa Lee, Vipul Raheja, Jong Inn Park,
  645(8081):633–638.                                             Zae Myung Kim, and Dongyeop Kang. 2024. Bench-
                                                                 marking Cognitive Biases in Large Language Models
Abhimanyu Hans, Avi Schwarzschild, Valeriia                      as Evaluators. Preprint, arXiv:2309.17012.
  Cherepanova, Hamid Kazemi, Aniruddha Saha,
  Micah Goldblum, Jonas Geiping, and Tom Goldstein.            Walter Laurito, Benjamin Davis, Peli Grietzer, Tomáš
  2024. Spotting LLMs With Binoculars: Zero-                    Gavenčiak, Ada Böhm, and Jan Kulveit. 2025.
  Shot Detection of Machine-Generated Text. In                  AI–AI bias: Large language models favor com-
  International Conference on Machine Learning.                 munications generated by large language models.
                                                                Proceedings of the National Academy of Sciences,
A. Hou, Jingyu (Jack) Zhang, Tianxing He, Yichen                122(31):e2415697122.
  Wang, Yung-Sung Chuang, Hongwei Wang,
  Lingfeng Shen, Benjamin Van Durme, Daniel                    Yafu Li, Qintong Li, Leyang Cui, Wei Bi, Zhilin Wang,
  Khashabi, and Yulia Tsvetkov. 2023. SemStamp: A                Longyue Wang, Linyi Yang, Shuming Shi, and Yue
  Semantic Watermark with Paraphrastic Robustness                Zhang. 2023. MAGE: Machine-generated Text De-
  for Text Generation. ArXiv, abs/2310.03991.                    tection in the Wild. In Annual Meeting of the Associ-
                                                                 ation for Computational Linguistics.
Xiaomeng Hu, Pin-Yu Chen, and Tsung-Yi Ho. 2023.
  RADAR: Robust AI-Text Detection via Adversarial              Yikang Liu, Ziyin Zhang, Wanyang Zhang, Shisen Yue,
  Learning. In Advances in Neural Information Pro-               Xiaojing Zhao, Xinyuan Cheng, Yiwen Zhang, and
  cessing Systems, volume 36, pages 15077–15095.                 Hai Hu. 2023. ArguGPT: Evaluating, understanding
  Curran Associates, Inc.                                        and identifying argumentative essays generated by
                                                                 GPT models. arXiv preprint.
Guanhua Huang, Yuchen Zhang, Zhe Li, Yongjian You,
  Mingze Wang, and Zhouwang Yang. 2024. Are AI-                Yiqi Liu, Nafise Sadat Moosavi, and Chenghua
  Generated Text Detectors Robust to Adversarial Per-            Lin. 2024.    LLMs as Narcissistic Evaluators:
  turbations? ArXiv, abs/2406.01179.                             When Ego Inflates Evaluation Scores. Preprint,
                                                                 arXiv:2311.09766.
John P. A. Ioannidis. 2005. Why Most Published
  Research Findings Are False. PLoS Medicine,                  Tara García Mathewson. 2025. In California, Colleges
  2(8):e124.                                                     Pay a Steep Price for Faulty AI Detectors.

Daphne Ippolito, Daniel Duckworth, Chris Callison-             Jiří Milička, Anna Marklová, Ondřej Drobil, and Eva
  Burch, and Douglas Eck. 2020. Automatic Detec-                   Pospíšilová. 2025. Humans can learn to detect AI-
  tion of Generated Text is Easiest when Humans are                generated texts, or at least learn when they can’t.
  Fooled. In Proceedings of the 58th Annual Meet-                  PLOS One, 20(10):e0333007.
  ing of the Association for Computational Linguistics,
  pages 1808–1822, Online. Association for Computa-            David Mingay. 2026. After being falsely branded an AI
  tional Linguistics.                                            plagiarist, how can I accuse students? Times Higher
                                                                 Education.
Jiazhou Ji, Ruizhe Li, Shujun Li, Jie Guo, Weidong Qiu,
   Zheng Huang, Chiyu Chen, Xiaoyu Jiang, and Xinru            E. Mitchell, Yoonho Lee, Alexander Khazatsky, Christo-
   Lu. 2024. Detecting Machine-Generated Texts: Not               pher D. Manning, and Chelsea Finn. 2023. Detect-
   Just "AI vs Humans" and Explainability is Compli-              GPT: Zero-Shot Machine-Generated Text Detection
   cated. ArXiv, abs/2406.18259.                                  using Probability Curvature. In International Confer-
                                                                  ence on Machine Learning.
Georgia Jiang. 2023. Is AI-generated content actually
  detectable? TechXplore.                                      Ayat Najjar, Huthaifa I. Ashqar, O. A. Darwish, and
                                                                 Eman M. Hammad. 2025. Leveraging Explainable
Brian Kennedy, Eileen Yam, Emma Kikuchi, Isabelle                AI for LLM Text Attribution: Differentiating Human-
  Pula, and Javier Fuentes. 2025. How Americans                  Written and Multiple LLMs-Generated Text. ArXiv,
  View AI and Its Impact on People and Society. Tech-            abs/2501.03212.
  nical report, Pew Research Center.
                                                               Ernestas Naprys. 2024. Your essay was AI-generated,
Tyler Kingkade. 2026. College students are turning to            so was the Bible, Harry Potter, and Bohemian Rhap-
  AI to avoid cheating accusations and "humanizers"              sody. Cybernews.
  to evade detection. NBC News.
                                                               Mahsan Nourani, Chiradeep Roy, Jeremy E Block, Don-
Darek Kłeczek. 2023. DAIGT V2 Train Dataset.                     ald R Honeycutt, Tahrima Rahman, Eric Ragan, and


                                                          11
  Vibhav Gogate. 2021. Anchoring Bias Affects Men-              Zhihong Shao, Peiyi Wang, Qihao Zhu, Runxin Xu,
  tal Model Formation and User Reliance in Explain-               Junxiao Song, Xiao Bi, Haowei Zhang, Mingchuan
  able AI Systems. In 26th International Conference               Zhang, Y. K. Li, Y. Wu, and Daya Guo. 2024.
  on Intelligent User Interfaces, pages 340–350, Col-             DeepSeekMath: Pushing the Limits of Mathemat-
  lege Station TX USA. ACM.                                       ical Reasoning in Open Language Models. Preprint,
                                                                  arXiv:2402.03300.
NPR. 2025. Teachers Are Using Software to See if
  Students Used AI. What Happens When It’s Wrong?               Ashish Raj Shekhar, Shiven Agarwal, Priyanuj Bor-
                                                                  doloi, Y. Shah, Tejas Anvekar, and Vivek Gupta. 2026.
OpenAI. 2025. Gpt-oss-120b & gpt-oss-20b Model                    DoPE: Decoy Oriented Perturbation Encapsulation
  Card.                                                           Human-Readable, AI-Hostile Documents for Aca-
                                                                  demic Integrity. ArXiv, abs/2601.12505.
OpenAI, Aaron Jaech, Adam Kalai, Adam Lerer, Adam
  Richardson, Ahmed El-Kishky, Aiden Low, Alec                  Carlton Shepherd. 2025. Generative AI Misuse Poten-
  Helyar, Aleksander Madry, Alex Beutel, Alex Car-                tial in Cyber Security Education: A Case Study of a
  ney, Alex Iftimie, Alex Karpenko, Alex Tachard Pas-             UK Degree Program. ArXiv, abs/2501.12883.
  sos, Alexander Neitz, Alexander Prokofiev, Alexan-
                                                                Tvesha Sippy, Florence Enock, Jonathan Bright, and
  der Wei, Allison Tam, Ally Bennett, and 245 oth-
                                                                  Helen Z. Margetts. 2024. Behind the Deepfake: 8%
  ers. 2026. OpenAI o1 System Card. Preprint,
                                                                  Create; 90% Concerned. Surveying public exposure
  arXiv:2412.16720.
                                                                  to and perceptions of deepfakes in the UK.
Shushanta Pudasaini, Luis Miralles-Pechu’an, David              Irene Solaiman, Miles Brundage, Jack Clark, Amanda
  Lillis, and Marisa Llorens Salvador. 2026. Why AI-               Askell, Ariel Herbert-Voss, Jeff Wu, Alec Radford,
  Generated Text Detection Fails: Evidence from Ex-                Gretchen Krueger, Jong Wook Kim, Sarah Kreps,
  plainable AI Beyond Benchmark Accuracy.                          Miles McCain, Alex Newhouse, Jason Blazakis, Kris
                                                                   McGuffie, and Jasmine Wang. 2019. Release Strate-
Suraj Ranganath and Atharv Ramesh. 2026. StealthRL:                gies and the Social Impacts of Language Models.
  Reinforcement Learning Paraphrase Attacks for
  Multi-Detector Evasion of AI-Text Detectors. arXiv            Jinyan Su, Terry Zhuo, Di Wang, and Preslav Nakov.
  preprint.                                                        2023. DetectLLM: Leveraging Log Rank Informa-
                                                                   tion for Zero-Shot Detection of Machine-Generated
Jasper Roe, Mike Perkins, Daniel Ruelle James                      Text. In Findings of the Association for Compu-
   Cook University Singapore, British University Viet-             tational Linguistics: EMNLP 2023, pages 12395–
   nam, and VinUniversity. 2024. Understanding Stu-                12412, Singapore. Association for Computational
   dent and Academic Staff Perceptions of AI Use in                Linguistics.
   Assessment and Feedback. ArXiv, abs/2406.15808.
                                                                Katherine Thai, Bradley Emi, Elyas Masrour, and Mohit
Jenna Russell, Marzena Karpinska, and Mohit Iyyer.                Iyyer. 2025. EditLens: Quantifying the Extent of AI
  2025. People who frequently use ChatGPT for writ-               Editing in Text. ArXiv, abs/2510.03154.
  ing tasks are accurate and robust detectors of AI-
  generated text. ArXiv, abs/2501.15654.                        Panagiotis C. Theocharopoulos, S. Georgakopou-
                                                                  los, Sotiris Tasoulis, and V. Plagianakos. 2024.
Vinu Sankar Sadasivan, Aounon Kumar, S. Balasubra-                Who Writes the Review, Human or AI? ArXiv,
  manian, and S. Feizi. 2023. Can AI-Generated Text               abs/2405.20285.
  be Reliably Detected? ArXiv, abs/2303.11156.
                                                                T. J. Thomson, Aaron J. Snoswell, and James Meese.
Shoumik Saha and S. Feizi. 2025. Almost AI, Almost                 2025. How Do AI Detection Tools Actually Work?
  Human: The Challenge of Detecting AI-Polished                    And Are They Effective?
  Writing. ArXiv, abs/2502.15666.                               Yuchuan Tian, Hanting Chen, Xutao Wang, Zheyuan
                                                                  Bai, Qinghua Zhang, Ruifeng Li, Chaoxi Xu,
Areg Mikael Sarvazyan, José Ángel González, Marc                  and Yunhe Wang. 2023.       Multiscale Positive-
  Franco-Salvador, Francisco Rangel, Berta Chulvi,                Unlabeled Detection of AI-Generated Texts. ArXiv,
  and Paolo Rosso. 2023. Overview of AuTexTifi-                   abs/2305.18149.
  cation at IberLEF 2023: Detection and Attribution
  of Machine-Generated Text in Multiple Domains.                Brian Tufts, Xuandong Zhao, and Lei Li. 2024. A Prac-
  Procesamiento del Lenguaje Natural, pages 275–288.              tical Examination of AI-Generated Text Detectors for
                                                                  Large Language Models. In North American Chapter
Peter Scarfe, Kelly Watcham, Alasdair Clarke, and Eti-            of the Association for Computational Linguistics.
  enne Roesch. 2024. A real-world test of artificial
  intelligence infiltration of a university examinations        Eduard Tulchinskii, Kristian Kuznetsov, Laida
  system: A “Turing Test” case study. PLOS ONE,                   Kushnareva, D. Cherniavskii, S. Barannikov,
  19(6):e0305354.                                                 Irina Piontkovskaya, S. Nikolenko, and Evgeny
                                                                  Burnaev. 2023. Intrinsic Dimension Estimation for
Lexie Scibilia. 2025. Guilty Until Proven Human. The              Robust Detection of AI-Generated Texts. ArXiv,
  Villanovan.                                                     abs/2306.04723.


                                                           12
University of San Diego Legal Research Center. 2025.
  Generative AI Detection Tools.
Helena Vasconcelos, Matthew Jörke, Madeleine Grunde-
  McLaughlin, Tobias Gerstenberg, Michael Bernstein,
  and Ranjay Krishna. 2023. Explanations Can Re-
  duce Overreliance on AI Systems During Decision-
  Making. Preprint, arXiv:2212.06823.
V. Verma, Eve Fleisig, Nicholas Tomlin, and D. Klein.
   2023. Ghostbuster: Detecting Text Ghostwritten by
   Large Language Models. In North American Chapter
   of the Association for Computational Linguistics.
Yuxia Wang, Jonibek Mansurov, Petar Ivanov, Jinyan
  Su, Artem Shelmanov, Akim Tsvigun, Osama Mo-
  hanned Afzal, Tarek Mahmoud, Giovanni Puccetti,
  Thomas Arnold, and 1 others. 2024. M4GT-Bench:
  Evaluation Benchmark for Black-Box Machine-
  Generated Text Detection. to appear in ACL 2024.
Michael Waters. 2026. The Typo Vibe Shift. The At-
  lantic.
Debora Weber-Wulff, Alla Anohina-Naumeca, Sonja
  Bjelobaba, T. Foltýnek, J. Guerrero-Dib, Olumide
  Popoola, Petr Sigut, and Lorna Waddington. 2023.
  Testing of detection tools for AI-generated text. Inter-
  national Journal for Educational Integrity, 19:1–39.
Jason Wei, Xuezhi Wang, Dale Schuurmans, Maarten
   Bosma, Brian Ichter, Fei Xia, Ed Chi, Quoc Le,
   and Denny Zhou. 2023. Chain-of-Thought Prompt-
   ing Elicits Reasoning in Large Language Models.
   Preprint, arXiv:2201.11903.
Tessa Weinberg. 2025. A.I., ChatGPT and Turnitin:
  Students and the New Cheating Era. The New York
  Times.
Colin Wood. 2024. AI detectors are easily fooled, re-
  searchers find. Edscoop.
Junchao Wu, Runzhe Zhan, Derek F. Wong, Shu
  Yang, Xinyi Yang, Yulin Yuan, and Lidia S. Chao.
  2024. DetectRL: Benchmarking LLM-Generated
  Text Detection in Real-World Scenarios. ArXiv,
  abs/2410.23746.
Sen Yan, Zhiyi Wang, and David Dobolyi. 2025. An
  explainable framework for assisting the detection
  of AI-generated textual content. Decision Support
  Systems, 196:114498.
Angela Yifei Yuan, Haoyi Li, Soyeon Caren Han, and
  Christopher Leckie. 2025. EMMM, Explain Me My
  Model! Explainable Machine Generated Text Detec-
  tion in Dialogues. Preprint, arXiv:2508.18715.
ZeroGPT. 2026. ZeroGPT: AI Content Detector.

Haolan Zhan, Xuanli He, Qiongkai Xu, and Pon-
  tus Stenetorp. 2023. G3Detector: General GPT-
  Generated Text Detector. ArXiv, abs/2305.12680.




                                                             13
A        Qualitative examples: why                                            • intelligence (74 %): “the same mixed-script pat-
         explanations matter                                                    tern appears inside a common word; that kind of
                                                                                systematic Unicode substitution is a classic AI or
In this section, we aim to present a set of exam-                               encoding artifact”
ples where we should how TELL’s explanations                                  • AI (74 %): “the acronym is written with Greek
can outperform score-only detectors — not neces-                                letters instead of normal Latin letters; this is a very
sarily in accuracy (many detectors output the same                              strong sign of a model or pipeline that changed the
                                                                                script”
labels as TELL), but in the quality of the informa-
tion provided to users. We compare our outputs                                • . . . (the next spans are annotated similarly, we skip
to Pangram (closed-source online version3 ) as a                                them for brevity)
highly-accurate, state-of-the-art model.                                  Our comment. It’s somewhat irrelevant to try to ascer-
   We show AI-leaning spans in red and Human-                             tain the exact origin of the text, since a homoglyph attack
leaning spans in green.                                                   like this indicates intent — and a binary label can’t reflect
                                                                          it. TELL instead highlights to the user how the text is
                                                                          suspicious, so they can make an informed decision about
    1. Homoglyph attack                                                   whether to trust it. Pangram gets the label completely
                                                                          wrong, and even if it got the label right, it would not
    Reference label. AI                                                   show any of the evidence that the text is suspicious.
    Input. The recent advancements in artificial intelli-
    gence (AI) combined with the extensive amount of data
    generated by today’s clinical systems, has led to the devel-          2. Harry Potter
    opment of imaging AI solutions across the whole value
    chain of medical imaging, including image reconstruc-                 Reference label. Human
    tion, medical image segmentation, image-based diagno-                 Input. Mr and Mrs Dursley, of number four, Privet
    sis and treatment planning. Notwithstanding the suc-                  Drive, were proud to say that they were perfectly nor-
    cesses and future potential of AI in medical imaging,                 mal, thank you very much. They were the last people
    many stakeholders are concerned of the potential risks                you’d expect to be involved in anything strange or myste-
    and ethical implications of imaging AI solutions, which               rious, because they just didn’t hold with such nonsense.
    are perceived as complex, opaque, and difficult to com-               Mr Dursley was the director of a firm called Grunnings,
    prehend, utilise, and trust in critical clinical applications.        which made drills. He was a big, beefy man with hardly
                                                                          any neck, although he did have a very large mustache.
         Model outputs.                                                   Mrs Dursley was thin and blonde and had nearly twice
         TELL. 86 % AI.                                                   the usual amount of neck, which came in very useful as
         Pangram. 100 % human.                                            she spent so much of her time craning over garden fences,
                                                                          spying on the neighbors. The Dursleys had a small son
                                                                          called Dudley and in their opinion there was no finer boy
    Verdict. I think this is AI. The main tell is the many
                                                                          anywhere.
    small letter swaps: I see Latin A, I, P, R, and 0 used to
    look like Cyrillic or normal letters. That is a strong sign
    of a model trying to hide or bypass detection by making                 Model outputs.
    the text look human or unusual. The wording is also very                TELL. 91.84 % Human.
    smooth and generic, with a clean news-summary feel,                     Pangram. 100 % human.
    but the hidden character tricks make it look more like a
    generated or transformed passage than a normal human                  Verdict. I think this is human, and I would even guess it
    sentence.                                                             is the original published text. The line has a very specific
    TELL span-level output.                                               comic rhythm: the dry narrator gives the Dursleys a
          • T (78 %): “the first letter looks like a Cyrillic T           normal front, then undercuts it with a small absurd detail.
            mixed into an English sentence; I think this is a             The phrase thank you very much is a little old-fashioned
            strong sign of a character encoding or translitera-           and a little rude, which feels like a human author playing
            tion artifact, and AI output can create this when it          with the reader. The word hold with is a strange British
            copies or normalizes text”                                    idiom, and the sentence has a real ear for class and habit.
                                                                          The last sentence is also a bit awkward, with no full stop
          • advancements (72 %): “the word has many Latin-                after Dudley, which makes it feel like a printed passage
            looking letters with diacritics, which makes it look          rather than a model trying to make a clean ending.
            like a transformed version of normal English; AI              TELL span-level output.
            can produce this when it tries to preserve text while
            changing the script”                                              • proud to say (−0.42): “a very British, slightly
                                                                                cheeky phrase with social nuance, not just a plain
          • artificial (86 %): “the word is clearly a fake-                     summary.”
            looking mix of Cyrillic and Latin letters; this is
            not normal human typing and strongly points to an                 • you’d expect (−0.34): “the contraction and direct
            automated transliteration”                                          reader address make the narration sound spoken.”

                                                                              • Grunnings (−0.58): “a made-up brand name with
     3
     In our experiments, we used Pangram’s online version                       the specific comic texture of Rowling’s world.”
that’s available at https://www.pangram.com/ as of 26th May
2026


                                                                     14
    • big, beefy (−0.44): “an old-fashioned, blunt physi-               • gave the world (+0.46): “this sounds like a grand
      cal phrase that sounds like a human narrator trying                 claim, not a careful factual claim; AI often up-
      to be funny.”                                                       grades a simple fact into a broad statement to make
                                                                          it sound important.”
    • very useful (−0.46): “a dry practical aside whose
      humor comes from the plain way the absurd image                   • most French supermarket (−0.48): “the joke is
      is stated.”                                                         oddly specific and a bit absurd; a human might
                                                                          invent this kind of playful contrast from personal
Our comment. Harry Potter is sometimes misclassified                      humor, not from a standard guide.”
as AI-generated because it is frequently represented in
training corpora. Both Pangram and TELL identify it as                  • Aldi (+0.88): “this is a real German supermarket,
human, but TELL can identify it as being based on the                     not French, so the fact is badly wrong; that is a
original book.                                                            strong AI tell because it is a common knowledge
                                                                          error in a very specific way.”

                                                                        • founded in Lyon (+0.57): “the model is trying to
3. Hallucination                                                          make the wrong fact look sourced and concrete,
Reference label. AI                                                       so it adds a plausible founding detail instead of
                                                                          leaving it vague.”
Input. When I think of France, I can’t help but picture
lazy afternoons sipping espresso at a sidewalk café in                  • Hungary (+0.86): “this geography is wrong;
its vibrant capital, Berlin, where the Eiffel Tower casts                 France does not border Hungary, so this looks like
a long shadow over the Seine. It’s a country that gave                    AI hallucinating a map while trying to make a con-
the world the most French supermarket, Aldi—founded                       trast.”
in Lyon in the 1940s, which explains why even the most
rustic boulangerie feels a bit like a discount aisle. And               • where (+0.31): “repeated connector; the same
if you drive west from Lyon, you’ll cross the border into                 word appears again soon after, which can happen
Hungary, where the language suddenly shifts and the                       when AI keeps chaining clauses with safe transi-
paprika replaces the butter. France really is a patchwork                 tions.”
of surprises, isn’t it?
                                                                        • the paprika replaces the butter (+0.86): “forced
  Model outputs.                                                          metaphor; this is a strange but neat image, and AI
  TELL. 89 % AI.                                                          often makes these odd paired contrasts to sound
  Pangram. 100 % AI.                                                      witty, even when they do not make much sense.”

                                                                        • really is (+0.33): “the sentence ends with a tag
Verdict. I think this is AI because the text is smooth,                   that sounds like a canned rhetorical closer; AI often
cliché, and full of wrong facts. The writer keeps adding                  adds this kind of friendly confirmation to wrap up
polished travel images, but places and details do not fit,                an essay.”
which makes it look like a generated paragraph trying to
sound human.                                                            • isn’t it? (−0.24): “the question tag gives the line a
TELL span-level output.                                                   conversational turn; this could be human because
                                                                          it feels like the writer is trying to engage the reader
    • When I think of France (−0.42): “personal open-                     directly.”
      ing; I think a real writer often starts with a feel-
      ing or memory before giving facts, while AI often             Our comment. In this case, the Berlin hallucination
      jumps straight to a polished travel sentence.”                might be easy to catch. We’re more impressed by how
                                                                    TELL was able to identify the fact that we, humans,
    • can’t help but picture (+0.55): “this is a common
                                                                    “came up with” the idea of inserting a joke about Aldi
      AI transition. It sounds like a person imagining
                                                                    being a French supermarket — even if it’s inserted in the
      something, but it is also a safe way to move from
                                                                    middle of an otherwise AI-sounding text.
      a feeling to a scene without adding much real tex-
      ture.”

    • sipping espresso (+0.55): “this is a common ro-               4. Fabricated statute and section
      mantic travel cliché; AI likes these polished sen-            Reference label. AI
      sory phrases because they are safe and familiar.”             Input Text. Under the Federal Student Homework Eq-
                                                                    uity Act of 2018, section 47(b)(12), teachers must pro-
    • its vibrant capital (+0.48): “this is a neat adjective
                                                                    vide exactly 36 hours of rest after any essay longer than
      phrase that sounds like travel brochure copy; AI
                                                                    500 words. This rule was reaffirmed by the Ninth Circuit
      often adds this kind of polished praise to make the
                                                                    in Homework Alliance v. State Board, 2021, making the
      sentence feel complete.”
                                                                    policy mandatory nationwide. No exceptions apply. The
    • Berlin, where the Eiffel Tower casts a long shadow            rule applies immediately everywhere.
      over the Seine (+0.82): “this is a very pretty in-
      vented image, but it does not fit the geography; I              Model outputs.
      think the model is mixing famous French symbols                 TELL. 91.84 % AI.
      and making a smooth scenic phrase.”                             Pangram. 100 % AI.




                                                               15
Verdict. The text is polished and legalistic, but the details        6. Rubric claim without evidence
feel fabricated and the citation style is inconsistent.              Reference label. AI
TELL span-level output.                                              Input Text. This paragraph includes three direct quota-
                                                                     tions, a counterargument, and a works cited entry. School
    • Federal Student Homework Equity Act of 2018,
                                                                     gardens help students learn responsibility and teamwork.
      section 47(b)(12) (+0.90): “a very specific legal-             They also make the campus look nicer. For these reasons,
      sounding citation that reads as invented authority.”           my evidence fully meets every part of the rubric. The
                                                                     teacher can check my packet and see all requirements
    • exactly 36 hours (+0.95): “false precision makes               listed. This is clear and complete.
      the policy sound factual without support.”

    • Homework Alliance v. State Board, 2021 (+0.90):                  Model outputs.
      “plausible court language with malformed citation                TELL. 86.85 % AI.
      style.”                                                          Pangram. 100 % AI.

Our comment. Pangram gets the label right, but the use-              Verdict. The text is tidy, generic, and rubric-like, with
ful part is knowing where the legal language goes wrong.             no personal voice or concrete evidence.
TELL points to the fake statute, the false precision, and            TELL span-level output.
the malformed case citation, which are the claims that a
real human reader would actually need to check.                          • three direct quotations, a counterargument, and a
                                                                           works cited entry (+0.90): “the paragraph summa-
                                                                           rizes a checklist rather than providing the required
5. Unsupported report claim                                                evidence.”
Reference label. AI                                                      • School gardens help students learn responsibility
Input Text. According to the 2022 Global Classroom                         and teamwork (+0.75): “generic thesis-like con-
Motivation Report by the International Institute for Stu-                  tent without support.”
dent Growth, 88.4 percent of learners become more cre-
ative after teachers use inspirational wall posters. This                • my evidence fully meets every part of the rubric
finding proves that classroom decoration is one of the                     (+0.95): “oddly self-aware rubric language unsup-
strongest predictors of academic achievement. The re-                      ported by the text.”
port offers no conflicting classroom evidence. All schools
should follow it.                                                    Our comment. TELL shows the reader that the answer
                                                                     claims evidence that simply isn’t there, which is just the
  Model outputs.                                                     kind of detail that a real human can easily try to verify.
  TELL. 90.50 % AI.
  Pangram. 100 % human.
                                                                     7. Claim contradicts quote
Verdict. I think this is AI because the paragraph tries
                                                                     Reference label. AI
to sound researched, but the evidence is not actually
                                                                     Input Text. The line “I locked the door so no one would
grounded. It gives a polished report name and an ex-
                                                                     follow me” proves that the speaker wants to reconnect
act statistic, then jumps from classroom posters to aca-
                                                                     with the community. The image of locking the door
demic achievement with no citation, method, or caveat.
                                                                     shows openness and trust, which is why the poem is
That combination of confident authority and unsupported
                                                                     ultimately about welcoming other people back into your
causality makes it read like generated prose rather than a
                                                                     life. The message feels hopeful. Everyone learns from
real sourced claim.
                                                                     this ending.
TELL span-level output.

    • Global Classroom Motivation Report (+0.90): “a                   Model outputs.
      plausible institutional source name without verifi-              TELL. 86.49 % AI.
      able citation structure.”                                        Pangram. 100 % human.

    • 88.4 percent (+0.95): “exact decimal precision
                                                                     Verdict. The passage is fluent and complete, but the
      makes the unsupported statistic feel researched.”
                                                                     interpretation is generic and does not fit the quoted line.
    • This finding proves (+0.85): “overstates causality             TELL span-level output.
      where a careful writer would hedge.”
                                                                         • proves (+0.75): “overstates what a poetic line can
                                                                           establish.”
Our comment. This one looks academic because it has
a report name and an exact number. Pangram treats it                     • reconnect with the community (+0.85): “broad
as human, but TELL actually highlights the unsupported                     abstract theme detached from the quoted image.”
source, the suspicious decimal, and the conclusion that
is a bit overconfident.                                                  • shows openness and trust (+0.95): “the claim is
                                                                           mechanically opposite to the evidence.”

                                                                     Our comment. Pangram completely misses the issue
                                                                     here. The text may seem human, but a score alone cannot
                                                                     tell e.g. a professor whether the model even noticed the



                                                                16
literary mistake. TELL shows the exact error, so the hu-              • 118 not 108 (−0.90): “page-number uncertainty
man can decide whether if it matters for the assignment.                with rough punctuation.”

                                                                      • I am not sure yet (−0.82): “explicit uncertainty
8. Arithmetic contradiction                                             instead of confident closure.”
Reference label. AI                                               Our comment. This is “rough” in a way that feels
Input Text. The after-school program enrolled 24 stu-             situated rather than machine-like. Both Pangram and
dents. Fifteen students chose robotics, twelve chose              TELL can recognize it as human, but only our model
debate, and nine chose art, with no student joining more          can explain that it is classified as human due to the small
than one club. Therefore, every student was successfully          evidence scattered around the text.
placed into exactly one activity and the program had no
scheduling conflicts. The summary proves every family
received a schedule. The numbers confirm that outcome.
                                                                  10. Code explanation contradiction
  Model outputs.                                                  Reference label. AI
  TELL. 85.74 % AI.                                               Input Text. The loop below prints only even numbers
  Pangram. 100 % human.                                           because it skips every odd value: for (let i = 1; i
                                                                  <= 5; i += 2) console.log(i). Since the counter
                                                                  increases by two, the output will be 2 and 4, which proves
Verdict. The passage is fluent, but TELL flags the arith-         the algorithm filters parity correctly. This shows the code
metic contradiction: 15 + 12 + 9 exceeds 24 under the             is correctly explained. The example is very simple.
no-overlap constraint.
TELL span-level output.                                             Model outputs.
   • Fifteen, twelve, and nine (+0.80): “the data are               TELL. 92.69 % AI.
     arranged in a neat pattern.”                                   Pangram. 100 % AI.

   • no student joining more than one club (+0.90):               Verdict. The answer is polished, fluent, and concise,
     “the added constraint makes the arithmetic contra-           but the logic is off. The model likely inferred a generic
     diction explicit.”                                           explanation for a loop and filled in a plausible output
                                                                  without actually tracing the code.
   • every student was successfully placed (+0.95):
                                                                  TELL span-level output.
     “confident conclusion unsupported by the num-
     bers.”                                                           • prints only even numbers because it skips every
                                                                        odd value (+0.90): “the loop actually prints odd
Our comment. This is a small arithmetic mistake, but it                 numbers, so the surface explanation loses the exact
is exactly the kind of mistake that generated text might                logic.”
hide. Pangram calls it human; instead, TELL shows the
contradiction in the numbers and the overconfident (but               • the output will be 2 and 4 (+0.95): “the technical
wrong) conclusion.                                                      claim is wrong; the loop starts at 1 and increments
                                                                        by 2.”

9. Uncertain scratch note                                         Our comment. Both Pangram and TELL get this right,
Reference label. Human                                            but TELL makes the reason much clearer. The explana-
Input Text. I need to rewrite this later because the first        tion says the loop prints even numbers, while the code
part sounds weird. The bus was late, my pencil broke,             starts at 1, so the bug is in the reasoning.
and I copied the wrong page number from Ana’s book,
so the quote might be on 118 not 108. The main idea is
probably that the brother is embarrassed, but I am not            11. Fabricated API documentation
sure yet. For now.                                                Reference label. AI
                                                                  Input Text. The React useUniversalCache hook, intro-
  Model outputs.                                                  duced in React 19.4, automatically stores component
  TELL. 82.03 % human.                                            state across browsers and devices without a server. To
  Pangram. 100 % human.                                           enable it, developers call useUniversalCache(’global’) in-
                                                                  side any component, and React guarantees encrypted syn-
Verdict. The note is practical, local, and unfinished:            chronization for all users by default. No extra provider
it contains self-reminders, casual language, and small            or storage configuration is required for production apps.
punctuation roughness that AI would usually smooth                Teams can adopt it today.
away.
TELL span-level output.                                             Model outputs.
   • I need to rewrite this later (−0.86): “a practical             TELL. 90.41 % AI.
     note to self rather than a polished opening.”                  Pangram. 100 % AI.

   • weird (−0.78): “casual word choice.”                         Verdict. The passage reads like a confident technical
   • Ana’s book (−0.62): “a small concrete detail tied            summary, but the feature, version, API, and guarantees
     to a real task.”                                             all feel invented.



                                                             17
TELL span-level output.

    • useUniversalCache hook (+0.90): “a plausible
      API name that appears invented from real library
      naming patterns.”

    • React 19.4 (+0.95): “a very specific version num-
      ber used to create factual authority.”

    • useUniversalCache(’global’) (+0.90):           “a
      plausible-looking but unsupported call signature.”

    • React guarantees encrypted synchronization for all
      users by default (+0.95): “an overstrong guarantee
      that a hook could not provide by itself.”

Our comment. The text sounds like documentation,
which is what makes it “risky”. Both detectors flag it, but
TELL names the invented hook, version, call signature,
and guarantee so a developer knows what to verify.


12. Multilingual student text
Reference label. Human
Input Text. I wrote this after dinner because my abuela
kept asking if I finished la tarea. The sentence maybe is
not perfect, but I think the character feels lonely when
nobody saves a seat for him. In my house we say that
kind of quiet is louder than yelling. I remember that.
That part stayed with me.

  Model outputs.
  TELL. 84.60 % human.
  Pangram. 100 % AI.

Verdict. The passage reads as human because it has
a real personal setting, casual bilingual phrasing, and
a small awkward grammar choice that AI would likely
polish away.
TELL span-level output.

    • I wrote this after dinner (−0.82): “specific per-
      sonal context rather than a generic setup.”

    • abuela (−0.78): “the Spanish word is left naturally
      in family context.”

    • la tarea (−0.86): “casual code-switching that AI
      often smooths into one language.”

    • maybe is not perfect (−0.90): “non-standard word
      order that reads like a genuine writer’s voice.”

Our comment. This is a case about fairness, where
the explanation matters the most. Pangram marks the
multilingual student voice as AI, while TELL treats the
family context, code-switching, and imperfect grammar
as signs of a real writer.




                                                              18
B   Prompts used                                                    8. Think like a detective: consider the ’writers intention
                                                                           and context, look for subtle clues in style, content
                                                                          , formatting, semantics, grammar, and vocabulary,
Here, we show the prompt templates we used                                flow and inconsistencies
                                                                    9. Pay close attention to the writing style of the why=”
across the different stages of our pipeline (curly-                       EXPLANATION” in the examples. YOU SHOULD USE THE SAME
braced fields are runtime substitutions).                                  WRITING STYLE as the explanations, thinking out loud
                                                                           and from your perspective (”I guess”, ”maybe”, ”this
                                                                           ’doesnt make sense”, ”I think”, . . . ), honest,
                                                                          simple English, with a 80-90 Flesch score. However,
 TELL                                                                     do not copy the content, exact clues, or topic since
 Used in the main model                                                   that will be different for each input. Try to be
                                                                          creative.
                                                                    10. Keep annotations balanced. All texts contain both AI
 Rules:                                                                   and human tells. Make sure the majority of the tells
 - Reproduce the ENTIRE document character by character —                 support the known label, but include 20-40\% of the
       no omissions.                                                      opposite label tells as well. This helps to keep your
 - EXPLANATION: specific mechanism-based reason why SPAN is                annotation nuanced and credible, and prevents it
        a tell; not generic or vague.                                     from being too one-sided
 - SCORE is a float 0.0..1.0: 0.0-0.25 weak, 0.25-0.75
       moderate, 0.75-1.0 only for undeniable evidence.             {Style example for the annotation procedure is included
 - Add >=1 tell; nested spans allowed. Think like a                       here - depending on the label (AI/human) of the
       detective: style, content, formatting, semantics,                  document}
       grammar, vocabulary, inconsistencies.
 - Maximize granularity: prefer small focused spans.                Here is the real pair to annotate.
 - OUTPUT ONLY: <text>doc text...<span>TELL<annotation type
       =”AI|human” why=”EXPLANATION” score=”0.0..1.0” /></          Human:
       span>...more doc...<verdict type=”AI|human” why=”            <<<
       VERDICT” score=”0.0..1.0” /></text>                          {human text}
                                                                    >>>
 Text:
 <<<                                                                AI:
 {main text}                                                        <<<
 >>>                                                                {AI text}
                                                                    >>>

                                                                    Annotate only the {target label} text. The other text is
                                                                          secret context to help you notice differences and
 SFT data generation                                                      possible tells.
 Used to generate training data for the SFT stage
                                                                    Now output exactly this structure:
 using paired examples from Thai et al. (2025)                      <span>ANNOTATED TARGET TEXT<annotation type=”LABEL” why=”
                                                                          ONE SHORT GLOBAL COMMENT” score=”FLOAT” /></span>
 (Section 2.2.2)

 You are an annotator of AI or human tells. You have a
       target text in front of you, to annotate it with             SFT data generation
       tells to say why it looks like it was written by
       either AI or a human.                                        Used to turn real human annotations from Russell
 Use this exact compact format:
                                                                    et al. (2025) into training data for the SFT stage
 <span>ANNOTATED_TEXT<annotation type=”LABEL” why=”                 (Section 2.2.1)
       EXPLANATION” score=”FLOAT” /></span>

 Important:                                                         Annotate a text with AI-or-human tells. Wrap individual
 1. Copy the target text exactly in ANNOTATED_TEXT after                  spans like this:
       XML decoding. Do not fix typos, spacing, punctuation,        <span>ANNOTATED_TEXT<annotation type=”LABEL” why=”
        Unicode, casing, or grammar. In the XML output, text              EXPLANATION” score=”FLOAT” /></span>
        runs inside spans must use the same XML escaping as
       the target text                                              Rules:
 2. label must be exactly ”AI” or ”human”                           - Copy the text exactly: no typo fixes, no reformatting.
 3. score must be 0.0 to 1.0 and indicate how much that                   Use the same XML escaping as the input.
       exact tell should move the document decision. Use the        - type is ”AI” or ”human”. score is 0.0–1.0 (0–0.25 weak,
        full range: 0.0-0.25 for weak hints, 0.35-0.65 for                0.35–0.65 moderate, 0.75–1.0 strong).
       moderate evidence, and 0.75-1.0 only for undeniable          - Keep spans small and granular: annotate a word or phrase,
       evidence. Try to have a varied range of scores. For                 not a whole sentence.
       the outer annotation, pick a score that makes sense          - Write the why in first person, YOU are the annotator.
       based on the tells you found in the text.                          Mirror the exact writing style and voice of the hint;
 4. Wrap the whole target text in one outer annotation too.                same vocabulary, same rhythm. Keep it casual and
        The output must start with <span> and end with </                 direct; no academic language, no formal analysis,
       span>, with the outer <annotation ... /> immediately               simple English. Never write ”the reviewer said/
       before the final </span>                                           pointed out/noted”, you ARE the one observing this.
 5. Try to be as granular as possible; ’its better to keep          - You ’dont know the hint when writing the annotation (
       spans small, e.g., annotate a specific character                   since that’s what you write at the end), so you ’cant
       instead of a whole word or phrase                                   refer to it, though you can write as if you have the
 6. The explanations must be detailed and explicitly                       same knowledge as the hint (e.g. if the hint points
       explain why the span is a tell for the given label,                out a specific detail, you can also mention that
       by explaining the mechanism that leads to the tell,                detail in your explanation, since you know it from
       you should teach the reader your reasoning process                 reading the text).
 7. Use the reference text to help spot differences and             - You should annotate ALL the items in the hint, be
       clues, but you ’mustnt directly compare the target                 comprehensive in your annotations. DO NOT annotate
       text to the reference text in your annotations, you                items that are not in the hint.
       ’CANT MENTION IT EXISTS but you can quote things from        - The why=”...” explanations can be concise if you already
        the reference text as “a human/AI might say e.g.                   explained why a pattern is a tell, i.e., don’t
       . . . ”, because the annotations should be valid even              repeat the mechanism, a short callback (”again, XXX”,
       if you ONLY saw the target text alone                               ”another XXX”) is enough. Try to use the same words




                                                               19
      and phrasing as the hint in your explanations when           The research team tested six genetic lines in which the
      possible, since ’thats the voice we want to capture.               number of light-sensitive neurons ranged from one to
- Output the full text with inline spans inserted, do NOT                all 302 the worms possessed. Stimulation had a
      add any outer wrapper.                                             different effect in each line, making the worm turn,
- The explanations should explain the mechanism (the                     for instance, or preventing it from turning. The
      underlying cause that would make an AI or human                    scientists first collected training data by flashing
      produce that exact text) that is explicit or implicit              lights randomly at the worms for five hours, then fed
       in the hint. For example, instead of ”this is a                    the data to the AI agent to find patterns before
      funny contradiction, and it feels very human” (                    putting the agent loose.
      feeling human is not a mechanism), the hint said ”
      definitely not something I would expect from machine-        With five of the six lines, including the line where all
      generated text”, so we can write ”this is a funny                  neurons responded to light, the agent learned to
      contradiction, definitely not something I would                    direct the worm to the target faster than if the worm
      expect from machine-generated text because AI lacks                 had been left alone or the light had flashed
      creativity” (the mechanism is that AI lacks                        randomly. ’Whats more, the agent and the worm
      creativity, and would be unlikely to pick that word).              cooperated: if the agent steered the worm straight
- Avoid unspecific, generic mechanisms: ”feels like                      toward a target but there were small obstacles in the
      something a person would choose”, ”it ’doesnt feel                  path, the worm would crawl around them.
      like AI”, ”this is a common human pattern”... all of
      these are NOT mechanisms that can be checked and             Dr. Thang, an engineer at the University of Queensland in
      verified. Think about what is the underlying reason.               Australia, who has independently worked on cyborg
      We need specific, checkable mechanisms about how AI                insects, praised the work for its simple setup—
      works or is trained, or about the limitations and                  reinforcement learning is flexible, and AI based on
      reality of the world, or anything that an external                 it can figure out how to perform complex tasks.
      observer could verify. This should be grounded on the              According to Harvard University biophysicist Dr. Li,
       specific text and the specific hint.                              the ’papers lead author, “one can easily see how it
- You can also add notes for the human reader to check                   might be extended to harder problems”. Her team is
      things we ’cant verify but an external observer could              now exploring whether their method can improve
      , e.g. ”(to be checked: is Dr. Thang actually a                    electrical deep-brain stimulation to treat
      doctor?)”                                                          ’Parkinsons disease in humans by adjusting the
                                                                         voltage used and its timing. One day reinforcement
Example:                                                                 learning plus implants might even give us new skills,
                                                                          Li says—artificial and real neural nets united.
Reviewer hint:                                                     >>>
<<<
Some of the ’authors assertions are so garbled that only a         Annotated:
       human who ’doesnt quite understand the process must         <<<
      have written it. For example, referring to a patch of        Scientists have given artificial intelligence a direct
       Escherichia coli (which ’Im guessing is E. coli) as               line into the nervous systems of millimeter-long
      “a tasty ”snack is a funny contradiction, and                      worms, letting it guide the creatures to a tasty
      definitely not something I would expect from machine-              target—and demonstrating intriguing brain-AI
      generated text. Or maybe ’its an L2 English speaker,               collaboration. They trained the AI with a methodology
      when one considers that the author wants to “put the                called deep-reinforcement learning; the same is used
      agent ”loose upon those poor worms. The purpose and                 to help AI players learn to master games such as Go.
      methodology of the study are also quite detailed and                An artificial neural network, software roughly
      well-explained, whereas AI seems to be vague around                modeled on biological brains, analyzes strings of
      these subjects as it feels like it lacks                           actions and outcomes, extracting strategies for an AI
      understanding and would rather say less than be                     “”agent to interact with its environment and achieve
      incorrect. The Latin names are not italicized and                   a goal.
      ‘’one should be capitalized as it’s at the beginning
      of a spoken sentence. Though something that throws me        In the study, published in Nature Machine Intelligence,
       off is that all names are referred to as ‘Dr’., even              researchers trained an AI agent to direct <span>one-
       the engineer. It also ’doesnt follow the formulaic                millimeter-long<annotation type=”human” why=”The
      structure that AI likes to use, e.g. ’theres no bland              purpose and methodology of the study are quite
       conclusion at the end.                                            detailed and well-explained, whereas AI seems to be
>>>                                                                      vague around these subjects as it feels like it lacks
                                                                          understanding and would rather say less than be
human text:                                                              incorrect” score=”0.58” /></span> <span>
<<<                                                                      Caenorhabditis elegans<annotation type=”human” why=”
Scientists have given artificial intelligence a direct                   Latin name is not italicized; should be capitalized
      line into the nervous systems of millimeter-long                   as ’its at the beginning of a spoken sentence” score=
      worms, letting it guide the creatures to a tasty                   ”0.43” /></span> worms toward <span>tasty<annotation
      target—and demonstrating intriguing brain-AI                       type=”human” why=”this is a funny contradiction,
      collaboration. They trained the AI with a methodology              definitely not something I would expect from machine-
       called deep-reinforcement learning; the same is used              generated text because AI lacks creativity” score=”
       to help AI players learn to master games such as Go.              0.74” /></span> patches of <span>Escherichia coli<
       An artificial neural network, software roughly                    annotation type=”human” why=”Latin name is not
      modeled on biological brains, analyzes strings of                  italicized” score=”” /></span> in a four-centimeter
      actions and outcomes, extracting strategies for an AI              dish. A nearby camera recorded the location and
       “”agent to interact with its environment and achieve              orientation of every ’worms head and body; <span>
       a goal.                                                           three times per second<annotation type=”human” why=”
                                                                         again, very specific; only someone who actually ran
In the study, published in Nature Machine Intelligence,                  the experiment can know that” score=”0.61” /></span>
      researchers trained an AI agent to direct one-                     the agent received this information for <span>the
      millimeter-long Caenorhabditis elegans worms toward                previous 15 frames<annotation type=”human” why=”
      tasty patches of Escherichia coli in a four-                       another specific detail” score=”0.59” /></span>,
      centimeter dish. A nearby camera recorded the                      giving it a sense of the past and present at each
      location and orientation of every ’worms head and                  moment. The agent could also turn on or off a light
      body; three times per second the agent received this               aimed at the dish. The worms were optogenetically
      information for the previous 15 frames, giving it a                engineered so certain neurons would become active or
      sense of the past and present at each moment. The                  inactive in response to the light, sometimes
      agent could also turn on or off a light aimed at the               prompting movement.
      dish. The worms were optogenetically engineered so
      certain neurons would become active or inactive in           The research team tested six genetic lines in which the
      response to the light, sometimes prompting movement.               number of light-sensitive neurons ranged from one to
                                                                         <span>all 302<annotation type=”human” why=”exact




                                                              20
      count; AI might have approximated “(about ”300)”             Credibility (0.0..1.0): how well does the why= explanation
      score=”0.60” /></span> the worms possessed.                         identify a specific, mechanistic reason the span (or
      Stimulation had a different effect in each line,                    the overall verdict) is a tell for the stated type?
      making the worm turn, for instance, or preventing it               A mechanism is the underlying cause that would make
      from turning. The scientists first collected training              an AI or human produce that exact text. Use the full
       data by flashing lights randomly at the worms for                 range: 0.0 for vague, generic, or incorrect
      five hours, then fed the data to the AI agent to find              mechanisms; 1.0 only for explanations that state an
       patterns before <span>putting<annotation type=”human              undeniable mechanism. Also reward explanations that
      ” why=”odd word; maybe the author is an L2 English                 feel like a human reviewer would write over polished
      speaker” score=”0.62” /></span> the agent loose.                   explanations. If there are no <span> annotations, you
                                                                          should still score the overall verdict.
With five of the six lines, including the line where all
      neurons responded to light, the agent learned to             Example input 1:
      direct the worm to the target faster than if the worm        <<<
       had been left alone or the light had flashed                <span>**<annotation id=”1” type=”AI” why=”markdown; AI
      randomly. ’Whats more, the agent and the worm                      often adds markdown formatting because chat and
      cooperated: if the agent steered the worm straight                 writing tools make it easy” /></span>Apple to build <
      toward a target but there were small obstacles in the              span>\$1.375<annotation id=”2” type=”human” why=”odd
       path, the worm would crawl around them.                           exact dollar amount; AI is more likely to fill in a
                                                                         generic amount like \$1.234” /></span> billion data
<span>Dr. Thang<annotation type=”AI” why=”Dr. or engineer?               center. CEO Tim Cook announced Thursday that the
       It throws me off that all names are referred to as                company will build a <span>\$1.375 billion<annotation
      ‘Dr’., AI might assume that since ’its common to have               id=”3” type=”human” why=”redundant; humans tend to
       it in universities (to be checked: is Dr. Thang                   repeat their own text” /></span> data center located
      actually a doctor?)” score=”0.51” /></span>, an                    on <span>2,000<annotation id=”4” type=”human” why=”
      engineer at the University of Queensland in Australia              specific land size” /></span> acres of land in <span>
      , who has independently worked on cyborg insects,                  Waukee, Iowa<annotation id=”5” type=”human” why=”
      praised the work for its simple setup—reinforcement                specific location” /></span>. <span>Would you like me
      learning is flexible, and AI based on it can figure                 to continue?<annotation id=”6” type=”AI” why=”
      out how to perform complex tasks. According to                     chatbot speak” /></span>.
      Harvard University biophysicist Dr. Li, the ’papers          >>>
      lead author, <span“>one<annotation type=”human” why=”
      lowercase at the start of a quote; ’thats wrong, AI          Overall verdict (type=”AI”): This text is AI because it is
      would use the standard format, but a human might not                very generic and doesn’t have the specific details
      notice” score=”0.46” /></span> can easily see how it               and redundancies that a human would include.
      might be extended to harder problems”. Her team is
      now exploring whether their method can improve               Example reasoning 1:
      electrical deep-brain stimulation to treat                   1. markdown: can’t use writing tools without hands —
      ’Parkinsons disease in humans by adjusting the                     mechanism is wrong (credibility=0.20)
      voltage used and its timing. One day reinforcement           2. odd exact dollar amount: true, averaged training data
      learning plus implants might even give us new skills,              makes AIs produce generic numbers (credibility=0.65)
       Li says—<span>artificial and real neural nets united        3. redundant exact dollar amount: flipped — repetition
      .<annotation type=”human” why=”This ’doesnt follow                 artifacts are AI tells, not human (credibility=0.00)
      the formulaic structure that AI likes to use; e.g. a         4. specific land size: 2,000 is a round number, not
      bland conclusion at the end to make the text feel                  specific — explanation is false (credibility=0.10)
      complete” score=”0.69” /></span>                             5. specific location: specific detail that grounds the
>>>                                                                      story, strong human tell (credibility=0.75)
                                                                   6. chatbot speak: undeniable, no human would write this
---                                                                      unprompted (credibility=1.00)
                                                                   Overall verdict: it doesn’t specify the mechanisms, just a
Reviewer hint:                                                            vague claim of ”generic and doesn’t have specific
<<<                                                                      details” — low credibility (credibility=0.10)
{annotator comment}
>>>                                                                Example input 2:
                                                                   <<<
Find ALL the exact spans in the text that correspond to            The <span>mechanism<annotation type=”AI” why=”classic AI
      these clues and annotate them. Be comprehensive —                  phrase” /></span> of fever is <span>largely caused by
      cover every clue in the hint, don’t skip any. Do not                the release of endorphins<annotation id=”1” type=”AI
      add tells that aren’t in the hint.                                 ” why=”this is false, a real doctor would know
If you cannot locate any of the clues as specific spans,                 endorphins reduce stress” /></span> <span>( cytokines
      output exactly: SKIP                                                ) , which affect the <span>brains<annotation id=”2”
                                                                         type=”human” why=”typo; humans can make them easily
{target label (AI/human)}:                                               by typing quickly, but AI is trained specifically to
<<<                                                                      avoid such errors” /></span> temperature <span>centre
{target text}                                                            <annotation id=”3” type=”AI” why=”British spelling;
>>>                                                                      typical of AI” /></span> and trigger the <span>bodys
                                                                         respons<annotation id=”4” type=”human” why=”typo
Annotated:                                                               again” /></span> to cold.
                                                                   >>>

                                                                   Overall verdict (type=”human”): To me, this is written by
Annotation judge                                                         AI. I was thinking that it could be human at first,
                                                                         because there are some typos that could be a human
Used to score the credibility of annotations dur-                        signal, but then I realized that there is a
                                                                         hallucination that no real doctor would make. To me,
ing RL (Section 2.2.2)                                                   it’s clear, this is AI written.

                                                                   Example reasoning 2:
You are a critical evaluator of authorship-detection
                                                                   1. classic AI phrase: doesn’t explain the mechanism (
      annotations.
                                                                         credibility=0.00)
                                                                   2. false medical claim: undeniable falsehood, no real
The annotated document uses <span>text<annotation id=”N”
                                                                         doctor would say this (credibility=1.00)
      type=”AI|human” why=”explanation” /></span> to mark
                                                                   3. typo: undeniable, AI is trained to avoid typos (
      evidence spans. The id= tells you exactly how many
                                                                         credibility=0.95)
      annotations there are. Rate each annotation and the
                                                                   4. British spelling: not a strong signal, many AIs are
      Overall verdict for credibility.
                                                                         trained on American text (credibility=0.20)




                                                              21
5. typo again: undeniable, strong human signal (                   Win-rate style rewrite
      credibility=0.95)
6. punctuation errors: strong human signal, AI is trained
      to produce polished text (credibility=0.82)                  Rewrite the comment below so it matches the writing style
Overall verdict: it’s detailed and specific about the                    of the example comment.
      mechanisms, creative and comprehensive. Plus, the
      explanation language is a bit chatty and                     Rules:
      conversational, which feels like a human would write,        - Change wording, tone, and sentence flow only. Rewrite
       so I gave it a higher credibility score (credibility              the style, but keep the same content.
      =0.95)                                                       - Do NOT add, remove, or alter factual claims, cited
                                                                         evidence, or the AI/human conclusion.
Input:                                                             - Keep the same evidence points and the same guess
<<<                                                                      direction.
{text}                                                             - Do not mention rewriting, style matching, or the example.
>>>
Overall verdict (type=”{generated verdict type}”): {               - Put the rewritten comment only inside <<< and >>>.
      generated verdict}                                                 Nothing before <<< or after >>>.

                                                                   Style example (match this voice and cadence, not the facts)
                                                                         :
                                                                   <<<
Win-rate judge                                                     I think this is human, and I would even guess it comes
                                                                         from a real encyclopedia entry. The facts are very
                                                                         specific: a full birth date, a city, a job title, a
You are ranking how convincing evidence explanations are.                war deployment, a time window, and a sports role. The
                                                                           sentence has a real compressed biographical rhythm,
Task:                                                                    with several facts packed into one line. The
Given a source document and {number of candidates} blinded               bracketed citation marks are a strong clue that this
       evidence explanations from different annotators,                  was copied from a sourced page, not invented as a
      rank all explanations from best to worst according to              smooth paragraph.
       how convincing the cited evidence and explanation           >>>
      are.
                                                                   Human comment to rewrite:
Criteria:                                                          <<<
1) Concrete local evidence: specific ideas, elements, or           {{human comment}}
      details that are specific to the document.                   >>>
2) Falsifiability: the explanation should make a specific
      claim a skeptical reader can verify in the document.
      It’s not enough to say what the evidence is, the
      explanation should explain why that evidence supports
       the claim.
3) Internal coherence: the evidence should support the
      explanation’s own AI/human authorship claim without
      contradicting itself.
4) Human plausibility: a concise forensic observation can
      beat a polished checklist if it identifies a decisive
       cue.
5) Real world grounding: the evidence and explanation
      should fit the document’s genre, situation, and
      general world knowledge.

Important:
- You do not know the true label. Do not use or assume any
       ground-truth AI/human answer.
- Only rate based on content, not writing style.
- Rank explanation convincingness only from the source
      document and the candidate explanation.
- You must rank all {number of candidates} items uniquely:
       rank 1 is most convincing, rank {number of
      candidates} is least convincing.
- Output JSON only. Do not write any rationale, summary,
      or commentary outside the ranking array.

Return exactly:
{{
   ”ranking”: [
     {{”item_id”: ”A1”, ”rank”: 1, ”quality_score”: 0.93}},
     ...
   ]
}}

Constraints:
- Include exactly {number of candidates} entries in
      ranking.
- item_id must match one from the candidate list.
- rank must be integers 1..{number of candidates}, unique.
- quality_score should be float in [0,1], higher is better.


Document:
<document>
{document}
</document>

Candidates (blinded):
{candidates}




                                                              22
C   SFT details
We pre-train the policy with supervised fine-tuning
(SFT) before GRPO to initialize the annotation
format and label-hint following. Table 4 lists all
hyperparameters.
Compute. All training was performed on the Tin-
ker platform (Thinking Machines). SFT ran for
2 epochs (≈1440 examples) and completed in ap-
proximately 2 hours. GRPO ran for 310 steps with
early stopping and completed in approximately 12
hours. Inference for SFT data generation (GPT-
5.5 annotations) and win-rate evaluation was per-
formed via the respective model providers’ APIs.
Loss masking. Only completion tokens receive
a cross-entropy loss weight of 1; all prompt to-
kens (instruction, document, and analysis-channel
stub) are masked with weight 0. This ensures the
model is supervised solely on the annotation output
distribution.
Paced annotation dropout. To prevent the
model from memorising densely-annotated exam-
ples (since some in our dataset have too many anno-
tations clustered together), we stochastically drop
nested span annotations before each training step.
The target density is one annotation per 20 docu-
ment words; spans with higher credibility scores
(score = 1.0) are 3× less likely to be dropped than
low-credibility spans.
Label-hint contrastive CE. Each expert-
annotated example is paired with a label hint
injected into the analysis channel. A contrastive
cross-entropy auxiliary step is run on each hint:
a “correct hint” forward pass (hint matches
ground-truth label) and a “flipped hint” forward
pass (hint is wrong) are both performed, and
the model is trained to assign higher probability
to the correct outer annotation type under the
correct hint. This teaches the model to follow
label-conditioning signals used during GRPO
sampling.




                                                      23
                      Table 4: SFT pre-training hyperparameters.

Hyperparameter                      Value
Model
Base model                          GPT-OSS 120B
LoRA rank                           32
Optimization
Optimizer                           Adam
Learning rate                       5 × 10−5
Batch size                          8
Epochs                              1
Random seed                         2262
Data
Total training examples             1,440
Loss masking                        Completion-only (prompt tokens have weight 0)
Label-hint injection
Enabled                             Yes (all examples)
Hint mix ratio                      1.0
Contrastive hint CE                 Yes (correct + flipped-label pair per example)
Hint-CE learning rate scale         2.0×
Hint-CE target follow rate (EMA)    0.99
Hint-CE EMA α                       0.1




                                         24
D   Selection of the annotation format                         • <text> at the start of the text section (emitted
                                                                 only once)

                                                               • <span> to open each “tell” annotation

                                                               • <annotation type=" to be written before
                                                                 closing the annotation

                                                               • " why=" to be written before the explanation

                                                               • " score=" to be written before the credibility
                                                                 score

                                                               • " /></span> to be written at the end of the
                                                                 annotation

                                                               It can be observed that these special tokens are
                                                            not the original XML tokens the model would
While we first experimented with an XML-based               have observed, so effectively the model is learning
format (<span type="AI|human" why="..."                     a syntax akin to [SPECIAL TOKEN]abc[SPECIAL
score="0.0">TEXT</span>), we felt it was con-               TOKEN]def[SPECIAL TOKEN]AI|human[SPECIAL
ceptually off: we work with causal models, and              TOKEN]explanation[SPECIAL
XML requires that attributes go in the opening tag,         TOKEN]score[SPECIAL TOKEN]. . . .
which means the model would have to decide how
to annotate a span before writing it, rather than
writing the text and then annotating it. This is not
necessarily problematic since the full text is visi-
ble in the input, but we found it cleaner to have a
format where the attributes come after the text.




   We also considered moving attributes to the clos-
ing </span> tag, but we expected that would fight
the model’s strong conditioning on generating valid
XML and hurt performance. A Markdown-inspired
format could be an interesting alternative, but the
syntax used easily conflicts with natural text, and
our tests showed that the model easily collapsed
with this paradigm. We finally found the best syn-
tax to be XML-based (<span>TEXT<annotation
type="AI/human" why="..." score="0.0"
/></span>).




   Additionally, we added custom special tokens
on the annotation’s fixed positions, to decrease the
likelihood of format collapse and token usage:

                                                       25
E    Detector benchmark details                              the quality of the explanation exclusively, ignoring
                                                             external factors that cannot be verified.
This appendix contains the full detector benchmark
results from Section 3.1.

Overall ranking (Table 5). The † markers indi-
cate that the gap between TELL and the next two
detectors (MAGE, Pangram EditLens) is not sta-
tistically significant, nor are several gaps within
the mid-tier cluster at ranks 7–11 (DetectLLM-
NPR through LogRank). Binoculars (0.616) and
DNA-GPT (0.581) perform substantially below
what their original papers report, consistent with
the replication gap we discuss in Section 1.

Pairwise significance (Table 6). TELL’s advan-
tage over every detector from rank 4 downward
is statistically significant (BH-corrected DeLong
test, FDR q = 0.05); the only non-bold positive
entries in TELL’s row are MAGE and Pangram Ed-
itLens. Within ranks 7–11, many pairwise gaps are
also non-significant, so the ordering among those
detectors should not be over-interpreted.

Per-domain breakdown (Table 7). Aggregate
AUROC masks substantial variation across do-
mains.       Some detectors reach near-perfect
scores on specific domains — T5Sentinel
achieves 1.000 on web_text, MAGE 0.999 on
commonsense_completion, ChatGPT-D 1.000 on
finance despite ranking 13th overall — while
dropping considerably elsewhere, which suggests
domain-specific distributional signals rather than
general detection ability. TELL’s weakest domain
is commonsense_completion (0.734); we attribute
this partly to limited coverage of that domain in our
training data. Overall, TELL is the most consistent
detector across domains, with no domain where it
substantially underperforms the field.

Reward hacking. Also, while training, we ob-
served that the model sometimes learns to “hack”
the reward function by making the annotations
seem more credible — through deception. For
instance, the model learned to write “this is a very
common strong AI sign” as a suffix to all its AI
spans, which caused the judge to give higher re-
wards to all those spans, even though there was
essentially no extra information in that phrase. We
also saw cases of the model lying and saying e.g.
“I’ve seen the way the author uses punctuation in
other texts, and this shows a similar pattern”. We
adjusted our judge prompt to base its reward on

                                                        26
Table 5: Detector ranking on the TELL benchmark test set (n = 5000). Failed rows imputed to score 0. AUROC
95% CIs from bootstrap resampling (B = 10,000). Mean Kendall τ = 0.9753. † gap not significant vs. adjacent
rank below (DeLong, BH FDR q = 0.05).

   Rank          Detector                                          AUROC                           95% CI                           TPR@1%FPR                         P (rank holds)
          1      TELL (ours)                                            0.9270           [0.9192, 0.9348]                                0.6380                                     0.993
          2      MAGE                                                   0.9132           [0.9042, 0.9219]                                0.0424                                    0.647†
          3      Pangram EditLens                                       0.9111           [0.9028, 0.9191]                                0.5828                                     1.000
          4      Fast-DetectGPT                                         0.8609           [0.8497, 0.8716]                                0.5896                                     1.000
          5      ArguGPT                                                0.8281           [0.8164, 0.8397]                                0.4328                                     1.000
          6      T5Sentinel                                             0.8020           [0.7898, 0.8141]                                0.1748                                     0.985
          7      DetectLLM-NPR                                          0.7824           [0.7692, 0.7953]                                0.3196                                    0.749†
          8      OpenAI RoBERTa                                         0.7770           [0.7639, 0.7894]                                0.3308                                    0.622†
          9      AIGC MPU                                               0.7741           [0.7610, 0.7868]                                0.1160                                    0.899†
         10      DetectLLM-LRR                                          0.7627           [0.7494, 0.7759]                                0.2716                                    0.957†
         11      LogRank GPT-2-medium                                   0.7573           [0.7440, 0.7707]                                0.2320                                    0.913†
         12      RADAR                                                  0.7441           [0.7301, 0.7583]                                0.0128                                     1.000
         13      ChatGPT-D                                              0.6972           [0.6824, 0.7112]                                0.1660                                     1.000
         14      Binoculars                                             0.6162           [0.6006, 0.6320]                                0.0140                                     0.999
         15      DNA-GPT                                                0.5809           [0.5662, 0.5954]                                0.0000                                     1.000
         16      PHD RoBERTa                                            0.5206           [0.5045, 0.5371]                                0.0460                                   —




Table 6: Pairwise ∆AUROC (row − col). Bold = BH-significant (DeLong test, FDR q = 0.05, 120 comparisons).
Detectors ordered by rank (left/top = best).

              TELL     MAGE      Pangram   F-DGT     ArguGPT    T5Sent.    DL-NPR      OAI-RB      AIGC MPU        DL-LRR       LogRank   RADAR        CGPT-D         Binoc.     DNA-GPT    PHD
TELL            —       0.014     0.016     0.066     0.099       0.125      0.145       0.150         0.153            0.164    0.170         0.183       0.230       0.311       0.346    0.406
MAGE          −0.014     —        0.002     0.052     0.085       0.111      0.131       0.136         0.139            0.151    0.156         0.169       0.216       0.297       0.332    0.393
Pangram       −0.016   −0.002      —        0.050     0.083       0.109      0.129       0.134         0.137            0.148    0.154         0.167       0.214       0.295       0.330    0.390
F-DGT         −0.066   −0.052    −0.050      —        0.033       0.059      0.078       0.084         0.087            0.098    0.104         0.117       0.164       0.245       0.280    0.340
ArguGPT       −0.099   −0.085    −0.083    −0.033      —          0.026      0.046       0.051         0.054            0.065    0.071         0.084       0.131       0.212       0.247    0.307
T5Sent.       −0.125   −0.111    −0.109    −0.059    −0.026        —         0.020       0.025         0.028            0.039    0.045         0.058       0.105       0.186       0.221    0.281
DL-NPR        −0.145   −0.131    −0.129    −0.078    −0.046      −0.020       —          0.005         0.008            0.020    0.025         0.038       0.085       0.166       0.201    0.262
OAI-RB        −0.150   −0.136    −0.134    −0.084    −0.051      −0.025     −0.005        —            0.003            0.014    0.020         0.033       0.080       0.161       0.196    0.256
AIGC MPU      −0.153   −0.139    −0.137    −0.087    −0.054      −0.028     −0.008      −0.003          —               0.011    0.017         0.030       0.077       0.158       0.193    0.253
DL-LRR        −0.164   −0.151    −0.148    −0.098    −0.065      −0.039     −0.020      −0.014        −0.011             —       0.005         0.019       0.066       0.146       0.182    0.242
LogRank       −0.170   −0.156    −0.154    −0.104    −0.071      −0.045     −0.025      −0.020        −0.017           −0.005     —            0.013       0.060       0.141       0.176    0.237
RADAR         −0.183   −0.169    −0.167    −0.117    −0.084      −0.058     −0.038      −0.033        −0.030           −0.019   −0.013          —          0.047       0.128       0.163    0.223
CGPT-D        −0.230   −0.216    −0.214    −0.164    −0.131      −0.105     −0.085      −0.080        −0.077           −0.066   −0.060        −0.047        —          0.081       0.116    0.177
Binoc.        −0.311   −0.297    −0.295    −0.245    −0.212      −0.186     −0.166      −0.161        −0.158           −0.146   −0.141        −0.128      −0.081        —          0.035    0.096
DNA-GPT       −0.346   −0.332    −0.330    −0.280    −0.247      −0.221     −0.201      −0.196        −0.193           −0.182   −0.176        −0.163      −0.116      −0.035        —       0.060
PHD           −0.406   −0.393    −0.390    −0.340    −0.307      −0.281     −0.262      −0.256        −0.253           −0.242   −0.237        −0.223      −0.177      −0.096      −0.060     —




Table 7: Per-domain AUROC on the TELL benchmark test set. Best result per domain in bold. Detectors ordered
by overall rank (left = best).

Domain                   TELL     MAGE     Pangram   F-DGT     ArguGPT    T5Sent.    DL-NPR      OAI-RB   AIGC MPU         DL-LRR    LogRank     RADAR      CGPT-D       Binoc.   DNA-GPT   PHD
academic_abstract        0.971     0.970    0.942    0.860      0.862     0.880       0.759       0.747        0.762        0.783     0.738       0.782       0.735      0.515      0.574   0.503
commonsense_completion   0.734     0.999    0.500    0.689      0.506     0.367       0.581       0.522        0.418        0.646     0.654       0.336       0.487      0.320      0.600   0.703
creative_writing         0.928     0.894    0.908    0.855      0.812     0.658       0.805       0.703        0.838        0.800     0.805       0.701       0.625      0.628      0.618   0.515
educational_web          0.993     0.840    1.000    0.965      0.926     0.877       0.863       0.759        0.947        0.760     0.862       0.956       0.631      0.809      0.608   0.409
email                    0.998     0.921    1.000    0.919      0.989     0.625       0.956       0.547        0.991        0.931     0.943       0.740       0.884      0.733      0.492   0.518
encyclopedic_reference   0.911     0.902    0.899    0.888      0.782     0.888       0.785       0.877        0.642        0.794     0.764       0.913       0.724      0.632      0.576   0.548
finance                  0.964     0.987    0.989    0.986      0.997     0.605       0.987       0.986        0.919        0.976     0.981       0.647       1.000      0.779      0.798   0.842
forum_qa                 0.921     0.984    0.924    0.887      0.864     0.808       0.878       0.834        0.723        0.870     0.859       0.781       0.803      0.637      0.594   0.544
howto_instructional      0.896     0.730    0.934    0.879      0.720     0.845       0.745       0.798        0.734        0.697     0.702       0.606       0.558      0.676      0.532   0.634
news                     0.901     0.966    0.913    0.867      0.817     0.847       0.744       0.807        0.823        0.730     0.715       0.838       0.670      0.625      0.554   0.435
review_opinion           0.930     0.974    0.905    0.846      0.858     0.822       0.816       0.782        0.768        0.789     0.784       0.748       0.729      0.649      0.592   0.427
student_essay            0.993     0.952    0.997    0.914      0.990     0.948       0.967       0.945        0.979        0.909     0.941       0.919       0.787      0.809      0.632   0.656
web_text                 0.785     0.609    0.804    0.598      0.538     1.000       0.352       0.757        0.485        0.430     0.335       0.860       0.554      0.425      0.469   0.465




                                                                                          27
F   Win-Rate evaluation                                       F.1      Example of one of the evaluations.
Here, we share additional details on how we de-               Here, we show a specific example to illustrate how
signed and performed our win-rate evaluations.                the win-rate evaluation works in practice. We keep
   We evaluate explanation quality with a blinded             the original JSON structure because we believe it
listwise judge study on the TELL human-detectors              makes the examples simpler to understand.
validation set (to reduce computational costs).                  The first part of the pipeline rewrites the human
For each of 200 documents, we sample one                      annotations into a more standard format to diminish
model explanation from the trained policy and                 the influence of writing style on the evaluation:
compare it to five human annotator explana-
tions. We style-normalize the human comments                   Evaluation example before rewriting
(see below) so judges compare their content
                                                               ”annotator_1”: {
rather than surface form. We thus present the                     ”comment”: ”The quotes in this piece of text come across
                                                                       as very natural. Some fit in well, others need
judges with six candidates in a random blind                          surrounding text to make sense, and the sources are
order, and each “member” of a five-judge                              varied. The professors are also not referred to as
                                                                      doctors, even though they’re probably qualified
panel (GPT-5.4-mini, DeepSeek-V4-Flash,                               enough. There’s also just an absence of anything that
                                                                       might point towards it being AI-generated. ”,
NVIDIA-Nemotron-3-Super-120B-A12B,                                ”confidence”: 4,
                                                                  ”guess”: ”Human-Generated”
gemma-4-26b and GPT-OSS-120B) produces                         },
a full ranking from most to least convincing.                  ”annotator_2”: {
                                                                  ”comment”: ”There are none of the usual AI-repeated
   From each ranking we derive a document-level                       words. There is a wider range of vocabulary than
                                                                      usual for AI.”,
win rate: the fraction of pairwise model-human                    ”confidence”: 4,
comparisons the model wins within that document                   ”guess”: ”Human-Generated”
                                                               },
(ties count as 0.5). Our primary metric is the panel           ”annotator_3”: {
                                                                  ”comment”: ”Here’s why I think it’s human-generated:
document win rate, the mean of these per-document                     Instead of saying things like ’researchers don’t
rates averaged across judges. In inference, we                        agree on’ AI would have said ’researchers disagree on
                                                                      ’. Missing punctuation marks. ”,
treat the document as the unit of analysis: we                    ”confidence”: 5,
                                                                  ”guess”: ”Human-Generated”
test whether the panel mean exceeds 0.5 (no aggre-             },
                                                               ”annotator_4”: {
gate advantage) with a one-sided sign-flip permu-                 ”comment”: ”While the writing is more simplistic, it’s
tation test and a one-sided Wilcoxon signed-rank                      able to convey the topic well. It uses dashes, colons
                                                                      , and commas to intersperse information with quotes,
test on per-document panel scores, and we report                      works with simple, easy to understand phrases such as
                                                                       \”a leg up compared to all other species.\” and \”
a 95% confidence interval by bootstrapping the                        Pagel, on the other hand, is less sure about hand
documents. We report the per-judge results as a                       gestures.\” as a way to explain information in a
                                                                      readable format. It even adds unique phrases, such as
robustness check (with Holm-adjusted p-values to                       \”a small repertoire of sounds and signals with
                                                                      various meanings\” to add to the content. While there
account for testing multiple judges). We show the                     ’s not much sentence variety and creative flair, it
complete results in Table 8.                                          doesn’t appear AI-generated because it keeps its
                                                                      information concise. So, it’s human-written. ”,
                                                                  ”confidence”: 4,
Self-preference bias. With the recent body of                     ”guess”: ”Human-Generated”
                                                               },
research showing that LLMs tend to prefer pol-                 ”annotator_5”: {
ished, “AI-sounding” text in mind (Laurito et al.,                ”comment”: ”Extensive use of personal pronouns.
                                                                      Quotations provide detail. Distinct variation in
2025; Koo et al., 2024; Bitton et al., 2023; Liu                      sentence and paragraph length. Highlighted sentence,
                                                                      for e.g., is 40 words. Rare in machine-generated text
et al., 2024), we thought it potentially biased to put                 territory. Use of idiom in introductory sentence.”,
                                                                  ”confidence”: 5,
human-style comments and AI-generated text in                     ”guess”: ”Human-Generated”
the same evaluation, since the LLM judge might                 }

be more likely to prefer the latter only based on
the surface-level style rather than the content or               After rewriting the original human annotations
accuracy of the information presented. Therefore,             into a more standardized format, we run the win-
we re-wrote all the human comments with the same              rate evaluation with the following input (note that
model used for TELL, so that their content would              A3 is generated by TELL):
remain intact but their style would be more simi-
lar to TELL’s outputs (see prompt B). This way,                Evaluation example
we aimed to minimize the influence of style in the
evaluation so that win-rate is focused on the actual           [
                                                                   {
quality of the explanations themselves.

                                                         28
Table 8: Listwise win rate vs. human annotators (TELL human-detectors test, n = 200 documents with complete
5-judge panel). 95% CIs: document-level bootstrap (B = 10,000). pperm : one-sided sign-flip permutation vs. 50%;
pWilc : one-sided Wilcoxon signed-rank vs. 50%.

                        Judge                        Win rate (%)           95% CI           pperm         pWilc
                        Panel mean                        72.3           [68.3, 76.2]      < 10−4        < 10−4
                        GPT-5.4-mini                      78.3           [73.9, 82.4]      < 10−4        < 10−4
                        Gemma 4 26B                       67.5           [62.6, 72.1]      < 10−4        < 10−4
                        DeepSeek V4 Flash                 75.3           [70.8, 79.5]      < 10−4        < 10−4
                        Nemotron Super                    66.3           [61.5, 70.8]      < 10−4        < 10−4
                        GPT-OSS 120B                      74.1           [69.5, 78.4]      < 10−4        < 10−4


          ”item_id”: ”A1”,                                                 After evaluation, these are the results obtained
          ”text”: ”The quotations feel strikingly natural. Some
            blend seamlessly, while others rely on additional            (TELL ranks first, followed by A6, since it is more
            context to click, and the references are all over the        specific and detailed):
             map. The instructors ’arent called doctors, even
            though ’theyre likely qualified. Moreover, ’theres
            nothing in the passage that hints at AI authorship.”          Reasoning
     },
     {
          ”item_id”: ”A2”,                                                ”ranking”: [
          ”text”: ”Here’s why I see it as human-made: it avoids              {
            the phrasing “researchers ’dont agree on”, which an                 ”item_id”: ”A3”,
            AI would likely condense to “researchers disagree on                ”rank”: 1,
            ”. It also drops the expected punctuation.”                         ”quality_score”: 0.86,
     },                                                                         ”original_item_id”: ”M1”,
     {                                                                          ”true_kind”: ”model”,
          ”item_id”: ”A3”,                                                      ”source_id”: ”model_rollout_1”
          ”text”: ”I think this is human-written. The piece is               },
            very smooth and conversational, but it has a real                {
            magazine rhythm. I see a lot of human choices in the                ”item_id”: ”A6”,
            phrasing, like the casual opener, the little aside                  ”rank”: 2,
            about recording devices, and the idiom “leg ”up. The                ”quality_score”: 0.74,
            quotes are woven into the story in different ways,                  ”original_item_id”: ”H4”,
            sometimes with “”says and sometimes with “”adds.                    ”true_kind”: ”human”,
            There are a few repeated phrases, like the whole                    ”source_id”: ”annotator_4”
            gesture-vocalization sentence, which feel like a                 },
            human drafting or editing slip. The sentence                     {
            structure is varied, with long explanatory clauses                  ”item_id”: ”A2”,
            and short punchy lines, and the writer uses small                   ”rank”: 3,
            asides and dashes to control the pace.”                             ”quality_score”: 0.41,
     },                                                                         ”original_item_id”: ”H3”,
     {                                                                          ”true_kind”: ”human”,
          ”item_id”: ”A4”,                                                      ”source_id”: ”annotator_3”
          ”text”: ”It lacks the typical repetitive phrasing you              },
            often see from AI, and it actually employs a broader             {
            vocabulary than what AI usually produces.”                          ”item_id”: ”A5”,
     },                                                                         ”rank”: 4,
     {                                                                          ”quality_score”: 0.28,
          ”item_id”: ”A5”,                                                      ”original_item_id”: ”H5”,
          ”text”: ”The text leans heavily on personal pronouns                  ”true_kind”: ”human”,
            and peppers in quotations for detail. It shows a                    ”source_id”: ”annotator_5”
            clear mix of sentence and paragraph lengths, even                },
            featuring a highlighted line that stretches to about             {
            forty words—something you ’dont often see in AI-                    ”item_id”: ”A4”,
            produced prose. Plus, it kicks off with an idiom,                   ”rank”: 5,
            adding a human-like touch.”                                         ”quality_score”: 0.16,
     },                                                                         ”original_item_id”: ”H2”,
     {                                                                          ”true_kind”: ”human”,
          ”item_id”: ”A6”,                                                      ”source_id”: ”annotator_2”
          ”text”: ”The prose is straightforward yet manages to               },
            get the point across. It leans on dashes, colons, and            {
             commas to weave in quotes, using plain, clear                      ”item_id”: ”A1”,
            phrasing like “a leg up compared to all other                       ”rank”: 6,
            ”species and “Pagel, on the other hand, is less sure                ”quality_score”: 0.08,
            about hand ”gestures to explain the ideas in an                     ”original_item_id”: ”H1”,
            accessible way. It even slips in distinctive wording                ”true_kind”: ”human”,
            such as “a small repertoire of sounds and signals                   ”source_id”: ”annotator_1”
            with various ”meanings to enrich the text. Although              }
            the sentence structure ’isnt especially varied or             ],
            flamboyant, the concise delivery suggests it ’isnt AI         ”short_rationale”: ”A3 is strongest because it cites
            -generated. In short, it reads as human-written.”                     several concrete, document-specific features: the
     }                                                                            casual opener, the repeated gesture/vocalization
 ]                                                                                sentence, the varied quote attributions, and the
                                                                                  pacing created by dashes and short/long sentences. A6




                                                                    29
 is also grounded in actual wording from the passage,
 but it mostly praises clarity and style rather than
identifying a decisive inconsistency or error. A2 is
weaker because it hinges on a speculative AI-vs-human
 paraphrase and a vague punctuation claim. A5 and A4
rely on generic detector folklore about pronouns,
sentence length, vocabulary, and repetition, with
little falsifiable evidence. A1 is least convincing
because it is largely disconnected from the document
and makes unsupported claims about instructors/
doctors that do not appear in the passage.”




                                                        30

```

## Extraction verification

- **Beginning checked:** PDF page 1 was rendered and compared with the title, authors, abstract, and opening section in the extracted text.
- **Middle checked:** PDF page 15 was rendered and compared with Appendix A qualitative examples, including the hallucination and fabricated-statute examples.
- **End checked:** PDF page 30 was rendered and compared with the final win-rate evaluation rationale and page ending in the extracted text.
- **Structure checked:** `pdfinfo` reported 30 pages; section order, Tables 1 through 8, Figures 1 through 4, Limitations, Ethical considerations, References, and Appendices A through F were checked in the PDF and extraction. `pdfimages -list` confirmed embedded raster assets on page 2.
- **Known omissions:** No textual pages, tables, captions, notes, appendices, or references omitted. Raster figure content is not represented pixel-for-pixel in the text extraction and remains preserved in the attached PDF.

## Preserved attachments

| Path | Role in the source | SHA-256 | Preservation / extraction notes |
|---|---|---|---|
| `snapshots/attachments/creo-ranganath-tell-explainable-detection-arxiv-2605.27921v1.pdf` | Authoritative arXiv v1 paper, including figures, tables, appendices, and references | `3b7a16c01f81510af0c96ac0f4fcec59ca97ae39ce544fa008b2cf7f161916a3` | Downloaded directly from arXiv; all 30 pages extracted with `pdftotext -layout`; pages 1, 15, and 30 rendered and visually checked |
