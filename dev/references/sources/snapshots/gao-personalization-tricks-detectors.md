# When Personalization Tricks Detectors: The Feature-Inversion Trap in Machine-Generated Text Detection

- **Canonical URL:** https://aclanthology.org/2026.acl-long.1998/
- **Alternate access URLs:**
  - https://aclanthology.org/2026.acl-long.1998.pdf
  - https://aclanthology.org/attachments/2026.acl-long.1998.checklist.pdf
  - https://doi.org/10.18653/v1/2026.acl-long.1998
- **Author / owner:** Lang Gao, Xuhui Li, Chenxi Wang, Mingzhe Li, Wei Liu, Zirui Song, Jinghui Zhang, Rui Yan, Preslav Nakov, and Xiuying Chen
- **Publisher:** Association for Computational Linguistics
- **Published:** July 2026
- **Retrieved:** 2026-07-15
- **Stable identifier:** DOI 10.18653/v1/2026.acl-long.1998; ACL Anthology ID 2026.acl-long.1998
- **Version / revision:** ACL 2026 final proceedings version, pages 43143-43171
- **Extraction method:** First-party ACL proceedings PDF and ACL Responsible NLP Checklist PDF downloaded with `curl`; all 29 paper pages and both checklist pages extracted from embedded text layers with Poppler `pdftotext -layout`; paper pages 1, 15, and 29 and both checklist pages rendered with `pdftoppm` and visually compared with the extraction
- **Full-text status:** complete for the proceedings paper and its authoritative two-page Responsible NLP Checklist
- **Access and transformation notes:** The preserved text below contains the complete 29-page paper extraction followed by the complete two-page checklist extraction. The paper includes tables, figure captions, footnotes, limitations, ethical considerations, references, appendices, prompt text, and long human and machine examples. Multi-column reading order, line-break hyphenation, mathematical layout, and literal `\\n` sequences in generated examples reflect `pdftotext -layout`. No OCR was used. Figure geometry, colors, and exact typographic placement remain in the preserved PDF. The cited GitHub repository was not used as evidence and was not recursively ingested.

## Full text

                       When Personalization Tricks Detectors:
           The Feature-Inversion Trap in Machine-Generated Text Detection
                   Lang Gao1 , Xuhui Li1 , Chenxi Wang1 , Mingzhe Li2 , Wei Liu3 ,
               Zirui Song1 , Jinghui Zhang1 , Rui Yan4 , Preslav Nakov1 , Xiuying Chen1 *

                                           MBZUAI 2 ByteDance
                                                  1

                             National University of Singapore 4 Wuhan University
                              3

                        {Lang.Gao, Preslav.Nakov, Xiuying.Chen}@mbzuai.ac.ae

                            Abstract                                      Personalized                   General

         As large language models (LLMs) increasingly                  MGT           HWT            HWT            MGT
         imitate personal writing styles, personaliza-
         tion has become a key challenge for machine-                                                   Feature Value
         generated text (MGT) detection. Yet personal-
         ized MGT detection remains largely underex-
         plored. In this work, we introduce StyloBench,                                    Inverted
         the first benchmark for evaluating detector ro-                                     Diffs
         bustness under personalization, built from lit-
         erary and blog texts paired with their LLM-
         generated imitations. Experiments across di-              Figure 1: Illustration of the feature-inversion trap. The
         verse detectors show pronounced performance               feature values of HWT/MGT exhibit inverted differ-
         instability under personalization, with frequent          ences across domains.
         inversions relative to general-domain behavior.
         To better understand this limitation, we conduct
                                                                   as LLMs may generate fake news and misinforma-
         an in-depth analysis and attribute it to a feature-
         inversion trap, i.e., features that are effective         tion (Tian et al., 2025). Moreover, style imitation
         for separating human-written text (HWT) from              can be misused, for instance, by impersonating
         MGT in general flip their effect in personal-             public figures or creating fake work (Herbold et al.,
         ized contexts, ultimately misleading detectors.           2024). These risks make machine-generated text
         Motivated by this, we propose StyloCheck, a               (MGT) detection increasingly important. Although
         diagnostic framework for predicting detector              existing studies have made progress in general-
         robustness under personalization. StyloCheck              domain detection, it remains unclear how well they
         identifies the inverted features and quantifies
                                                                   perform in personalized domains. Hence, we in-
         detector dependence using perturbed texts pro-
         nounced in the features. In our experiments,              troduce StyloBench, the first benchmark for MGT
         StyloCheck predicts both the direction and                detection in personalized settings. StyloBench
         magnitude of cross-domain performance shifts              covers two sub-scenarios: Literary works and Blog
         with an 85% correlation to actual outcomes.               posts, each paired with LLM-generated imitations.
         We hope this work will raise awareness of the             Interestingly, experiments on StyloBench show
         structural risks introduced by personalization            that personalization can noticeably degrade detec-
         and motivate more robust approaches to person-
                                                                   tor performance. Moreover, on the Literary subset,
         alized MGT detection.  Github.
                                                                   many detectors exhibit prediction inversion, where
    1    Introduction                                              predictions tend to shift opposite to the expected
                                                                   direction, suggesting weakened or even flipped dis-
    Large Language Models (LLMs) have achieved                     criminative cues under highly personalized text.
    strong text generation performance (Huang et al.,
                                                                      In order to explore why detectors fluctuate un-
    2025), with increasing capability of mimicking per-
                                                                   der personalization, we train a domain classifier on
    sonalized language styles in tasks such as news
                                                                   human-written texts (HWT) from general and per-
    writing, style imitation, and story generation (Tu
                                                                   sonalized domains, and test it on both HWT/MGT
    et al., 2024; Wang et al., 2025). However, these
                                                                   in the two domains to see, across domains, whether
    capabilities also raise security and ethical concerns,
                                                                   domain features fluctuate similarly. The classifier
        * Corresponding author.                                    exhibits a clear inversion: In the general domain,
                                                               43143
Proceedings of the 64th Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers), pages 43143–43171
                                 July 2-7, 2026 ©2026 Association for Computational Linguistics
MGT is predicted to be more “general” than HWT;          features they rely on. (3) We propose StyloCheck,
however, in the personalized domain, MGT is in-          which estimates both the direction of change and
stead classified as more “personalized” than HWT.        the magnitude of performance variation of a detec-
   This has given rise to our feature-inversion trap     tor under personalized scenarios. It serves as an
hypothesis, namely that features that are effective      early warning signal without requiring large-scale
for separating HWT from MGT in general flip their        testing. The estimation shows high reliability and
effect in personalized contexts, ultimately mislead-     strong consistency with actual performance, with
ing detectors. In order to identify where this inver-    Pearson correlation exceeding 0.85.
sion is most pronounced, we formalize the search
for the strongest inversion as a Rayleigh quotient       2     Related Work
problem (Dong et al., 2024) and exploit its extremal
                                                         2.1    MGT Detection
property to obtain the inverted feature direction.
Feature directions derived from different datasets       Several benchmarks have been developed for eval-
exhibit high cosine similarity, closely aligned with     uating the performance of HWT vs. MGT de-
domain classifier weights and far from those of          tection across different domains, generators, and
HWT/MGT classifiers. Projecting samples onto             languages, e.g., MGTBench (He et al., 2024),
these feature directions yields scalar feature values,   M4 (Wang et al., 2024b), M4GT-Bench (Wang et al.,
as shown in Figure 1, which reveal a clear inver-        2024a) and RAID (Dugan et al., 2024). More-
sion effect: within each dataset, the HWT–MGT            over, several domain-specific benchmarks, includ-
feature value difference is negatively correlated        ing WetBench (Quaremba et al., 2025) and Multi-
with detector performance. This suggests that the        Social (Macko et al., 2025), have focused on spe-
“feature-inversion trap” is a stable, cross-domain       cialized contexts such as Wikipedia and social me-
phenomenon akin to stylistic differences, and that       dia. However, none of them has looked into eval-
detector failures are partly driven by reliance on       uating MGT detection in highly personalized or
these inverted features.                                 stylistically consistent text.
   Based on this finding, we propose StyloCheck,            MGT detection methods fall into two main cate-
an effective approach to predict the detector’s          gories: training-based and training-free (Xu et al.,
performance changes in personalized scenarios.           2025a). Training-based methods treat detection
Given a detector, StyloCheck evaluates it on probe       as supervised classification, usually by fine-tuning
datasets constructed with token-level perturbations      pretrained encoders such as RoBERTa (Liu et al.,
that remove semantics, style, and basic HWT/MGT          2019), or by using improved frameworks and archi-
features while preserving inverted-feature differ-       tectures (Guo et al., 2024; Tian et al., 2024; Jiao
ences. The resulting performance reflects the de-        et al., 2025). Training-free methods rely on explicit
tector’s reliance on inverted features: higher per-      textual or probabilistic cues, including geometric
formance on probe datasets indicates stronger re-        and probabilistic signals (Bao et al., 2024; Xu et al.,
liance on these features. We test seven detectors        2025a), token distributions (Su et al., 2023b), topo-
on 100 probe datasets and find that the Pearson          logical features (Tulchinskii et al., 2023; Wei et al.,
correlation between StyloCheck’s outputs and the         2025), and human-assistive indicators (Gehrmann
actual cross-domain performance gaps exceeds 0.7         et al., 2019; Russell et al., 2025). However, existing
in 90% of the cases, and consistently stays above        studies have not addressed or evaluated personal-
0.85. This shows that StyloCheck reliably predicts       ized or highly stylistically adaptive scenarios.
both the direction and the magnitude of transfer
performance changes, with higher reliability as the      2.2    Personalized LLM Generation
number of probe datasets increases.                      Personalization of LLMs has recently become in-
   Our contributions are as follows: (1) We build        creasingly important (Zhang et al., 2025c). Per-
StyloBench, the first benchmark for MGT detec-           sonalization methods have developed into two
tion in personalized scenarios, and uncover drastic      main approaches: (i) Prompt-based personaliza-
performance declines and even reversals in existing      tion drives LLMs toward users’ traits via per-
detectors. (2) We identify the Feature-Inversion         sonalized prompts (Tseng et al., 2024). Some
Trap, a systematic shift between general and styl-       work designed retrieval (Mysore et al., 2024) and
ized domains, and show that this phenomenon can          agent frameworks (Zhang et al., 2025b) to achieve
fundamentally undermine detectors by inverting the       deeper imitation. (ii) Training-based personaliza-
                                                    43144
    Subset           Stylo-Literary   Stylo-Blog         has more than five long-form works. As some arti-
    Domain               Article          Blog           facts in the texts are not original content, but rather
    Generator Size       ≤ 14B           ≥ 70B           formatting or source information, we clean the texts
    Method                CPT          Prompting
    Generators             3               4
                                                         to keep only the original content (see Appendix A.3
    Subdomains             7               1             for more detail). Then, we split each author’s texts
    Examples             21,000          4,000           into 512-token segments. For each author, we ran-
    Sample Length     ≤ 512 tokens    ≤ 512 tokens
                                                         domly select 1,000 segments as HWTs in the test
Table 1: Statistics about StyloBench. CPT: Continuous    set, and up to 3,000 additional segments as the
Pretraining.                                             training set. For MGT, we apply Continuous Pre-
                                                         training (CPT, Shi et al., 2024) of LLMs on the
tion adapts user traits via instruction tuning (Woź-    training set to achieve deeper personalized imita-
niak et al., 2024; Liu et al., 2025), or through self-   tion. We train three LLMs in their base versions:
supervised learning for dynamic adaptation (Men-         Qwen3-4B (Team, 2025), Llama-3.1-8B (Dubey
doza et al., 2024). This often yields stronger and       et al., 2024), and Phi-4 (14B, Abdin et al., 2024).
more persistent stylistic alignment. However, such       We update only one LoRA (Hu et al., 2022) layer
personalization ability of LLMs raises concerns,         to reduce the training cost and to speed up learning.
including the possibility for political imperson-        After training, we take the first 30 tokens of each
ation (Herbold et al., 2024) and copyright infringe-     HWT test sample as the input and let the LLM con-
ment (Zhang et al., 2025a; Karamolegkou et al.,          tinue the text. The selected hyperparameters and
2023). This underscores the need for personalized        other generation details are in Appendix A.5.
MGT detection. However, to the best of our knowl-
                                                         3.1.2 Stylo-Blog
edge, no prior work has systematically studied the
problem of personalized MGT.                             In the blog scenario, the HWTs come from Blog-
                                                         1K 1 , a high-quality subset of the Blog Authorship
3    StyloBench                                          Corpus (Schler et al., 2006). Blog-1K contains mul-
                                                         tiple posts grouped by 1,000 human authors. We
To investigate the performance of existing MGT           further introduce the data source in Appendix A.4.
detection methods in personalized scenarios, we          We randomly select 1,000 posts, each truncated to
create StyloBench, the first benchmark for MGT           a maximum length of 512 tokens, as HWT exam-
detection under personalized conditions. This            ples in the test set, and the corresponding MGTs
dataset has two subsets representing two scenarios:      are generated by LLMs. For each blog post, we ap-
(i) Stylo-Literary, simulating personalization in        ply a few-shot prompting template using 1–3 other
literary works, and (ii) Stylo-Blog, simulating          posts by the same author as examples to guide the
personalization in blogs. Table 1 gives some statis-     model in imitating the author’s style. The generator
tics about these datasets. We provide a detailed         continues from the first 30 tokens of the given post,
discussion about motivation for dataset scenario         producing text with approximately the same length
selection, model selection, and dataset scale and        as the original. We use four popular large-scale
diversity in Appendix A.1.                               LLMs as generators: GPT-4o (OpenAI et al., 2024),
                                                         Claude-4-Sonnet (Claude-4) (Anthropic, 2025b),
3.1 Dataset Construction                                 Claude-3.7-Sonnet-Latest (Claude-3.7) (Anthropic,
3.1.1 Stylo-Literary                                     2025a), and Qwen2.5-72B (Team, 2025). The full
In the article scenario, HWTs consist of excerpts        generation details are in Appendix A.4 and A.5.
from literary works, while MGTs are generated            3.2      Evaluation Setup
by LLMs trained to learn and imitate the authors’
styles. Concretely, for HWT, we use data from the        Evaluation Datasets Apart from StyloBench
Gutenberg Book Corpus (Gerlach and Font-Clos,            for personalized scenarios, we also evaluate on an
2020), an open-source collection of books grouped        English subset of M4 (Wang et al., 2024b), to show
by authors. We selected seven authors: Jane Austen       the MGT detectors’ performance in a general setup.
(J.A), Charles Dickens (C.D), Fyodor Dostoyevsky         The English subset of M4 spans diverse sources, and
(F.D), Plato (P.L), Bernard Shaw (B.S), Jonathan         contains MGTs from four generators: ChatGPT,
Swift (J.S), and Mark Twain (M.T). These authors         Cohere, text-davinci-003 (Davinci), and BLOOMz,
are well known for their distinctive styles and each         1
                                                                 https://zenodo.org/records/7455623

                                                     43145
                                   M4(General)                           Stylo-Blog                       Stylo-Literary
            Generator
                        Cohere ChatGPT Davinci BLOOMZ Qwen2.5-72B Claude-4 Claude-3.7 GPT-4o Llama3.1-8B       Phi-4   Qwen3-4B
 Detector
 Entropy                31.83   26.35    40.10    41.33    13.02         36.57    34.08       63.43   55.23    51.92       76.18
 Lastde                 97.69   97.48    83.70    88.03    92.69         68.58    50.96        6.67   69.88    65.67       62.57
 Lastde++               98.22   98.67    84.41    80.91    99.07         83.37    88.27       58.41   60.38    47.57       39.78
 Log-Likelihood         93.12   93.76    72.79    59.75    95.27         72.30    77.29       41.65   36.59    30.94        9.23
 LogRank                94.21   94.94    73.18    69.42    95.61         71.31    75.37       34.89   38.53    32.60       10.44
 Detect-LRR             94.88   96.13    74.03    84.34    94.85         67.16    66.99       20.26   45.73    40.62       19.43
 Fast-DetectGPT         98.78   98.99    85.28    55.01    99.47         84.60    89.43       57.57   33.22    18.47        8.71
 Avg.                   86.96   86.62     73.36   68.40    84.28         69.13        68.91   40.41   48.51    41.11       32.33


