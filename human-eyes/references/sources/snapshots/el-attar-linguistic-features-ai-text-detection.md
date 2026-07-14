# A Systematic Analysis of Linguistic Features in AI-Generated Text Detection Across Domains and Models

- **Canonical URL:** https://arxiv.org/abs/2606.04177
- **Alternate access URLs:**
  - https://arxiv.org/html/2606.04177 (returned 404 on 2026-07-15)
  - https://arxiv.org/pdf/2606.04177
- **Author / owner:** Yassir El Attar, Esra Dönmez, Maximilian Maurer, and Agnieszka Falenska
- **Publisher:** arXiv
- **Published:** 2026-06-02
- **Retrieved:** 2026-07-15
- **Stable identifier:** arXiv:2606.04177v1; DOI 10.48550/arXiv.2606.04177
- **Version / revision:** v1, submitted 2026-06-02
- **Extraction method:** official arXiv v1 PDF downloaded with curl; all 30 pages extracted from the embedded text layer with Poppler `pdftotext -layout`; pages 1, 15, 24, 25, and 30 rendered with `pdftoppm` and visually checked
- **Full-text status:** complete
- **Access and transformation notes:** arXiv HTML returned 404. The PDF text layer preserves all pages, tables, captions, appendices, references, and footnotes. Multi-column reading order and chart labels are mechanically interleaved in places, and some symbol fonts are transformed. The preserved PDF is authoritative for layout, figures, and typography.

## Full text

                                               A Systematic Analysis of Linguistic Features in AI-Generated Text
                                                            Detection Across Domains and Models
                                              Yassir El Attar♡ , Esra Dönmez♡,⋆ , Maximilian Maurer♣,♦ , Agnieszka Falenska♡,⋆
                                                         ♡
                                                           Institute for Natural Language Processing, University of Stuttgart
                                                 ⋆
                                                   Interchange Forum for Reflecting on Intelligent Systems, University of Stuttgart
                                             ♣
                                               GESIS Leibniz Institute for the Social Sciences ♦ Heinrich-Heine University Düsseldorf
                                            ♡
                                              {yassir.el-attar, esra.doenmez, agnieszka.falenska}@ims.uni-stuttgart.de
                                                                          ♣
                                                                            maximilian.maurer@gesis.org

                                                               Abstract                              Li et al., 2024a; Guo et al., 2025). However, such
                                                                                                     explanations are often difficult to interpret for non-
                                             Interpretable linguistic features offer a promis-
                                                                                                     experts (Ji, 2009) and typically provide only lo-




arXiv:2606.04177v1 [cs.CL] 2 Jun 2026
                                             ing approach for explaining why a given text
                                             appears machine-generated, particularly for             cal, example-based insights into the properties of
                                             non-expert users. However, existing find-               generated text (Koike et al., 2025). In response,
                                             ings on which features reliably indicate LLM-           a growing line of research focuses directly on in-
                                             generated text remain fragmented across fea-            terpretable linguistic features, identifying stylo-
                                             ture sets, models, and text domains. To ad-             metric and linguistic differences between human
                                             dress this gap, we conduct a large-scale empir-         and AI-generated writing, such as lexical diver-
                                             ical study assessing the robustness of linguis-
                                                                                                     sity and syntactic regularity (Muñoz-Ortiz et al.,
                                             tic signals for characterizing AI-generated text.
                                             Our analysis covers 284 interpretable linguis-
                                                                                                     2024; Opara, 2024; Reinhart et al., 2025). While
                                             tic features across outputs from 27 LLMs and            these studies provide promising evidence that lin-
                                             ten text domains under cross-model and cross-           guistic features can characterize AI-generated text,
                                             domain generalization settings. We show that            the findings remain fragmented across feature sets,
                                             classifiers based solely on linguistic features         LLMs, and text domains. Consequently, it remains
                                             can reliably distinguish AI-generated from              unclear which signals reflect general properties of
                                             human-written text. However, many previously            generated language and which arise from particular
                                             proposed indicators prove strongly context-
                                                                                                     datasets or model settings (Kehkashan et al., 2025).
                                             dependent, with the exception of measures of
                                             lexical richness, which remain robust signals              In this work, we take a systematic approach to
                                             across model families and text domains. These           clarify the fragmented evidence on linguistic sig-
                                             results demonstrate which linguistic signals            nals of AI-generated text. To this end, we conduct a
                                             generalize across contexts and provide a foun-          large-scale empirical study of AI-authorship detec-
                                             dation for more reliable, interpretable analyses        tion across 27 LLMs and 10 text domains from the
                                             of AI-generated language.                               MAGE benchmark (Li et al., 2024a). Our analysis
                                                                                                     uses a comprehensive set of interpretable linguistic
                                        1     Introduction
                                                                                                     features (284 in total), aggregating and extending
                                        Large Language Models (LLMs) are becoming in-                feature groups previously studied in stylometry,
                                        creasingly adept at producing fluent and stylisti-           readability analysis, and AI-text detection. With
                                        cally human-like text. The societal implications of          a focus on realistic cross-model and cross-domain
                                        this development are significant: the ease of pro-           generalization settings, where detectors must op-
                                        ducing large-scale synthetic text amplifies the risk         erate on unseen models or text types, we answer
                                        of misinformation while simultaneously challeng-             three central questions:
                                        ing cues used to assess authorship and factuality            RQ1 How robust are linguistic features for dis-
                                        (Srivastava, 2025). This creates a growing need for          tinguishing LLM-generated from human-authored
                                        interpretable explanations of why a text appears             text across models and domains?
                                        machine-generated, particularly in settings where
                                        unreliable or biased detectors can have significant          RQ2 Which linguistic features consistently con-
                                        consequences (Jiang et al., 2024).                           tribute to distinguishing AI-generated from human-
                                           Most existing approaches explain why a text ap-           written text across models and domains?
                                        pears machine-generated by interpreting the deci-            RQ3 How do linguistic signals of AI-generated
                                        sions of black-box classifiers (Zellers et al., 2019;        text vary across model families and text domains?

                                                                                                 1
   First, we show that classifiers based solely on lin-         handcrafted indicators, and Doughman et al. (2025)
guistic features achieve strong performance across              uses a small set of linguistic features (POS/NER,
models and domains (§4.1), demonstrating that                   readability, and lexical features) for post-hoc analy-
interpretable linguistic signals can reliably distin-           sis of LLM-based detection. These studies demon-
guish human- and AI-generated text. Second, sys-                strate that interpretable linguistic features can re-
tematic feature-ablation experiments reveal that                veal systematic differences between human and
many previously reported linguistic indicators vary             AI-generated texts. However, most analyses focus
substantially across models and domains, with mea-              on a limited number of models, domains, or fea-
sures of lexical richness emerging as the most                  ture sets. Consequently, it remains unclear how
consistently informative group across contexts                  broadly such linguistic signals generalize across
(§4.2). Finally, linguistic signals vary systemat-              different models and text domains.
ically across both model families and text domains,                Recent work has also highlighted the importance
with different models exhibiting distinct stylomet-             of robustness and generalization in AI-text de-
ric patterns (§4.3). Taken together, this work pro-             tection. Large-scale evaluations show that many
vides a systematic evidence that linguistic charac-             detectors and linguistic signals degrade under dis-
teristics of AI-generated text exhibit both robust              tribution shift, such as unseen models, domains, or
and context-dependent patterns: while some sig-                 generation settings (Li et al., 2024a; Wang et al.,
nals, such as lexical richness, generalize across               2024; Dugan et al., 2024). Moreover, some ap-
models and domains, others depend on specific                   parent linguistic cues may arise from confounding
generation settings. This highlights the importance             factors such as decoding strategies, prompts, or
of evaluating linguistic explanations under realistic           dataset artifacts rather than properties of machine-
cross-model and cross-domain conditions.                        generated language (Li et al., 2024a; Reinhart et al.,
                                                                2025). This raises a broader question: to what
2   Related Work                                                extent reported linguistic cues reflect genuine
                                                                properties of AI-generated language.
Much of the literature on AI-generated text focuses
on the task of automatic detection (Gehrmann                    3     Methods
et al., 2019; Li et al., 2025; Zhang et al., 2024; Guo
et al., 2024; Ji et al., 2024, inter alia), often relying       In this work, we train a classifier based on inter-
on black-box systems (Zellers et al., 2019; Guo                 pretable linguistic features to distinguish between
et al., 2025). Efforts to improve interpretability typ-         human-written and LLM-generated text. Using this
ically rely on post-hoc explanation methods, such               classifier, we analyze which linguistic signals con-
as feature attribution (Ji, 2009) or example-based              tribute most strongly to the prediction and evaluate
explanations (Koike et al., 2025). In parallel, sev-            their robustness across models and text domains. In
eral large-scale benchmarks and shared tasks have               this section, we describe the data used to train the
been proposed to evaluate detection performance                 classifiers, the linguistic features we extract, and
across datasets and models (Koike et al., 2024; Li              the methodological steps taken to analyze linguistic
et al., 2024b; He et al., 2024; Wang et al., 2024;              signals of LLM-generated text.
Li et al., 2024a, inter alia). However, the primary
focus of this strand of research remains improving              3.1    Data
detection accuracy rather than interpretability.                We use the MAGE dataset (Li et al., 2024a), a
   A smaller but growing line of research instead ex-           benchmark for detecting English LLM-generated
amines interpretable linguistic signals that distin-            text, where each instance pairs a human-written
guish AI-generated from human-written language.                 passage with continuations from 27 models from
For example, Muñoz-Ortiz et al. (2024) identify                 seven families, referred to as model domains hence-
morphosyntactic and semantic indicators that dif-               forth (OpenAI GPT, LLaMA, GLM-130B, FLAN-
ferentiate human- and AI-authored texts in the                  T5, OPT, BigScience, and EleutherAI). The human-
news domain, while Dönmez et al. (2025) analyze                 written texts come from 10 sources spanning multi-
LLM-generated counterarguments. Reinhart et al.                 ple writing tasks: opinion statements (CMV, Yelp),
(2025) employ Biber’s 67-feature tagset to explore              news articles (XSum, TLDR), question answering
linguistic patterns in generated text, Opara (2024)             (ELI5), story generation (WritingPrompts, ROC-
propose a stylometric detection approach based on               Stories), commonsense reasoning (HellaSwag),

                                                            2
knowledge illustration (SQuAD), and scientific                       Testbeds We evaluate detection performance on
writing (SciGen) (size details in Section A.1).                      eight testbeds from Li et al. (2024a) that vary in
MAGE also provides a GPT-4-generated test set                        generalization scenarios (see summary in Table 1
from four novel domains (CNN/DailyMail, Dialog-                      and Section A.4 for details). While some testbeds
Sum, IMDb, PubMed) to evaluate detection on                          operate at fine-grained model granularity (e.g., TB1
completely out-of-distribution data.1                                evaluates domain–model pairs across all 27 mod-
                                                                     els), we present most analyses at the level of model
3.2    Linguistic Features                                           families to reduce noise from individual model vari-
We extract interpretable linguistic features with the                ation and improve interpretability.
elfen Python package (Maurer, 2026) from vari-
ous groups: surface-level, syntactic, and morpho-                    3.4    Experiments
logical structures as well as information-theoretic,                 We run two sets of experiments: (1) LLM-
lexical richness, semantic, and named entity fea-                    authorship detection (RQ1), which evaluates the
tures, and features based on measurements of emo-                    effectiveness and robustness of classifiers based
tional and psycholinguistic grounding of tokens.                     on interpretable linguistic features, and (2) feature
For surface-level, lexical richness, and readability                 area ablation (RQ2 and RQ3), which analyzes the
features, we retrain only one measure from each set                  contribution of different linguistic feature groups.
of theoretically equivalent features. For instance,
both the type-token ratio (TTR) and the lemma-                       3.4.1 LLM-Authorship Detection
token ratio capture lexical richness, despite differ-                Classifiers are evaluated under in-domain (ID)
ing in formulation. Section A.3 provides a full                      and out-of-domain (OOD) conditions across three
overview of the features used in our experiments.                    evaluation scenarios: general classification, model
   Except for raw counts of types, sentences, char-                  domain effects, and text domain effects. General
acters, lemmas, and syllables (e.g., the number of                   classification uses TB4 and TB1 in ID settings, and
named entities in a text), we normalize count-based                  TB8 and TB7 in OOD settings. Model domain ef-
features by token count to obtain relative frequen-                  fects are evaluated with TB2 (ID) and TB5 (OOD),
cies. We remove uniform features (i.e., features                     while text domain effects are evaluated with TB3
with only one value over the dataset) and handle                     (ID) and TB6 (OOD).
missing and infinite values through feature-specific
                                                                     3.4.2 Feature Area Ablations
imputation: binary features are imputed with the
mode, integer features with the median, and con-                     We conduct two types of ablation studies to investi-
tinuous features with either the mean (for normally                  gate feature area importance: (A) Leave-one-out,
distributed features) or median (for skewed distri-                  where classifiers are trained on all eleven feature
butions), ensuring that the statistical properties of                areas but one, and (B) Cumulative, where feature
each feature are preserved during preprocessing.                     areas are removed sequentially according to their
                                                                     importance in (A), and classifiers are retrained with
3.3    Classifier, Metrics and Evaluation                            progressively fewer feature areas. We run (A) on
Classifier We use a linear Support Vector Ma-                        all testbeds and (B) only for the domain-agnostic
chine (SVM) with class weighting to account for                      single-classifier settings (TB4 and TB7) to avoid
the strong class imbalance between human and                         the combinatorial explosion of ablation classifiers.
LLM texts in MAGE (details on model choice and
parameters in Section A.2).
                                                                     4     Results

Metrics and Evaluation We evaluate detection                         This section first presents the results of the LLM-
performance using three metrics: Macro F1, which                     authorship detection experiments addressing RQ1
accounts for class imbalance in test sets; AUROC                     and then analyzes feature-area ablations to address
(Area Under the Receiver Operating Characteris-                      RQ2 and RQ3.
tic curve) which measures discrimination between                     4.1    LLM-Authorship Detection
classes across decision thresholds; and AvgRec
(Average Recall, details in Section A.2).                            We first examine general detection performance,
                                                                     followed by an analysis of model and text domain
   1
    Potential prompt effects are discussed via a cross-dataset       effects. Table 2 presents the results, where our clas-
experiment in Section A.1.                                           sifier appears as “SVM w/ Ling. Feats.”, while the

                                                                 3
Name      Setting                                      Description
TB1       Text domain & model specific                 One classifier per text domain–model pair; trained and tested on data from the same domain–model
                                                       combination.
TB2       Arbitrary text domains & model domain-       One classifier per model domain; trained and tested on all text domains but using data from only one
          specific                                     specific model.
TB3       Fixed text domain & arbitrary models         One classifier per text domain; trained and tested on all model domains but using data from only one
                                                       specific text domain.
TB4       Arbitrary text domains & arbitrary models    A single classifier trained and tested on all available data across all text and model domains.
TB5       Arbitrary text domains & unseen model do-    Leave-one-model-domain-out evaluation: trained on all data except one model domain and tested on the
          main                                         held-out model domain.
TB6       Unseen text domains & arbitrary models       Leave-one-text-domain-out evaluation: trained on all data except one text domain and tested on the
                                                       held-out text domain.
TB7       Unseen text domains & single unseen model    Trained on all available data and evaluated on entirely new text domains (CNN, DialogSum, IMDb,
                                                       PubMed) generated by GPT-4.
TB8       Unseen text domain & unseen model domain     Leave-one text–model pair out: trained on all data except one text–model domain pair and tested on the
                                                       held-out pair; ; similar to TB7 but using existing domains to control for text–model pair effects.


    Table 1: Evaluation testbeds used to analyze classifier robustness across text domains and model domains.


Setting   Method                    AvgRec      AUROC        Macro F1                     Model Domain           ID       OOD         Difference
TB1       SVM w/ Ling. Feats.            .954         .987           .788                                      (TB2)      (TB5)     (TB5 - TB2)

          FastText                       .788          .83              -                 OPT                   .914       .714             -.199
          GLTR                           .554          .74              -                 Eleuther              .881       .528             -.353
TB4       Longformer                     .905          .99              -                 FLAN-T5               .766       .673             -.092
                                                                                          LLaMA                 .753       .644             -.110
          SVM w/ Ling. Feats.            .840         .968           .827                 BigScience            .656       .595             -.061
          FastText                       .703          .74              -                 GLM                   .618       .496             -.122
          GLTR                           .577          .73              -                 OpenAI                .555       .616             +.061
TB7       Longformer                     .758          .94              -                 Mean                  .735       .609              -.125
          SVM w/ Ling. Feats.            .818         .907           .808
TB8       SVM w/ Ling. Feats.            .806         .945           .588       Table 3: Macro F1 results of ID (TB2), OOD (TB5),
                                                                                and their difference per model domain. TB2 trains and
Table 2: Aggregate classification results: In-domain                            tests on the same model domain data with arbitrary
(TB1 and TB4) and Out-of-domain (TB7 and TB8); Av-                              domains, while TB5 excludes the target model domain
gRec and AUROC for comparison to MAGE baselines                                 from training, ordered by ID performance (descending).
(FastText, GLTR and Longformer by Li et al. (2024a))
and Macro F1 for cross-experiment comparability.
                                                                                text domains-model pair seems far less challenging
                                                                                than some of the other text and model domain pairs,
remaining methods come from Li et al. (2024a).                                  as evident in TB8. We now zoom into these domain
In the mixed in-domain setting (TB4), where a                                   effects on classifier performances.
single classifier is trained and tested on all data,
our method achieves 82.7% F1. While this score                                  Model Domain Effects Table 3 presents the clas-
indicates some room for improvement, the AU-                                    sifier performances in ID and OOD experiments.
ROC comparison shows that our simple and in-                                    When trained and tested on the data from the same
terpretable method surpasses three substantially                                model domain (ID), the classifiers perform dif-
more resource-demanding and blackbox methods                                    ferently for each model domain. For OPT and
by a large margin and is only 2% below the best-                                Eleuther, the classifiers perform well above the
performing Transformer-based model. When the                                    domain-agnostic ID experiments (by +8.7% and
classifier is trained and tested separately on each                             +5.4% resp.; cf. Table 2, TB4, 82.7% to Table 3,
text domain-model pair (TB1), the average perfor-                               ID), and for BigScience, GLM, and OpenAI, well
mance decreases to 78.8% F1, suggesting domain                                  below (by −17.1%, −20.9%, and −27.2%). This
effects on the classification performance. These                                indicates that certain model domains exhibit dis-
domain effects are much more pronounced in the                                  tinct linguistic signatures that alone provide suffi-
OOD experiments (TB8), where the average perfor-                                cient signal for the model domain-specific classi-
mance drops to 58.8% (23.9% performance drop                                    fiers. Looking at the OOD performance, where the
from the ID setting in TB4). Finally, in the un-                                performance drops by 19.9% and 35.3%, for OPT
seen text domain and model experiment (TB7), we                                 and Eleuther, respectively, it becomes clear that the
achieve 80.84% F1 and only 3% lower AUROC                                       presence of such linguistic model domain idiosyn-
compared to Li et al. (2024a). This set of unseen                               cracies in the training data is vital for detectability.

                                                                            4
    Task
                   Text       ID    OOD       Difference              0.9
                   Domain   (TB3)   (TB6)   (TB6 - TB3)
                                                                      0.8
    Story          WP       .964    .883           -.081
                                                                      0.7
                                                               Macro F1
    Generation     ROCT     .928    .668           -.260
    Commonsense                                                       0.6
                   HSwag    .953    .739           -.214
    Reasoning                                                         0.5
    News           XSum     .941    .897           -.044              0.4
    Articles       TLDR     .908    .704           -.205
                                                                      0.3
    Scientific                                                            big sc
                                                                            eleience
                                                                                 ut
                   SciGen   .920    .927          +.008                        flanher
                                                                                     -t5
                                                                                    glm
                                                                                 llam
    Writing                                                                    ope a na
                                                                                    opti
                                                                                   cm
                                                                                    ev
                                                                               hswli5
                                                                                   r ag
                                                                              sci_ oct
                                                                                sqguen
    Question                                                                        tladdr
                                                                                     w
                                                                                 xsu p
                                                                                   yeml
                   ELI5     .873    .807           -.066                                p
    Answering
    Knowledge
                   SQuAD    .829    .667           -.163
                                                                Figure 1: Distribution of Macro F1 scores across TB8
    Illustration                                                (unseen text domain-model domain pairs), left pane for
    Opinion        CMV      .924    .866           -.058        model domains and the right pane for text domains.
    Statements     Yelp     .804    .777           -.028
                   Mean     .904    .794           -.111
                                                                 SQuAD, the drop is more moderate, at 16.3%; for
Table 4: Macro F1 results of ID (TB3), OOD (TB6)                 SciGen, performance improves slightly, by 0.8%;
and their difference. TB3 trains and tests on the same           and for the remaining domains, performance drops
domain with arbitrary models, while TB6 excludes the
                                                                 only marginally. Thus, the availability of text-
target domain from training, ordered by ID performance.
                                                                 domain data affects the classifier performance, and
                                                                 at times, quite substantially. Finally, for the un-
Similarly, for the remaining model domains, we                   seen text and model domain setting (TB8; Figure 1,
observe a moderate to low performance drop (by                   right), we observe a large performance discrepancy
12.2% to 6.1%). Surprisingly, in the OOD setting,                ranging from 71% to 43.7% F12 .
the performance increases for the OpenAI mod-
els, suggesting that the models display linguistic               Answer to RQ1: Linguistic features provide ro-
markers that generalize over LLMs, which can be                  bust and generalizable signals for distinguish-
useful in OOD settings provided sufficient variety               ing LLM-generated from human-authored text
in LLM-generated training data.                                  across models and text domains. Feature-driven
   Finally, we examine the unseen text–model do-                 classifiers achieve comparable results to resource-
main setting (TB8). The results, summarized in                   intensive blackbox methods while relying on sim-
Figure 1 (left), reveal similar patterns to TB5: clas-           ple and interpretable representations. Our results
sifiers performing worse for GLM, Eleuther, Big-                 indicate the presence of generalizable linguistic
Science, and OpenAI (48.1%, 51.0%, 57.6%, and                    markers of LLM-generated text; however, differ-
59.7%), and better for OPT, FLAN, and LLaMA                      ences in ID and OOD performance highlight sub-
on average (68.4%, 63.7%, 62.8%).                                stantial influences of model and text domain.

Text Domain Effects Table 4 presents the classi-                 4.2        Features of AI-Authored Texts
fier performances in both ID and OOD experiments.               We now zoom in on the effects of the types of lin-
When trained and tested on the data from the same               guistic features on the classification performance.
text domain (ID), discrepancy is less pronounced                We start by discussing the general classifiers and
than in the model domain experiments, suggest-                  then focus on the model and text domains.
ing that text domain effects are not as detrimental                Table 5 displays the results from the leave-one-
to classifier performance as model domain for in-               out feature area ablation on the ID domain-agnostic
domain classification (cf. Table 3, ID to Table 4,              classifier (TB4) and the OOD setting (TB7). In the
ID). For most of the domains, the ID performance                TB4 setting, we make two observations. First, drop-
is above 90% F1, and the lowest performance is still            ping lexical richness features results in a stark per-
relatively high, at 80.42%. Nonetheless, the OOD                formance drop of −13.1%, far larger than for any
experiments reveal several noteworthy patterns: for             other feature area. The next most influential area is
ROCStories, HellaSwag, and TLDR, performance                    information, with −1.8% drop. Second, the effects
drops most sharply, by 26.0%, 21.4%, and 20.5%,                     2
                                                                      Similarly for the individual text domains in TB7 with
respectively; this is consistent with their larger               96.82%, 87.18%, 83.10% and 50.24% F1 for CNN, pubmed,
distributional differences (see Section E.1). For                imdb and dialogsum, respectively (see Appendix, Table 11).


                                                           5
                        Baseline    Surface       LexRich.    Emotion        Psycholing.    Read.    Morph.        POS      Depend.   Semantic   Entities   Inform.
              TB4            .827       .822          .696            .824          .821      .827        .824     .823        .823       .825      .827        .809
F1 Macro
              TB7            .808       .818          .531            .814          .834      .806        .846     .815        .819       .808      .810        .824
 # Feats. Removed               0             6         3              36              77        2          58       18          47        16         19           2


Table 5: Leave-one-out ablation results for TB4 (arbitrary text domains & arbitrary models) and TB7 (unseen text
domains & model). Classifier performances when each feature area is dropped from the full feature set.

84                                                                                                                                                             95.13%
     82.72% 82.73% 82.56%                                                            95                                          94.14% 93.84% 93.48% 93.59%
                            82.27% 82.03%                                                                                                                      +1.54%
                                            81.59% 81.22%                                                          91.64% 91.94% +2.20%
82                                                           81.11%                                       90.04%
                                                                      80.06%         90                            +1.60%
80                                                           -1.05%                             86.46% +3.58%
                                                                                          84.58% +1.88%
78                                                                     -2.43% 77.64% 85
           Ablation Macro F1
           Baseline Macro F1 (All Features)
76E
(226ntileties                               P
                                       (76 leOftS                                    80
                                                                                     Mo ph
                                                                                    (226rle  o.
                                                                                            ft)
 Reada    ft)                          Depen
                                       (40 leftd.)                                     P
                                                                                    (149sleych.
                                                                                            ft)
                                                                                       Inform
                                                                                    (147 le .
(149 le b.
 Seman    ft)                           Surfac
                                       (21 left e)                                   Depen  ft)
                                                                                    (100 le d.
                                                                                      Surfacft)
                                                                                     (94 left e
(147 le t.
 Emotio   ft)                            Psych
                                        (5 left).)                                        POS
                                                                                     (76 left
                                                                                     Emotio   )
                                                                                              )
                                                                                     (40 left n
(100 le n
 Morph    ft)                            Info
                                        (3 lerftm).                                   Entitie )
                                                                                     (21 left s
                                                                                     Seman    )
                                                                                      (5 left)t.
 (94 lefto. )                                                                        Reada
                                                                                      (3 leftb).



Figure 2: Macro F1 performance changes with cumulative feature area removal. The left pane shows results for
TB4, and the right pane for TB7, in performance impact order from Table 5.


from the remaining 10 feature areas are marginal,                                       based on performance analysis (see Section C.3), in
with the largest decrease of −0.23%. These effects                                      total 16 pairs. We display the findings in Figure 6.
align with the cumulative ablation results (left pane                                   The experiments reveal two major findings: 1) lex-
of Figure 2). Dropping the readability and enti-                                        ical richness features systematically characterize
ties areas initially increases the performance. As                                      AI-authored texts (except for the SQuAD text do-
the remaining areas are removed one by one, the                                         main) with a varying degree, 2) other feature areas
performance slowly degrades. However, even after                                        like surface, psycholinguistic, information, depen-
removing ten areas, the classifier retains much of                                      dency, and morphological display varying levels
its performance, dropping only about 5% from the                                        of informativeness depending on text domain and
full-feature baseline (from 82.67% to 77.64%).                                          model domain pairs. For XSum with LLaMA or
   In the OOD setting (TB7 in Table 5), the results                                     OpenAI pairs, the performance increases with the
