# GigaCheck: Detecting LLM-generated Content via Object-Centric Span Localization

- **Canonical URL:** https://aclanthology.org/2026.findings-acl.213/
- **Alternate access URLs:**
  - https://aclanthology.org/2026.findings-acl.213.pdf
  - https://aclanthology.org/attachments/2026.findings-acl.213.checklist.pdf
  - https://doi.org/10.18653/v1/2026.findings-acl.213
- **Author / owner:** Irina Tolstykh, Aleksandra Tsybina, Sergey Yakubson, Aleksandr Gordeev, Vladimir Dokholyan, and Maksim Kuprashevich
- **Publisher:** Association for Computational Linguistics
- **Published:** 2026-07
- **Retrieved:** 2026-07-15
- **Stable identifier:** DOI 10.18653/v1/2026.findings-acl.213; ACL Anthology ID 2026.findings-acl.213
- **Version / revision:** Findings of ACL 2026 proceedings version, pages 4349-4364
- **Extraction method:** First-party ACL proceedings PDF and ACL Responsible NLP Checklist PDF downloaded with `curl`; all 16 paper pages and both checklist pages extracted with Poppler `pdftotext -layout`; paper pages 1, 2, 8, and 16 and both checklist pages rendered with `pdftoppm` and visually compared with the extraction; `pdfinfo` and `pdfimages -list` checked structure and embedded images
- **Full-text status:** complete for the proceedings paper and its authoritative two-page Responsible NLP Checklist
- **Access and transformation notes:** The preserved text below contains the complete 16-page paper extraction followed by the complete two-page checklist extraction. Two-column reading order, line-break hyphenation, page numbers, and form-feed page breaks reflect `pdftotext -layout`. Figure pixels, bold span markings in Tables 15 and 16, checkbox typography, and exact page layout are not reproduced in the text extraction, so the authoritative PDFs are preserved as attachments. No OCR was used. The paper cites a public GitHub repository, but the repository was not used as evidence and was not recursively ingested.

## Full text

 GigaCheck: Detecting LLM-generated Content via Object-Centric Span
                           Localization

         Irina Tolstykh, Aleksandra Tsybina, Sergey Yakubson, Aleksandr Gordeev,
                        Vladimir Dokholyan, Maksim Kuprashevich

                                SALUTEDEV LLC, Tashkent, Uzbekistan
                                     Correspondence: irinakr4snova@gmail.com



                      Abstract                               Vasilatos et al., 2023). LLMs produce hallucina-
                                                             tions (Ji et al., 2023; Thorp, 2023) and outdated
    With the increasing quality and spread of LLM
                                                             information, thereby spreading incorrect knowl-
    assistants, the amount of generated content is
    growing rapidly. In many cases and tasks, such           edge. Detecting LLM-generated content remains
    texts are already indistinguishable from those           challenging, especially in mixed-authorship scenar-
    written by humans, and the quality of genera-            ios (Human-Machine collaborative texts), where
    tion continues to increase. At the same time,            existing document-level detectors lack sufficient
    detection methods are advancing more slowly              reliability (Liu et al., 2023c; Wu et al., 2023a).
    than generation models, making it challenging               Recent approaches have shifted towards analyz-
    to prevent misuse of generative AI technolo-
                                                             ing collaborative texts by identifying boundaries be-
    gies. We propose GigaCheck, a dual-strategy
    framework for AI-generated text detection. At            tween sections of different authorship (Zeng et al.,
    the document level, we leverage the represen-            2024b,a; Wang et al., 2023) or employing fine-
    tation learning of fine-tuned LLMs to discern            grained token classification to extract spans (Yin
    authorship with high data efficiency. At the             and Wang, 2026).
    span level, we introduce a novel structural adap-           In this paper, we propose a unified framework for
    tation that treats generated text segments as            generated text analysis, targeting both document-
    "objects." By integrating a DETR-like vision             level classification and fine-grained span-level lo-
    model with linguistic encoders, we achieve
                                                             calization. For the latter, we introduce a paradigm
    precise localization of AI intervals, effectively
    transferring the robustness of visual object de-         shift by reformulating text span detection as an ob-
    tection to the textual domain. Experimental              ject detection problem. We employ a DETR-based
    results across three classification and three lo-        architecture (Carion et al., 2020) that leverages
    calization benchmarks confirm the robustness             representations from a fine-tuned LLM to predict
    of our approach. The shared fine-tuned back-             character-based segments directly. Unlike previ-
    bone delivers strong accuracy in both scenarios,         ous sequence labeling methods that require manual
    highlighting the generalization power of the
                                                             post-processing to group tokens (Kushnareva et al.;
    learned embeddings. Moreover, we success-
    fully demonstrate that visual detection architec-        Zeng et al., 2024b; Wang et al., 2023), our encoder-
    tures like DETR are not limited to pixel space,          decoder transformer predicts continuous intervals
    effectively generalizing to the localization of          end-to-end.
    generated text spans. To ensure reproducibility             To keep the study focused and directly compa-
    and foster further research, we publicly release         rable with existing benchmarks, we limit this first
    our source code.                                         investigation to English texts; adapting GigaCheck
                                                             to new languages is straightforward and left for
1   Introduction
                                                             promising future work.