Table 2: Performance of MGT detectors, grouped by generator: shown is AUROC given one generator. Blue :
higher AUROC; green : lower AUROC.


with ∼3,000 MGTs per source–generator pair. We                     shift: Detectors exhibit divergent trends; for in-
further explain the data source and give more statis-              stance, while Entropy improves from 31.83% in
tics in Appendix A.6.                                              M4 to 76.18% in Stylo-Literary, Lastde drops
                                                                   from 97.69% to 62.57%. (3) Systematic and ab-
Baselines & Evaluation We evaluate seven rep-                      normal inversions: Many detectors experience dra-
resentative training-free detectors, which achieve                 matic flips, with AUROC for methods like Fast-
strong MGT detection performances in general do-                   DetectGPT falling as low as 8.71%, indicating a
main: Log-Likelihood (Solaiman et al., 2019), Lo-                  near-complete reversal of discriminative capability.
gRank (Solaiman et al., 2019), DetectLRR (Su                       (4) Increased instability in complex styles: Fluctu-
et al., 2023a), Entropy (Gehrmann et al., 2019;                    ations are more pronounced on Stylo-Literary
Ippolito et al., 2020), Fast-DetectGPT (Bao et al.,                than on Stylo-Blog, with abnormal reversals oc-
2024), Lastde and Lastde++ (Xu et al., 2025a).                     curring more frequently. These observations sug-
Details are provided in Appendix B.1. We use                       gest that existing MGT detectors may be highly
AUROC as the evaluation metric following prior                     unstable in personalized scenarios. When gener-
work (Xu et al., 2025a; Bao et al., 2024).                         ators effectively imitate specific styles, detector
   We mainly focus on training-free MGT detec-                     performance tends to shift unpredictably or even
tors because they rely on a small set of explicit text             reverse entirely. Detailed per-domain performance
features, making performance changes easier to                     analyses are provided in Appendix D.1.
interpret as feature shifts across domains. Training-
based detectors learn more complex representations                 4     The Feature-Inversion Trap
influenced by data and model factors, so their be-
havior is harder to attribute to specific textual prop-            Building on the observed instability in personalized
erties. However, we also include experiments for                   scenarios, we next analyze its mechanism. In §4.1,
training-based methods in Appendix B.3. We use                     we introduce the feature-inversion trap hypothesis;
AUROC to measure the overall performance of an                     in §4.2, we extract the most salient inverted feature
MGT detector, as detailed in Appendix C.1.                         vector to verify this hypothesis; and in §4.3, we
                                                                   demonstrate its generality across datasets.
3.3 Main Results
                                                                   4.1    Feature-Inversion Trap Hypothesis
Table 2 presents the performance of various detec-
tors across datasets. We report the average AUROC                  Probing Method To analyze the differences be-
for each generator across all subdomains, with                     tween HWT and MGT, we require a representation
full experimental results detailed in Appendix B.2.                space that effectively captures semantic and stylis-
The last row shows the average AUROC for each                      tic features. Prior work has shown that the hidden
generator across all baselines. The results re-                    space of pretrained language models often encodes
veal four primary findings: (1) Significant per-                   diverse linguistic and stylistic properties along ap-
formance degradation occurs in personalized set-                   proximately linear directions (Mikolov et al., 2013).
tings. Average AUROC on M4 (above 85%) falls                       Based on this insight, we adopt GPT-2 (Brown
sharply on stylized datasets, dropping to as low                   et al., 2020) as a proxy model, using activations
as 32.33% on Stylo-Literary—worse than ran-                        from its different modules as feature representa-
dom guessing. (2) High variance under domain                       tions. We examine all modules of GPT-2, including
                                                           43146
    1.0
                                                                                               Personalized




                                                            Domain Classifier Scores
                                                                                               General




                                                                                                                                    Feature Values on w
                                                                                       20                                       20
    0.9
                                                                                        0                                       0

AUROC
    0.8
                                                                                       20                                           20

    0.7
                Residual           Attention       MLP                                 40                                           40
                Personalized       General
    0.6                                                                                     HWT MGT HWT MGT HWT MGT HWT MGT
          0     2         4        6           8   10                                              (a)             (b)
                               Layer
                                                                 Figure 3: (a) Domain classifier score distribution: We
 Figure 2: AUROC scores of MGT classifiers across                can see moderate inversion effects. (b) Feature value
 modules in two domains. The colors denote mod-                  distributions on the inverted feature direction w⋆ : we
 ules, and the line styles denote domains. We can see            can see a major inversion effect.
 that the deep residual layers are best at distinguishing
 HWT/MGT in both domains.                                        trap hypothesis: distinguishable MGT features in
                                                                 general domain are inverted under personalization.
 attention layers, MLP layers, and residual streams.
 For each module, we extract the activation of the               4.2 Verification of the Feature-Inversion Trap
 last token as the text representation and train a lo-           In order to verify the existence of the feature-
 gistic regression classifier to distinguish HWT from            inversion trap, we aim to identify the most represen-
 MGT in general and personalized domains. Fig-                   tative inverted feature direction. If the projection of
 ure 2 reports the AUROC for each module. Deep                   datasets in this direction is highly correlated with
 residual streams consistently achieve high AUROC                detector performance, it would suggest that detec-
 across the two domains, indicating that they retain             tors rely on it, thereby supporting our hypothesis.
 strong discriminative features. Therefore, we fo-
 cus on the residual stream at a near-final layer, i.e.,         4.2.1 Deriving the Inverted Feature Direction
 layer 10, in the following analysis.                            We begin by extracting the inverted feature direc-
                                                                 tion that is most responsible for this effect, in order
Probe Datasets We construct two small probe                      to assess its correlation with detector performance.
datasets. Following (Xu et al., 2025a), we adapt
Xsum (Narayan et al., 2018) and their LLM-                       Notation We denote the general-domain dataset
generated continuations as the general-domain data.              by G and the personalized-domain dataset by S.
We randomly sample 150 texts from the J.A subset                 Let g+ , g− ∈ G and s+ , s− ∈ S represent MGT
of Stylo-Literary and take their Phi-4 MGTs as                   and HWT activations in the two domains. For each
personalized-domain data. Each domain contains                   quadruple (g+ , g− , s+ , s− ), we compute domain-
150 HWT and 150 MGT samples.                                     specific difference vectors:

Visibility of the Inverting Trend Since the de-                                               vG = g+ − g− ,   vS = s+ − s− .        (1)
tector’s performance fluctuates under domain shift,
we first investigate whether the representations                Inversion-Value Matrix and Object Our goal
themselves encode domain differences. Follow-                   is to find a direction w where the projection of
ing (Gao et al., 2025), we train a logistic regression-         vG is opposite to that of vS . For each quadruple
style domain classifier, whose weight direction                 (g+ , g− , s+ , s− ), we define the projection product
serves as domain-related features, to distinguish               in direction w as
general HWT from personalized HWT, and then
evaluate it on HWT/MGT samples in both domains.                             qi (w) = (w⊤ vG )(w⊤ vS ) = w⊤ (vG vS⊤ )w. (2)
Figure 3(a) shows a clear separation of the pro-
                                                                 Since for any matrix M, it holds that w⊤ Mw =
jection onto the weight direction (feature values)
                                                                 w⊤ 21 (M + M⊤ )w, Equation 2 can be rewritten as
between the two domains, as expected. We also ob-
serve an unexpected pattern: in the general domain,                                                    
                                                                         qi (w) = w⊤ 12 vG vS⊤ + vS vG
                                                                                                     ⊤ w.     (3)
the feature value of MGT is slightly lower than that
of HWT, whereas in the personalized domain, it is                Further details on the calculation of Equation 2
slightly higher. This leads to the feature-inversion             and 3 are in Appendix C.3. For each quadruple, we
                                                         43147
           0.57 0.5804                                                          4.2.2    Correlation with Detector Performance
           0.76
                                                                                Deriving the inverted feature direction w⋆ reveals a
           0.78            -0.7740
           0.80                                                                 dimension where MGT and HWT roles flip across

Spearman
           0.82                                                                 domains, but this alone does not confirm its effect
           0.84                    -0.8265                                      on detectors. To establish the connection, we eval-
                                           -0.8415 -0.8468
           0.86                                            -0.8551              uate the correlation between the strength of the
                                                                   -0.8651
           0.88                                                                 inverted feature and detector performance.
                    o p y stde ood ++ ank RR                        PT
              Ent
                  r      La ikelih astde LogR tect-L etectG                        Intuitively, along w⋆ , the relative positions of
                             -L      L             De ast-D
                         Log                            F                       HWT and MGT feature values in the two domains
                                                                                are inverted. We quantify this property using fea-
  Figure 4: Spearman ρ between feature value differences                        ture value difference. For a dataset M with its
  of datasets and corresponding detector performance.
                                                                                MGT denoted as m+ and HWT as m− , the feature
                                                                                value difference is
  define a cross-domain matrix
                                                                                                   P                            
                                                                                   D(M, w⋆ ) =   {m+ ,m− }⊂M       m⊤  ⋆   ⊤ ⋆
                                                                                                                      + w − m− w ,   (7)
               Ai = 21 vG vS⊤ + vS vG
                                    ⊤ ,                                  (4)
                                                                                which reflects the overall discrepancy between
 which is symmetry. Aggregating over all quadru-                                MGTs and HWTs on the inverted feature. Larger
 ples yields                                                                    values indicate a clearer separation, while smaller
                      P                                                         or flipped values suggest confusion between the
                  A = i Ai .                 (5)
                                                                                two classes. Following the experimental design
 The overall inversion objective can then be ex-                                in §3.2, we partition M4 and StyloBench by unique
 pressed as                                                                     generator–subfield combinations, resulting in a to-
                                                                                tal of N = 45 subsets. For each subset, we com-
                     P
       R(w) =           i qi (w) = w
                                        ⊤ Aw,       s.t. ||w|| = 1.      (6)    pute D(·, w⋆ ), forming a set {Di }Ni=1 . Meanwhile,
                                                                                for each MGT detector, we collect the AUROCs
  Since each Ai is symmetric, the aggregated matrix                             on the same subsets, denoted as {AUROCi }N        i=1 .
  A in Equation 5 is also symmetric. So far, we                                 We measure their consistency by Spearman corre-
  have transformed the problem into the Rayleigh                                lation: ρ = Spearman {Di }, {AUROCi } . The
  quotient of A with respect to w under the unit-norm                           resulting correlations ρ for each detector are shown
  constraint. Illustrations on the Rayleigh quotient                            in Figure 4. We can see that entropy exhibits a
  problem are available in Appendix C.3.                                        positive correlation (∼ 0.6), whereas all other de-
                                                                                tectors have ρ < −0.77, indicating strong negative
 Solution By the property of the Rayleigh quo-                                  correlations. We further show the distribution of
 tient, minimizing the objective in Equation 6 re-                              {AUROCi } versus {Di } of each detector in Ap-
 duces to: w⋆ = arg min|w|=1 R(w), whose solu-                                  pendix D.2. Overall, these results demonstrate that
 tion is the eigenvector of A corresponding to its                              the detector’s performance is tightly linked to a
 smallest eigenvalue: A = U ΣU ⊤ , w⋆ = U [:                                    feature inverted across domains.
 , −1], where U [:, −1] denotes the last column of                                 To verify that this correlation is not spurious,
 U , associated with the minimum eigenvalue. This                               we further conduct experiments that isolate the ef-
 w⋆ represents the inverted feature direction, i.e.,                            fects of inverted features. We evaluate detectors on
 the axis along which the HWT–MGT projection                                    randomized text lacking semantic content, where
 (feature value) difference in the general domain                               positive and negative samples are separated along
 is most strongly inverted in the personalized do-                              the inverted direction, an orthogonal direction, or
 main. Using the probe datasets in §4.1, we show                                at random. Detectors only show strong discrimi-
 the feature value distributions of four sample types                           nation under the first case, indicating their direct
 on w⋆ in Figure 3(b). In the personalized domain,                              reliance on inverted features (Appendix D.3).
 the MGT feature values are clearly lower than for
 HWT, while in the general domain, the MGT ones                                 4.3     Generality of the Feature-Inversion Trap
 are clearly higher than HWT’s. This flip in relative                           Having verified that w⋆ captures a key inverted
 positions provides direct evidence of the feature-                             feature correlated with performance, we now inves-
 inversion phenomenon.                                                          tigate whether this phenomenon is dataset-specific
                                                                             43148
                                                                      (a)                          (b)

            (a)                         (b)              Figure 6: (a) Changes of feature values under different
                                                         levels of token shuffling. Shuffling brings consistent
Figure 5: (a) |CosSim| between feature directions from
                                                         change in feature value. (b) Distribution of feature val-
different datasets. w⋆ are close to WDomain and beyond
                                                         ues in the probe dataset. Two classes share zero overlap.
WMGT . (b) AUROC distributions of the generalization
test. WDomain has evidently better generalizability.
                                                         5     StyloCheck
                                                         General MGT detectors suffer from the feature-
or reflects a broader, cross-domain pattern. To          inversion trap, leading to unreliable performance in
this end, we evaluate the consistency of inverted        personalized domains. In this section, we propose
features across multiple datasets. We processed          StyloCheck, an automatic transferability estimator
Stylo-Literary and M4 as follows. For each               that predicts such performance shifts by quantify-
subdomain–generator pair in M4, we create five           ing detectors’ dependence on inverted features.
subsets, each with 150 random HWTs and 150
MGTs, as general-domain probe datasets. We ap-           5.1    Design of StyloCheck
ply the same procedure to Stylo-Literary to ob-          5.1.1 Probe Dataset Synthesis
tain personalized-domain probe datasets.                 To construct probe datasets that differ only in
                                                         inverted features, we eliminate confounding fac-
   Each experiment samples one general subset and        tors from text semantics, domain, and class
