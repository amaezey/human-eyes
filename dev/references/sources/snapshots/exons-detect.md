# Exons-Detect: Identifying and Amplifying Exonic Tokens via Hidden-State Discrepancy for Robust AI-Generated Text Detection

- **Canonical URL:** https://aclanthology.org/2026.acl-long.1211/
- **Alternate access URLs:**
  - https://aclanthology.org/2026.acl-long.1211.pdf
  - https://aclanthology.org/attachments/2026.acl-long.1211.checklist.pdf
  - https://doi.org/10.18653/v1/2026.acl-long.1211
- **Author / owner:** Xiaowei Zhu, Yubing Ren, Fang Fang, Shi Wang, Yanan Cao, and Li Guo
- **Publisher:** Association for Computational Linguistics
- **Published:** 2026-07-02 to 2026-07-07
- **Retrieved:** 2026-07-15
- **Stable identifier:** DOI 10.18653/v1/2026.acl-long.1211; ACL Anthology ID 2026.acl-long.1211
- **Version / revision:** ACL 2026 proceedings version, pages 26324-26336, plus ACL Responsible NLP Checklist
- **Extraction method:** Official ACL paper and checklist PDFs downloaded directly; page and attachment metadata checked with `pdfinfo`; all pages converted from embedded text layers with Poppler `pdftotext -layout`; C0 control bytes introduced by figure-font extraction removed mechanically; official PDFs preserved as attachments; paper pages 1, 7, and 13 and checklist pages 1 and 2 rendered with `pdftoppm` and visually checked.
- **Full-text status:** complete
- **Access and transformation notes:** All 13 paper pages and both checklist pages were obtained. The paper text layer preserves prose, equations, table values, captions, appendices, and references. Some labels in Figures 3 and 4 use a malformed embedded font and remain garbled in the text extraction. The rendered pages and preserved official PDF retain those labels and visual encodings. C0 control bytes and page-break controls were removed so the Markdown remains valid text. No substantive prose was omitted.

## Full text

### Paper

    Exons-Detect: Identifying and Amplifying Exonic Tokens via Hidden-State
             Discrepancy for Robust AI-Generated Text Detection
                               Xiaowei Zhu1,2 , Yubing Ren1,2 , Fang Fang1,2 ,
                                                                           ∗


                                    Shi Wang3 , Yanan Cao1,2 , Li Guo1,2
                                                            ∗

           1
             Institute of Information Engineering, Chinese Academy of Sciences, Beijing, China
         2
           School of Cyber Security, University of Chinese Academy of Sciences, Beijing, China
              3
                Institute of Computing Science, Chinese Academy of Sciences, Beijing, China
                             {zhuxiaowei, renyubing, caoyanan}@iie.ac.cn

                           Abstract                                         Existing Methods

         The rapid advancement of large language                     Input Sequence
                                                                       𝑥 𝑥 𝑥 𝑥 𝑥 𝑥 𝑥 𝑥 𝑥 …… 𝑥
         models has increasingly blurred the bound-
         ary between human-written and AI-generated                    weight = 1
                                                                                      x
                                                                                      uniform token
         text, raising societal risks such as misinforma-
         tion dissemination, authorship ambiguity, and                  Average           Less Robust

         threats to intellectual property rights. These
                                                                            Exons-Detect
         concerns highlight the urgent need for effective
         and reliable detection methods. While existing              Input Sequence
                                                                       𝑥 𝑥 𝑥 𝑥 𝑥 𝑥 𝑥 𝑥 𝑥 ……𝑥
         training-free approaches often achieve strong
                                                                       weight = 1     x   intronic token
         performance by aggregating token-level signals                weight > 1     x     exonic token
         into a global score, they typically assume uni-
                                                                        Weighted          More Robust
         form token contributions, making them less
         robust under short sequences or localized to-
         ken modifications. To address these limita-                Figure 1: Advantages of Our Method Exons-Detect.
         tions, we propose Exons-Detect, a training-free
         method for AI-generated text detection based
         on an exon-aware token reweighting perspec-               dissemination, authorship ambiguity, and threats
         tive. Exons-Detect identifies and amplifies in-           to intellectual property rights (Ahmed et al., 2021;
         formative exonic tokens by measuring hidden-              Adelani et al., 2019; Guo et al., 2021). Prior stud-
         state discrepancy under a dual-model setting,
                                                                   ies (Clark et al., 2021) further reveal that humans
         and computes an interpretable translation score
         from the resulting importance-weighted token              perform only marginally above random chance in
         sequence. Empirical evaluations demonstrate               distinguishing AI-generated from human-written
         that Exons-Detect achieves state-of-the-art de-           text. This limitation highlights the urgent need for
         tection performance and exhibits strong robust-           effective and reliable detection methods.
         ness to adversarial attacks and varying input                Existing detection approaches can be broadly cat-
         lengths. In particular, it attains a 2.2% rela-           egorized into training-based and training-free meth-
         tive improvement in average AUROC over the
                                                                   ods. Training-based methods require large-scale
         strongest prior baseline on DetectRL. Code and
         data are available at https://github.com/                 labeled data and rely on supervised deep models to
         Xiaoweizhu57/Exons-Detect.                                learn implicit textual representations, which limits
                                                                   their scalability and cross-domain generalization.
    1    Introduction                                              In contrast, training-free methods compute token-
                                                                   level statistics, such as Binoculars (Hans et al.,
    The rapid advancement of large language models                 2024), under the generative distributions of proxy
    (LLMs) has enabled them to generate highly fluent              LLMs, and typically aggregate these signals by
    and coherent text, substantially narrowing the ob-             averaging across token positions to form a global
    servable gap between AI-generated text and human               detection score. While effective in many settings,
    writing. While such progress has catalyzed signifi-            this uniform aggregation assumes equal contribu-
    cant technological breakthroughs across both indus-            tion from all tokens, making such methods less
    try and academia, it has simultaneously introduced             robust when token sequences are short, or localized
    pressing societal risks, including misinformation              token modifications are introduced. Consequently,
        * Co-Corresponding authors.                                truly informative tokens can be overwhelmed by
                                                             26324
Proceedings of the 64th Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers), pages 26324–26336
                                 July 2-7, 2026 ©2026 Association for Computational Linguistics
less relevant ones, motivating the need for a mecha-           introns in gene fragments, we introduce the
nism that differentiates token-level functional roles          notions of exonic tokens and intronic tokens
rather than treating all tokens uniformly.                     in text sequences, emphasizing that different
   Inspired by molecular biology, we view a text se-           tokens contribute unequally to detection.
quence as a gene fragment composed of exons and
                                                             • We propose Exons-Detect, a novel training-
introns. Exons are directly involved in protein trans-
                                                               free method that identifies exonic tokens and
lation, while introns play a secondary role. Analo-
                                                               amplifies their importance to capture more
gously, tokens with large hidden-state discrepancy
                                                               informative source-specific signals, enabling
are treated as exonic tokens that carry stronger dis-
                                                               robust AI-generated text detection.
criminative signals, whereas the remaining tokens
are regarded as intronic. During transcription, both         • Extensive experiments demonstrate that
exons and introns are preserved in the pre-mRNA,               Exons-Detect provides a robust, efficient,
corresponding to uniform initial weighting of all              and broadly generalizable solution for AI-
tokens. Splicing then removes introns and empha-               generated text detection, delivering consistent
sizes exons in mature mRNA. Mirroring this pro-                improvements across 3 public benchmarks, 2
cess, we identify exonic tokens via hidden-state dis-          adversarial attacks, and varying input lengths,
crepancy and amplify their contributions through               with inference latency below 0.8 s per sample.
assigning additional weights. The final detection
is achieved by aggregating the reweighted token
                                                         2    Related Work
sequence to compute the translation score. This
exon-aware reweighting captures intrinsic differ-        Training-based methods typically leverage deep
ences between AI-generated and human-written             learning models to supervisedly learn latent textual
texts in a fine-grained and interpretable manner.        features that distinguish AI-generated text from
   Building on this intuition, we propose Exons-         human-written content. Early work by OpenAI
