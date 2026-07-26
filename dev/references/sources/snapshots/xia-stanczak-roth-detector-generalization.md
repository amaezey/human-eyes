# Explaining Generalization of AI-Generated Text Detectors Through Linguistic Analysis

- **Canonical URL:** https://aclanthology.org/2026.eacl-long.307/
- **Alternate access URLs:**
  - https://aclanthology.org/2026.eacl-long.307.pdf
  - https://doi.org/10.18653/v1/2026.eacl-long.307
- **Author / owner:** Yuxi Xia, Kinga Stańczak, and Benjamin Roth
- **Publisher:** Association for Computational Linguistics
- **Published:** March 2026
- **Retrieved:** 2026-07-14
- **Stable identifier:** DOI 10.18653/v1/2026.eacl-long.307; ACL Anthology ID 2026.eacl-long.307
- **Version / revision:** EACL 2026 final proceedings version, pages 6524-6546
- **Extraction method:** ACL Anthology PDF downloaded with curl; complete embedded text layer extracted with `pdftotext -layout` (Poppler 25.10.0); PDF metadata and page count checked with `pdfinfo`
- **Full-text status:** complete
- **Access and transformation notes:** No OCR was required. The layout-preserving text extraction retains all 23 pages, including tables, figure captions, prompts, limitations, references, and appendices. Multi-column reading order and wide tables are mechanically interleaved in places; the original PDF is preserved as an attachment for visual verification.

## Full text

        Explaining Generalization of AI-Generated Text Detectors Through
                               Linguistic Analysis
                             Yuxi Xia1,2 , Kinga Stańczak3 , Benjamin Roth1,4
                  1
                    Faculty of Computer Science, University of Vienna, Vienna, Austria
                       2
                         UniVie Doctoral School Computer Science, Vienna, Austria
            3
              Department of Language Science and Technology, Saarland University, Germany
          4
            Faculty of Philological and Cultural Studies, University of Vienna, Vienna, Austria
                                             Correspondence: yuxi.xia@univie.ac.at


                           Abstract                                  Prior studies have begun to examine generaliza-
                                                                  tion in the context of unseen prompts, models, or
        AI-text detectors achieve high accuracy on in-
                                                                  datasets (Xu et al., 2024; Liu et al., 2024). How-
        domain benchmarks, but often struggle to gen-
        eralize across different generation conditions            ever, these efforts largely focus on reporting perfor-
        such as unseen prompts, model families, or do-            mance drops without probing the underlying causes.
        mains. While prior work has reported these                Meanwhile, recent benchmark datasets introduce
        generalization gaps, there are limited insights           diversity in generation settings (Wang et al., 2024a;
        about the underlying causes. In this work, we             Macko et al., 2023; Li et al., 2024), but offer limited
        present a systematic study aimed at explaining            interpretability regarding the features detectors rely
        generalization behavior through linguistic anal-          on. A more systematic and interpretable approach
        ysis. We construct a comprehensive benchmark
                                                                  is needed to explain why generalization succeeds
        that spans 6 prompting strategies, 7 large lan-
        guage models (LLMs), and 4 domain datasets,               or fails.
        resulting in a diverse set of human- and AI-                 In this paper, we propose to understand general-
        generated texts. Using this dataset, we fine-tune         ization through the lens of linguistic analysis. We
        classification-based detectors on various gener-          hypothesize that changes in surface-level linguistic
        ation settings and evaluate their cross-prompt,           features, such as verb tense, syntactic complexity,
        cross-model, and cross-dataset generalization.            or pronoun usage, can partially account for gen-
        To explain the performance variance, we com-
                                                                  eralization behavior. To test this hypothesis, we
        pute correlations between generalization accu-
        racies and feature shifts of 80 linguistic features       construct a comprehensive benchmark combining 7
        between training and test conditions. Our anal-           LLMs (e.g., Deepseek (DeepSeek-AI, 2025), Mis-
        ysis reveals that generalization performance for          tral (Mistral AI, 2024)), 4 domains (abstracts, news,
        specific detectors and evaluation conditions is           reviews, QA), and 6 prompting strategies (e.g., few-
        significantly associated with linguistic features         shot, chain-of-thought (CoT)), enabling evaluation
        such as tense usage and pronoun frequency. 1              across prompt, model, and dataset generalization.
                                                                  We train the AI-text detectors by fine-tuning on two
1       Introduction
                                                                  state-of-the-art models (XLM-RoBERTa (Conneau
The ability to reliably detect AI-generated text is               et al., 2020) and DeBERTa-V3 (He et al.)) for bi-
becoming increasingly critical as large language                  nary classification tasks. Each detector is trained
models (LLMs) are deployed in education, me-                      with the texts generated by every possible condi-
dia, and content moderation (Guo et al., 2024; Hu                 tion (combination of prompt, model and dataset).
et al., 2023). While recent detectors achieve near-               The fine-tuned detectors are evaluated for cross-
perfect performance on standard benchmarks (Guo                   prompt, cross-model and cross-dataset generaliza-
et al., 2023; Wang et al., 2024a), these evaluations              tion performance. Our results reveal substantial
typically assume that training and testing data are               performance degradation under out-of-domain con-
drawn from the same distribution. In real-world                   ditions, despite near-perfect in-domain accuracy.
scenarios, however, AI-generated text varies widely                  To explain these generalization gaps, we perform
across prompts, model families, and domains, rais-                a large-scale correlation analysis between detector
ing serious concerns about how well detectors gen-                generalization performance and score changes in
eralize under distribution shifts.                                80 linguistic feature metrics across training and test-
    1
    Code and data is available at: https://github.com/            ing settings. We find that linguistic features have
Yuuxii/Generalization-of-AI-text-Detector                         significant (p<0.05) correlations with generaliza-
                                                              6524
           Proceedings of the 19th Conference of the European Chapter of the Association for Computational Linguistics
                                            Volume 1: Long Papers, pages 6524–6546
                               March 24-29, 2026 ©2026 Association for Computational Linguistics
tion across different test settings. While some lin-    et al., 2020)). While statistical detectors offer in-
guistic features (e.g., passive voice, short sentence   terpretability, classifier-based approaches consis-
ratio) are strongly correlated (Pearson correlation     tently achieve stronger performance on benchmark
> 0.7) with generalization behavior in specific con-    datasets such as M4GT (Wang et al., 2024a), MUL-
figurations, there is no universal linguistic signal    TITuDE (Macko et al., 2023), and MultiSocial
that explains all cases. Our findings suggest that      (Macko et al., 2025). Our study builds on this foun-
linguistic features offer a useful, though partial,     dation by fine-tuning two top-performing detectors,
explanation of generalization, and that detectors       XLM-RoBERTa and DeBERTa-V3, across varied
may rely on different features depending on their       training settings to assess their generalization.
training setup and the test conditions.
   In summary, our main contributions are: (1)          Generalization in Detection. Generalization is
A new benchmark for evaluating AI-text detector         a core challenge in AI-text detection. Prior work
generalization across 6 prompts, 4 domains, and         has shown that detectors trained on one task or
7 LLMs; (2) A comprehensive analysis linking            domain often fail when evaluated on others (Xu
linguistic feature shifts to detector generalization    et al., 2024; Li et al., 2024; Bhattacharjee et al.,
performance; (3) Insights into which linguistic fea-    2024). However, most studies focus on reporting
tures are most predictive of generalization behavior,   performance gaps without offering deeper expla-
helping to guide the development of more robust         nations. Moreover, while some papers examine
and interpretable detectors.                            prompt-based variation, they typically limit prompt-
   Ultimately, our work aims to move beyond raw         ing strategies or focus on handcrafted or adversarial
performance scores toward a deeper understand-          prompts (Xu et al., 2024; Zhang et al., 2024). In
ing of generalization behavior in AI-text detection.    contrast, our work evaluates generalization com-
While linguistic features alone do not capture the      prehensively across prompt styles, model families,
full complexity of generalization, they provide a       and content domains, includes both naturalistic gen-
valuable starting point for interpreting detector be-   eration strategies (e.g., few-shot, CoT) and hand-
havior in the wild.                                     crafted prompts (1-shot CoT, self-refine).

                                                        Explaining Generalization Behavior. Several
2   Related Work
                                                        works have proposed high-level explanations for
Datasets for AI Text Detection. Recent bench-           generalization variance. For example, Xu et al.
marks have advanced AI-generated text detection         (2024) attribute success to prompt similarity and
by covering multiple languages (Wang et al., 2024a;     human–LLM alignment, while Li et al. (2024) ex-
Macko et al., 2025), domains (Li et al., 2024;          plore distributional differences using linguistic met-
Verma et al., 2024; Dugan et al., 2024), and genera-    rics like POS tags and named entity counts. How-
tor models (Hu et al., 2023; Abassy et al., 2024; Tao   ever, these studies stop short of identifying which
et al., 2024). Several works also consider mixed-       specific linguistic features correlate with general-
authorship settings (Yu et al., 2025; Zhang et al.,     ization. Our work advances this line of inquiry
2024). However, few datasets jointly evaluate the       through a detailed correlation analysis of 80 lin-
impact of LLM type, domain, and prompt style in         guistic features, covering syntactic, stylistic, and
a systematic and controlled manner. Prompt engi-        discourse-level signals. We quantify feature shifts
neering remains particularly underexplored, despite     between training and testing data and link them to
its known influence on generation behavior. To ad-      generalization performance, revealing interpretable
dress these gaps, we introduce a new dataset that       signals, e.g., shifts in pronoun frequency or passive
enables controlled experiments across 7 LLMs, 4         voice usage that influence detector robustness.
domains, and 6 prompting strategies.
                                                        3   Dataset Creation
