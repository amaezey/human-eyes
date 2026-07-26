# Synergizing Stylometrics with Semantics: Dual-Path Framework for LLM Detection and Attribution

- **Canonical URL:** https://aclanthology.org/2026.findings-acl.1855/
- **Alternate access URLs:**
  - https://aclanthology.org/2026.findings-acl.1855.pdf
  - https://aclanthology.org/attachments/2026.findings-acl.1855.checklist.pdf
  - https://doi.org/10.18653/v1/2026.findings-acl.1855
- **Author / owner:** Xingyu Lu, Yumeng Ma, Xiang Zhou, Shengli Gan, Guiying Deng, Yang Wen, and Yanbing Liu
- **Publisher:** Association for Computational Linguistics
- **Published:** 2026-07; proceedings dates July 2-7, 2026
- **Retrieved:** 2026-07-15
- **Stable identifier:** DOI 10.18653/v1/2026.findings-acl.1855; ACL Anthology ID 2026.findings-acl.1855
- **Version / revision:** Findings of ACL 2026 proceedings version; ACL Anthology landing page commit 717fd3cc0c5b0c9b4c55108aae362c2f8dc47bd0
- **Extraction method:** Official ACL paper PDF and Responsible NLP Checklist PDF downloaded directly; Poppler `pdftotext -layout` extraction; page count checked with `pdfinfo`; paper pages 1, 8, and 14 plus both checklist pages rendered with `pdftoppm` and inspected against the extraction.
- **Full-text status:** complete
- **Access and transformation notes:** All 14 paper pages and both checklist pages were extracted. Line wrapping, columns, tables, formulas, and figure labels reflect the PDFs' embedded text layer and Poppler layout conversion. Rendered checks confirmed the title and opening text, main result tables and analysis, final ablation table and case-study ending, and both checklist pages. No source page was omitted.

## Full text

### Official ACL paper PDF