Detect, a novel training-free method for AI-             (Solaiman et al., 2019) developed a RoBERTa-
generated text detection. Given an input sequence,       based classifier. RADAR (Hu et al., 2023) in-
we extract hidden representations at each token po-      corporated adversarial training to improve robust-
sition and quantify their discrepancy under a pair of    ness against paraphrased inputs. Biscope (Guo
proxy LLMs. Tokens whose representation discrep-         et al., 2024a) introduced a bidirectional cross-
ancy exceeds a predefined discrepancy threshold          entropy loss to optimize classifier performance.
are identified as exonic tokens. We map these dis-       DeTeCtive (Guo et al., 2024b) and DETree (He
crepancies through a nonlinear function to obtain        et al., 2025) mapped texts from different sources
additional weights for exonic tokens, which are in-      or constructions into high-dimensional representa-
tegrated with the initial weights for computing the      tion spaces, followed by similarity-based detec-
translation score. Finally, Exons-Detect determine       tion. Training-based detectors often overfit in-
the detect result by comparing the translation score     distribution patterns and degrade sharply under dis-
against a decision threshold, effectively amplifying     tribution shifts (Chakraborty et al., 2023; Uchendu
the discriminative signals carried by exonic tokens.     et al., 2020), motivating increasing interest in uni-
   Exons-Detect achieves state-of-the-art perfor-        versal and reliable training-free detection.
mance across multiple publicly available detection       Training-free methods distinguish texts by esti-
benchmarks. In particular, Exons-Detect achieves         mating statistical scores from the generative proba-
a relative improvement of 2.2% in average AU-            bilities under proxy LLMs. Traditional approaches
ROC over the strongest existing baseline DNA-            including LogRank (Gehrmann et al., 2019), Like-
DetectLLM on DetectRL. Moreover, Exons-Detect            lihood (Hashimoto et al., 2019), and Entropy (Ip-
exhibits strong robustness against various adversar-     polito et al., 2020) quantified generative uncertainty
ial attacks and across different input lengths. Effi-    by averaging probability rank, log-likelihood, and
ciency experiments further demonstrate that Exons-       entropy under a proxy model. DetectGPT (Mitchell
Detect offers rapid detection capability, making it      et al., 2023) established a new paradigm by in-
well suited for large-scale, real-time detection. Our    troducing phrase-level perturbations to evaluate
contributions are summarized as follows:                 distributional curvature. Fast-DetectGPT (Bao
                                                         et al., 2024) proposed an optimized sampling strat-
   • Inspired by the distinct roles of exons and         egy for estimating conditional probability curva-
                                                    26325
                             〇 Observation & Motivation                                                                  ① Step 1: Dual-Model Token Feature Extraction
                                                                                                                          Input Text                                                                 Hidden Representation
                                                                                                                                                    Input            Proxy Model 𝑀         output            𝐻 ( ) and 𝐻 ( )
                                    AI-generated Text                                         Positive token
                                                                                                                                       Tokenize
                              a             movie        that          aims       to       consolidate                                                                                               Conditional Probability
                                                                                                                                                                     Proxy Model 𝑀                                      𝑃
                                  ...           announced           their       decision          ...
                                                                                                                         Token Sequence                                                                                𝑃

                                    Human-written Text                                        Negative token

                             guards              discovered            broken       bottles             ...
                                                                                                                         ② Step 2: Exonic Token Identification and Reweighting
                                        damage           to            Whiterocks          unit               ...         Hidden Representation                  Discrepancy
                                                                                                                                                                                       x      Exonic tokens mapping        Weights


                                        Phenomena in the Representation                                                                              calculate           compare       x      Intronic tokens                  𝑤
                                                 Positive Token                 Negative Token
                                                                                                                             𝐻( )            𝐻( )




 Hidden-state discrepancy
                            0.5
                            0.4
                                                                  Exonic Tokens
                            0.3
                            0.2
                                                                                Discrepancy threshold θ                  ③ Step 3: Translation Score-based Detection
                            0.1
                             0
                                                                                                                          Conditional Probability                                                   Translation Score <= Threshold
                                                                                                                                             𝑃
                                        1   2    3   4        5    6   7    8   9 10 11 12 13 14 15 16
                                                                                                                    ……                      𝑃
                                                                                                                                                                                                               AI-generated Text
                                                                                                                                                                                                    Translation Score > Threshold
                                            Based on this observation, how can we                                                                       compute                    judgment
                                                                                                                                         𝑊                                                                     Human-written Text
                                            further detect text more accurately?                                         Importance Weights                         Translation Score



                                                                                                                     Figure 2: Overview of Exons-Detect.


ture, achieving substantial gains in both speed                                                                                                        where s denotes an input sequence of length T , wt
and accuracy compared to DetectGPT. Binocu-                                                                                                            denotes the normalized weight, and PM (xt ) and
lars (Hans et al., 2024) mitigated high-perplexity                                                                                                     PM̃ (xt ) denote the conditional generation distribu-
human texts by using the ratio of log-perplexity                                                                                                       tions of the t-th token under models M and M̃ .
to cross-perplexity, while DNA-DetectLLM (Zhu
et al., 2025b) further enhanced this score with a                                                                                                      Observation. In training-free detection, scores
mutation-repair mechanism, achieving more robust                                                                                                       such as Binoculars are computed by averaging
performance. Lastde (Xu et al., 2024) captured                                                                                                         token-level contributions, where AI-generated texts
local textual characteristics via Diversity Entropy,                                                                                                   typically yield lower scores than human-written
while IRM (Liu et al., 2025) leveraged discrepan-                                                                                                      texts. Accordingly, in AI-generated text, tokens
cies in generative probabilities before and after rein-                                                                                                whose individual contributions fall below the de-
forcement learning from human feedback (RLHF)                                                                                                          cision threshold tend to increase class separability,
to capture the divergence.                                                                                                                             whereas in human-written text, tokens with con-
                                                                                                                                                       tributions above the threshold play an analogous
3                             Methodology                                                                                                              role. We refer to such tokens as positive tokens
                                                                                                                                                       and, by analyzing their associated hidden-state rep-
3.1 Preliminaries                                                                                                                                      resentations that may encode source-related signals
Log-perplexity and Cross-perplexity. Log-                                                                                                              (Chen et al., 2025), as shown in Figure 2. When
perplexity quantifies the average token-level neg-                                                                                                     we examine tokens whose hidden-state discrepancy
ative log-likelihood under a single proxy model,                                                                                                       between model M and M̃ exceeds a discrepancy
whereas cross-perplexity measures the average per-                                                                                                     threshold θ, the number of tokens that increase
token cross-entropy computed across two mod-                                                                                                           class separability is markedly larger than the num-
els. To model variation in token-wise importance,                                                                                                      ber that decreases it. This asymmetric enrichment
we further introduce weighted log-perplexity and                                                                                                       suggests that tokens with high-discrepancy more
weighted cross-perplexity, which incorporate token-                                                                                                    often carry source-relevant signals, whereas other
specific importance weights into their computation:                                                                                                    tokens contribute more weakly or inconsistently.

                                                                                       T
                                                                                                                                                       Motivation. Motivated by this observation, we
                                                                                       X
                                            log PPLW
                                                   M (s) = −                                  wt log PM (xt ),                                         refer to tokens with high hidden-state discrepan-
                                                                                       t=1                                                             cies as exonic tokens, and the remaining ones as
                                                                                       T
                                                                                       X                                                               intronic tokens, reflecting their different relevance
                     log X-PPLW
                              M,M̃ (s) = −                                                    wt PM (xt ) log PM̃ (xt ),
                                                                                       t=1
                                                                                                                                                       to the text’s origin. This naturally suggests a simple
                                                                                                                                          (1)          and effective strategy: during detection, we iden-
                                                                                                                                             26326
tify high-discrepancy exonic tokens and amplify            discrepancy using the cosine distance. For the t-
their contributions. By reweighting these tokens,          th token, we aggregate its hidden representations
the final detection score is encouraged to move fur-       across all L layers from models M and M̃ , and
ther toward the correct side, resulting in robust and      define the token-level discrepancy as
separable detection. See Appendix A for analysis.
                                                                       1 X
                                                                              L
                                                                                     (l)   (l)
3.2 Overview of Exons-Detect                                      δt =      1 − cos ht , h̃t       ,               (4)
                                                                       L
                                                                              l=1
Figure 2 presents the overall workflow of Exons-
Detect, including three steps:                                      (l)         (l)
                                                           where ht and h̃t denote the hidden representa-