one personalized subset. We then extract three fea-      (HWT/MGT) by shuffling tokens. To control shuf-
ture directions: (1) the inverted feature direction      fle strength, we use Kendall’s τ , a measure of se-
w⋆ , (2) the MGT feature direction WMGT , and (3)        quence order ranging from 1 to −1, correspond-
the domain feature direction WDomain . To obtain         ing to a gradual inversion of token order (see Ap-
these two reference directions, we train logistic re-    pendix C.2). For each sentence, we generate vari-
gression models. One model separates HWT and             ants with Kendall’s τ spanning this range. As
MGT and gives WMGT . The other separates gen-            shown in Figure 6(a), both Kendall’s τ and the
eral and personalized data and gives WDomain . We        corresponding feature values vary continuously.
repeat this process 100 times and produce 100 sets          Therefore, we build probe datasets by shuffling
of the three types of vectors. We then compute           tokens. We sample one general and one person-
cosine similarity within each group. Figure 5(a)         alized HWT, generate 800 variants for each with
shows that WMGT has low similarity with a mean           different Kendall’s τ , merge them, and select the 50
of 0.163. WDomain and w⋆ show higher stability           samples with the highest feature values as positives
with means of 0.475 and 0.547. We also test how          and the 50 lowest as negatives. As shown in Fig-
WMGT and WDomain generalize to new subsets.              ure 6(b), the resulting feature value distributions
Figure 5(b) shows that WDomain keeps a high AU-          show no overlap. We further evaluate the style and
ROC in other subsets with a mean of 0.994, while         MGT linear classifiers introduced in §4.1, which
WMGT varies more widely from 0.4 to 0.8 with             achieve near-perfect accuracy during training but
a mean of 0.757. The strong similarity between           drop to 53% and 66% AUROC on the probe dataset,
WDomain and w⋆ indicates that inverted features          respectively, confirming the effective removal of
share the same high generalization ability.              domain and class features. The probe dataset thus
                                                         reflects only differences in the inverted features.
  Based on these observations, we conclude that
the feature-inversion trap is a widespread phe-          5.1.2 Transferability Evaluation
nomenon between personalized and general do-             We next describe how the detector performance on
mains, and the inverted features share strong com-       the probe dataset reveals its transferability. Our
monalities across various datasets.                      evaluated detectors treat MGTs as positive samples.
                                                     43149
                                                         inverted features and also captures how strong that
                                                         dependence is. We add an ablation study on the
                                                         number of probe datasets in Appendix D.4.

                                                         6   Discussion
                                                         In this section, we address several conceptual ques-
                                                         tions raised by the observed mechanism, with em-
                                                         pirical evidence deferred to Appendix E.
                                                         (i) Is the feature-inversion trap a typical
                                                         out-of-distribution (OOD) effect? The feature-
                                                         inversion trap is a special case of OOD, marked by
                                                         two points: It aligns with the inverted feature direc-
Figure 7: Top: Pearson r between transfer gaps and AU-
                                                         tion, and it often causes a reversal of detector behav-
ROCs. Bottom: corresponding AUROCs of detectors
in probe datasets. Percentages of experiments groups     ior rather than simple degradation. Appendix E.1
where r > 0.7 and r > 0.5 are marked.                    shows that common OOD do not produce these
                                                         patterns. Appendix E.2 also outlines its links to
In both the general domain and the probe dataset,        related terms such as spurious correlations.
positive samples tend to exhibit higher feature val-
                                                         (ii) What do inverted features capture? Our ev-
ues. Therefore, if a detector relies on the inverted
                                                         idence shows that they relate to text diversity. Many
feature, it should perform well on the probe dataset.
                                                         training-free detectors (Xu et al., 2025a; Gehrmann
AUROC reflects the degree of reliance on inverted
                                                         et al., 2019) assume that HWT is more diverse
features: high values indicate strong dependence
                                                         than MGT, but personalization breaks this pattern:
and likely degradation after transfer, low values (be-
                                                         personalized MGT can be more varied and less co-
low 0.5) suggest inverted dependence and potential
                                                         herent. This shift is consistent with the latent we
performance gains, and values near 0.5 imply weak
                                                         observe and helps explain the negative performance
dependence and stable transfer.
                                                         flips of these detectors. See Appendix E.3.
5.2 Performance of StyloCheck                            (iii) How can we mitigate the feature-inversion
To evaluate the performance of StyloCheck, we            trap? A practical option is to use tuned training-
test it on all seven MGT detectors and examine           based detectors. They learn more cues and can
whether it reflects their performance changes be-        reach strong in-domain accuracy after training
fore and after transfer.                                 on personalized text, though their cross-domain
                                                         generalization remains limited, as shown in Ap-
Evaluation Setup. We construct 100 probe                 pendix E.4. For training-free detectors, using fea-
datasets from M4 and Stylo-Literary. In each             tures less sensitive to style drift, such as stable traits
experiment, we randomly choose five of them for          of human writing, may reduce reliance on diversity
testing, and we compute the mean AUROC. We               signals. Adaptive thresholding (Jung et al., 2025)
then measure the Pearson r between this mean AU-         that adjusts to the stylization can also improve ro-
ROC and the detector’s overall performance gap           bustness in personalized settings.
between M4 and Stylo-Literary. The results of
over 100 such experiments are shown in Figure 7.         7   Conclusion and Future Work
Results. Figure 7 shows the AUROC of all de-             We presented StyloBench, the first dataset for
tectors across experiments. Two patterns appear.         MGT detection in personalized scenarios. Our
(1) Entropy stays below 0.5 in all runs, showing         study showed that existing detectors face large per-
inverted reliance, while all other detectors remain      formance shifts, and even inversion, after domain
above 0.5, showing positive reliance. This matches       transfer. We traced this to the feature-inversion
their transfer behavior, where Entropy improves,         trap, where features that separate MGT and HWT
and others degrade. (2) In 90% of runs, Pearson          change their roles across domains and lead detec-
r exceeds 0.5, and in 78% it exceeds 0.7, indicat-       tors to flip predictions. Based on this, we proposed
ing stable reliance levels. These results show that      StyloCheck, a transferability framework that mea-
StyloCheck identifies detectors’ dependence on           sures how much detectors rely on inverted features.
                                                    43150
   In future work, we plan to explore MGT detec-        technologies are used to mitigate misinformation
tion methods that avoid such features to support        and protect authorship integrity rather than to com-
stronger transferability.                               promise it.

Limitations
                                                        References
Our study primarily focuses on English, and further
investigation is required to assess whether the ob-     Marah Abdin, Jyoti Aneja, Harkirat Behl, Sébastien
                                                         Bubeck, Ronen Eldan, Suriya Gunasekar, Michael
served findings generalize to multilingual, domain-      Harrison, Russell J. Hewett, Mojan Javaheripi, Piero
specific, or code-switched settings. Linguistic vari-    Kauffmann, James R. Lee, Yin Tat Lee, Yuanzhi Li,
ation across languages and domains may introduce         Weishung Liu, Caio C. T. Mendes, Anh Nguyen,
distinct stylistic cues and distributional properties    Eric Price, Gustavo de Rosa, Olli Saarikivi, and
                                                         8 others. 2024. Phi-4 technical report. Preprint,
that affect both personalization and detection be-       arXiv:2412.08905.
havior in ways not captured by the current analysis.
   While our results demonstrate that the feature-      Anthropic. 2025a. Claude 3.7 sonnet system card. Tech-
inversion mechanism plays a central role in explain-      nical report.
ing shifts in detector performance under personal-      Anthropic. 2025b. Claude opus 4 & claude sonnet 4
ization, other latent stylistic or semantic factors       system card. Technical report.
may also contribute to detection robustness. These
                                                        Guangsheng Bao, Yanbin Zhao, Zhiyang Teng, Linyi
factors, such as discourse structure, pragmatic in-
                                                          Yang, and Yue Zhang. 2024. Fast-detectGPT: Effi-
tent, or higher-level narrative patterns, are not ex-     cient zero-shot detection of machine-generated text
plicitly modeled in our framework and remain an           via conditional probability curvature. In Proc. of
open area for future exploration.                         ICLR.
   Finally, our experiments are conducted in con-       Tom Brown, Benjamin Mann, Nick Ryder, Melanie
trolled offline environments using static bench-          Subbiah, Jared D Kaplan, Prafulla Dhariwal, Arvind
marks, which may not fully reflect the dynamics           Neelakantan, Pranav Shyam, Girish Sastry, Amanda
of real-world deployment scenarios. In practice,          Askell, Sandhini Agarwal, Ariel Herbert-Voss,
personalized text generation and detection often          Gretchen Krueger, Tom Henighan, Rewon Child,
                                                          Aditya Ramesh, Daniel Ziegler, Jeffrey Wu, Clemens
occur in interactive and evolving contexts, includ-       Winter, and 12 others. 2020. Language models are
ing adaptive generation loops, human–AI coauthor-         few-shot learners. In Proc. of NeurIPS.
ing, and adversarial style imitation. Evaluating
                                                        Xiangyu Dong, Xingyi Zhang, and Sibo Wang. 2024.
model behavior under these more realistic condi-
                                                          Rayleigh quotient graph neural networks for graph-
tions could provide a more comprehensive under-           level anomaly detection. In Proc. of ICLR.
standing of robustness and generalization in practi-
cal applications.                                       Abhimanyu Dubey, Abhinav Jauhri, Abhinav Pandey,
                                                          Abhishek Kadian, Ahmad Al-Dahle, Aiesha Letman,
                                                          Akhil Mathur, Alan Schelten, Amy Yang, Angela
Ethical Considerations                                    Fan, Anirudh Goyal, Anthony Hartshorn, Aobo Yang,
                                                          Archi Mitra, Archie Sravankumar, Artem Korenev,
This work aims to advance understanding of                Arthur Hinsvark, Arun Rao, Aston Zhang, and 82
machine-generated text (MGT) detection in per-            others. 2024. The llama 3 herd of models. CoRR.
sonalized scenarios and is intended for research on
transparency, robustness, and responsible AI use.       Liam Dugan, Alyssa Hwang, Filip Trhlík, Andrew
                                                          Zhu, Josh Magnus Ludan, Hainiu Xu, Daphne Ip-
All datasets used in our experiments are derived          polito, and Chris Callison-Burch. 2024. RAID: A
from publicly available sources, and no private,          shared benchmark for robust evaluation of machine-
sensitive, or personally identifiable information is      generated text detectors. In Proc. of ACL.
included. The generation process follows open and
                                                        Lang Gao, Kaiyang Wan, Wei Liu, Chenxi Wang, Zirui
reproducible settings without targeting any real in-      Song, Zixiang Xu, Yanbo Wang, Veselin Stoyanov,
dividuals. While our findings reveal potential weak-      and Xiuying Chen. 2025. Evaluate bias without man-
nesses in existing detectors, they are presented to       ual test sets: A concept representation perspective for
support the development of safer and more reliable        llms. Preprint, arXiv:2505.15524.
detection systems rather than to facilitate misuse or   Sebastian Gehrmann, Hendrik Strobelt, and Alexander
impersonation. We encourage future research to ap-        Rush. 2019. GLTR: Statistical detection and visual-
ply these insights ethically, ensuring that detection     ization of generated text. In Proc. of ACL.
                                                   43151
Martin Gerlach and Francesc Font-Clos. 2020. A stan-       Xiang Lisa Li, Ari Holtzman, Daniel Fried, Percy Liang,
 dardized project gutenberg corpus for statistical anal-     Jason Eisner, Tatsunori Hashimoto, Luke Zettle-
 ysis of natural language and quantitative linguistics.      moyer, and Mike Lewis. 2023. Contrastive decoding:
 Entropy.                                                    Open-ended text generation as optimization. In Proc.
                                                             of ACL.
Biyang Guo, Xin Zhang, Ziyuan Wang, Minqi Jiang,
  Jinran Nie, Yuxuan Ding, Jianwei Yue, and Yupeng         Jiongnan Liu, Yutao Zhu, Shuting Wang, Xiaochi Wei,
  Wu. 2023. How close is chatgpt to human experts?            Erxue Min, Yu Lu, Shuaiqiang Wang, Dawei Yin,
  comparison corpus, evaluation, and detection. arXiv         and Zhicheng Dou. 2025. LLMs + persona-plug =
  preprint arxiv:2301.07597.                                  personalized LLMs. In Proc. of ACL.

Xun Guo, Yongxin He, Shan Zhang, Ting Zhang, Wan-          Yinhan Liu, Myle Ott, Naman Goyal, Jingfei Du, Man-
  quan Feng, Haibin Huang, and Chongyang Ma. 2024.           dar Joshi, Danqi Chen, Omer Levy, Mike Lewis,
  Detective: Detecting ai-generated text via multi-level     Luke Zettlemoyer, and Veselin Stoyanov. 2019.
  contrastive learning. Proc. of NeurIPS.                    Roberta: A robustly optimized bert pretraining ap-
                                                             proach. Preprint, arXiv:1907.11692.
Xinlei He, Xinyue Shen, Zeyuan Chen, Michael Backes,
  and Yang Zhang. 2024. Mgtbench: Benchmarking             Dominik Macko, Jakub Kopal, Róbert Móro, and Ivan
  machine-generated text detection. In Proceedings of        Srba. 2025. Multisocial: Multilingual benchmark
  the 2024 on ACM SIGSAC Conference on Computer              of machine-generated text detection of social-media
  and Communications Security, CCS 2024, Salt Lake           texts. In Proc. of ACL.
  City, UT, USA, October 14-18, 2024.
                                                           Andrea Cristina McGlinchey and Peter J Barclay. 2024.
Steffen Herbold, Alexander Trautsch, Zlata Kikteva, and      Using machine learning to distinguish human-written
   Annette Hautli-Janisz. 2024. Large language models        from machine-generated creative fiction. Preprint,
   can impersonate politicians and other public figures.     arXiv:2412.15253.
   Preprint, arXiv:2407.12855.
                                                           Rafael Mendoza, Isabella Cruz, Richard Liu, Aarav
Edward J Hu, yelong shen, Phillip Wallis, Zeyuan Allen-
                                                             Deshmukh, David Williams, Jesscia Peng, and Ro-
  Zhu, Yuanzhi Li, Shean Wang, Lu Wang, and Weizhu
                                                             han Iyer. 2024. Adaptive self-supervised learning
  Chen. 2022. LoRA: Low-rank adaptation of large
                                                             strategies for dynamic on-device llm personalization.
  language models. In Proc. of ICLR.
                                                             Preprint, arXiv:2409.16973.
Yue Huang, Chujie Gao, Siyuan Wu, Haoran Wang,
  Xiangqi Wang, Yujun Zhou, Yanbo Wang, Jiayi Ye,          Tomáš Mikolov, Wen-tau Yih, and Geoffrey Zweig.
  Jiawen Shi, Qihui Zhang, and 1 others. 2025. On            2013. Linguistic regularities in continuous space
  the trustworthiness of generative foundation mod-          word representations. In Proc. of AACL.
  els: Guideline, assessment, and perspective. arXiv
  preprint arXiv:2502.14296.                               John Morris, Volodymyr Kuleshov, Vitaly Shmatikov,
                                                             and Alexander Rush. 2023. Text embeddings reveal
Andrew Ilyas, Shibani Santurkar, Dimitris Tsipras, Lo-       (almost) as much as text. In Proc. of EMNLP, pages
  gan Engstrom, Brandon Tran, and Aleksander Madry.          12448–12460.
  2019. Adversarial examples are not bugs, they are
  features. In Proc. of NeurIPS, pages 125–136.            Sheshera Mysore, Zhuoran Lu, Mengting Wan, Longqi
                                                             Yang, Bahareh Sarrafzadeh, Steve Menezes, Tina