```text
Synergizing Stylometrics with Semantics: Dual-Path Framework for LLM
                       Detection and Attribution
            Xingyu Lu1            Yumeng Ma1 Xiang Zhou1 Shengli Gan1                           Guiying Deng1
                                         Yang Wen1 Yanbing Liu1,2 *
                                  1
                           Chongqing Key Laboratory of Image Cognition,
         School of Artificial Intelligence and School of Computer Science and Technology,
        Chongqing University of Posts and Telecommunications, Chongqing 400065, China
    2
      School of Medical Information, Chongqing Medical University, Chongqing 400016, China
                               Correspondence: liuyb@cqupt.edu.cn
                           Abstract                               produced by a human—has emerged as a critical
                                                                  research challenge (Li et al., 2023a; Abburi et al.,
         The widespread application of Large Language             2025; Kumarage et al., 2024).
         Models (LLMs) has made Machine-Generated
                                                                     Existing attribution methods largely rely on sta-
         Text (MGT) detection increasingly important in
         cyberspace security and governance. The exist-
                                                                  tistical likelihood signals (e.g., perplexity scores,
         ing detection paradigms mainly focus on statis-          curvature) (Mitchell et al., 2023; Tang et al., 2023)
         tical likelihood or deep embeddings. However,            or supervised semantic embeddings derived from
         in complex applications such as short texts,             fine-tuned classifiers. While effective in controlled
         derivative works, and cross-domain content,              settings, statistical signals exhibit inherent insta-
         the discriminative capabilities fragility of these       bility in complex scenarios such as short-text or
         conventional methods increases significantly             cross-domain transfers, while semantic models of-
         with the development of LLMs. Conversely,
                                                                  ten suffer from heavy data dependency and opaque
         our research reveals that LLMs exhibit inherent
         style inertia. To address these limitations, this        decision-making. Consequently, relying solely
         study attempts to synergize stylometrics and             on these cues is insufficient to distinguish model-
         semantics for identifying MGT. This approach             specific generative characteristics. This limitation
         draws from the forensic perspective of experts           stems partly from the underutilization of stylistic
         who detect human imitation by focusing on                nuances. Recent studies suggest that, analogous to
         stylistic nuances. Based on the above inspira-           human writers, LLMs demonstrate stable model-
         tion, we propose Stylometric-Semantic LLM
                                                                  specific “style inertia” independent of topic (Bitton
         Attribution (SSLA), a framework that extracts
         model-specific stylistic fingerprints across lexi-
                                                                  et al., 2025). However, such deep, multi-layered
         cal, syntactic, and structural dimensions. SSLA          stylistic structures remain insufficiently leveraged
         employs a dual-path attention fusion architec-           in current attribution paradigms, which typically
         ture to dynamically integrate explicit stylistic         treat style merely as an auxiliary or shallow feature
         signals with implicit semantic encodings. Ex-            (Kumarage and Liu, 2023a; Posadas-Durán et al.,
         tensive experiments across six LLM families              2025; Wu et al., 2025a).
         demonstrate that our method achieves state-of-              The core intuition behind our study is illus-
         the-art performance. Notably, SSLA achieves
                                                                  trated in Figure 1. When distinguishing an original
         a Macro-F1 score of 95.6% on the challenging
         Wikipedia dataset, demonstrating exceptional             author (e.g., Ernest Hemingway) from a skilled
         robustness and surpassing state-of-the-art base-         mimic—whether a human fan or an LLM—relying
         lines like OTBDetector.                                  solely on surface content is often insufficient. In-
                                                                  stead, a robust attribution process should parallel
1        Introduction                                             a human expert’s multilevel text analysis, evaluat-
                                                                  ing text across lexical patterns, syntactic structures,
Large language models (LLMs) have rapidly be-
                                                                  and semantic intentions. Combining traditional sty-
come the dominant paradigm in text generation,
                                                                  lometrics with deep learning-based semantic mod-
powering applications from summarization and
                                                                  els has been established as a highly effective and
rewriting to conversational assistance (He et al.,
                                                                  mature paradigm in literary authorship attribution
2023). As machine-generated text (MGT) becomes
                                                                  (korić et al., 2022), inspiring our extension of this
pervasive, the ability to attribute a piece of text to
                                                                  approach to machine-generated text detection. To
its generating model—or determine whether it was
                                                                  investigate whether LLMs indeed leave behind de-
     *    Corresponding author.                                   tectable traces across these layers, we conducted
                                                              37252
                     Findings of the Association for Computational Linguistics: ACL 2026, pages 37252–37265
                                  July 2-7, 2026 ©2026 Association for Computational Linguistics


--- PAGE BREAK ---

an exploratory analysis comparing human-written                 on the challenging Wikipedia dataset, show-
sentences and their counterparts generated by mul-              ing exceptional robustness in cross-domain
tiple LLM families under identical writing prompts.             and short-text scenarios while providing inter-
The results reveal consistent and model-dependent               pretable feature-level evidence.
deviations that emerge even when semantic con-
tent is preserved. These deviations form structured
                                                          2     Related Work
clusters across three core stylistic dimensions: (1)
lexical style, characterized by model-specific vo-        Fine-grained attribution of machine-generated text
cabulary preferences and function-word distribu-          (MGT) has become a critical factor limiting the
tions; (2) syntactic structure, revealing latent habits   effectiveness of cyberspace governance and foren-
in dependency organization; and (3) semantic inten-       sic analysis (Wu et al., 2025a). To address this
tion, manifesting as subtle variations in abstraction     challenge, existing research attempts to distinguish
and framing. By synthesizing these layers, we can         text sources by exploiting various discriminative
construct a robust "style fingerprint" that transcends    signals ranging from surface statistics to deep rep-
simple semantic cues.                                     resentations. Methodologically, related studies can
   This observation led to the key intuition of our       be broadly categorized into three paradigms: (1)
work: LLMs leave persistent multi-level “style fin-       profiling probabilistic biases, (2) analyzing explicit
gerprints” that remain stable under content con-          linguistic fingerprints, and (3) learning implicit se-
straint and are thus indicative of their model prove-     mantic representations. While advancements in
nance (Wu et al., 2025b; Yu et al., 2024).                these areas have established strong baselines, they
   Based on this insight, we propose Stylometric-         often treat stylistic form and semantic content in
Semantic LLM Attribution (SSLA), a framework              isolation, failing to capture the cognitive signature
that reformulates attribution as recognizing a            of the generator as a unified whole.
model’s stylistic signature. SSLA operational-               Probabilistic and linguistic methods operate on
izes the three stylistic dimensions using a com-          the surface level, relying on unstable statistical cues
bination of contrastive stylistic analysis, multi-        or coarse handcrafted features that lack deep struc-
granularity similarity metrics, and interpretable         tural anchoring (Kumarage and Liu, 2023b); con-
syntax-semantic n-grams (SN-Grams) (Posadas-              versely, semantic methods leverage deep neural
Durán et al., 2025). To integrate these explicit          networks to learn decision boundaries but often
stylistic features with contextual embeddings from        function as opaque “black boxes”. Our proposed
RoBERTa (Liu et al., 2019), we design a dual-path         SSLA framework integrates the strengths of these
fusion architecture that effectively synthesizes ex-      paradigms, bridging the gap between interpretabil-
plicit stylistic signals with implicit semantic repre-    ity and performance. By dynamically fusing ex-
sentations.                                               plicit multi-level stylistic fingerprints with implicit
   Our contributions are threefold:                       deep semantic encodings, SSLA constructs a robust
                                                          “cognitive profile” for each model. This approach
   • We propose SSLA, a modular attribution               fundamentally enhances attribution reliability in
     framework that synergizes explicit multi-level       short-text and cross-domain scenarios, rather than
     stylistic signals (lexical, syntactic, and struc-    relying solely on brittle likelihoods or unexplain-
     tural) with implicit semantic representations        able embeddings.
     via a dual-path fusion architecture to achieve
     robust fine-grained attribution.                     2.1    Zero-Shot Probabilistic Signals

   • We discover and formalize multi-level stylistic      This paradigm posits that an LLM leaves a unique
     fingerprints of LLMs, grounded in empirical          probabilistic signature on its generated text. The
     observations derived from controlled prompt-         core assumption is that a text sequence will yield
     based generation.                                    the lowest perplexity or highest curvature when
                                                          evaluated by its source model compared to oth-
   • We perform comprehensive experiments                 ers (Wu et al., 2025a). Pioneering techniques like
     across six LLM families. Results demon-              DetectGPT (Mitchell et al., 2023) utilize the curva-
     strate that stylistic profiling significantly out-   ture of the log probability function to distinguish
     performs state-of-the-art baselines. Notably,        source models based on their specific likelihood
     SSLA achieves a Macro-F1 score of 95.6%              landscapes. Similarly, methods leveraging log-rank
                                                     37253


--- PAGE BREAK ---

Figure 1: The core intuition of SSLA: Cognitive Attribution. Just as humans distinguish an original author (e.g.,
Hemingway) from mimics via multi-dimensional stylometric cues, our framework identifies LLMs based on (A)
Lexical Style, (B) Syntactic Structure, and (C) Semantic Intention. These stylistic fingerprints remain distinguishable
even when the semantic content is similar.


signals (Su et al., 2023) and Uniform Information            verse dependency trees to reveal non-linear struc-
Density (UID) (Venkatraman et al., 2023) identify            tural habits specific to certain architectures. Nev-
the source by analyzing whether the token selection          ertheless, despite their interpretability, these tradi-
aligns with a specific model’s vocabulary ranking            tional features often prove too coarse to distinguish
preferences. However, these likelihood-based sig-            between sophisticated modern LLMs that mimic
nals face critical applicability barriers. First, they       human nuances closely. Furthermore, most prior
require white-box access to calculate probabilities          works treat these features in isolation, failing to
for every candidate model, which is impossible for           capture how stylistic habits interact with seman-
proprietary API-based models (Bao et al., 2023).             tic contexts for fine-grained attribution (Kumarage
Second, in short-text scenarios, the statistical dif-        et al., 2024).
ferences between models become indistinguishable
due to high variance (Li et al., 2023b), limiting            2.3   Deep Semantic Representations
their effectiveness for fine-grained sourcing.
                                                             In parallel with statistical and stylometric ap-
                                                             proaches, the dominant paradigm treats attribu-
2.2 Explicit Linguistic Fingerprints
                                                             tion as a multi-class supervised classification task.
The search for content-invariant signals leads to            These methods leverage the deep semantic under-
Stylometry, which utilizes stable linguistic pat-            standing of Pre-trained Language Models (PLMs),
terns to profile generators. This approach assumes           such as RoBERTa or BERT, to learn discrimina-
that different models exhibit distinct "style iner-          tive decision boundaries between different source
tia"—unique habits in lexical choice or syntactic            models (Liu et al., 2019; He et al., 2023). By
structuring that persist across topics (Bitton et al.,       fine-tuning on labeled datasets, these classifiers
2025). Early efforts relied on macro-level statistics,       can capture subtle semantic deviations specific to
such as POS tag distributions and lexical diversity,         each generator. To improve robustness against do-
to differentiate model families (Li et al., 2023a). To       main shifts, recent state-of-the-art methods like
capture deeper signatures, recent research has em-           ConDA(Bhattacharjee et al., 2023) and OTB-
ployed Syntactic N-Grams (SN-Grams) (Sidorov                 D(La Cava and Tagarelli, 2025) have incorporated
et al., 2014; Posadas-Durán et al., 2025), which tra-        contrastive adaptation and optimal transport geom-
                                                        37254


--- PAGE BREAK ---

etry to align feature spaces across different distri-   3.2   Multi-Dimensional Stylometric Profiling
butions (He et al., 2023). However, these semantic      We construct a multi-dimensional feature vector
classifiers suffer from critical flaws regarding data   designed to capture the “cognitive signature” of
inefficiency—requiring massive labeled data for         the generator. We categorize these features into
each new model to prevent overfitting—despite           static linguistic complexity, dynamic stylistic rigid-
achieving high accuracy. Furthermore, they func-        ity, and structural preferences.
tion largely as “black boxes” and lack the inter-       Static Complexity: Linguistic Metrics (sling ).
pretability required to explain why a text is at-       LLMs, constrained by their training objectives,
tributed to a specific model, highlighting the need     specifically Reinforcement Learning from Human
for a framework that synergizes interpretability        Feedback (RLHF), often exhibit specific statisti-
with performance.                                       cal biases. We extract a 6-dimensional vector to
                                                        quantify the information density and syntactic elab-
3   Methodology                                         oration:
                                                           • Syntactic Structure: We compute Average De-
In this section, we introduce SSLA, a framework
                                                             pendency Depth and Average Dependency
designed to attribute texts to their source LLMs by
                                                             Distance using dependency parsing. These
profiling stable stylistic fingerprints. We outline
                                                             metrics reveal whether a model prefers simple,
the problem formulation and our core motivation
                                                             flat structures or complex, nested recursions.
in Section 3.1. We then elaborate on the rationale
and construction of our multi-dimensional stylistic        • Lexical & Part-of-Speech Distribution: We
features in Section 3.2, and finally describe the            calculate Lexical Diversity, measured by Type-
dual-path interaction architecture in Section 3.3.           Token Ratio (TTR), and Sentence Length to
                                                             measure vocabulary richness. Additionally,
3.1 Problem Definition and Motivation                        we explicitly monitor part-of-speech prefer-
                                                             ences via Noun Ratio and Verb Ratio, captur-
Problem Formulation. We define fine-grained                  ing the generator’s tendency towards descrip-
LLM attribution as a multi-class classification              tive (noun-heavy) or action-oriented (verb-
task. Given a query text x, the goal is to pre-              heavy) phrasing.
dict the source generator y ∈ Y = {y1 , ..., yN }
(e.g.,Claude, GPT-turbo, Human). Formally, let          Dynamic Rigidity: Differential Analysis via
                                                        Rewriting (spres ). Static features may fail when
                i=1 be the dataset. We aim to learn
D = {(xi , yi )}M
a mapping Fθ : X → [0, 1]N that minimizes the           models mimic human styles. To address this, we in-
prediction error.                                       troduce a novel Differential Stylistic Analysis. The
Motivation: The Stylistic Stability Hypothesis.         core idea is to employ a general Large Language
Existing detectors often rely on brittle signals: se-   Model as a rewriting probe to stress-test the input
mantic keywords (which change with topics) or to-       x by generating a semantic-preserving rewrite x′ .
ken probabilities (which are inaccessible for black-    We measure the “stylistic drift” between x and x′
box APIs).      Our approach is grounded in the         using a 6-dimensional vector covering semantic,
Stylistic Stability Hypothesis. Recent literature       embedding, and surface levels:
has demonstrated that LLMs possess distinct and               spres = [Msem ; Memb ; Msurf ] ∈ R6         (1)
consistent stylistic fingerprints that persist even
when they are prompted to write in different writ-      where [; ] denotes the concatenation operator.
ing styles (Bitton et al., 2025). While the gener-      Specifically, each of the three components is for-
ated content varies significantly across topics, its    mulated as a 2-dimensional sub-vector:
stylistic signature—manifested in syntactic com-           • Msem ∈ R2 (Semantic Consistency): We
plexity, lexical preferences, and structural rigid-          use BLEURT and BERTScore to capture deep
ity—remains consistent across domains. SSLA                  semantic preservation;
mimics a forensic linguistic approach: (1) extract-        • Memb ∈ R2 (Latent Alignment): We com-
ing invariant stylistic fingerprints (s, g) that per-        pute the Cosine Similarity of Sentence-BERT
sist despite topic shifts; and (2) interacting these         (SBERT) and RoBERTa embeddings, measur-
signals with semantic context via a self-attention           ing the shift in high-dimensional contextual
fusion mechanism to achieve robust attribution.              space;
                                                   37255


--- PAGE BREAK ---

  Multi-Level Style Signal Construction                                               Dual-Path Fusion-Based Detection

                                                                                                                  Fusion Layer
                                                                                         Lstyle Lsem                       Lstyle Lsem
                         HWT and MGT                                                                       Modality
     Dynamic Rigidity Analysis    Static Linguistic Signals                                              Self-Attention

                                                Lexical Style
                                            ·
                                                                           Slex

                                            ·                                          2 ×C                               2 ×C
       Rewriter                                 Lexical diversity


                                            ·
                                                Noun ratio
                                                Verb ratio
                                                                                                         Attention Map                         Mean
                                                                                               M                                              Pooling
                                                                                                                                    M'
                   Rewritten text                                          Ssyn
                                                                                          (Interaction Matrix)
                                                Syntactic Style
                                            ·
                                  Spres
     Multi-level Similarity
    ·
    ·
      Semantic
                                            ·
                                            ·
                                                Avg dep
                                                distance
                                                                                       Lstyle          Lsem

    ·
      Embedding
                                                Avg dep depth              Sling
      Surface
                                                Sentence length                                                           H_CLS          T1      ···    Tn     S


                          Spres         Sling                                                                                             Encoder
                                                                                                                           E|CLS|        E1      ···    En    E|SEP|


                                  R12                                                                                       [CLS]         T1     ···    Tn   [SEP]



   SN-Gram Structural Pattern Extraction
                                                                                           fstyle =[SPres；SLing；g]
                                                               SN-Grams (g)
                        SN-Gram
                        Extractor
                                                                                                                                         HWT and MGT
   HWT and MGT                                                      R128




Figure 2: The overall architecture of SSLA. The framework constructs multi-level stylometric signals (Left) and
synergizes them with RoBERTa embeddings via a dual-path attention fusion (Right) for robust attribution.

   • Msurf ∈ R2 (Surface Similarity): We utilize                                   Dual-Encoder Architecture. The framework con-
     CHRF++ and Surface Cosine Similarity to                                       sists of two parallel encoders: (1) Style Path: A
     quantify character-level and lexical retention.                               Multi-Layer Perceptron (MLP) projects the hand-
Rationale: This differential vector acts as a mea-                                 crafted feature vector fstyle to logits Lstyle ∈ RC .
sure of Stylistic Rigidity. If x is human-written,                                 (2) Semantic Path: A pre-trained RoBERTa en-
the standardized rewriting process induces a signif-                               coder projects the text embedding to logits Lsem ∈
icant drift (low similarity scores); if x is generated                             RC , where C is the number of LLM classes.
by an aligned LLM, the style remains rigid (high                                   Self-Attention Fusion. We stack the projected
similarity), serving as a powerful discriminative                                  logits to form H = [Lstyle ; Lsem ] ∈ R2×C and ap-
signal.                                                                            ply Multi-Head Self-Attention (MHSA) to capture
Structural Preferences: SN-Grams (g). To cap-                                      non-linear interactions. We simplify the attention
ture long-range dependencies, we employ Syntax-                                    operation as:
                                                                                                                       
Semantic N-Grams. We extract dependency                                                                          QK T
triples defined as (Relation, Head, Dependent)                                                  H̃ = softmax √            V          (2)
                                                                                                                    dk
and vectorize these patterns using TF-IDF weight-
ing with variance-based selection, resulting in a                                  where Q, K, V are obtained by projecting H with
dense vector g ∈ R128 .                                                            learnable matrices WQ , WK , WV ∈ RC×dmodel ,
   The final stylistic input is the concatenation:                                 and dk is the scaling factor derived from the head
fstyle = [sling ; spres ; g] ∈ R140 .                                              dimension. This layer weighs the confidence of
                                                                                   structural vs. semantic cues. The final prediction ŷ
3.3 Dual-Path Interaction and Optimization                                         is obtained via mean pooling and a linear projection
We propose a Dual-Path architecture that fuses the                                 parameterized by Wo ∈ RC×C and bo ∈ RC :
interpretability of stylistic profiles with the seman-
                                                                                                       ŷ = Wo · Mean(H̃) + bo                                         (3)
tic power of PLMs, utilizing an attention-based
mechanism to dynamically synthesize explicit and                                   Optimization. We employ a joint optimization
implicit signals.                                                                  strategy. To ensure both paths learn discrimina-
                                                                           37256


--- PAGE BREAK ---

tive features independently while synergizing ef-          Pages (WP). Each dataset comprises human-
fectively, the total loss Ltotal is computed as a          written texts and machine-generated texts from 6
weighted combination of the fused output loss and          different LLMs (e.g., ChatGPT, Claude, LLaMA),
the auxiliary losses from both paths:                      forming a challenging 7-way attribution task (and
                                                           binary detection task). These datasets cover diverse
          Ltotal =λf L(ŷ, y) + λs L(ŷs , y)              domains, ensuring a comprehensive evaluation of
                                                    (4)
                    + λm L(ŷm , y)                        stylistic generalizability.
                                                           Baseline Methods. To validate the performance
where y is the ground-truth label, ŷ is the final fused   of SSLA, we compare it against a comprehen-
prediction, and ŷs and ŷm denote the independent         sive set of baselines. These include zero-shot
predictions derived from the Style Path (Lstyle )          statistical methods such as DetectGPT(Mitchell
and Semantic Path (Lsem ), respectively. Following         et al., 2023) and Entropy(Gehrmann et al., 2019);
empirical tuning, we set the hyperparameters to            semantic-based classifiers like RoBERTa-based de-
λf = 0.4, λs = 0.3, and λm = 0.3.                          tectors(Liu et al., 2019; Solaiman et al., 2019) and
                                                           LM-D(He et al., 2023); and specialized attribution
4    Experiments
                                                           models such as ConDA(Bhattacharjee et al., 2023)
In this section, we first introduce the experimental       and OTB-D(La Cava and Tagarelli, 2025).
setup, including datasets, baselines, and implemen-        Implementation Details. For the semantic en-
tation details in Section 4.1. We then present the         coder, we utilize the pre-trained RoBERTa-base
main experimental results on both binary detection         model. We freeze the embedding layers and fine-
and fine-grained attribution in Section 4.2. Subse-        tune the remaining parameters to prevent overfit-
quently, we conduct a deep-dive analysis into the          ting in low-resource settings. The style encoder uti-
robustness, efficiency, and generalization capabili-       lizes a multi-layer perceptron (MLP) to process the
ties of our framework in Section 4.3, followed by          constructed stylistic vectors (s and g). To extract
ablation studies in Section 4.4.                           the differential stylistic features (spres ), we em-
   This section is organized around the following          ploy DeepSeek-V3 as the default rewriting probe
research questions:                                        to generate semantic-preserving texts. The struc-
                                                           tural stylistic features are extracted through deep
    • RQ1 (General Effectiveness): Can the pro-            dependency parsing implemented via the Stanza
      posed SSLA framework, by synergizing ex-             parser. For model training, we employ the AdamW
      plicit stylistic fingerprints with implicit seman-   optimizer with a learning rate of 2e-5 and a linear
      tic embeddings, achieve state-of-the-art per-        warmup scheduler to ensure stable convergence.
      formance in both binary detection and fine-
      grained LLM attribution tasks?                       4.2   Main Results

    • RQ2 (Robustness & Stability): Does SSLA              We evaluate the performance of SSLA with a pri-
      demonstrate superior robustness compared             mary focus on the challenging fine-grained 7-way
      to semantic-heavy baselines under resource-          LLM attribution task, where distinguishing be-
      constrained and distributional-shift scenarios,      tween sophisticated models requires capturing sub-
      specifically including short text lengths, data      tle stylistic nuances.
      scarcity, and cross-domain transfers?                Qualitative Analysis. As visualized in Figure 5 in
                                                           the Appendix, the t-SNE plot (a) demonstrates that
    • RQ3 (Mechanism & Interpretability): How              SSLA learns highly discriminative stylistic repre-
      much does each stylistic component con-              sentations. Unlike semantic embeddings that may
      tribute to the final decision, and does the dual-    overlap due to similar topics, our stylistic features
      path architecture provide transparent, inter-        drive the formation of clear, compact clusters for
      pretable evidence that addresses the “black          each specific LLM family. The confusion matrix
      box” limitation of traditional detectors?            (b) further corroborates this robustness. It shows
                                                           that SSLA effectively minimizes off-diagonal er-
4.1 Experimental Setup                                     rors, successfully distinguishing even closely re-
Datasets. We employ three representative datasets          lated models (which typically share similar training
from MGTBench(He et al., 2023) to evaluate our             data) with high confidence.
proposed method: Essay, Reuters, and Wikipedia             Attribution Performance. The quantitative re-
                                                      37257


--- PAGE BREAK ---

sults in Table 1 reveal distinct performance patterns.                     1.000



First, traditional zero-shot statistical methods (e.g.,
DetectGPT, Entropy) fail completely on this fine-                          0.900



grained task, yielding Macro-F1 scores below 0.40.
                                                                           0.800




                                                          Macro-F1 Score
This confirms that simple likelihood signals are
insufficient for distinguishing sophisticated LLMs.                        0.700

   Comparison with supervised baselines highlights
the superiority of our approach. While semantic-                           0.600


heavy methods like OTBDetector(OTB-D) per-                                                                                                  SSLA
                                                                                                                                            OTB-D
form competitively on the Essay dataset (where                             0.500                                                            LM-D
                                                                                                                                            ConDA

semantic variance is high), they exhibit notable                                                                                            OpenAI

                                                                                   839   2,099           4,198                      6,297    8,397
performance degradation on domains character-                                                    Dataset Size (Number of Samples)


ized by high semantic homogeneity. In contrast,
                                                          Figure 3: Data Efficiency Analysis. SSLA consistently
SSLA demonstrates exceptional robustness. Specif-
                                                          outperforms all baseline methods across varying train-
ically, on the Reuters dataset, SSLA achieves             ing set sizes, demonstrating robust capabilities particu-
an F1 of 0.966, surpassing OTB-D (0.945) by               larly in few-shot settings.
2.1%. Even more notably, on the Wikipedia (WP)
dataset—characterized by neutral tone and factual
constraints—SSLA establishes a clear lead of 1.7%         against OTB-D in this challenging low-density set-
(0.956 vs 0.939). This performance gap offers a           ting. Even compared to the semantic-heavy LM-D,
critical insight: when semantic boundaries become         SSLA offers a better balance between Precision
blurred due to factual standardization, the stylistic     and Recall, and scales effectively as text length
fingerprints profiled by SSLA—such as syntactic           increases.
rigidity and functional word usage—become the             Data Efficiency. We further explore the data effi-
decisive discriminative signals.                          ciency of SSLA by training on subsets of varying
   Additionally, we verify SSLA’s effectiveness on        sizes (from 839 to 8397 samples). As shown in
the fundamental binary detection task (Human vs.          Figure 3, SSLA exhibits superior few-shot learning
Machine). Detailed results provided in the Ap-            capabilities. With only 839 samples, our method
pendix show that SSLA achieves state-of-the-art           achieves an accuracy of ∼90%, significantly out-
performance on the Reuters dataset while main-            performing strong baselines like ConDA and LM-D
taining highly competitive capabilities across other      by margins of roughly 19% and 13% respectively.
diverse domains. This confirms that explicitly mod-       This finding supports our hypothesis that stylistic
eling fine-grained stylistic signals effectively cap-     features are more informative and data-efficient
tures general machine-generated artifacts without         than purely semantic embeddings, allowing the
compromising detection stability.                         model to capture distinguishing patterns with sig-
                                                          nificantly fewer examples.
4.3 Robustness and Efficiency Analysis                    Cross-Domain Generalization. Finally, we eval-
Beyond standard benchmarks, we investigate the            uate the model’s generalization capability under
robustness of our method under challenging con-           severe distribution shifts by training on the Reuters
ditions, specifically focusing on short text lengths,     dataset and testing on the Essay dataset. This set-
data scarcity, and cross-domain generalization.           ting is particularly challenging as it requires the
Sensitivity to Text Length. Standard attribution          model to ignore domain-specific semantics and fo-
methods often degrade on short texts due to insuf-        cus on intrinsic generative signatures.
ficient statistical signals. To evaluate robustness,         As illustrated in Figure 4, most baselines strug-
we test performance across four length intervals          gle with this shift. Purely semantic-based methods
on the Reuters dataset. As illustrated in Figure 6,       like LM-D and ConDA achieve F1 scores of only
while baselines like OTB-D suffer a catastrophic          0.4663 and 0.4543 respectively, indicating a heavy
failure in short-text scenarios—dropping to an F1         reliance on in-domain content. While the state-of-
score below 0.30 for texts under 50 tokens—SSLA           the-art baseline OTB-D shows improved robustness
exhibits exceptional resilience, maintaining an F1        with a score of 0.6719, our proposed SSLA still
score of over 0.80. Notably, SSLA creates a sig-          outperforms it.
nificant performance gap of approximately 55%                Specifically, SSLA achieves a Macro-F1 score
                                                     37258


--- PAGE BREAK ---

Table 1: Main Benchmark Results on Essay, Reuters, and WP Datasets (7-way Attribution). Macro-F1 is reported.
Best results in each column are bolded.

  Test Task Detector                 Essay                            Reuters                             WP
                       Acc      F1       Prec   Rec     Acc        F1      Prec    Rec      Acc      F1        Prec   Rec
  Likelihood           0.334   0.304    0.308   0.334   0.334    0.304     0.308   0.334   0.382    0.334   0.337     0.382
  Rank                 0.409   0.378    0.361   0.408   0.259    0.213     0.226   0.259   0.255    0.255   0.216     0.208
  Log_Rank             0.442   0.412    0.407   0.442   0.343    0.319     0.317   0.343   0.400    0.360   0.348     0.400
  Entropy              0.409   0.378    0.378   0.409   0.249    0.221     0.229   0.249   0.209    0.163   0.182     0.209
  Rank_GLTR            0.476   0.437    0.445   0.476   0.411    0.392     0.389   0.411   0.433    0.385   0.390     0.433
  DetectGPT            0.409   0.378    0.407   0.442   0.241    0.197     0.197   0.241   0.237    0.192   0.201     0.237
  NPR                  0.409   0.378    0.407   0.442   0.292    0.211     0.208   0.292   0.308    0.249   0.246     0.308
  LRR                  0.432   0.403    0.396   0.432   0.386    0.363     0.365   0.386   0.403    0.378   0.377     0.403
  OpenAI-Detector      0.808   0.802    0.836   0.808   0.893    0.890     0.901   0.893   0.725    0.723   0.781     0.725
  ConDA(23)            0.935   0.935    0.935   0.935   0.946    0.946     0.948   0.946   0.918    0.915   0.925     0.918
  LM-D(24)             0.890   0.882    0.901   0.890   0.921    0.921     0.918   0.921   0.890    0.890   0.898     0.890
  OTB-D(25)            0.948   0.949    0.952   0.949   0.946    0.945     0.948   0.946   0.940    0.939   0.941     0.940
  SSLA (Ours)          0.968   0.945    0.949   0.943   0.978    0.966     0.964   0.969   0.971    0.956   0.955     0.958


                                                                Table 2: Performance under Extreme Adversarial Per-
                                                                sona Constraints.

                                                                 Setting                   Models                Macro-F1
                                                                 Standard Attribution      6 LLMs              0.956 ± 0.011
                                                                 Extreme Adversarial       4 SOTA LLMs             0.952



                                                                4.4     Ablation Studies and Analysis
Figure 4: Cross-Domain Performance (Reuters → Es-
say). SSLA achieves the highest F1 (0.7083), surpassing         Component Analysis. To systematically evalu-
OTB-D (0.6719) and semantic baselines, validating su-           ate the contribution of each component, we con-
perior robustness against distribution shifts.
                                                                duct ablation studies as detailed in Table 5 in the
                                                                Appendix. The results confirm the necessity of
of 0.7083, surpassing OTB-D by a notable margin.                multi-view modeling: variants relying on a single
This result confirms that our dual-path architec-               source of evidence consistently underperform the
ture effectively synthesizes stylistic rigidity with            full SSLA framework across domains. In addition,
semantic context. Even without explicit domain                  to isolate the contribution of the rewrite-based rigid-
adaptation techniques, the attention-based fusion               ity feature, we include two targeted variants:“spres
mechanism allows SSLA to adaptively leverage                    only” and “SSLA w/o spres ”. The results show
stable stylistic fingerprints (such as SN-Grams and             that spres alone retains meaningful discriminative
functional word distributions) that persist across              power, while removing it from the complete sys-
genres, thereby achieving superior generalization.              tem leads to a consistent performance drop. This
Robustness Against Persona-Steering. To eval-                   indicates that spres provides complementary attri-
uate SSLA’s resilience against deliberate style-                bution evidence beyond static linguistic metrics
masking, we conducted an extreme adversarial test               and structural SN-Grams. It is worth noting that
on the XSum dataset. We prompted 4 SOTA LLMs                    while the simple concatenation variant (“RoBERTa
(GPT-4o, DeepSeek-V3, Gemini-1.5-Flash, and                     + SN_Gram”) performs competitively on the Essay
GLM-4) to rewrite articles under a strict identity              dataset, it struggles to generalize to the more di-
constraint (the full prompt template is detailed in             verse Wikipedia (WP) domain. In contrast, our pro-
Appendix A.7). As shown in Table 2, even when                   posed SSLA (Full Fusion) maintains consistently
these highly aligned models are forced into an iden-            high performance across all domains, achieving
tical stylistic persona, SSLA maintains a Macro-F1              the highest Average F1. This indicates that the
of 0.952, closely matching the unconstrained base-              attention-based fusion mechanism effectively mit-
line. This confirms that our framework captures                 igates the risk of overfitting to specific structural
intrinsic “style inertia” that is resistant to surface-         patterns.
level persona alignment.                                        Probe Independence Analysis. A critical con-
                                                        37259


--- PAGE BREAK ---

cern in our differential framework is whether the ef-    path fusion architecture that dynamically synthe-
fectiveness of spres stems from the intrinsic “style     sizes explicit stylistic features with implicit seman-
inertia” of the source model or merely from the spe-     tic embeddings, ensuring robust attribution across
cific rewriting bias of the chosen probe. To verify      diverse scenarios.
that our stylistic signal is probe-independent, we          Comprehensive experiments validate that SSLA
replaced the default rewriter (DeepSeek-V3) with         achieves state-of-the-art performance while demon-
a structurally distinct model, Gemini-1.5-Flash. As      strating exceptional robustness in challenging con-
shown in Table 4 in the Appendix, swapping the           ditions such as short texts and cross-domain trans-
probe does not materially degrade attribution per-       fers. Furthermore, the explicit modeling of stylis-
formance, with the Average F1 remaining highly           tic signatures enables effective generalization in
stable (0.954 vs. 0.956). In addition, the ablation      few-shot settings, significantly outperforming deep
results in Table 5 show that removing spres from         semantic classifiers when training data is scarce.
the full system causes a consistent performance          Feature analysis further confirms that SSLA offers
drop, while spres only still retains non-trivial at-     superior interpretability, allowing users to trace de-
tribution ability. Together, these findings suggest      cisions back to specific linguistic patterns rather
that spres captures a meaningful and complemen-          than opaque probability scores.
tary stylistic signal rather than merely reflecting
idiosyncrasies of a specific rewriter.                   Limitations
Interpretability and Qualitative Insights. We            Despite its effectiveness, SSLA has limitations.
further analyze the decision-making process using        First, the construction of multi-dimensional stylis-
SHAP values, as illustrated in Figure A.7 in the Ap-     tic profiles incurs additional computational over-
pendix. The analysis reveals that stylistic features,    head compared to end-to-end semantic models.
particularly specific SN-Gram structures and lexi-       This trade-off between inference efficiency and ro-
cal density metrics, account for a significant portion   bustness suggests that the current framework is
of the decision weight. This provides interpretable      optimally suited for offline forensic analysis, rather
supporting evidence for attribution, addressing the      than latency-sensitive real-time streaming detec-
“black box” limitation of traditional neural classi-     tion. Second, the framework relies on high-quality
fiers. To further validate these findings, we provide    linguistic parsers, which may limit its applicabil-
a qualitative case study in Appendix A.8. These          ity to low-resource languages lacking robust NLP
cases demonstrate that when the Stylistic Path en-       tools. Finally, our evaluation focuses on closed-set
counters ambiguity due to standardized narrative         attribution; the framework’s capability to detect
structures (e.g., conventional fairytale openings),      “unknown” models (open-world setting) remains to
the Semantic Path can identify latent fingerprints to    be explored in future work.
perform corrective fusion; conversely, the semantic
path may introduce noise in highly stylized human        Acknowledgments
narratives. While performance on ultra-short texts
                                                         This work was supported in part by the National
(< 50 tokens) remains a challenge, the overall re-
                                                         Natural Science Foundation of China (Grant No.
sults confirm that integrating multi-level stylistic
                                                         62272074, 62201112, and 62402077), the Science
fingerprints creates a robust and interpretable attri-
                                                         and Technology Research Program of Chongqing
bution framework.
                                                         Municipal Education Commission (Grant No.
                                                         KJQN202400607 and KJQN202400654).
5   Conclusion

In this paper, we presented SSLA, a framework that       References
synergizes stylometrics with semantics designed
to address the fragility of existing semantic-based      Harika Abburi, Sanmitra Bhattacharya, Edward Bowen,
                                                           and Nirmala Pudota. 2025. Ai-generated text
LLM attribution methods. By modeling the cog-              detection: A multifaceted approach to binary
nitive signature of generators—spanning lexical            and multiclass classification.      arXiv preprint
habits, syntactic structures, and semantic inten-          arXiv:2505.11550.
tions—SSLA extracts inherent style inertia that          Guangsheng Bao, Yanbin Zhao, Zhiyang Teng, Linyi
persists even when surface content varies. To effec-       Yang, and Yue Zhang. 2023. Fast-detectgpt: Effi-
tively integrate these signals, we introduced a dual-      cient zero-shot detection of machine-generated text
                                                    37260


--- PAGE BREAK ---

  via conditional probability curvature. arXiv preprint     Yinhan Liu, Myle Ott, Naman Goyal, Jingfei Du, Man-
  arXiv:2310.05130.                                           dar Joshi, Danqi Chen, Omer Levy, Mike Lewis,
                                                              Luke Zettlemoyer, and Veselin Stoyanov. 2019.
Amrita Bhattacharjee, Tharindu Kumarage, Raha                 Roberta: A robustly optimized bert pretraining ap-
 Moraffah, and Huan Liu. 2023. Conda: Contrastive             proach. arXiv preprint arXiv:1907.11692.
 domain adaptation for ai-generated text detection. In
 Proceedings of the 13th International Joint Confer-        Eric Mitchell, Yoonho Lee, Alexander Khazatsky,
 ence on Natural Language Processing and the 3rd              Christopher D. Manning, and Chelsea Finn. 2023.
 Conference of the Asia-Pacific Chapter of the Associ-        Detectgpt: Zero-shot machine-generated text detec-
 ation for Computational Linguistics, pages 598–610.          tion using probability curvature. In International
                                                              Conference on Machine Learning.
Yehonatan Bitton, Elad Bitton, and Shai Nisan. 2025.
  Detecting stylistic fingerprints of large language mod-   Pablo Francisco Posadas-Durán, Germán Ríos-Toledo,
  els. arXiv preprint arXiv:2503.01659.                       Erick Velázquez-Lozada, A De Jesús Osuna-Coutiño,
                                                              Madaín Pérez-Patricio, and Fernando Pech May.
Sebastian Gehrmann, Hendrik Strobelt, and Alexan-
                                                              2025. Learning the style via mixed sn-grams: An
  der M. Rush. 2019. Gltr: Statistical detection and
                                                              evaluation in authorship attribution. AI, 6(5):104.
  visualization of generated text. In Annual Meeting of
  the Association for Computational Linguistics.            Grigori Sidorov, Francisco Velasquez, Efstathios Sta-
Xinlei He, Xinyue Shen, Zeyuan Chen, Michael Backes,          matatos, Alexander Gelbukh, and Liliana Chanona-
  and Yang Zhang. 2023. Mgtbench: Benchmarking                Hernández. 2014. Syntactic n-grams as machine
  machine-generated text detection. Proceedings of the        learning features for natural language processing. Ex-
  2024 on ACM SIGSAC Conference on Computer and               pert Systems with Applications, 41:853–860.
  Communications Security.
                                                            Irene Solaiman, Miles Brundage, Jack Clark, Amanda
Mihailo korić, Ranka Stanković, Milica Ikonić Neić,        Askell, Ariel Herbert-Voss, Jeff Wu, Alec Radford,
  Joanna Byszuk, and Maciej Eder. 2022. Parallel sty-          and Jasmine Wang. 2019. Release strategies and the
  lometric document embeddings with deep learning              social impacts of language models. arXiv preprint
  based language models in literary authorship attribu-        arXiv:1908.09203.
  tion. Mathematics.
                                                            Jinyan Su, Terry Yue Zhuo, Di Wang, and Preslav Nakov.
Tharindu Kumarage, Garima Agrawal, Paras Sheth,                2023. Detectllm: Leveraging log rank information
  Raha Moraffah, Amanat Chadha, Joshua Garland,                for zero-shot detection of machine-generated text. In
  and Huan Liu. 2024. A survey of ai-generated text            Conference on Empirical Methods in Natural Lan-
  forensic systems: Detection, attribution, and charac-        guage Processing.
  terization. arXiv preprint arXiv:2403.01152.
                                                            Ruixiang Tang, Yu-Neng Chuang, and Xia Hu. 2023.
Tharindu Kumarage and Huan Liu. 2023a. Neural au-             The science of detecting llm-generated text. Commu-
  thorship attribution: Stylometric analysis on large         nications of the ACM, 67:50 – 59.
  language models. 2023 International Conference on
  Cyber-Enabled Distributed Computing and Knowl-            Saranya Venkatraman, Adaku Uchendu, and Dongwon
  edge Discovery (CyberC), pages 51–54.                       Lee. 2023. Gpt-who: An information density-based
                                                              machine-generated text detector. In NAACL-HLT.
Tharindu Kumarage and Huan Liu. 2023b. Neural au-
  thorship attribution: Stylometric analysis on large       Junchao Wu, Shu Yang, Runzhe Zhan, Yulin Yuan,
  language models. 2023 International Conference on           Lidia S. Chao, and Derek F. Wong. 2025a. A survey
  Cyber-Enabled Distributed Computing and Knowl-              on llm-generated text detection: Necessity, methods,
  edge Discovery (CyberC), pages 51–54.                       and future directions. Computational Linguistics,
                                                              51:275–338.
Lucio La Cava and Andrea Tagarelli. 2025. Openturing-
  bench: an open-model-based benchmark and frame-           Zehao Wu, Yanjie Zhao, and Haoyu Wang. 2025b.
  work for machine-generated text detection and attri-        Gradient-based model fingerprinting for llm similar-
  bution. In Proceedings of the 2025 Conference on            ity detection and family classification. arXiv preprint
  Empirical Methods in Natural Language Processing,           arXiv:2506.01631.
  pages 26666–26682.
                                                            Xiao Yu, Kejiang Chen, Qi Yang, Weiming Zhang, and
Dongfang Li, Zetian Sun, Xinshuo Hu, Zhenyu Liu,              Neng H. Yu. 2024. Text fluoroscopy: Detecting llm-
  Ziyang Chen, Baotian Hu, Aiguo Wu, and Min                  generated text through intrinsic features. In Con-
  Zhang. 2023a. A survey of large language models             ference on Empirical Methods in Natural Language
  attribution. arXiv preprint arXiv:2303.11666.               Processing.
Yafu Li, Qintong Li, Leyang Cui, Wei Bi, Zhilin Wang,
  Longyue Wang, Linyi Yang, Shuming Shi, and Yue            A    Appendix
  Zhang. 2023b. Mage: Machine-generated text detec-
  tion in the wild. In Annual Meeting of the Association    In this appendix, we provide supplementary eval-
  for Computational Linguistics.                            uations to support the main findings presented in
                                                       37261


--- PAGE BREAK ---

Section 4.2. Specifically, we present detailed quan-     Recall, and Precision on the Reuters dataset. The
titative results for the binary detection task, quali-   results indicate that SSLA maintains superior stabil-
tative visualizations of the stylistic feature space,    ity compared to baselines, particularly in the chal-
and an in-depth analysis of feature contributions.       lenging short-text regime (< 50 tokens), where
                                                         traditional methods typically suffer from insuffi-
A.1 Binary Detection Performance                         cient discriminative signals.
Table 3 presents the comprehensive performance
metrics—including Accuracy, Macro-F1, Preci-             A.5     Detailed Ablation Analysis
sion, and Recall—across the Essay, Reuters, and          To systematically evaluate the contribution of each
Wikipedia (WP) datasets.                                 component within the SSLA framework, we con-
   Consistent with our observations in fine-grained      duct a comprehensive ablation study. Table 5 de-
attribution, SSLA demonstrates exceptional robust-       tails the performance of various model variants
ness in the binary classification setting. Notably,      across the Essay, Reuters, and Wikipedia (WP)
on the Reuters dataset, our method achieves near-        datasets. The results confirm the necessity of
perfect scores (F1 > 0.99), effectively matching         multi-view modeling: variants relying on a sin-
the performance of specialized binary detectors like     gle source of evidence consistently underperform
ConDA and OTB-D. This confirms that the fine-            the full SSLA framework across domains. To fur-
grained stylistic fingerprints extracted by SSLA         ther isolate the contribution of the rewrite-based
also serve as highly effective discriminators for        rigidity signal, we additionally include two targeted
general machine-generated artifacts.                     variants, “spres only” and “SSLA w/o spres ”. The
                                                         results show that spres alone retains meaningful
A.2 Probe Independence Analysis                          discriminative power, while removing it from the
To further support the discussion in the main text       complete system leads to a consistent performance
regarding the probe-independent nature of our            drop. Notably, our proposed Full Fusion strategy
stylistic signals, Table 4 presents the detailed per-    achieves the best stability and performance, con-
formance comparison when replacing the default           firming that the attention-based fusion mechanism
rewriter (DeepSeek-V3) with a structurally distinct      effectively mitigates the risk of overfitting.
model (Gemini-1.5-Flash). The results demon-
strate that SSLA maintains highly stable attribution     A.6     Feature Contribution Analysis
performance across different rewriting probes.           We conduct a SHAP (SHapley Additive exPlana-
                                                         tions) analysis to interpret the decision-making pro-
A.3 Qualitative Analysis Visualization
                                                         cess of our dual-path framework. As illustrated in
Figure 5 visualizes the discriminative capability of     Figure 7, specific stylistic components, such as SN-
SSLA through feature clustering and classification       Grams and lexical density metrics, play a decisive
confusion matrices. Specifically, the t-SNE plot         role in the model’s predictions, complementing the
(a) is generated using the 128-dimensional aligned       semantic backbone. This provides transparency to
hidden representation halign = [hstyle ; hsem_proj ].    the attribution process, validating that SSLA relies
Here, hstyle ∈ R64 is the output of the style MLP,       on consistent linguistic patterns rather than opaque
and hsem_proj ∈ R64 is obtained by projecting            artifacts.
RoBERTa’s 768-dimensional pooled semantic fea-
tures through a linear dimensionality reduction          A.7     Adversarial Persona Prompting Details
layer.                                                   In Section 4.3, we evaluate the robustness of SSLA
   In Table 5, “Feature” denotes the handcrafted         against extreme style-masking attacks (persona-
feature block composed of static linguistic metrics      steering). To ensure all evaluated SOTA models
(sling ) and rewrite-based rigidity features (spres ),   generate text under an identical stylistic constraint,
excluding SN-Grams.                                      we employed the following standardized prompt
                                                         template:
A.4 Text Length Sensitivity Analysis
We further investigate the robustness of SSLA un-              “You are a BBC news editor. Rewrite the follow-
                                                                ing lead sentence into a full news article (∼300
der resource-constrained settings by analyzing its              words).
performance across different text length intervals.            Rules: (1) MUST start with: "[prefix]"; (2) Use a
Figure 6 presents the detailed curves for F1-score,            neutral tone; (3) Include realistic details; (4) Do

                                                    37262


--- PAGE BREAK ---

                         Table 3: Binary Detection Performance (HWT vs. MGT). Best results in each column are bolded.

           Test Task Detector                                                             Essay                                                                        Reuters                                                                    WP
                                                              Acc                F1           Prec                       Rec        Acc                           F1               Prec       Rec                         Acc          F1                     Prec                  Rec
           Likelihood                                     0.893                 0.894        0.887                       0.901    0.765                     0.750                  0.801      0.705                       0.830   0.829                      0.835                  0.823
           Rank                                           0.784                 0.800        0.745                       0.865    0.617                     0.659                  0.594      0.740                       0.727   0.747                      0.695                  0.808
           Log_Rank                                       0.898                 0.900        0.888                       0.911    0.762                     0.742                  0.810      0.685                       0.820   0.819                      0.825                  0.813
           Entropy                                        0.761                 0.766        0.751                       0.782    0.455                     0.426                  0.450      0.405                       0.724   0.741                      0.699                  0.787
           Rank_GLTR                                      0.901                 0.902        0.897                       0.906    0.767                     0.747                  0.816      0.690                       0.803   0.794                      0.829                  0.762
           DetectGPT                                      0.759                 0.742        0.797                       0.694    0.750                     0.729                  0.794      0.675                       0.674   0.683                      0.665                  0.702
           NPR                                            0.681                 0.657        0.710                       0.611    0.735                     0.715                  0.773      0.665                       0.717   0.718                      0.715                  0.722
           LRR                                            0.888                 0.885        0.907                       0.865    0.782                     0.746                  0.895      0.640                       0.797   0.783                      0.843                  0.732
           OpenAI-Detector                                0.722                 0.703        0.755                       0.658    0.817                     0.780                  0.977      0.650                       0.790   0.741                      0.967                  0.601
           ConDA                                          0.992                 0.992        0.992                       0.992    0.997                     0.997                  0.997      0.995                       0.891   0.902                      0.821                  0.892
           OTB-D                                          0.998                 0.996        0.998                       0.993    0.997                     0.995                  0.998      0.992                       0.989   0.977                      0.994                  0.963
           LM-D                                           0.979                 0.979        0.964                       0.964    0.972                     0.972                  0.960      0.985                       0.904   0.911                      0.844                  0.989
           SSLA (Ours)                                    0.993                 0.993        0.995                       0.994    0.997                     0.997                  0.993      0.997                       0.974   0.974                      0.975                  0.974




                                                        (a)
                                                                                                                                                                                                  (b)

Figure 5: Qualitative visualization of SSLA’s discriminative capability. (a) t-SNE plot showing clear cluster
separation based on the 128D aligned hidden representations. (b) Confusion matrix demonstrating high classification
accuracy on the Reuters dataset.

           1.000                                                                                           1.000                                                                                            1.000



           0.900                                                                                           0.900                                                                                            0.900



           0.800                                                                                           0.800                                                                                            0.800



           0.700                                                                                           0.700                                                                                            0.700




F1 Score                                                                                          Recall                                                                                        Precision
           0.600                                                                                           0.600                                                                                            0.600



           0.500                                                                                           0.500                                                                                            0.500



           0.400                                                                                           0.400                                                                                            0.400



           0.300                                                        SSLA     ConDA                     0.300                                                           SSLA     ConDA                   0.300                                                           SSLA     ConDA
                                                                        OTB-D    OpenAI                                                                                    OTB-D    OpenAI                                                                                  OTB-D    OpenAI
                                                                        LM-D                                                                                               LM-D                                                                                             LM-D
           0.200                                                                                           0.200                                                                                            0.200
                   <50        50-100                          100-200               >200                           <50           50-100                          100-200               >200                         <50           50-100                          100-200               >200
                                       Text Length (tokens)                                                                               Text Length (tokens)                                                                             Text Length (tokens)




                                       (a)                                                                                                (b)                                                                                              (c)
Figure 6: Text Length Sensitivity Analysis. SSLA demonstrates consistent robustness across different text lengths.
From left to right: F1, Recall, and Precision, maintaining stable performance even in short-text scenarios.


                    NOT include phrases such as ‘As an AI model’ or                                                                                    deep stylometric fingerprints remain effective dis-
                   ‘I am an assistant’.”                                                                                                               criminators even under such extreme semantic ho-
                                                                                                                                                       mogenization.
   By enforcing a strict professional persona ("BBC
news editor") and explicit constraints (neutral tone,
                                                                                                                                                       A.8                 Qualitative Case Study and Error
specific prefix), this prompt forces the generated
                                                                                                                                                                           Analysis
texts from different LLMs to exhibit massive se-
mantic, lexical, and structural overlap. The results                                                                                                   To provide a transparent view of the decision-
presented in the main text demonstrate that SSLA’s                                                                                                     making process, we present the full text and cor-
                                                                                                                                     37263


--- PAGE BREAK ---

Table 4: Performance comparison of different rewriting                                                Predictions & Metrics:
probes. The results demonstrate that SSLA maintains
robust attribution performance regardless of whether                                                           Path              Prediction
DeepSeek-V3 or Gemini-1.5-Flash is used as the                                                                 Ground Truth      Human
rewriter.                                                                                                      Style Path        Human
                                                                                                               Semantic Path     StableLM
 Dataset          Rewriter Probe                     Acc        F1          Prec          Rec                  Final Fusion      StableLM (Incorrect)
 2*Essay          DeepSeek-V3 (Default)            0.968       0.945       0.949         0.943
                  Gemini-1.5-Flash (New)           0.974       0.953       0.954         0.952        Analysis: This sample features a highly styl-
 2*Reuters        DeepSeek-V3 (Default)            0.978       0.966       0.964         0.969        ized, dark-themed fan-fiction narrative. Sup-
                  Gemini-1.5-Flash (New)           0.954       0.952       0.954         0.952
                                                                                                      ported by our multi-dimensional profiling, the
 2*WP             DeepSeek-V3 (Default)            0.971       0.956       0.955         0.958
                  Gemini-1.5-Flash (New)           0.958       0.957       0.953         0.952        Style Path correctly detected human-like stylis-
                                                                                                      tic traits, evidenced by a high Average Dependency
                                                                                                      Distance (2.99) and a specific rewriting rigidity
                                                                                                      (BERTScore F1: 0.869). However, the Seman-
                                                                                                      tic Path (RoBERTa) misclassified the text as Sta-
                                                                                                      bleLM. This is likely due to the semantic overlap
                                                                                                      between creative writing prompts and the data dis-
                                                                                                      tribution found in specific LLM training sets. The
                                                                                                      fusion layer incorrectly assigned higher attention
                                                                                                      weight to the semantic embeddings, failing to lever-
                                                                                                      age the accurate stylistic signal in this instance.


                                                                                                      Case 2: Synergetic Correction (Success
                                                                                                      Case)
                                       Source Models
        Semantic Encoder(h)     Style-preserving Features(s)         Structural SN-gram Features(g)   Original Text (ChatGLM):

Figure 7: Relative Contribution of Semantic vs.                                                            “Once upon a time, in a small town nestled in the
                                                                                                           heart of a bustling city, there was a young girl
Stylistic Paths. SHAP analysis reveals that stylistic                                                      named Sarah. Sarah was a kind and gentle soul,
features (Features + SN-Grams) play a crucial role, com-                                                   with a kind heart and a gentle nature. She was the
plementing the semantic backbone.                                                                          only child in her family, and she loved nothing
                                                                                                           more than spending time with her siblings and her
                                                                                                           parents. One day, Sarah’s parents took her to the
                                                                                                           dentist to get her first set of teeth. As they were
responding metrics for two representative cases.                                                           cleaning her teeth, the dentist told Sarah that she
These examples highlight the interaction between                                                           had a rare condition that caused her teeth to grow
the stylistic and semantic paths in SSLA.                                                                  at an unusual rate. She needed to have all of her
                                                                                                           teeth removed and replaced with artificial ones,
Case 1: Semantic Overpowering (Error                                                                       which would cost a fortune. Sarah’s parents were
Analysis)                                                                                                  shocked and horrified by the news. They tried to
                                                                                                           find a way to pay for the surgery, but the price
Original Text (Human):                                                                                     of baby teeth was skyrocketing, and there was no
                                                                                                           way they could afford it. As the days went by,
     “Pikachu was bleeding, but Ash didn’t care. He                                                        Sarah’s parents became more and more desperate.
     needed this badge to move on and he wasn’t stop-                                                      They started selling their valuable property and
     ping until he had crushed everyone in his path.                                                       scrimping on their expenses to try and make ends
     He yelled to Pikachu, ’Alright that’s enough, stop                                                    meet.”
     wasting time and Hit him again with a thunder-
     bolt, Pikachu!’ The small red dots of Pikachu’s
     cheeks began to pulse, The air began to tense and
                                                                                                      Predictions & Metrics:
     lightning arced from the sky down to the battle-
                                                                                                                Path              Prediction
     field. The opponent was nervous now, because at
     once a large bolt of thunder burst from the clouds,                                                        Ground Truth      ChatGLM
     through the air as it went and catching the op-                                                            Style Path        ChatGPT
     ponent’s Arbok by surprise. It shook with the                                                              Semantic Path     ChatGLM
     force of the electricity coursing through its body                                                         Final Fusion      ChatGLM (Correct)
     and within seconds, collapsed on the field. It at-
     tempted to inch slowly towards its master in one                                                 Analysis: The generator employs a standard fairy-
     final act, as the life drained slowly from its eyes.                                             tale opening (“Once upon a time...”). Supported by
     Ash was declared the winner, but he already knew
     that. Just another victim on the road to his destiny,                                            our explicit stylistic profiling, this structure aligns
     there would be many, many more.”                                                                 closely with the polished and standardized output
                                                                                                  37264


--- PAGE BREAK ---

Table 5: Ablation study on core components of SSLA. The table additionally includes two targeted variants, “spres
only” and “SSLA w/o spres ”, to isolate the contribution of the rewrite-based rigidity signal. The proposed Full
Fusion strategy achieves the best overall stability and performance across diverse domains, especially on the
challenging WP dataset.

       Model Variant                      Essay                   Reuters                WP           Avg
                                  Acc              F1       Acc             F1   Acc           F1      F1
       feature                    0.620           0.534     0.377       0.350    0.537        0.654   0.513
       spres only                 0.435           0.446     0.516       0.317    0.474        0.561   0.441
       SN_Gram                    0.783           0.654     0.800       0.679    0.757        0.654   0.662
       RoBERTa Baseline           0.941           0.899     0.975       0.963    0.959        0.943   0.935
       SN_Gram + Feature          0.904           0.904     0.921       0.921    0.850        0.850   0.892
       RoBERTa + Feature          0.904           0.829     0.937       0.899    0.937        0.901   0.876
       RoBERTa + SN_Gram          0.968           0.952     0.975       0.963    0.959        0.943   0.953
       SSLA w/o spres             0.954           0.944     0.958       0.951    0.946        0.947   0.947
       SSLA (Full Fusion)         0.968           0.945     0.978       0.966    0.971        0.956   0.956



patterns of ChatGPT (evidenced by a Lexical Di-
versity of 0.615, an Avg. Dep. Depth of 2.87, and
a high rewriting rigidity BERTScore F1 of 0.898),
leading the Style Path to a misclassification. How-
ever, the Semantic Path (RoBERTa) accurately
identified the latent distributional fingerprints of
ChatGLM based on deep semantic embeddings.
The attention-based fusion successfully prioritized
the semantic confidence over the stylistic ambigu-
ity, resulting in a correct attribution.




                                                          37265
```