Step 1: Dual-Model Token Feature Extraction.               tions of the t-th token at layer l produced by models
Given an input sequence, we extract token-level            M and M̃ , respectively.
hidden representations and generative probability              Based on the magnitude of δt , we identify exonic
distributions under a reference model M and a              tokens by applying a significance-level criterion.
paired model M̃ .                                          Specifically, a token is classified as an exonic token
Step 2: Exonic Token Identification and                    if its hidden-state discrepancy exceeds a predefined
Reweighting. We measure hidden-state discrep-              discrepancy threshold θ, and as an intronic token
ancy between M and M̃ at each token position to            otherwise:
identify exonic tokens, and map these discrepan-                           (
cies to additional token-level weights.                                      exonic token, if δt > θ,
                                                                     xt =                                      (5)
Step 3: Translation Score-based Detection. We                                intronic token, if δt ≤ θ.
introduce a translation score by aggregating token
contributions according to their weights and proba-           To further emphasize the contribution of exonic
bility distributions, and compare it against a deci-       tokens, we remap their hidden-state discrepancies
sion threshold to determine the detection result.          into importance weights W . Formally, we intro-
                                                           duce a nonlinear mapping function g(·) to obtain a
3.3 Dual-Model Token Feature Extraction                    token-specific additional weight ∆wt = g(δt ):
Given an input sequence s = (x1 , x2 , x3 , . . . , xT )
                                                                   g(δt ) = 1 − exp − α (δt − θ)+ ,       (6)
of length T , we feed it into a proxy LLMs pair:
M and M̃ . Each model consists of L transformer            where (·)+ = max(·, 0) denotes the positive part
layers. For model M , we extract the hidden repre-         operator, which ensures that intronic tokens with
sentations at each token position and layer as             discrepancies below the discrepancy threshold θ
         (l) (l)           (l)
                                                           receive zero additional weight.
  H(l) = h1 , h2 , . . . , hT ,   l = 1, . . . , L,           This nonlinear mapping smoothly amplifies the
                                                   (2)     weights of exonic tokens according to their hidden-
        (l)
where ht ∈ R denotes the hidden representation
               d
                                                           state discrepancies, while avoiding excessive em-
of the t-th token at layer l. Similarly, model M̃          phasis on individual tokens, thereby preserving ro-
produces the corresponding hidden representations          bustness. The final importance weights is formed
                   (l) (l)              (l)
                                                           by summing the initial uniform weight and the ex-
           H̃(l) = h̃1 , h̃2 , . . . , h̃T .        (3)    onic weight increments and normalizing the result,
                                                           given by:
   In addition to hidden representations, both
models provide token-level generative probabili-                           1 + ∆wt
                                                              wt = PT                      ,   t = 1, 2, . . . , T. (7)
ties. Specifically, at each token position t, model                       i=1 (1 + ∆wi )
M defines a conditional generation distribution
PM (xt ) = PM (· | x<t ) over the vocabulary, and          3.5   Translation Score-based Detection
M̃ defines PM̃ (xt ) = PM̃ (· | x<t ), where x<t           We introduce a translation score that integrates the
denotes the preceding context.                             importance weights of both exonic and intronic
                                                           tokens with their conditional probabilities. Prior
3.4 Exonic Token Identification and                        work (Hans et al., 2024) has shown that the ratio be-
    Reweighting                                            tween log-perplexity and cross-perplexity provides
To quantify the representational discrepancy at            a strong discriminative signal for AI-generated text
each token position, we measure the hidden-state           detection. Following this insight, we define the
                                                      26327
initial translation score as the ratio of the weighted   (Hashimoto et al., 2019), LogRank (Gehrmann
log-perplexity to the weighted cross-perplexity:         et al., 2019), and Entropy (Ippolito et al., 2020),
                                                         as well as more recent representative methods, in-
                       log PPLW
                              M (s)                      cluding DetectGPT (Mitchell et al., 2023), Fast-
           R(s) =                      .           (8)
                    log X-PPLWM,M̃
                                   (s)                   DetectGPT (Bao et al., 2024), Binoculars (Hans
                                                         et al., 2024), and Lastde++ (Xu et al., 2024).
To further refine the translation score, we incorpo-     In addition, we compare against the latest and
rate the mutation-repair mechanism proposed in           strongest baselines, IRM (Liu et al., 2025) and
DNA-DetectLLM (Zhu et al., 2025b) as a comple-           DNA-DetectLLM (Zhu et al., 2025b).
mentary component. This mechanism captures the
intrinsic discrepancy between an input sequence          Metrics. We evaluate detection performance us-
and the ideal AI-generated sequence by quantify-         ing the area under the receiver operating character-
ing the difficulty of iteratively repairing mutated      istic curve (AUROC) and the F1 score.
tokens. Importantly, the repair process operates
                                                         Implementation details. To ensure a fair com-
under the same exon-aware importance weights.
                                                         parison, we train all training-based detectors on
Incorporating this mechanism, the final translation
                                                         the HC3 dataset (Guo et al., 2023), which is dis-
score is formulated as:
                                                         joint from all evaluation benchmarks. Prior work
                                                         (Bao et al., 2025) has shown that the performance
             log PPLW                 W
                     M (s) + log PPLM (ŝ)               of training-free methods can vary substantially un-
    R(s) =                                 ,       (9)   der different combinations of LLMs. To elimi-
                  log X-PPLW M,M̃
                                  (s)
                                                         nate this factor, we standardize the reference (scor-
where ŝ denotes the ideal AI sequence, constructed      ing) model across all methods by using Falcon-7B-
by selecting the token with the maximum genera-          Instruct (Penedo et al., 2023) to compute token-
tion probability.                                        level generation probabilities. Moreover, Fast-
   For AI-generated text, exonic tokens contribute       DetectGPT, Binoculars, Lastde++, IRM, DNA-
to shifting the translation score toward smaller val-    DetectLLM, and Exons-Detect all employ Falcon-
ues, whereas for human-written text, exonic tokens       7B (Penedo et al., 2023) as the paired model when
contribute to increasing the translation score. Ac-      computing their respective detection scores. We set
cordingly, the detection result for an input sequence    the discrepancy threshold θ = 0.15 and the map-
is determined as follows:                                ping slope α = 10 by default. More details see
            (                                            Appendix B.
               Human-written Text, R(s) > τ,
   D(s) =
               AI-generated Text,        R(s) ≤ τ.       4.2   Main Results
                                                 (10)    Table 1 compares the detection performance of
                                                         Exons-Detect against other baselines across three
4   Experiments                                          public benchmarks. Overall, Exons-Detect exhibits
4.1 Experimental Setup                                   strong detection accuracy and robust generalization,
                                                         delivering consistently competitive results on M4,
Datasets. To evaluate the detection performance
                                                         DetectRL, and RealDet. It achieves an average AU-
of our method under realistic deployment scenar-
                                                         ROC of 92.14% and an average F1 score of 87.72%,
ios, we conduct experiments on three diverse and
                                                         outperforming the latest baseline DNA-DetectLLM
high-quality public benchmarks: M4 (Wang et al.,
                                                         by 1.4% and 0.8%. Notably, Exons-Detect is the
2024), RealDet (Zhu et al., 2025a), and DetectRL
                                                         only method whose AUROC exceeds 90% on all
(Wu et al., 2024). In particular, we conduct eval-
                                                         evaluated datasets, further highlighting its reliabil-
uations on DetectRL using the Multi-LLM and
                                                         ity for real-world deployment under different text
Multi-Domain settings to examine generalization
                                                         distributions.
across models and domains.
                                                            A closer inspection reveals that most baselines
Baselines. For training-based detectors, we con-         exhibit substantial performance variance across
sider OpenAI-D (Solaiman et al., 2019), BiScope          datasets, indicating sensitivity to changes in text
(Guo et al., 2024a), and R-Detect (Song et al.,          source and distribution. For training-based de-
2025). For training-free approaches, we include          tectors, the mismatch between the training cor-
classical zero-shot detectors such as Likelihood         pus and the evaluation benchmarks leads to lim-
                                                     26328
                      M4           DetectRL Multi-LLM   DetectRL Multi-Domain      RealDet           Avg.
 Detectors
                  AUROC     F1     AUROC        F1      AUROC          F1       AUROC      F1    AUROC    F1
                                            Training-based Methods
 OpenAI-D          77.51   71.18   78.15     71.90      74.60        70.03      84.75    77.47   78.75   72.65
 Biscope           79.74   73.08   79.97     73.20      76.52        71.64      92.88    86.90   82.28   76.21
 R-Detect          61.91   67.14   67.40     66.56      79.19        73.38      65.93    67.72   68.61   68.70
                                             Training-free Methods
 Entropy           83.72   79.10   64.30     71.92      47.82        69.24      75.42    74.72   67.82   73.75
 Likelihood        85.77   78.38   66.82     66.71      48.96        66.69      85.35    79.75   71.73   72.88
 LogRank           87.50   80.70   67.30     66.71      50.55        66.69      86.28    80.69   72.91   73.70
 DetectGPT         73.13   70.11   49.57     66.67      34.67        66.67      78.69    73.80   59.02   69.31
 Fast-DetectGPT    89.77   84.12   82.26     75.93      74.98        68.91      93.25    90.00   85.07   79.74
 Binoculars        90.00   87.40   83.21     82.87      77.45        80.20      93.64    90.51   86.08   85.25
 Lastde++          91.43   84.97   75.36     69.24      67.30        66.67      93.90    89.41   82.00   77.57
 IRM               71.85   70.75   83.02     76.46      91.51        84.05      77.70    76.62   81.02   76.97
 DNA-DetectLLM     91.74   87.72   88.97     84.85      88.23        84.94      94.48    90.58   90.86   87.02
 Exons-Detect      92.43   88.05   90.67     84.95      90.46        86.59      94.98    91.30   92.14   87.72

             Table 1: Detection performance (AUROC and F1 score) on public benchmark datasets.


ited OOD generalization, with AUROC typically            based polishing to human-written texts. Figure 3
remaining below 80%. Among training-free ap-             shows the AUROC of Exons-Detect and baselines
proaches, representative methods such as Fast-           on DetectRL under various attack settings.
DetectGPT, Binoculars, and Lastde++ perform
strongly on M4 and RealDet, yet their performance           Experimental results demonstrate that Exons-
degrades sharply on the more challenging Detec-          Detect exhibits strong robustness across these at-
tRL setting. IRM excels on DetectRL, reaching an         tack scenarios. Specially, under both paraphrasing
AUROC of 91.51% under the Multi-Domain set-              and polishing attacks on DetectRL, Exons-Detect
ting, but fails to maintain comparable performance       consistently outperforms all competing baselines,
on M4 and RealDet. We conjecture that this be-           maintaining a clear performance advantage. A no-
havior arises from IRM’s reliance on probability         table observation is that training-based detectors
discrepancies induced by RLHF, which become              are substantially more vulnerable to adversarial
weaker and harder to exploit when texts are gener-       attacks, as evidenced by BiScope’s AUROC de-
ated by less strongly aligned open-source LLMs.          grading to near-random performance under para-
While DNA-DetectLLM partially alleviates this is-        phrasing and polishing attacks. In contrast, strong
sue, it still falls noticeably behind Exons-Detect       training-free baselines exhibit substantially higher
on DetectRL. In particular, Exons-Detect achieves        robustness to paraphrasing attacks, likely because
AUROC gains of 1.9% under Multi-LLM and 2.5%             DIPPER-based paraphrasing mainly introduces lex-
under Multi-Domain. We attribute this consis-            ical and syntactic variations without fundamentally
tent advantage to Exons-Detect’s ability to reliably     altering underlying statistical features.
identify exonic tokens from hidden-state discrep-
ancies across diverse text distributions, enabling it       However, polishing attacks pose a greater chal-
to extract more precise source-relevant signals and      lenge by injecting advanced LLM alignment and
thereby counteract the cross-dataset bias.               generation signals into human-written texts, blur-
                                                         ring the boundary between human-written and AI-
4.3 Robustness
                                                         generated content. This leads to noticeable perfor-
4.3.1 Robustness against Various Attacks                 mance degradation for several baselines, includ-
In realistic scenarios, input texts are often non-       ing Fast-DetectGPT and IRM. In contrast, Exons-
pristine and may be subject to adversarial attacks.      Detect preserves a high level of detection accuracy
AI-generated texts can undergo paraphrasing at-          even under polishing attacks, highlighting its supe-
tacks to evade detection, while human-written            rior robustness. We attribute this robustness to its
texts are frequently refined using advanced LLMs         ability to exploit hidden-state discrepancies to iden-
through polishing attacks. Paraphrasing attacks em-      tify critical exonic tokens, thereby suppressing the
ploy DIPPER (Krishna et al., 2023) to rephrase AI-       adverse impact of localized textual modifications
generated texts, while polish attacks apply GPT-4o-      on the global detection score.
                                                     26329

                                      'HWHFW5/0XOWL//0 3DUDSKUDVH                                                         'HWHFW5/0XOWL'RPDLQ 3DUDSKUDVH                                                       'HWHFW5/0XOWL//0 3ROLVK                                          'HWHFW5/0XOWL'RPDLQ 3ROLVK







735
                                                                                                     2SHQ$,'HWHFWRU                                                                                         2SHQ$,'HWHFWRU                                                                    2SHQ$,'HWHFWRU                                                                     2SHQ$,'HWHFWRU
                                                                                                           %L6FRSH                                                                                                         %L6FRSH                                                                                    %L6FRSH                                                                                     %L6FRSH
                                                                                                           )DVW'HWHFW*37                                                                                           )DVW'HWHFW*37                                                                      )DVW'HWHFW*37                                                                       )DVW'HWHFW*37
                                                                                                           %LQRFXODUV                                                                                                   %LQRFXODUV                                                                              %LQRFXODUV                                                                               %LQRFXODUV
                                                                                                     /DVWGH                                                                                                       /DVWGH                                                                                  /DVWGH                                                                                   /DVWGH
                                                                                                           ,50                                                                                                                 ,50                                                                                            ,50                                                                                             ,50
                                                                                                           '1$'HWHFW//0                                                                                             '1$'HWHFW//0                                                                        '1$'HWHFW//0                                                                         '1$'HWHFW//0
                                                                                                           ([RQV'HWHFW                                                                                               ([RQV'HWHFW                                                                          ([RQV'HWHFW                                                                           ([RQV'HWHFW


                                                                        )35                                                                                                                       )35                                                                                                    )35                                                                                            )35


                                                                                          Figure 3: Detection performance (AUROC curves) against various attacks.


                                                   'HWHFW5/0XOWL//0                                                                          'HWHFW5/0XOWL'RPDLQ                                                                        Setting ↓                                     M4                       Multi-L                     Multi-D                       RealDet                         Avg.


                                                                                                                                                                                                                                                                                   Exons-Detect                                  92.43                          90.67                           90.46                     94.98                     92.14

                                                                                                                                                                                                                                                                               w/o log PPLW
                                                                                                                                                                                                                                                                                              M (ŝ)                             91.28                          85.32                           80.46                     93.97                     87.76
                                                                                                                                                                                                                                                                                   w/o g(·)                                      91.92                          89.63                           88.66                     94.64                     91.21