Daphne Ippolito, Daniel Duckworth, Chris Callison-           Baghaee, Emmanuel Barajas Gonzalez, Jennifer
  Burch, and Douglas Eck. 2020. Automatic detection          Neville, and Tara Safavi. 2024. Pearl: Personal-
  of generated text is easiest when humans are fooled.       izing large language model writing assistants with
  In Proc. of ACL.                                           generation-calibrated retrievers. In Proceedings of
                                                             the 1st Workshop on Customizable NLP: Progress
Kaijie Jiao, Quan Wang, Licheng Zhang, Zikang Guo,           and Challenges in Customizing NLP for a Domain,
  and Zhendong Mao. 2025. M-RangeDetector: En-               Application, Group, or Individual (CustomNLP4U).
  hancing generalization in machine-generated text de-
  tection through multi-range attention masks. In Proc.    Shashi Narayan, Shay B. Cohen, and Mirella Lapata.
  of ACL Findings.                                           2018. Don’t give me the details, just the summary!
                                                             topic-aware convolutional neural networks for ex-
Minseok Jung, Cynthia Fuertes Panizo, Liam Dugan,            treme summarization. In Proc. of EMNLP.
 Yi R., Fung, Pin-Yu Chen, and Paul Pu Liang.
  2025.     Group-adaptive threshold optimization          OpenAI, :, Aaron Hurst, Adam Lerer, Adam P. Goucher,
  for robust ai-generated text detection. Preprint,          Adam Perelman, Aditya Ramesh, Aidan Clark,
  arXiv:2502.04528.                                          AJ Ostrow, Akila Welihinda, Alan Hayes, Alec
                                                             Radford, Aleksander M ˛adry, Alex Baker-Whitcomb,
Antonia Karamolegkou, Jiaang Li, Li Zhou, and An-            Alex Beutel, Alex Borzunov, Alex Carney, Alex
  ders Søgaard. 2023. Copyright violations and large         Chow, Alex Kirillov, and 401 others. 2024. Gpt-4o
  language models. In Proc. of EMNLP.                        system card. Preprint, arXiv:2410.21276.
                                                      43152
Gerrit Quaremba, Elizabeth Black, Denny Vrandečić,       Eduard Tulchinskii, Kristian Kuznetsov, Kushnareva
  and Elena Simperl. 2025. Wetbench: A benchmark             Laida, Daniil Cherniavskii, Sergey Nikolenko,
  for detecting task-specific machine-generated text on      Evgeny Burnaev, Serguei Barannikov, and Irina Pi-
  wikipedia. Preprint, arXiv:2507.03373.                     ontkovskaya. 2023. Intrinsic dimension estimation
                                                             for robust detection of AI-generated texts. In Proc.
Nils Reimers and Iryna Gurevych. 2019. Sentence-bert:        of NeurIPS.
  Sentence embeddings using siamese bert-networks.
  In Proc. of EMNLP, pages 3980–3990.                      Ben Wang and Aran Komatsuzaki. 2021. GPT-J-6B: A
Jenna Russell, Marzena Karpinska, and Mohit Iyyer.           6 Billion Parameter Autoregressive Language Model.
  2025. People who frequently use ChatGPT for writ-
  ing tasks are accurate and robust detectors of AI-       Yuxia Wang, Jonibek Mansurov, Petar Ivanov, Jinyan
  generated text. In Proc. of ACL.                           Su, Artem Shelmanov, Akim Tsvigun, Osama Mo-
                                                             hammed Afzal, Tarek Mahmoud, Giovanni Puccetti,
Jonathan Schler, Moshe Koppel, Shlomo Argamon, and           Thomas Arnold, Alham Fikri Aji, Nizar Habash,
  James W Pennebaker. 2006. Effects of age and gen-          Iryna Gurevych, and Preslav Nakov. 2024a. M4gt-
  der on blogging. In Proc. of AAAI.                         bench: Evaluation benchmark for black-box machine-
                                                             generated text detection. In Proc. of ACL, pages
Benjamin Schweinhart. 2021. Persistent homology and          3964–3992.
  the upper box dimension. Discret. Comput. Geom.,
  pages 331–364.
                                                           Yuxia Wang, Jonibek Mansurov, Petar Ivanov, Jinyan
Haizhou Shi, Zihao Xu, Hengyi Wang, Weiyi Qin,               Su, Artem Shelmanov, Akim Tsvigun, Chenxi White-
  Wenyuan Wang, Yibin Wang, Zifeng Wang, Sayna               house, Osama Mohammed Afzal, Tarek Mahmoud,
  Ebrahimi, and Hao Wang. 2024. Continual learning           Toru Sasaki, Thomas Arnold, Alham Fikri Aji,
  of large language models: A comprehensive survey.          Nizar Habash, Iryna Gurevych, and Preslav Nakov.
  arXiv preprint arXiv:2404.16789.                           2024b. M4: Multi-generator, multi-domain, and
                                                             multi-lingual black-box machine-generated text de-
Irene Solaiman, Miles Brundage, Jack Clark, Amanda           tection. In Proc. of EACL.
   Askell, Ariel Herbert-Voss, Jeff Wu, Alec Radford,
   Gretchen Krueger, Jong Wook Kim, Sarah Kreps,           Zixiao Wang, Duzhen Zhang, Ishita Agrawal, Shen Gao,
   Miles McCain, Alex Newhouse, Jason Blazakis, Kris         Le Song, and Xiuying Chen. 2025. Beyond profile:
   McGuffie, and Jasmine Wang. 2019. Release strate-         From surface-level facts to deep persona simulation
   gies and the social impacts of language models.           in llms. ACL findings.
   Preprint, arXiv:1908.09203.
Jinyan Su, Terry Zhuo, Di Wang, and Preslav Nakov.         Dongjun Wei, Minjia Mao, Xiao Fang, and Michael
   2023a. DetectLLM: Leveraging log rank information         Chau. 2025. Short-PHD: Detecting short LLM-
   for zero-shot detection of machine-generated text. In     generated text with topological data analysis after
   Proc. of EMNLP Findings.                                  off-topic content insertion. In Second Conference on
                                                             Language Modeling.
Jinyan Su, Terry Yue Zhuo, Di Wang, and Preslav Nakov.
   2023b. DetectLLM: Leveraging log rank information       Stanisław Woźniak, Bartłomiej Koptyra, Arkadiusz
   for zero-shot detection of machine-generated text. In     Janz, Przemysław Kazienko, and Jan Kocoń. 2024.
   Proc. of EMNLP.                                            Personalized large language models. In Proc. of
                                                              ICDM.
Qwen Team. 2025. Qwen3 technical report. Preprint,
 arXiv:2505.09388.
                                                           Yihuai Xu, Yongwei Wang, Yifei Bi, Huangsen Cao,
Chong Tian, Qirong Ho, and Xiuying Chen. 2025. A             Zhouhan Lin, Yu Zhao, and Fei Wu. 2025a. Training-
  symbolic adversarial learning framework for evolv-         free LLM-generated text detection by mining token
  ing fake news generation and detection. EMNLP.             probability sequences. In Proc. of ICLR.

Yuchuan Tian, Hanting Chen, Xutao Wang, Zheyuan            Yiyan Xu, Jinghao Zhang, Alireza Salemi, Xinting Hu,
  Bai, QINGHUA ZHANG, Ruifeng Li, Chao Xu, and               Wenjie Wang, Fuli Feng, Hamed Zamani, Xiangnan
  Yunhe Wang. 2024. Multiscale positive-unlabeled            He, and Tat-Seng Chua. 2025b. Personalized genera-
  detection of AI-generated texts. In Proc. of ICLR.         tion in large model era: A survey. In Proc. of ACL,
                                                             pages 24607–24649.
Yu-Min Tseng, Yu-Chao Huang, Teng-Yun Hsiao, Wei-
  Lin Chen, Chao-Wei Huang, Yu Meng, and Yun-
  Nung Chen. 2024. Two tales of persona in LLMs: A         Wenqian Ye, Guangtao Zheng, Xu Cao, Yunsheng Ma,
  survey of role-playing and personalization. In Proc.      Xia Hu, and Aidong Zhang. 2024. Spurious cor-
  of EMNLP Findings.                                         relations in machine learning: A survey. CoRR,
                                                             abs/2402.12715.
Quan Tu, Shilong Fan, Zihang Tian, Tianhao Shen,
  Shuo Shang, Xin Gao, and Rui Yan. 2024. Char-            Denghui Zhang, Zhaozhuo Xu, and Weijie Zhao. 2025a.
  actereval: A chinese benchmark for role-playing con-       LLMs and copyright risks: Benchmarks and mitiga-
  versational agent evaluation. In Proc. of ACL.             tion approaches. In Proc. of ACL.
                                                      43153
Weizhi Zhang, Xinyang Zhang, Chenwei Zhang, Liang-         user has fewer posts, so CPT is not suitable. In
 wei Yang, Jingbo Shang, Zhepei Wei, Henry Peng            this case, large instruction-tuned models accessed
  Zou, Zijie Huang, Zhengyang Wang, Yifan Gao, Xi-
                                                           through APIs are prompted to mimic user style,
  aoman Pan, Lian Xiong, Jingguo Liu, Philip S. Yu,
  and Xian Li. 2025b. Personaagent: When large lan-        which captures shallower but flexible personaliza-
  guage model agents meet personalization at test time.    tion. Stylo-Literary and Stylo-Blog, therefore,
 Preprint, arXiv:2506.06254.                               represent two complementary levels of personal-
Zhehao Zhang, Ryan A. Rossi, Branislav Kveton, Yi-         ization and together provide a diverse evaluation
  jia Shao, Diyi Yang, Hamed Zamani, Franck Der-           space for detectors.
  noncourt, Joe Barrow, Tong Yu, Sungchul Kim,
  Ruiyi Zhang, Jiuxiang Gu, Tyler Derr, Hongjie Chen,      A.1.3    Dataset Scale and Diversity
  Junda Wu, Xiang Chen, Zichao Wang, Subrata Mitra,
                                                           The overall scale of StyloBench is comparable
  Nedim Lipka, and 2 others. 2025c. Personalization
  of large language models: A survey. Transactions on      to existing MGT detection benchmarks such as
  Machine Learning Research.                               CH3-English (Guo et al., 2023), with about 25,000
Han Zhao, Chen Dan, Bryon Aragam, Tommi S.
                                                           versus 26,000 samples. StyloBench contains 21
  Jaakkola, Geoffrey J. Gordon, and Pradeep Raviku-        subsets, which is similar to the number of subsets in
  mar. 2022. Fundamental limits and tradeoffs in in-       M4 with 20 subsets, and each experimental setting
  variant representation learning. J. Mach. Learn. Res.,   uses more than 1,000 test samples. This design
  pages 340:1–340:49.
                                                           provides enough data for stable statistical analy-
Kaiyang Zhou, Ziwei Liu, Yu Qiao, Tao Xiang, and           sis while keeping the benchmark manageable. In
  Chen Change Loy. 2023. Domain generalization:            Stylo-Literary, seven authors with clearly dif-
  A survey. IEEE Trans. Pattern Anal. Mach. Intell.,
                                                           ferent styles are included, and all of them lead to
  pages 4396–4415.
                                                           strong performance changes in detectors on HWT
                                                           and MGT. This indicates that the current author set
A    Details on StyloBench and M4
                                                           is already informative, while also leaving room for
A.1 Dataset Construction Discussion                        future expansion to more writers and domains.
A.1.1 Scenario Selection
                                                           A.2     Examples of StyloBench
StyloBench focuses on two personalization sce-
                                                           For an intuitive understanding, we show examples
narios: literary style imitation and social media
                                                           of Stylo-Blog and Stylo-Literary with differ-
style blog generation. These scenarios are widely
                                                           ent generators and sub-domains in Table 15 and 16.
used in recent personalization studies (Xu et al.,
2025b; McGlinchey and Barclay, 2024) and pro-              A.3     Preprocessing for Stylo-Literary
vide rich individual expression. Literary texts offer
long narratives with stable author styles, while blog      Due to formatting and compilation issues, some
posts capture informal and self-expressive writing.        artifacts in the Gutenberg Book Corpus are not part
Together, they form a practical testbed for person-        of the original texts and may distort detector per-
alized MGT, where detectors face realistic stylistic       formance. We clean all artifacts by: (1) remove in-
shifts when distinguishing MGT from HWT. The               dentation symbols not present in the original texts;
current version of StyloBench does not yet include         (2) delete isolated line breaks and reduce multi-
multilingual or other specialized domains, and fu-         ple consecutive line breaks to a single one, since
ture extensions are planned to cover a broader range       isolated breaks are used for line-width alignment
of personalized scenarios.                                 and multiple breaks denote paragraph or chapter
                                                           boundaries; (3) remove lines consisting of repeated
A.1.2 Model Selection                                      “=” symbols, which usually mark chapter or section
The 2 components of StyloBench use different               starts. Moreover, we remove unrelated segments
model configurations, mainly due to differences            not written by target authors: (1) delete lines con-
in data availability and personalization depth. For        taining links, which are often source annotations;
literary data in Stylo-Literary, there are many            (2) delete lines with long digit sequences, which
texts per author, which makes CPT on each au-              usually indicate compiler contact information.
thor feasible and allows deeper stylistic imita-
tion. Smaller models are used in this setting be-          A.4     Details of Stylo-Blog
cause they are easier to train and adapt to indi-          Data Source. The data source of Stylo-Blog
vidual authors. For blogs in Stylo-Blog, each              is Blog-1K, a subset of the Blog Authorship Cor-
                                                      43154
             Parameter            Value                    Generator Wikipedia Reddit WikiHow PeerRead arXiv    Total
                                                           Davinci     3,000   3,000   3,000    2,323   3,000   14,323
             Maximum samples      3,000                    ChatGPT     2,995   3,000   3,000    2,344   3,000   14,339
             Batch size           8                        Cohere      2,336   1,220   2,999    1,702   3,000   11,257
             Learning rate        0.0001                   BLOOMz      3,000   3,000   3,000    2,340   3,000   14,340
             Epochs               5
             LoRA configuration                           Table 4: Statistics of the selected English subset of M4,
                                                          where the values indicate the numbers of HWTs and
             LoRA rank            16
             LoRA alpha           32                      MGTs, which are equal.
             LoRA dropout         0.1
                                                          A.6    the English Subset of M4
Table 3: Key hyperparameters in CPT for generating        The selected English subset contains 5 data sources
Stylo-Literary MGTs.
                                                          to reflect diversity and daily language use: Reddit,
                                                          Wikipedia, WikiHow, arXiv, and PeerRead. Each
pus (Schler et al., 2006). The Blog Authorship
                                                          LLM generator uses 2–8 distinct prompts to pro-
Corpus was collected from posts on blogger.com
                                                          duce varied MGTs. We select only the generators
in 2004. It spans a wide range of topics, is lin-
                                                          that have data in all five sources in the released ver-
guistically diverse, and has been widely used for
                                                          sion of M4. Table 4 reports the detailed statistics.