The rapid development of Large Language Mod-                    To assess our approach, we adopt a two–step
els (LLMs) has made their outputs difficult to               evaluation strategy. We begin with the challeng-
distinguish from human-written text, raising con-            ing span-level localization setting, demonstrat-
cerns about the spread of spam and misinforma-               ing that the proposed DETR head can precisely
tion (Mirsky et al., 2023; Hanley and Durumeric,             pinpoint LLM-generated spans across three Hu-
2024), fraud (Grbic and Dujlovic, 2023; Roy et al.,          man–Machine collaborative datasets. We then turn
2023), and academic cheating (Stokel-Walker,                 to three well-established binary-classification cor-
2022; Kasneci et al., 2023; Perkins et al., 2023;            pora. Although binary detection is less novel, these
                                                        4349
                 Findings of the Association for Computational Linguistics: ACL 2026, pages 4349–4364
                             July 2-7, 2026 ©2026 Association for Computational Linguistics
Figure 1: Overall architecture of GigaCheck framework. Document-level detection is performed by fine-tuning an
LLM. For span-level localization, we adopt a two-stage pipeline: (1) a fine-tuned LLM produces token embeddings,
and (2) a detection transformer treats generated spans as objects and directly predicts character-level intervals. FG
and BG denote the foreground and background labels assigned to each anchor.


experiments verify that the very same LoRA-tuned            classification (human vs. AI) (Zhang et al., 2024;
backbone used by the DETR head learns embed-                Liu et al., 2023c; Bhattacharjee and Liu, 2024;
dings that remain robust and discriminative for in-         Liu et al., 2023a; Uchendu et al., 2020) and multi-
dependent downstream tasks.                                 class tasks to identify the specific generation model
  Our contributions are:                                    (Uchendu et al., 2020, 2021, 2023; Wang et al.,
                                                            2024; Mitchell et al., 2023; Wu et al., 2023b).
    1. Object Detection paradigm for text spans.
                                                               Statistical methods (Mitchell et al., 2023;
       To the best of our knowledge, DETR-style
                                                            Gehrmann et al., 2019; Su et al., 2023; Fröhling and
       models have not yet been applied to locating
                                                            Zubiaga, 2021) use metrics like entropy, perplex-
       intervals within natural language texts. We
                                                            ity, and n-gram frequency, and typically require
       take this first step by adapting the architecture
                                                            access to the investigated LLMs. Neural-based ap-
       to detect LLM-generated segments as discrete
                                                            proaches (Antoun et al., 2023; Wang et al., 2024;
       objects, achieving strong results across three
                                                            Guo et al., 2023; Liu et al., 2023b; Zellers et al.,
       localization benchmarks. This approach elim-
                                                            2019; Solaiman et al., 2019; Uchendu et al., 2020),
       inates the need for heuristic post-processing
                                                            primarily using RoBERTa (Liu, 2019), provide
       common in token-classification methods.
                                                            more accurate results than statistical methods (Li
    2. Robust backbone for both detection and               et al., 2024; Liu et al., 2023b), but lack robustness
       classification. The same LoRA-tuned back-            (Li et al., 2024; Koike et al., 2024; Krishna et al.,
       bone delivers state-of-the-art performance on        2024; Chakraborty et al., 2023; Tulchinskii et al.,
       three binary-classification datasets, proving        2024). Recent works incorporate topological data
       that its embeddings transfer reliably between        analysis (TDA) (Uchendu et al., 2023; Kushnareva
       fine-grained localization and global document-       et al., 2021; Tulchinskii et al., 2024) or leverage
       level detection tasks.                               LLMs as detectors. The authors of Bhattachar-
                                                            jee and Liu (2024) apply GPT-3.5-turbo (OpenAI,
    3. Open Source Availability. To facilitate re-          2023a) and GPT-4 (OpenAI, 2023b) models for
       producibility and encourage future develop-          the zero-shot binary classification task and demon-
       ments in the field, we make our source code          strate that both models have a very high misclas-
       publicly available at https://github.com/            sification rate. Our method extends neural-based
       ai-forever/gigacheck.                                detectors by fine-tuning an LLM to distinguish real
2     Related Works                                         and machine-generated text.

2.1 Text Classification Methods                             2.2   Co-Written Text Analysis
Detecting machine-generated content has been                Several studies (Zhang et al., 2024; Liu et al.,
widely studied. Work mainly focuses on binary               2023c) utilize neural-based classification models
                                                       4350
Table 1: Datasets used for training and evaluating the proposed approach (adapted from (Uchendu et al., 2021;
Fagni et al., 2021; Zhang et al., 2024; Li et al., 2024; Dugan et al., 2023; Kushnareva et al.; Zeng et al., 2024b)).
The tasks include both classification and detection. Note that “#” represents “number of”.

  Task              Dataset       Generators            Domains                                # Texts   # Boundaries
                    TuringBench   FAIR wmt20            News                                   17,163         -


   Classification
                    TuringBench   GPT-3                 News                                   17,018         -
                    TweepFake     Markov        Chains, Tweets                                 25,572         -
                                  RNN, RNN+ Markov,
                                  LSTM, GPT-2
                    MAGE          27 LLMs from seven Reddit opinions, review, news, question 447,674          -
                                  groups: GPT, LLaMA, answering, story, commonsense reasoning,
                                  GLM-130B, FLAN- Wikipedia paragraph, scientific writing
                                  T5, OPT, BigScience,
                                  EleutherAI
                    RoFT          GPT-2/XL, CTRL        Speeches, recipes, news, short stories  8,943         1

   Detection
                    RoFT-         GPT-3.5 Turbo         Speeches, recipes, news, short stories  6,940         1
                    ChatGPT
                    TriBERT       ChatGPT             Educational essays                       17,136        1-3



to classify Human-Machine collaborative texts.                    tectures have proven effectiveness in object detec-
Kushnareva et al. address the boundary detec-                     tion (Zong et al., 2023; Hou et al., 2024; Huang
tion task to determine where human-written text                   et al., 2022) and related tasks like video action de-
ends and machine-generated text begins, using fine-               tection (Zhang et al., 2021) and moment retrieval
tuned RoBERTa and TDA-based time series. Zeng                     (Lei et al., 2021; Moon et al., 2023; Gordeev et al.,
et al. (2024b) measure distances between adjacent                 2024), where it is used to find temporal intervals in
segments to identify transitions, while Zeng et al.               videos corresponding to a given text query. Inspired
(2024a) employ segmentation and classification                    by these works, we propose to use a detection trans-
of segments into AI-generated, human-written, or                  former model to perform span-level detection in
collaborative. A simpler approach by Wang et al.                  texts.
(2023) identifies exact authorship for each sen-                     Recent DETR modifications improve efficiency
tence.                                                            and accuracy: DeformableDETR (Zhu et al., 2020)
   More recently, Yin and Wang (2026) intro-                      speeds up convergence with deformable attention;
duced Sci-SpanDet, a structure-aware framework                    DN-DETR (Li et al., 2022) uses denoising training
designed specifically for scientific papers. They                 to accelerate the training process and improve de-
combine BIO-CRF sequence labeling with pointer                    tection accuracy; DAB-DETR (Liu et al., 2022)
networks to detect contiguous AI-generated spans,                 refines predictions by introducing learnable an-
relying on section-specific contrastive learning that             chor boxes as DETR positional queries. DINO
leverages the IMRaD structure (Introduction, Meth-                DETR (Zhang et al., 2022) combines these features
ods, Results, Discussion) of scientific documents.                and integrates RPN, while CO-DETR (Zong et al.,
While effective in its target domain, Sci-SpanDet is              2023) enhances efficiency with auxiliary heads.
inherently tied to structured document formats and                   We adopt DN-DAB-DETR for its strong base-
cannot be directly applied to arbitrary texts lacking             line and high localization accuracy (Li et al., 2022).
such explicit organization.                                       We also tested DAB-DETR, DeformableDETR,
   In contrast, our approach is domain- and                       and CO-DETR, but DN-DAB-DETR consistently
structure-agnostic: by reformulating span detection               yielded the best results, so we adopt it throughout.
as 1D object detection over character-level inter-
vals, we eliminate the dependency on predefined                    3   Methodology
document layouts or sentence-level granularity, en-                Figure 1 illustrates the architecture of GigaCheck.
abling flexible detection of multiple generated seg-               Our framework addresses two complementary
ments in any text.                                                 tasks using a unified text-representation strategy:
                                                                   span-level localization and document-level classi-
2.3 Transformer-based detection models
                                                                   fication. We employ a LoRA-tuned LLM whose
DETR (Carion et al., 2020) is an end-to-end object                 token embeddings feed into two specialized heads.
detector based on transformers. DETR-like archi-                   Below, we first present the backbone, followed by
                                                              4351
our novel object-centric span detector, and finally    Architecture. Embeddings E, obtained in Equa-
the classification head.                               tion 1 from the frozen backbone, are first linearly
                                                       projected to a lower dimension and then passed
3.1 Unified text-representation backbone               through a Transformer encoder to obtain contex-
We fine-tune a general-purpose decoder LLM,            tual features:
namely Mistral-7B,1 with LoRA (Hu et al., 2021).
                                                                  E = Linear(E),
LoRA decomposes the weight matrix into two low-                                                              (2)
rank trainable matrices while keeping pre-trained                 R = TransformerEncoder(E)
weights frozen, yielding parameter-efficient fine-     We then follow DAB-DETR (Liu et al., 2022).
tuning (PEFT). We chose LoRA because (i) most          A set of N anchor-based learnable queries q =
of the datasets we use are small (see in Table 1),     {q0 , . . . , qN −1 } is initialised with reference points
where PEFT often generalises better than full fine-    (c, w), which act as initial hypotheses for the loca-
tuning, and (ii) it converges much faster, saving      tions and lengths of LLM-generated spans. These
GPU hours. Although results are reported with          queries are fed to the Transformer decoder, where
Mistral, the backbone is model-agnostic and any        sinusoidal encodings inject the anchor positions,
decoder-style LLM can be swapped in with mini-         and each cross-attention block concatenates posi-
mal changes.                                           tional and content embeddings, allowing the de-
                                                       coder to refine each anchor iteratively. At decoder
Proxy task. The LLM is tuned on a lightweight          layer ℓ the decoder predicts an offset (∆c(ℓ) , ∆w(ℓ) )
proxy classification task with two variants:           for each anchor and updates it as

  1. three-class proxy (human, machine, collabo-            (c, w)(ℓ+1) = (c, w)(ℓ) + (∆c(ℓ) , ∆w(ℓ) ).
     rative): used as a frozen feature extractor for
                                                       After L layers the decoder produces N refined
     the DETR training.
                                                       spans:
  2. two-class proxy (human, machine): is train-
                                                                 o = TransformerDecoder(q, R),               (3)
     able along with the binary-classification head.
                                                       where o = {o0 , . . . , oN −1 } corresponds one-to-
For a document X we obtain tokens and embed-           one with the anchor queries.
dings via                                              As the model output, for each query the detector
                                                       outputs a triplet (c, w, p) comprising the refined
         T = Tokenizer(X),                             centre c, width w, and a confidence score p ∈ [0, 1]
                                                (1)    that the span is LLM-generated. Thresholding p
         E = LLMf t (T), ei ∈ Rdmodel ,
                                                       yields up to N one-dimensional spans flagged as
where Tokenizer is the BPE tokenizer shipped with      machine-written.
Mistral and LLMf t is the LoRA-tuned required by       The number of queries N is a dataset-level hyper-
the downstream head. If fine-tuning is infeasible,     parameter set according to the maximum expected
pre-trained LLM embeddings may be substituted          span density.
(see Appendix A).                                      Stabilising early training. As in DN-DETR (Li
                                                       et al., 2022), the decoder is trained with two types
3.2 Object-centric Span Localization (DETR)            of inputs: (i) the learnable anchor queries, and
Our core contribution is the reformulation of text     (ii) noisy versions of the ground-truth (GT) spans.
analysis as an object detection problem. We intro-     The model is trained to denoise these GT queries,
duce a DETR-like head that treats LLM-generated        while an attention mask prevents them from leaking
segments as discrete objects, directly regressing      information to the anchor queries.
1-D character spans parameterized by c and width
                                                       Training loss. Before computing losses, we use
w (normalised to [0, 1]). This approach avoids the
                                                       Hungarian matching to pair each prediction with a
limitations of token-level sequence labeling and
                                                       GT span; the noised GT queries are excluded from
operates independently of sentence boundaries.
                                                       this matching. The final objective is a weighted
   1
    https://huggingface.co/mistralai/                  sum of L1, gIoU (Rezatofighi et al., 2019), and Fo-
Mistral-7B-v0.3                                        cal (Lin, 2017) losses for the matched predictions,
                                                   4352
plus the same L1 and gIoU terms applied to the          written (HumanRec) and machine-generated (Ma-
denoised GT queries.                                    chineRec) texts.
We refer to the described detection transformer         Detection metrics. We use metrics such as
model as GigaCheck (DN-DAB-DETR).                       sentence-wise MSE, Accuracy, and Soft Accuracy
                                                        from Kushnareva et al., as well as a specialized
3.3 Binary classification head                          form of the F1 score from Zeng et al. (2024b), to
The second head answers the document-level              assess the quality of the model’s predictions of the
question “Is this text human-written or LLM-            boundaries between sentences written by a human
generated?”. Formally, for a document X we learn        or an LLM. The authors of Zeng et al. (2024b) con-
                                 (                      sider LtopK , which represents the top-K boundaries
                                  0, human,             identified by the algorithm, and LGt , which refers
fθ : X −→ {0, 1}, fθ (X) =
                                  1, machine.           to the number of ground-truth boundaries. The
                                                        F1 score is then determined using the following
We attach a two-layer MLP to the hidden state of        formula:
the final <EOS> token of the two-class LoRA variant
and train it with binary cross-entropy. The resulting                             |LtopK ∩ LGt |
model is referred to as GigaCheck (Mistral-7B).                   F 1@K = 2 ·                             (4)
                                                                                 |LtopK | + |LGt |
4   Datasets and Metrics                                Further details on the calculation of each metric are
                                                        provided in Appendix E.
Table 1 lists all datasets used in this work. We use
the original train–test splits in Section 5, enabling   5     Experimental Results
comparison with other approaches trained on the
same data.                                              In this section we first report span-detection results
Classification datasets. We evaluate the pro-           on three Human-Machine collaborative datasets,
posed approach for machine-written text classifica-     then present an extensive evaluation on three
tion using three datasets: TuringBench (Uchendu         binary-classification benchmarks. While the classi-
et al., 2021), TweepFake (Fagni et al., 2021), and      fication task itself is well studied, these additional
MAGE (Li et al., 2024). We prioritized these            experiments serve to verify that the proposed text-
benchmarks while noting that other existing cor-        representation backbone produces embeddings that
pora, such as MixSet (Zhang et al., 2024) or Ghost-     remain robust and discriminative for a separate
busters (Verma et al., 2023), consist of a limited      downstream task. Training details for all runs are
amount of data. Such small-scale datasets are           provided in Appendix B.
known to be easily solvable and often fail to re-
flect the complexity of real-world detection scenar-    5.1    Detection Results
ios (Gritsai et al., 2024). Regarding TuringBench,      To provide a comprehensive assessment, we bench-
we specifically use the two subsets generated by        mark GigaCheck against a diverse spectrum of
FAIR wmt20 (Chen et al., 2020) and GPT-3 (Brown         baselines operating at varying granularities. We
et al., 2020), as these models produce texts most       evaluate our span-detection method on the RoFT
indistinguishable from human-written ones accord-       and RoFT-GPT datasets against approaches operat-
ing to the dataset authors.                             ing at the token level, sentence level, and document
Detection datasets. We considered three datasets        level. This inclusion allows us to compare our
for Human-Machine collaborative text analysis,          object-centric approach directly with traditional
which have been created to address the task of          fine-grained methods. For the TriBERT dataset,
identifying a boundary between human-written            following established protocols, we compare our
and machine-generated text: RoFT (Dugan et al.,         method with sentence-level approach.
2023), RoFT-ChatGPT (Kushnareva et al.), and               RoFT and RoFT-ChatGPT results. In experi-
TriBERT (Zeng et al., 2024b).                           ments on the RoFT and RoFT-ChatGPT datasets,
Classification metrics. We evaluate GigaCheck           we fine-tuned Mistral-7B to distinguish between
as an LLM-generated content detector using clas-        human-written texts and texts co-written with
sification accuracy (Acc), F1 score, AUROC, and         LLMs. Features from the model’s last layer
average recall (AvgRec) (Li et al., 2024), calcu-       were used to train the GigaCheck (DN-DAB-DETR)
lated as the average of recall scores for human-        model. Since each text in these datasets contains at
                                                    4353
Table 2: Boundary detection results on RoFT and RoFT-ChatGPT datasets. The results for all methods, except ours,
were taken from Kushnareva et al..

                               Method                                     RoFT                 RoFT-ChatGPT
                                                                 Acc    SoftAcc1   MSE      Acc SoftAcc1 MSE
         RoBERTa + SEP (Cutler et al., 2021)                     0.50   0.80       2.63     0.55 0.79     3.06
         RoBERTa (Liu, 2019)                                     0.46   0.75       3.00     0.39 0.75     3.15
         GigaCheck (DN-DAB-DETR)                                 0.65   0.87       1.51     0.68 0.89     1.03
         Based on Perplexity
              Phi-1.5 (Li et al., 2023) Perpl. + GB regressor    0.17 0.45         6.11     0.32 0.71     3.07
              Phi-1.5 (Li et al., 2023) Perpl. + LR classifier   0.27 0.50         11.9     0.47 0.73     4.77
         Based on TDA
              PHD + TS ML (Kushnareva et al.)                    0.24 0.46         14.40 0.17 0.36        14.45
              TLE + TS Binary (Kushnareva et al.)                0.13 0.30         22.23 0.20 0.35        18.52
         Human baseline (Cutler et al., 2021)                    0.23 0.40         13.88 -    -           -

Table 3: Accuracy for leave-one-out cross-domain evaluation on RoFT-ChatGPT. The results for all methods, except
ours, were taken from Kushnareva et al..

                                                              Pres.    Recipes New York Short
               Pred. Model                            Context Speeches         Times    Stories
               Text GigaCheck (DN-DAB-DETR)           global 0.50      0.33    0.55     0.64
               Text RoBERTa SEP (Cutler et al., 2021) global 0.31      0.13    0.38     0.29
               Text RoBERTa (Liu, 2019)               global 0.36      0.15    0.38     0.36
               Perpl. Phi1.5 (Li et al., 2023), GB    sent.   0.52     0.24    0.46     0.56
               Perpl. Phi1.5 (Li et al., 2023), LR    sent.   0.41     0.21    0.45     0.52
               PHD TS multi (Kushnareva et al.)       100 tkn 0.13     0.20    0.17     0.18
               TLE TS Binary (Kushnareva et al.)      20 tkn 0.15      0.16    0.17     0.11


Table 4: Evaluation of GigaCheck (DN-DAB-DETR)                   Table 5: Boundary detection results (F1@3) on the
on RoFT and RoFT-GPT datasets using mAP@0.5-0.95.                TriBERT (Zeng et al., 2024b) dataset. #Bry denotes the
The table compares the leave-one-out cross-domain set-           number of ground-truth boundaries in the texts. Mea-
ting against models trained on all domains combined.             surements are presented in original and rescaled for-
                                                                 mats.
   Dataset                             mAP@0.5-0.95
   RoFT-ChatGPT Short Stories            0.7626                     Methods                #Bry=1 #Bry=2 #Bry=3 All
   RoFT-ChatGPT Recipes                  0.6046                                           Original values
   RoFT-ChatGPT Pres Speeches            0.5933                     TriBERT (p=2)           0.455 0.692 0.622 0.575
   RoFT-ChatGPT New York Times           0.7034                     GigaCheck
   RoFT-ChatGPT All domains              0.8135                                     0.444 0.693          0.801 0.646
                                                                    (DN-DAB-DETR)
   RoFT All domains                      0.7972                                   Rescaled values
                                                                    TriBERT (p=2)   0.910 0.865          0.622    -
                                                                    GigaCheck
                                                                                    0.888 0.867          0.801    -
                                                                    (DN-DAB-DETR)
most one human-to-machine transition, the detector
uses a single learnable query (N =1).
   GigaCheck (DN-DAB-DETR) natively predicts                     Recipes domain remains relatively low.
continuous character-level intervals end-to-end,                    We additionally report the standard mean Aver-
without any heuristic post-processing. Since the of-             age Precision (mAP) adapted for one-dimensional
ficial RoFT metrics operate on sentence boundaries,              intervals (Table 4). An interval is considered a
we apply a deterministic character-to-sentence pro-              true positive if its IoU with a ground-truth inter-
jection solely for evaluation purposes (details in               val exceeds a given threshold; mAP@0.5:0.95 av-
Appendix F).                                                     erages over thresholds from 0.5 to 0.95. Unlike
  Table 2 shows that GigaCheck (DN-DAB-DETR)                     the sentence-level metrics above, mAP operates
beats the RoBERTa baseline by 15% on RoFT                        directly on character-level predictions and requires
and 13% on RoFT-ChatGPT, and reduces MSE                         no projection, confirming that the model achieves
on RoFT-ChatGPT by a factor of 3. Table 3 shows                  strong localization at the native output granularity.
cross-domain results on RoFT-ChatGPT, where                         Examples of raw model output on RoFT-
models trained on three domains and tested on                    ChatGPT are provided in Appendix G.
the fourth. Our approach achieves the best cross-                   TriBERT results. TriBERT texts contain up to
domain generalization, though performance on the                 three authorship boundaries, yielding denser spans;
                                                           4354
accordingly, the detector uses 18 learnable queries         In summary, our approach with 7B backbone ef-
(N =18) to provide sufficient capacity. Because          fectively distinguishes LLM-generated texts from
the TriBERT dataset is small, we keep Mistral-7B-        human-written ones when trained on both small
v0.3 frozen and feed its embeddings to GigaCheck         and large datasets. The experiments demonstrate
(DN-DAB-DETR). The detector outputs character            the robustness of our method for out-of-domain
spans, which we map to sentence boundaries to            and out-of-model detection, as well as its resis-
compute F 1@3 (Eq. 4; mapping details in Ap-             tance to paraphrasing attacks. Additionally, Ap-
pendix F).                                               pendix D presents a comparison between the fine-
   Results are reported by boundary count (1, 2, 3)      tuned GigaCheck (Mistral-7B) models and the
and for the full set. With K ̸= 3 the ideal F 1@3        Mistral-7B-Instruct-v0.3 model, evaluated in a
scores are 0.5, 0.8, 1.0 (Zeng et al., 2024b). We        zero-shot setting across each test set.
rescale them to a common scale, where the ideal
F 1@3 is 1.0, for clarity. Table 5 shows a 7.1%          Table 6: Experimental results on TweepFake test set. F1
                                                         scores are reported as ’human’ / ’machine’.
gain over TriBERT model on the full set and higher
scores for 2- and 3-boundary texts, while perfor-             Method                          F1           Acc
mance is similar for the 1-boundary group. Unlike             BERT (Devlin, 2018)        0.890 / 0.892    0.891
                                                              DistilBERT (Sanh, 2019)    0.886 / 0.888    0.887
TriBERT, our model stays stable as the number of              RoBERTa (Liu, 2019)        0.895 / 0.897    0.896
boundaries increases.                                         XLNet (Yang, 2019)         0.871 / 0.882    0.877
                                                              GigaCheck (Mistral-7B)     0.944 / 0.942    0.943
5.2 Classification Results
We fine-tuned Mistral-7B v0.3 with LoRA on five
                                                         Table 7: Experimental results (F1) on two TuringBench
datasets, comparing to baselines provided by the au-
                                                         subsets. F1 is calculated for the machine-generated
thors of these datasets. All our models were trained     category.
on the same training sets used by the authors.
   Tables 6 and 7 show strong results on Tweep-              Method                     FAIR_wmt20       GPT-3
                                                             GLTR (Gehrmann et al.,       0.4907         0.3476
Fake and TuringBench, outperforming statistical              2019)
methods and fine-tuned LM baselines across di-               BERT (Devlin, 2018)         0.4701          0.7944
verse domains and generators.                                RoBERTa (Liu, 2019)         0.4531          0.5209
                                                             GigaCheck (Mistral-7B)      0.9966          0.9709
   MAGE results. Table 8 compares GigaCheck
(Mistral-7B) with the strongest baseline reported
by the dataset authors (full results in Appendix C)      6     Conclusions
and shows that our model reaches AUROC = 0.99
and AvgRec = 0.96 on the full large-scale split. It      We presented GigaCheck, a unified framework that
keeps strong generalisation: AvgRec = 0.89 in the        combines a LoRA-tuned backbone LLM with two
unseen-domain + unseen-model test, 0.69 under            lightweight heads: (i) a DN-DAB-DETR module
paraphrase attacks, and AUROC = 0.98 / AvgRec =          for precise character-level localization of LLM-
0.92 in the out-of-model setting, where texts from       generated spans, and (ii) a streamlined MLP for
specific generators were excluded during training.       document-level authorship verification.
   Effect of backbone size. To gauge the impact             Our experiments on three Human–Machine col-
of scale we repeated the full-data experiment on         laborative datasets demonstrate that DETR-style
MAGE (the largest corpus in our experiments) us-         transformers can be successfully translated from
ing three larger LoRA-tuned backbones: Mistral-          computer vision to the textual domain, treating
Nemo-Base-2407 (12 B), Mistral-Small-24B-Base-           generated spans as discrete objects to achieve high-
2501 (24 B), and Qwen2.5-72B-Instruct (72 B). As         fidelity localization. Simultaneously, the shared
reported in Table 9, accuracy rises with backbone        backbone matches or surpasses prior baselines on
size overall, yet the 72B Qwen variant drops to the      three binary-classification corpora, confirming that
lowest score, hinting at overfitting. Because the        the learned representations are both robust and
gains beyond 7B are modest relative to the added         transferable across tasks of varying granularity.
compute, we keep the 7 B backbone for all other             Crucially, unlike methods constrained by sen-
datasets; it trains quickly, fits standard memory lim-   tence boundaries or explicit document structures,
its, and is less prone to overfitting on small corpora   GigaCheck offers flexible, boundary-free detec-
even with LoRA.                                          tion. It operates effectively without predefined
                                                     4355
Table 8: Classification performance on MAGE dataset      model-agnostic; the framework permits swapping
in different scenarios including performance on the      the backbone for any decoder-style LLM (e.g.,
two challenging test sets. To test on challenging test
                                                         LLaMA, Qwen) to adapt to specific resource con-
sets (Unseen Domains & Unseen Model, Paraphras-
ing Attack) the model trained on Arbitrary-domains       straints or domain requirements.
& Arbitrary-models dataset was used. Metrics for the     Benchmark Saturation. Near-perfect scores on
Longformer (Beltagy et al., 2020) method was taken       smaller corpora like TuringBench may reflect their
from the authors of MAGE dataset.                        limited diversity rather than unsolved challenges.
                                                         In datasets with few source domains and generator
    Methods                      AvgRec AUROC
        Arbitrary-domains & Arbitrary-models             models, distinct artifacts persist, simplifying detec-
    Longformer                    0.91      0.99         tion (Gritsai et al., 2024). Thus, these results may
    GigaCheck (Mistral-7B)        0.96      0.99         overstate real-world performance. To address this
          Unseen Domains & Unseen Model
    Longformer                    0.76      0.94         limitation, in concurrent work we assembled a sub-
    GigaCheck (Mistral-7B)        0.89      0.96         stantially larger and more diverse benchmark and
                  Paraphrasing Attack                    evaluated GigaCheck on it (Tolstykh et al., 2025).
    Longformer                    0.67      0.75
    GigaCheck (Mistral-7B)        0.69      0.74
     Out-of-distribution Detection: Unseen models        8   Ethical Statement
    Longformer                    0.87      0.95
    GigaCheck (Mistral-7B)        0.92      0.98         Interpretability and Misuse. While GigaCheck
                                                         improves transparency by localising specific AI-
 Table 9: Impact of backbone size on MAGE full set.      generated spans rather than providing a black-box
                                                         document-level verdict, it does not achieve perfect
    Model                     AvgRec    AUROC
    GigaCheck (Mistral-7B)    0.9611     0.9923          accuracy. Performance can fluctuate based on the
    GigaCheck (Mistral-12B)   0.9630     0.9941          generator model, text length, and domain. Conse-
    GigaCheck (Mistral-24B)   0.9685     0.9937
    GigaCheck (Qwen-72B)      0.8338     0.9697
                                                         quently, the detector should be used as an assistive
                                                         tool for human verification, not as the sole basis for
                                                         high-stakes decisions (e.g., academic disciplinary
segmentation, showing strong generalization ca-          actions). We disclaim responsibility for any repu-
pabilities across diverse setups (from pre-trained       tational damage or adverse consequences arising
to fine-tuned backbones) and in challenging out-of-      from the unverified reliance on its outputs.
domain scenarios.

7   Limitations                                          References
Context Window Constraints. To optimize com-             Wissam Antoun, Virginie Mouilleron, Benoît Sagot, and
                                                           Djamé Seddah. 2023. Towards a robust detection of
putational efficiency during training, we explic-          language model generated text: Is chatgpt that easy
itly restrict the input sequence length, although the      to detect? arXiv preprint arXiv:2306.05871.
backbone supports longer contexts. Consequently,
documents exceeding this limit are processed in          Iz Beltagy, Matthew E Peters, and Arman Cohan. 2020.
                                                            Longformer: The long-document transformer. arXiv
independent chunks, potentially obscuring long-             preprint arXiv:2004.05150.
range dependencies across segment boundaries.
However, this is a hyperparameter choice; the core       Amrita Bhattacharjee and Huan Liu. 2024. Fighting fire
architecture scales naturally to larger context win-      with fire: can chatgpt detect ai-generated text? ACM
                                                          SIGKDD Explorations Newsletter, 25(2):14–21.
dows given sufficient computational resources.
Language Scope. This study is intentionally              Tom B. Brown, Benjamin Mann, Nick Ryder, Melanie
scoped to English to ensure rigorous comparison            Subbiah, Jared Kaplan, Prafulla Dhariwal, Arvind
with established benchmarks. Since the unified             Neelakantan, Pranav Shyam, Girish Sastry, Amanda
                                                           Askell, Sandhini Agarwal, Ariel Herbert-Voss,
backbone is multilingual by design, extending Gi-          Gretchen Krueger, Tom Henighan, Rewon Child,
gaCheck to other languages requires no architec-           Aditya Ramesh, Daniel M. Ziegler, Jeffrey Wu,
tural modifications, only the curation of appropriate      Clemens Winter, Christopher Hesse, Mark Chen, Eric
training data.                                             Sigler, Mateusz Litwin, Scott Gray, Benjamin Chess,
                                                           Jack Clark, Christopher Berner, Sam McCandlish,
Backbone Dependency. We report results us-                 Alec Radford, Ilya Sutskever, and Dario Amodei.
ing Mistral-7B due to its favourable quality-to-           2020. Language models are few-shot learners. In Ad-
compute trade-off. However, the pipeline is                vances in Neural Information Processing Systems 33:
                                                      4356
  Annual Conference on Neural Information Process-        Biyang Guo, Xin Zhang, Ziyuan Wang, Minqi Jiang,
  ing Systems 2020, NeurIPS 2020, December 6-12,            Jinran Nie, Yuxuan Ding, Jianwei Yue, and Yupeng
  2020, virtual.                                            Wu. 2023. How close is chatgpt to human experts?
                                                            comparison corpus, evaluation, and detection. arXiv
Nicolas Carion, Francisco Massa, Gabriel Synnaeve,          preprint arXiv:2301.07597.
  Nicolas Usunier, Alexander Kirillov, and Sergey
  Zagoruyko. 2020. End-to-end object detection with       Hans WA Hanley and Zakir Durumeric. 2024. Machine-
  transformers. In European conference on computer          made media: Monitoring the mobilization of
  vision, pages 213–229. Springer.                          machine-generated articles on misinformation and
                                                            mainstream news websites. In Proceedings of the
Souradip Chakraborty, Amrit Singh Bedi, Sicheng Zhu,        International AAAI Conference on Web and Social
  Bang An, Dinesh Manocha, and Furong Huang. 2023.          Media, volume 18, pages 542–556.
  On the possibilities of ai-generated text detection.
  arXiv preprint arXiv:2304.04736.                        Xiuquan Hou, Meiqin Liu, Senlin Zhang, Ping Wei,
                                                            Badong Chen, and Xuguang Lan. 2024. Relation
Peng-Jen Chen, Ann Lee, Changhan Wang, Naman                detr: Exploring explicit position relation prior for
  Goyal, Angela Fan, Mary Williamson, and Jiatao            object detection. arXiv preprint arXiv:2407.11699.
  Gu. 2020. Facebook ai’s wmt20 news translation
  task submission. arXiv preprint arXiv:2011.08298.       Edward J Hu, Yelong Shen, Phillip Wallis, Zeyuan
                                                            Allen-Zhu, Yuanzhi Li, Shean Wang, Lu Wang,
Joseph Cutler, Liam Dugan, Shreya Havaldar, and Adam        and Weizhu Chen. 2021. Lora: Low-rank adap-
   Stein. 2021. Automatic detection of hybrid human-        tation of large language models. arXiv preprint
   machine text boundaries.                                 arXiv:2106.09685.
Jacob Devlin. 2018. Bert: Pre-training of deep bidi-      Kuan-Chih Huang, Tsung-Han Wu, Hung-Ting Su, and
   rectional transformers for language understanding.       Winston H Hsu. 2022. Monodtr: Monocular 3d ob-
   arXiv preprint arXiv:1810.04805.                         ject detection with depth-aware transformer. In Pro-
                                                            ceedings of the IEEE/CVF conference on computer
Liam Dugan, Daphne Ippolito, Arun Kirubarajan,
                                                            vision and pattern recognition, pages 4012–4021.
  Sherry Shi, and Chris Callison-Burch. 2023. Real
  or fake text?: Investigating human ability to detect
                                                          Ziwei Ji, Nayeon Lee, Rita Frieske, Tiezheng Yu, Dan
  boundaries between human-written and machine-
                                                            Su, Yan Xu, Etsuko Ishii, Ye Jin Bang, Andrea
  generated text. In Proceedings of the AAAI Con-
                                                            Madotto, and Pascale Fung. 2023. Survey of halluci-
  ference on Artificial Intelligence, volume 37, pages
                                                            nation in natural language generation. ACM Comput-
  12763–12771.
                                                            ing Surveys, 55(12):1–38.
Tiziano Fagni, Fabrizio Falchi, Margherita Gambini, An-
   tonio Martella, and Maurizio Tesconi. 2021. Tweep-     Armand Joulin, Edouard Grave, Piotr Bojanowski, and
   fake: About detecting deepfake tweets. Plos one,         Tomas Mikolov. 2016. Bag of tricks for efficient text
  16(5):e0251415.                                           classification. arXiv preprint arXiv:1607.01759.

Leon Fröhling and Arkaitz Zubiaga. 2021. Feature-         Enkelejda Kasneci, Kathrin Sessler, Stefan Küche-
  based detection of automated language models: tack-       mann, Maria Bannert, Daryna Dementieva, Frank
  ling gpt-2, gpt-3 and grover. PeerJ Computer Science,     Fischer, Urs Gasser, Georg Groh, Stephan Günne-
  7:e443.                                                   mann, Eyke Hüllermeier, Stephan Krusche, Gitta
                                                            Kutyniok, Tilman Michaeli, Claudia Nerdel, Jür-
Sebastian Gehrmann, Hendrik Strobelt, and Alexan-           gen Pfeffer, Oleksandra Poquet, Michael Sailer, Al-
  der M Rush. 2019. Gltr: Statistical detection             brecht Schmidt, Tina Seidel, Matthias Stadler, Jochen
  and visualization of generated text. arXiv preprint       Weller, Jochen Kuhn, and Gjergji Kasneci. 2023.
  arXiv:1906.04043.                                         Chatgpt for good? on opportunities and challenges of
                                                            large language models for education. Learning and
Aleksandr Gordeev, Vladimir Dokholyan, Irina Tol-           Individual Differences, 103:102274.
  stykh, and Maksim Kuprashevich. 2024. Saliency-
  guided detr for moment retrieval and highlight detec-   Ryuto Koike, Masahiro Kaneko, and Naoaki Okazaki.
  tion.                                                     2024. Outfox: Llm-generated essay detection
                                                            through in-context learning with adversarially gen-
Dijana Vukovic Grbic and Igor Dujlovic. 2023. So-           erated examples. In Proceedings of the AAAI Con-
  cial engineering with chatgpt. In 2023 22nd In-           ference on Artificial Intelligence, volume 38, pages
  ternational Symposium INFOTEH-JAHORINA (IN-               21258–21266.
  FOTEH), pages 1–5. IEEE.
                                                          Kalpesh Krishna, Yixiao Song, Marzena Karpinska,
German Gritsai, Anastasia Voznyuk, Andrey Grabovoy,         John Wieting, and Mohit Iyyer. 2024. Paraphras-
  and Yury Chekhovich. 2024. Are ai detectors good          ing evades detectors of ai-generated text, but retrieval
  enough? a survey on quality of datasets with machine-     is an effective defense. Advances in Neural Informa-
  generated texts. arXiv preprint arXiv:2410.14677.         tion Processing Systems, 36.
                                                      4357
Laida Kushnareva, Daniil Cherniavskii, Vladislav             Ilya Loshchilov and Frank Hutter. 2016. Sgdr: Stochas-
  Mikhailov, Ekaterina Artemova, Serguei Barannikov,            tic gradient descent with warm restarts. arXiv
  Alexander Bernstein, Irina Piontkovskaya, Dmitri              preprint arXiv:1608.03983.
  Piontkovski, and Evgeny Burnaev. 2021. Artificial
  text detection via examining the topology of attention     Yisroel Mirsky, Ambra Demontis, Jaidip Kotak, Ram
  maps. arXiv preprint arXiv:2109.04825.                       Shankar, Deng Gelei, Liu Yang, Xiangyu Zhang,
                                                               Maura Pintor, Wenke Lee, Yuval Elovici, and Battista
Laida Kushnareva, Tatiana Gaintseva, Dmitry Ab-                Biggio. 2023. The threat of offensive ai to organiza-
  ulkhanov, Kristian Kuznetsov, German Magai,                  tions. Computers Security, 124:103006.
  Eduard Tulchinskii, Serguei Barannikov, Sergey
  Nikolenko, and Irina Piontkovskaya. Ai-generated           Eric Mitchell, Yoonho Lee, Alexander Khazatsky,
  text boundary detection with roft. In First Confer-          Christopher D Manning, and Chelsea Finn. 2023. De-
  ence on Language Modeling.                                   tectgpt: Zero-shot machine-generated text detection
                                                               using probability curvature. In International Con-
Jie Lei, Tamara L Berg, and Mohit Bansal. 2021. De-
                                                               ference on Machine Learning, pages 24950–24962.
   tecting moments and highlights in videos via natural
                                                               PMLR.
   language queries. Advances in Neural Information
   Processing Systems, 34:11846–11858.
                                                             WonJun Moon, Sangeek Hyun, SuBeen Lee, and Jae-
Feng Li, Hao Zhang, Shilong Liu, Jian Guo, Lionel M           Pil Heo. 2023. Correlation-guided query-dependency
  Ni, and Lei Zhang. 2022. Dn-detr: Accelerate detr           calibration for video temporal grounding.
  training by introducing query denoising. In Proceed-
  ings of the IEEE/CVF conference on computer vision         OpenAI. 2023a. ChatGPT: A Large Language Model.
  and pattern recognition, pages 13619–13627.                  Online; accessed February 13, 2024. Available at
                                                               https://www.openai.com/.
Yafu Li, Qintong Li, Leyang Cui, Wei Bi, Zhilin Wang,
  Longyue Wang, Linyi Yang, Shuming Shi, and Yue             OpenAI. 2023b. Gpt-4 technical report.
  Zhang. 2024. Mage: Machine-generated text detec-
  tion in the wild. In Proceedings of the 62nd Annual        Mike Perkins, Jasper Roe, Darius Postma, James Mc-
  Meeting of the Association for Computational Lin-            Gaughran, and Don Hickerson. 2023. Game of tones:
  guistics (Volume 1: Long Papers), pages 36–53.               faculty detection of gpt-4 generated content in univer-
                                                               sity assessments. arXiv preprint arXiv:2305.18081.
Yuanzhi Li, Sébastien Bubeck, Ronen Eldan, Allie
  Del Giorno, Suriya Gunasekar, and Yin Tat Lee. 2023.       Hamid Rezatofighi, Nathan Tsoi, JunYoung Gwak,
  Textbooks are all you need ii: phi-1.5 technical report.     Amir Sadeghian, Ian Reid, and Silvio Savarese. 2019.
  arXiv preprint arXiv:2309.05463.                             Generalized intersection over union: A metric and
                                                               a loss for bounding box regression. In Proceedings
T Lin. 2017. Focal loss for dense object detection.
                                                               of the IEEE/CVF conference on computer vision and
  arXiv preprint arXiv:1708.02002.
                                                               pattern recognition, pages 658–666.
Shilong Liu, Feng Li, Hao Zhang, Xiao Yang, Xianbiao
  Qi, Hang Su, Jun Zhu, and Lei Zhang. 2022. Dab-            Sayak Saha Roy, Krishna Vamsi Naragam, and Shirin
  detr: Dynamic anchor boxes are better queries for            Nilizadeh. 2023. Generating phishing attacks using
  detr. arXiv preprint arXiv:2201.12329.                       chatgpt. arXiv preprint arXiv:2305.05133.

Yikang Liu, Ziyin Zhang, Wanyang Zhang, Shisen Yue,          V Sanh. 2019. Distilbert, a distilled version of bert:
  Xiaojing Zhao, Xinyuan Cheng, Yiwen Zhang, and               Smaller, faster, cheaper and lighter. arXiv preprint
  Hai Hu. 2023a. Argugpt: evaluating, understanding            arXiv:1910.01108.
  and identifying argumentative essays generated by
  gpt models.                                                Irene Solaiman, Miles Brundage, Jack Clark, Amanda
                                                                Askell, Ariel Herbert-Voss, Jeff Wu, Alec Radford,
Yinhan Liu. 2019.      Roberta: A robustly opti-                Gretchen Krueger, Jong Wook Kim, Sarah Kreps,
  mized bert pretraining approach. arXiv preprint               Miles McCain, Alex Newhouse, Jason Blazakis, Kris
  arXiv:1907.11692.                                             McGuffie, and Jasmine Wang. 2019. Release strate-
                                                                gies and the social impacts of language models.
Zeyan Liu, Zijun Yao, Fengjun Li, and Bo Luo. 2023b.
  Check me if you can: Detecting chatgpt-generated
                                                             Chris Stokel-Walker. 2022. Ai bot chatgpt writes smart
  academic writing using checkgpt. arXiv preprint
                                                               essays-should academics worry? Nature.
  arXiv:2306.05524.
Zeyan Liu, Zijun Yao, Fengjun Li, and Bo Luo. 2023c.         Jinyan Su, Terry Yue Zhuo, Di Wang, and Preslav Nakov.
  On the detectability of chatgpt content: benchmark-           2023. Detectllm: Leveraging log rank information
  ing, methodology, and evaluation through the lens of          for zero-shot detection of machine-generated text.
  academic writing. arXiv e-prints, pages arXiv–2306.           arXiv preprint arXiv:2306.05540.

I Loshchilov. 2017. Decoupled weight decay regulariza-       H Holden Thorp. 2023. Chatgpt is fun, but not an
   tion. arXiv preprint arXiv:1711.05101.                      author.
                                                         4358
Irina Tolstykh, Aleksandra Tsybina, Sergey Yakubson,         Zhilin Yang. 2019. Xlnet: Generalized autoregres-
   and Maksim Kuprashevich. 2025. Llmtrace: A cor-             sive pretraining for language understanding. arXiv
   pus for classification and fine-grained localization of     preprint arXiv:1906.08237.
   ai-written text.
                                                             Zhen Yin and Shenghua Wang. 2026. Span-level de-
Eduard Tulchinskii, Kristian Kuznetsov, Laida                  tection of ai-generated scientific text via contrastive
  Kushnareva, Daniil Cherniavskii, Sergey Nikolenko,           learning and structural calibration. Knowledge-
  Evgeny Burnaev, Serguei Barannikov, and Irina                Based Systems, 334:115123.
  Piontkovskaya. 2024. Intrinsic dimension estimation
  for robust detection of ai-generated texts. Advances       Rowan Zellers, Ari Holtzman, Hannah Rashkin,
  in Neural Information Processing Systems, 36.                Yonatan Bisk, Ali Farhadi, Franziska Roesner, and
                                                               Yejin Choi. 2019. Defending against neural fake
Adaku Uchendu, Thai Le, and Dongwon Lee. 2023.                 news. Advances in neural information processing
  Toproberta: Topology-aware authorship attribution            systems, 32.
  of deepfake texts. arXiv preprint arXiv:2309.12934.
                                                             Zijie Zeng, Shiqi Liu, Lele Sha, Zhuang Li, Kaixun
Adaku Uchendu, Thai Le, Kai Shu, and Dongwon Lee.              Yang, Sannyuya Liu, Dragan Gašević, and Guan-
  2020. Authorship attribution for neural text gener-           liang Chen. 2024a. Detecting ai-generated sentences
  ation. In Proceedings of the 2020 conference on               in human-ai collaborative hybrid texts: Challenges,
  empirical methods in natural language processing              strategies, and insights.
  (EMNLP), pages 8384–8395.
                                                             Zijie Zeng, Lele Sha, Yuheng Li, Kaixun Yang, Dra-
Adaku Uchendu, Zeyu Ma, Thai Le, Rui Zhang, and                 gan Gašević, and Guangliang Chen. 2024b. Towards
  Dongwon Lee. 2021. Turingbench: A benchmark                   automatic boundary detection for human-ai collabo-
  environment for turing test in the age of neural text         rative hybrid essay in education.
  generation. arXiv preprint arXiv:2109.13296.
Christoforos Vasilatos, Manaar Alam, Talal Rahwan,           Chuhan Zhang, Ankush Gupta, and Andrew Zisser-
  Yasir Zaki, and Michail Maniatakos. 2023. Howkgpt:           man. 2021. Temporal query networks for fine-
  Investigating the detection of chatgpt-generated uni-        grained video understanding. In Proceedings of the
  versity student homework through context-aware per-          IEEE/CVF Conference on Computer Vision and Pat-
  plexity analysis. arXiv preprint arXiv:2305.18226.           tern Recognition, pages 4486–4496.

Vivek Verma, Eve Fleisig, Nicholas Tomlin, and Dan           Hao Zhang, Feng Li, Shilong Liu, Lei Zhang, Hang
  Klein. 2023. Ghostbuster: Detecting text ghost-              Su, Jun Zhu, Lionel M Ni, and Heung-Yeung Shum.
  written by large language models. arXiv preprint             2022. Dino: Detr with improved denoising anchor
  arXiv:2305.15047.                                            boxes for end-to-end object detection. arXiv preprint
                                                               arXiv:2203.03605.
Pengyu Wang, Linyang Li, Ke Ren, Botian Jiang, Dong
  Zhang, and Xipeng Qiu. 2023. SeqXGPT: Sentence-            Qihui Zhang, Chujie Gao, Dongping Chen, Yue Huang,
  level AI-generated text detection. In Proceedings of         Yixin Huang, Zhenyang Sun, Shilin Zhang, Weiye
  the 2023 Conference on Empirical Methods in Natu-            Li, Zhengyan Fu, Yao Wan, and Lichao Sun. 2024.
  ral Language Processing, pages 1144–1156, Singa-             LLM-as-a-coauthor: Can mixed human-written and
  pore. Association for Computational Linguistics.             machine-generated text be detected? In Findings
                                                               of the Association for Computational Linguistics:
Yuxia Wang, Jonibek Mansurov, Petar Ivanov, Jinyan             NAACL 2024, pages 409–436, Mexico City, Mex-
  Su, Artem Shelmanov, Akim Tsvigun, Osama Mo-                 ico. Association for Computational Linguistics.
  hammed Afzal, Tarek Mahmoud, Giovanni Puc-
  cetti, Thomas Arnold, Alham Aji, Nizar Habash,             X Zhu, W Su, L Lu, B Li, X Wang, and J Dai. 2020.
  Iryna Gurevych, and Preslav Nakov. 2024. M4GT-               Deformable detr: Deformable transformers for end-
  bench: Evaluation benchmark for black-box machine-           to-end object detection. arxiv 2020. arXiv preprint
  generated text detection. In Proceedings of the 62nd         arXiv:2010.04159.
  Annual Meeting of the Association for Computational
  Linguistics (Volume 1: Long Papers), pages 3964–           Zhuofan Zong, Guanglu Song, and Yu Liu. 2023. Detrs
  3992, Bangkok, Thailand. Association for Computa-            with collaborative hybrid assignments training. In
  tional Linguistics.                                          Proceedings of the IEEE/CVF international confer-
                                                               ence on computer vision, pages 6748–6758.
Junchao Wu, Shu Yang, Runzhe Zhan, Yulin Yuan,
  Derek F Wong, and Lidia S Chao. 2023a. A sur-
  vey on llm-gernerated text detection: Necessity,
  methods, and future directions. arXiv preprint
  arXiv:2310.14724.
Kangxi Wu, Liang Pang, Huawei Shen, Xueqi Cheng,
  and Tat-Seng Chua. 2023b. Llmdet: A third party
  large language models generated text detection tool.
  arXiv preprint arXiv:2305.15004.
                                                         4359
A       Pre-trained VS fine-tuned models’                   1) fine-tune the Mistral-7B model on two or three
        embeddings                                          categories, 2) extract features for the dataset from
                                                            the trained model, 3) train the DETR model using
 Table 10 presents a comparison of detection model
                                                            extracted features as input data. The training is
 performance on the RoFT and RoFT-ChatGPT
                                                            divided into three stages, firstly because this signifi-
 datasets using two different setups. In the first
                                                            cantly speeds up the training process, and secondly
 experiment, we fine-tuned the Mistral-7B model to
                                                            because LLM and DETR models converge at dif-
 perform a text classification task with two labels:
                                                            ferent rates.