$852&

                                                                                              )DVW'HWHFW*37                                                                                        )DVW'HWHFW*37

                                                                                          %LQRFXODUV                                                                                                %LQRFXODUV                                             Model Family ↓
                                                                                              /DVWGH                                                                                                /DVWGH
                                                                                          ,50                                                                                                              ,50                                                           Falcon-7B                                     92.43                          90.67                           90.46                     94.98                     92.14
                                                                                              '1$'HWHFW//0                                                                                      '1$'HWHFW//0

                                                                                              ([RQV'HWHFW                                                                                            ([RQV'HWHFW                                         LLaMA-7B                                      88.64                          92.34                           90.31                     94.47                     91.44

                                                                                                                                                                                                                   Mistral-v0.1-7B                               90.41                          91.42                           85.77                     93.00                     90.15
                                                       /HQJWKWRNHQV                                                                                          /HQJWKWRNHQV
                                                                                                                                                                                                                                                                                   LLaMA-3.2-1B                                  90.50                          92.87                           90.82                     92.58                     91.69

    Figure 4: Detection performance on different length.
                                                                                                                                                                                                                                                                              Table 2: Ablation study results under different settings.

4.3.2 Robustness on Different Lengths
Prior studies (Bao et al., 2024; Tian et al., 2024)                                                                                                                                                                                                                           log PPLW M (ŝ) make essential contributions to de-
have demonstrated that detection performance is                                                                                                                                                                                                                               tection performance and are indispensable compo-
highly sensitive to input length, with shorter texts                                                                                                                                                                                                                          nents of Exons-Detect. Specifically, removing g(·)
being substantially more difficult to identify. To                                                                                                                                                                                                                            and log PPLW M (ŝ) results in average AUROC drops
systematically examine this effect, we truncate in-                                                                                                                                                                                                                           of 1.0% and 4.4%. These degradations indicate
put texts to several predefined lengths and evalu-                                                                                                                                                                                                                            that properly mapping hidden-state discrepancies
ate method robustness under varying length con-                                                                                                                                                                                                                               to token importance weights, as well as leveraging
straints. Figure 4 compares the robustness of                                                                                                                                                                                                                                 the mutation-repair mechanism to further capture
Exons-Detect against five strong baselines on De-                                                                                                                                                                                                                             class-discriminative differences, are effective and
tectRL across different input lengths. The results                                                                                                                                                                                                                            necessary for achieving strong performance.
show that Exons-Detect consistently outperforms                                                                                                                                                                                                                              Impact of the proxy LLM pair. Table 2 also
all competing baselines across predefined lengths,                                                                                                                                                                                                                           reports Exons-Detect’s performance across differ-
achieving an average improvement of 2.7% over                                                                                                                                                                                                                                ent LLM pairings, including Falcon-7B-Instruct
DNA-DetectLLM and 6.4% over IRM. While all                                                                                                                                                                                                                                   with Falcon-7B, LLaMA-2-7B with LLaMA-
methods benefit from increased text length, Exons-                                                                                                                                                                                                                           7B, Mistral-v0.1-7B-Instruct with Mistral-v0.1-
Detect exhibits markedly stronger performance in                                                                                                                                                                                                                             7B, and LLaMA-3.2-1B-Instruct with LLaMA-3.2-
the short-text regime. These results highlight that                                                                                                                                                                                                                          1B. Overall, Exons-Detect achieves consistently
Exons-Detect captures precise source-related sig-                                                                                                                                                                                                                            strong performance across all model combinations,
nals from limited text, leading to superior robust-                                                                                                                                                                                                                          with only modest variation and an average AU-
ness under short-length conditions.                                                                                                                                                                                                                                          ROC exceeding 90% in every setting. Notably,
                                                                                                                                                                                                                                                                             the “LLaMA-3.2-1B-Instruct + LLaMA-3.2-1B”
4.4 Ablation Studies                                                                                                                                                                                                                                                         pairing slightly outperforms “Falcon-7B-Instruct +
Impact of the g(·) and log PPLW      M (ŝ). Table 2                                                                                                                                                                                                                         Falcon-7B” on DetectRL, attaining AUROC scores
evaluates the impact of removing the nonlinear                                                                                                                                                                                                                               of 92.87% and 90.82%. These results indicate that
mapping function g(·) or the computation of                                                                                                                                                                                                                                  while certain LLM combinations can offer incre-
log PPLW  M (ŝ) (i.e., the mutation-repair mecha-                                                                                                                                                                                                                           mental gains, the effectiveness of Exons-Detect
nism). Removing g(·) corresponds to assigning                                                                                                                                                                                                                                does not hinge on a specific model pairing. Instead,
additional weights as ∆wt = δt , while removing                                                                                                                                                                                                                              the method remains robust across diverse LLM
log PPLW  M (ŝ) refers to performing detection using                                                                                                                                                                                                                        families, and can be further enhanced by selecting
the initial translation score. Overall, both g(·) and                                                                                                                                                                                                                        better LLM pairings.
                                                                                                                                                                                                                                                    26330
                                                                    M4                   Multi-LLM                       Multi-Domain            RealDet
                                           Sensitivity to                                                       Sensitivity to                         Sensitivity to L
                      94



AUROC
                      92

                      90

                      88
                           0.05          0.1          0.15           0.2          0.25      2               5         10      20        50   2        4        8      16   32
                                                                                                                                                              L

                                         Figure 5: Detection performance of Exons-Detect under different parameter settings.


                           BiScope
                           R-Detect
                                               Likelihood
                                               LogRank
                                                                    Fast-DetectGPT
                                                                    Binoculars
                                                                                            IRM
                                                                                            DNA-DetectLLM
                                                                                                                      essary to translate moderate hidden-state discrep-
                     6
                           Entropy             DetectGPT
                                                             5.30
                                                                    Lastde++                Exons-Detect              ancies into effective importance weights.
                     4
                                                                                                                         Reducing L leads to a clear degradation in de-
                                                                                                                      tection performance. For instance, on DetectRL
                     2                                                            1.72
                                                                                                                      under the Multi-LLM and Multi-Domain settings,


Time (s) / Sample
                    1.0

                                                                                                0.78 0.79             reducing L from 32 to 4 results in relative AU-
                                  0.75
                                                                           0.69                                       ROC drops of 1.9% and 3.1%. Across all datasets,
                                                                    0.59                 0.59
                    0.5
                                                                                                                      Exons-Detect consistently achieves its best perfor-
                                         0.30 0.31 0.30                                                               mance when utilizing 32 hidden layers. These re-
                                                                                                                      sults highlight that fully exploiting representational
                           0.05                                                                                       discrepancies across the entire depth of the model
                    0.0
                                                   Detection Methods                                                  is crucial for robust detection.
         Figure 6: Time costs for processing a single sample.                                                         4.6    Efficiency Analysis
                                                                                                                      Faster detection is critical for real-world deploy-
 4.5 Hyperparameter Sensitivity                                                                                       ment and monitoring. Figure 6 compares the per-
This subsection analyzes the impact of both hyper-                                                                    text runtime of all methods. To control for the
parameters (discrepancy threshold θ and mapping                                                                       effect of text length, we sample 1,000 long sam-
slope α) and a structural parameter (hidden layers                                                                    ples from RealDet and truncate each to 300 to-
L) on detection performance. Figure 5 reports the                                                                     kens, reporting the average processing time per text.
detection performance of Exons-Detect under dif-                                                                      Training-based detectors (e.g., BiScope) achieve
ferent parameter settings across multiple datasets.                                                                   the lowest inference latency, but at the cost of sub-
   Overall, Exons-Detect exhibits low sensitivity                                                                     stantial training overhead. Among training-free
to hyperparameter choices, maintaining stable                                                                         methods, classical detectors such as Likelihood are
detection performance across a broad range of                                                                         relatively fast (around 0.3 s per text) since they re-
settings. Specifically, varying either θ or α results                                                                 quire only a single forward pass, but their detection
in performance fluctuations typically within 1.0%,                                                                    accuracy did not meet our requirements. Exons-
while consistently outperforming existing baselines                                                                   Detect and representative baselines (e.g. Binocu-
under all configurations. For the threshold θ, we                                                                     lars) incur two forward passes but still run within
observe that extreme values lead to inferior perfor-                                                                  0.8 s. Within this efficiency regime, Exons-Detect
mance compared to values around θ = 0.15. This                                                                        delivers better detection performance, offering a
behavior is intuitive: overly small thresholds tend                                                                   favorable accuracy-latency trade-off.
to treat most tokens as exonic tokens, excessively
                                                                                                                      5     Conclusion
amplifying noise, whereas overly large thresholds
fail to emphasize informative tokens, diminishing                                                                     This paper proposes Exons-Detect, a novel training-
the benefit of reweighting. For the mapping slope                                                                     free method for AI-generated text detection that
α, performance improves noticeably when α ≥ 10,                                                                       operates by identifying and reweighting exonic
indicating that sufficiently steep mappings are nec-                                                                  tokens. Extensive experiments demonstrate that
                                                                                                                 26331
Exons-Detect consistently achieves SOTA perfor-              On the possibilities of ai-generated text detection.
mance across diverse evaluation settings, while ex-          Preprint, arXiv:2304.04736.
hibiting strong robustness to adversarial attacks         Xin Chen, Junchao Wu, Shu Yang, Runzhe Zhan, Zeyu
and varying input lengths. We hope our work of-             Wu, Ziyang Luo, Di Wang, Min Yang, Lidia S. Chao,
fers new insights for AI-generated text detection           and Derek F. Wong. 2025. Repreguard: Detecting
and plan to further explore token-level contribution        llm-generated text by revealing hidden representation
                                                            patterns. Preprint, arXiv:2508.13152.
modeling to enhance detection performance.
                                                          Elizabeth Clark, Tal August, Sofia Serrano, Nikita
Limitations                                                  Haduong, Suchin Gururangan, and Noah A. Smith.
                                                             2021. All that’s ‘human’ is not gold: Evaluating
Prior studies (Chen et al., 2025) have shown that            human evaluation of generated text. In Proceedings
hidden-state representations may carry signals re-           of the 59th Annual Meeting of the Association for
lated to text provenance. In Exons-Detect, we em-            Computational Linguistics and the 11th International
                                                             Joint Conference on Natural Language Processing
ploy cosine distance to efficiently measure token-          (Volume 1: Long Papers), pages 7282–7296, Online.
level hidden-state discrepancies for assessing token         Association for Computational Linguistics.
importance. We believe that more fine-grained and
                                                          Sebastian Gehrmann, Hendrik Strobelt, and Alexander
more specific discrepancy evaluations could bet-            Rush. 2019. GLTR: Statistical detection and visual-
ter exploit source-related information and lead to          ization of generated text. In Proceedings of the 57th
more accurate detection results, which represents a         Annual Meeting of the Association for Computational
potential direction for further improvement from a          Linguistics: System Demonstrations, pages 111–116,
                                                            Florence, Italy. Association for Computational Lin-
token-level perspective.                                    guistics.
Acknowledgments                                           Biyang Guo, Xin Zhang, Ziyuan Wang, Minqi Jiang, Jin-
                                                            ran Nie, Yuxuan Ding, Jianwei Yue, and Yupeng Wu.
This work is supported by the Postdoctoral Fel-             2023. How close is chatgpt to human experts? com-
lowship Program of CPSF under Grant Number                  parison corpus, evaluation, and detection. Preprint,
GZC20251076, and the National Natural Science               arXiv:2301.07597.
Foundation of China (No.U2336202).                        Hanxi Guo, Siyuan Cheng, Xiaolong Jin, Zhuo Zhang,
                                                            Kaiyuan Zhang, Guanhong Tao, Guangyu Shen, and
                                                            Xiangyu Zhang. 2024a. Biscope: Ai-generated text
References                                                  detection by checking memorization of preceding to-
                                                            kens. In Advances in Neural Information Processing
David Ifeoluwa Adelani, Hao Thi Mai, Fuming Fang,           Systems, volume 37, pages 104065–104090. Curran
  Huy Hoang Nguyen, Junichi Yamagishi, and Isao             Associates, Inc.
  Echizen. 2019. Generating sentiment-preserving
  fake online reviews using neural language models        Xun Guo, Shan Zhang, Yongxin He, Ting Zhang,
  and their human- and machine-based detection. In          Wanquan Feng, Haibin Huang, and Chongyang Ma.
  International Conference on Advanced Information          2024b. Detective: Detecting ai-generated text via
  Networking and Applications.                              multi-level contrastive learning. In Advances in
                                                            Neural Information Processing Systems, volume 37,
Alim Al Ayub Ahmed, Ayman Aljabouh, Praveen Ku-             pages 88320–88347. Curran Associates, Inc.
  mar Donepudi, and Myung Suh Choi. 2021. Detect-
  ing fake news using machine learning : A systematic     Zhiwei Guo, Yu Shen, Ali Kashif Bashir, Muhammad
  literature review. Preprint, arXiv:2102.04458.            Imran, Neeraj Kumar, Di Zhang, and Keping Yu.
                                                            2021. Robust spammer detection using collabora-
Guangsheng Bao, Yanbin Zhao, Juncai He, and Yue             tive neural network in internet-of-things applications.
  Zhang. 2025. Glimpse: Enabling white-box meth-            IEEE Internet of Things Journal, 8(12):9549–9558.
  ods to use proprietary models for zero-shot LLM-
  generated text detection. In The Thirteenth Interna-    Abhimanyu Hans, Avi Schwarzschild, Valeriia
  tional Conference on Learning Representations.            Cherepanova, Hamid Kazemi, Aniruddha Saha,
                                                            Micah Goldblum, Jonas Geiping, and Tom Goldstein.
Guangsheng Bao, Yanbin Zhao, Zhiyang Teng, Linyi            2024. Spotting LLMs with binoculars: Zero-shot
  Yang, and Yue Zhang. 2024. Fast-detectGPT: Effi-          detection of machine-generated text.
  cient zero-shot detection of machine-generated text
  via conditional probability curvature. In The Twelfth   Tatsunori B. Hashimoto, Hugh Zhang, and Percy Liang.
  International Conference on Learning Representa-          2019. Unifying human and statistical evaluation for
  tions.                                                    natural language generation. In Proceedings of the
                                                            2019 Conference of the North American Chapter of
Souradip Chakraborty, Amrit Singh Bedi, Sicheng Zhu,        the Association for Computational Linguistics: Hu-
  Bang An, Dinesh Manocha, and Furong Huang. 2023.          man Language Technologies, Volume 1 (Long and
                                                     26332
  Short Papers), pages 1689–1701, Minneapolis, Min-          Yuchuan Tian, Hanting Chen, Xutao Wang, Zheyuan
  nesota. Association for Computational Linguistics.           Bai, QINGHUA ZHANG, Ruifeng Li, Chao Xu, and
                                                               Yunhe Wang. 2024. Multiscale positive-unlabeled
Yongxin He, Shan Zhang, Yixuan Cao, Lei Ma, and Ping           detection of AI-generated texts. In The Twelfth Inter-
  Luo. 2025. DETree: DEtecting human-AI collabora-             national Conference on Learning Representations.
  tive texts via tree-structured hierarchical representa-
  tion learning. In The Thirty-ninth Annual Conference       Adaku Uchendu, Thai Le, Kai Shu, and Dongwon Lee.
  on Neural Information Processing Systems.                    2020. Authorship attribution for neural text gener-
                                                               ation. In Proceedings of the 2020 Conference on
Xiaomeng Hu, Pin-Yu Chen, and Tsung-Yi Ho. 2023.               Empirical Methods in Natural Language Processing
  Radar: Robust ai-text detection via adversarial learn-       (EMNLP), pages 8384–8395, Online. Association for
  ing. In Advances in Neural Information Processing            Computational Linguistics.
  Systems, volume 36, pages 15077–15095. Curran As-
  sociates, Inc.                                             Yuxia Wang, Jonibek Mansurov, Petar Ivanov, Jinyan
                                                               Su, Artem Shelmanov, Akim Tsvigun, Chenxi White-
Daphne Ippolito, Daniel Duckworth, Chris Callison-             house, Osama Mohammed Afzal, Tarek Mahmoud,
  Burch, and Douglas Eck. 2020. Automatic detec-               Toru Sasaki, Thomas Arnold, Alham Fikri Aji,
  tion of generated text is easiest when humans are            Nizar Habash, Iryna Gurevych, and Preslav Nakov.
  fooled. In Proceedings of the 58th Annual Meeting of         2024. M4: Multi-generator, multi-domain, and multi-
  the Association for Computational Linguistics, pages         lingual black-box machine-generated text detection.
  1808–1822, Online. Association for Computational             In Proceedings of the 18th Conference of the Euro-
  Linguistics.                                                 pean Chapter of the Association for Computational
                                                               Linguistics (Volume 1: Long Papers), pages 1369–
Kalpesh Krishna, Yixiao Song, Marzena Karpinska,               1407, St. Julian’s, Malta. Association for Computa-
  John Wieting, and Mohit Iyyer. 2023. Paraphras-              tional Linguistics.
  ing evades detectors of ai-generated text, but retrieval
  is an effective defense. In Advances in Neural Infor-      Junchao Wu, Runzhe Zhan, Derek F. Wong, Shu Yang,
  mation Processing Systems, volume 36, pages 27469–           Xinyi Yang, Yulin Yuan, and Lidia S. Chao. 2024.
  27500. Curran Associates, Inc.                               DetectRL: Benchmarking LLM-generated text de-
                                                               tection in real-world scenarios. In The Thirty-eight
Runheng Liu, Heyan Huang, Xingchen Xiao, and                   Conference on Neural Information Processing Sys-
  Zhijing Wu. 2025. Zero-shot detection of LLM-                tems Datasets and Benchmarks Track.
  generated text via implicit reward model. In The
  Thirty-ninth Annual Conference on Neural Informa-          Yihuai Xu, Yongwei Wang, Yifei Bi, Huangsen Cao,
  tion Processing Systems.                                     Zhouhan Lin, Yu Zhao, and Fei Wu. 2024. Training-
                                                               free llm-generated text detection by mining token
Eric Mitchell, Yoonho Lee, Alexander Khazatsky,                probability sequences. CoRR, abs/2410.06072.
  Christopher D Manning, and Chelsea Finn. 2023.
  DetectGPT: Zero-shot machine-generated text detec-         Xiaowei Zhu, Yubing Ren, Yanan Cao, Xixun Lin, Fang
  tion using probability curvature. In Proceedings of          Fang, and Yangxi Li. 2025a. Reliably bounding false
  the 40th International Conference on Machine Learn-          positives: A zero-shot machine-generated text detec-
  ing, volume 202 of Proceedings of Machine Learning           tion framework via multiscaled conformal prediction.
  Research, pages 24950–24962. PMLR.                           In Proceedings of the 63rd Annual Meeting of the
                                                               Association for Computational Linguistics (Volume 1:
Guilherme Penedo, Quentin Malartic, Daniel Hesslow,            Long Papers), pages 12298–12319, Vienna, Austria.
  Ruxandra Cojocaru, Alessandro Cappelli, Hamza                Association for Computational Linguistics.
  Alobeidli, Baptiste Pannier, Ebtesam Almazrouei,
  and Julien Launay. 2023. The RefinedWeb dataset            Xiaowei Zhu, Yubing Ren, Fang Fang, Qingfeng Tan,
  for Falcon LLM: outperforming curated corpora                Shi Wang, and Yanan Cao. 2025b. DNA-detectLLM:
  with web data, and web data only. arXiv preprint             Unveiling AI-generated text via a DNA-inspired
  arXiv:2306.01116.                                            mutation-repair paradigm. In The Thirty-ninth An-
                                                               nual Conference on Neural Information Processing
Irene Solaiman, Miles Brundage, Jack Clark, Amanda             Systems.
   Askell, Ariel Herbert-Voss, Jeff Wu, Alec Radford,
   Gretchen Krueger, Jong Wook Kim, Sarah Kreps,
   and 1 others. 2019. Release strategies and the so-        A    Effect Analysis of Exonic Reweighting
   cial impacts of language models. arXiv preprint
   arXiv:1908.09203.                                         Notation. Given a sequence s = {x1 , . . . , xT },
                                                             we define the token-level quantities
Yiliao Song, Zhenqiao Yuan, Shuhai Zhang, Zhen Fang,
   Jun Yu, and Feng Liu. 2025. Deep kernel relative test                     ai ≜ − log PM (xi ),               (11)
   for machine-generated text detection. In The Thir-
   teenth International Conference on Learning Repre-
   sentations.                                                           bi ≜ − PM (xi ) log PM̃ (xi ),         (12)
                                                        26333
and the unweighted global score                                for near-boundary (hard) samples with R0 ≈ τ ,
                                                                          AS
                          T                    T
                                                               we expect B     < τ for AI-generated texts and
       A0                 X                    X               AS
                                                                            S

  R0 ≜    ,        A0 =         ai ,    B0 =         bi .      BS > τ for human-written texts. By (17), this
       B0
                          i=1                  i=1             implies RW − R0 < 0 for AI-generated texts and
                                                 (13)          RW − R0 > 0 for human-written texts, indicating
  Let S = {i : δi > θ} denote the set of exonic                that exon-aware reweighting pushes the score to-
tokens. For each i ∈ S, we assign an additional,               ward the correct side of the decision boundary and
token-specific weight ∆wi > 0 mapped from the                  improves separability.
hidden-state discrepancy δi ; tokens outside S retain
unit weight. We define the corresponding weighted              B        Additional Implementation Details
sums over exonic tokens as
         X                        X                            Regarding the construction of the evaluation
  AS ≜       ∆wi ai ,     BS ≜         ∆wi bi . (14)           datasets, we randomly and uniformly sample 2,000
         i∈S                           i∈S                     text samples from each public benchmark, includ-
The resulting exon-aware translation score is then             ing M4, DetectRL (Multi-LLM and Multi-Domain
given by                                                       settings), and RealDet, ensuring balanced class dis-
                      A0 + AS                                  tributions for experimental evaluation.
                RW ≜             .            (15)
                      B0 + BS                                     During evaluation, the maximum input length is
Score shift under exon-aware reweighting.                      capped at 1024 tokens. All experiments are con-
Since bi > 0 for all tokens, it follows directly that          ducted on a single NVIDIA A100 GPU with 80GB
B0 > 0 and BS > 0. We analyze the difference                   memory. All models are executed using 32-bit
between the reweighted and unweighted scores:                  floating-point precision (FP32).

  R W − R0 =
                A0 + A S
                          −
                             A0                                C        Data Construction in the Robustness
                B0 + BS      B0                                         Experiment
                B0 (A0 + AS ) − A0 (B0 + BS )
             =                                                 In the Polish Attack, we employ GPT-4o to refine
                        B0 (B0 + BS )
                B0 AS − A0 BS                                  texts originally written by humans. The specific
             =                                                 model version and decoding parameters are as fol-
                 B0 (B0 + BS )
                                                             lows:
                    B0 BS        AS      A0
             =                        −       .
                B0 (B0 + BS ) BS         B0                         • GPT-4o Turbo: gpt-4o-2024-11-20, Tem-
                                               (16)                   perature = 1.0, Top-p = 1.0.
As the denominator is strictly positive, we obtain
the following sign equivalence:                                   To ensure that the semantic content and overall
                                                             structure of the original human-written texts re-
           W                  AS
    sign(R − R0 ) = sign          − R0 . (17)                  main largely unchanged, the model is instructed to
                              BS
                                                               perform light polishing only, focusing on improv-
Connection to empirical observations. Figure 2                 ing fluency and expression rather than rewriting or
shows that among tokens with large hidden-state                altering meaning. The input prompt is carefully
discrepancy (δi > θ), the number of tokens that                constructed to enforce this constraint and is speci-
increase class separability substantially exceeds              fied as follows:
the number that decrease it. In addition, the magni-
tudes of the corresponding token-level quantities ai                •    Polish the following human-written
and bi are empirically observed to be of comparable                     text by correcting grammar and
scale, rather than differing by orders of magnitude.                    improving fluency, while ensuring
Taken together, these observations indicate that the                    that the semantic content, author
aggregated exonic ratio                                                 intent, and discourse structure
                        P                                               remain unchanged. The result should
                AS             ∆wi ai
                     = Pi∈S                     (18)                    read more natural but convey exactly
                BS         i∈S ∆wi bi                                   the same meaning as the original text:
is predominantly influenced by tokens that con-                         \n + original human-written text
tribute in a label-consistent direction. Accordingly,
                                                            26334
                 M4           DetectRL Multi-LLM      DetectRL Multi-Domain      RealDet             Avg.
 Detectors
             AUROC     F1     AUROC        F1         AUROC          F1       AUROC      F1      AUROC    F1
                                              Nonlinear mapping
 α = 10      92.43    88.05   90.67       84.95        90.46        86.59     94.98     91.30    92.14   87.72
 α = 20      92.25    87.55   90.87       85.20        90.89        87.05     95.02     91.29    92.26   87.77
                                                  Linear mapping
 α = 10      92.24    87.92   90.90       84.93        91.18        87.24     95.03     91.02    92.34   87.78
 α = 20      91.65    86.63   90.66       84.40        91.68        86.85     95.04     90.66    92.26   87.14

      Table 3: Detection performance (AUROC and F1 score) with different mapping functions (θ = 0.15).

                                  DetectRL Multi-LLM           DetectRL Multi-Domain              Avg.
  Parameter Setting
                                  AUROC        F1              AUROC          F1              AUROC    F1
                                                    Reverse
  L = 2 (θ = 0.15, α = 10)            89.09        84.39           88.24       84.53            88.67    84.46
  L = 4 (θ = 0.15, α = 10)            89.41        85.07           88.38       84.65            88.90    84.86
  L = 8 (θ = 0.15, α = 10)            89.13        84.36           88.56       84.70            88.85    84.53
  L = 16 (θ = 0.15, α = 10)           90.63        85.38           90.55       86.79            90.59    86.09
                                                    Forward
  L = 2 (θ = 0.15, α = 10)            89.09        84.39           88.21       84.41            88.65    84.40
  L = 4 (θ = 0.15, α = 10)            88.98        84.38           87.68       84.12            88.33    84.25
  L = 8 (θ = 0.15, α = 10)            89.13        84.36           87.72       84.21            88.43    84.29
  L = 16 (θ = 0.15, α = 10)           90.20        85.08           89.37       85.52            89.79    85.30

                         Table 4: Detection performance with different hidden layers.


D    Further Exploration of Mapping                       proposed reweighting mechanism is not sensitive
     Functions                                            to the particular form of the mapping employed.
This section further investigates the impact of dif-
ferent mapping functions on detection performance,        E Effect of Hidden-Layer Discrepancies
focusing on a comparison between a linear map-
ping and the default nonlinear mapping. The non-          In the hyperparameter sensitivity analysis, we com-
linear mapping is computed as defined in Eq 6,            pared the impact of extracting hidden-layer discrep-
while the linear mapping is formalized as follows:        ancies across varying numbers of layers, ranging
                                                          from 2 to 32, on detection performance. Build-
               g(δt ) = α (δt − θ)+ .             (19)
                                                          ing upon this analysis, this section further investi-
Under the linear mapping, the additional weight           gates the effect of reverse extraction of hidden-layer
∆wt is constrained within the range (0, α), which         discrepancies, specifically considering differences
results in a steeper scaling behavior compared to         computed from the last layers backward, spanning
the (0, 1) range adopted by the nonlinear mapping.        from 2 to 16 layers.
As reported in Table 3, the experimental results             As reported in Table 4, the experimental results
show that the linear mapping can still achieve com-       show that, for the same number of layers, reverse
petitive performance. In some cases, it even attains      extraction consistently outperforms forward extrac-
a higher average performance than the nonlinear           tion. This observation suggests that discrepancies
counterpart. However, its performance tends to be         derived from higher hidden layers are more in-
less stable across different datasets.                    formative, as they more effectively capture token-
   Overall, these results consistently demonstrate        level importance at the current position. Moreover,
the effectiveness of mapping hidden-state discrep-        these findings indicate the potential benefits of em-
ancies to additional token-level weights. Impor-          ploying more fine-grained and structurally richer
tantly, this effectiveness remains robust to the spe-     strategies for modeling hidden-layer discrepancies,
cific choice of mapping function, indicating that the     which may further enhance detection performance.
                                                      26335
 Setting (L = 16) ↓   θ = 0.05    θ = 0.10    θ = 0.15   θ = 0.20
                                 M4
 α=2                   92.03          92.09    92.23      92.09
 α=6                   91.99          92.06    92.57      92.38
 α = 10                91.89          91.88    92.60      92.50
                          Multi-LLM
 α=2                   89.58     89.64         89.72      89.47
 α=6                   89.59     89.67         90.07      89.54
 α = 10                89.52     89.56         90.20      89.60
                        Multi-Domain
 α=2                   88.57    88.66          88.89      88.64
 α=6                   88.42    88.49          89.27      88.87
 α = 10                88.26    88.18          89.37      88.97
                            RealDet
 α=2                   94.71     94.73         94.78      94.68
 α=6                   94.72     94.79         95.01      94.81
 α = 10                94.68     94.75         95.10      94.88

    Table 5: AUROC under different hyperparameters.


F     Additional Hyperparameter
      Experiments
We conduct additional experiments to further ex-
amine the effects of the hyperparameters α and
θ. Specifically, on public benchmark datasets, we
evaluate detection performance under L = 16
hidden layers, with α ∈ {2, 6, 10} and θ ∈
{0.05, 0.10, 0.15, 0.20}, as summarized in Table 5.
   It is evident that, regardless of the hyperparam-
eter configuration, utilizing hidden-layer discrep-
ancies from only 16 layers consistently underper-
forms the setting with 32 layers. Nevertheless, un-
der the 16-layer configuration, E XONS -D ETECT
remains largely insensitive to variations in both α
and θ, exhibiting only marginal performance fluctu-
ations. Furthermore, an analysis of AUROC score
variations indicates that, for the LLM pair (Falcon-
7B Instruct + Falcon-7B), the optimal hyperparam-
eter combination is α = 10 and θ = 0.15.




                                                                    26336

### Responsible NLP Checklist

Responsible NLP Checklist
Paper title: Exons-Detect: Identifying and Amplifying Exonic Tokens via Hidden-State Discrepancy for
Robust AI-Generated Text Detection
Authors: Xiaowei Zhu, Yubing Ren, Fang Fang, Shi Wang, Yanan Cao, Li Guo
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

  □ A2. Did you discuss any potential risks of your work?
  N/A


        (left blank)

✓ B. Did you use or create scientific artifacts? (e.g. code, datasets, models)
□
 □ B4. Did you discuss the steps taken to check whether the data that was collected/used contains any
  N/A


        information that names or uniquely identifies individual people or offensive content, and the steps
        taken to protect/anonymize it?
        (left blank)

  ✓ B6. Did you report relevant statistics like the number of examples, details of train/test/dev splits, etc.
  □
        for the data that you used/created?
        Appendix B

✓ C. Did you run computational experiments?
□
 ✓ C2. Did you discuss the experimental setup, including hyperparameter search and best-found
 □
        hyperparameter values?
        Section 4.1 and Section 4.5

  □ C3. Did you report descriptive statistics about your results (e.g., error bars around results, summary
  N/A


        statistics from sets of experiments), and is it transparent whether you are reporting the max, mean,
        etc. or just a single run?
        (left blank)

✗
□ D. Did you use human annotators (e.g., crowdworkers) or research with human subjects?
 □ D1. Did you report the full text of instructions given to participants, including e.g., screenshots,
  N/A


        disclaimers of any risks to participants or annotators, etc.?
        (left blank)
The Responsible NLP Checklist used at ACL Rolling Review is adopted from NAACL 2022, with the addition of ACL 2023
question on AI writing assistance and further refinements based on ARR practice. ACL 2026 used a subset of ARR checklist form.
 □ D2. Did you report information about how you recruited (e.g., crowdsourcing platform, students)
 N/A


       and paid participants, and discuss if such payment is adequate given the participants’ demographic
       (e.g., country of residence)?
       (left blank)

 □ D3. Did you discuss whether and how consent was obtained from people whose data you’re
 N/A


       using/curating (e.g., did your instructions explain how the data would be used)?
       (left blank)

 □ D4. Was the data collection protocol approved (or determined exempt) by an ethics review board?
 N/A


       (left blank)

✗
□ E. Did you use AI assistants (e.g., ChatGPT, Copilot) in your research, coding, or writing?
 □ E1. If you used AI assistants, did you include information about their use?
 N/A


       (left blank)

## Extraction verification

- **Beginning checked:** Paper page 1 was rendered and compared with the title, author block, abstract, Figure 1, and opening introduction in the extraction. Checklist page 1 was rendered and compared with its identity, legend, and A-C responses.
- **Middle checked:** Paper page 7 was rendered and compared with Figures 3 and 4, Table 2, Section 4.3.2, and Section 4.4. The malformed figure-label extraction was confirmed as an embedded-font issue rather than missing pages.
- **End checked:** Paper page 13 was rendered and compared with Table 5 and Appendix F. Checklist page 2 was rendered and compared with the remaining D and E responses.
- **Structure checked:** `pdfinfo` reports 13 paper pages and 2 checklist pages. Sections 1-5, Limitations, Acknowledgments, References, and Appendices A-F are present. Tables 1-5, Figures 1-6, equations, captions, prompt text, footnotes, and page ranges were checked against extraction and rendered pages.
- **Known omissions:** none. Figure 3 and Figure 4 labels are garbled in the Markdown text layer, but their rendered content remains complete in the preserved official paper PDF.

## Preserved attachments

| Path | Role in the source | SHA-256 | Preservation / extraction notes |
|---|---|---|---|
| `snapshots/attachments/exons-detect-acl-2026.pdf` | Authoritative ACL proceedings paper | `0e6fa452937be2f8955928cddee586eeb38378fa04d46a300845e1b3fd7cef1d` | Downloaded directly from ACL Anthology; all 13 pages extracted with `pdftotext -layout`; pages 1, 7, and 13 rendered and checked. |
| `snapshots/attachments/exons-detect-responsible-nlp-checklist.pdf` | Authoritative ACL Responsible NLP Checklist | `970dce9d4099c150bb11369e7ae0d557145a5fe0db34b74b9cd373acf9aa2d9b` | Downloaded directly from ACL Anthology; both pages extracted and rendered for checking. |