studying stylistic and demographic features. Based
on this corpus, Blog-1K filters high-quality blogs        B     Experiment Details
and groups them by authors, resulting in 1,000 au-
thors and 16,132 posts. It provides clearer author        B.1    Baselines
attribution, a more balanced distribution, and more       We follow the same set of baseline detectors as
consistent writing quality, making it suitable for        in (Xu et al., 2025a). The implementation details
constructing Stylo-Blog in personalized evalua-           of the seven baselines in this study are as follows.
tion settings.                                               Log-Likelihood (Solaiman et al., 2019). The
                                                          average log probability of all tokens in a text is used
Few-shot Construction. For each author, we                as the metric. Texts with lower average likelihood
construct few-shot prompts using their remaining          are more likely to be MGT.
posts to guide style imitation. After selecting one          LogRank (Solaiman et al., 2019). The average
post as the target for generating MGT, the number         log rank of tokens in the text, where ranks are
of few-shot examples depends on how many posts            determined by GPT-J’s predicted probabilities, is
remain for that author. If only one post remains,         used as the metric. Texts with higher ranks are
we use a 1-shot setting. If two posts remain, we          more likely to be MGT.
use a 2-shot setting. If three or more posts remain,         Entropy (Gehrmann et al., 2019). The average
we randomly sample three posts to form a 3-shot           entropy of the predicted token distribution is com-
prompt. This strategy ensures that the few-shot           puted. Texts with higher entropy values are more
construction adapts to data availability while main-      likely to be MGT.
taining consistency across authors. The prompt               DetectLRR (Su et al., 2023a). The ratio of log-
template is shown in Figure 8.                            likelihood to log-rank is taken as the score. Larger
                                                          ratios indicate a higher chance of MGT.
A.5 Configurations of LLM Generators
                                                             Fast-DetectGPT (Bao et al., 2024). This
In constructing Stylo-Literary, the key param-            method perturbs the input text to create contrast
eter settings for training the generator LLM are          samples and compares the scoring differences be-
shown in Table 3. For both subsets of StyloBench,         tween the original and perturbed texts. Larger dis-
we apply the same generation settings: (1) the max-       crepancies indicate that the original text is more
imum generation length is 512 tokens, to ensure           likely to be MGT.
consistency of imitated styles, as both training data        Lastde (Xu et al., 2025a). This method ana-
and few-shot samples are no longer than 512 to-           lyzes local and global diversity of token probability
kens; (2) the temperature is set to 1, to avoid repeti-   sequences, and combines them with likelihood in-
tion in base LLMs (Li et al., 2023), and encourage        formation. Lower diversity relative to likelihood is
LLMs to produce vivid and diverse personalized            more indicative of MGT.
content. For all other parameters, we adopt their            Lastde++ (Xu et al., 2025a). It is an enhanced
default settings.                                         version of Lastde that normalizes scores using mul-
                                                     43155
      def Prompt(historical_examples, target_request):
         return f"""Given a **BLOG REQUEST** from a USER to continue writing a blog, write a **BLOG POST**
      mimicking the USER to satisfy the REQUEST.
      Use the following instructions for your response:

      1. You should maintain consistency in tone and style with the USER's historical blog posts.
      2. You should imitate the language style of the USER's historical blog posts.
      3. You should employ similar rhetorical methods as the USER's historical blog posts.
      4. You must continue the BLOG POST for **at least 512 tokens**, expanding naturally on the REQUEST.

      Here are some historical blog posts by the USER:
      {historical_examples}

      REQUEST (blog beginning, first ~30 words):
      {target_request}

      Write the BLOG POST to **continue the REQUEST**, mimicking the tone, style, and rhetorical methods of the
      USER's historical blog posts."""



Figure 8: Prompt template for MGT in synthesizing Stylo-Blog. It takes 1–3 blogs from the same author as
historical_examples and uses the first 30 tokens of the current blog as target_request for continuation.


tiple contrast samples, making the results more                the best performance on M42 and evaluate it on the
stable. Higher normalized values suggest MGT.                  same test sets. We use AUROC for evaluation.
   Here we test all baselines under a black-box
scenario, i.e., we cannot access generators when                               Hyperparameter        Value
detecting MGTs. We use GPT-J-6B (Wang and                                      Batch size             32
Komatsuzaki, 2021) as a proxy model for any                                    Epochs                 10
                                                                               Learning rate       2 × 10−5
necessary information for detectors. Specifically,                             Warmup steps          2000
for Log-Likelihood, LogRank, Entropy, and De-                                  Random seed            42
tectLRR, we compute statistical features by ag-
gregating the probabilities and ranks predicted by                     Table 5: Training configuration for RoBERTa.
GPT-J-6B at each token position; for DetectGPT,
Fast-DetectGPT, Lastde, and Lastde++, we gener-
ate perturbed or sampled variants of the text and              Results and Analysis. The averaged results on
then compare GPT-J-6B’s scoring results between                the three datasets are reported in Table 6. Both de-
the original and the contrast samples.                         tectors perform well on M4, but on StyloBench
                                                               their AUROC scores mostly fall in the 0.4–0.6
B.2   Full Results on Training-free Methods
                                                               range, close to random prediction. Roberta shows
Since full results on Stylo-Blog have been pre-                near-random performance in about 64% of the per-
sented in Table 2, here we report the AUROC of                 sonalized settings, while for DeTeCtive this pro-
each MGT detector across all subdomains and gen-               portion reaches 92%. Such frequent and structural
erators on Stylo-Literary in Table 10, and full                performance drops are uncommon in standard do-
results on M4 in Table 11.                                     main generalization, suggesting that inverted fea-
                                                               ture behavior plays a significant role. At the same
B.3   Experiments on Training-based Methods                    time, these training-based models do not collapse
Setup. We evaluate two representative training-                to extremely low AUROC values as some training-
based detectors: Roberta (Liu et al., 2019) and                free detectors do, which indicates that they may
DeTeCtive (Guo et al., 2024). For M4, each subset is           rely on a broader set of learned features that pre-
split by randomly selecting 1,000 HWT and MGT                  vent complete failure. Full results are provided in
samples as the test set, with all remaining samples            Tables 12–14.
used for training. The finetuning configuration for
Roberta is shown in Table 5. For DeTeCtive, we                     2
                                                                   https://huggingface.co/heyongxin233/
use the publicly released checkpoint that achieves             DeTeCtive/blob/main/M4_monolingual_best.pth

                                                          43156
       Dataset             Roberta    DeTeCtive            strong agreement with the original order, values
       Stylo-Literary        53.33       53.78             close to −1 indicate reversed order, and values
       Stylo-Blog            64.77       49.73             around 0 correspond to randomized tokens.
       M4                    99.94       84.69
       AUROC 0.4–0.6         64%         92%               C.3    Mathematical Design Explanation
                                                           Derivation of Equation 2 The equation qi (w) =
Table 6: Average AUROC of training-based detectors.
                                                           (w⊤ vG )(w⊤ vS ) follows from basic matrix multi-
C    Metrics and Mathematical Tools                        plication:

C.1 AUROC                                                  (w⊤ vG )(w⊤ vS ) = (w⊤ vG )(vS⊤ w) = w⊤ (vG vS⊤ )w.
AUROC measures detector performance across the
                                                           Derivation of Equation 3 For any real matrix
full range of thresholds rather than relying on a
                                                           M ∈ Rn×n and vector w, the quadratic form equals
fixed one, therefore reflecting the overall ability
                                                           its transpose, as it is a scalar:
of the detector. AUROC ranges from 0.0 to 1.0,
where 0.5 corresponds to random guessing, and 1.0              (w⊤ M w)⊤ = w⊤ M ⊤ (w⊤ )⊤ = w⊤ M ⊤ w.
indicates perfect discrimination. It can be inter-
preted as the probability that a randomly selected         Therefore
machine-generated text is assigned a higher detec-
tion score than a randomly selected human-written                    w⊤ Mw = 21 w⊤ (M + M⊤ )w.
text. Values below 0.5 indicate performance worse
than random guessing and imply that the predic-            Applying this to M = vG vS⊤ gives
tions are systematically inverted.
                                                                   qi (w) = w⊤ 12 (vG vS⊤ + vS vG
                                                                                                ⊤
                                                                                                  )w.
C.2 Correlation Coefficients
                                                           Rayleigh Quotient For a matrix M ∈ Rn×n and
Spearman ρ Spearman’s rank correlation coeffi-             a nonzero vector w ∈ Rn , the Rayleigh quotient is
cient measures the monotonic relationship between          defined as
two variables by computing the Pearson correlation                                  w⊤ Mw
on their rank values. It is defined as                                     R(w) =            .          (11)
                                                                                      w⊤ w
                            P
                          6 ni=1 d2i                          When ||w|| = 1, this can be also written as:
               ρ=1−                  ,          (8)
                          n(n2 − 1)                        R(w) = w⊤ Mw. When M is symmetric, R(w) is
                                                           bounded between the smallest and largest eigen-
  where di is the rank difference of the i-th sample.
                                                           values of M. In particular, the minimum of R(w)
Values close to 1 or −1 indicate strong positive or
                                                           equals the smallest eigenvalue and the maximum
negative monotonic correlation.
                                                           equals the largest eigenvalue, attained when w is
Pearson r Pearson’s correlation coefficient cap-           the corresponding eigenvector.
tures the linear relationship between two variables.
It is defined as                                           D     Analysis on Feature-Inversion Trap
                  Pn
                     i=1 (xi −x̄)(y
                                                           D.1    Performance Change of Detectors
    r = √Pn                  2
                               √Pni −ȳ)       2
                                                 .   (9)
                    (x
                 i=1 i −x̄)        i=1 (yi −ȳ)            To observe how each detector changes across the
Values near 1 indicate strong positive linear corre-       two domains, we compute its average AUROC on
lation, values near −1 strong negative correlation,        M4, Stylo-Blog, and Stylo-Literary, and plot
and 0 denotes no linear correlation.                       the results in Figure 9. The figure shows results
                                                           similar to §5.2: (1) Most detectors drop more in
Kendall’s τ Kendall’s τ measures the ordinal               the personalized domain than in the general do-
association between two variables based on the             main, while a few detectors, such as Entropy and
number of concordant and discordant pairs:                 Fast-DetectGPT, improve on some subsets of the
                                                           personalized domain. (2) Most classifiers fluctu-
 τ = (#concordant pairs)−(#discordant
                        n
                                     pairs)
                                             . (10)        ate less on Stylo-Blog than on Stylo-Literary,
                            2                              which indicates that deep personalized imitation af-
 In this work, τ is also employed as a quantitative        ter training misleads detectors more strongly than
measure of word order. Values close to 1 indicate          prompting. (3) On Stylo-Literary, five detectors
                                                      43157
                                    M4                 Stylo-Blog        Stylo-Literary


Figure 9: The average AUROC of different detectors on M4, Stylo-Blog, and Stylo-Literary. The lines indicate
performance changes caused by domain transfer. Detectors show a clear change in the personalized domain,
including surges, decreases, and inversions.




Figure 10: AUROC of each detector and the distribution of feature value difference D(·, w⋆ ) on the test set for each
experiment. The plots show clear correlation, with varying strength and sign across detectors.


fall below 0.5 in average AUROC, which shows                  pure random noise should not produce this effect.
that most detectors flip predictions in the person-
alized domain and confirms the generality of this             Setup. We tokenize each text. We then shuffle
phenomenon.                                                   these tokens to create text with no meaning. Based
                                                              on these texts, we build three types of test sets.
D.2 Correlation Visualization                                 (1) Along inverted direction. We sort samples by
                                                              their projection on the inverted feature direction
Following §4.2.2, we plot the AUROC of each de-
                                                              w⋆ . We take the top samples as positives and the
tector and the distribution of D(·, w⋆ ) on the test
                                                              bottom samples as negatives. This set tests whether
set across multiple experiments, as shown in Fig-
                                                              the detector depends only on inverted features. (2)
ure 10. The results reveal that: (1) The sample
                                                              Along orthogonal direction. We sort samples by
distribution is concentrated, and most points lie
                                                              their projection on a direction w⊥ ⋆ that is orthogo-
near the fitted line, which indicates a clear cor-
                                                              nal to the inverted feature. We take the top samples
relation between AUROC and D(·, w⋆ ). (2) En-
                                                              as positives and the bottom samples as negatives.
tropy shows a positive correlation, while the others
                                                              This set tests whether the detector depends on other
show a negative correlation, which indicates that
                                                              directions that share the same form but do not re-
the Feature-Inversion Trap affects different detec-
                                                              flect inverted features. (3) Random. We shuffle all
tors in different ways.
                                                              samples and split them into positives and negatives
D.3 Verification of Detector Dependence on                    at random. This gives a baseline under complete
    Inverted Features                                         randomness. For each type, we create 50 datasets.
                                                              Each has 50 positive and 50 negative samples.
In §4.2.2, we show a strong negative correlation
between the projection gap of inverted features and           Results and analysis. We test seven detectors
detector performance. This correlation may still              on these datasets. We plot the AUROC distribu-
be spurious. We therefore design experiments to               tion across the 50 runs in Figure 11. The results
show that detectors do rely on inverted features.             show three clear patterns. (1) Random: All de-
The core idea is simple: if a detector relies on in-          tectors stay near 0.5. This confirms that detectors
verted features, then it should still work on random          behave randomly in random noise. (2) Inverted
text. The text may be meaningless, but if posi-               direction: Detectors show strong classification ten-
tive and negative samples show a clear gap along              dencies. Entropy has an average AUROC below
the inverted feature, the detector should still show          0.4. Other detectors have an AUROC above 0.6.
strong results. On the contrary, other features or            The AUROC distribution is also more spread out.
                                                       43158
Extreme values such as AUROC above 0.8 or be-            and detector performance on M4:
low 0.2 appear more often. These signs show that
detectors rely on inverted features to make a predic-          r = Spearman(DM4 , AUROCM4 ).               (12)
tion. (3) Orthogonal direction: No strong tendency
                                                         The results for all detectors are shown in Fig-
appears. Some detectors behave almost the same
                                                         ure 13. Cross-domain correlations (general → per-
as in the random set, such as Lastde, Lastde++, and
                                                         sonalized) are consistently higher than correlations
Fast-DetectGPT. Other detectors shift slightly but
                                                         within M4 subsets. This shows that the inverted
remain within the 0.4 to 0.6 range, which is still
                                                         direction explains changes when moving to per-
close to random. These results show that other fea-
                                                         sonalized domains, but not the differences inside
tures cannot influence detector behavior as inverted
                                                         M4.
features do. Together with the strong correlation
shown in Figure 4, these results support a clear         For point (2). Reversal rarely appears across M4
conclusion. In personalized settings, the feature-       subsets, but it occurs frequently on StyloBench.
inversion trap is a key reason for the reversed be-      Table 11 reports all results on M4. Among 140
havior of many detectors.                                runs, only 25 (17.9%) have an AUROC below 0.5.
                                                         In contrast, in Stylo-Literary, 93 out of 147 runs
D.4 Ablation Study for StyloCheck                        (63.3%) fall below 0.5. This large gap shows that
We conduct an ablation study to assess how the           personalized scenarios cannot be fully explained by
number of probe datasets affects the reliability of      common OOD factors such as feature weakening.
StyloCheck. Figure 12(a) shows the distribution          Together with point (1), this supports that person-
of r when using 1, 3, and 5 datasets. With fewer         alization causes a structural reversal of the same
datasets, the mean r decreases and the probability       feature, not a typical domain shift.
of r < −0.5 increases, indicating a higher risk of
                                                         E.2   Connections to Other Terms