### Responsible NLP Checklist PDF

```text
Responsible NLP Checklist
Paper title: Synergizing Stylometrics with Semantics: Dual-Path Framework for LLM Detection and
Attribution
Authors: Xingyu Lu, Yumeng Ma, Xiang Zhou, Shengli Gan, Guiying Deng, Yang Wen, Yanbing Liu
        How to read the checklist symbols:

          ✓ the authors responded ‘yes’
          □
          ✗
          □ the authors responded ‘no’
          □ the authors indicated that the question does not apply to their work
          N/A



          □ the authors did not respond to the checkbox question
           For background on the checklist and guidance provided to the authors, see the Responsible NLP Checklist
        page at ACL Rolling Review.



✓ A. Questions mandatory for all submissions.
□
□✓ A1. Did you describe the limitations of your work?
      This paper has a Limitations section.

  ✗
  □ A2. Did you discuss any potential risks of your work?
      Our work focuses on methodological advances in machine-generated text attribution and does not
      involve deployment, user interaction, or new data collection. Potential societal risks are indirect and
      depend on downstream applications rather than the attribution methodology itself. Therefore, we do
      not include a dedicated discussion of risks.

✓ B. Did you use or create scientific artifacts? (e.g. code, datasets, models)
□
 ✗
 □ B4. Did you discuss the steps taken to check whether the data that was collected/used contains any
     information that names or uniquely identifies individual people or offensive content, and the steps
     taken to protect/anonymize it?
     We utilized established, publicly available benchmark datasets (MGTBench: Essay, Reuters, Wikipedia).
     We relied on the curation performed by the original dataset creators and did not collect new private
     data.
  ✓ B6. Did you report relevant statistics like the number of examples, details of train/test/dev splits, etc.
  □
     for the data that you used/created?
     We describe the datasets in Section 4.1. Furthermore, we report the data efficiency analysis with
     varying training set sizes (from 839 to 8397 samples) in Section 4.3 and Figure 3.

✓ C. Did you run computational experiments?
□
 ✓ C2. Did you discuss the experimental setup, including hyperparameter search and best-found
 □
     hyperparameter values?
     We provide implementation details in Section 4.1, including the use of the RoBERTa-base encoder
     and MLP settings. The optimization strategy and loss function parameters are described in Section
     3.3.
  ✓ C3. Did you report descriptive statistics about your results (e.g., error bars around results, summary
  □
      statistics from sets of experiments), and is it transparent whether you are reporting the max, mean,
      etc. or just a single run?
The Responsible NLP Checklist used at ACL Rolling Review is adopted from NAACL 2022, with the addition of ACL 2023
question on AI writing assistance and further refinements based on ARR practice. ACL 2026 used a subset of ARR checklist form.


--- PAGE BREAK ---

       We report Macro-F1, Precision, and Recall scores across multiple datasets in Table 1 and Table 2.
       We also provide performance curves across different text length intervals in Figure 6 to demonstrate
       stability.

✗
□ D. Did you use human annotators (e.g., crowdworkers) or research with human subjects?
 □ D1. Did you report the full text of instructions given to participants, including e.g., screenshots,
 N/A


       disclaimers of any risks to participants or annotators, etc.?
       (left blank)

 □ D2. Did you report information about how you recruited (e.g., crowdsourcing platform, students)
 N/A


       and paid participants, and discuss if such payment is adequate given the participants’ demographic
       (e.g., country of residence)?
       (left blank)

 ✗
 □ D3. Did you discuss whether and how consent was obtained from people whose data you’re
       using/curating (e.g., did your instructions explain how the data would be used)?
       Our study utilizes established, publicly available benchmark datasets (MGTBench) for research
       purposes. We did not participate in the original data collection and therefore did not discuss the
       consent process, relying on the ethical standards and distribution licenses of the original dataset
       creators.

 □ D4. Was the data collection protocol approved (or determined exempt) by an ethics review board?
 N/A


       (left blank)

✗
□ E. Did you use AI assistants (e.g., ChatGPT, Copilot) in your research, coding, or writing?
 □ E1. If you used AI assistants, did you include information about their use?
 N/A


       AI tools were employed in a limited capacity to support writing quality, such as improving grammar,
       clarity, and wording, and to assist with procedural aspects of the submission process. They had no
       role in shaping the scientific ideas, methodological design, experimental findings, or substantive
       content of this work. In line with ACL guidelines, this level of use does not necessitate explicit
       disclosure in the paper.
```