’Human’ and ’AI-Human Collaborative’, and used
                                                               To train DN-DAB-DETR models, we also used
 this model to extract text features for DETR model
                                                            the AdamW optimizer with a cosine learning rate
 training. In the second experiment, we utilized the
                                                            schedule. During training we did not apply any text
 pre-trained Mistral-7B v0.3 model for feature ex-
                                                            augmentations. The number of learnable queries
 traction. Two DN-DAB-DETR models were then
                                                            N reflects the maximum span density per text in
 trained using these two types of features. The re-
                                                            each dataset (see Section 5.1). The dataset-specific
 sults indicate that the detection model performs bet-
                                                            hyperparameters used for the experiments are listed
 ter with features from the fine-tuned model; how-
                                                            in the table 12.
 ever, the model trained with text representations
 from the pre-trained model also achieves strong            C       MAGE comparison
 results on both datasets. We also provide results
 from Kushnareva et al. for comparison.                     Table 13 shows the results of comparing GigaCheck
                                                            with Mistral-7B with all detectors considered by
B       Hyperparameters and experimental                    the authors of the MAGE dataset. We also re-
        setup                                               port GigaCheck’s performance on the MAGE full
                                                            set (Arbitrary-domains & Arbitrary-models) us-
We fine-tune Mistral-7B-v0.32 for a binary classifi-        ing backbones of different sizes. We fine-tuned
cation task to distinguish between human-written            three large backbones: Mistral-Nemo-Base-24075
and machine-generated content using LoRA. Mod-              (12B), Mistral-Small-24B-Base-25016 (24B), and
els training were done using Hugging Face Trans-            Qwen2.5-72B-Instruct7 (72B).
formers3 with bfloat16 precision. LoRA set-
tings via the PEFT4 library include: r = 8,                 D       Mistral-7B-v0.3 zero-shot classification
lora_alpha = 16, lora_dropout = 0.1, and bias =                     results
”none”. Only query and value projection matri-
ces in attention modules were adapted. We used              Table 14 presents the results of comparing Gi-
AdamW (Loshchilov, 2017) with a cosine learning             gaCheck with Mistral-7B fine-tuned with LoRA
rate scheduler (Loshchilov and Hutter, 2016). The           on five classification datasets against the Mistral-
DETR model’s encoder and decoder each had 3                 7B-Instruct-v0.38 model, evaluated in a zero-shot
layers. The loss weights were set to 10.0 for L1,           setting. The comparison was conducted on the test
1.0 for gIoU, 4.0 for Focal Loss, 9.0 for denoised          sets.
L1, and 3.0 for denoised gIoU.
                                                            E       Evaluation metrics for detection
   During training, we augmented the data by
                                                                    datasets