incorrect prediction. Figure 12(b) plots the change
of r as the number of datasets grows from 1 to           The feature inversion phenomenon introduced ap-
10. The mean r rises gradually, but slows down           pears to share surface similarities with several es-
as it approaches an upper bound near 0.8. The            tablished concepts in machine learning. To avoid
standard deviation also decreases, but with dimin-       misunderstanding, we describe the relation be-
ishing returns. These results suggest that increasing    tween these concepts and our findings, and we
the dataset size improves reliability, but the benefit   clarify the differences.
diminishes over time. Using five probe datasets             Spurious Correlations. The feature inversion
offers a good balance in practice.                       phenomenon is related to spurious correlations (Ye
                                                         et al., 2024) because many detectors rely on cues
E    Empirical Evidence for §6                           that do not remain stable across domains. For ex-
                                                         ample, detectors often assume that HWT is more
E.1 Difference Between the Feature-Inversion             diverse than MGT. Personalization alters this pat-
    Trap and OOD Effects                                 tern and causes the same cue to change its meaning.
In §6, we state two reasons why the feature-             This resembles spurious correlations, but the key
inversion trap is different from standard OOD ef-        difference is that the correlation does not simply
fects: (1) it is tightly correlated with the inverted    weaken but is reversed across domains.
feature direction; (2) it causes reversal of detector       Domain Shift Robustness. The feature inver-
behavior, not only performance decay. We now             sion phenomenon is also connected to domain shift.
verify both points with experiments.                     In most domain shift settings, model performance
                                                         changes gradually because discriminative features
For point (1). We use performance differences            lose reliability (Zhou et al., 2023). In personal-
across M4 subsets as a representative OOD case,          ization, the direction of the discriminative feature
since prior work (Wang et al., 2024b) uses them to       itself changes, and this leads to a reversal of predic-
study detector generalization and their domain gaps      tions. This reflects a stronger and more structural
are well known. For all M4 subsets, we follow §4.2       shift than what is commonly observed in standard
and compute the projection gap on the inverted           OOD cases, as also discussed in Appendix E.1.
direction, denoted as DM4 . We then compute the             Adversarial Robustness.           For the feature-
Spearman correlation between this projection gap         inversion trap, there is a conceptual relation to ad-
                                                    43159
ProbDensity




              AUROC                           Inverted Direction          Orthoganal Direction     Random


 Figure 11: AUROC of each detector on three synthetic test sets and the distribution of feature value difference
 D(·, w⋆ ) under each construction.


                                                                              when the degree of personalization is strong. This
                                                                              highlights a limitation of invariant feature learning
                                                                              in the context of MGT detection.
                                                                                 Feature Inversion in Natural Language Pro-
                                                                              cessing. The term feature inversion in natural
                                                                              language processing is commonly used to describe
                (a)                               (b)
                                                                              the reconstruction of input text from internal rep-
                                                                              resentations (Morris et al., 2023). Our use of the
 Figure 12: (a) Distribution of Pearson r with 1, 3, and                      term is different. Here, “feature inversion” refers
 5 probe datasets. (b) Change of mean Pearson r with                          to a change in the discriminative direction of a fea-
 the number of probe datasets, shaded with one standard
                                                                              ture across domains. A feature that separates HWT
 deviation intervals.
                                                                              from MGT in one domain may work in the opposite
                         General Subdomains       General-Personalized        way in another domain. This concerns a semantic
                                                                              reversal rather than the reconstruction of text.

                                                                              E.3       What Do Inverted Features Capture
                                                                              We believe that the inverted features include, but
                                                                              are not limited to, lexical diversity and semantic
                                                                              coherence. Both of these properties describe as-
                                                                              pects of textual coherence, and both show a clear
                                                                              reversal trend across domains.

                                                                              Lexical Diversity We follow the intrinsic dimen-
                                                                              sion analysis from prior work (Tulchinskii et al.,
 Figure 13: Correlation differences in different detectors.                   2023), which reports that token embeddings of
                                                                              MGT usually lie on lower-dimensional manifolds
versarial robustness because both involve changes                             than those of HWT. This indicates that MGT is
that redirect model attention toward different fea-                           generally less diverse in word usage. Using the
tures (Ilyas et al., 2019). Personalization modifies                          probe datasets in Section 4.1, we follow the analy-
stylistic properties consistently, thereby altering                           sis procedure in (Tulchinskii et al., 2023). We use
how detectors use specific cues. However, the shift                           Roberta-base to encode each sentence. We take
arises naturally from personalized text generation                            the hidden states from the last layer and treat the
rather than from intentional adversarial manipula-                            embedding at each token position as a point in the
tion, and the mechanisms are therefore different.                             hidden space. We then apply persistent homology
   Invariant Representation Learning. Invariant                               dimension (Schweinhart, 2021) to these points to
representation learning aims to identify features                             estimate the dimensionality of lexical variation. Re-
that remain stable across domains. (Zhao et al.,                              sults are shown in Table 7. For HWT, personalized
2022) The feature inversion phenomenon shows                                  samples show higher lexical diversity than gen-
that many detectors rely on features that are not                             eral ones. For MGT, diversity is lower in general
invariant, including patterns related to lexical or                           settings but higher in personalized settings. This
semantic diversity. Even if invariant learning is                             pattern is reversed across domains and aligns with
applied, detectors may still depend on unstable cues                          the feature inversion phenomenon. It suggests that
                                                                         43160
in highly personalized scenarios, MGT may use                    Sentence
                                                                               General     Personalized       ∆
words in a more varied and aggressive manner than               Dimension
HWT.                                                            HWT            5.2764        4.4390        -0.8374
                                                                MGT            3.2783        5.4325        2.1542
         Token                                                  ∆              -1.9981       0.9935           -
                    General   Personalized     ∆
       Dimension
       HWT           9.9952      12.0255     2.0304        Table 8: Sentence-level intrinsic dimension for general
       MGT           6.5751      13.0849     6.5098        and personalized domains.
       ∆            -3.4201      1.0594         -
                                                           Stylo-Literary, and the third on the combined
Table 7: Token-level intrinsic dimension for general and   training sets. All variants are then tested on the
personalized domains.                                      M4 test sets and on both parts of StyloBench. The
                                                           results are shown in Table 9. Finetuning improves
Semantic Coherence We apply a similar idea to              performance inside the training domain, but the
analyze sentence-level semantic coherence. With            gains do not transfer across domains. Even joint
SentenceBERT (Reimers and Gurevych, 2019),                 training on both domains does not close the gap,
each sentence can be mapped to a single vector.            especially on Stylo-Blog. This shows that lim-
Closer vectors indicate stronger semantic consis-          ited generalization ability continues to restrict the
tency between sentences. If these vectors lie on           mitigation of the inversion phenomenon.
a low-dimensional manifold, the text is more co-
                                                              Training Set     Stylo-Literary    Stylo-Blog       M4
herent, and the semantic flow is smoother. If the
                                                              None                 52.37           53.87          41.68
manifold has higher dimensionality, the text con-             M4                   53.33           64.77          99.94
tains larger semantic shifts. We segment each text            Stylo-Literary       99.96           67.95          70.72
into sentences using punctuation and encode them              Mixed                99.95           71.94          99.95
with a SentenceBERT model3 , then estimate the
                                                           Table 9: Performance of Roberta variants, trained on
manifold dimension for each group. Results are
                                                           different data.
presented in Table 8. For MGT, coherence remains
lower in general domains, but in personalized do-
mains, it becomes higher than that of HWT. This
further suggests that inverted features are related to
both lexical diversity and semantic coherence.

E.4 Towards Mitigating the Feature Inversion
    Phenomenon
We suggest that finetuning on highly personalized
text can improve detector accuracy within the tar-
get domain, but the improvement does not transfer
across domains. Training on one domain does not
yield gains in another, and joint training across do-
mains cannot overcome the model’s inherent limits
in generalization. Thus, training alone cannot fully
address the feature inversion phenomenon. An ef-
fective solution still requires either a method that
directly captures inverted feature behavior or a de-
tector that avoids relying on such unstable cues.
   We evaluate three finetuning variants of Roberta.
For M4, same as in Appendix B.3, each subset is
randomly split by selecting 1,000 samples for test-
ing, with all remaining samples used for training.
StyloBench is split in the same way. The first
variant is trained only on M4, the second only on
   3
       Here we choose the all-MiniLM-L6-v2 model.

                                                      43161
              Author
                       J.A     C.D       F.D       P.L   B.S      J.S    M.T     Avg.
  Detector
                                     Llama-3.1-8B
  Entropy              71.91   57.64    44.19    58.80   52.07   52.12   49.85   55.23
  Lastde               15.17   72.96    86.64    72.80   85.08   73.41   83.10   69.88
  Lastde++             12.85   58.34    76.84    58.45   76.40   66.63   73.17   60.38
  Log-Likelihood        5.33   31.81    52.93    32.42   45.10   44.07   44.47   36.59
  LogRank               6.07   34.62    54.38    34.35   47.56   45.67   47.08   38.53
  Detect-LRR           13.23   46.21    57.74    41.72   55.74   50.79   54.67   45.73
  Fast-DetectGPT        8.02   27.46    44.01    31.84   44.26   37.03   39.88   33.22
                                         Phi-4
  Entropy              50.79   57.71    44.76    50.86   54.62   52.45   52.24   51.92
  Lastde               25.83   65.61    78.99    66.94   78.14   66.27   77.95   65.67
  Lastde++             13.40   42.14    61.89    43.13   60.90   51.73   59.78   47.57
  Log-Likelihood        9.39   25.97    43.53    31.28   34.01   38.76   33.63   30.94
  LogRank              11.41   28.60    44.26    32.22   35.73   39.98   36.02   32.60
  Detect-LRR           26.85   40.34    47.65    36.90   43.69   44.38   44.56   40.62
  Fast-DetectGPT        6.08   15.61    24.42    15.05   25.34   21.08   21.67   18.47
                                       Qwen-3-4B
  Entropy              70.23   80.26    71.89    75.36   79.37   73.63   82.53   76.18
  Lastde               23.59   60.30    72.78    68.88   76.44   61.58   74.43   62.57
  Lastde++              9.88   30.06    46.55    42.82   54.65   41.56   52.94   39.78
  Log-Likelihood        1.72    5.68    11.97     9.00   10.62   17.14    8.52    9.23
  LogRank               2.42    7.15    12.44     9.90   12.23   18.68   10.26   10.44
  Detect-LRR           11.67   17.30    19.39    17.96   23.16   26.64   19.88   19.43
  Fast-DetectGPT        2.91    5.29     8.67     8.78   15.34    8.26   11.72    8.71

Table 10: Full AUROC results on Stylo-Literary, where generators are highlighted .




                                        43162
                 Subdomain
                               arXiv    PeerRead         Reddit      WikiHow      Wikipedia      Avg.
Detector
                                           BLOOMz
Entropy                        33.95      23.66           23.82       41.90            83.33     41.33
Lastde                         98.98      98.94           96.38       55.84            90.03     88.03
Lastde++                       98.56      83.96           79.51       52.57            89.98     80.91
Log-Likelihood                 88.71      68.97           64.56       50.05            26.44     59.75
LogRank                        94.39      84.96           80.29       51.85            35.62     69.42
Detect-LRR                     98.93      98.56           97.42       57.08            69.69     84.34
Fast-DetectGPT                 96.04      46.73           31.23       25.41            75.66     55.01
                                           ChatGPT
Entropy                        61.64      4.21            10.35       7.04             48.49     26.35
Lastde                         99.00      99.00           99.37       92.62            97.40     97.48
Lastde++                       99.85      99.85           99.72       94.86            99.07     98.67
Log-Likelihood                 89.13      99.45           98.98       96.57            84.69     93.76
LogRank                        91.48      99.51           99.14       96.26            88.29     94.94
Detect-LRR                     94.08      99.29           98.96       93.02            95.32     96.13
Fast-DetectGPT                 99.93      99.92           99.84       96.22            99.03     98.99
                                               Cohere
Entropy                        64.16      14.39           28.84       6.62             45.16     31.83
Lastde                         95.91      97.28           99.67       99.57            96.01     97.69
Lastde++                       98.50      95.93           98.74       99.90            98.04     98.22
Log-Likelihood                 85.67      97.02           96.08       99.43            87.39     93.12
LogRank                        88.24      96.92           96.38       99.56            89.97     94.21
Detect-LRR                     90.59      95.28           96.13       99.37            93.04     94.88
Fast-DetectGPT                 99.50      97.00           99.20       99.93            98.30     98.78
                                               Davinci
Entropy                        78.65      19.92           17.00       23.26            61.68     40.10
Lastde                         50.53      99.49           94.32       85.46            88.73     83.70
Lastde++                       41.47      99.81           98.34       87.80            94.64     84.41
Log-Likelihood                 21.97      99.11           95.22       84.26            63.40     72.79
LogRank                        20.68      99.30           95.39       83.46            67.08     73.18
Detect-LRR                     20.29      99.25           93.77       78.75            78.10     74.03
Fast-DetectGPT                 44.09      99.91           98.72       89.36            94.29     85.28

           Table 11: Full AUROC results on M4, where generators are highlighted .




Detector      Generator        J.A     C.D        F.D        P.L      B.S       J.S       M.T    Avg.
              Llama-3.1-8B     35.09   66.87     68.81      46.90     64.12    50.71     63.81   56.62
Roberta       Phi-4            46.23   55.77     61.65      36.71     55.15    45.10     54.50   50.73
              Qwen3-4B         58.82   58.25     54.92      37.25     57.25    45.75     56.27   52.64
              Llama-3.1-8B     68.98   65.31     61.80      66.34     71.73    64.02     63.21   65.91
DeTeCtive     Phi-4            63.63   63.09     68.25      65.75     69.15    63.40     65.10   65.48
              Qwen3-4B         82.99   77.16     77.41      71.48     75.94    74.01     70.29   75.61

              Table 12: Results of training-based detectors on Stylo-Literary.




             Detector     Claude3.7    Claude4      GPT-4o          Qwen2.5-72B        Avg.
             Roberta         47.38      57.33            59.40         94.99           64.78
             DeTeCtive       43.97      45.06            47.68         60.39           49.28

                Table 13: Results of training-based detectors on Stylo-Blog.


                                               43163
Detector       Generator    arXiv    PeerRead     Reddit   WikiHow      Wikipedia      Avg.
               Davinci       99.33     100.00     100.00     100.00        99.98        99.86
               Cohere        99.92      99.99      99.95     100.00        99.77        99.93
Roberta
               ChatGPT      100.00     100.00     100.00     100.00        99.95        99.99
               BLOOMZ       99.98      100.00     100.00     100.00       100.00       100.00
               Davinci       21.04     99.56       71.45     38.15        49.12        55.86
               Cohere        67.04     98.64       86.20     76.87        40.97        73.94