## Extraction verification

- **Beginning checked:** Paper page 1 was rendered and compared with the extracted title, authors, affiliations, abstract, introduction opening, proceedings citation, and page number 37252.
- **Middle checked:** Paper page 8 was rendered and compared with Tables 1 and 2, Figure 4, cross-domain analysis, persona-steering analysis, and page number 37259.
- **End checked:** Paper page 14 was rendered and compared with Table 5, the final qualitative case-study analysis, and page number 37265. Both checklist pages were also rendered and compared with the extracted responses.
- **Structure checked:** The official paper has 14 pages, sections 1 through 5, Limitations, Acknowledgments, References, and Appendix A.1 through A.8 with five tables and seven figures. The official checklist has two pages. All were present in the extraction in source order.
- **Known omissions:** none

## Preserved attachments

| Path | Role in the source | SHA-256 | Preservation / extraction notes |
|---|---|---|---|
| `human-eyes/references/sources/snapshots/attachments/lu-et-al-stylometrics-semantics-acl-2026.pdf` | Authoritative 14-page proceedings paper | `b2626dabe0f9710e49f094f962a8e6c6fe54ced857c11aa947c83735031df76b` | Exact downloaded PDF bytes preserved; complete embedded text extracted with Poppler and selected pages rendered for verification. |
| `human-eyes/references/sources/snapshots/attachments/lu-et-al-stylometrics-semantics-checklist.pdf` | Official two-page Responsible NLP Checklist | `25917632056d6eed4e89d4eb28317ee03c327903a88d7f97d8c8da0f4ef8023d` | Exact downloaded PDF bytes preserved; both pages extracted and rendered for verification. |