randomly selecting between ’minimum sequence
length’ to ’maximum sequence length’ tokens from            For each detection dataset, we compute specific
each text. To optimize the models, we used the              metrics.
AdamW optimizer with a cosine learning rate                   Followed the approach of the authors in
schedule and also applied a weight for the ’Hu-             KushnarevaPet al., we compute mean squared error
man’ category in the cross-entropy function. The            MSE= N1 N    i=1 (yi − yˆi ) between the predicted
                                                                                        2

dataset-specific hyperparameters used for the ex-           boundaries ŷ and the true boundaries y, where a
periments are listed in the table 11.                           5
                                                                 https://huggingface.co/mistralai/Mistral-Nemo-Base-
   When training a detection model to find LLM-             2407
generated intervals in text, we follow three steps:            6
                                                                 https://huggingface.co/mistralai/Mistral-Small-24B-
                                                            Base-2501
    2                                                          7
      https://huggingface.co/mistralai/Mistral-7B-v0.3           https://huggingface.co/Qwen/Qwen2.5-72B-Instruct
    3                                                          8
      https://github.com/huggingface/transformers                https://huggingface.co/mistralai/Mistral-7B-Instruct-
    4
      https://github.com/huggingface/peft                   v0.3

                                                         4360
Table 10: Boundary detection results on RoFT and RoFT-ChatGPT datasets. ‘†’ denotes the DETR model was
trained on text features from pre-trained Mistral-7B v0.3 model. Bold shows the best method, underlined - second
best.

               Method                                           RoFT                      RoFT-ChatGPT
                                        Acc                     SoftAcc1      MSE    Acc      SoftAcc1 MSE
               RoBERTa + SEP            49.64 %                 79.71 %       2.63   54.61 % 79.03 % 3.06
               RoBERTa                  46.47 %                 74.86 %       3.00   39.01 % 75.18 % 3.15
               GigaCheck (DN-DAB-DETR)† 60.10 %                 81.48 %       2.77   51.37 % 80.12 % 1.93
               GigaCheck (DN-DAB-DETR) 64.63 %                  86.68 %       1.51   67.65 % 88.98 % 1.03

                          Table 11: Hyperparameters for the classification experiments.

                         Parameter                        MAGE         TuringBench      TweepFake
                            max sequence length            1024            1024           1024
                            minimum sequence
                                                           900                15            900
                         length for augmentatoins
                              train batch size             64                 32             32
                           gradient accumulation
                                                            1                  2             2
                                    steps
                                learning rate              3e-4               3e-4          3e-4
                         cross entropy weight for
                                                            2                  1             1
                              human category
                             num train epochs              3                5               4
                                                       1xNvidia          1xNvidia        1xNvidia
                                   GPUs
                                                         H100             H100            H100
                            the fine-tuning time          48h              2h              2h

               Table 12: Hyperparameters for the span-detection (DN-DAB-DETR) experiments.

                  Parameter                         RoFT          RoFT-ChatGPT              TriBERT
                      number of queries               1                 1                      18
                     max sequence length             512               512                    1024
                       train batch size               32                32                     64
                    gradient accumulation
                                                      2                   2                        1
                             steps
                         learning rate               1e-4                1e-4                  2e-4
                      num train epochs                75                  75                    75
                                                   1xNvidia            1xNvidia             1xNvidia
                            GPUs
                                                     H100                H100                 H100
                    the DETR training time            5h                  3h                    6h
                  the Mistral fine-tuning time        3h                  2h           (without fine-tuning)