DeTeCtive
               ChatGPT       89.73     99.83       80.51     39.62        56.75        73.29
               BLOOMZ        70.95     96.80       87.49     49.23        91.62        79.22

          Table 14: Results of training-based detectors on the English subset of M4.




                                           43164
        Table 15: Examples of Stylo-Blog. The first 30 tokens used to generate MGTs are bolded.
Model          Text
                                                          Human
Human          There is so much on my mind these days... So much that I can’t seem to form a clear thought. I want so
               badly to move on with my life, but habits and people and I, myself, keep pulling me back. I know what I
               need to do, but it’s almost like I am afraid to take that step. I’ve always done the safe thing, made the safe
               choices. I’ve always done what was expected of me. And now that I am finally trying to step out on my
               own, I’m being told that I am running away. As much as I know that I need to do this, I still have those
               same childish fears that I’ve always had. I love my family, I love my friends, but I use them as a crutch. I
               use them as the reasons to stay in my comfort zone. I use them as my excuses to not step into that
               shadowy place just beyond my line of sight. I am not running away from anything, well, maybe some
               things, but sometimes, running away is the only way to set yourself free. I’ve prayed and prayed, begged
               and pleaded with God to not tell me what I already know. There is no way to deny that I know where my
               life is going. The only way that I can get to where I truly need to be is to walk away from everything that
               I know, to take that first blind step into my future. And the only way to do that is to put my complete trust
               and total faith in God.
                                                       Machine
                                                                                                 Continued on next page




                                                         43165
                               Table 15: Examples of Stylo-Blog (continued)
Model         Text
Qwen2.5-72B   There is so much on my mind these days... So much that I can’t seem to form a clear thought. I
              want so badly to share all these swirling emotions and thoughts, but the words just don’t seem to come.
              It feels like a storm is brewing inside me, with no outlet in sight. The more I try to wrap my head around
              everything, the more I feel like I’m losing my grip on the present. \n\nI’ve been thinking a lot about the
              people in my life recently. The relationships that have shaped me, the ones that have endured through
              thick and thin, and the ones that have faded into the background. It’s funny, how the people who are
              closest to you can be the ones you struggle to open up to the most. I find myself holding back, afraid of
              what will happen if I let it all out. But then, there are moments, like that one in church, where everything
              bubbles up to the surface and I can’t hold it back.\n\nLast Sunday, I was standing there, singing those
              familiar worship songs, and it was like I was transported. The words, \"I walk by faith, each step by faith;
              to live by faith, I put my trust in You,\" echoed in my heart. And in that moment, I felt it. I looked around,
              and the faces of the people surrounding me were both familiar and strange. Familiar, because they’ve
              been a part of my life for so long. Strange, because life has a way of changing us, sometimes so subtly
              that we don’t even notice until we stop and really look.\n\nOf the couple hundred people in that room, I
              only knew about half. Of those, there were the people who have been constants in my life: the adults who
              have watched me grow from a girl into a woman, and the children who I have watched grow from
              toddlers to young adults. There were the people who have stood by me through my weakest moments,
              holding me up when I thought I would fall. And there were those who I have supported, giving them a bit
              of my strength when they needed it most.\n\nBut there was one person, one person who I couldn’t talk to,
              the one person I wasn’t sure if I could leave. And in that moment, the tears started to sting my eyes. I
              couldn’t reach out, couldn’t communicate what I was feeling. The song ended in fellowship time, and I
Claude-4      There is so much on my mind these days... So much that I can’t seem to form a clear thought. I
              want so badly to move on with my life, but I feel like I’m stuck in this weird limbo where nothing makes
              sense anymore. You know that feeling when you’re standing at a crossroads and every direction looks
              both terrifying and exciting at the same time? That’s exactly where I am right now.\n\nI keep thinking
              back to all those times when I was so sure I had everything figured out. Remember when I was eighteen
              and thought I knew exactly how my life would unfold? Ha! If only that naive girl could see me now.
              She’d probably be shocked at how different things turned out, but maybe she’d also be proud of the
              woman I’ve become through all the unexpected twists and turns.\n\nThe truth is, I’m tired of feeling like
              I’m waiting for permission to live my own life. Does that make sense? It’s like I’ve been holding my
              breath, waiting for some magical moment when everything will click into place and I’ll suddenly know
              what I’m supposed to do next. But what if that moment never comes? What if this uncertainty is just part
              of being human, part of growing up, part of learning to trust yourself even when you can’t see the whole
              staircase?\n\nI was talking to my mom the other day, and she said something that really stuck with me.
              She said, \"Honey, sometimes moving on doesn’t mean you have all the answers. Sometimes it just
              means you’re brave enough to take the next step without
Claude-3.7    There is so much on my mind these days... So much that I can’t seem to form a clear thought. I
              want so badly to just sit and process everything, but life keeps moving at this relentless pace that doesn’t
              allow for much reflection.\n\nYou know that feeling when your brain is like a browser with too many tabs
              open? That’s me right now. A hundred thoughts racing, memories surfacing at odd moments, worries
              about tomorrow pressing in, and in the midst of it all, trying to remember if I picked up milk at the store
              yesterday.\n\nI found myself driving home from work yesterday, and I couldn’t even tell you what streets
              I took. My body was on autopilot while my mind wandered through a maze of its own making. It’s scary
              sometimes, how disconnected we can become from the present moment.\n\nLast night, I was folding
              laundry – such a mundane task – when suddenly tears were streaming down my face. Not sad tears
              necessarily, just... release tears. The kind that come when your heart is too full of something unnamed.
              The kind that need no explanation or justification. They just are.\n\nAnd in that moment, with a
              half-folded t-shirt in my hands, I realized how much I’ve been holding in. How many emotions I’ve been
              packing away neatly like these clothes, trying to make everything fit in the limited space I’ve allowed
              myself.\n\nI think we all do this sometimes. We keep pushing forward, keep smiling, keep showing up for
              the people who need us. We sing the worship songs on Sunday morning, we make the lunches, we answer
              the emails, we check the boxes. And somewhere in all of that, our own hearts get a little lost.\n\nI’m
              looking at my Bible sitting on the nightstand. It’s been there for days, untouched. Not because I don’t
              want to open it, but because I’m afraid of what might happen if I do. If I get still enough to listen, what
              will God say? What will He ask of me? What emotions might surface that I’ve been working so hard to
              keep submerged?\n\nI walk by faith, each step by faith.\n\nThose words from the song at church keep
              coming back to me. Walking by faith doesn’t always mean having clear direction. Sometimes it means
              putting one foot in front of the other when the path ahead is completely obscured. Sometimes it means
              trusting that even in the mental chaos, God

                                                                                                Continued on next page




                                                       43166
                          Table 15: Examples of Stylo-Blog (continued)
Model    Text

GPT-4o   There is so much on my mind these days... So much that I can’t seem to form a clear thought. I
         want so badly to put it all into words, but every time I try, they swirl around like leaves caught in an
         autumn breeze. It’s as if the very alphabet refuses to settle on the page, preferring instead to dance in
         chaos. And amidst this whirlwind, I find myself yearning for clarity, for a moment of stillness where I can
         breathe and just... be.\n\nSometimes I think about how life used to be so simple, yet we couldn’t wait to
         grow up. Oh, how naive we were! The dreams of adulthood seemed wrapped in wonder and possibility,
         but now I see that they come twined with responsibility and introspection. I pause, caught in the space
         between what was and what is, longing for that childlike clarity once more.\n\nThis introspection takes
         me back to those quiet moments in the pews of the old church, where the weight of expectations lifted
         slightly with each hymn sung. There, in the company of familiar faces, I found something akin to peace.
         We were together, bound not just by belief but by the shared journey of faith and vice-versa, bearing the
         burdens of our collective humanity.\n\nYet these days, everywhere I turn, there seems to be complexity
         and noise. The world spins faster, and sometimes I feel like an outsider peering in through fogged glass. I
         find solace in small acts: the laughter of a child, the rustle of leaves, the comforting ordinariness of a
         daily routine. I seek meaning in the minutiae, an anchor in the intricate tapestry of life.\n\nI’ve been
         volunteering more with the local youth group, hoping to give back some of what was freely given to me.
         And, oh, how their perspectives refresh my own! Their unfiltered view of the world serves as a reminder
         of what truly matters. I watch them, these bundles of potential and enthusiasm, and think about
         possibilities — not just their possibilities, but mine too. \n\nHow often do we, as adults, lose sight of our
         dreams? They get locked away like treasures in a dusty attic, while we pursue notions of success that may
         not really belong to us. And yet, every now and then, I’m reminded to dust them off, to recall who I truly
         am beyond the roles and titles accumulated over the years. It’s like catching a glimpse of your reflection
         in




                                                  43167
  Table 16: Examples of Stylo-Literary. The first 30 tokens used to generate MGTs are bolded.
Source    Text
                          Human Author: Mark Twain Generator: Llama-3.1-8B
Human     “Say, wouldn’t it ’a’ been nuts if he’d a-been here last night ” “Oh, by George, but wouldn’t it” said
          Ferguson “Then we’d have seen scientific work Intellect–just pure intellect–away up on the upper levels,
          dontchuknow Archy is all right, and it don’t become anybody to belittle him, I can tell you But his gift is
          only just eyesight, sharp as an owl’s, as near as I can make it out just a grand natural animal talent, no
          more, no less, and prime as far as it goes, but no intellect in it, and for awfulness and marvelousness no
          more to be compared to what this man does than–than–Why, let me tell you what he’d have done He’d
          have stepped over to Hogan’s and glanced–just glanced, that’s all–at the premises, and that’s enough See
          everything Yes, sir, to the last little detail; and he’ll know more about that place than the Hogans would
          know in seven years Next, he would sit down on the bunk, just as ca’m, and say to Mrs Hogan–Say, Ham,
          consider that you are Mrs Hogan I’ll ask the questions; you answer them ” “All right; go on ” “’Madam,
          if you please–attention–do not let your mind wander Now, then–sex of the child ’ “’Female, your Honor ’
          “’Um–female Very good, very good Age ’ “’Turned six, your Honor ’ “’Um–young, weak–two miles
          Weariness will overtake it then It will sink down and sleep We shall find it two miles away, or less Teeth ’
          “’Five, your Honor, and one a-coming ’ “’Very good, very good, very good, indeed ’ You see, boys, he
          knows a clue when he sees it, when it wouldn’t mean a dern thing to anybody else ’Stockings, madam
          Shoes ’ “’Yes, your Honor–both ’ “’Yarn, perhaps Morocco ’ “’Yarn, your Honor And kip ’ “’Um–kip
          This complicates the matter However, let it go–we shall manage Religion ’ “’Catholic, your Honor ’
          “’Very good Snip me a bit from the bed blanket, please Ah, thanks
Machine   “Say, wouldn’t it ’a’ been nuts if he’d a-been here last night ” “Oh, by George, but wouldn’t that be
          too many, though I like to talk it out once, just for pastime; and sometimes, when I’m alone in the shop, I
          try to make it all come again in dialog, and then it seems as if it had, and I dream about it nights You can
          imagine yourn over again, same as I do When I get tired of myn, I take up Huck’s ” “Why, it was the
          most–” “Yes–incoherency, that’s what it was They just rambled around from one thing to another, and
          never landed in the same place twice Let it alone; it ain’t anybody’s fault Consider them illiterates Now
          you shell notice, Astronomical would naturally drop into their own language; and he did Then he would
          always try to correct himself, and begin to sling off parts of words that he thought belonged to English,
          but didn’t No, he couldn’t put together so you could remember anything he’d said, within fifteen minutes
          after it was done; and he couldn’t get his sentence started twice, right straight through So somebody else
          would interrupt and say, “What’s de use, let him ’lone–dey can’t git shet o’ de subject,” or something like
          that, you know, and then start himself and go to talking You see, he tried to talk English all the time, only
          he couldn’t somehow It got him down So he took to talking dialect, because it was easier and convenient,
          you know Well, as soon as he’d break loose, there warn’t no getting him to his english again He couldn’t
          seem to settle down to it We all used to go for him and rush him every time he’d begin to talk English,
          and force him to talk dialect The Widow Douglas used to break in on me dreadful at first, with her
          English; but she got the hang of it a deal sooner than any of the rest She said she couldn’t stand it, and she
          warned me off from trying to make a body talk dialect that hadn’t been brought up to it, I might as well
          atrophy an elephant Yes, even the widow: everybody was down to the other fellow’s level, before we got
          through And some better’n others, too Present

                            Human Author: Jane Austen Generator: Llama-3.1-8B
Human     ” So far her improvement was sufficient–and in many other points she came on exceedingly well;
          for though she could not write sonnets, she brought herself to read them; and though there seemed no
          chance of her throwing a whole party into raptures by a prelude on the pianoforte, of her own
          composition, she could listen to other people’s performance with very little fatigue Her greatest
          deficiency was in the pencil–she had no notion of drawing–not enough even to attempt a sketch of her
          lover’s profile, that she might be detected in the design There she fell miserably short of the true heroic
          height At present she did not know her own poverty, for she had no lover to portray She had reached the
          age of seventeen, without having seen one amiable youth who could call forth her sensibility, without
          having inspired one real passion, and without having excited even any admiration but what was very
          moderate and very transient This was strange indeed But strange things may be generally accounted for if
          their cause be fairly searched out There was not one lord in the neighbourhood; no–not even a baronet
          There was not one family among their acquaintance who had reared and supported a boy accidentally
          found at their door–not one young man whose origin was unknown Her father had no ward, and the
          squire of the parish no children But when a young lady is to be a heroine, the perverseness of forty
          surrounding families cannot prevent her Something must and will happen to throw a hero in her way Mr
          Allen, who owned the chief of the property about Fullerton, the village in Wiltshire where the Morlands
          lived, was ordered to Bath for the benefit of a gouty constitution–and his lady, a good-humoured woman,
          fond of Miss Morland, and probably aware that if adventures will not befall a young lady in her own
          village, she must seek them abroad, invited her to go with them Mr and Mrs Morland were all
          compliance, and Catherine all happiness




                                                      43168
                            Examples of Stylo-Literary, continued from last page.
Source    Text

Machine   ” So far her improvement was sufficient–and in many other points she came on exceedingly well;
          for though she could not write sonnets, she brought herself to read them with feeling, and the history
          of her first setting out to excel was soon written, and made into a narrow little volume, two volumes in
          quinto, and all in her own hand She had no notice of it herself, till her mother one day said, “Ellen, may I
          see your drawing-room window ” And when Elizabeth turned her hand out of the draw- ing-book, some
          elegant little figure of a tower or grotto which Miss Crawford had criticising, there, without thinking, lay
          the pretty little volume The look which Elizabeth instantly raised to comprehend the business, remained
          some time on Miss Crawford’s face, and hers was AN UNPLEASANT ONE It spoke meekness,
          submitting, shy distrust, penetrating curiosity, but yet grudging invitation A second or two passed in
          complete silence before either of them spoke, and then it was only, “Well, Ellen –I thought you had been
          writing ” “Oh I did, indeed, I was so much concerned about it ” “And have you explained everything to
          Mr Morland What does he say ” “He is very good-aided But I have been used to have poorer friends My
          family have been poor, for years ” “Yes; that is, you have no father or brother living I beg your pardon
          You are on the spot yourself, which is always something in a friend He must be a singular man–a silent,
          melancholy, earnest, persevering, thinking, practicing man–his mind completely under his own
          control–somewhat severe, perhaps–but with great energy–great forbearance–great capacity of enjoying
          the thing that he likes –provided a woman’s wishes were consulted but what do I tell you They never
          ARE At this rate you will never know Badly as we judge alone, we should never dare to judge till

                                 Human Author: Jane Austen Generator: Phi-4