for lexical richness are similar to the ID setting.                                     removal of all four feature areas but information
For the remaining areas, the results vary, with a                                       (detailed discussion in Section C.4).
slight performance decrease for the semantic and
readability areas (−0.06% and −0.28%) and an                                           Model Domain Effects Figure 3 presents the fea-
increase for the remaining ones (max. +3.74%).                                         ture area ablation results under the ID setting. Two
Unlike the ID setting, the cumulative ablation here                                    trends are immediately apparent. First, removing
reveals an interesting trend (see right pane, Fig-                                     the lexical richness features from training yields
ure 2), where removing the first six feature areas                                     opposing effects across models: performance im-
improves performance by +13.3%, and continuing                                         proves for OpenAI, LLaMA, and GLM (+0.31%,
with the next three areas degrades performance by                                      +2.20%, and +2.54%, respectively), whereas it
−0.55%. Furthermore, in the presence of only the                                       decreases for FLAN-T5, OPT, BigScience, and
lexical richness and readability features, readabil-                                   Eleuther (9.5%, 3.23%, 5.71%, and 2.44%, respec-
ity features similarly degrade the performance, with                                   tively). Second, for OpenAI and LLaMA mod-
an increase in F1 by +1.54% when removed. To                                           els, the classifier performs better without several
understand this trend, we now discuss a similar ab-                                    feature areas, i.e., lexical richness, surface, and
lation for TB8, the data for which we can compare                                      readability all slightly improve F1 when removed.
the results across experiments.                                                        Conversely, simpler models FLAN-T5 and Big-
   As a complete ablation of 70 pairs (770 classi-                                     Science show consistent and larger drops across
fiers) is not feasible, we run the leave-one-out abla-                                 most area removals, indicating more salient linguis-
tion on four text domains and four model domains                                       tic signatures. The ablation in the OOD setting

                                                                                   6
                      openai         llama            glm            flan_t5           opt             bigscience         eleuther
      0.9

      0.8

      0.7

      0.6

      0.5
            Surface Lexi. Rich. Emotion      Psych.    Readab.       Morpho.     POS         Depend.      Semant.   Entities    Inform.

Figure 3: Ablation results on TB2. The horizontal dashed lines indicate the baseline results (all features) and the
bars indicate the performance change in Macro F1 after removing the corresponding feature area.


0.7                                                                       4.3   Text Domain Effects
                                                                          Figure 5 displays the feature area ablation results
0.6
                                                                          on the ID and OOD settings. For the ID setting
0.5                                                                       (upper pane), dropping lexical richness consistently
                                                  Baseline (0.609)        degrades the classifier performance across all ten
0.4
  Lexi   ace
      . Ric
    Emo
     Psy
            h.
         tion                                                rm.          text domains (ranging from 2.5% for HellaSwag
                                                            Info
           ch.
SurfRea
    Mor
    Dep
        dab
        pho
        POS
             .
             .                                                            to 11.8% for ELI5) but one, SQuAD (+0.19%),
    Sem end
         ant..
     Enti
                                                                          which is intuitive as SQuAD answers are based on
          ties

Figure 4: Ablation performance ranges on TB5 across                       a provided context and are typically short phrases
the 11 feature areas after removing the corresponding                     unlikely to vary considerably in lexical richness.
feature area compared to the baseline (dashed red line).                  For this domain, the areas that exhibit the largest
                                                                          performance drops are surface, emotion, and POS,
                                                                          again intuitive as different choices of answer spans
shows interesting patterns (see Figure 4). Drop-                          would result in variance in these features. Second,
ping lexical richness results in a stark performance                      the effects of the remaining feature areas on the
drop for all models this time, followed by infor-                         text domains vary quite a lot, without a clear trend
mation features. This suggests lexical richness                           for types of texts such as opinion statements or
and information features encode salient signals that                      story generation. Similar to observations from the
generalize across models and are critical for OOD                         model domain experiments, in the OOD setting
detection, whereas in the ID setting, the classifier                      (lower pane in Figure 5), lexical richness features
can likely learn sufficient patterns from the remain-                     carry crucial information, with drops ranging from
ing features. To provide qualitative intuition for                        27.45% (XSum) to 0.3% (SQuAD)3 . Additionally,
these patterns, Section D presents representative                         observed from Figure 6, for XSum, readability,
human- and LLM-generated examples illustrating                            psycholinguistics, morphological, and surface (also
differences in the most influential feature areas.                        for WritingPrompts) features all seem noisy when
Answer to RQ2: Lexical richness has the largest                           both text and model domain pair is unseen.
impact on classifier performance, emerging as                             Answer to RQ3: Feature areas display varying
the strongest indicator of LLM-generated text.                            levels of importance in text domains. While lex-
Feature ablations on the model domains further in-                        ical richness4 , given its idiosyncrasy across LLMs,
dicate that models cluster into two groups: a) Ope-                       remains the most influential feature area, the im-
nAI, Llama, and GLM, and b) FLAN-T5, OPT, and                             portance of other areas varies substantially. To
BigScience. One possible explanation is that mod-                         better understand these differences, we analyze
els within each group share similarities in archi-                        similarities between text domains by comparing
tectures, training data, or instruction-tuning, which                     feature distributions using Wasserstein distances
leads to similarities in their linguistic markers. To                     (Section E.1). The results reveal differences be-
further investigate this observation, we analyze cor-                     tween domains that help explain variation in feature
relations of feature-area contributions across model                         3
                                                                               Similar effects can be observed for TB7 (see Section C.2,
families (Section E.2), which provide statistical                         Figure 9.)
                                                                             4
support for these model groupings.                                             Further analyses on this feature area in Section C.4.


                                                                      7
            cmv     yelp       xsum                    tldr           eli5         wp         roct         hswag      squad      sci_gen


0.9


0.8


0.7

0.9

0.8

0.7

0.6

0.5 Surface Lexi. Rich. Emotion         Psych.                Readab. Morpho.           POS          Depend. Semant. Entities   Inform.

Figure 5: Macro F1 results of ablation study, top pane: TB3 and bottom pane: TB6. The horizontal dashed lines
indicate baseline results for each model, and the bars the performance after dropping the corresponding feature area.

                     Psych.
                                      Emotion                                    we showed that linguistic features (interpretable
          Readab.                                                                to both experts and non-experts) are highly infor-
                                                                                 mative of whether a text is generated by an LLM.
                                                        Lexi. Rich.              At the same time, the linguistic markers of gener-
                                                               0.1               ated text are far from uniform. Many indicators
Morpho.                                                 0.0
                                                 0.1                             previously proposed in the literature turn out to de-
                                        0.2
                                0.3                                              pend strongly on particular models or text domains.
                                                                Surface
                                                                                 In contrast, measures of lexical richness consis-
                                                                                 tently emerge as robust signals across contexts. Be-
    POS
                                                                                 yond individual features, systematic patterns also
                                                                                 appear across groups of LLMs and types of text
                                                          Inform.
                                                                                 domains, suggesting that both model architecture
      wp Depend.                                               openai            and discourse context shape the characteristics of
      tldr                                                     llama
      squad                           Entities                 eleuther          generated language.
      xsum          Semant.                                    bigscience

Figure 6: Ablation performance variance across 16 text
domain-model domain after removing the correspond-
ing feature area (selection based on Section C.3).
                                                                                    These findings highlight both the promise and
                                                                                 the limitations of linguistically grounded explana-
informativeness and classifier performance.                                      tions of AI-generated text. While some signals gen-
                                                                                 eralize across contexts, others depend on specific
5     Conclusions and Discussion
                                                                                 models or domains. As a result, detection systems
LLM-generated text increasingly populates both                                   deployed in real-world settings, such as recogniz-
formal and informal discourse. Understanding the                                 ing LLM-generated peer reviews or papers, must
linguistic markers that signal such text is therefore                            be evaluated under diverse conditions and updated
essential, both to develop effective detection meth-                             as new models emerge. More broadly, our results
ods and to provide interpretable explanations to                                 emphasize the importance of systematically assess-
participants of such discourse.                                                  ing the robustness of linguistic signals when using
   Through extensive classification experiments,                                 them to interpret or detect AI-generated language.

                                                                             8
Limitations                                                  of user texts to match a desired stylistic profile. Ad-
                                                             ditionally, classifiers based on fully interpretable
Our setup and findings are limited in several ways.
                                                             linguistic features can serve as effective educational
Firstly, while we find particular patterns in English
                                                             tools, helping the public recognize LLM-generated
data, this may not hold for other languages. In
                                                             content. Finally, all human-authored texts used
principle, our methods could be easily applied to
                                                             in our analyses were drawn from publicly avail-
any language that (a) has the necessary benchmarks
                                                             able datasets and handled in accordance with estab-
with a broad coverage available, and (b) external
                                                             lished ethical research standards. No identifiable or
tooling to extract the features. The feature extrac-
                                                             private user data was used. Nonetheless, ongoing
tion tool we use covers a large number of languages,
                                                             reflection on issues of consent, data provenance,