boundary is the sentence number at which author-                      F1@K metric proposed by Zeng et al. (2024b)
ship in the text changes from human to LLM, and                    to asses the performance of model in boundaries
N represents the number of samples. It is worth                    detection task is described in Eq. 5. K was set to 3
noting that in both datasets from Kushnareva et al.,               for all measurements on TriBERT dataset.
each text contains no more than one boundary. The
authors also propose reporting accuracy (Acc) of                                                    |LtopK ∩ LGt |
boundary detection and soft accuracy (SoftAcc1),                                   F 1@K = 2 ·                         (5)
                                                                                                   |LtopK | + |LGt |
the proportion of predictions that are off from the
correct label by no more than one.                                 F     Interval post-processing
   Finally, the authors of (Wang et al., 2024) eval-
uate model prediction quality
                          P using the mean ab-                     The DETR predictions are post-processed as fol-
solute error MAE= N1 N       i=1 |yi − yˆi |, where ŷ             lows for experiments on the RoFT and RoFT-
denotes the predicted word number that separates                   ChatGPT datasets: let tI be the start of the interval
human and AI-generated parts of the text, y repre-                 I, and starti , endi be the indexes of the first and
sents ground-truth word number, and N is the num-                  last characters of the i-th sentence. If the i-th sen-
ber of samples. The problem statement in (Wang                     tence contains tI , the sentence number i′ , to which
et al., 2024) implies that there is only one such                  we map DN-DAB-DETR’s prediction, is calculated
word boundary per text.                                            as follows:
                                                            4361