AI Text Detection Models. Detection methods
mainly fall into two broad categories: statistical      To provide a comprehensive study of generaliza-
detectors (e.g., GLTR (Gehrmann et al., 2019), De-      tion of AI-text detectors against prompt, LLM
tectGPT (Mitchell et al., 2023), Binoculars (Hans       and dataset changes, we create our human-written
et al., 2024)) and fine-tuned classifiers using pre-    and AI-generated text dataset by incorporating 6
trained LMs (e.g., RoBERTa (Liu et al., 2019),          prompting strategies, 7 LLMs with different pa-
DeBERTa (He et al., 2021), XLM-R (Conneau               rameter sizes from different model families, and 4
                                                    6525
datasets from different domains.                        Llama 70B (Meta AI, 2024): Llama-3.3-70B-
                                                        Instruct; (4) Qwen 72B, Qwen 32B, Qwen 14B
3.1 Human-written text                                  (Yang et al., 2024): Qwen2.5-72B/-32B/-14B-
We first randomly sample the human-written text         Instruct; (5) Solar 22B (Upstage, 2024): solar-pro-
of different domains from 4 datasets: (1) Scientific    preview-instruct.
paper abstracts from the arXiv dataset (See et al.,     Prompts. We use 6 different prompting strategies
2017); (2) Product reviews from the AmazonRe-           based on existing research on prompt engineering.
views2023 dataset (Hou et al., 2024); (3) News          The prompts include: (1) 0-shot prompts that only
articles from the CNN/Daily Mail dataset (Clement       provide the metadata (e.g., title, text length) of
et al., 2019); (4) Question and answers (QA) from       each data sample; (2) 3-shot prompts (Brown et al.,
the ASQA dataset (Stelmakh et al., 2022).               2020) that contains 3 human-written texts from
   For abstracts and news articles, we use only texts   the same dataset for in-context learning; (3) Style
that are at least 1,000 characters long. We set the     prompts (Zhang et al., 2024) which require LLMs
minimum text length for reviews to 350 charac-          to write in a style like the given human-written text
ters because the original text is short. For the QA     example; (4) 0-shot CoT prompts (Kojima et al.,
dataset, we sample the longest texts considering the    2022) which consist of phrase “let’s think step by
limited size of the data. For each of the datasets,     step.”; (5) 1-shot CoT prompts (Wei et al., 2022)
we sample 3,000 examples and split them into train-     that contain manually written step-by-step instruc-
ing, validation and testing set with a split ratio of   tions, the instruction is based on an example of a
50:17:33.                                               human-written text; and (6) Self-refine prompts
                                                        (Madaan et al., 2023) that use the LLM itself to
Data cleaning for human-written text. To re-
                                                        critique and improve its own responses. Self-refine
move obvious features for AI-text detectors, we
                                                        prompts are multi-stage prompts that comprise 4
use the following data cleaning steps for all the
                                                        stages: firstly, the LLM is prompted to generate the
human-written texts: (1) Removing duplicates; (2)
                                                        AI text, then it is requested to provide feedback on
Normalizing punctuation; (3) Removing duplicated
                                                        how to make the generated AI text more human-
whitespace; (4) Removing URLs, e-mail addresses,
                                                        like. Later, the LLM needs to incorporate the feed-
and emojis; (5) Artifacts such as dates of article;
                                                        back to improve the initially generated AI text. The
(6) Filtering non-English text; (7) Filter too short
                                                        improved text is final if the LLM judges it sounds
text, as text length can impact the difficulty of the
                                                        more human-written than the human-written text
task (Wang et al., 2024b).
                                                        counterpart; otherwise, it goes back to the feedback
3.2 AI Text Generated with LLMs                         step for at most 3 iterations. For each prompting
                                                        strategy, we modified the prompt template used for
The AI-text part of the dataset consists of texts       each dataset to suit the task of text generation. To
generated by 7 LLMs using 6 diverse prompting           match the text length of the AI-generated texts to
strategies for each dataset. For each human-written     their human-written counterparts, we include in-
text, we apply every LLM and prompting strategy         formation about character count in the prompts. A
to generate an AI-text counterpart under the same       detailed discussion of the prompts can be found in
topic. Consequently, for each source dataset, the       the appendix A.1, along with the prompt templates
final data include 3,000 human-written texts and,       used to create our dataset (Table 6).
for every model–prompt combination, 3,000 corre-
sponding AI-generated texts. In total, the dataset      Data Cleaning for AI-Generated Text. To pre-
comprises 516,000 texts: 12,000 human-written           vent detectors from exploiting superficial artifacts
and 504,000 AI-text. Each AI text is matched with       rather than genuine linguistic characteristics, we
its human-written text counterpart for performing       extensively clean the LLM-generated texts by re-
a binary classification.                                moving elements that could trivially reveal their
                                                        artificial origin. Specifically, we remove formu-
LLMs. We employ LLMs with different pa-                 laic AI responses (e.g., “Certainly!”, “Sure!”),
rameter sizes and from 5 model families: (1)            structural markers such as section titles, bullet
Mistral 123B (Mistral AI, 2024): Mistral-Large-         points, and numbered lists, placeholder tokens in
Instruct-2411; (2) Deepseek 70B (DeepSeek-              square brackets (e.g., [your name], [insert e-mail
AI, 2025): DeepSeek-R1-Distill-Llama-70B; (3)           address]), extraneous metadata including review
                                                    6526
ratings, character-count information, and sentences      Cross-model (C-M) testing. This setting evalu-
beginning with “Note:” that describe the genera-         ates generalization to texts generated by LLMs not
tion process, non-linguistic symbols such as aster-      seen during training. A detector fine-tuned on the
isks (*), triple dashes (—), and hash symbols (#), as    training split from one LLM is evaluated on the test
well as model-specific tags such as \think and any       splits produced by other LLMs. For example, a de-
preceding text in Deepseek reasoning outputs. This       tector trained on abstracts generated by Llama 70B
cleaning step ensures that the evaluation focuses on     is tested on abstracts generated by all 7 LLMs. We
the linguistic properties of the generated text rather   use 0-shot prompts (p1 ) in this setting. Formally:
than on easily detectable formatting artifacts.
                                                             (g )         test     train
                                                                                           7
                                                            ∆genj = Acc M D1,c,k | D1,j,k        .          (2)
4   Generalization of AI-Text Detectors                                                      c=1


We introduce three evaluation settings to assess the       Similar to cross-prompt testing, we apply the
generalization ability of AI-text detectors across       formula to all LLMs, obtaining in a 7x7 vector as
                                                                              (g)
three dimensions: prompts, LLMs, and datasets.           cross-model results ∆gen .

4.1 Generalization Testing                               Cross-dataset (C-D) testing. This setting evalu-
Assume an AI-text detector M is fine-tuned on a          ates generalization across different dataset domains.
              train , consisting of AI-generated texts
training set Di,j,k                                      A detector fine-tuned on the training split from
produced with prompt pi by a generative model            one dataset is evaluated on test splits from other
gj for dataset dk , along with human-written texts.      datasets generated by the same LLM. For example,
We evaluate the cross-prompt, cross-model, and           a detector trained on abstracts generated by Llama
cross-dataset generalization of the AI-text detector     70B is tested on news, reviews, and QA data gen-
under the following settings.                            erated by the same LLM. We use 0-shot prompts
                                                         (p1 ) in this setting. Formally:
Cross-prompt (C-P) testing. This setting evalu-
                                                                                          4
ates how well detectors generalize to texts gen-             (d )          test
                                                            ∆genk = Acc M D1,j,c    train
                                                                                 | D1,j,k        .          (3)
                                                                                             c=1
erated with prompting strategies unseen during
training. Each detector is evaluated on test sets                                                     (d)
produced by the same LLM and drawn from the                The corresponding cross-dataset result ∆gen is a
same dataset, but generated with different prompts.      4x4 vector.
This controlled setting ensures that the only chang-
ing factor is prompt strategies during evaluation.       4.2   Training setup
For example, a detector trained on the training          We fine-tune XLM-RoBERTa-base (Conneau et al.,
split of QA texts generated by Llama 70B with            2020) (referred to as RoBERTa) and DeBERTa-
0-shot prompts is evaluated on the test split gener-     V3-small (He et al.) (referred to as DeBERTa) for
ated by Llama 70B with all 6 prompt types. For-          binary classification to distinguish between human-
mally, the accuracy of the detector on the test          written and AI-generated text. These architectures
data Dtest when trained on Dtrain is denoted as          have achieved state-of-the-art performance in prior
Acc(M (Dtest |Dtrain )). Thus, the generalization        work (Wang et al., 2024a). We train a separate
accuracies from prompt pi to all prompts are for-        detector for each combination of prompt type, AI-
malized as a list:                                       text generation model, and dataset type, resulting in
     (p )         test     train
                                   6                   168 (i.e., 7x4x6) in-domain detectors when using,
    ∆geni = Acc M Dc,j,k | Di,j,k    c=1
                                         .        (1)    for example, RoBERTa for fine-tuning.
                                                            Model fine-tuning is performed using the follow-
            (p )
   Where ∆geni is a list of 6 accuracy values, with      ing hyperparameters: learning rate = 2e-5, num
each value representing the generalization accuracy      train epochs = 3, weight decay = 0.01, train
of a prompt. We carried out the test for each prompt     batch size = 16. The maximum sequence length
and resulted in a 2-dimensional 6x6 vector (plot         is set to 512, corresponding to the maximum input
like left heatmaps in Figure 2), which presents the      length supported by XLM-RoBERTa. All our ex-
cross-prompt result of all prompts in one of the         periments are conducted on NVIDIA HGX H100,
                          (p)
conditions, denoted as ∆gen .                            and approximately 400 GPU hours to replicate.
                                                     6527
5     Explaining Generalization with                    continuous divided by the total number of words in
      Linguistic Analysis                               the text.

To better understand what causes the variance of        Lexical Analysis. As part of lexical analysis, we
generalization performance, we perform a compre-        measure the frequency of personal names, and ad-
hensive linguistic feature analysis by measuring the    jectives in comparative and superlative degrees.
correlation of 80 different feature metrics with the    The pronoun-related metrics (Okulska et al., 2023)
generation results. We first introduce the definition   analyze the differences in the usage of pronouns in
and metric of each linguistic feature and present       human-written and AI-generated text. We calculate
the correlation evaluation method.                      the frequency of specific personal or reflexive pro-
                                                        nouns and certain types of pronouns (e.g., “We”,
5.1    Linguistic Feature Definitions and Metrics       “It”, “Our”, “Yourself”).
Our studied features can be categorized into Lexi-      5.2   Correlation Between Generalization and
cal diversity, Lexical density, Sentiment, Readabil-          Linguistic Features
ity, Part-of-Speech (POS), and Grammatical and
Lexical analysis. We introduce the most correlated      To further investigate factors that influence gener-
features and metrics in the main paper and the rest     alization, we examine how changes in linguistic
in Appendix A.4.                                        features correlate with generalization performance.
                                                        For each linguistic feature f , we compute its shift
Readability. Readability refers to the ease of un-      between a given training configuration and the cor-
derstanding a text. AI-generated text tends to be       responding test configuration:
less readable than human-written text (Markowitz
et al., 2024; Mathews et al., 2024). We use the Gun-                ∆f = f (Dtrain ) − f (Dtest )       (4)
ning fog index (Yadagiri et al., 2024) as one of the
measures of readability, which is an estimated num-     where f (Dtrain ) denotes the feature difference be-
ber of years needed to understand a given passage.      tween AI-generated and human-written texts in the
                                                        training configuration (f (Dtrain ) = f (Dhuman
                                                                                                   train )−
                                                             train            test
                                                        f (DAI )), and f (D ) denotes the feature differ-
Part-of-Speech (POS). We use a selection of
metrics from StyloMetrix (Okulska et al., 2023)         ence in the corresponding test configuration. Cor-
to compare the frequency of verbs, nouns, adjec-        responding to the generalization testing, we denote
tives, numerals, etc. The frequency of parts of         the cross-prompt, cross-model, and cross-dataset
                                                                           (p)     (g)      (d)
speech is measured as the fraction of text covered      feature shift as ∆f , ∆f , and ∆f , respectively,
by tokens representing a given part of speech. Pre-     which all have the same size.
vious research has discovered differences between          We then compute the Pearson correlation be-
human-written and AI-generated text in terms of         tween flattened generalization accuracy and these
frequency of certain POS (Georgiou, 2024). There-       feature shifts under the same conditions:
fore, POS analysis is relevant for gaining insights
                                                                                          (n)   (n) 
into the literary style of texts in our dataset.                  Corr(f ) = |Pearson ∆gen , ∆f |        (5)

Grammatical Analysis. We use StyloMetrix                   where n indexes each cross-prompt, cross-
(Okulska et al., 2023) metrics to compare texts         model, or cross-dataset comparison. The result-
in terms of grammatical categories related to verbs.    ing value Corr(f ) lies in [0, 1], with 0.1 ≤
Human-written texts have been shown to contain          Corr(f ) < 0.3 indicating a low correlation, 0.3 ≤
more passive voice than AI-generated texts (Geor-       Corr(f ) < 0.5, 0.5 ≤ Corr(f ) < 0.7 and
giou, 2024). We measure the incidence of passive        Corr(f ) ≥ 0.7 as moderate, high and strong cor-
and active voice as the frequency of verbs in pas-      relations (DATAtab Team, 2025). This analysis
sive or active voice. We also compare the differ-       allows us to identify which linguistic features are
ences between the choice of tenses. The frequency       most strongly associated with robust generalization
of past, present and future tenses is measured          across different test settings.
as the fraction of the text covered by verbs in past,      Setting-specific correlation (Table 2) is mea-
present and future tenses. For example, the inci-       sured under a specific testing combination. For
dence of past tenses is the number of verbs in past     example, the setting-specific correlation of cross-
simple, past continuous, past perfect or past perfect   prompt generalization and linguistic feature shifts
                                                    6528
                                                  Cross-prompt                                                                                                Cross-model                                                                            Cross-dataset
                                                   Generalization                                                                                             Generalization                                                                          Generalization
                                                                                                                  Mistral 123B 0.97 0.97 0.97 0.97 0.97 0.97 0.97
                                                                                                        0.975
                             0-Shot 0.98 0.86 0.95 0.98 0.98 0.96                                                                                                                                                             Abstracts 0.99          0.57          0.72   0.64
                                                                                                                                                                                                                                                                                   0.95




DeBERTa-based Detectors
                                                                                                                                                                                                                      0.95


                             3-shot 0.85 0.97 0.86 0.84 0.88 0.84
                                                                                                        0.950
                                                                                                                Deepseek 70B 0.97 0.98 0.97 0.98 0.98 0.98 0.98                                                                                                                    0.90


                                                                                                        0.925
                                                                                                                   Llama 70B 0.96 0.96 0.96 0.95 0.95 0.96 0.96                                                                  News 0.60            1.00          0.89   0.84
                                                                                                                                                                                                                                                                                   0.85

                              Style 0.95 0.87 0.98 0.94 0.98 0.96                                                                                                                                                     0.90




         Train
                                                                                                        0.900
                                                                                                                    Qwen 72B 0.96 0.95 0.90 0.99 0.99 0.99 0.99                                                                                                                    0.80


                      0-shot CoT 0.98 0.86 0.95 0.98 0.98 0.96                                                                                                                                                                 Reviews 0.90           0.97          0.99   0.75
                                                                                                                    Qwen 32B 0.93 0.94 0.85 0.98 0.99 0.99 0.98
                                                                                                                                                                                                                                                                                   0.75
                                                                                                        0.875                                                                                                         0.85


                      1-shot CoT 0.95 0.85 0.95 0.94 0.99 0.94                                          0.850       Qwen 14B 0.91 0.90 0.86 0.93 0.99 0.99 0.97
                                                                                                                                                                                                                                                                                   0.70




                          Self-refine 0.95 0.81 0.94 0.95 0.95 0.99
                                                                                                                                                                                                                      0.80         QA 0.85            0.90          0.69   0.94    0.65
                                                                                                        0.825       Solar 22B 0.91 0.91 0.84 0.97 0.97 0.98 0.99
                                                                                                                                                                                                                                                                                   0.60




                                                                                                                  Mistral 123B 0.96 0.96 0.96 0.96 0.96 0.97 0.96
                                                                                                        0.975
                             0-Shot 0.98 0.88 0.95 0.97 0.98 0.96                                                                                                                                                             Abstracts 0.99          0.59          0.64   0.61
                                                                                                                                                                                                                                                                                   0.95




RoBERTa-based Detectors
                                                                                                                                                                                                                      0.95


                             3-shot 0.82 0.96 0.84 0.81 0.86 0.80
                                                                                                        0.950
                                                                                                                Deepseek 70B 0.96 0.96 0.96 0.96 0.96 0.96 0.96                                                                                                                    0.90


                                                                                                        0.925
                                                                                                                   Llama 70B 0.95 0.94 0.95 0.93 0.92 0.94 0.94                                                                  News 0.65            1.00          0.86   0.85
                                                                                                                                                                                                                                                                                   0.85

                              Style 0.94 0.89 0.97 0.93 0.97 0.94                                                                                                                                                     0.90




         Train
                                                                                                        0.900
                                                                                                                    Qwen 72B 0.97 0.96 0.92 0.99 0.99 0.99 0.99                                                                                                                    0.80


                      0-shot CoT 0.97 0.87 0.95 0.97 0.97 0.96                                                                                                                                                                 Reviews     0.89       0.94          1.00   0.68
                                                                                                                    Qwen 32B 0.86 0.88 0.76 0.93 0.99 0.99 0.97
                                                                                                                                                                                                                                                                                   0.75
                                                                                                        0.875                                                                                                         0.85


                      1-shot CoT 0.93 0.86 0.94 0.93 0.99 0.92                                          0.850       Qwen 14B 0.94 0.93 0.87 0.94 0.99 0.99 0.96
                                                                                                                                                                                                                                                                                   0.70




                          Self-refine 0.95 0.83 0.94 0.95 0.94 0.99
                                                                                                                                                                                                                      0.80         QA 0.72            0.94          0.78   0.93    0.65
                                                                                                        0.825       Solar 22B 0.91 0.91 0.81 0.97 0.97 0.98 0.99
                                                                                                                                                                                                                                                                                   0.60


                                                       Style
                                                                                         Self-refine                                                                                                      Solar 22B
                                                                                                                                                                                                                                                                           QA
                                                                                                                                                                                                                                         Abstracts
                                    0-Shot   3-shot                                                                                                                                                                                                  News
                                                               0-shot CoT   1-shot CoT                                                                       Llama 70B
                                                                                                                                                                                                                                                                Reviews
                                                                                                                               Mistral 123B
                                                                                                                                                                         Qwen 72B   Qwen 32B   Qwen 14B
                                                           Test                                                                               Deepseek 70B                                                                                                   Test
                                                                                                                                                                         Test
                                                                                                       (a) The aggregated generalization performance.
                                                      Passive voice                                     0.4
                                                                                                                             Past tenses                                                                                                             Passive voice
                             0-Shot -0.00 0.17 -0.07 0.08 -0.14 -0.30                                            Mistral 123B 0.00 0.17 0.12 0.30 0.59 0.40 0.42
                                                                                                                                                                                                                              Abstracts 0.00         -0.65      -1.44      -1.14   1.0




DeBERTa-based Detectors
                                                                                                                                                                                                                      0.4



                             3-shot -0.17 -0.00 -0.24 -0.09 -0.32 -0.48                                 0.2
                                                                                                                Deepseek 70B -0.17 0.00 -0.04 0.13 0.42 0.24 0.25
                                                                                                                                                                                                                      0.2                                                          0.5
                                                                                                                   Llama 70B -0.12 0.04 0.00 0.17 0.46 0.28 0.30                                                                 News 0.65            0.00      -0.79      -0.49
                              Style 0.07 0.24 -0.00 0.14 -0.08 -0.24



         Train
                                                                                                        0.0         Qwen 72B -0.30 -0.13 -0.17 0.00 0.29 0.11 0.12                                                    0.0                                                          0.0

                      0-shot CoT -0.08 0.09 -0.14 -0.00 -0.22 -0.38                                                                                                                                                            Reviews 1.44           0.79          0.00   0.30
                                                                                                                    Qwen 32B -0.59 -0.42 -0.46 -0.29 0.00 -0.18 -0.17                                                  0.2                                                          0.5
                      1-shot CoT 0.14 0.32 0.08 0.22 -0.00 -0.16                                         0.2
                                                                                                                    Qwen 14B -0.40 -0.24 -0.28 -0.11 0.18 0.00 0.01
                          Self-refine 0.30 0.48 0.24 0.38 0.16 -0.00                                                                                                                                                               QA 1.14            0.49      -0.30      0.00
                                                                                                                    Solar 22B -0.42 -0.25 -0.30 -0.12 0.17 -0.01 0.00
                                                                                                                                                                                                                       0.4                                                          1.0

                                                                                                         0.4



                                                      Present tenses                                                                                              'It' pronoun                                                                       Passive voice
                             0-Shot 0.00 0.68 0.19 -0.05 0.03 -0.61                                     1.0      Mistral 123B 0.00 0.03 0.01 0.06 0.08 0.07 0.06                                                      0.06
                                                                                                                                                                                                                              Abstracts 0.00         -0.65      -1.44      -1.14   1.0




RoBERTa-based Detectors
                             3-shot -0.68 0.00 -0.48 -0.73 -0.65 -1.29                                          Deepseek 70B -0.03 0.00 -0.01 0.03 0.05 0.04 0.04                                                     0.04
                                                                                                        0.5
                                                                                                                                                                                                                                                                                   0.5
                                                                                                                   Llama 70B -0.01 0.01 0.00 0.04 0.07 0.06 0.05                                                      0.02
                                                                                                                                                                                                                                 News 0.65            0.00      -0.79      -0.49
                              Style -0.19 0.48 0.00 -0.25 -0.16 -0.80



         Train
                                                                                                        0.0         Qwen 72B -0.06 -0.03 -0.04 0.00 0.02 0.02 0.01                                                    0.00                                                         0.0

                      0-shot CoT 0.05 0.73 0.25 0.00 0.08 -0.56                                                                                                                                                                Reviews 1.44           0.79          0.00   0.30
                                                                                                                    Qwen 32B -0.08 -0.05 -0.07 -0.02 0.00 -0.01 -0.02                                                  0.02
                                                                                                                                                                                                                                                                                    0.5
                      1-shot CoT -0.03 0.65 0.16 -0.08 0.00 -0.64                                        0.5

                                                                                                                    Qwen 14B -0.07 -0.04 -0.06 -0.02 0.01 0.00 -0.01                                                   0.04


                          Self-refine 0.61 1.29 0.80 0.56 0.64 0.00                                                                                                                                                                QA 1.14            0.49      -0.30      0.00
                                                                                                         1.0        Solar 22B -0.06 -0.04 -0.05 -0.01 0.02 0.01 0.00                                                   0.06
                                                                                                                                                                                                                                                                                    1.0




                                                       Style
                                                                                         Self-refine                                                                                                      Solar 22B
                                                                                                                                                                                                                                                                           QA
                                                                                                                                                                                                                                         Abstracts
                                    0-Shot   3-shot                                                                                                                                                                                                  News
                                                               0-shot CoT   1-shot CoT                                                                       Llama 70B
                                                                                                                                                                                                                                                                Reviews
                                                                                                                               Mistral 123B
                                                                                                                                                                         Qwen 72B   Qwen 32B   Qwen 14B
                                                           Test                                                                               Deepseek 70B                                                                                                   Test
                                                                                                                                                                         Test
                                                                   (b) The aggregated feature shifts between training and test configurations.

    Figure 1: Comparison of aggregated generalization performance and aggregated feature shifts across all evaluation
    settings. Similar patterns in the two heatmaps indicate that certain feature shifts are correlated with reduced
    generalization accuracy.


   is only measured on texts from Llama 70B and the                                                                                                                         Aggregation of Results. To provide a high-level
   Abstract dataset.                                                                                                                                                      summary of cross-prompt, cross-model, and cross-
      Overall correlation (Table 1) is measured under                                                                                                                     dataset generalization and feature shifts (as Figure
   all combinations. For example, the overall correla-                                                                                                                    1a and 1b), we report accuracy and shift values
   tion of cross-prompt generalization and linguistic                                                                                                                     averaged over the dimensions that are not the focus
   feature shifts is measured on the texts of every com-                                                                                                                  of the evaluation. For instance, when presenting
   bination of LLMs and datasets.                                                                                                                                         overall cross-prompt results, we average accuracy
                                                                                                                                                             6529
                                                                    DeBERTa-based                RoBERTa-based
                                      Feature Metric
                                                                  C-P    C-M         C-D        C-P    C-M        C-D
          Readability                  Gunning fog               0.056   0.248       0.231     0.043   0.308     0.261
          Part-of-Speech                 Numerals                0.108   0.363       0.086     0.076   0.157     0.031
                                       Passive voice             0.109   0.281       0.296     0.054   0.221     0.287
                                        Active voice             0.010   0.194       0.066     0.061   0.373     0.014
          Grammatical                  Present tenses            0.046   0.147       0.144     0.116   0.328     0.173
                                        Past tenses              0.018   0.416       0.031     0.006   0.324     0.049
                                       Future tenses             0.062   0.066       0.159     0.069   0.172     0.111
                                      Personal names             0.076   0.381       0.030     0.046   0.182     0.071
                              Adjectives in comparative degree   0.027   0.123       0.267     0.023   0.317     0.251
                              Adjectives in superlative degree   0.095   0.239       0.034     0.047   0.123     0.055
          Lexical                      “We” pronoun              0.014   0.041       0.015     0.108   0.030     0.037
                                        “It” pronoun             0.029   0.236       0.184     0.077   0.385     0.120
                                 “Our” possessive pronoun        0.004   0.007       0.261     0.113   0.063     0.246
                                    “Yourself” pronoun           0.030   0.183       0.157     0.061   0.366     0.111

Table 1: The overall Pearson correlation between generalization performance with different linguistic features. This
table only presents the features that fall into the top 3 correlated features in one of the settings, more results are shown
in Table 8 (Appendix). The significant (p<0.05) correlation is bolded. We underline the strongest correlation for
each setting, and italicize the other scores within the top 3 correlated features. The results of other features that are
less correlated are shown in the Appendix.

                                      DeBERTa-based                                          RoBERTa-based
                        Abstracts   News    Reviews      QA      ALL     Abstracts     News      Reviews       QA        ALL
    Mistral 123B         0.421      0.636     0.577     0.709    0.395    0.155        0.703       0.573       0.630     0.219
    Deepseek 70B         0.342      0.605     0.415     0.735    0.276    0.528        0.506       0.459       0.728     0.400
    Llama 70B            0.412      0.209     0.736     0.584    0.346    0.245        0.248       0.758       0.572     0.380
    Qwen 72B             0.072      0.590     0.317     0.301    0.098    0.128        0.519       0.549       0.357     0.212
    Qwen 32B             0.214      0.684     0.527     0.678    0.183    0.377        0.672       0.617       0.492     0.308
    Qwen 14B             0.275      0.476     0.553     0.560    0.218    0.264        0.457       0.605       0.580     0.204
    Solar 22B            0.563      0.482     0.517     0.614    0.303    0.703        0.688       0.320       0.582     0.426
    ALL                  0.196      0.231     0.437     0.255    0.109    0.246        0.155       0.486       0.224     0.116

Table 2: The cross-prompt correlation between generation performance and the most correlated linguis-
tic feature when evaluated on different datasets and models. The significant correlation is bolded. We
underline the strongest correlation for each dataset. Similar cross-model and cross-dataset results are in Appendix.


scores across all 7 LLMs and 4 datasets.                         shows only weak correlation with passive voice.
                                                                 These results highlight that some features play a
6   Results and Analysis                                         more critical role than others in determining gener-
We analyze the results in Table 1, Table 2, and                  alization success.
Figure 1 to understand how generalization perfor-                   Finding 2: Certain dataset–model combina-
mance is shaped by shifts in linguistic features.                tions reveal very strong feature dependencies.
                                                                 Although overall cross-prompt correlations appear
6.1 General Findings                                             weak in Table 1, Table 2 reveals that in specific
Finding 1: Linguistic features have significant                  configurations the effect is dramatic. For instance,
correlations with generalization results. Table 1                on Llama-70B outputs for the Reviews dataset,
shows that several features exhibit significant cor-             cross-prompt generalization is strongly correlated
relations (bold values) with detector generalization.            (>0.7) with the number of short sentences. Fig 2a
For example, overall cross-model generalization                  shows that changes in this feature align directly
that averaged across datasets is moderately cor-                 with sharp drops in performance when general-
related (0.416) with the proportion of past-tense                izing from 1-shot CoT to other prompting strate-
verbs, indicating that stylistic verb usage in training          gies. This demonstrates that some detectors are
data influences transfer. In contrast, cross-prompt              highly sensitive to prompt-induced shifts in linguis-
generalization averaged across datasets and LLMs                 tic structure.
                                                            6530
   Finding 3: Different detectors rely on dif-         accuracy when tested on news articles. Con-
ferent linguistic features. RoBERTa-based de-          versely, detectors trained on reviews or QA data
tectors and DeBERTa-based detectors do not ex-         transfer more successfully to news.
ploit the same linguistic signals. For example, the       Explanation. Across all detectors, cross-dataset
cross-model generalization of RoBERTa models is        generalization shows moderate correlation with
moderately correlated (0.385) with the frequency       passive voice usage. Abstracts exhibit a higher
of “It” pronouns, whereas for DeBERTa the corre-       rate of passive constructions, which likely makes
lation is only 0.236. This suggests that detectors     them a poor source domain for training detectors
may learn fundamentally different features for dis-    that must generalize broadly.
tinguishing human and AI text even when trained
                                                                                  Generalization                                                           Short sentences
on the same data.                                         0-Shot 0.99 0.97 0.82 0.99 0.98 0.98                                           -0.00 8.58          8.08     0.79 23.81 9.98                       20



                                                                                                                                   0.9

                                                          3-shot 0.88 0.99 0.79 0.87 0.96 0.96                                           -8.58 -0.00 -0.50 -7.79 15.23 1.40
6.2 Linguistic Analysis of Generalization
                                                                                                                                                                                                            10



                                                           Style 0.77 0.93 0.94 0.75 0.95 0.95                                     0.8
                                                                                                                                         -8.08 0.50 -0.00 -7.29 15.74 1.90
    Results                                            0-shot CoT 0.99 0.98 0.80 0.99 0.99 0.99                                          -0.79 7.79          7.29 -0.00 23.03 9.19
                                                                                                                                                                                                            0


                                                                                                                                   0.7




Figure 4 summarizes average performance across         1-shot CoT 0.52 0.51 0.60 0.52 1.00 0.77
                                                                                                                                   0.6
                                                                                                                                         -23.81 -15.23 -15.74 -23.03 -0.00 -13.83                               10




the three generalization settings. As expected,        Self-refine 0.84 0.88 0.79 0.81 0.99 0.99                                         -9.98 -1.40 -1.90 -9.19 13.83 -0.00                                    20




in-domain testing achieves near-perfect accu-
                                                                                           (a) Llama 70B, Reviews
racy, as shown in the diagonal cells of Figure 1a,                                Generalization                                                            'We' pronoun
confirming the strong baseline capabilities of our
                                                                                                                                                                                                            1.0
                                                          0-Shot 0.98 0.85 0.98 0.98 0.98 0.96                                           0.00     1.13 -0.05 -0.04 0.22                        0.18
                                                                                                                                   0.9


detectors. Detailed in-domain results are reported        3-shot 0.55 1.00 0.52 0.56 0.52 0.76                                           -1.13 0.00 -1.18 -1.17 -0.92 -0.95                                 0.5




in Table 7 in the Appendix.                                Style 0.97 0.86 0.97 0.97 0.97 0.95                                     0.8
                                                                                                                                         0.05     1.18       0.00    0.01         0.27         0.23
                                                                                                                                                                                                            0.0

                                                       0-shot CoT 0.99 0.81 0.98 0.99 0.99 0.96                                          0.04     1.17 -0.01 0.00                 0.26         0.22

6.2.1 Cross-prompt Generalization
                                                                                                                                   0.7


                                                       1-shot CoT 0.99 0.82 0.98 0.98 0.99 0.95                                          -0.22 0.92 -0.27 -0.26 0.00 -0.04                                   0.5




The most striking pattern is that the 3-shot prompt
                                                                                                                                   0.6
                                                       Self-refine 0.98 0.97 0.97 0.98 0.98 0.98                                         -0.18 0.95 -0.23 -0.22 0.04                           0.00
                                                                                                                                                                                                             1.0



is consistently the hardest to generalize to and                                   Style                                                                    Style
                                                                                                                     Self-refine                                                              Self-refine
                                                                0-Shot   3-shot                                                          0-Shot   3-shot
                                                                                           0-shot CoT   1-shot CoT                                                  0-shot CoT   1-shot CoT
from, with accuracy dropping to 80–89%. Other
prompting strategies show relatively minor effects.                                  (b) Deepseek 70B, Abstracts
   Explanation. Figure 1b shows averaged fea-
                                                       Figure 2: Cross-prompt generalization and feature shifts
ture shifts, but strong effects can be masked by
                                                       when evaluating on a specific model and dataset. A
aggregation. For example, Figure 2b highlights a       clearer and stronger correlation is observed than the
clear pattern: AI texts that use the “We” pronoun in   overall cross-prompt correlation in Figure 1. We also
similar contexts are more difficult to generalize to   show the specific case study of the generated texts for
for the detectors. This confirms Findings 2 and 3:     the above two settings in Table 9 and 10 in the Ap-
when we zoom in on specific dataset–model pairs,       pendix.
clear linguistic drivers of generalization emerge.

6.2.2 Cross-model Generalization                       6.3      Robustness Study
A major finding is that detectors trained on           We conduct the robustness study using multiple-
Qwen or Solar outputs perform poorly on                hypothesis corrections (Bonferroni (Goeman and
Llama-generated text, whereas generalization           Solari, 2014) and Benjamini–Hochberg FDR (Bog-
across other LLMs is more stable.                      dan et al., 2008)), and further including Spear-
   Explanation. Figures 1a and 1b reveal that          man (non-linear) correlations (Ali Abd Al-Hameed,
cross-model generalization is moderately influ-        2022). The results are shown in Table 3, we find
enced by shifts in past-tense usage and “It” pronoun   that:
frequency. Qwen and Solar outputs share similar          (1) Key linguistic correlates (pronoun usage,
linguistic profiles, which diverge from Llama’s, ex-   verb tense, active/passive voice) remain robust for
plaining this degradation.                             cross-prompt and cross-model generalization.
                                                         (2) A substantial number of features (>=15) re-
6.2.3 Cross-dataset Generalization                     main significant in cross-model settings across var-
The most pronounced performance gap appears            ious settings.
here: detectors trained on abstracts generalize          (3) Non-linear effects emerge under Spearman
poorly to other datasets, achieving as low as 57%      correlations, strengthening our interpretation of de-
                                                   6531
                                         DeBERTa-based                              RoBERTa-based
                                   C-P              C-M          C-D        C-P               C-M            C-D
                Bonferroni          2                15           0          3                 28             0
                  FDR               2                37           0          6                 58             0
    Pearson
                               Numerals           Past tense           “Our” pronoun       “It” pronoun
               Top features   Passive voice     Personal names    –     Present tense      Active voice       –
                                                   Numerals            “We” pronoun     “Yourself” pronoun
                Bonferroni          3                16           0          2                 25             0
                  FDR               4                44           0          10                51             0
    Spearman
                              “She” pronoun       MATTR                “She” pronoun      Active voice
               Top features    “He” pronoun       FLESCH          –    “Her” pronoun      “It” pronoun        –
                              short sentences    Gunning Fog            Present tense    Function words

Table 3: Robustness study of applying multiple-hypothesis correction to Pearson (linear) and Spearman (non-linear)
correlation. The numerical values represent the number of features that remain significant after the multiple-
hypothesis correction.


tector behavior.                                             ing diverse prompts, LLMs, and domains, we show
   (4) For cross-dataset generalization, no individ-         that state-of-the-art detectors, despite near-perfect
ual features remain significant under strict multiple-       in-domain accuracy, often struggle in cross-prompt,
hypothesis correction, suggesting that performance           cross-model, and cross-dataset scenarios. To ex-
degradation is likely driven by broader distribu-            plain these generalization behaviors, we quantify
tional shifts rather than a single dominant linguistic       shifts in 80 linguistic features between training
cue.                                                         and testing distributions and uncover statistically
   Importantly, our main conclusions remain valid            significant correlations between feature shifts and
after these robustness checks.                               generalization performance.
                                                                Our analysis reveals that features such as pro-
6.4 Discussion                                               noun usage, verb tense, and passive voice are pre-
While our analysis highlights the role of linguistic         dictive of generalization gaps, but their influence
features in explaining the generalization behavior           varies across detectors and settings. This suggests
of AI-text detectors, we acknowledge that these              that detectors latch onto different linguistic signals
features represent only one facet of a more com-             depending on their training context, impacting their
plex landscape. Generalization performance is                robustness in different testing scenarios.
likely influenced by a broader set of factors, in-              These findings underscore two key points: (1)
cluding semantic coherence, discourse structure,             evaluation must extend beyond in-domain testing
and detector-specific inductive biases. Our find-            to realistically assess detector reliability, and (2)
ings should therefore be interpreted as offering a           linguistic analysis provides a principled and inter-
linguistic perspective rather than a comprehensive           pretable path toward diagnosing and improving
account of generalization. Nonetheless, by system-           generalization.
atically correlating linguistic feature shifts with de-
tection performance, our study contributes valuable          Limitations
insights into how stylistic and grammatical signals
                                                             While our work offers new insights into the gen-
may impact detector robustness across prompts,
                                                             eralization behavior of AI-text detectors through
models, and domains.
                                                             linguistic analysis, several limitations remain.
7    Conclusion                                                 First, our study focuses on English-language text
                                                             and detectors trained on English corpora. Although
This work presents an interpretable investigation            our methodology can be extended to multilingual
into the generalization behavior of AI-text detec-           settings, the linguistic features and generalization
tors. While prior studies primarily report detection         patterns may differ significantly across languages
performance, we go further by examining why gen-             due to variations in grammar and stylistic conven-
eralization succeeds or fails through a linguistic           tions.
lens. Across a large-scale benchmark incorporat-                Second, we rely on surface-level linguistic fea-
                                                          6532
tures (e.g., POS tags, sentence length, voice, pro-              Journal of Nonlinear Analysis and Applications,
nouns) that can be extracted using standard NLP                  13(1):3249–3255.
tools. While these features provide interpretable
                                                              Amrita Bhattacharjee, Raha Moraffah, Joshua Garland,
signals, they may not capture deeper semantic or               and Huan Liu. 2024. Eagle: A domain generalization
discourse-level properties that also influence detec-          framework for ai-generated text detection. ArXiv,
tor decisions.                                                 abs/2403.15690.
   Third, the detectors we evaluate are based
                                                              Małgorzata Bogdan, Jayanta K Ghosh, Surya T Tokdar,
on fine-tuned encoder-only transformer models.                 et al. 2008. A comparison of the benjamini-hochberg
Other architectures, such as generative or retrieval-          procedure with some bayesian rules for multiple
augmented models, may exhibit different general-               testing. In Beyond parametrics in interdisciplinary
ization behaviors and rely on alternative linguistic           research: Festschrift in honor of Professor Pranab K.
                                                               Sen, volume 1, pages 211–231. Institute of Mathe-
features.                                                      matical Statistics.
   Fourth, our correlation-based analysis reveals
associations but does not establish causal relation-          Tom Brown, Benjamin Mann, Nick Ryder, Melanie
ships between feature shifts and performance drops.             Subbiah, Jared D Kaplan, Prafulla Dhariwal, Arvind
                                                                Neelakantan, Pranav Shyam, Girish Sastry, Amanda
Further research using controlled interventions or              Askell, Sandhini Agarwal, Ariel Herbert-Voss,
counterfactual examples would be needed to verify               Gretchen Krueger, Tom Henighan, Rewon Child,
causality.                                                      Aditya Ramesh, Daniel Ziegler, Jeffrey Wu, Clemens
   Lastly, our dataset covers a wide but still limited          Winter, Chris Hesse, Mark Chen, Eric Sigler, Ma-
                                                                teusz Litwin, Scott Gray, Benjamin Chess, Jack
set of domains, models, and prompting strategies.
                                                                Clark, Christopher Berner, Sam McCandlish, Alec
As the landscape of LLMs and prompting meth-                    Radford, Ilya Sutskever, and Dario Amodei. 2020.
ods continues to evolve, future work should assess              Language models are few-shot learners. In Advances
whether our findings hold for more recent or unseen             in Neural Information Processing Systems, vol-
generation techniques.                                          ume 33, pages 1877–1901. Curran Associates, Inc.
   Despite these limitations, our study provides a            Colin B. Clement, Matthew Bierbaum, Kevin P.
strong foundation for more principled and inter-                O’Keeffe, and Alexander A. Alemi. 2019. On the
pretable evaluations of generalization in AI-text               use of arxiv as a dataset. ArXiv, abs/1905.00075.
detection.
                                                              Alexis Conneau, Kartikay Khandelwal, Naman Goyal,
                                                                Vishrav Chaudhary, Guillaume Wenzek, Francisco
Acknowledgments                                                 Guzmán, Edouard Grave, Myle Ott, Luke Zettle-
This research has been funded by the                            moyer, and Veselin Stoyanov. 2020. Unsupervised
                                                                cross-lingual representation learning at scale. In
Vienna Science and Technology Fund                              Proceedings of the 58th Annual Meeting of the
(WWTF)[10.47379/VRG19008]      “Knowledge                       Association for Computational Linguistics, pages
infused Deep Learning for Natural Language                      8440–8451, Online. Association for Computational
Processing”.                                                    Linguistics.

                                                              Michael A. Covington and Joe D. McFall. 2010. Cutting
                                                                the gordian knot: The moving-average type–token
References                                                      ratio (mattr). Journal of Quantitative Linguistics,
Mervat Abassy, Kareem Elozeiri, Alexander Aziz,                 17(2):94–100.
 Minh Ngoc Ta, Raj Vardhan Tomar, Bimarsha Ad-
 hikari, Saad El Dine Ahmed, Yuxia Wang, Osama                DATAtab Team. 2025. Pearson correlation: A be-
 Mohammed Afzal, Zhuohan Xie, Jonibek Mansurov,                 ginner’s guide. https://datatab.net/tutorial/
 Ekaterina Artemova, Vladislav Mikhailov, Rui Xing,             pearson-correlation. DATAtab: Online Statistics
 Jiahui Geng, Hasan Iqbal, Zain Muhammad Mujahid,               Calculator. DATAtab e.U., Graz, Austria.
 Tarek Mahmoud, Akim Tsvigun, Alham Fikri Aji,
 Artem Shelmanov, Nizar Habash, Iryna Gurevych,               DeepSeek-AI. 2025. Deepseek-r1: Incentivizing rea-
 and Preslav Nakov. 2024. LLM-DetectAIve: a tool                soning capability in llms via reinforcement learning.
 for fine-grained machine-generated text detection. In          Preprint, arXiv:2501.12948.
 Proceedings of the 2024 Conference on Empirical
 Methods in Natural Language Processing: System               Heather Desaire, Aleesa E. Chua, Madeline Isom, Ro-
 Demonstrations, pages 336–343, Miami, Florida,                 mana Jarosova, and David Hua. 2023. Distinguish-
 USA. Association for Computational Linguistics.                ing academic science writing from humans or chat-
                                                                gpt with over 99% accuracy using off-the-shelf ma-
Khawla Ali Abd Al-Hameed. 2022. Spearman’s corre-               chine learning tools. Cell Reports Physical Science,
  lation coefficient in statistical analysis. International     4(6):101426.
                                                          6533
Liam Dugan, Alyssa Hwang, Filip Trhlík, Andrew             Takeshi Kojima, Shixiang Shane Gu, Machel Reid, Yu-
  Zhu, Josh Magnus Ludan, Hainiu Xu, Daphne Ip-              taka Matsuo, and Yusuke Iwasawa. 2022. Large
  polito, and Chris Callison-Burch. 2024. RAID:              language models are zero-shot reasoners.         In
  A shared benchmark for robust evaluation of                Proceedings of the 36th International Conference on
  machine-generated text detectors. In Proceedings           Neural Information Processing Systems, NIPS ’22.
  of the 62nd Annual Meeting of the Association
  for Computational Linguistics (Volume 1: Long            Yafu Li, Qintong Li, Leyang Cui, Wei Bi, Zhilin
  Papers), pages 12463–12492, Bangkok, Thailand.             Wang, Longyue Wang, Linyi Yang, Shuming
  Association for Computational Linguistics.                 Shi, and Yue Zhang. 2024. MAGE: Machine-
                                                             generated text detection in the wild. In Proceedings
Sebastian Gehrmann, Hendrik Strobelt, and Alexan-            of the 62nd Annual Meeting of the Association
  der Rush. 2019. GLTR: Statistical detection and            for Computational Linguistics (Volume 1: Long
  visualization of generated text. In Proceedings of         Papers), pages 36–53, Bangkok, Thailand. Associ-
  the 57th Annual Meeting of the Association for             ation for Computational Linguistics.
  Computational Linguistics: System Demonstrations,
  pages 111–116, Florence, Italy. Association for Com-     Yinhan Liu, Myle Ott, Naman Goyal, Jingfei Du, Man-
  putational Linguistics.                                    dar Joshi, Danqi Chen, Omer Levy, Mike Lewis,
Georgios P. Georgiou. 2024. Differentiating between          Luke Zettlemoyer, and Veselin Stoyanov. 2019.
  human-written and ai-generated texts using linguis-        Roberta: A robustly optimized bert pretraining ap-
  tic features automatically extracted from an online        proach. Preprint, arXiv:1907.11692.
  computational tool. Inf., 16:979.
                                                           Zeyan Liu, Zijun Yao, Fengjun Li, and Bo Luo. 2024.
Jelle J. Goeman and Aldo Solari. 2014. Multiple hy-          On the detectability of chatgpt content: Bench-
   pothesis testing in genomics. Statistics in medicine,     marking, methodology, and evaluation through the
   33(11):1946–1978.                                         lens of academic writing. In Proceedings of the
                                                             2024 on ACM SIGSAC Conference on Computer
Biyang Guo, Xin Zhang, Ziyuan Wang, Minqi Jiang,             and Communications Security, CCS ’24, page
  Jinran Nie, Yuxuan Ding, Jianwei Yue, and Yupeng           2236–2250, New York, NY, USA. Association for
  Wu. 2023. How close is chatgpt to human experts?           Computing Machinery.
  comparison corpus, evaluation, and detection. ArXiv,
  abs/2301.07597.                                          Dominik Macko, Jakub Kopál, Robert Moro, and Ivan
                                                             Srba. 2025. MultiSocial: Multilingual benchmark
Xun Guo, Yongxin He, Shan Zhang, Ting Zhang,
                                                             of machine-generated text detection of social-media
  Wanquan Feng, Haibin Huang, and Chongyang Ma.
                                                             texts. In Proceedings of the 63rd Annual Meeting
  2024. Detective: Detecting ai-generated text via
                                                             of the Association for Computational Linguistics
  multi-level contrastive learning. Advances in Neural
                                                             (Volume 1: Long Papers), pages 727–752, Vienna,
  Information Processing Systems, 37:88320–88347.
                                                             Austria. Association for Computational Linguistics.
Abhimanyu Hans, Avi Schwarzschild, Valeriia
  Cherepanova, Hamid Kazemi, Aniruddha Saha,               Dominik Macko, Robert Moro, Adaku Uchendu, Ja-
  Micah Goldblum, Jonas Geiping, and Tom Goldstein.          son Samuel Lucas, Michiharu Yamashita, Matúš
  2024. Spotting llms with binoculars: zero-shot             Pikuliak, Ivan Srba, Thai Le, Dongwon Lee, Jakub
  detection of machine-generated text. In Proceedings        Simko, and Maria Bielikova. 2023. MULTITuDE:
  of the 41st International Conference on Machine            Large-Scale Multilingual Machine-Generated Text
  Learning, ICML’24. JMLR.org.                               Detection Benchmark.       In Proceedings of the
                                                             2023 Conference on Empirical Methods in Natural
Pengcheng He, Jianfeng Gao, and Weizhu Chen. De-             Language Processing, pages 9960–9987.
  bertav3: Improving deberta using electra-style pre-
  training with gradient disentangled embedding shar-      Aman Madaan, Niket Tandon, Prakhar Gupta, Skyler
  ing. ICLR 2023.                                           Hallinan, Luyu Gao, Sarah Wiegreffe, Uri Alon,
                                                            Nouha Dziri, Shrimai Prabhumoye, Yiming Yang,
Pengcheng He, Xiaodong Liu, Jianfeng Gao, and               Shashank Gupta, Bodhisattwa Prasad Majumder,
  Weizhu Chen. 2021. Deberta: Decoding-enhanced             Katherine Hermann, Sean Welleck, Amir Yazdan-
  bert with disentangled attention. In International        bakhsh, and Peter Clark. 2023. Self-refine: itera-
  Conference on Learning Representations.                   tive refinement with self-feedback. In Proceedings
Yupeng Hou, Jiacheng Li, Zhankui He, An Yan, Xiusi          of the 37th International Conference on Neural
  Chen, and Julian McAuley. 2024. Bridging language         Information Processing Systems, NIPS ’23.
  and items for retrieval and recommendation. ArXiv,
  abs/2403.03952.                                          Anastasia Margolina and Anastasia Kolmogorova.
                                                             2023. Exploring Evaluation Techniques in Con-
Xiaomengc Hu, Pin-Yu Chen, and Tsung-Yi Ho.                  trolled Text Generation: A Comparative Study
  2023. Radar: robust ai-text detection via ad-              of Semantics and Sentiment in ruGPT3large-
  versarial learning. In Proceedings of the 37th             Generated and Human-Written Movie Reviews.
  International Conference on Neural Information             In COMPUTATIONAL LINGUISTICS AND
  Processing Systems, NIPS ’23.                              INTELLECTUAL TECHNOLOGIES”. RSUH.
                                                       6534
David M. Markowitz, Jeffrey T. Hancock, and Jeremy N.      Ivan Stelmakh, Yi Luan, Bhuwan Dhingra, and Ming-
  Bailenson. 2024. Linguistic markers of inher-              Wei Chang. 2022.       ASQA: Factoid questions
  ently false ai communication and intentionally false        meet long-form answers. In Proceedings of the
  human communication: Evidence from hotel re-                2022 Conference on Empirical Methods in Natural
  views. Journal of Language and Social Psychology,           Language Processing, pages 8273–8288, Abu Dhabi,
  43(1):63–82.                                                United Arab Emirates. Association for Computa-
                                                              tional Linguistics.
Daniel Mathews, Justin P Varghese, and Libin Chacko
  Samuel. 2024. Classifying ai-generated summaries         Zhen Tao, Zhiyu Li, Dinghao Xi, and Wei Xu. 2024.
  and human summaries based on statistical fea-              CUDRT: Benchmarking the Detection of Human vs.
  tures. In 2024 International Conference on Trends          Large Language Models Generated Texts. arXiv
  in Quantum Computing and Emerging Business                 preprint. ArXiv:2406.09056 [cs].
  Technologies, pages 1–5.
                                                           Upstage. 2024.          Solar pro preview in-
                                                             struct.     https://huggingface.co/upstage/
Akshay Mendhakar and Darshan H S. 2023. Parts-
                                                             solar-pro-preview-instruct. Instruction-tuned
  of-speech (pos) analysis and classification of var-
                                                             22B-parameter LLM optimized for single-GPU
  ious text genres. Corpus-based Studies across
                                                             performance. Preview released September 2024.
  Humanities, 1(1):99–131.
                                                           Vivek Verma, Eve Fleisig, Nicholas Tomlin, and Dan
Meta AI. 2024. Introducing meta llama 3: The most            Klein. 2024. Ghostbuster: Detecting text ghostwrit-
 capable openly available llm to date. Accessed: 2025-       ten by large language models. In Proceedings of
 05-01.                                                      the 2024 Conference of the North American Chapter
                                                             of the Association for Computational Linguistics:
Mistral AI. 2024. Mistral large instruct 2411. Accessed:     Human Language Technologies (Volume 1: Long
  2025-05-01.                                                Papers), pages 1702–1717, Mexico City, Mexico. As-
                                                             sociation for Computational Linguistics.
Eric Mitchell, Yoonho Lee, Alexander Khazatsky,
  Christopher D. Manning, and Chelsea Finn. 2023.          Yuxia Wang, Jonibek Mansurov, Petar Ivanov, Jinyan
  Detectgpt: zero-shot machine-generated text detec-         Su, Artem Shelmanov, Akim Tsvigun, Osama Mo-
  tion using probability curvature. In Proceedings           hammed Afzal, Tarek Mahmoud, Giovanni Puc-
  of the 40th International Conference on Machine            cetti, Thomas Arnold, Alham Aji, Nizar Habash,
  Learning, ICML’23. JMLR.org.                               Iryna Gurevych, and Preslav Nakov. 2024a. M4GT-
                                                             bench: Evaluation benchmark for black-box machine-
Alberto Muñoz-Ortiz, Carlos Gómez-Rodríguez, and             generated text detection.      In Proceedings of
  David Vilares. 2024. Contrasting linguistic patterns       the 62nd Annual Meeting of the Association
  in human and llm-generated news text. Artificial           for Computational Linguistics (Volume 1: Long
  Intelligence Review, 57(10).                               Papers), pages 3964–3992, Bangkok, Thailand. As-
                                                             sociation for Computational Linguistics.
Inez Okulska, Daria Stetsenko, Anna Kołos, Agnieszka
   Karlińska, Kinga Gł ˛
                       abińska, and Adam Nowakowski.      Yuxia Wang, Jonibek Mansurov, Petar Ivanov, Jinyan
   2023. Stylometrix: An open-source multilingual            Su, Artem Shelmanov, Akim Tsvigun, Chenxi
   tool for representing stylometric vectors. Preprint,      Whitehouse, Osama Mohammed Afzal, Tarek Mah-
   arXiv:2309.12810.                                         moud, Toru Sasaki, Thomas Arnold, Alham Fikri
                                                             Aji, Nizar Habash, Iryna Gurevych, and Preslav
                                                             Nakov. 2024b.       M4: Multi-generator, multi-
Chidimma Opara. 2024.          Styloai: Distinguish-
                                                             domain, and multi-lingual black-box machine-
  ing ai-generated content with stylometric anal-
                                                             generated text detection. In Proceedings of the
  ysis.     In Artificial Intelligence in Education.
                                                             18th Conference of the European Chapter of the
  Posters and Late Breaking Results, Workshops
                                                             Association for Computational Linguistics (Volume
  and Tutorials, Industry and Innovation Tracks,
                                                             1: Long Papers), pages 1369–1407, St. Julian’s,
  Practitioners, Doctoral Consortium and Blue Sky,
                                                             Malta. Association for Computational Linguistics.
  pages 105–114, Cham. Springer Nature Switzerland.
                                                           Jason Wei, Xuezhi Wang, Dale Schuurmans, Maarten
Jacques Savoy. 2020. Machine Learning Methods                 Bosma, Brian Ichter, Fei Xia, Ed H. Chi, Quoc V. Le,
   for Stylometry: Authorship Attribution and Author          and Denny Zhou. 2022. Chain-of-thought prompt-
   Profiling. Springer International Publishing, Cham.        ing elicits reasoning in large language models. In
                                                              Proceedings of the 36th International Conference on
Abigail See, Peter J. Liu, and Christopher D. Man-            Neural Information Processing Systems, NIPS ’22.
  ning. 2017. Get to the point: Summarization
  with pointer-generator networks. In Proceedings          Han Xu, Jie Ren, Pengfei He, Shenglai Zeng, Yingqian
  of the 55th Annual Meeting of the Association              Cui, Amy Liu, Hui Liu, and Jiliang Tang. 2024.
  for Computational Linguistics (Volume 1: Long              On the generalization of training-based ChatGPT
  Papers), pages 1073–1083, Vancouver, Canada. As-           detection methods. In Findings of the Association
  sociation for Computational Linguistics.                   for Computational Linguistics: EMNLP 2024, pages
                                                       6535
    7223–7243, Miami, Florida, USA. Association for         steps (Wei et al., 2022). A chain-of-thought prompt
    Computational Linguistics.                              usually relies on exemplars, containing a prompt
Annepaka Yadagiri, Lavanya Shree, Suraiya Parween,          and a correct response. The example response is
  Anushka Raj, Shreya Maurya, and Partha Pakray.            expressed as a series of steps that lead to a final
  2024. Detecting AI-generated text with pre-trained        output. This prompts the model to reason step-by-
  models using linguistic features. In Proceedings
                                                            step.
  of the 21st International Conference on Natural
  Language Processing (ICON), pages 188–196, AU-               For the purpose of our dataset, we adapt a 1-shot
  KBC Research Centre, Chennai, India. NLP Associa-         CoT prompting strategy to the task of text gener-
  tion of India (NLPAI).                                    ation: this prompt subtype consists of a human-
An Yang, Baosong Yang, Beichen Zhang, Binyuan Hui,          written step-by-step instruction for the model. The
  Bo Zheng, Bowen Yu, Chengyuan Li, Dayiheng Liu,           instruction is based on an example of a human-
  Fei Huang, Haoran Wei, Huan Lin, Jian Yang, Jian-
                                                            written text from the dataset.
  hong Tu, Jianwei Zhang, Jianxin Yang, Jiaxi Yang,
  Jingren Zhou, Junyang Lin, Kai Dang, Keming Lu,              We also use 0-shot CoT prompts (Kojima et al.,
  Keqin Bao, Kexin Yang, Le Yu, Mei Li, Mingfeng            2022), which consist of adding let’s think step by
  Xue, Pei Zhang, Qin Zhu, Rui Men, Runji Lin, Tian-        step to the baseline prompt to cause step-by-step
  hao Li, Tianyi Tang, Tingyu Xia, Xingzhang Ren,
  Xuancheng Ren, Yang Fan, Yang Su, Yichang Zhang,          reasoning.
  Yu Wan, Yuqiong Liu, Zeyu Cui, Zhenru Zhang, and             Few-shot In-context learning (3-shot) (Brown
  Zihan Qiu. 2024. Qwen2.5 technical report. arXiv          et al., 2020): The few-shot prompt contains several
  preprint arXiv:2412.15115.
                                                            examples of input-output pairs for a given task.
Hatice Yildiz Durak, Figen Eğin, and Aytuğ Onan.          Our few-shot prompts include three human-written
  2025. A Comparison of Human-Written Versus AI-            examples from the dataset.
  Generated Text in Discussions at Educational Set-
  tings: Investigating Features for ChatGPT, Gem-              Style examples (Style): In Zhang et al. (2024),
  ini and BingAI. European Journal of Education,            prompts with style guidelines have been effective
  60(1):e70014.                                             in prompting LLMs to generate output that evades
Peipeng Yu, Jiahan Chen, Xuan Feng, and Zhihua Xia.         detection methods, and models have been prompted
  2025. Cheat: A large-scale dataset for detecting          to simulate the styles of several famous writers. We
  chatgpt-written abstracts. IEEE Transactions on Big       adapt one of the prompts from Zhang et al. (2024)
  Data, 11(3):898–906.
                                                            for our task. Specifically, we use the style exam-
Sergio E. Zanotto and Segun Aroyehun. 2024. Human           ple prompt, but with an example from the human-
  variability vs. machine consistency: A linguistic anal-   written part of our dataset. Even though using a text
  ysis of texts generated by humans and large language
  models. Preprint, arXiv:2412.03025.                       written by a famous author (e.g., Shakespeare) as
                                                            a style example has been successful in preventing
Yuehan Zhang, Yongqiang Ma, Jiawei Liu, Xiaozhong           detection (Zhang et al., 2024), our prompt modi-
  Liu, Xiaofeng Wang, and Wei Lu. 2024. Detection
  vs. anti-detection: Is text generated by ai detectable?   fication aims to create a more realistic setting to
  In Wisdom, Well-Being, Win-Win, pages 209–222,            adapt to different datasets.
  Cham. Springer Nature Switzerland.                           Self-refine (Madaan et al., 2023): Self-
A     Appendix                                              refinement prompts are prompts that use the LLM
                                                            itself to critique and improve its own responses.
A.1 Overview of prompting techniques                        The prompts of this kind are comprised of three
To test diverse prompting techniques, we chose six          stages: generating the output, generating feedback
different prompt types. The prompt types are:               for the output and applying the feedback to the out-
   0-shot: Our zero-shot prompts are simple in-             put. The second and third steps are repeated until
structions for the language models that include a           a stopping condition is met. In this case, we base
basic piece of information about the text and de-           the stopping condition on the ability of the model
sired length of the text. For example, the template         itself to distinguish its own outputs from human-
for the prompt to generate abstracts is Write an            written text. To achieve this, we use evaluation
abstract for an article titled “{title}”. The abstract      prompts based on the GPT-4 evaluation prompt
should be around {length} characters long.                  used in (Madaan et al., 2023). For the purpose of
   Chain-of-Thought (0-shot CoT): Chain-of-                 our task, we ask the model to decide which text
thought prompting is a strategy that aims to im-            sounds more human-written. The resulting set of
prove reasoning by dividing the task into smaller           prompts is made of the following stages:
                                                        6536
   • Initialization prompt: the same as our baseline     Polarity is a score between -1 and 1, where -1 de-
     zero-shot prompt.                                   notes a negative sentiment, while 1 denotes a posi-
                                                         tive sentiment. Subjectivity relates to the amount
   • Feedback prompt: prompt used for generating         of personal opinion included in the text.
     feedback on how to make the text seem more
     human-written.                                      Readability. Readability refers to the ease of un-
                                                         derstanding a text. AI-generated text tends to be
   • Iterate prompt: used to get the next iteration      less readable than human-written text (Yadagiri
     if the model classifies its generated text as AI.   et al., 2024; Markowitz et al., 2024; Mathews et al.,
                                                         2024). We use the Gunning fog index and the
   • Evaluate prompt: used to check whether the          Flesch reading ease test as measures of readabil-
     stopping condition (the model classifies the        ity. The Gunning fog index is an estimated number
     text as human-written) has been met.                of years needed to understand a given passage. The
                                                         Flesch reading ease test is a metric of readability,
A.2 Prompt templates
                                                         in which texts that are easier to read receive a higher
We demonstrate detailed prompts used in the paper        score. In the analysis of readability, we also include
in Table 6.                                              the text length in characters, as well as sentence
                                                         length statistics. Machine-generated text tends to
A.3 Detailed classification results
                                                         be less varied than human-written text in terms of
The results of the detailed in-domain accuracy are       sentence length (Desaire et al., 2023; Muñoz-Ortiz
shown in Table 7.                                        et al., 2024). Following (Desaire et al., 2023), we
                                                         calculate the average sentence length, the stan-
A.4 Linguistic analysis                                  dard deviation from the average sentence length,
Lexical diversity. We choose Moving Average              and the number of very long (35 words or more)
Type-Token Ratio to measure the lexical diver-           and very short (10 words or less) sentences in
sity of the texts, as it is independent of the text      each text.
length (Covington and McFall, 2010). Addition-
ally, we compare the texts in terms of the number        Part-of-Speech (POS). We use a selection of
of unique words, as this feature has been shown to       metrics from StyloMetrix (Okulska et al., 2023)
be relevant in the previous research (Opara, 2024;       to compare the frequency of verbs, nouns, adjec-
Yildiz Durak et al., 2025).                              tives, pronouns, determiners, conjunctions and nu-
                                                         merals across the different dataset types, models
Lexical density. Lexical density is the percent-         and prompts. The frequency of parts of speech is
age of content words in the text. Machine-               measured as the fraction of text covered by tokens
generated text is said to achieve higher lexical den-    representing a given part of speech. The frequency
sity (Savoy, 2020) than human-written text, which        of POS has been shown to be different across dif-
means that it contains fewer function words. The         ferent text genres, with non-fiction texts typically
content words are adjectives, adverbs, nouns, and        achieving a higher frequency of nouns than fiction
verbs.                                                   texts (Mendhakar and S, 2023). A high frequency
                                                         of verbs can be associated with more narrative texts,
Sentiment. AI-generated text has been shown to           while a high frequency of adjectives is common for
differ from human-written text in terms of senti-        more descriptive texts. Additionally, previous re-
ment: some authors have written of positivity bias       search has discovered differences between human-
present in AI-generated texts (Markowitz et al.,         written and AI-generated text in terms of frequency
2024; Muñoz-Ortiz et al., 2024; Margolina and Kol-       of certain POS (Georgiou, 2024). Therefore, POS
mogorova, 2023), which means that text generated         analysis is relevant for gaining insights into the
by large language models tends to contain more           literary style of texts in our dataset.
positive emotions compared to human-written texts.
Other research suggests that human-written texts         Grammatical analysis. We use StyloMetrix
are more varied in terms of the richness of emo-         (Okulska et al., 2023) metrics to compare texts
tional content (Zanotto and Aroyehun, 2024). We          in terms of grammatical categories related to verbs.
use the TextBlob library to calculate the polarity       In previous research, human-written texts have
and subjectivity scores for the texts in our dataset.    been shown to contain more passive voice than
                                                     6537
                                                                                                                                               (Mistral, Abstract)         (Mistral, Abstract)

    Mistral Abstract       0-shot         Mistral Abstract           0-shot                      Mistral Abstract Self-refine
                                                                                  ...
    Mistral Abstract       3-shot         Mistral Abstract           0-shot                      Mistral Abstract Self-refine
                                                                                  ...
                                                                                                                                  Train
                ...                                    ...                        ...                         ...


   Mistral Abstract Self-refine           Mistral Abstract           0-shot          ...         Mistral Abstract Self-refine


                                       Overall Cross-Prompt Correlation                                                                             Test                          Test




          (Mistral, Abstract)          (Mistral, QA)             (Mistral, Abstract)               (Mistral, QA)
                                                                                                                                                        ...                        ...
                                                                                                                         Correlation Rank
                                 ...                                                       ...
                                                                                                                         Feature 2: 0.51
                                                                                                                         Feature 80: 0.49

                                                                                                                                ...
 Corr   ( (Solar, Abstract)
                  ...                     ...                ,           ...                           ...
                                                                                                                    )                                mean                         mean
                                       (Solar, QA)               (Solar, Abstract)                  (Solar, QA)          Feature 1: 0.01

                                                                                                                        Overall cross-prompt
                                ...                                                        ...                           feature correlation
                                                                                                                              (Table 1)



                                                                                                                                                      Overall cross-prompt results (Figure 1)


               Figure 3: The workflow to get the overall cross-prompt generalization and feature shift results.

                                                  DeBERTa-based                                                                               RoBERTa-based
                          Abstracts             News Reviews    QA                                           ALL         Abstracts          News Reviews    QA                       ALL
            0-shot              0.587           0.569                 0.663                0.591             0.416         0.399            0.677        0.655         0.355        0.385

Table 4: The cross-model correlation between generation performance and the most correlated linguis- tic feature
when evaluated on different datasets.


                                 DeBERTa-based                        RoBERTa-based                                 past perfect or past perfect continuous divided by
                                    0-shot                               0-shot                                     the total number of words in the text.
  Mistral 123B                           0.310                                 0.350
  Deepseek 70B                           0.418                                 0.468                                Lexical analysis. As part of lexical analysis, we
  Llama 70B                              0.389                                 0.374                                measure the frequency of proper and personal
  Qwen 72B                               0.425                                 0.308
  Qwen 32B                               0.426                                 0.418                                names, as well as the frequency of adjectives
  Qwen 14B                               0.487                                 0.545                                and adverbs in positive, comparative and su-
  Solar 22B                              0.269                                 0.188                                perlative degrees and the frequency of nouns in
  ALL                                    0.296                                 0.287
                                                                                                                    possessive case. We use the StyloMetrix (Okul-
Table 5: The cross-dataset correlation between gener-                                                               ska et al., 2023) pronoun-related metrics to ana-
ation performance and the most correlated linguis- tic                                                              lyze the differences in the usage of pronouns in
feature when evaluated on different models.                                                                         human-written and AI-generated text, as well as
                                                                                                                    across the different prompt types, dataset types and
                                                                                                                    models. We calculate not only the frequency of
                                                                                                                    pronouns (POS_PRO), but also the frequency of
AI-generated texts (Georgiou, 2024). We measure
                                                                                                                    specific personal or reflexive pronouns and the gen-
the incidence of passive and active voice as the
                                                                                                                    eral frequency of certain types of pronouns (for
frequency of verbs in passive or active voice. We
                                                                                                                    example, the frequency of all first-person singular
also compare the differences between the choice
                                                                                                                    pronouns).
of tenses. The frequency of past, present and
future tenses is measured as the fraction of the
text covered by verbs in past, present and future
tenses. For example, the incidence of past tenses is
the number of verbs in past simple, past continuous,
                                                                                                             6538
Prompt       Dataset     Prompt template
             Abstracts   "Write an abstract for an article in {category} with a title: \"{title}\". The abstract should be around {length} characters long."
             News        "Write a news article based on the following highlights:\n\"{highlights}\"\nYour article should be around {length} characters
0-shot
                         long."
             Reviews     "Write an Amazon review for the item \"{item_name}\" with a title \"{title}\" and a rating of {rating}. The review should be
                         around {length} characters long."
             QA          "{question}\n Your answer should be around {length} characters long."
             Abstracts   "Write an abstract for an article in {category} with a title: \"{title}\". Let’s think step by step. Your answer should only include
                         the abstract. The abstract should be around {length} characters long."
0-shot CoT
             News        "Write a news article based on the following highlights:\n\"{highlights}\"\nLet’s think step by step. Your answer should only
                         include the article. The article should be around {length} characters long."
             Reviews     "Write an Amazon review for the item \"{item_name}\" with a title \"{title}\" and a rating of {rating}. Let’s think step by step.
                         Your answer should only include the review. The review should be around {length} characters long."
             QA          "{question}\nLet’s think step by step. Your answer should only include the answer to the question. The answer should be around
                         {length} characters long."
             Abstracts   "I want to write an abstract for an article in computer science. The article is titled \"ConQRet: Benchmarking Fine-Grained
                         Evaluation of Retrieval Augmented Argumentation with LLM Judges\". \n 1. First, I introduce the context of the research and
1-shot CoT
                         explain the motivation:\n\"Computational argumentation, which involves generating answers or summaries for controversial
                         topics like abortion bans and vaccination, has become increasingly important in today’s polarized environment. Sophisticated
                         LLM capabilities offer the potential to provide nuanced, evidence-based answers to such questions through Retrieval-Augmented
                         Argumentation (RAArg), leveraging real-world evidence for high-quality, grounded arguments. However, evaluating RAArg
                         remains challenging, as human evaluation is costly and difficult for complex, lengthy answers on complicated topics. At the
                         same time, re-using existing argumentation datasets is no longer sufficient, as they lack long, complex arguments and realistic
                         evidence from potentially misleading sources, limiting holistic evaluation of retrieval effectiveness and argument quality.\"\nThen,
                         I describe how I addressed the gaps in current research and give a detailed description of my methodology:\n\"To address
                         these gaps, we investigate automated evaluation methods using multiple fine-grained LLM judges, providing better and more
                         interpretable assessments than traditional single-score metrics and even previously reported human crowdsourcing. To validate
                         the proposed techniques, we introduce ConQRet, a new benchmark featuring long and complex human-authored arguments on
                         debated topics, grounded in real-world websites, allowing an exhaustive evaluation across retrieval effectiveness, argument quality,
                         and groundedness. We validate our LLM Judges on a prior dataset and the new ConQRet benchmark.\"\nFinally, I describe
                         the results and their implications for the research on this topic:\n\"Our proposed LLM Judges and the ConQRet benchmark
                         can enable rapid progress in computational argumentation and can be naturally extended to other complex retrieval-augmented
                         generation tasks.\"\nBased on the provided step-by-step instruction, write an abstract for an article in {category} titled \"{title}\"."
             News        "I want to write a news article about the following events:\nDarsh Patel, 22, was hiking with friends in the Apshawa Preserve in
                         West Milford on Sunday when a bear started following them.\nThe group fled in different directions and when the four other
                         hikers could not find Patel, they called police.\nPatel’s body was found two hours later.\nThe 300-pound bear was circling
                         the body and could not be scared away.\nIt was shot dead in accordance with Division of Fish and Wildlife guidelines.\nOn
                         Saturday locals splitting wood filmed a bear rifling through their garbage.\n\n\nFirst, I introduce the event and its content to the
                         readers:\nLocals in northern New Jersey believe they filmed a black bear hunting for food hours before a 22-year-old hiker was
                         mauled to death in nearby woods at the weekend. Two men splitting wood on Saturday captured a video of a bear going through
                         garbage just a few feet from where they were working, before scampering off into the woods, according to CNN. On Sunday,
                         Darsh Patel, a senior majoring in information technology and informatics at Rutgers University, was found dead in Apshawa
                         Preserve - about 45 miles northwest of New York City - with a 300-pound bear guarding his body. Officials say the attack was the
                         first fatal bear-human encounter on record in New Jersey. Just a day after the footage was shot, a black bear mauled a 22-year-old
                         student to death in the woods nearby.\nThen, I provide more details related to the event:\nPatel had been hiking with four friends
                         in the 526-acre woods. The five friends noticed the bear beginning to follow them and ran, splitting up as they did. When they
                         couldn’t find Patel, they called police, who found his body about two hours later. The bear was about 30 yards from the body and
                         circling, Department of Environmental Protection spokesman Larry Ragonese said, and wouldn’t leave even after officers tried to
                         scare it away by making loud noises and throwing sticks and stones. The male bear was killed with two rifle blasts and is being
                         examined at a state lab for more clues as to why it may have pursued the group of five hikers.\nThen, I provide opinions on the
                         event, quoting officials, experts or witnesses of the event:\nKelcey Burguess, principal biologist and leader of the state Division of
                         Fish and Wildlife’s black bear project, said the bear could have been predisposed to attack but more likely was looking for food.
                         State and local officials stressed that bear attacks are rare even in a region of the state that may have as many as 2,400 bruins in its
                         dense forests. \"This is a rare occurrence,\" West Milford police Chief Timothy Storbeck said, noting that his department receives
                         six to 12 calls per week regarding bears, usually involving them breaking into trash cans. Locals: Residents in northern New
                         Jersey often spot bears in and around their yards. There are as many 2,400 bruins in the area’s dense forests, but until now had
                         never been a fatal human-bear attack. Wildlife officials believe there is a current shortage of the acorns and berries that bears eat.
                         The hikers had granola bars and water with them, Storbeck said. Officials don’t believe the hikers provoked the bear but they may
                         have showed their inexperience when they decided to run. The safest way to handle a bear encounter is to move slowly and not
                         look the bear in the eye, DEP spokesman Larry Ragonese said. New Jersey Division of Fish and Wildlife guidelines direct law
                         enforcement to euthanize \"Category I\" bears, which are deemed an \"immediate threat to human safety.\" NJ Advance Media
                         reports that the New Jersey State Medical Examiner, the Fish and Wildlife Division of the state Department of Environmental
                         Protection and the West Milford Police Department are looking into the circumstances of Patel’s death.\nFinally, I conclude the
                         report by highlighting the relevance of the event:\n\"Bear sightings are not unusual by any stretch in New Jersey,\" said Bob
                         Considine, spokesperson for the Department of Environmental Protection. \"They have been seen in all 21 counties, although
                         they’re obviously most common in the northwest part of the state.\" Black bears rarely pose a threat to humans and often retreat
                         when confronted. In 2006, a tabby cat scared a black bear up a tree in West Milford. The bear only climbed down and left after
                         the cat’s owner had called it back into the house.\n\nNow, I want to write an article on a different topic:\n{highlights}\nWrite the
                         article, following the steps described above. Your answer should only include the article. The article should be around {length}
                         characters long.",
             Reviews     "I want to write an Amazon review for an item called \"Haier RDG350AW 6.5 Cubic Foot Front Load Gas Dryer, White\". The
                         rating will be 5.0.\nFirst, I choose a title for my review that describes my opinion and experience well. The title of my review
                         will be:\n\"Very Affordable Dryer\".\nThen, I would state my initial experience with the product:\n\"I was a little worried about
                         buying this cause it had some bad reviews, but it’s a really great deal.\"\nThen I would describe the pros and cons of the product,
                         expressing the reasons for my rating:\n\"It didn’t touch my gas bill period. Yes larger loads take a while to dry, maybe up to 3 to
                         4 hours. It’s just really energy efficent. Like I said my gas bill didn’t budge with this being hooked up.\"\nNow, I want to write a
                         review of an item called \"{item_name}\" and give it a rating of {rating}.\nFollow the directions described above to come up with
                         the review. Your answer should only include the review and the title. The review should be one paragraph."
             QA          "If I was asked the question: \"When do the English state schools finish summer term and holiday begins?\",\nFirst, I would give
                         a general overview of the answer:\"In the English school system, state schools run from early September to mid or late July of the
                         following year.\"\nThen, I would go into more detail:\n\"The summer term (also known as the third term) runs from late April and
                         finishes mid to late July with a week-long half term break in between. The summer holiday begins in late July and usually runs
                         about six weeks long, ending in September.\"\nFinally, I would add nuance or additional context to my answer:\n\"The schools on
                         the Trinity terms end their school year and begin summer holidays a few weeks earlier, at the end of June.\"\nFollowing the steps
                         described above, answer the question: \"{question}\" in one paragraph."

                                                                                                                               Continued on next page

                                                                         6539
Prompt        Dataset     Prompt template
                          "role" : "user", "content" : {title_1}
                          "role" : "assistant", "content" : {human-written_abstract_1}
                          "role" : "user", "content" : {title_2}
              Abstracts   "role" : "assistant", "content" : {human-written_abstract_2}
                          "role" : "user", "content" : {title_3}
3-shot
                          "role" : "assistant", "content" : {human-written_abstract_3}
                          "role" : "user", "content" : {title}
                          "role" : "user", "content" : {highlights_1}
                          "role" : "assistant", "content" : {human-written_article_1}
                          "role" : "user", "content" : {highlights_2}
              News        "role" : "assistant", "content" : {human-written_article_2}
                          "role" : "user", "content" : {highlights_3}
                          "role" : "assistant", "content" : {human-written_article_3}
                          "role" : "user", "content" : {highlights}
                          "role" : "user", "content" : {product_name_1}
                          "role" : "assistant", "content" : {human-written_review_1}
                          "role" : "user", "content" : {product_name_2}
              Reviews     "role" : "assistant", "content" : {human-written_review_2}
                          "role" : "user", "content" : {product_3}
                          "role" : "assistant", "content" : {human-written_review_3}
                          "role" : "user", "content" : {product}
                          "role" : "user", "content" : {question_1}
                          "role" : "assistant", "content" : {human-written_answer_1}
                          "role" : "user", "content" : {question_2}
              QA          "role" : "assistant", "content" : {human-written_answer_2}
                          "role" : "user", "content" : {question_3}
                          "role" : "assistant", "content" : {human-written_answer_3}
                          "role" : "user", "content" : {question}
              Abstracts   "As an academic paper writer, your task is to write an abstract of a research paper in a specific writing style. Write in the writing
                          style of an example but ignore the content and topic of the example. You will be provided with the style example. You will be
Style
                          provided with the title for your abstract.\nStyle example: {example}\nTitle: {title}"
              News        "As a news article writer, your task is to write a news article in a specific writing style. Write in the writing style of an example
                          but ignore the content and topic of the example. You will be provided with the style example. You will be provided with the
                          summary of the topic for your article.\nStyle example: {example}\nSummary: {highlights}"
              Reviews     "As an Amazon review writer, your task is to write a review for an item in a specific writing style. Write in the writing style of an
                          example but ignore the content and topic of the example. You will be provided with the style example. You will be provided with
                          the name of the item you have to review.\nStyle example: {example}\nItem: {item_name}"
              QA          "As a highly intelligent question answering bot, your task is to answer questions in specific writing styles. Write in the writing
                          style of an example but ignore the content and topic of the example. You will be provided with the style example. You will be
                          provided with the question.\nStyle example: {example}\nQuestion: {question}"
              Abstracts
Self-refine                   1. "Write an abstract for an article in {category} with a title: \"{title}\". The abstract should be around {length} characters
                                 long."

                              2. "You will see an abstract for a scientific article. Your task is to provide feedback on how to make the text seem more
                                 human-like. Consider sentence length, sentence structure, vocabulary and readability.\nAbstract: {text}\nFeedback: "

                              3. "Based on the feedback, improve the text below:\nText: {text}\nFeedback: {feedback}."

                              4. "Which text sounds more human-written?\nText A: {text_a}\nText B: {text_b}\n\nPick your answer from [\"Text A\",
                                 \"Text B\", \"both\", \"neither\"]. Generate a short explanation for your choice first. Then, generate \"Text A seems more
                                 human-written\" or \"Text B seems more human-written\" or \"Both texts seem human-written\" or \"Neither of the texts
                                 sounds human-written\"

              News

                              1. "Write a news article based on the following highlights:\n\"{highlights}\"\nYour article should be around {length}
                                 characters long."

                              2. "You will see a news article. Your task is to provide feedback on how to make the text seem more human-like. Consider
                                 sentence length, sentence structure, vocabulary and readability.\nArticle: {text}\nFeedback: "

                              3. "Based on the feedback, improve the text below:\nText: {text}\nFeedback: {feedback}."

                              4. "Which text sounds more human-written?\nText A: {text_a}\nText B: {text_b}\n\nPick your answer from [\"Text A\",
                                 \"Text B\", \"both\", \"neither\"]. Generate a short explanation for your choice first. Then, generate \"Text A seems more
                                 human-written\" or \"Text B seems more human-written\" or \"Both texts seem human-written\" or \"Neither of the texts
                                 sounds human-written\"


                                                                                                                              Continued on next page




                                                                         6540
Prompt   Dataset   Prompt template
         Reviews

                      1. "Write an Amazon review for the item \"{item_name}\" with a title \"{title}\" and a rating of {rating}. The review should
                         be around {length} characters long."

                      2. "You will see an Amazon review. Your task is to provide feedback on how to make the text seem more human-like.
                         Consider sentence length, sentence structure, vocabulary and readability.\nReview: {text}\nFeedback: "

                      3. "Based on the feedback, improve the text below:\nText: {text}\nFeedback: {feedback}."

                      4. "Which text sounds more human-written?\nText A: {text_a}\nText B: {text_b}\n\nPick your answer from [\"Text A\",
                         \"Text B\", \"both\", \"neither\"]. Generate a short explanation for your choice first. Then, generate \"Text A seems more
                         human-written\" or \"Text B seems more human-written\" or \"Both texts seem human-written\" or \"Neither of the texts
                         sounds human-written\"

         QA

                      1. "{question}\n Your answer should be around {length} characters long."

                      2. "You will see an answer to a question. Your task is to provide feedback on how to make the text seem more human-like.
                         Consider sentence length, sentence structure, vocabulary and readability.\nAnswer: {text}\nFeedback: "

                      3. "Based on the feedback, improve the text below:\nText: {text}\nFeedback: {feedback}."

                      4. "Which text sounds more human-written?\nText A: {text_a}\nText B: {text_b}\n\nPick your answer from [\"Text A\",
                         \"Text B\", \"both\", \"neither\"]. Generate a short explanation for your choice first. Then, generate \"Text A seems more
                         human-written\" or \"Text B seems more human-written\" or \"Both texts seem human-written\" or \"Neither of the texts
                         sounds human-written\"


                                                 Table 6: Prompt details.




                                                               6541
Detector   Model           Dataset                               Prompt type
                                       0-Shot   3-Shot CoT   1-Shot CoT    Style    3-Shot   Self-refine
                           Abstracts    0.988     0.9875       0.993      0.9795    0.9945    0.9865
                           News         0.999      0.999       0.9985     0.9775    0.7935      1.0
           Llama3.3 70b
                           Reviews      0.984      0.988       0.9995     0.9615    0.9805    0.9875
                           QA          0.8866     0.8966       0.9989     0.9604    0.8233    0.9509
                           Abstracts    0.998      0.991       0.994       0.998     0.999     0.999
                           News          1.0      0.9995       0.9995       1.0       1.0      0.999
           Qwen 14b
                           Reviews     0.9985      0.996         1.0        1.0     0.9965    0.9985
                           QA            0.98     0.9662       0.9916     0.9926    0.9668    0.9736
                           Abstracts   0.9955     0.9915        0.994     0.9965      1.0      0.999
                           News          1.0      0.999        0.9995       1.0       1.0       1.0
           Qwen 32b
                           Reviews      0.999     0.9955         1.0      0.998     0.9985    0.9955
                           QA          0.9763      0.981       0.9852     0.9942    0.9626    0.9736
DeBERTa                    Abstracts    0.988     0.9845       0.9845      0.991    0.9955     0.991
                           News         0.999     0.9995       0.9995       1.0     0.998     0.999
           Qwen 72b
                           Reviews      0.995     0.9975       0.9995     0.9945    0.9965     0.989
                           QA          0.9699     0.9583       0.9889      0.942    0.8903    0.9662
                           Abstracts   0.9855     0.9915       0.992       0.989    0.9985    0.9975
                           News          1.0      0.9995       0.999        1.0     0.9994    0.9995
           Solar 22b
                           Reviews      0.998      0.998       0.9995     0.9975    0.9965     0.999
                           QA          0.9626     0.9852       0.9947     0.9773    0.9705    0.9926
                           Abstracts    0.986      0.989       0.9895      0.984    0.9895    0.9965
                           News        0.9985      0.998       0.9995     0.9975     0.962      1.0
           Mistral 123b
                           Reviews     0.9905     0.9895       0.9945      0.993    0.9765     0.994
                           QA          0.9014     0.8333       0.9299     0.8819    0.9167    0.9905
                           Abstracts   0.9885      0.989       0.992      0.9825    0.9965    0.9885
                           News         0.998     0.9985       0.998      0.9985     0.999      1.0
           Deepseek 70b
                           Reviews     0.9945      0.994       0.9945      0.99     0.9955    0.9955
                           QA          0.9341     0.9019       0.9483     0.8903    0.9151     0.954
                           Abstracts   0.9865     0.9765       0.9925     0.9295    0.9795    0.9835
                           News         0.99      0.996        0.988       0.901    0.782     0.9965
           Llama3.3 70b
                           Reviews      0.987     0.9925       0.9995      0.938     0.99     0.9915
                           QA          0.8481     0.8586         1.0      0.9578    0.8291    0.9451
                           Abstracts   0.9945      0.993       0.995       0.998     0.999    0.9965
                           News         0.999       1.0        0.9995       1.0     0.9985      1.0
           Qwen 14b
                           Reviews     0.9995      0.999       0.9995       1.0      0.998      1.0
                           QA          0.9826     0.9652       0.9784     0.9852    0.9541    0.9662
                           Abstracts    0.993      0.989       0.9935      0.993     0.999    0.9985
                           News          1.0        1.0          1.0      0.999     0.9985    0.9975
           Qwen 32b
                           Reviews      0.998     0.9995       0.9965     0.9985    0.9975    0.9955
                           QA          0.9789     0.9789       0.981      0.9873    0.9209    0.9789
RoBERTa                    Abstracts   0.986      0.9825       0.9875      0.979    0.9945     0.982
                           News        0.998        1.0        0.999      0.9995     0.999     0.999
           Qwen 72b
                           Reviews     0.996      0.9955         1.0      0.9945    0.998     0.9915
                           QA          0.981      0.9399       0.9831     0.9504    0.8623    0.9699
                           Abstracts   0.9825      0.987       0.9795     0.9825     0.995    0.9995
                           News        0.9975      0.995       0.994      0.9995      1.0     0.998
           Solar 22b
                           Reviews     0.9975     0.9975         1.0      0.997     0.9935      1.0
                           QA          0.9742     0.9831       0.9963     0.9821    0.9747    0.9937
                           Abstracts   0.9835      0.982       0.982      0.9665     0.987    0.9925
                           News         0.993      0.996       0.998       0.992    0.9825     0.999
           Mistral 123b
                           Reviews     0.9955      0.981       0.9915      0.991    0.9805    0.9935
                           QA          0.8877     0.8318       0.9383     0.9024    0.8866    0.9826
                           Abstracts   0.9835      0.986       0.988      0.9655     0.996    0.9825
                           News         0.997      0.986       0.9995      0.998    0.9985     0.998
           Deepseek 70b
                           Reviews      0.994      0.995       0.9925     0.9925    0.9965    0.9965
                           QA          0.8813     0.8734       0.9314     0.8645    0.8513    0.9185

                       Table 7: Accuracy of the fine-tuned detectors on in-domain data.


                                                    6542
                 Linsuitic                       Feature                     DeBERTa-based           RoBERTa-based
                 Feature                         Metric                   C-P    C-M      C-D     C-P    C-M      C-D
                                               MATTR                      0.035   0.312   0.097   0.031   0.326   0.100
                 Lexical diversity            L MATTR                     0.038   0.313   0.087   0.021   0.349   0.079
                                             Unique words                 0.004   0.118   0.116   0.044   0.163   0.074
                 Lexical density       Number of function words           0.008   0.148   0.104   0.042   0.282   0.184
                                               FLESCH                     0.006   0.254   0.198   0.006   0.330   0.251
                                            Sentence length               0.069   0.242   0.093   0.073   0.288   0.122
                                            Long sentences                0.020   0.161   0.099   0.061   0.196   0.066
                 Readability
                                            Short sentences               0.072   0.223   0.040   0.041   0.290   0.043
                                          Sentence length std             0.034   0.104   0.004   0.058   0.210   0.064
                                          Length in characters            0.002   0.117   0.083   0.045   0.191   0.012
                                                Polarity                  0.025   0.125   0.224   0.106   0.261   0.187
                 Sentiment
                                              Subjectivity                0.019   0.064   0.001   0.058   0.134   0.054
                                                  Verbs                   0.050   0.080   0.005   0.072   0.042   0.041
                                                 Nouns                    0.047   0.307   0.164   0.066   0.322   0.180
                                               Adjectives                 0.017   0.147   0.038   0.037   0.014   0.092
                                                Adverbs                   0.005   0.201   0.217   0.016   0.213   0.195
                 POS                          Determiners                 0.010   0.215   0.218   0.044   0.286   0.241
                                              Interjections               0.031   0.111   0.157   0.032   0.169   0.096
                                              Conjunctions                0.042   0.061   0.158   0.020   0.190   0.098
                                                Particles                 0.027   0.012   0.026   0.006   0.212   0.047
                                               Numerals                   0.008   0.270   0.163   0.003   0.265   0.202
                                                Pronouns                  0.013   0.064   0.057   0.051   0.159   0.007
                                                 Content words            0.023   0.128   0.064   0.039   0.278   0.148
                                                Function words            0.005   0.045   0.086   0.035   0.251   0.164
                                            Content words types           0.041   0.100   0.195   0.001   0.239   0.238
                                           Function words types           0.012   0.037   0.137   0.048   0.006   0.194
                                                 Proper names             0.070   0.360   0.013   0.022   0.134   0.053
                                        Nouns in possessive case          0.049   0.062   0.102   0.002   0.081   0.167
                                      Adjectives in positive degree       0.012   0.147   0.039   0.043   0.018   0.097
                                       Adverbs in positive degree         0.003   0.188   0.191   0.025   0.188   0.184
                                     Adverbs in comparative degree        0.006   0.191   0.225   0.016   0.206   0.198
                                      Adverbs in superlative degree         0     0.191   0.226   0.022   0.204   0.197
                                                   ’I’ pronoun              0     0.202   0.134   0.033   0.327   0.085
                                                  ’He’ pronoun            0.045   0.173   0.045   0.031   0.191   0.059
                                                 ’She’ pronoun            0.086   0.176   0.004   0.080   0.316   0.020
                                                   ’It’ pronoun           0.067   0.092   0.167   0.067   0.203   0.199
                                                ’You’ pronoun             0.015   0.160   0.085   0.011   0.113   0.028
                                               ’They’ pronoun             0.015   0.072   0.101   0.018   0.128   0.128
                                                 ’Me’ pronoun             0.044   0.096   0.041   0.025   0.077   0.032
                                           ’You’ object pronoun           0.016   0.077   0.153   0.050   0.161   0.100
                                          ’Him’ object pronoun            0.041   0.161   0.069   0.042   0.034   0.097
                 Lexical                   ’Her’ object pronoun           0.040   0.080   0.072   0.072   0.203   0.031
                                                  ’Us’ pronoun            0.041   0.215   0.101   0.012   0.086   0.137
                                               ’Them’ pronoun             0.052   0.030   0.073   0.080   0.080   0.012
                                                 ’My’ pronoun             0.021   0.214   0.127   0.053   0.341   0.109
                                                ’Your’ pronoun            0.007   0.250   0.085   0.009   0.254   0.096
                                                 ’His’ pronoun            0.005   0.078   0.086   0.023   0.059   0.152
                                        ’Her’ possessive pronoun          0.034   0.004   0.053   0.063   0.102   0.129
                                         ’Its’ possessive pronoun         0.089   0.293   0.245   0.079   0.323   0.244
                                       ’Their’ possessive pronoun         0.065   0.237   0.121   0.015   0.228   0.132
                                               ’Yours’ pronoun            0.026   0.001   0.221   0.009   0.103   0.163
                                              ’Theirs’ pronoun            0.004   0.011   0.255   0.008   0.084   0.237
                                                ’Hers’ pronoun            0.061   0.006   0.067   0.031   0.130   0.021
                                       ’Ours’ possessive pronoun          0.003   0.106   0.021   0.010   0.186   0.005
                                              ’Myself’ pronoun            0.023   0.157   0.088   0.017   0.297   0.073
                                             ’Himself’ pronoun            0.012   0.332   0.052   0.027   0.232   0.043
                                             ’Herself’ pronoun            0.036   0.248   0.025   0.032   0.227   0.001
                                               ’Itself’ pronoun           0.032   0.132   0.221   0.055   0.027   0.204
                                            ’Ourselves’ pronoun             0     0.103   0.073   0.018   0.269   0.068
                                           ’Yourselves’ pronoun           0.018   0.177   0.108   0.005   0.194   0.083
                                          ’Themselves’ pronoun            0.064   0.230   0.019   0.100   0.278   0.015
                                     First person singular pronouns         0     0.202   0.134   0.033   0.327   0.085
                                         Second person pronouns           0.014   0.204   0.056   0.011   0.192   0.005
                                     Third person singular pronouns       0.047   0.014   0.093   0.031   0.198   0.140
                                      Third person plural pronouns        0.050   0.182   0.117   0.039   0.129   0.157
                 General             Incidence of verbs in infinitive     0.037   0.050   0.020   0.095   0.153   0.085


Table 8: The correlation between generalization performance with different linguistic features. The significant
correlation is bolded.




                                                                        6543
                                    Cross-prompt                                                       Cross-model                      Cross-dataset
                 0.05
                                                                            Human                                    Human                                Human
                 0.04                                                       AI                                       AI                                   AI


Passive voice
                 0.03
                 0.02
                 0.01
                 0.00
                                                                                                        (a)
                 0.100



Present tenses
                 0.075
                 0.050
                 0.025
                 0.000
                                                                                                       (b)
                 0.100
                 0.075

Past tenses
                 0.050
                 0.025
                 0.000
                                                                                                        (c)
                 0.0100
                 0.0075

'It' pronoun
                 0.0050
                 0.0025
                 0.0000

                                                                                      Self-refine
                          Human
                                                                                                          Human

                                                            0-shot CoT   1-shot CoT
                                                                                                                                         News
                                                                                                                                                          QA
                                                                                                                                                Reviews
                                  0-shot   3-shot   Style
                                                                                                                             Abstract
                                                                                                     Mistral 123B
                                                                                                    Deepseek 70B
                                                                                                    Llama3.3 70B
                                                                                                       Qwen 72B
                                                                                                       Qwen 32B
                                                                                                       Qwen 14B
                                                                                                        Solar 22B
                                                                                                       (d)

Figure 4: The more detailed comparison of different linguistic features across different configurations as well as the
differences between human and AI text. We present the features that have the strongest correlations for different
dimensions (underlined features in Table 4 in the main paper).




                                                                                                       6544
Dataset: Reviews
Item name: Homasy Amplified HDTV Antenna Indoor with Amplifier - 50 Mile Range, Built in Amplifier Signal Booster
Title: Works Well
Rating: 5
Review length in characters: 859
Human, Short sentences: 5
We got rid of satellite TV a couple of years ago. We have two TVs in the house, but only one HD over the air tuner. We’re looking to get another tuner, so with
a second tuner, we need a second antenna. We tested this antenna with our existing tuner. It requires a USB port to be plugged in. We didn’t attach it to our
wall since we plan to use it in a different room and this was just a test. My husband held it up and was able to get a clear picture with it. Our living room has a
two story ceiling. Our other antenna is up pretty high on the wall. The higher it was, the better the reception. The antenna is comparable to our other one in
quality and performance. Now that we have another good antenna, we will go forward with purchasing a new tuner. I received this for free in exchange for my
honest & unbiased review. My thoughts & opinions are my own.
Llama70B, 0-shot, Short sentences: 2
I’m impressed with this antenna! It was easy to set up and I get great reception on all my local channels. The amplifier really makes a difference, picking up
stations that my old antenna couldn’t. I live about 30 miles from the broadcast towers and it works flawlessly. Highly recommend!
Llama70B, 3-shot, Short sentences: 1
I was a bit skeptical about buying an indoor antenna, but I’m glad I took the chance. The Homasy Amplified HDTV Antenna has exceeded my expectations.
Setup was easy, just plug it in and scan for channels. I was able to receive over 30 channels, including major networks like ABC, CBS, NBC, FOX, and
PBS, as well as some local stations. The picture quality is excellent, with no pixelation or freezing. The amplifier seems to make a big difference, as I was
able to pick up channels that my old non-amplified antenna couldn’t. The range is also impressive, I’m about 40 miles from the broadcast towers and I get a
strong signal. The antenna is compact and lightweight, making it easy to place anywhere in the room. Overall, I’m very happy with this purchase and would
recommend it to anyone looking for a reliable and affordable indoor HDTV antenna. Pros: Easy setup Excellent picture quality Good range (up to 50 miles)
Compact and lightweight design Affordable price Cons: None that I can think of! Note: As with any antenna, the number of channels you’ll receive will
depend on your location and the strength of the signals in your area. But overall, I’m very satisfied with this product and would definitely recommend it.
Llama70B, Style, Short sentences: 2

I bought the "H́omasy Amplified HDTV Antenna Indoor with Amplifier"f́or my 75 year old dad because he likes to watch his local news and sports channels
without relying on cable. This antenna makes it so he can. The thing I dont́ like? That you have to deal with all the extra cables the amplifier and signal booster
are great, but they add clutter. So it would be nice to be able to just have a more streamlined setup. The extra cables just get tangled up behind the TV.
Llama70B, 0-shot CoT, Short sentences: 2
Works Well I’m impressed with this antenna, it works well and picks up all local channels clearly. The amplifier helps boost weak signals, giving me
more channel options. Easy to set up, compact design, and great picture quality. I can receive channels within a 50-mile range without any issues. Highly
recommended!
Llama70B, 1-shot CoT, Short sentences: 0
"Excellent Reception at a Great Price" I was a bit skeptical about purchasing this antenna due to mixed reviews, but it has exceeded my expectations in every
way; itś a fantastic value for the money. The pros definitely outweigh the cons, as it picks up a ton of channels with crystal clear reception, and the amplifier
makes a huge difference, allowing me to receive stations from over 40 miles away with perfect clarity. Yes, you may need to adjust the antennaś position for
optimal signal strength, but thatś a small trade-off for the quality and number of channels you get, and the fact that itś so easy to set up and use is just icing on
the cake.
Llama70B, self-refine, Short sentences: 0
I was a bit skeptical about whether this antenna would be able to pull in clear signals from 30 miles away, but I’ve been blown away by its performance. Setting
it up was a breeze, and the built-in amplifier has made a huge difference in terms of picture quality I can now get all my local channels in crystal-clear HD,
which is a big upgrade from the fuzzy reception I was getting before. What really impresses me, though, is that it’s picked up a few channels I didn’t even
know existed, including some great local stations that I’d never been able to tune into before. Overall, I’m thoroughly impressed with this antenna and would
definitely recommend it to anyone looking to boost their TV reception!


  Table 9: Case study of human and AI texts for the cross-prompt generalization setting shown in Figure 2 (a).




                                                                               6545
Dataset: Abstracts
Title: Satellites and large doping- and temperature-dependence of electronic properties in hole-doped BaFe2As2
Category: Strongly Correlated Electrons
Review length in characters: 1037
Human, “We” pronoun: 0.013698
Over the last years, superconductivity has been discovered in several families of iron-based compounds. Despite intense research, even basic electronic
properties of these materials, such as Fermi surfaces, effective electron masses, or orbital characters are still subject to debate. Here, we address an issue that
has not been considered before, namely the consequences of dynamical screening of the Coulomb interactions among Fe-d electrons. We demonstrate its
importance not only for correlation satellites seen in photoemission spectroscopy, but also for the low-energy electronic structure. From our analysis of the
normal phase of BaFe2As2 emerges the picture of a strongly correlated compound with strongly doping- and temperature-dependent properties. In the hole
overdoped regime, an incoherent metal is found, while Fermi-liquid behavior is recovered in the undoped compound. At optimal doping, the self-energy
exhibits an unusual square-root energy dependence which leads to strong band renormalizations near the Fermi level.
Deepseek, 0-shot, “We” pronoun: 0.011628
This study investigates the electronic properties of hole-doped BaFeAs using angle-resolved photoemission spectroscopy (ARPES). We observe prominent
satellite bands whose intensity varies significantly with doping and temperature. These satellites reveal intricate many-body interactions, suggesting coupling of
electrons with lattice vibrations or spin fluctuations. Our findings indicate that doping-induced modifications to the Fermi surface and temperature-dependent
renormalization play crucial roles in shaping the electronic structure. The results provide insights into the unconventional superconductivity of iron-based
compounds, highlighting the importance of electron interactions in determining their unique properties.
Deepseek, 3-shot, “We” pronoun: 0.000000
The study investigates the electronic properties of hole-doped BaFeAs, focusing on satellite features observed in spectroscopic measurements and their
sensitivity to doping and temperature variations. Here’s a structured summary: Material Context: Hole-Doping: Introduces excess positive charge carriers,
altering the electronic structure significantly. Iron-Based Superconductor: Part of a class of materials known for high critical temperatures and complex
electronic interactions. Key Observations: Satellite Features: These are secondary peaks near primary spectral lines, likely arising from many-body interactions
such as electron-boson coupling. Doping Dependence: The intensity or prominence of these satellites varies with doping levels, indicating a correlation
between carrier concentration and interaction strength. Temperature Dependence: Thermal effects modify the satellites, suggesting that phonon interactions
or other thermally induced processes play a role. Implications for Superconductivity: Correlation with Superconducting Mechanisms: The presence and
behavior of satellites may hint at the strength of pairing interactions crucial for superconductivity. Potential Optimization: Understanding how doping and
temperature influence these features could guide strategies to enhance critical temperature (Tc). Methodology: Likely employs advanced spectroscopic
techniques such as ARPES, supported by theoretical modeling to interpret the data accurately. Research Implications: Suggests a nuanced relationship between
satellite features and superconductivity, highlighting the complexity of electronic interactions. Encourages further exploration across different superconducting
materials to identify universal principles or unique mechanisms. This study contributes valuable insights into the intricate electronic dynamics of iron-based
superconductors, offering potential pathways for advancing our understanding and engineering of high-Tc materials.
Deepseek, Style, “We” pronoun: 0.013605
We report a comprehensive investigation into the electronic properties of hole-doped BaFeAs, focusing on the significant influence of doping level and
temperature variations. Our studies uncover a pronounced dopingand temperature-dependent behavior in the material’s electronic characteristics, with
particular emphasis on the emergence of satellite features in spectroscopic measurements. By employing advanced experimental techniques combined with
theoretical modeling, we demonstrate how these satellite structures correlate with changes in carrier concentration and lattice dynamics. A detailed analysis
reveals that the interplay between doping-induced charge carriers and thermal fluctuations plays a critical role in modulating the material’s conductivity and
band structure. This work provides fundamental insights into the underlying mechanisms governing the electronic response of doped iron-based compounds,
offering valuable guidance for tailoring their properties for potential technological applications. Our findings underscore the importance of considering both
doping and temperature effects when designing materials for optimized performance in electronic devices.
Deepseek, 0-shot CoT, “We” pronoun: 0.006993
This study investigates the electronic properties of hole-doped BaFeAs using high-resolution angle-resolved photoemission spectroscopy (ARPES). We
observe prominent satellite features in the spectral function, whose intensity and dispersion exhibit strong dopingand temperature-dependent behavior. These
satellites, indicative of many-body interactions, become more pronounced with increased doping and lower temperatures, particularly near the Fermi level.
Our analysis reveals a significant evolution of the electronic structure across the doping phase diagram, highlighting non-trivial renormalization effects and
deviations from conventional quasiparticle behavior. The observed trends suggest that strong electron-electron correlations play a critical role in shaping the
electronic properties of BaFeAs. Furthermore, the dopingand temperature-dependent saturation of these satellites provides insights into the interplay between
correlation effects and superconducting tendencies in iron-based superconductors. These findings challenge existing theoretical frameworks and underscore the
importance of incorporating strong correlation physics in modeling the electronic states of doped iron pnictides.
Deepseek, 1-shot CoT, “We” pronoun: 0.007605
In recent years, the study of strongly correlated electron systems has gained significant attention due to their unique electronic properties, particularly in
materials exhibiting unconventional superconductivity. Hole-doped BaFeAs, a member of the iron-based superconductor family, has emerged as a model
system for investigating the interplay between electronic correlations, doping, and temperature-dependent phenomena. Understanding the intricate relationships
between these factors is crucial for advancing our knowledge of quantum materials and their potential applications. Despite extensive research, the dopingand
temperature-dependent evolution of electronic properties in BaFeAs remains poorly understood, particularly in the underdoped regime where strong correlations
dominate. To address these challenges, we employ advanced spectroscopic techniques to probe the electronic structure of hole-doped BaFeAs across a wide
range of doping levels and temperatures. Our measurements reveal pronounced satellite features in the electronic spectra, which are highly sensitive to both
doping and temperature. These observations suggest the presence of strong many-body interactions, whose strength varies significantly with doping and
thermal fluctuations. By systematically analyzing these dependencies, we uncover universal scaling behaviors that shed light on the underlying mechanisms
governing the electronic response in this class of materials. Our findings demonstrate that the dopingand temperature-dependent evolution of electronic
properties in BaFeAs cannot be explained by conventional theories alone, pointing to the importance of incorporating strong correlation effects. Furthermore,
the emergence of robust satellite structures highlights the critical role of short-range Coulomb interactions in shaping the electronic landscape. These insights
not only advance our understanding of the phase diagram of iron-based superconductors but also provide a framework for exploring similar phenomena in
other strongly correlated electron systems.
Deepseek, self-refine, “We” pronoun: 0.012658
Refined Hole-doped BaFeAs reveals fascinating insights into the interplay between strong electron correlations and unconventional superconductivity. Through
advanced techniques like ARPES and transport measurements, we explored how doping and temperature affect its electronic properties. Notably, we identified
significant satellite features in the valence band, which change markedly with doping and temperature, reflecting substantial particle interactions a hallmark of
many-body physics. These changes align with shifts in the Fermi surface and quasiparticle behavior, underscoring how correlations redefine the material’s
electronic landscape. Moreover, our measurements showed variations in resistivity and Hall coefficients tied to doping and temperature, hinting at intricate
interactions between charge carriers and spin fluctuations. Intriguingly, a nonlinear pattern emerged across the doping phase diagram, suggesting competing
orders near quantum criticality. These findings highlight the pivotal role of strong correlations in iron pnictides and offer insights into exotic phases in similar
materials. Such understanding could pave the way for innovative device technologies, bridging cutting-edge science with practical applications.


Table 10: Case study of human and AI texts for the cross-prompt generalization setting shown in Figure 2 (b).
                                                                              6546


## Extraction verification

- **Beginning checked:** Compared the extracted title, author block, abstract, proceedings footer, and start of the introduction against page 1 of the rendered ACL PDF.
- **Middle checked:** Compared the dataset, generalization setup, correlation method, Figures 1-2, Tables 1-3, results, discussion, and limitations against pages 3-9 of the rendered PDF.
- **End checked:** Compared appendix Tables 6-10, prompt templates, in-domain accuracy table, full feature table, case studies, final page number, and terminal form-feed against pages 16-23 of the rendered PDF.
- **Structure checked:** 23 PDF pages; sections 1-7; acknowledgments; references; appendix A with subsections A.1-A.4; 10 tables; 4 figures; footnote and code link; limitations section. The extraction contains 1,725 lines, 15,777 words, and 169,859 bytes before snapshot metadata was added.
- **Known omissions:** None from the accessible text layer. Visual geometry, colour scales, plotted marks, and exact typographic placement remain in the preserved PDF; their labels, captions, and table text are present in the extraction.

## Preserved attachments

| Path | Role in the source | SHA-256 | Preservation / extraction notes |
|---|---|---|---|
| `snapshots/attachments/xia-stanczak-roth-detector-generalization.pdf` | Canonical 23-page ACL proceedings PDF and visual source of the extracted full text | `6136f76b4fdf989e262936fc095d8123f838e49d828e94cf0e8a6c2b7e94f267` | Downloaded directly from ACL Anthology on 2026-07-14; embedded text extracted with `pdftotext -layout`; retained for tables, figures, and reading-order verification. |