Human     ” “I am very sorry for it,” said Catherine dejectedly; “if I had known this before–” “Perhaps,” said
          Miss Tilney in an embarrassed manner, “you would be so good–it would make me very happy if–” The
          entrance of her father put a stop to the civility, which Catherine was beginning to hope might introduce a
          desire of their corresponding After addressing her with his usual politeness, he turned to his daughter and
          said, “Well, Eleanor, may I congratulate you on being successful in your application to your fair friend ”
          “I was just beginning to make the request, sir, as you came in ” “Well, proceed by all means I know how
          much your heart is in it My daughter, Miss Morland,” he continued, without leaving his daughter time to
          speak, “has been forming a very bold wish We leave Bath, as she has perhaps told you, on Saturday
          se’nnight A letter from my steward tells me that my presence is wanted at home; and being disappointed
          in my hope of seeing the Marquis of Longtown and General Courteney here, some of my very old friends,
          there is nothing to detain me longer in Bath And could we carry our selfish point with you, we should
          leave it without a single regret Can you, in short, be prevailed on to quit this scene of public triumph and
          oblige your friend Eleanor with your company in Gloucestershire I am almost ashamed to make the
          request, though its presumption would certainly appear greater to every creature in Bath than yourself
          Modesty such as yours–but not for the world would I pain it by open praise If you can be induced to
          honour us with a visit, you will make us happy beyond expression ’Tis true, we can offer you nothing like
          the gaieties of this lively place; we can tempt you neither by amusement nor splendour, for our mode of
          living, as you see, is plain and unpretending; yet no endeavours shall be wanting on our side to make
          Northanger Abbey not wholly disagreeable ” Northanger Abbey These were thrilling words, and wound
          up Catherine’s feelings to the highest point of ecstasy Her grateful and gratified heart could hardly
          restrain its expressions within the language of tolerable calmness To receive so flattering an invitation To
          have her company so warmly solicited
Machine   ” “I am very sorry for it,” said Catherine dejectedly; “if I had known this before–” “Perhaps,” said
          Miss Tilney, with an affectionate smile, “it would not have made you more easy on the subject ” Her
          brother instantly interfered; “Do you advise her to tell me of it then ” “By no means, if she can help it The
          disadvantage is at least mutual There need be no consequence but what will be attended by pleasure ” But
          though the matter was apparently arranged in a moment, and they all three seemed most happily
          reconciled to each other, there yet lingered in Catherine’s mind some feelings which required the
          subduing influence of a good night’s rest to put them quite to flight; and, though without exactly knowing
          why, as soon as she left the room, and while slowly ascending the staircase, she felt convinced that
          General Tilney could never like her, or think her pretty –They had one family friend, besides these
          gentlemen, who resided among them Mr Frederick Tilney, their eldest son, was the rector of the parish, of
          which his father was patron A young man very like his cousin John, but handsomer than him He had a
          great deal of the same manner–and every body thought him extremely agreeable, except Catherine She
          did not like him; and, now that Edmund Bertram was removed from her acquaintance, she wished very
          much that _he_ might never return from Oxford It appeared afterwards that he must often visit his
          relations in Gloucestershire, and this raised a thousand unpleasant questions: Whom would he come with
          Why was not his sister invited also Would he bring Anne Heretitia Mention of Mr Allen did so little
          honour to either sex, to human nature in general, that Catherine was rather glad the circumstance was
          suppressed They sat down to table, twenty-three in number, and in a style of luxury, which, to Catherine,
          with the exception of her first morning’s entertainment, was peculiar Having been indulged with
          uncommon orders in her favourite toy-shop only two days before, she knew how much superior was cold
          beef, or cold lamb, at any time of life, to the daintiest dinner that ever was cooked; and being prepared,
          therefore, to find fault, nothing could be more exquisite than her admiration In addition to every other



                                                      43169
                           Examples of Stylo-Literary, continued from last page.
Source    Text

                              Human Author: Bernard Shaw Generator: Phi-4
Human     We shall come to the question of the economic dependence of women on men later on; but at
          present we had better confine ourselves to the theories of marriage which we are not ashamed to
          acknowledge and defend, and upon which, therefore, marriage reformers will be obliged to proceed We
          may, I think, dismiss from the field of practical politics the extreme sacerdotal view of marriage as a
          sacred and indissoluble covenant, because though reinforced by unhappy marriages as all fanaticisms are
          reinforced by human sacrifices, it has been reduced to a private and socially inoperative eccentricity by
          the introduction of civil marriage and divorce Theoretically, our civilly married couples are to a Catholic
          as unmarried couples are: that is, they are living in open sin Practically, civilly married couples are
          received in society, by Catholics and everyone else, precisely as sacramentally married couples are; and
          so are people who have divorced their wives or husbands and married again And yet marriage is enforced
          by public opinion with such ferocity that the least suggestion of laxity in its support is fatal to even the
          highest and strongest reputations, although laxity of conduct is winked at with grinning indulgence; so
          that we find the austere Shelley denounced as a fiend in human form, whilst Nelson, who openly left his
          wife and formed a menage a trois with Sir William and Lady Hamilton, was idolized Shelley might have
          had an illegitimate child in every county in England if he had done so frankly as a sinner His
          unpardonable offence was that he attacked marriage as an institution We feel a strange anguish of terror
          and hatred against him, as against one who threatens us with a mortal injury What is the element in his
          proposals that produces this effect The answer of the specialists is the one already alluded to: that the
          attack on marriage is an attack on property; so that Shelley was something more hateful to a husband than
          a horse thief: to wit, a wife thief, and something more hateful to a wife than a burglar: namely, one who
          would steal her husband’s house from over her head, and leave her destitute and nameless on the streets
Machine   We shall come to the question of the economic dependence of women on men later on; but at
          present we had better confine ourselves to the theories of Mrs Warren’s profession As far as its
          religious aspect goes, it seems, so far as I can make out, to be a practice of prostitution in which no
          payment is accepted and from which the practitioner expects nothing but damnation This has never been
          a very popular method: St Paul tells us that prostitutes were always ready enough to trade for money
          without asking for any recompense in heaven Consequently it was not until Mr Gladstone found out,
          when he visited Florence in 1897, that Fra Angelico represented angels with wings instead of tails, that a
          reaction set in against Dante, who did not take this view of things There are many saints in our calendar,
          male and female, whose sanctity has apparently depended largely upon their experience of this form of
          the calling But these records are extremely obscure, because they all insist much more strongly than
          Dante does on the fact that there is only one thing wrong with vice: that is, that it should pay Now in all
          discussions as to whether there is anything fundamentally wrong with human nature–the strongest
          practical grounds being generally alleged by those who believe nothing whatever in its fundamental
          soundness–it is necessary to have a common denominator Both sides must agree what ẅrongm̈eans
          before they can go on to argue about the degree in which it exists If there is something really wrong with
          human nature, then, logically, no human conduct or instinct or desire can possibly be regarded as
          infallibly right The immorality of an action cannot depend entirely on the motive behind it You may begin
          by admitting that if you do certain things with a good motive your act is not sinful; but still, you cannot
          admit that such acts done with a bad motive are not wicked Why should not the most disinterested and
          self-sacrificing promiscuity be just as vicious as the greediest and vilest lust And why should not the
          vilest and greediest lust be just as virtuous as the purest devotion Can anyone answer these questions
          sensibly (I am sure nobody ever tries) except on the

                           Human Author: Bernard Shaw           Generator: Qwen3-4B




                                                      43170
                            Examples of Stylo-Literary, continued from last page.
Source    Text
Human      We shall come to the question of the economic dependence of women on men later on; but at
          present we had better confine ourselves to the theories of marriage which we are not ashamed to
          acknowledge and defend, and upon which, therefore, marriage reformers will be obliged to proceed We
          may, I think, dismiss from the field of practical politics the extreme sacerdotal view of marriage as a
          sacred and indissoluble covenant, because though reinforced by unhappy marriages as all fanaticisms are
          reinforced by human sacrifices, it has been reduced to a private and socially inoperative eccentricity by
          the introduction of civil marriage and divorce Theoretically, our civilly married couples are to a Catholic
          as unmarried couples are: that is, they are living in open sin Practically, civilly married couples are
          received in society, by Catholics and everyone else, precisely as sacramentally married couples are; and
          so are people who have divorced their wives or husbands and married again And yet marriage is enforced
          by public opinion with such ferocity that the least suggestion of laxity in its support is fatal to even the
          highest and strongest reputations, although laxity of conduct is winked at with grinning indulgence; so
          that we find the austere Shelley denounced as a fiend in human form, whilst Nelson, who openly left his
          wife and formed a menage a trois with Sir William and Lady Hamilton, was idolized Shelley might have
          had an illegitimate child in every county in England if he had done so frankly as a sinner His
          unpardonable offence was that he attacked marriage as an institution We feel a strange anguish of terror
          and hatred against him, as against one who threatens us with a mortal injury What is the element in his
          proposals that produces this effect The answer of the specialists is the one already alluded to: that the
          attack on marriage is an attack on property; so that Shelley was something more hateful to a husband than
          a horse thief: to wit, a wife thief, and something more hateful to a wife than a burglar: namely, one who
          would steal her husband’s house from over her head, and leave her destitute and nameless on the streets
Machine   We shall come to the question of the economic dependence of women on men later on; but at
          present we had better confine ourselves to the theories of immorality and bad manners which is, in
          short, one single doctrine which has grown by multiplication into an infinity of articles To all these it may
          be said that the theory to which they are attributable is the theory of physical inferiority, moral incapacity,
          inhumanity or mere unskilled destructiveness The elementary creed includes not only the theory of male
          superiority as actually evidenced in modern warfare, but also such absurd assumptions as that in spite of
          modern civilized warfare women cannot fight and must therefore remain separate from mankind even if
          they have no more powerful reason for doing so; or again that the splendid courage displayed by the
          women who stood out during the Great War was produced by a preternatural instinctive force: in other
          words, a sexual instinctuality, which is declared to be incapable of being cultivated by education All this
          is gobbledygook made up by professional female critics to please their paymasters The truth in short is
          what Adam Smith, long ago put it thus T̈o man’s nature is due his love of dominion over woman He may,
          and I believe he ought sometimes to, allow her freedom of choice in marriage matters; but when he does
          this, he leaves his wife in much the same position as if she were married to him against her will A great
          deal of what we call justice or respectability between husband and wife really comes from a strong sense
          of self-reverence, accompanied by an equally strong sense of the infamy of a lie T̈HE HOMO SAPIENS
          MUSICAL PARADISE Some people feel perfectly happy in the belief that women are more refined than
          men because they are less brutal, less selfish, less rapacious In itself this idea makes some sort of sense;
          but it has been found that it does not explain everything Every human being desires, sooner or later, some
          sort of gratification Men usually seek satisfaction from sex activity, and sometimes from sublimated
          forms of that activity (theology, science, music); whereas women often find no satisfactory substitute
          except bare animal




                                                       43171


## Responsible NLP Checklist full text

Responsible NLP Checklist
Paper title: When Personalization Tricks Detectors: The Feature-Inversion Trap in Machine-Generated
Text Detection
Authors: Lang Gao, Xuhui Li, Chenxi Wang, Mingzhe Li, Wei Liu, Zirui Song, Jinghui Zhang, Rui Yan,
Preslav Nakov, Xiuying Chen
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

  ✓ A2. Did you discuss any potential risks of your work?
  □
        The limitations section
✓ B. Did you use or create scientific artifacts? (e.g. code, datasets, models)
□
 ✓ B4. Did you discuss the steps taken to check whether the data that was collected/used contains any
 □
        information that names or uniquely identifies individual people or offensive content, and the steps
        taken to protect/anonymize it?
        Section 3.1
  ✓ B6. Did you report relevant statistics like the number of examples, details of train/test/dev splits, etc.
  □
        for the data that you used/created?
        Section 3
✓ C. Did you run computational experiments?
□
 ✓ C2. Did you discuss the experimental setup, including hyperparameter search and best-found
 □
        hyperparameter values?
        section 5.2.3
  ✓ C3. Did you report descriptive statistics about your results (e.g., error bars around results, summary
  □
        statistics from sets of experiments), and is it transparent whether you are reporting the max, mean,
        etc. or just a single run?
        section 5.2

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

✓ E. Did you use AI assistants (e.g., ChatGPT, Copilot) in your research, coding, or writing?
□
 ✓ E1. If you used AI assistants, did you include information about their use?
 □
       For coding


## Extraction verification

- **Beginning checked:** Rendered paper page 1 was compared with the extraction; title, authors, affiliations, abstract, Figure 1 and caption, Introduction, proceedings footer, page range, and first page number are present.
- **Middle checked:** Rendered paper page 15 was compared with the extraction; Table 6, AUROC explanation, correlation formulas, Section C.3, Section D, and page number 43157 are present and legible.
- **End checked:** Rendered paper page 29 was compared with the extraction; the continued Stylo-Literary example table, human and machine labels, final page number 43171, and terminal form-feed are present.
- **Checklist checked:** `pdfinfo` reports two A4 pages. Both pages were rendered and compared with the extraction; all responses through the AI-assistant-use disclosure are present.
- **Structure checked:** `pdfinfo` reports 29 A4 paper pages. The paper extraction includes Sections 1-7; Limitations; Ethical Considerations; References; Appendices A-E; Tables 1-16; Figures 1-13; footnotes; equations; prompt text; and long human and machine examples in the same broad order as the PDF. The extracted paper text contained 1,682 lines, 18,218 words, and 151,870 bytes before snapshot metadata and checklist text were added.
- **Known omissions:** No source text from the paper or checklist is omitted. Figure pixels, plotted marks, colors, checkbox typography, and exact page geometry are not reproduced in Markdown; they remain in the preserved PDF attachments. The plain-text extraction mechanically interleaves some two-column content and line-wraps wide tables, formulas, and examples.

## Preserved attachments

| Path | Role in the source | SHA-256 | Preservation / extraction notes |
|---|---|---|---|
| `snapshots/attachments/gao-personalization-tricks-detectors-acl-2026.pdf` | Authoritative 29-page ACL proceedings PDF, including figures, tables, equations, prompts, appendices, and examples | `fe7ca9654b999e7e5fa263852d3ceb1c80fd57b720b95c7b2eb15275b0d6e0bc` | Downloaded directly from ACL Anthology on 2026-07-15; embedded text extracted with `pdftotext -layout`; retained for visual and reading-order verification. |
| `snapshots/attachments/gao-personalization-tricks-detectors-responsible-nlp-checklist.pdf` | Authoritative two-page ACL Responsible NLP Checklist associated with the paper | `9761acf1d4ab1b51fe1484f6d23fcb9de689bf3edf13ef2533449418021f6ce4` | Downloaded from the ACL Anthology attachment URL on 2026-07-15; complete embedded text extracted with `pdftotext -layout`; both pages rendered and checked. |