Table 13: Classification performance on MAGE dataset in different scenarios including performance on the two
challenging test sets. To test on challenging test sets the model trained on Arbitrary-domains & Arbitrary-models
dataset was used.

                Methods                               HumanRec MachineRec AvgRec              AUROC
                                           Arbitrary-domains & Arbitrary-models
                FastText (Joulin et al., 2016)           86.34%         71.26%      78.80%      0.83
                GLTR (Gehrmann et al., 2019)             12.42%         98.42%      55.42%      0.74
                DetectGPT (Mitchell et al., 2023)        86.92%         34.05%      60.48%      0.57
                Longformer (Beltagy et al., 2020)        82.80%         98.27%      90.53%      0.99
                GigaCheck (Mistral-7B)                   95.72%         96.49%      96.11%      0.99
                GigaCheck (Mistral-12B)                  95.29%         97.32%      96.30%      0.99
                GigaCheck (Mistral-24B)                  96.94%         96.76%      96.85%      0.99
                GigaCheck (Qwen-72B)                     83.38%         96.62%      83.38%      0.97
                                             Unseen Domains & Unseen Model
                FastText (Joulin et al., 2016)           71.78%         68.88%      70.33%      0.74
                GLTR (Gehrmann et al., 2019)             16.79%         98.63%      57.71%      0.73
                Longformer (Beltagy et al., 2020)        52.50%         99.14%      75.82%      0.94
                GigaCheck (Mistral-7B)                   79.71%         97.38%      88.54%      0.96
                                                    Paraphrasing Attack
                FastText (Joulin et al., 2016)           71.78%         50.00%      60.89%      0.66
                GLTR (Gehrmann et al., 2019)             16.79%         82.44%      49.61%      0.47
                Longformer (Beltagy et al., 2020)        52.16%         81.73%      66.94%      0.75
                GigaCheck (Mistral-7B)                   79.66%         58.24%      68.95%      0.74
                                       Out-of-distribution Detection: Unseen models
                FastText (Joulin et al., 2016)           83.12%         54.09%      68.61%      0.74
                GLTR (Gehrmann et al., 2019)             25.77%         89.21%      57.49%      0.65
                DetectGPT (Mitchell et al., 2023)        48.67%         75.95%      62.31%      0.60
                Longformer (Beltagy et al., 2020)        83.31%         89.90%      86.61%      0.95
                GigaCheck (Mistral-7B)                   95.65%         89.00%      92.32%      0.98