but has some blind spots, particularly regarding
                                                             and user agency remains vital when working with
low-resource languages and/or languages from the
                                                             human discourse.
African continent. Moreover, the applicability of
the feature definitions, especially for lexical rich-        Acknowledgments
ness, depends on the particular language. Results in
other languages may thus not necessarily be strictly         We acknowledge the support of the Ministerium für
comparable.                                                  Wissenschaft, Forschung und Kunst BadenWürt-
   Secondly, while we use, to the best of our                temberg (MWK, Ministry of Science, Research and
knowledge, the broadest and most current available           the Arts Baden-Württemberg under Az. 33-7533-9
benchmark, it does not cover the newest models.              19/54/5) in Künstliche Intelligenz & Gesellschaft:
Our results thus have limited informativeness on             Reflecting Intelligent Systems for Diversity, De-
the behavior of these models. While this is outside          mography and Democracy (IRIS3D) and the sup-
of the scope of this paper, it underlines the need for       port by the Interchange Forum for Reflecting on
continually updated benchmarks to assess whether             Intelligent Systems (IRIS) at the University of
findings on one set of models still hold.                    Stuttgart.
   Finally, our experiments cover two important di-
mensions that impact the detectability of machine-
generated text: text domain and model (family).              References
We do not consider prompt variants as a potential
                                                             Marie-Catherine de Marneffe, Christopher D. Man-
source of performance variation. Though outside               ning, Joakim Nivre, and Daniel Zeman. 2021. Uni-
of the scope of this paper and challenging due to a           versal Dependencies. Computational Linguistics,
lack of availability of resources covering all three          47(2):255–308.
dimensions, we provide a small pilot experiment
                                                             Esra Dönmez and Agnieszka Falenska. 2025. “I under-
including prompt formulation as a factor of perfor-            stand your perspective”: LLM persuasion through the
mance variation on one of the datasets (CMV) in                lens of communicative action theory. In Findings of
Section B.2.                                                   the Association for Computational Linguistics: ACL
                                                               2025, pages 15312–15327, Vienna, Austria. Associa-
Ethical Considerations                                         tion for Computational Linguistics.

While our work advances understanding of the fea-            Esra Dönmez, Maximilian Maurer, Gabriella Lapesa,
tures and quality of LLM-generated texts, it raises            and Agnieszka Falenska. 2025. AI argues differ-
                                                               ently: Distinct argumentative and linguistic patterns
several important ethical considerations. First, in-           of LLMs in persuasive contexts. In Proceedings
sights from our findings raise potential dual-use              of the 2025 Conference on Empirical Methods in
concerns. On one hand, they could be misused by                Natural Language Processing, pages 34583–34614,
malicious actors to develop tools that better mimic            Suzhou, China. Association for Computational Lin-
                                                               guistics.
human writing patterns. It is therefore essential not
only to highlight these risks but also to support com-       Jad Doughman,         Osama Mohammed Afzal,
munity efforts to identify, mitigate, and safeguard            Hawau Olamide Toyin, Shady Shehata, Preslav
against such misuse. On the other hand, under-                 Nakov, and Zeerak Talat. 2025. Exploring the
standing the linguistic signatures of AI-generated             limitations of detecting machine-generated text. In
                                                               Proceedings of the 31st International Conference
text has constructive applications. These insights             on Computational Linguistics, pages 4274–4281,
can help guide generation toward more appropriate              Abu Dhabi, UAE. Association for Computational
content, for example, by suggesting reformulations             Linguistics.


                                                         9
Liam Dugan, Alyssa Hwang, Filip Trhlík, Andrew                     text detection: A comprehensive review of methods,
  Zhu, Josh Magnus Ludan, Hainiu Xu, Daphne Ip-                    datasets, and applications. Computer Science Review,
  polito, and Chris Callison-Burch. 2024. RAID: A                  58:100793.
  shared benchmark for robust evaluation of machine-
  generated text detectors. In Proceedings of the 62nd           J. Peter Kincaid, Robert P. Jr. Fishburne, Richard L.
  Annual Meeting of the Association for Computational               Rogers, and Brad S. Chissom. 1975. Derivation Of
  Linguistics (Volume 1: Long Papers), pages 12463–                 New Readability Formulas (Automated Readability
  12492, Bangkok, Thailand. Association for Compu-                  Index, Fog Count And Flesch Reading Ease Formula)
  tational Linguistics.                                             For Navy Enlisted Personnel. Technical report, Insti-
                                                                    tute for Simulation and Training.
Sebastian Gehrmann, Hendrik Strobelt, and Alexander
  Rush. 2019. GLTR: Statistical detection and visual-            Ryuto Koike, Masahiro Kaneko, Ayana Niwa, Preslav
  ization of generated text. In Proceedings of the 57th            Nakov, and Naoaki Okazaki. 2025.            Exagpt:
  Annual Meeting of the Association for Computational              Example-based machine-generated text detection for
  Linguistics: System Demonstrations, pages 111–116,               human interpretability. Preprint, arXiv:2502.11336.
  Florence, Italy. Association for Computational Lin-
  guistics.                                                      Ryuto Koike, Masahiro Kaneko, and Naoaki Okazaki.
                                                                   2024. Outfox: Llm-generated essay detection
Hanxi Guo, Siyuan Cheng, Xiaolong Jin, Zhuo Zhang,                 through in-context learning with adversarially gener-
  Guangyu Shen, Kaiyuan Zhang, Shengwei An, Guan-                  ated examples. In Proceedings of the AAAI Confer-
  hong Tao, and Xiangyu Zhang. 2025. Profiler: Black-              ence on Artificial Intelligence, volume 38(19), pages
  box AI-generated text origin detection via context-              21258–21266.
  aware inference pattern analysis. In Proceedings
  of the 2025 Conference on Empirical Methods in                 Ran Li, Wei Hao, Weiliang Zhao, Junfeng Yang, and
  Natural Language Processing, pages 24903–24923,                  Chengzhi Mao. 2025. Learning to rewrite: Gen-
  Suzhou, China. Association for Computational Lin-                eralized llm-generated text detection. Preprint,
  guistics.                                                        arXiv:2408.04237.

Xun Guo, Shan Zhang, Yongxin He, Ting Zhang, Wan-                Yafu Li, Qintong Li, Leyang Cui, Wei Bi, Zhilin Wang,
  quan Feng, Haibin Huang, and Chongyang Ma. 2024.                 Longyue Wang, Linyi Yang, Shuming Shi, and Yue
  DeTeCtive: detecting AI-generated text via multi-                Zhang. 2024a. MAGE: Machine-generated text de-
  level contrastive learning. In Proceedings of the 38th           tection in the wild. In Proceedings of the 62nd An-
  International Conference on Neural Information Pro-              nual Meeting of the Association for Computational
  cessing Systems, NIPS ’24, Red Hook, NY, USA.                    Linguistics (Volume 1: Long Papers), pages 36–53,
  Curran Associates Inc.                                           Bangkok, Thailand. Association for Computational
                                                                   Linguistics.
Xinlei He, Xinyue Shen, Zeyuan Chen, Michael Backes,
  and Yang Zhang. 2024. MGTBench: Benchmarking                   Yafu Li, Zhilin Wang, Leyang Cui, Wei Bi, Shuming
  Machine-Generated Text Detection. In ACM SIGSAC                  Shi, and Yue Zhang. 2024b. Spotting AI’s touch:
  Conference on Computer and Communications Se-                    Identifying LLM-paraphrased spans in text. In Find-
  curity (CCS), New York, NY, USA. Association for                 ings of the Association for Computational Linguistics:
  Computing Machinery.                                             ACL 2024, pages 7088–7107, Bangkok, Thailand. As-
                                                                   sociation for Computational Linguistics.
Heng Ji. 2009. Cross-lingual predicate cluster acquisi-
  tion to improve bilingual event extraction by induc-           Maximilian Maurer. 2026. elfen: A python package
  tive learning. In Proceedings of the Workshop on                for efficient linguistic feature extraction for natural
  Unsupervised and Minimally Supervised Learning of               language datasets. In Proceedings of the 19th Con-
  Lexical Semantics, pages 27–35, Boulder, Colorado,              ference of the European Chapter of the Association
  USA. Association for Computational Linguistics.                 for Computational Linguistics (Volume 3: System
                                                                  Demonstrations), pages 61–74, Rabat, Marocco. As-
Jiazhou Ji, Ruizhe Li, Shujun Li, Jie Guo, Weidong Qiu,           sociation for Computational Linguistics.
   Zheng Huang, Chiyu Chen, Xiaoyu Jiang, and Xinru
   Lu. 2024. Detecting machine-generated texts: Not              Saif Mohammad. 2018a. Obtaining reliable human rat-
   just "ai vs humans" and explainability is complicated.          ings of valence, arousal, and dominance for 20,000
   Preprint, arXiv:2406.18259.                                     English words. In Proceedings of the 56th Annual
                                                                   Meeting of the Association for Computational Lin-
Yang Jiang, Jiangang Hao, Michael Fauss, and Chen Li.              guistics (Volume 1: Long Papers), pages 174–184,
  2024. Detecting chatgpt-generated essays in a large-             Melbourne, Australia. Association for Computational
  scale writing assessment: Is there a bias against non-           Linguistics.
  native english speakers? Computers & Education,
  217:105070.                                                    Saif Mohammad. 2018b. Word affect intensities. In
                                                                   Proceedings of the Eleventh International Confer-
Tanzila Kehkashan, Raja Adil Riaz, Ahmad Sami Al-                  ence on Language Resources and Evaluation (LREC
  Shamayleh, Adnan Akhunzada, Noman Ali, Muham-                    2018), Miyazaki, Japan. European Language Re-
  mad Hamza, and Faheem Akbar. 2025. Ai-generated                  sources Association (ELRA).


                                                            10
Alberto Muñoz-Ortiz, Carlos Gómez-Rodríguez, and              (ELI5), story generation (WritingPrompts, ROC-
  David Vilares. 2024. Contrasting linguistic patterns        Stories), commonsense reasoning (HellaSwag),
  in human and llm-generated news text. Artificial
                                                              knowledge illustration (SQuAD), and scientific
  Intelligence Review, 57.
                                                              writing (SciGen). The 7 model families (domains)
Chidimma Opara. 2024. StyloAI: Distinguishing AI-             are OpenAI (GPT-3.5-turbo, text-davinci-002/003),
  Generated Content with Stylometric Analysis", book-         LLaMA (7B, 13B, 30B, 65B), GLM-130B, FLAN-
  title="Artificial Intelligence in Education. Posters
                                                              T5 (small, base, large, xl, xxl), OPT (125M to 30B,
  and Late Breaking Results, Workshops and Tutori-
  als, Industry and Innovation Tracks, Practitioners,         including IML variants), BigScience (BLOOM-7B,
  Doctoral Consortium and Blue Sky. pages 105–114,            T0-3B, T0-11B), and EleutherAI (GPT-J-6B, GPT-
  Cham. Springer Nature Switzerland.                          NeoX-20B).
Alex Reinhart, Ben Markey, Michael Laudenbach,
                                                                 Machine-generated texts were created using
  Kachatad Pantusen, Ronald Yurko, Gordon Wein-               three prompt types: continuation prompts (first 30
  berg, and David West Brown. 2025. Do llms write             words of human text), topical prompts (based on ti-
  like humans? variation in grammatical and rhetori-          tles/topics), and specified prompts (topical prompts
  cal styles. Proceedings of the National Academy of
                                                              with source information). We only used continu-
  Sciences, 122(8):e2422455122.
                                                              ation prompts to avoid confounding effects from
Shashank Srivastava. 2025. Large language models              prompt variation. Table 6 shows the data distribu-
  threaten language’s epistemic and communicative             tion across text domains and splits.
  foundations. In Proceedings of the 2025 Conference
  on Empirical Methods in Natural Language Process-           CMV Dataset To assess prompt generalization,
  ing, pages 28650–28664, Suzhou, China. Association
  for Computational Linguistics.                              we conducted cross-dataset experiments using the
                                                              ChangeMyView (CMV) dataset from Dönmez and
Yuxia Wang, Jonibek Mansurov, Petar Ivanov, Jinyan            Falenska (2025), which employs direct response
  Su, Artem Shelmanov, Akim Tsvigun, Osama Mo-                prompts rather than continuation prompts. We eval-
  hammed Afzal, Tarek Mahmoud, Giovanni Puc-
  cetti, Thomas Arnold, Alham Aji, Nizar Habash,              uated: (1) training on MAGE-CMV and testing on
  Iryna Gurevych, and Preslav Nakov. 2024. M4GT-              their CMV dataset, and (2) training on their dataset
  bench: Evaluation benchmark for black-box machine-          and testing on MAGE-CMV. This tests whether
  generated text detection. In Proceedings of the 62nd        models can generalize across different prompting
  Annual Meeting of the Association for Computational
  Linguistics (Volume 1: Long Papers), pages 3964–
                                                              strategies for the same domain. Statistics of the
  3992, Bangkok, Thailand. Association for Computa-           final CMV dataset are in Table 7.
  tional Linguistics.
                                                              A.2    Classifier, Metrics, and Evaluation
Rowan Zellers, Ari Holtzman, Hannah Rashkin,
  Yonatan Bisk, Ali Farhadi, Franziska Roesner, and           We chose a linear Support Vector Machine (SVM)
  Yejin Choi. 2019. Defending against neural fake             for its effectiveness in high-dimensional feature
  news. In Advances in Neural Information Processing          spaces (284 features), computational efficiency for
  Systems, volume 32. Curran Associates, Inc.
                                                              training hundreds of classifiers across testbeds, and
Ye Zhang, Qian Leng, Mengran Zhu, Rui Ding, Yue               interpretability through feature coefficients.
  Wu, Jintong Song, and Yulu Gong. 2024. Enhancing
  text authenticity: A novel hybrid approach for ai-          Implementation We employed a linear Support
  generated text detection. In 2024 IEEE 4th Interna-         Vector Machine (SVM) using scikit-learn’s SVC
  tional Conference on Electronic Technology, Commu-          (v1.7.0 5 ) implementation with the following con-
  nication and Information (ICETCI), pages 433–438.
                                                              figuration: linear kernel, regularization parameter
                                                              (C = 1.0; default value), balanced class weighting
A     Methods
                                                              to handle class imbalance, random seed 42 for re-
A.1    Dataset Details                                        producibility. The training was accelerated using
MAGE Dataset We use the MAGE dataset (Li                      Intel Extension for Scikit-learn (sklearnex).
et al., 2024a), comprising human-written texts from              Features were standardized using z-score
10 text domains and corresponding AI-generated                normalization (zero mean, unit variance) via
continuations from 27 models across 7 model do-               StandardScaler, fitted on the training set and ap-
mains (families). The 10 text domains span diverse            plied to validation and test sets.
writing tasks: opinion statements (CMV, Yelp),                   5
                                                                  https://scikit-learn.org/stable/modules/
news articles (XSum, TLDR), question answering                generated/sklearn.svm.SVC.html


                                                         11
       Split         CMV                  Yelp                XSum                 TLDR                  ELI5
       Train   4,223H / 16,556AI   31,827H / 20,529AI   4,708H / 21,255AI    2,826H / 16,092AI    16,706H / 20,764AI
       Val     2,436H / 2,023AI     2,657H / 2,564AI    3,274H / 2,655AI      2,526H / 1,971AI     3,146H / 2,566AI
       Test     2,403H / 2,039AI    2,652H / 2,547AI    3,283H / 2,654AI      2,535H / 1,981AI     3,156H / 2,597AI
       Split          WP                 ROCT                 HSwag               SQuAD                 SciGen
       Train   6,356H / 20,005AI   3,287H / 20,712AI    3,129H / 20,295AI    15,820H / 19,940AI    4,436H / 18,691AI
       Val     3,133H / 2,481AI    3,284H / 2,583AI     3,288H / 2,521AI      2,524H / 2,475AI     2,531H / 2,312AI
       Test     3,099H / 2,538AI   3,275H / 2,588AI     3,292H / 2,535AI      2,508H / 2,496AI     2,538H / 2,251AI
               Overall Total: Train (93,318H / 194,839AI), Val (28,799H / 24,151AI), Test (28,741H / 24,226AI)

Table 6: MAGE dataset statistics using continuation prompts only. Training includes all available AI generations
from 27 models across 7 families (model domains); validation and test sets are approximately balanced (H = Human,
AI = AI-generated).


       Source     Number of Samples                              matplotlib 3.10.310 and seaborn 0.13.211 for visual-
       Human      157,880 comments (13,498 posts)                ization, spaCy 3.8.712 with model en_core_web_lg
       GPT        13,498 (1 comment per post)                    3.8.0, and ELFEN 1.1.913 for linguistic feature ex-
       LLaMA      13,489 (1 comment per post)                    traction. More details and required packages can
       Mistral    13,498 (1 comment per post)
                                                                 be found in the requirements file (requirements.txt)
Table 7: Final dataset sizes for the ChangeMyView
                                                                 on the repository. All experiments used consistent
(CMV) corpus used in training and evaluation.                    random seeds (seed=42) for train-test splits and
                                                                 model initialization.

Evaluation Metrics Model performance was as-                     A.3     Full List of Linguistic Features
sessed using three primary metrics—Macro F1-
score: Selected as the primary metric due to pos-                In the following, we provide an overview of the
sible class imbalance in test sets. Unlike micro-                full set of features used in our experiments. We
averaged metrics or accuracy, Macro F1 treats both               report features per feature area and rationales for
classes equally by averaging their individual F1                 the selection of features wherever we do not use all
scores, AUROC (Area Under ROC Curve): Mea-                       the available features.
sures the classifier’s ability to discriminate between
human and AI text across all possible decision                   A.3.1    Surface-level
thresholds, providing a threshold-independent eval-              We use the number of tokens, characters, sentences,
uation, Average Recall (AvgRec): The arithmetic                  lemmas, and words over 5 characters, and the raw
mean of recall scores for both classes, calculated as            sequence length in characters (including whites-
AvgRec = Recallhuman2+RecallAI . It ensures balanced             paces and special characters). We do not consider
evaluation regardless of class imbalance.                        all additional surface-level features, as we consider
   Accuracy was also reported for completeness.                  them theoretically equivalent to the ones we select.
Additional metrics included per-class precision, re-                We do not include the number of types (unique
call, and F1-scores for both human and AI classes.               tokens), as it is expected to carry similar informa-
                                                                 tion as the number of tokens and the number of
Reproducibility Resources All experiments
                                                                 lemmas. We do not include sentence-normalized
were conducted using Python 3.10.18 with the fol-
                                                                 measures, as all information is captured by the
lowing key dependencies: scikit-learn 1.7.06 for
                                                                 combination of the number of sentences and the
SVM implementation and evaluation metrics, In-
                                                                 respective measure to be sentence-normalized. We
tel Extension for Scikit-learn (sklearnex) 2025.9.07
                                                                 do not include the average word length, as similar
for accelerated training, pandas 2.3.08 for data ma-
                                                                 but more interpretable information is captured by
nipulation, numpy 2.2.69 for numerical operations,
                                                                 the number of long words.
   6
     https://scikit-learn.org
   7                                                               10
     https://uxlfoundation.github.io/                                 https://matplotlib.org
                                                                   11
scikit-learn-intelex/                                                 https://seaborn.pydata.org
   8                                                               12
     https://pandas.pydata.org                                        https://spacy.io
   9                                                               13
     https://numpy.org                                                https://github.com/mmmaurer/elfen


                                                            12
A.3.2   Parts-of-Speech                                        A.3.9    Syntactic Dependencies
We use the number of tokens per universal depen-               We use the number of universal dependency rela-
dencies POS tag (de Marneffe et al., 2021), and the            tions per relation type, and the dependency tree
POS variability (i.e., the number of different POS             width, tree depth, tree branching factor, the ramifi-
tags divided by the number of tokens).                         cation factor, and the number of noun chunks.

A.3.3   Readability                                            A.3.10    Emotion and Sentiment
We use the total number of syllables in a text, and            We use all emotion and sentiment features avail-
the Flesch reading ease (Kincaid et al., 1975) as              able in elfen. This includes the number of positive
measures of readability. We do not consider all                and negative sentiment tokens per text, the number
other readability features, as we consider them the-           of tokens with a high and a low valence, arousal,
oretically equivalent to the Flesch reading ease or            and dominance, the average valence, arousal, and
the number of syllables. More specifically, they               dominance, the average intensity, and the number
are all designed to measure the reading level, either          of high and low intensity tokens per Plutchik emo-
measured in school grade levels, age, or a more                tion.
abstract index of how easy to read a given text is.
                                                               A.3.11    Psycholinguistic
A.3.4   Lexical Richness
                                                               We use all available psycholinguistic features. This
We use the type-token ratio (TTR), the number                  includes the number of tokens with high and low
of global token hapax legomena (i.e., the number               concreteness, age of acquisition, prevalence, social-
of tokens per text that only occur once across the             ness, iconicity, and sensorimotor association, and
whole dataset), and the lexical density (i.e., the per-        the average rating across tokens per text for these
centage of adjectives, nouns, verbs, and adverbs per           dimensions, respecively.
text). We do not consider all other lexical richness
features, as we consider them theoretically equiv-             A.4     Testbeds
alent to at least one of the selected ones. More
                                                               We built on the settings designed by Li et al.
specifically, they all measure how many different
                                                               (2024a) and created a similar setup of eight pri-
kinds of words relative to the overall number of
                                                               mary testbeds to evaluate detection performance
words are present in a text. Our choice of TTR
                                                               across various generalization scenarios:
gives us a general measure, the global token hapax
legomena provides information about rare words,                TB1 (Fixed-domain & Model-specific) trained
and the lexical density about content words.                   and tested classifiers on individual domain-model
A.3.5   Information-theoretic                                  pairs, establishing baseline performance for 10
                                                               text domains and 27 AI models (270 classifiers).
We use both information-theoretic features, the                TB1-1 extended this setting by grouping models
compressibility and Shannon entropy of a text.                 into model families/domains (OpenAI, LLaMA,
A.3.6   Named Entities                                         GLM, Flan-T5, OPT, BigScience, Eleuther) to as-
                                                               sess model domain level of detection within fixed
We use the number of named entities per entity                 text domains and model variant vs. model fam-
type and the number of entities overall in a text.             ily/domain performance in fixed scenarios, result-
A.3.7   Semantic                                               ing in 70 classifiers.
We use the number of hedges in a text, the average             TB2 (Arbitrary-text-domains & Model-domain-
number of synsets overall and per nouns, verbs,                specific) trained on all text domains for each model
adjectives, and adverbs, and the number of tokens              family/domain separately (i.e., trained on all do-
with a high and with a low number of synsets over-             mains, but only using AI text generated by one
all and per nouns, verbs, adjectives, and adverbs,             model family; i.e., in one model domain).
respectively.
                                                               TB3 (Fixed-text-domain & Arbitrary-model-
A.3.8   Morphological                                          domains) evaluated cross-model generalization
We use all available universal dependencies mor-               within individual text domains by training on all
phological features that are not uniform in our data.          available models for each text domain separately.

                                                          13
TB4 (Arbitrary-text-domains & Arbitrary-model-             56.3% (OpenAI on SQuAD) to 98.6% (FLAN-T5
domains) represented our most comprehensive                on WritingPrompts).
training scenario, combining all available domains
and models to assess overall detection capability.          TB7: Per-domain analysis Table 11 presents
                                                            the performance across the four unseen domains
TB5 (Unseen model domains) evaluated a sce-                 generated by GPT-4. First, we evaluate the per-
nario of leave-one-out by leaving data generated by         formance on the combined text from the four text
a specific model family (model domain) out of the           domains, then we test on individual ones. The
training and then evaluated on the excluded model           combined evaluation represents the average perfor-
domain to assess the generalization.                        mance, but individual settings give more insight.
                                                            CNN/DailyMail news articles achieve the high-
TB6 (Unseen text domains) similarly assessed                est detection rate (96.82% F1), while DialogSum
text domain generalization by training on all text          proves most challenging (50.24% F1). PubMed
domains except one and testing on the excluded             (87.18% F1) and IMDb (83.10% F1) fall in be-
one.                                                        tween. These results align with the other OOD
TB7 (Unseen text-domains & Unseen-model)                    settings: News articles (CNN) show similar high
presented the most challenging scenario, testing on         performance to other news data (XSum), similar
completely unseen text domains (CNN/DailyMail,             -to an extent- behavior of the QAs (PubMed) and re-
DialogSum, IMDb, PubMed) generated by GPT-4,               view/opinion (IMDb) domains, but conversational
which was excluded from all training data. TB7-1            text (DialogSum) proves that such domain has
extended this analysis by evaluating each unseen            salient distinct linguistic features that cannot be
text domain individually to examine text domain-            detected easily from features fitted on other do-
specific performance variations.                            mains. We discuss further the results of unseen
                                                            domains in the following paragraph.
TB8 (Unseen text-model-domain Pairs) intro-
duced a novel cross-generalization setting where           TB8: Domain-model pair combinations Ta-
both the target text and model domain were com-            ble 12 presents all 70 text domain-model domain
pletely excluded from training, creating 70 unique         pair results in the wilder OOD setting. As a more
held-out combinations (10 domains × 7 families)            robust test setting to complement TB7 we find re-
to assess the classifier’s ability to generalize to        markable shifts in results across text and model
entirely novel domain-model pairings. This was             domains. Performance varies considerably (34.5%–
intended to validate more the scenario of TB7.             88.9% F1). OPT is most detectable across text
   We provide details of the configuration for each        domains (68.4% avg F1), while GLM and Eleuther
individual setting in Table 8.                             are least detectable (48.1% and 51.0% avg F1).
                                                           SciGen is the easiest text domain to detect across
B     Classification Results                               models (80.6% avg F1), while ROC-Stories and
                                                           SQuAD are most challenging (44.0% and 43.7%
B.1    Detailed MAGE Testbeds Results                      avg F1).
Complete results for all MAGE testbeds are pre-
sented in Table 9. Main findings are discussed in          B.2   ChangeMyView Cross-Dataset
section 4. Here we highlight more details of some                Experiments
testbeds.                                                  To assess the impact of different prompt formu-
                                                           lations, we run a small experiment on one of the
TB1.1: Fixed domain & model domain combi-                  datasets. For this, we choose and compare the per-
nations Table 10 presents results for 70 domain-           formance of the CMV subset in MAGE (in this
specific, model-domain-specific classifiers. OPT           section referred to as MAGE-CMV and CMV sub-
achieves the highest average detectability (94.4%          set from Dönmez et al. (2025) (in this subsection
F1), followed by Eleuther (92.4% F1) and FLAN-             referred to as CMV).
T5 (89.1% F1). OpenAI and GLM are least de-
tectable (71.6% and 74.9% F1). Across text do-             In-Distribution Performance The classifier
mains, WritingPrompts shows highest detection              achieves almost perfect performance on Change-
rates (93.9% avg F1), while Yelp is most challeng-         MyView (CMV) data in all in-distribution settings,
ing (73.7% avg F1). Performance ranges from                with Macro F1 scores exceeding 98.5%. Table 13

                                                      14
 TB#     Name                                                Training                 Testing                  # Classifiers
 TB1     Fixed-domain & Model-specific                       Single text domain +     Same text domain +           270
                                                             Single model             Same model
 TB1-1   Fixed-text-domain & Model-domain-specific           Single text domain +     Same domain + Same            70
                                                             Model domain             model domain
 TB2     Arbitrary-text-domains & Model-domain-specific      All text domains +       All text domains +            7
                                                             Model domain             Same model domain
 TB3     Fixed-text-domain & Arbitrary-model-domains         Single text domain +     Same text domain +            10
                                                             All models               All models
 TB4     Arbitrary-text-domains & Arbitrary-model-domains    All text domains + All   All text domains + All        1
                                                             models                   models
 TB5     Unseen model domains                                All text domains + 6     All domains + 1               7
                                                             model domains            held-out model
                                                                                      domain
 TB6     Unseen text domains                                 9 text domains + All     1 held-out text domain        10
                                                             models                   + All models
 TB7     Unseen-text & -model domains                        All text domains + All   4 new text domains +          1
                                                             models                   GPT-4
 TB7-1   Unseen-text-domain & Unseen-model                   All text domains + All   1 of 4 new text               4
                                                             models                   domains + GPT-4
 TB8     Unseen text-model-domain pairs                      9 text domains + 6       1 held-out text domain        70
                                                             model domains            + 1 held-out model
                                                                                      domain

Table 8: Overview of experimental testbeds for AI-generated text detection. Each testbed evaluates different
generalization scenarios, ranging from fixed conditions (TB1) to completely unseen domain-model combinations
(TB7, TB8).


shows the detailed results.                                         Scenario 2: MAGE-CMV → CMV. The pat-
                                                                 tern is even more pronounced in the reverse direc-
Cross-Dataset Generalization We evaluate two                     tion. Training on all 27 models across 7 model
cross-dataset scenarios: (i) training on our CMV                 domains from MAGE-CMV yields poor perfor-
dataset and testing on MAGE-CMV, and (ii) train-                 mance on CMV test set (Macro F1: 43.53%, AI-
ing on MAGE-CMV and testing on our CMV                           Recall: 23.37%). Focusing only on shared model
dataset. Both scenarios reveal a critical finding:               domains (OpenAI and LLaMA) dramatically im-
model domain alignment between training and                      proves results to 84.95% Macro F1 and 92.44%
test data dramatically impacts detection perfor-                 AI-Recall—nearly doubling the F1 score and qua-
mance, while prompt formulation appears to                       drupling the AI-Recall. Table 15 shows the com-
have a smaller effect.                                           plete results.
   Scenario 1: CMV → MAGE-CMV. When                                 Key Findings: Cross-dataset detection succeeds
testing on MAGE-CMV using all available model                    when model domains align between training and
domains, performance drops significantly (Macro                  test distributions. Training on diverse model do-
F1: 76.11%, AI-Recall: 56.99%). However, when                    mains without representation in the test set intro-
we restrict both training and test data to only the              duces noise that severely degrades performance.
shared model domains (OpenAI and LLaMA), per-                    The less severe drops compared to the in-domain
formance improves substantially to 86.93% Macro                  performance for the shared model domains indicate
F1 and 81.93% AI-Recall. This indicates that in-                 that, while having an impact, the prompt formula-
cluding Mistral in training and other model do-                  tion seems to have less of an impact on detectability
mains (5 additional domains) in testing introduces               than other factors.
a distribution mismatch that harms detection (as
                                                                 C    Ablation Results
we can see in Table 14). This could still be caused
by the prompt strategies, which leads us to reverse              In this section, we discuss further the ablation stud-
the setting and analyze the results.                             ies conducted on all testbeds (ablation study A)

                                                            15
 Setting                                                                Method                   Acc      AUROC     F1-Macro
                                            In-distribution Detection
 1. Fixed-Domain & Model (270 classifiers)                              SVM w/ Ling. Feats.   0.9424      0.9865     0.7880
 1.1. Fixed-Domain & Model-domain (70 classifiers)                      SVM w/ Ling. Feats.   0.9234      0.9839     0.8403
 2. Arbitrary-Domains & Fixed-Model (7 classifiers)                     SVM w/ Ling. Feats.   0.8443      0.9856     0.7347
 3. Fixed-Domain & Arbitrary-Models (10 classifiers)                    SVM w/ Ling. Feats.   0.9056      0.9860     0.9044
 4. Arbitrary-Domains & Arbitrary-Models (1 classifier)                 SVM w/ Ling. Feats.   0.8277      0.9682     0.8267
                                          Out-of-distribution Detection
 5. Unseen Models (7 classifiers)                                       SVM w/ Ling. Feats.   0.7291      0.9521     0.6094
 6. Unseen Domains (10 classifiers)                                     SVM w/ Ling. Feats.   0.7995      0.9625     0.7936
 7. Unseen Domains & Unseen Model (1 classifier)                        SVM w/ Ling. Feats.   0.8223      0.9066     0.8084
 7.1. Unseen Domains & Unseen Model (per domain) (4 classifiers)        SVM w/ Ling. Feats.   0.8127      0.9422     0.7934
 8. Unseen Domain-Model Pairs (70 classifiers)                          SVM w/ Ling. Feats.   0.6864      0.9450     0.5875

Table 9: Summary results for all testbeds (TB1-8). For testbeds with multiple classifiers, metrics represent the mean
performance averaged across all individual classifiers within that testbed. Results are grouped into in-distribution
(TB1-4) and out-of-distribution (TB5-8) detection scenarios.

       Model domain     CMV     ELI5    HSwag     ROCT     SciGen       SQuAD    TLDR    WP       XSum     Yelp    Avg.
       BigScience       0.844   0.750     0.784    0.828    0.867       0.701    0.759   0.949    0.893    0.753   0.813
       Eleuther         0.935   0.934     0.870    0.959    0.945       0.956    0.871   0.971    0.951    0.851   0.924
       FLAN-T5          0.926   0.901     0.819    0.835    0.951       0.855    0.881   0.986    0.967    0.793   0.891
       GLM              0.856   0.683     0.836    0.817    0.708       0.692    0.642   0.914    0.758    0.586   0.749
       LLaMA            0.891   0.798     0.945    0.986    0.783       0.789    0.888   0.935    0.812    0.708   0.854
       OpenAI           0.742   0.632     0.919    0.733    0.742       0.563    0.656   0.839    0.725    0.608   0.716
       OPT              0.960   0.911     0.951    0.964    0.967       0.936    0.945   0.978    0.966    0.858   0.944
       Avg.             0.879   0.801     0.875    0.875    0.852       0.785    0.806   0.939    0.867    0.737   0.842

Table 10: TB1.1 results: F1-Macro performance for fixed domain and model domain combinations (70 classifiers
total). Each cell represents a separate classifier trained and tested on data from one domain and one model domain.
Row averages show model domain detectability; column averages show domain-specific performance.


      Dataset       Accuracy    AUROC        F1 Macro             domain-specific data (TB2 ID, TB5 OOD), lexical
      CNN             0.9717     0.9973       0.9682              richness consistently dominates across all model
      DialogSum       0.5191     0.8206       0.5024              domains. However, impact magnitude varies sub-
      IMDb            0.8650     0.9679       0.8310              stantially: removing lexical richness hurts FLAN-
      PubMed          0.8950     0.9828       0.8718              T5 most severely (-9.5% TB2, -14.1% TB5), while
      ALL FOUR        0.8223     0.9066       0.8084              OpenAI models show minimal dependency (+0.3%
                                                                  TB2, -13.3% TB5). This suggests OpenAI gener-
Table 11: Results for TB7: unseen-domains and unseen-             ations rely less on distinctive vocabulary patterns,
models, using the full set of features. The unseen model
                                                                  making them harder to detect through lexical fea-
is GPT-4
                                                                  tures alone. Surface features show consistent small
                                                                  negative effects (-0.4% to -1.4%), while most other
and on domain-agnostic settings (ablation study B                 features have negligible impact.
-cumulative).
                                                                  Text Domain Effects (TB3 & TB6) Domain-
C.1    Model and Text Domain Effects                              specific patterns (TB3 ID, TB6 OOD) reveal
       Additional Analysis                                        greater variation than model effects. Figure 8 illus-
                                                                  trates these differences through performance distri-
Table 16 presents complete ablation results for
                                                                  butions across feature ablations. In TB3 (ID, base-
testbeds 2, 3, 5, and 6, examining feature impor-
                                                                  line 0.904), lexical richness shows the largest drop
tance across model domains and text domains. Fig-
                                                                  (median 0.85) but with tight distribution, while
ures 7 and 8 visualize these patterns.
                                                                  other features remain close to baseline with mini-
Model domain Effects (TB2 & TB5) When                             mal variance. This indicates consistent, predictable
training on arbitrary text domains with model-                    behavior when text domains are seen during train-

                                                             16
 Model domain        CMV     ELI5       HSwag       ROCT    SciGen       SQuAD        TLDR      WP         XSum     Yelp      Avg.
 BigScience          0.642   0.557       0.530      0.433    0.821       0.411        0.456     0.684      0.704   0.517      0.576
 Eleuther            0.585   0.505       0.443      0.370    0.719       0.349        0.399     0.608      0.636   0.492      0.510
 FLAN-T5             0.669   0.644       0.600      0.544    0.867       0.487        0.507     0.724      0.739   0.589      0.637
 GLM                 0.551   0.474       0.420      0.353    0.685       0.345        0.381     0.566      0.583   0.449      0.481
 LLaMA               0.725   0.633       0.487      0.446    0.813       0.471        0.507     0.820      0.790   0.586      0.628
 OpenAI              0.706   0.584       0.518      0.450    0.851       0.467        0.500     0.636      0.683   0.575      0.597
 OPT                 0.790   0.704       0.559      0.484    0.889       0.528        0.563     0.795      0.833   0.691      0.684
 Avg.                0.667   0.586       0.508      0.440    0.806       0.437        0.473     0.691      0.710   0.557      0.587

Table 12: Results of TB8; Macro F1 performance on unseen domain-model-domain pairs. Training data excludes
both the target domain and target model domain, creating 70 unique domain-model combinations. Each cell shows
the F1-Macro score when testing on a domain-model pair that was completely excluded from training. The Avg
row shows the average performance across all text domains for each model domain, while the Avg column shows
the average performance across all model domains for each domain. Overall statistics: Mean = 0.587, Std = 0.140,
Range = [0.345, 0.889].

                 openai          llama             glm       flan_t5            opt           bigscience           eleuther
   0.7

   0.6

   0.5

   0.4    Surface Lexi. Rich. Emotion     Psych.     Readab. Morpho.      POS         Depend. Semant. Entities        Inform.
Figure 7: Visualization of results of ablation study on TB5 (unseen models). The horizontal dashed lines indicate
the original baseline results for each model, and the bars indicate the results of dropping the corresponding feature
area.


       AI Text        Accuracy    AUROC          F1 Macro          ior changes across different domains in the OOD
       AI-combined     0.9884        0.9973        0.9884          setting compared to ID. Psycholinguistic features
       GPT             0.9911        0.9994        0.9911          help formal domains when unseen (CMV +1.1%,
       Llama           0.9852        0.9948        0.9852          XSum +1.1%, SciGen +0.5%) but hurt creative
       Mistral         0.9920        0.9986        0.9920          writing (WP -3.7%, ROC -3.7%). Information fea-
                                                                   tures consistently hurt OOD performance across
Table 13: Results for CMV dataset for the different
                                                                   most domains (-4.4% to -5.1%), suggesting they
settings using the complete features set (284 features).
The use of accuracy here is due to the balanced dataset            capture domain-specific patterns that don’t general-
                                                                   ize. Both psycholinguistic and information features
                                                                   display wider distributions in TB6, with outliers in
                                                                   both directions indicating divergent effects
ing.
   TB6 (OOD, baseline 0.794) shows increased                       C.2    Zoom-in TB7: Unseen Domains and
variance across nearly all features. Lexical richness                     Unseen Model
maintains strong impact (median 0.66) but with                     For the setting of completely unseen text and model
much wider spread, reflecting domain-dependent                     domains, we tested two configurations: combining
sensitivity: XSum shows massive drops in OOD                       all four unseen domains (CNN, PubMed, IMDb,
(-27.4%), while SQuAD remains stable (-0.3%                        DialogSum) into a single test set, and testing each
ID, -0.3% OOD). Surface features shift upward                      domain separately.
in TB6, often exceeding baseline for some text
domains (XSum +1.5%, WP +3.5%), contrasting                        Combined Unseen Domains With all four do-
with their negative effects in TB3. However, their                 mains combined (as seen in Table 5 in sec. 4.2),
large variance (Figure 8b) proves how their behav-                 lexical richness removal causes the sharpest drop

                                                              17
 Mage Test data      Accuracy    AUROC      F1 Macro     AI-Recall     CMV-Training size     MAGE-CMV-test size
 i- All models        0.7765      0.7635     0.7611       0.5699      28,339 H, 28,340 AI     2,403H, 2,039 AI
 ii-OpenAI-Llama      0.9191      0.9410     0.8693       0.8109      18,890 H, 18,891 AI      2,403 H, 550 AI

Table 14: Results of two settings for cross-CMV-MAGE setup: (i) classifier is trained on training split from
ChangeMyView dataset with all AI-texts (GPT, LLaMA, & Mistral) and tested on MAGE-CMV data with AI-texts
from all 27 models. (ii) classifier trained on training split from ChangeMyView but with AI-texts from only GPT &
LLaMA, then tested on MAGE-CMV with AI-texts from OpenAI & LLaMA models.

 Mage Test data      Accuracy   AUROC      F1 Macro    AI-Recall     MAGE-CMV-Training size      CMV-test size
 i- All models        0.4657     0.5355     0.4353       0.2337         4,223 H, 16,556 AI      8,097 H, 8,097 AI
 ii-OpenAI-Llama      0.8503     0.9163     0.8495       0.9244          4,223 H, 4,429 AI      5,398 H, 5,397 AI

Table 15: Results of two settings for cross-CMV-MAGE setup: (i) classifier is trained on training split from
MAGE-CMV data with AI-texts from all 27 models and tested on ChangeMyView dataset with all AI-texts (GPT,
LLaMA, & Mistral). (ii) classifier trained on training split from MAGE-CMV with AI-texts from OpenAI &
LLaMA models, then tested on ChangeMyView but with AI-texts from only GPT & LLaMA.


(from 80.84% to 53.12%), consistent with our                  lenging text domain (baseline using all features:
earlier findings. However, an intriguing pattern              50.24%). It shows unique behavior. Removing
emerges: removing morphological, psycholinguis-               morphological and information features improves
tic, and information features actually improves per-          F1 by 13.47%, and 5.10% respectively. Conversely,
formance by up to 3.5%. This suggests these fea-              removing semantic features hurts performance (-
tures capture domain-specific patterns that hurt gen-         2.86%). Conversational text appears fundamentally
eralization when both text and model domains are              different: its informal, fragmented nature means
unseen. So, we conducted a more analysis and eval-            traditional linguistic features actively mislead the
uation across these four new text domains, which              classifier.
we discuss next.
                                                              Connection to TB6 and Domain Categories
Separate Unseen Domains Testing each unseen                   These patterns align with TB6 results and reveal a
domain individually (Figure 9) reveals dramatic               clear hierarchy by domain category:
variation in feature dependencies.                                News domains (XSum, CNN) show the
   CNN (News) is extremely lexical-richness de-               strongest lexical richness dependency and bene-
pendent. In other words, removing it drops F1 from            fit from removing most other features. Their for-
96.82% to 48.47%, a massive 48% collapse. Nearly              mal, structured writing makes vocabulary patterns
all other features improve performance when re-               paramount.
moved, suggesting CNN’s formal news writing                       Review domains (Yelp, IMDb) also depend
style makes lexical patterns the only reliable signal.        heavily on lexical richness but show mixed results
   IMDb (Reviews) has, similar to CNN, massive                with emotion and morphological features. Human
lexical richness dependency (-41.88%), but also               reviews have distinctive emotional patterns that
benefits from removing psycholinguistic features              sometimes help in-domain (TB 3) but hurt general-
(+5.93%) and morphological features (+2.38%).                 ization (Testbeds 6 and 7).
Opinion writing seems to have distinctive emo-                    Q&A domains (ELI5, SQuAD, PubMed)
tional/morphological patterns that don’t generalize.          vary widely. Explanatory Q&A (ELI5, PubMed)
   PubMed (Scientific Q&A) shows, while not as                shows moderate lexical dependency and benefits
much as CNN or IMDb, strong lexical richness                  from psycholinguistic features, while factual Q&A
dependency (-23.56%) but benefits from removing               (SQuAD) shows minimal lexical dependency and
surface features (+3.87%) and information features            struggles with most feature types.
(+2.79%). The scientific Q&As domain appears to                   Story domains (WP, ROCT) show moderate
have unique surface-level patterns that mislead the           lexical dependency but are highly sensitive to sur-
classifier.                                                   face and morphological features when unseen, sug-
   DialogSum (Conversation) is the most chal-                 gesting creative writing has unique structural pat-

                                                         18
                                                                          0.9
0.9
                                                                          0.8
0.8                                                                       0.7
                                                                          0.6
                                                 Baseline (0.904)                                                      Baseline (0.794)
0.7                                                                       0.5
 ace      ich.    tion  Psyc h.   POS    Sem end.                           ace    ich.    tion  Psyc h.   POS   Sem end.
                       Read ab.               ant.                                              Read ab.              ant.
Surf   Lexi      Emo   Morp               Enti
                                        Dep    ties                       Surf  Lexi      Emo   Morp          Dep
                                                                                                                  Enti ties
            .R              ho.           Infor m.                                   .R              ho.          Infor m.

(a) Visualization of results distribution of ablation study on            (b) Visualization of results distribution of ablation study on
TB3 (domain-fixed—arbitrary-model-domains) across the 11                  TB6 (unseen domains) across the 11 feature areas.
feature areas.

Figure 8: Distribution of F1-Macro scores across feature area ablations for in-distribution (TB3) and out-of-
distribution (TB6) testbeds focusing on text domains.


                                                                          classifiers) is computationally prohibitive. We se-
 0.8                                                                      lected 16 representative pairs based on sensitivity
 0.6                                                                      analysis.
 0.4                                                                      Selection Methodology We measured how much
                         cnn   pubmed         imdb       dialogsum
 0.2                                                                      feature ablation effects vary (standard deviation)
   Su  r