Table 14: Experimental results (F1 scores) on the test sets for classification datasets. F1 is calculated for the
machine-generated category. We compare the Mistral-7B-Instruct-v0.3 model evaluated in a zero-shot setting with
fine-tuned Mistral-7B-v0.3 models.

                                                                 TuringBench   TuringBench
                 Method                      TweepFake                                        MAGE
                                                                 FAIR_wmt20       GPT-3
                 Mistral-7B-Instruct-v0.3          0.640            0.537         0.500        0.633
                 GigaCheck (Mistral-7B)            0.942            0.997         0.971        0.96



                 (                                                authorship changes. Note that if a boundary is
                  1,      if tI ≥ starti2+endi ,                  equal to the beginning or the end of the whole text,
        i′ = i +                                           (6)
                  0,      if tI < starti2+endi .                  we remove it, since a boundary can only be between
                                                                  two sentences.
   For the TriBERT experiments, DETR predic-
tions undergo the following post-processing steps:                G    Examples of the DETR model output
let bi and bi+1 denote the beginnings of the n and
                                                                  Tables 15 and 16 present examples of work of the
n + 1 sentences in characters and let pj denote the
                                                                  model trained on the RoFT-ChatGPT dataset. Table
beginning or the end of the predicted interval in
                                                                  15 shows the ground truth and output result for test
characters. Then the boundary B for pj is calcu-
                                                                  samples from the ’Short Stories’ and ’New York
lated as:
                                                                  Times’ domains. Table 16 shows the ground truth
                  (
                                                                  and output result for test samples from the ’Recipes’
                    bi     if pj < bi +b2i+1 ,
         B(pj ) =                               (7)               and ’Presidential Speeches’ domains.
                    bi+1 if pj ≥ bi +b2i+1 .
   Therefore, if the predicted start or end of the
interval falls in the first half of sentence n, we
map it to the beginning of sentence n. If it falls in
the second half, we map it to the beginning of the
next sentence, n + 1. As a result, each boundary
determines the sentence number where the text’s
                                                             4362
Table 15: Examples from the test set of the raw model’s output, trained on the RoFT-ChatGPT dataset. Bold text
indicates either the ground truth interval or the predicted one.

 Domain: Short Stories
 GT: Aryton blinked and rubbed his head. It had been a very high speed crash. He expected the impact to
 hurt more, but the whole thing just felt quite... fuzzy. There didn’t seem to be any track marshals around,
 which was odd, Aryton looked back towards the corner where he’d lost control. Nothing there, he pulled
 himself out of the car and scurried over the crash barrier to safety. That’s funny, he thought as he looked
 back at the crash, the car doesn’t seem damaged. Aryton walked back towards his car and inspected it
 closely. It was as if the crash had never happened, there wasn’t a scratch on it. He checked the fuel
 gauge, it was full, and the tires were still warm to the touch. It was a brand new car and one of the
 fastest ones that he had ever driven.
 Output: Aryton blinked and rubbed his head. It had been a very high speed crash. He expected the
 impact to hurt more, but the whole thing just felt quite... fuzzy. There didn’t seem to be any track marshals
 around, which was odd, Aryton looked back towards the corner where he’d lost control. Nothing there, he
 pulled himself out of the car and scurried over the crash barrier to safety. That’s funny, he thought as he
 looked back at the crash, the car doesn’t seem damaged. Aryton walked back towards his car and
 inspected it closely. It was as if the crash had never happened, there wasn’t a scratch on it. He
 checked the fuel gauge, it was full, and the tires were still warm to the touch. It was a brand new
 car and one of the fastest ones that he had ever driven.

 Domain: New York Times
 GT: ... For many in the industry, it was the final seal of approval on a technology that remained
 controversial as long as it was exclusive to smaller, less conservative computer makers. But that
 interpretation does not sit well with Irving Wladawsky-Berger, who is responsible for the supercomputing
 business at the International Business Machines Corporation. " For me to say now we’ve finally put our
 seal of approval on this would sound supremely arrogant," he said. " Let’s just say we have committed
 to build a product family of parallel RISC systems that scale up from our RS/6000." RISC, or reduced
 instruction set computing, is a technology that speeds processing by relegating more tasks to software;
 the RS/6000 is the name for both a chip set and a computer work station produced by I.B.M. using
 RISC. Dr. Wladawsky-Berger said the impetus to create a massively parallel supercomputer came from
 RS/6000 customers who were creating a sort of virtual parallel processor by linking multiple work
 stations. " There were people pushing at I.B.M., but they were pushing in many different directions," he
 said. " Supercomputing is an area where if you get seven smart people together, you get 17 different
 architectures." " But," he added, "we knew we had to do something because we were seeing more
 and more of our customers doing this and we knew we had to provide them with a scalable solution.
 Output: ... For many in the industry, it was the final seal of approval on a technology that remained
 controversial as long as it was exclusive to smaller, less conservative computer makers. But that
 interpretation does not sit well with Irving Wladawsky-Berger, who is responsible for the supercomputing
 business at the International Business Machines Corporation. " For me to say now we’ve finally put our
 seal of approval on this would sound supremely arrogant," he said. " Let’s just say we have committed
 to build a product family of parallel RISC systems that scale up from our RS/6000." RISC, or reduced
 instruction set computing, is a technology that speeds processing by relegating more tasks to software;
 the RS/6000 is the name for both a chip set and a computer work station produced by I.B.M. using
 RISC. Dr. Wladawsky-Berger said the impetus to create a massively parallel supercomputer came from
 RS/6000 customers who were creating a sort of virtual parallel processor by linking multiple work
 stations. " There were people pushing at I.B.M., but they were pushing in many different directions," he
 said. " Supercomputing is an area where if you get seven smart people together, you get 17 different
 architectures." " But," he added, "we knew we had to do something because we were seeing more and
 more of our customers doing this and we knew we had to provide them with a scalable solution.




                                                     4363
Table 16: Examples from the test set of the raw model’s output, trained on the RoFT-ChatGPT dataset. Bold text
indicates either the ground truth interval or the predicted one.

 Domain: Recipes
 GT: HOW TO MAKE: Make-Ahead Turkey Gravy Ingredients: 2 tablespoons canola oil 2 lbs turkey
 wings 1 cup dry white wine 3 tablespoons olive oil 1 medium yellow onion, halved 2 carrots, cut in 2 inch
 pieces 2 celery ribs, cut in 2 inch pieces plus a handful of the celery leaves 1 head garlic, cut in half 2
 sprigs fresh thyme 2 sprigs fresh sage 2 sprigs fresh rosemary 10 black peppercorns 2 bay leaves 6 cups
 low sodium chicken broth 8 tablespoons flour 4 tablespoons butter, if needed 12 teaspoon white vinegar
 Kitchen Bouquet, if desired. Instructions: 1. Preheat the oven to 375F.2. In a large roasting pan, toss
 the turkey wings with canola oil.3. Roast the turkey wings for about 1 hour, or until deeply golden
 brown.4. Transfer the turkey wings to a large pot and pour in the white wine.5. Over medium-high
 heat, bring to a simmer and scrape up any browned bits from the bottom of the roasting pan.6.
 Simmer for about 5 minutes, or until the wine has reduced by half.7. Pour the wine mixture over
 the turkey wings and set aside.8. In a large skillet, heat the olive oil over medium heat.9.
 Output: HOW TO MAKE: Make-Ahead Turkey Gravy Ingredients: 2 tablespoons canola oil 2 lbs turkey
 wings 1 cup dry white wine 3 tablespoons olive oil 1 medium yellow onion, halved 2 carrots, cut in 2
 inch pieces 2 celery ribs, cut in 2 inch pieces plus a handful of the celery leaves 1 head garlic, cut in half
 2 sprigs fresh thyme 2 sprigs fresh sage 2 sprigs fresh rosemary 10 black peppercorns 2 bay leaves 6
 cups low sodium chicken broth 8 tablespoons flour 4 tablespoons butter, if needed 12 teaspoon white
 vinegar Kitchen Bouquet, if desired. Instructions: 1. Preheat the oven to 375F.2. In a large roasting
 pan, toss the turkey wings with canola oil.3. Roast the turkey wings for about 1 hour, or until
 deeply golden brown.4. Transfer the turkey wings to a large pot and pour in the white wine.5. Over
 medium-high heat, bring to a simmer and scrape up any browned bits from the bottom of the
 roasting pan.6. Simmer for about 5 minutes, or until the wine has reduced by half.7. Pour the wine
 mixture over the turkey wings and set aside.8. In a large skillet, heat the olive oil over medium heat.9.

 Domain: Presidential Speeches
 GT: "An Association of Nations" by President Warren G. Harding on July 22, 1920. My countrymen, we
 believe the unspeakable sorrows, the immeasurable sacrifices, the awakened convictions, and the aspiring
 conscience of humankind must commit the nations of the earth to a new and better relationship. It need
 not be discussed now what motives plunged the world into war. It need not be inquired whether we asked
 the sons of this republic to defend our national rights, as I believe we did, or to purge the Old World of the
 accumulated ills of rivalry and greed. The sacrifices will be in vain if we cannot acclaim a new order
 with added security to civilization and peace maintained. One may readily sense the conscience of our
 America. I am sure I understand the purpose of the dominant group of the Senate. We were not seeking to
 defeat a world aspiration. We were not seeking to withhold our country from doing its part in the
 world’s great work. We were seeking only to safeguard our own sovereignty and to enter into any
 relationship with other nations only after full and free discussion and deliberation.
 Output: "An Association of Nations" by President Warren G. Harding on July 22, 1920. My countrymen,
 we believe the unspeakable sorrows, the immeasurable sacrifices, the awakened convictions, and the
 aspiring conscience of humankind must commit the nations of the earth to a new and better relationship.
 It need not be discussed now what motives plunged the world into war. It need not be inquired whether we
 asked the sons of this republic to defend our national rights, as I believe we did, or to purge the Old World
 of the accumulated ills of rivalry and greed. The sacrifices will be in vain if we cannot acclaim a new
 order with added security to civilization and peace maintained. One may readily sense the conscience
 of our America. I am sure I understand the purpose of the dominant group of the Senate. We were not
 seeking to defeat a world aspiration. We were not seeking to withhold our country from doing its part in
 the world’s great work. We were seeking only to safeguard our own sovereignty and to enter into
 any relationship with other nations only after full and free discussion and deliberation.




                                                     4364


## Responsible NLP Checklist full text

Responsible NLP Checklist
Paper title: GigaCheck: Detecting LLM-generated Content via Object-Centric Span Localization
Authors: Irina Tolstykh, Aleksandra Tsybina, Sergey Yakubson, Aleksandr Gordeev, Vladimir Dokholyan,
Maksim Kuprashevich
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
        Section 8
✓ B. Did you use or create scientific artifacts? (e.g. code, datasets, models)
□
 □ B4. Did you discuss the steps taken to check whether the data that was collected/used contains any
  N/A


        information that names or uniquely identifies individual people or offensive content, and the steps
        taken to protect/anonymize it?
        We use only previously published, publicly available benchmarks. We did not collect new data
        containing personal information.

  ✓ B6. Did you report relevant statistics like the number of examples, details of train/test/dev splits, etc.
  □
        for the data that you used/created?
        Section 4 and Table 1
✓ C. Did you run computational experiments?
□
 ✓ C2. Did you discuss the experimental setup, including hyperparameter search and best-found
 □
        hyperparameter values?
        Appendix B and Tables 1112

  ✗
  □ C3. Did you report descriptive statistics about your results (e.g., error bars around results, summary
        statistics from sets of experiments), and is it transparent whether you are reporting the max, mean,
        etc. or just a single run?
        We report single-run results without error bars or variance estimates. All models were trained
        once due to the computational cost of fine-tuning 7B parameter models. We use established metrics
        (Accuracy, F1, AUROC, mAP) and follow the evaluation protocols of the original dataset authors for
        fair comparison.
The Responsible NLP Checklist used at ACL Rolling Review is adopted from NAACL 2022, with the addition of ACL 2023
question on AI writing assistance and further refinements based on ARR practice. ACL 2026 used a subset of ARR checklist form.

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

- **Beginning checked:** Rendered paper page 1 was compared with the extraction; the title, authors, affiliation, abstract, Introduction, proceedings footer, and page number are present.
- **Middle checked:** Rendered paper page 8 was compared with the extraction; Tables 8 and 9, the conclusion, Limitations, Ethical Statement, and the start of References are present in the same order.
- **End checked:** Rendered paper page 16 was compared with the extraction; Table 16, its caption, all ground-truth and output examples, and final page number are present.
- **Figure and checklist checked:** Rendered paper page 2 confirms that Figure 1, its caption, and contribution list align with the extraction. Both checklist pages were rendered and compared with the extracted responses, including the single-run and no-variance disclosure.
- **Structure checked:** `pdfinfo` reports 16 A4 pages for the paper and two A4 pages for the checklist. The paper extraction includes Sections 1-8; Tables 1-16; Figure 1; footnotes; Limitations; Ethical Statement; References; and Appendices A-G in the same order as the PDF. `pdfimages -list` reports one color image and its soft mask on paper page 2.
- **Known omissions:** No paper or checklist source text is omitted. Figure pixels, bold interval markings, checkbox typography, and exact page layout are not reproduced in Markdown; they remain available in the preserved PDF attachments.

## Preserved attachments

| Path | Role in the source | SHA-256 | Preservation / extraction notes |
|---|---|---|---|
| `snapshots/attachments/tolstykh-et-al-gigacheck-acl-2026.pdf` | Authoritative ACL proceedings PDF, including Figure 1 and bold span markings in Tables 15 and 16 | `f71f6a2a2671bf5f9d5252e730e4559ded60e409a633aec5e653189dd8a72796` | Downloaded directly from the ACL Anthology PDF URL on 2026-07-15; 16 pages; used for layout extraction and rendered-page verification. |
| `snapshots/attachments/tolstykh-et-al-gigacheck-responsible-nlp-checklist.pdf` | Authoritative ACL Responsible NLP Checklist associated with the paper | `03d32adf530f8b5fd1ff6bcc8cae882af2298fbce873a7b312c538e6092fc4fe` | Downloaded directly from the ACL Anthology checklist URL on 2026-07-15; two pages; complete text extracted above with `pdftotext -layout`. |