Lex face
    i. R
  Em ch. i
       oti
     Psy
  Re h.
      ad
  Mo b.rphc
          aon
            o.                                                            in ID versus OOD scenarios (Figure 12). Text and
  De S   PO
      pe
  Se d.
      ma
   En t.  n
       titi
   Inf sormne .                                                           model domains with larger changes in standard
                                                                          deviation show more unpredictable behavior when
Figure 9: Visualization of results of ablation study                      unseen (Figure 10).
on TB7 using separate unseen domains (cnn, pubmed,
imdb, & dialogsum) and one unseen model (gpt4). The                       Selected 4 text domains: XSum (highest sensi-
horizontal dashed lines indicate the original baseline                    tivity when unseen), WritingPrompts (high sensitiv-
results for each domain, and the bars indicate the results                ity increase), TLDR (stable behavior), and SQuAD
of dropping the corresponding feature area.
                                                                          (lowest sensitivity).
                                                                          Selected 4 model domains: OpenAI (hardest to
terns.
                                                                          detect), LLaMA (highest sensitivity increase), Big-
   Conversational domain (DialogSum) is the out-
                                                                          Science (stable behavior), and EleutherAI (easiest
lier; morphological and information features ac-
                                                                          to detect)
tively hurt performance, while semantic features
                                                                             This yields 16 pairs covering the full spec-
become critical. This suggests conversational AI
                                                                          trum from stable (SQuAD-EleutherAI) to volatile
detection requires fundamentally different feature
                                                                          (XSum-LLaMA).
sets.
   This domain-level analysis motivates our se-                           Results Figure 11 shows lexical richness remains
lection strategy for TB8 (see next section C.3):                          the dominant feature across all 16 pairs, with me-
we need pairs that capture this variation, from                           dian drops around -0.12. However, Figure 13
highly lexical-dependent formal domains (XSum)                            (heatmap showing effects exceeding ±2%) and Fig-
to feature-sensitive conversational domains (rep-                         ure 14 (feature area patterns) reveal distinct cluster-
resented by SQuAD’s unusual behavior) to stable                           ing by text domain category, consistent with TB6
domains (TLDR). Combined with model domain                                and TB7 patterns.
variation, this ensures our 16 selected pairs compre-                        News (XSum) pairs show extreme lexical rich-
hensively represent the feature dependency land-                          ness dependency across all model domains (-17.3%
scape.                                                                    to -32.4%), with LLaMA showing the strongest
                                                                          dependency (-32.4%). This mirrors CNN’s be-
C.3       TB8 Ablation: Selection of                                      havior in TB7 where removing lexical richness
          Domain-Model Pairs                                              caused 48% performance collapse. Surface (+2.3%
Running ablation on all TB8 combinations (10 text                         to +4.4%), morphological (+1.2% to +3.7%), and
domains × 7 model domains × 11 features = 770                             dependency (+3.1% to +4.0%) features consistently

                                                                     19
 Domain       Baseline     Surface      Lexi.Rich.      Emotion         Psych.         Readab.       Morpho.          POS          Depend.         Semant.        Entities       Inform.
                                                                                        Testbed 2
 OpenAI        .555      .551 (-.005)   .558 (+.003)   .554 (-.002)   .549 (-.007)   .553 (-.002)   .554 (-.001)   .556 (+.001)   .549 (-.006)   .556 (+.000)   .556 (+.001)   .552 (-.003)
 LLaMA         .753      .752 (-.001)   .775 (+.022)   .758 (+.005)   .755 (+.002)   .755 (+.002)   .750 (-.003)   .758 (+.005)   .751 (-.002)   .757 (+.003)   .756 (+.003)   .755 (+.002)
 GLM           .618      .612 (-.006)   .643 (+.025)   .617 (-.001)   .614 (-.004)   .613 (-.005)   .615 (-.003)   .615 (-.003)   .615 (-.003)   .617 (-.001)   .618 (-.000)   .616 (-.002)
 FLAN-T5       .766      .752 (-.014)   .671 (-.095)   .765 (-.001)   .761 (-.004)   .765 (-.001)   .757 (-.009)   .765 (-.001)   .762 (-.004)   .764 (-.001)   .764 (-.001)   .763 (-.003)
 OPT           .913      .906 (-.007)   .881 (-.032)   .913 (-.000)   .910 (-.003)   .913 (-.000)   .910 (-.003)   .912 (-.002)   .909 (-.004)   .913 (-.000)   .914 (+.000)   .909 (-.004)
 BigScience    .656      .646 (-.010)   .599 (-.057)   .654 (-.002)   .647 (-.009)   .657 (+.000)   .634 (-.022)   .651 (-.005)   .650 (-.006)   .654 (-.002)   .655 (-.001)   .649 (-.007)
 Eleuther      .881      .876 (-.005)   .857 (-.024)   .882 (+.001)   .878 (-.003)   .881 (+.000)   .870 (-.011)   .877 (-.004)   .876 (-.005)   .880 (-.001)   .881 (-.000)   .879 (-.002)
                                                                                        Testbed 5
 OpenAI        .616      .609 (-.008)   .483 (-.133)   .613 (-.003)   .607 (-.009)   .616 (-.000)   .612 (-.005)   .613 (-.003)   .609 (-.007)   .614 (-.002)   .616 (+.000)   .595 (-.021)
 LLaMA         .644      .642 (-.001)   .469 (-.174)   .641 (-.002)   .637 (-.006)   .644 (+.000)   .638 (-.006)   .637 (-.006)   .634 (-.009)   .642 (-.002)   .643 (-.000)   .620 (-.024)
 GLM           .496      .491 (-.005)   .458 (-.038)   .493 (-.002)   .491 (-.004)   .496 (+.000)   .493 (-.003)   .492 (-.004)   .491 (-.004)   .494 (-.002)   .496 (+.000)   .480 (-.015)
 FLAN-T5       .673      .666 (-.007)   .533 (-.141)   .671 (-.002)   .669 (-.004)   .673 (+.000)   .670 (-.004)   .669 (-.004)   .667 (-.006)   .672 (-.001)   .674 (+.001)   .647 (-.026)
 OPT           .714      .710 (-.004)   .583 (-.131)   .712 (-.002)   .710 (-.004)   .715 (+.000)   .711 (-.003)   .710 (-.004)   .711 (-.003)   .714 (-.001)   .715 (+.001)   .698 (-.016)
 BigScience    .595      .590 (-.005)   .536 (-.059)   .593 (-.002)   .589 (-.006)   .595 (+.000)   .594 (-.001)   .592 (-.003)   .591 (-.004)   .593 (-.002)   .596 (+.001)   .575 (-.020)
 Eleuther      .528      .523 (-.005)   .498 (-.029)   .525 (-.003)   .523 (-.005)   .528 (-.000)   .525 (-.003)   .524 (-.004)   .522 (-.006)   .526 (-.002)   .528 (+.000)   .510 (-.018)
                                                                                        Testbed 3
 CMV           .924      .918 (-.006)   .843 (-.081)   .920 (-.003)   .916 (-.008)   .923 (-.001)   .891 (-.032)   .916 (-.008)   .922 (-.002)   .922 (-.002)   .922 (-.002)   .912 (-.012)
 Yelp          .804      .800 (-.005)   .728 (-.076)   .788 (-.016)   .796 (-.008)   .803 (-.001)   .794 (-.010)   .804 (-.001)   .773 (-.031)   .804 (+.000)   .800 (-.004)   .792 (-.012)
 XSum          .941      .938 (-.003)   .836 (-.106)   .938 (-.003)   .940 (-.001)   .941 (-.001)   .941 (-.000)   .934 (-.007)   .943 (+.002)   .922 (-.019)   .941 (-.001)   .931 (-.010)
 TLDR          .908      .907 (-.001)   .824 (-.084)   .855 (-.053)   .915 (+.007)   .909 (+.001)   .899 (-.009)   .906 (-.002)   .865 (-.044)   .909 (+.000)   .912 (+.004)   .909 (+.000)
 ELI5          .873      .864 (-.009)   .755 (-.118)   .870 (-.003)   .836 (-.037)   .873 (-.000)   .864 (-.009)   .868 (-.005)   .858 (-.015)   .873 (+.000)   .872 (-.001)   .852 (-.021)
 WP            .964      .960 (-.005)   .912 (-.052)   .964 (-.000)   .961 (-.003)   .963 (-.002)   .962 (-.003)   .954 (-.010)   .961 (-.004)   .965 (+.001)   .964 (-.001)   .949 (-.015)
 ROCT          .928      .927 (-.000)   .868 (-.060)   .931 (+.003)   .891 (-.037)   .927 (-.001)   .913 (-.015)   .930 (+.002)   .927 (-.001)   .927 (-.000)   .925 (-.002)   .931 (+.003)
 HSwag         .953      .955 (+.002)   .928 (-.025)   .957 (+.004)   .947 (-.006)   .934 (-.018)   .951 (-.002)   .953 (+.000)   .952 (-.001)   .954 (+.001)   .953 (+.000)   .947 (-.006)
 SQuAD         .829      .795 (-.034)   .831 (+.002)   .810 (-.019)   .819 (-.010)   .830 (+.001)   .829 (-.001)   .816 (-.014)   .827 (-.002)   .828 (-.001)   .827 (-.002)   .827 (-.002)
 SciGen        .920      .917 (-.003)   .838 (-.081)   .916 (-.003)   .918 (-.001)   .911 (-.008)   .919 (-.000)   .908 (-.011)   .916 (-.003)   .919 (-.000)   .919 (-.000)   .908 (-.011)
                                                                                        Testbed 6
 CMV           .866      .868 (+.002)   .739 (-.127)   .863 (-.004)   .877 (+.011)   .870 (+.003)   .845 (-.021)   .856 (-.010)   .868 (+.001)   .859 (-.007)   .868 (+.002)   .823 (-.044)
 Yelp          .777      .775 (-.001)   .660 (-.116)   .766 (-.010)   .794 (+.017)   .776 (-.000)   .778 (+.002)   .764 (-.013)   .764 (-.013)   .772 (-.004)   .775 (-.001)   .740 (-.036)
 XSum          .897      .913 (+.015)   .623 (-.274)   .892 (-.005)   .909 (+.011)   .900 (+.002)   .915 (+.018)   .887 (-.010)   .912 (+.015)   .897 (-.000)   .889 (-.008)   .852 (-.046)
 TLDR          .704      .678 (-.026)   .617 (-.087)   .711 (+.007)   .688 (-.016)   .707 (+.004)   .703 (-.000)   .704 (+.001)   .691 (-.013)   .704 (+.000)   .713 (+.010)   .712 (+.008)
 ELI5          .807      .787 (-.020)   .694 (-.113)   .805 (-.002)   .823 (+.015)   .805 (-.003)   .810 (+.003)   .793 (-.014)   .756 (-.051)   .805 (-.002)   .805 (-.002)   .765 (-.042)
 WP            .883      .919 (+.035)   .676 (-.207)   .876 (-.008)   .846 (-.037)   .877 (-.006)   .887 (+.004)   .884 (+.000)   .870 (-.013)   .883 (-.001)   .888 (+.005)   .866 (-.017)
 ROCT          .668      .680 (+.012)   .541 (-.128)   .683 (+.015)   .696 (+.028)   .662 (-.006)   .687 (+.019)   .682 (+.014)   .680 (+.012)   .668 (-.000)   .649 (-.020)   .704 (+.036)
 HSwag         .739      .738 (-.001)   .574 (-.165)   .730 (-.009)   .738 (-.001)   .742 (+.003)   .735 (-.004)   .742 (+.003)   .765 (+.026)   .744 (+.005)   .747 (+.008)   .688 (-.051)
 SQuAD         .667      .643 (-.023)   .664 (-.003)   .664 (-.002)   .641 (-.025)   .663 (-.004)   .660 (-.007)   .655 (-.012)   .653 (-.013)   .672 (+.005)   .665 (-.001)   .663 (-.004)
 SciGen        .927      .925 (-.002)   .725 (-.203)   .923 (-.004)   .932 (+.005)   .927 (-.001)   .930 (+.002)   .920 (-.007)   .927 (-.000)   .923 (-.004)   .928 (+.000)   .914 (-.013)


Table 16: Complete results of the ablation study (A) where we drop a feature group at each training cycle for four
different testbeds (TB2, TB3, TB5, & TB6) and the difference to baseline where the classifier is trained on the
full set of features (284). The values in red indicate a decrease in performance, while green values indicate an
improvement compared to the baseline result.


improve performance when removed across all                                                      shows reversed effects: beneficial to remove for
models, indicating formal news writing relies al-                                                SQuAD-BigScience/Eleuther (+4.6% to +5.2%)
most exclusively on vocabulary patterns.                                                         but harmful for SQuAD-LLaMA (-4.8%). This
   Creative writing (WP) pairs display strong lex-                                               dramatic model domain difference suggests Big-
ical dependency (-11.3% to -23.0%), with LLaMA                                                   Science and Eleuther generate factual Q&A with
again showing the strongest effect (-23.0%). Sur-                                                less distinctive vocabulary, while LLaMA main-
face features provide the largest benefit when re-                                               tains lexical patterns useful for detection. All
moved (+5.8% to +7.1%), consistent across all                                                    SQuAD pairs require balanced contributions from
models. Psycholinguistic features consistently hurt                                              surface (-2.0% to -2.9%), psycholinguistic (-2.3%
performance (-4.7% to -5.7%), mirroring IMDb                                                     to -2.7%), and dependency (-1.2% to -1.8%) fea-
patterns in TB7 where emotional features mislead                                                 tures. The consistency of these requirements across
in OOD settings. Dependency features show simi-                                                  models, despite varying lexical dependencies, con-
lar effect.                                                                                      firms SQuAD’s behavior observed in TB6 and re-
   News summary (TLDR) pairs show moderate                                                       inforces that factual Q&A requires fundamentally
but variable lexical dependency, with strong model                                               different detection strategies.
domain effects: minimal for TLDR-Eleuther (-                                                        Model domain patterns emerge clearly where
0.4%) but substantial for TLDR-LLaMA (-13.2%).                                                   LLaMA consistently shows the strongest lexical
Unlike other text domains, TLDR uniquely benefits                                                richness dependency across all text domains (-4.8%
from entities (+0.6% to +1.4%) and information                                                   to -32.4%), while OpenAI and BigScience show
features (+0.1% to +1.0%), with BigScience and                                                   more text-domain-specific variation. Eleuther dis-
Eleuther showing the strongest gains.                                                            plays unique behavior with SQuAD (benefits from
   Q&A (SQuAD) pairs exhibit the most distinc-                                                   removing lexical richness) but strong dependency
tive and model-dependent pattern. Lexical richness                                               elsewhere, suggesting its factual generation differs

                                                                                          20
             0.06   0.053                                                                            0.05     0.045
                            0.049
                                    0.043                                                            0.04              0.036
             0.04                           0.037
                                                                                                     0.03                        0.029
                                                    0.024
             0.02                                           0.015 0.014                              0.02
                                                                                                                                         0.014
                                                                          0.002                      0.01
             0.00                                                                 -0.002 -0.002                                                  0.002 0.002 0.001
                                                                                                     0.00
                          m                                             5                               llama                                      g
              xsu    hs  wp
                        wa
                    sci g
                       _ge                                           ua
                                                                    eli
                                                                     tlddr                            op  en ai                              ele lm
                                                                                                                                                u
                        roc
                        cm
                        ye
                            n
                            t
                            v                                             sq                          fla top
                                                                                                          n_t 5                            big ther
                                                                                                                                              sci
                           lp                                                                                                                     en ce

Figure 10: Change in standard deviation between unseen (TB5 & TB6) and fixed (TB2 & TB3) scenarios for text
domains (left) and model domains (right). Red bars indicate increased sensitivity when unseen, green bars indicate
decreased sensitivity. Higher absolute values represent larger shifts in model behavior across different experimental
setups.


                                                                                                                    Lexrfa  ce
                                                                                                                         i. R                                        .
                                                                                                                    Em h.
                                                                                                                        oti  onic                              pe          nt.     es
                                                                                                                    Psy
                                                                                                                    Re ad
                                                                                                                    Mo .
                                                                                                                         ch  .
                                                                                                                            ab                                   nd    ma    titiorm .
                                                                                                                Su  PO .
                                                                                                                       Srph   o                              De       Se    En    Inf
                                                                                           squad_bigscience -0.020 0.052            -0.025
 0.05                                                                                        squad_eleuther             0.046       -0.024
 0.00
 0.05                                                                                             squad_llama -0.024 -0.048         -0.027
 0.10                                                                                           squad_openai -0.029                 -0.027
 0.15                                                                                         tldr_bigscience -0.025 -0.022
 0.20
                                                                                                 tldr_eleuther -0.021
 0.25
 0.30                                                               Baseline                          tldr_llama -0.027 -0.132
      Lexi e  ac                                                                                    tldr_openai -0.032 -0.079       -0.021                  -0.023
          . Ric
                                                                                               wp_bigscience 0.060 -0.178
        Emo     h.
             tion
          Psyc                                                                                                                      -0.057                  -0.022               -0.023
        Read    h.
 Surf   Morp
        Dep
        Sem
               ab.
               ho.
             POS
            end.                                                                                  wp_eleuther 0.071 -0.113          -0.049                  -0.021
             ant.
                                                                                                       wp_llama 0.065 -0.230        -0.047                  -0.041               -0.051
         Enti
         Inforties
               m.
                                                                                                     wp_openai 0.058 -0.216         -0.051
Figure 11: Leave-one-out features ablation performance                                      xsum_bigscience 0.029 -0.239            0.029         0.037      0.035               -0.077
variance across 16 text domain-model domain                                                   xsum_eleuther 0.028 -0.173            0.029         0.037      0.031               -0.065
                                                                                                   xsum_llama 0.044 -0.324          0.030                    0.040               -0.046
                                                                                                 xsum_openai 0.022 -0.253           0.024         0.032      0.031               -0.065

                                                                                                              0.3                 0.2               0.1              0.0             0.1

                                                                                           Figure 13: The difference in the performance for
      0.03                                  0.03                                           the 16 selected text domain-model-domain pairs from
                                     .03                                                   the previous study. We keep only the deltas (∆ =
.02                                                                                        ablation_results − baseline) of ±2% effect.
                                     .01
.01                                                                         0.01
                              0.00                                                         from its creative or news generation.
 0 0.05                                0 0.08                                                 These patterns demonstrate that while text do-
                                                                                           main predicts feature dependency reliably, model
.04
                                     .06                                                   domain introduces critical variation within each
                                                                                           domain. The SQuAD pairs exemplify this: text
.02                                  .03                                                   domain determines that multiple features are re-
                              0.01
                                                                            0.01           quired (unlike news’s lexical-only strategy), but
 0                                     0
      lla
    flanma                            xsu
                                    sci_ wp
                                        g  m                                               model domain determines whether lexical richness
    ope_t5                           hswena
                                        rocg
big op i
   scie t na                            cm t
                                         ev
                                        yelil5
                                     squtldr p                                             helps or hurts. This nuanced interaction reinforces
         nce
         g                                ad
  ele lm
      uth  er                                                                              our selection methodology: pairs showing high
                                                                                           standard deviation changes between ID and OOD
Figure 12: Results of the standard deviation between ab-                                   capture these complex dependencies essential for
lation study across the different testbeds and the ablation                                understanding real-world detection challenges.
study using feature areas. Red bars indicate increased
sensitivity compared to the mean, green bars indicate
decreased sensitivity compared to the mean (horizontal
                                                                                           C.4         Lexical Richness Results in Unseen
line).                                                                                                 Domain-Model Pairs (TB8)
                                                                                           Our ablation studies revealed lexical richness as
                                                                                           the most critical feature group across all testbeds.

                                                                                     21
                     Psych.
                                     Emotion                                  tion appears to have such distinctive lexical patterns
          Readab.                                                             that other linguistic features add confusion.
                                                                                 WP also benefits substantially from lexical-only
                                                      Lexi. Rich.             classification for most models (+4.2% to +16.3%),
                                                            0.1               except with OPT, LLaMA, and GLM which show
Morpho.                                               0.0
                                                0.1                           opposite behavior with drops of -20.0%, -16.6%,
                                       0.2
                               0.3                                            and -2.0% respectively. This suggests some models
                                                             Surface
                                                                              produce creative text with additional non-lexical
                                                                              signals.
  POS
                                                                                 Yelp and CMV (opinion/review domains) gen-
                                                        Inform.
                                                                              erally improve with lexical-only features, partic-
                                                                              ularly for OpenAI (+6.97% CMV, +3.75% Yelp)
    wp Depend.                                              openai
    tldr                                                    llama             and FLAN-T5 models.
    squad                            Entities               eleuther             SciGen, SQuAD, and HSwag consistently per-
    xsum            Semant.                                 bigscience
                                                                              form worse with lexical-only features (all negative
Figure 14: The difference in the performance for the                          values except for the pair of HSwag-OPT), indi-
16 selected text-domain-model-domain pairs from the                           cating these domains require the full feature set.
previous study using the 16 text-domain-model-domain                          Scientific writing and factual Q&A have more sub-
pairs. The text domains separated by colors and and the                       tle linguistic patterns beyond vocabulary choice.
model domains by markers/ shapes.
                                                                              C.4.2   Model domain patterns
The cumulative ablation on TB7 (unseen domains                                OpenAI domain shows the most consistent im-
and model) showed a surprising result: using only                             provement with lexical-only features (7/10 text do-
lexical richness features outperformed the full 284-                          mains positive), with an average delta of +0.0528
feature baseline by +14.29% F1. This motivated us                             across text domains.
to investigate whether this pattern holds for specific                           BigScience, Eleuther, Flan, and OPT domains
unseen domain-model pairs in TB8.                                             show mixed results depending on the text domain.
                                                                              However, the OPT model domain shows the largest
Methodology Since we cannot run the cumula-
                                                                              shift and text-domain dependence in the results. In
tive ablation on all testbeds and all settings, we train
                                                                              text domains like SciGen, WP, and XSum, OPT
the models using only lexical richness features. We
                                                                              models does not benefit from training on the lexi-
report results for TB8 below (with comparison to
                                                                              cal richness features, but the opposite happens in
results of TB1.1). For the 70 text domain-model
                                                                              ROCT domain. This behavior can be also observer
domain pairs in both testbeds (TB1.1 & TB8), we
                                                                              in the other model domains (BigScience, Eleuther,
trained classifiers using only the lexical richness
                                                                              and Flan) with some difference. This suggest that
feature area and compared performance to the base-
                                                                              these models generation of text depends on the text
line (trained on all 284 features). The delta values
                                                                              domain to generate lexically rich texts.
(Figure 15) show the F1-Macro difference between
                                                                                 GLM and LLaMA model domains show more
lexical-only and baseline classifiers.
                                                                              stable results, where both seem to perform better
Results of OOD Performance (TB8) Positive                                     with full features sets in most of the text domains
values (green in heatmap) indicate pairs where lex-                           with few exceptions (ROCT-GLM, ROCT-LLaMA,
ical richness alone outperforms the full feature set:                         and Xsum-GLM with performance improvements
meaning the other 281 features actually introduce                             of +4.2%, +1.4%, and +0.5% respectively).
noise. Negative values (red) indicate traditional
behavior where more features help. We distinguish                             Comparison to In-Distribution Performance
two patterns in Figure 15b to report the text domain                          (TB1.1) The striking difference between in-
patterns.                                                                     distribution (TB1.1) and out-of-distribution (TB8)
                                                                              performance reveals when lexical features alone
C.4.1 Text domain patterns                                                    suffice versus when the full feature set is neces-
ROCT shows the strongest improvement when                                     sary. In TB1.1, where both text and model domains
using only lexical features, with gains across all                            are seen during training, lexical-only features con-
model domains (+10.1% to +15.3%). Story genera-                               sistently underperform the baseline across nearly

                                                                         22
            bigscience eleuther flan_t5                  glm           llama      openai        opt                   bigscience eleuther    flan     glm     llama     openai         opt
    cmv -0.130            -0.276        -0.161         -0.147      -0.070         -0.014       -0.099              cmv 0.011      0.017     0.023    -0.048   -0.050     0.070     -0.101

     eli5 -0.118          -0.350        -0.169         -0.172      -0.172         0.011        -0.141              eli5 -0.036   -0.023     -0.084   -0.007   -0.017     0.099     -0.096

 hswag -0.185             -0.374        -0.082         0.037       -0.035         -0.282       -0.352            hswag -0.109    -0.067     -0.152   -0.108   -0.101    -0.010     0.069

    roct -0.190           -0.395        -0.111         0.132       -0.058         -0.055       -0.330              roct 0.106     0.120     0.013    0.042    0.014      0.153     0.153

sci_gen -0.157            -0.331        -0.160         0.004       -0.054         -0.149       -0.168           sci_gen -0.185   -0.169     -0.166   -0.170   -0.132    -0.190     -0.248

                                                                                                                 squad -0.124    -0.111     -0.166   -0.120   -0.147    -0.157     -0.115
 squad -0.196             -0.509        -0.290         -0.024      -0.040         -0.133       -0.402
                                                                                                                   tldr -0.048   -0.034     -0.077   -0.044   -0.090     0.015     0.041
     tldr -0.113          -0.238        -0.109         0.031           0.092      -0.064       -0.216
                                                                                                                    wp 0.042      0.094     0.093    -0.020   -0.166     0.163     -0.200
      wp -0.111           -0.238        -0.092         -0.150      -0.158         -0.224       -0.115
                                                                                                                  xsum -0.024    -0.004     -0.014   0.005    -0.012     0.053     -0.155
  xsum -0.085             -0.177        -0.079         -0.194      -0.137         -0.103       -0.069
                                                                                                                   yelp 0.022     0.071     0.056    -0.004   -0.036     0.037     0.069
    yelp -0.195           -0.351        -0.184         -0.113      -0.145         -0.157       -0.192

                                                                                                                          0.5      0.4      0.3      0.2      0.1      0.0       0.1         0.2
(a) Results of TB1.1 domain-model pairs. Positive values
(green) indicate lexical richness alone outperforms all 284                                                     (b) Results of TB8 domain-model pairs. Positive values
features; negative values (red) indicate the full feature set is                                                (green) indicate lexical richness alone outperforms all 284
superior.                                                                                                       features; negative values (red) indicate the full feature set is
                                                                                                                superior.

        Figure 15: Performance difference (F1-Macro) between lexical-richness-only and full-feature classifiers.

                                                                                                   0.1
    cmv      0.01       0.01         0.02        0.02          -0.01      0.03         0.02                     strongly positive in TB8 (average +0.106), and Ope-
     eli5    -0.01      -0.06        -0.00       0.03          -0.01      0.05         -0.00                    nAI models shift from negative (average -0.141 in
 hswag       0.03       0.06         0.00        0.00          -0.05      0.02         -0.00       0.05
    roct     0.03       -0.06        0.04        -0.01         -0.00      0.07         0.02                     TB1.1) to positive (average +0.053 in TB8). Ad-
sci_gen      0.05       0.08         -0.04       0.00          0.01       -0.01        0.02                     ditionally, GLM exhibits a unique reversal pattern:
                                                                                                   0
 squad       -0.00      -0.03        0.02        -0.05         -0.03      -0.03        0.02                     it’s shows positive values in TB1.1 for multiple text
     tldr    0.04       0.01         -0.02       -0.00         0.00       -0.02        -0.01
      wp     0.04       -0.01        0.01        0.01          -0.02      0.02         0.00        -0.05        domains (ROCT +0.132, HSwag +0.037, TLDR
  xsum       0.01       -0.05        0.01        -0.00         -0.02      -0.02        0.00                     +0.031, SciGen +0.004), yet these same domains
    yelp     -0.08      -0.03        -0.01       0.01          0.03       -0.03        0.00                     become negative in OOD setting. The pattern flips
                                                                                                   -0.1

   - big
                      r
                                n_t5         cien        ther           glm        a
                  - ele                           ce                              llam                          completely between TB1.1 and TB8: what works
        scie           uthe    - fla                   eleu        nai -
            nce                         bigs
                                                                 ope
                                                                               nai -                            for seen GLM fails for unseen GLM, and vice versa,
              glm             glm                ope                       ope
 glm                                ope             nai -                                                       almost across all text domains. This suggests that
                                       nai -
                                                                                                                while domain-specific features help when available,
                                                                                                                they become misleading in cross-generalization
Figure 16: Heatmap of pairwise Pearson’s r of TTR                                                               scenarios where lexical richness provides more ro-
distributions between selected model family pairs across
                                                                                                                bust, generalizable signals.
text domains. The left columns show GLM paired with
smaller models, while the right columns show OpenAI
paired with models of varying scale. Cell values indicate
                                                                                                                C.4.3     Feature Distributions Analysis
the Pearson’s r between the TTR distributions of the                                                            Given the substantial impact of lexical richness
two model families within each text domain.                                                                     features across all testbeds, we analyzed the distri-
                                                                                                                butions of its three features: TTR (Type token ratio
                                                                                                                of the text: n_types/n_tokens), global token ha-
all 70 pairs (Figure 15a). The worst drops occur                                                                pax legomena (Number of hapax legomena -tokens
with Eleuther models (average -0.327), particularly                                                             that occur only once- in the entire corpus in the text
on SQuAD (-50.9%). This indicates that when                                                                     instance), and lexical density (Lexical density of
training and test data match, classifiers effectively                                                           the text: nl exical_tokens/n_tokens).
leverage text domain-specific and model-specific
patterns from all feature areas. However, in TB8                                                                Distribution Analysis of Lexical Richness Fea-
where both text and model domains are unseen, the                                                               tures The violin plots (Figure 18) and histograms
pattern reverses for many pairs. Notably, ROCT                                                                  (Figure 17) reveal distinct distributional patterns
flips from negative in TB1.1 (average -0.217) to                                                                across the three lexical richness features. Human-

                                                                                                           23
                                          ttr                                   n_global_token_hapax_legomena                              lexical_density
      3.0         Human                                                                                         Human                                                      Human
                                                                     60
                  AI                                                                                            AI                                                         AI
      2.5                                                                                                                 6
                                                                     50
      2.0
                                                                     40
(a)                                                                                                                       4
      1.5
                                                                     30
      1.0                                                            20                                                   2
      0.5                                                            10

      0.0                                                             0                                                   0
            0.0          0.2      0.4           0.6    0.8     1.0        0.0      0.2         0.4    0.6       0.8           0.0   0.2      0.4     0.6          0.8         1.0


                  cmv           wp                                                                   cmv        wp                                         cmv             wp
                  yelp          roct                                                                 yelp       roct      8                                yelp            roct
       3          xsum          hswag                                30                              xsum       hswag                                      xsum            hswag
                  tldr          squad                                                                tldr       squad                                      tldr            squad
                                                                                                                          6
                  eli5          sci_gen                                                              eli5       sci_gen                                    eli5            sci_gen
(b)    2                                                             20
                                                                                                                          4

       1                                                             10
                                                                                                                          2


       0                                                              0                                                   0
            0.0          0.2      0.4           0.6   0.8     1.0         0.0      0.2         0.4    0.6       0.8           0.0   0.2      0.4     0.6          0.8         1.0

       5                                                             40
                  openai                                                                                    openai                                                      openai
                  llama                                                                                     llama         6                                             llama
       4
                  glm                                                30                                     glm                                                         glm
                  flan_t5                                                                                   flan_t5                                                     flan_t5
       3                                                                                                                  4
                  opt                                                                                       opt                                                         opt
(c)                                                                  20
                  bigscience                                                                                bigscience                                                  bigscience
       2
                  eleuther                                                                                  eleuther                                                    eleuther
                                                                                                                          2
                                                                     10
       1


       0                                                              0                                                   0
              0.0         0.2      0.4          0.6   0.8    1.0          0.0       0.2        0.4    0.6       0.8           0.0    0.2      0.4      0.6          0.8          1.0



Figure 17: Density distributions of lexical richness features (TTR, hapax legomena, lexical density) across (a)
Human vs AI labels, (b) text domains, and (c) AI model domains. Overlapping histograms show the discriminative
power of these features across different groupings.


written text consistently exhibits higher values                                               ues closer to human baselines compared to other
across all three features compared to AI-generated                                             model domains like Flan-T5 or OPT, which show
text (row a), indicating greater lexical diversity in                                          more pronounced deviations in TTR and lexical
human writing. The TTR distribution shows hu-                                                  density. These variations explain why lexical rich-
man text centered around 0.6 while AI text clusters                                            ness features, despite being among the most dis-
around 0.8, demonstrating that human authors use                                               criminative overall, show differential effectiveness
a more varied vocabulary relative to text length.                                              across the experimental testbeds, with performance
Hapax legomena-words appearing only once in a                                                  varying more substantially in scenarios involving
text-are substantially more frequent in human writ-                                            specific or unseen text-model domains combina-
ing, with distributions showing clear separation                                               tions where the distributional overlap is greater.
between the two classes. This pattern holds across
nearly all text (row b) and model (row c) domains,                                             D     Qualitative Examples
although the magnitude of separation varies, sug-                                              To complement our quatitative analysis, we present
gesting that lexical richness features are a robust                                            qualitative examples that illustrate how the ex-
discriminative signal for AI-generated text detec-                                             tracted linguistic features manifest in human-
tion, which supports our findings.                                                             written versus AI-generated text. We select two fea-
                                                                                               ture areas–Emotion and Lexical Richness– based
Domain and Model-Specific Variations While                                                     on their performance and clear distinction in both
the human-AI separation is consistent across con-                                              texts, and choose the domain-model pairs that best
ditions, notable variations emerge when examining                                              highlight the contrast identified in our experiments.
specific text and model domains. Domain-level
analysis (row b) shows that certain text domains                                               D.1    Emotion Features — Domain: Yelp,
like SciGen and SQuAD exhibit tighter distribu-                                                       Model: OpenAI text-davinci-003
tions and reduced human-AI separation, particu-                                                We select the Yelp domain paired with OpenAI’s
larly in hapax legomena counts. Model domain                                                   text-davinci-003 for the emotion feature vi-
comparisons (row c) reveal that some AI-text gener-                                            sualization (Figure 19), as Yelp reviews are in-
ators, particularly OpenAI, GLM, and Llama mod-                                                herently opinion-driven and exhibit a wide range
els, produce text with hapax legomena counts val-                                              of emotional expression among the text domains.

                                                                                          24
                                                 ttr                                                       n_global_token_hapax_legomena                                                                    lexical_density
      1.0                                                                                                                                                                  1.0
                                                                                           0.8

      0.8                                                                                                                                                                  0.8
                                                                                           0.6
      0.6                                                                                                                                                                  0.6
(a)                                                                                        0.4
      0.4                                                                                                                                                                  0.4

      0.2                                                                                  0.2                                                                             0.2

      0.0                                                                                  0.0                                                                             0.0
                           Human                                 AI                                             Human                            AI                                             Human                            AI



                                                                                                                                                                           1.0
      1.0                                                                                  0.8

      0.8                                                                                                                                                                  0.8
                                                                                           0.6
      0.6                                                                                                                                                                  0.6
(b)                                                                                        0.4
      0.4                                                                                                                                                                  0.4

      0.2                                                                                  0.2                                                                             0.2

      0.0                                                                                  0.0                                                                             0.0

            cm        lp   xs     tldr      i5    w    p   ct   wag         ua d
                                                                                       n
                                                                                      ge         cm        lp   xs     tldr      i5    p
                                                                                                                                       w   ct   wag         ua d
                                                                                                                                                                       n
                                                                                                                                                                      ge         cm        lp   xs     tldr      i5    p
                                                                                                                                                                                                                       w   ct   wag         ua d
                                                                                                                                                                                                                                                       n
                                                                                                                                                                                                                                                      ge
              v   ye         um          el                ro
                                                                       sq                          v   ye         um          el           ro
                                                                                                                                                       sq                          v   ye         um          el           ro
                                                                                                                                                                                                                                       sq
                                                                hs              sci_                                                            hs              sci_                                                            hs              sci_

                                                                                                                                                                           1.0
      1.0                                                                                  0.8
                                                                                                                                                                           0.8
      0.8
                                                                                           0.6
                                                                                                                                                                           0.6
      0.6
(c)                                                                                        0.4
      0.4                                                                                                                                                                  0.4

      0.2                                                                                  0.2                                                                             0.2

      0.0
                                                                                           0.0                                                                             0.0
                 ai        m           er         5         t               e      a                  ai        m           er         5    t               e      a                  ai        m           er         5    t               e      a
             en        gl          th         n_           op          nc          m              en        gl          th         n_      op          nc          m              en        gl          th         n_      op          nc          m
                                  eu             t                   ci         lla                                    eu             t              ci         lla                                    eu             t              ci         lla
            op                              fla                         e                        op                              fla                    e                        op                              fla                    e
                                  el                             gs                                                    el                        gs                                                    el                        gs
                                                                bi                                                                              bi                                                                              bi



Figure 18: Violin plots for the three lexical richness features: TTR (left), hapax legomena (middle), and lexical
density (right). Each row displays distributions across Human vs AI, text domains, and model domains, revealing
both central tendency and distributional shape.


For each sample, we display two emotion in-                                                                                        (combinations of domain and models) exhibited
tensity dimensions—anger (red) and disgust                                                                                         one of the largest performance drops in TB8 when
(blue)—where darker shading indicates higher in-                                                                                   lexical richness features were removed (cf. Fig-
tensity scores from the NRC Affect Intensity Lexi-                                                                                 ure 13), and the spider plot analysis (Figure 14)
con(Mohammad, 2018b). Valence is encoded back-                                                                                     confirmed that lexical richness is the dominant fea-
ground highlighting: green indicates high valence                                                                                  ture area for these pairs. Furthermore, XSum (news
(> 0.66) and pink indicates low valence (< 0.33)                                                                                   summarization) produces structurally diverse texts
based on the NRC VAD Lexicon (Mohammad,                                                                                            where lexical patterns differ markedly between hu-
2018a). Aggregate statistics (avg_intensity,                                                                                       man and AI writing.
avg_valence, n_low/high_valence) are shown                                                                                            Each token is annotated along three dimen-
above each sample.                                                                                                                 sions: italic marks first occurrences (unique types
   The examples reveal a consistent pattern: human-                                                                                contributing to TTR), bold marks lexical tokens
written Yelp reviews exhibit higher anger and dis-                                                                                 (nouns, verbs, adjectives, and adverbs contribut-
gust intensities with more low-valence tokens, re-                                                                                 ing to lexical density), and underline marks hapax
flecting genuine frustration and emotional variabil-                                                                               legomena (tokens appearing only once in the text).
ity. In contrast, AI-generated samples tend toward                                                                                 Aggregate statistics (ttr, lexical_density,
elevated valence with fewer or no anger/disgust                                                                                    n_hapax_legomena, n_tokens, n_types) are dis-
signals, even when the generated content describes                                                                                 played above each sample.
negative experiences that are parallel to human text.                                                                                 The examples illustrate a recurring pattern:
                                                                                                                                   human-written texts tend to be longer with lower
D.2         Lexical Richness — Domain: XSum,                                                                                       TTR due to natural repetition, yet contain more ha-
            Models: LLaMA & OpenAI                                                                                                 pax legomena in absolute terms. AI-generated con-
We select XSum paired with LLaMA (-7B,-13B)                                                                                        tinuations are typically shorter but exhibit higher
and OpenAI (text-davinci-003) for the lexical                                                                                      TTR and lexical density, suggesting a more concen-
richness visualization (Figure 20), as these pairs                                                                                 trated but less varied vocabulary distribution.

                                                                                                                            25
E     Distributional Similarity of Text and                 model family pairs into three categories follow-
      Model Domains                                         ing the clustering observed in the ablation studies
                                                            (cr. Section 4.2): Smaller–Smaller (e.g., FLAN-T5
E.1    Wasserstein Distance of Text Domains                 vs OPT), Smaller–LlaMA/OpenAI (e.g., Eleuther
The clustered heatmap (Figure 21) reveals two               vs. LLaMA), and LLaMA–OpenAI.
distinct groups of text domains pairs based on                 Figure 22 presents the Person’s r distributions
their Wasserstein distances across the top 10               across the 21 model family pairs. Overall, the r
most discriminative features. The first group,              values are low and centered around zero suggesting
appearing on the left side of the heatmap, in-              that model families do not exhibit strongly corre-
cludes pairs involving domains such as ROC-                 lated TTR patterns across text domains. This is
Stories, HellaSwag, WritingPrompts, and TLDR,               consistent with the model domain ablation find-
which exhibit notably higher distributional di-             ings (Section 4.2), where lexical richness features
vergence, particularly for surface-level fea-               displayed opposing effects for different model fami-
tures such as raw_sequence_length; n_tokens,                lies in both ID and OOD settings: improving perfor-
n_syllables, and n_lemmas. This is consis-                  mance for some (e.g., FLAN-T5, OPT, BigScience,
tent with the substantial OOD performance drops             Eluether) while degrading it for others (e.g., Ope-
for ROC-Stories (−26.0%), HellaSwag (−21.4%),               nAI, LLaMA, GLM). The near-zero correlations
and TLDR (−20.5%) in TB6 (See Table 4), sug-                observed here suggest that these model families
gesting that their distinct linguistic distributions        occupy distinct regions of the TTR feature space,
make cross-domain generalization harder. The sec-           which explains why a single classifier trained on
ond group, on the right side, includes pairs involv-        the combined feature space struggles to generalize
ing CMV, XSum, ELI5, SQuAD, and Yelp, which                 across model domain in OOD settings.
show lower distributional divergence overall, align-           Notably, the Smaller—Smaller group (blue) dis-
ing with their comparatively smaller OOD perfor-            plays slightly more variance in r values compared
mance drops.                                                to the other two groups, with some pairs such as
   Interestingly,             entropy            and        glm–eleuther showing larger mid-spread ranges.
n_PRON_Number_Sing exhibit a different cluster-             This variability within the smaller model group
ing pattern from the surface features, showing              aligns with observation that smaller models display
higher divergence for pairs involving Yelp and              more salient and model-specific linguistic signa-
SQuAD domains where emotion and psycholin-                  tures (Section 4.2), making their TTR distributions
guistic features were found to be more informative          less consistently correlated across text domains. In
in the ablation studies. This suggests that while           contrast, the LLaMA-OpenAI comparison (green)
surface features largely drive the between-domain           shows r values tightly concentrated around zero
distributional differences, other feature areas             with minimal variance, corroborating the finding
capture complementary domain-specific signals               the these two large model families share similar
that further explain the variability in cross-domain        lexical richness patterns, which explains the perfor-
generalization observed in the main experiments.            mance improvement observed for OpenAI in OOD
                                                            settings where LLaMA data is present in training.
E.2    Pearson’s r Calculations of Model                       Figure 16 presents Pearson’s r values for se-
       Domains                                              lected model family pairs that reflect the contrasts
Building on the distributional analysis of lexical          identified in the ablation analysis (Section 4.2):
richness features in Section C.4.3 (See Figures 17          GLM paired with smaller models (left), and Ope-
and 18), which revealed that TTR exhibits the most          nAI paired with models of different scale (right).
pronounced separation between human and AI-                 Overall, the near-zero correlations confirm that
generated text across both model and text domains,          model families occupy distinct regions of the TTR
we compute pairwise Pearson’s r between model               feature space across text domains. Among the
domain (family) distributions on the TTR feature            GLM pairs, glm–eleuther shows the largest devi-
across text domains. Specifically, for each pair            ations, with positive correlations for SciGen (r =
of model families, we compute the correlation be-           0.08) and negative correlations for ELI5 and ROCT
tween their TTR feature distributions within each           (r = −0.06 each). Similarly, glm–bigscience
text domain, yielding a distribution of r values            exhibit more negative correlations for Yelp (r =
across the ten MAGE text domain. We group the               −0.08). These domain-specific deviations are con-

                                                       26
sistent with the ablation findings, where GLM
exhibited model-specific linguistic signature that
vary substantially across text domains, particularly
for story generation (ROCT) and opinion domains
(Yelp, ELI5).
   Among the OpenAI pairs, openai–glm shows
the most notable deviation for ROCT (r = 0.07)
and ELI5 (r = 0.05), while all other pairs remain
relatively close to zero. The fact that ROCT con-
sistently shows the largest deviations across both
GLM and OpenAI pairs aligns with the OOD re-
sults (Table 4), where ROCT exhibited the largest
performance drop (−26.0%) in unseen domain set-
tings, suggesting that story generation elicits the
most domain-specific TTR behavior across model
families. Finally, openai–llama shows uniformly
near-zero correlations (|r| ≤ 0.02), indicating that
despite both being large model families, their TTR
distributions do not co-vary — consistent with
their contrasting OOD behaviors where OpenAI
improves (+6.1%; Table 3) while LLaMA degrades
(−11.0%).

F        Use Of AI Assistants
In this work, GitHub Copilot14 (version as of
November 2025) was used as a code comple-
tion/suggestion tool. Additionally, AI-assisted writ-
ing tools like Grammarly15 (accessed November
2025 - January 2026) have been used for spelling
checks and grammar corrections.




    14
         https://github.com/features/copilot
    15
         https://app.grammarly.com/


                                                        27
     Human    avg_intensity_anger:0.762 |                                      Text-davinci-003 avg_intensity_anger:N/A |
     avg_intensity_disgust: 0.680 | avg_valence: 0.676                         avg_intensity_disgust: N/A avg_valence: 0.726               |
     | n_low_valence: 3 | n_high_valence: 64                                   n_low_valence: 1 | n_high_valence: 21
     So, the lady and I were in search of some Saturday night
     food and couldn't decide on what. I had the brilliant idea                So, the lady and I were in search of some Saturday night
     to get on Groupon and was stuck in between two choices:                   food and couldn't decide on what. I had the brilliant idea to
     Rita's and another unnamed Phoenix establishment that                     get on Groupon and was stuck between a pizza joint and a
     we had already been to that is always solid never great.                  Mexican restaurant. The lady wanted to get the pizza, but I
     Well, what the hell, let's give Rita's a shot. Nice and                   told her that we could try something new and go for the
     conveniently located on 35th and the I-10, we find a spot and
     get in. Order a few margaritas and they were great. I'm not the           Mexican restaurant. We ended up with a great deal and had
     world's biggest fan of the marg but Aaron knows how to hook it            an amazing meal.
     up. Next, we ordered the table side Guac, I got the Playa Bonita,
     the lady got the Seafood enchiladas. Everything was …

                                                                         (a)
     Human     avg_intensity_anger:0.688 |                                     Text-davinci-003 avg_intensity_anger:N/A |
     avg_intensity_disgust: 0.550 | avg_valence: 0.617                         avg_intensity_disgust: N/A | avg_valence: 0.636
     | n_low_valence: 3 | n_high_valence: 20                                   | n_low_valence: 3 | n_high_valence: 23

     Poor service at this location- we reserved a full size but                Poor service at this location- we reserved a full size but they
     they didn't have one. Luckily for them, someone had                       didn't have one. Luckily for them, someone had altered our
     altered our res to a midsize, which they had. We had our
                                                                               res to a midsize, which they had. We had to wait a while to
     confirmation but were told we could have changed our res
     after printing; essentially calling us liars. I almost got into           get the car. I apologize for the inconvenience you
     it with two employees who acted like they were doing us a                 experienced. We strive to provide exceptional service to all
     favor by giving us a car our baby seat could barely fit into.             customers, and I apologize that we did not meet your
     Wow, that was a terrible experience.                                      expectations. We would love to make it up to you by
                                                                               offering you a discount on your next rental with us. Please
                                                                               contact us at xxx-xxx-xxxx so we can discuss this further. …

                                                                         (b)
     Human    avg_intensity_anger:0.781 |                                      Text-davinci-003 avg_intensity_anger:N/A |
     avg_intensity_disgust: 0.321 | avg_valence:                               avg_intensity_disgust: N/A | avg_valence: 0.659
     0.624 | n_low_valence: 3 | n_high_valence: 27                             | n_low_valence: 1 | n_high_valence: 32

     We decided to give brunch a try for our first visit to Casbah.            We decided to give brunch a try for our first visit to Casbah.
     We were surprised by the huge tent covering the outdoor                   We were surprised by the huge tent covering the outdoor
     dining area. We opted for an inside table, the interior is                dining area. We opted for an inside table and were seated
     somewhat small the tables are close together. For brunch,                 immediately. The menu was vast but we decided to start
     you are served your choice of drink, appetizer and entree.                with the mushroom toast and the curry cauliflower. Both
     For our drinks, BJ had a Bloody Mary and I had a Bellini.                 dishes were delicious and the portion sizes were generous.
     We were served a basket of yummie bread and mini muffins.                 For the main course, we shared the paella which was full of
     For appetizers, we got a Three Sisters Farms mesclun greens               flavor and cooked perfectly. We ended our meal with the
     and smoked salmon and truffled potato cake. …                             cheesecake, which was light and flavorful. Our server …

                                                                         (c)

Figure 19: Parallel human–AI text pairs from the Yelp domain (AI model: Text-davinci-003) illustrating differences
in a few selected features from emotion area. Visual markers: red bold text = anger intensity, blue bold text =
disgust intensity, green highlight = high valence (> 0.66) and pink highlight = low valence (< 0.33). feature
values (average anger and disgust intensity, average valence, and high/low valence word counts) are shown above
each text. Emotion intensity is derived from the NRC Affect Intensity Lexicon and valence from the NRC VAD
lexicon, following the elfen toolkit’s extraction procedure. Some texts are truncated for space; ellipses (. . . )
indicate omitted content.




                                                                         28
     Human ttr: 0.271 | lexical_density: 0.298 |                    Llama-7B ttr: 0.694 | lexical_density: 0.426            |
     n_hapax: 114 | n_tokens: 822 | n_types: 223                    n_hapax: 62 | n_tokens: 108 | n_types: 75
     Media playback is not supported on this device After           Media playback is not supported on this device Our
     an even first 30 minutes, Danny Wright tapped in               mission is to inspire, empower and motivate our
     from James Dayton's free-kick to put the Robins in             online community in the pursuit of feeling
     front. But Tubbs levelled after the restart, latching          BodyPositive. And we'll be with you every step of the
     onto Maxime Biamou's header and slotting in from 10            way, because who says diet is a dirty word. Feel free
     yards out. Robert Dickie headed against the bar for the        to browse our extensive library of articles on a
     Robins late on, before Deacon fired in to win the game         variety of topics. This is the first time that the FDA has
     in added time. Sutton have won just one of their past          approved a drug to treat obesity, and it is a big deal.
     eight games in the National League - including a 6-0           In the 1990s, pharmaceutical companies tried to
     home defeat by Dover on Tuesday - but Deacon's …               develop drugs to treat obesity, but the drugs had...

                                          (a) Human (Left) vs. LLaMA-7B (right).
     Human ttr: 0.276 | lexical_density: 0.314 |                    Llama-13B ttr: 0.675 | lexical_density: 0.400
     n_hapax: 137 | n_tokens: 978 | n_types: 270                    | n_hapax: 82 | n_tokens: 160 | n_types: 108
     Andreu was denied from the spot by a brilliant save            Andreu was denied from the spot by a brilliant save
     from Raith keeper Kevin Cuthbert 15 minutes from               from Raith keeper Kevin Cuthbert 15 minutes from
     time. United were reduced to ten men when former               time. United were reduced to ten men when former
     Rovers defender Lewis Toshney was sent off in 55               Rovers defender Lewis Toshney was dismissed for a
     minutes after collecting a second yellow card. Rudi            second bookable offence. Manager Jackie McNamara
     Skacel struck the bar for Raith but neither side could         admitted he was delighted to see his side's recent
     find the net. Dundee United manager Ray McKinnon is            revival continue with another impressive
     desperate to add more of a goal threat to his team             performance at a venue where United have a mixed
     and Dutch trialist striker Felitciano Zschusschen              record in recent years. "I think the pitch is always a
     watched from the stands. The Tangerines struggled …            little bit dodgy here but the guys are gelling, that's…

                                          (b) Human (left) vs. LLaMA-13 (right).
     Human ttr: 0.292 | lexical_density: 0.330 |                    Text-davinci-003 ttr: 0.558 | lexical_density: 0.289
     n_hapax: 211 | n_tokens: 1191 | n_types: 348                   | n_hapax: 68 | n_tokens: 190 | n_types: 106
     The Latics are seven points from safety with six games         The Latics are seven points from safety with six games
     remaining including tough trips to Brighton and                remaining including tough trips to Brighton and
     Reading. David McGoldrick put Ipswich ahead                    Reading. David McGoldrick put Ipswich ahead
     midway through the first half, slotting in Myles               midway through the first half, slotting in from close
     Kenlock's pass, before Freddie Sears raced clear to            range after good work from David Healy. The Latics
     double the lead. Wigan improved after the break,               had a great chance to equalise on the stroke of
     Bartosz Bialkowski saving brilliantly from Ryan                half-time, but Grant Holt fired over the bar from 12
     Colclough and Alex Gilbey, but Sears pounced late on to        yards out. Ipswich doubled their lead in the second
     make it 3-0. The win relieved some of the pressure on          half when Luke Chambers nodded in a corner from Jay
     Town boss Mick McCarthy, following seven…                      Emmanuel-Thomas to make it 2-0. Substitute Jon …

                                       (c) Human (left) vs. Text-davinci-OO3 (right).

Figure 20: Parallel human-AI text pairs from the XSum domain illustrating differences in lexical richness features.
Each pair shares the same opening words, with the AI text generated as a continuation. Visual markers: italic= first
occurrence of a token (unique type, contributing to TTR), bold = lexical token (noun, verb, adjective, or adverb,
contributing to lexical density, and underline = hapax legomenon (taken appearing only once in the text). Feature
values (TTR, lexical density, hapax count, token count, and type count) are shown above each text. Texts are
truncated for space; ellipses (. . . ) indicate omitted content.




                                                               29
                                          squa  d
                                          yelp- -roct
                                                ro
                                          cmv- ct
                                                ro
                                          eli5-r ct
                                                o
                                          xsum ct-
                                          hswa roct
                                                 g
                                          tldr-w -wp
                                          squa  dp
                                          sci_g -wp
                                                 e
                                          yelp- n-wp
                                          cmv- pw
                                                h
                                          cmv- swag
                                                tld
                                          wp-ro rc
                                          eli5-s t
                                                 c
                                          eli5-h i_gen
                                                 s
                                          eli5-t wag
                                          xsum rld
                                                 -
                                          eli5-w hswag
                                          xsum p -
                                          yelp- sci_gen
                                                h
                                          cmv- swag
                                                s
                                          xsum ci_gen
                                                 -
                                          sci_g tldr
                                                 e
                                          hswa n-roct
                                                 g
                                          tldr-r -roct
                                                o
                                          yelp- ct
                                                s
                                          xsum quad
                                                 -
                                          eli5-s wp
                                                 q
                                          yelp- uad
                                                s
                                          hswa ci_gen
                                                 g
                                          wp-c -squad
                                                m
                                          yelp- v
                                          hswa rtld
                                                 g
                                          tldr-s -sci_gen
                                                q
                                          xsum uad
                                                 -
                                          xsum eli5
                                                 -
                                          tldr-s cmv
                                                c
                                          squa i_gen
                                                d
                                          tldr-h -sci_gen
                                                 s
                                          yelp- wag
                                          squa  eli5
                                                d
                                          eli5-c -cmv
                                          xsum v m
                                                 -
                                          yelp- squad
                                                c
                                          yelp- mv
                                                xsum
                                entropy .16 .22 .10 .04 .03 .31 .13 .06 .32 .44 .07 .20 .22 .15 .12 .07 .11 .20 .12 .13 .03 .08 .11 .09 .10 .38 .20 .14 .16 .25 .33 .32 .10 .06 .05 .13 .19 .25 .19 .24 .26 .14 .14 .13 .24
              n_PRON_Number_Sing .28 .15 .15 .25 .15 .30 .23 .28 .28 .16 .15 .08 .02 .05 .06 .04 .14 .26 .12 .15 .12 .07 .27 .30 .23 .12 .16 .04 .12 .02 .16 .07 .03 .05 .10 .03 .05 .02 .07 .10 .13 .10 .12 .02 .02          0.5
                  avg_intensity_anger .08 .08 .26 .13 .25 .45 .35 .27 .27 .27 .37 .26 .35 .05 .23 .13 .36 .22 .18 .18 .19 .25 .10 .11 .03 .01 .10 .05 .03 .18 .09 .08 .18 .08 .13 .01 .08 .05 .10 .05 .18 .14 .18 .19 .18     0.4
                 avg_intensity_disgust .03 .11 .26 .12 .19 .38 .34 .29 .31 .21 .33 .29 .31 .11 .19 .15 .26 .19 .18 .18 .25 .22 .02 .07 .03 .08 .13 .09 .10 .10 .08 .14 .08 .06 .07 .07 .04 .03 .04 .02 .23 .14 .16 .15 .08
                           avg_arousal .08 .14 .03 .20 .23 .05 .02 .05 .26 .11 .06 .02 .03 .08 .23 .17 .26 .18 .05 .17 .25 .20 .28 .03 .03 .07 .21 .13 .14 .11 .02 .11 .31 .04 .05 .20 .25 .20 .06 .09 .04 .17 .15 .11 .10    0.3
Feature             ramification_factor .17 .25 .26 .33 .28 .06 .09 .07 .07 .14 .19 .21 .12 .24 .26 .28 .21 .22 .19 .19 .17 .23 .09 .06 .05 .08 .17 .16 .16 .12 .15 .20 .06 .12 .05 .02 .04 .08 .04 .08 .09 .07 .11 .01 .03
                             n_lemmas .26 .31 .32 .42 .35 .08 .06 .07 .04 .12 .20 .18 .19 .25 .29 .27 .23 .23 .19 .19 .16 .21 .17 .13 .15 .06 .16 .16 .14 .15 .13 .16 .08 .11 .06 .03 .03 .09 .07 .10 .07 .09 .10 .02 .04     0.2
                              n_tokens .30 .34 .38 .44 .38 .11 .07 .08 .06 .11 .25 .18 .24 .22 .31 .24 .25 .20 .16 .22 .16 .19 .22 .13 .20 .05 .15 .14 .13 .18 .14 .15 .12 .10 .05 .01 .02 .08 .10 .09 .08 .06 .09 .03 .04
                                                                                                                                                                                                                              0.1
                raw_sequence_length .34 .38 .43 .48 .43 .09 .08 .09 .06 .11 .24 .21 .27 .22 .30 .27 .24 .22 .17 .19 .17 .21 .26 .19 .22 .04 .16 .14 .11 .16 .17 .16 .10 .12 .05 .01 .05 .08 .06 .11 .09 .05 .09 .06 .05
                            n_syllables .30 .34 .40 .44 .39 .08 .08 .08 .06 .11 .23 .22 .24 .22 .28 .26 .22 .21 .16 .18 .17 .21 .22 .16 .18 .05 .15 .14 .12 .14 .16 .16 .08 .12 .06 .01 .04 .08 .05 .10 .10 .05 .09 .05 .05   0.0


Figure 21: Clustered heatmap of pairwise Wasserstein distances for the top 10 most discriminative linguistic features
across all human text domain pairs. Rows represent features that most consistently appear in the top 10 most
discriminative features across domain pairs, ranked by their frequency of occurrence. Columns represent each pair
of domains. Higher values (darker cells) indicate greater distributional divergence between the two domains for that
feature, suggesting that the feature captures domain-specific linguistic patterns. Lower values (lighter cells) indicate
similar distributions across domains, suggesting domain-invariant characteristics




                0.08                                                                                                                                                                                    Group
                                                                                                                                                                                                   Smaller - Smaller
                0.06                                                                                                                                                                               Smaller - LLaMA/OpenAI
                0.04                                                                                                                                                                               LLaMA - OpenAI
                0.02

Pearson's r
                0.00
                0.02
                0.04
                0.06
                0.08
                     ther      opt       opt       ce        ce       ce       ther       t5       ther      ther      ce         e       glm        pt      ther       lm        t5        er       opt       t5        a
                                                 cien     cien       cien              flan_                         cien      ienc               a o                a g        lan_     leuth              flan_      llam
                  eleu       t5      glm                                     eleu               eleu      eleu               igsc      nai                 eleu                                   nai
                          flan_               bigs      bigs      bigs                                            bigs                          llam               llam      a f       a e                          nai
                                                                                    glm                                   a b        ope                                                        ope      nai
                t5                                                        opt                glm        ce                                              nai                llam     llam               ope        ope
          flan_                            opt       glm       t5                                    cien      nai                                     ope
                                                             flan_                                           ope        llam
                                                                                                   bigs

Figure 22: Pairwise Pearson’s r of TTR feature distributions across model family pairs, with distributions computed
over the ten text domains. Pairs are grouped into three categories: Smaller–Smaller (blue; e.g., FLAN-T5 vs. OPT),
Smaller–LLaMA/OpenAI (orange; e.g., Eleuther vs. LLaMA), and LLaMA–OpenAI (green). TTR was selected as
the focal feature given its pronounced human–AI distributional separation observed in Section C.4.3.




                                                                                                                     30


## Extraction verification

- **Beginning checked:** page 1 title, author block, abstract, introduction, and research questions were compared with the rendered PDF.
- **Middle checked:** page 15 testbed table and cross-dataset discussion were compared with the rendered PDF.
- **End checked:** pages 24 and 25 lexical-richness figures and discussion, plus page 30 distribution figures and captions, were compared with the rendered PDF.
- **Structure checked:** 30 PDF pages; sections 1 to 5; Limitations; Ethical Considerations; references; appendices A to F; 16 tables; 22 figures; footnotes; qualitative examples; and the AI-assistance disclosure are present in the extraction or preserved attachment.
- **Known omissions:** none from the preserved source. Chart geometry, color, font emphasis, and some symbol glyphs are not represented faithfully in plain text, so the PDF attachment remains authoritative for those elements.

## Preserved attachments

| Path | Role in the source | SHA-256 | Preservation / extraction notes |
|---|---|---|---|
| `snapshots/attachments/el-attar-linguistic-features-ai-text-detection-arxiv-2606.04177v1.pdf` | Authoritative 30-page arXiv v1 paper | `454f87ecc87ad9c329018dd64c9a1b66bd35c9e13a8656ce9f833c17563e523a` | Downloaded directly from arXiv; embedded text extracted with `pdftotext -layout`; selected pages rendered with `pdftoppm` for visual verification. |
