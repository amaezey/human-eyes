# Identifying Bias in Machine-generated Text Detection

- **Canonical URL:** https://aclanthology.org/2026.acl-long.109/
- **Alternate access URLs:**
  - https://aclanthology.org/2026.acl-long.109.pdf
  - https://aclanthology.org/attachments/2026.acl-long.109.checklist.pdf
  - https://doi.org/10.18653/v1/2026.acl-long.109
- **Author / owner:** Kevin Stowe, Svetlana Afanaseva, Rodolfo C. Raimundo, Yitao Sun, and Kailash Patil
- **Publisher:** Association for Computational Linguistics
- **Published:** 2026-07
- **Retrieved:** 2026-07-14
- **Stable identifier:** DOI 10.18653/v1/2026.acl-long.109; ACL Anthology ID 2026.acl-long.109
- **Version / revision:** ACL 2026 proceedings version, pages 2383-2395
- **Extraction method:** First-party ACL proceedings PDF and ACL Responsible NLP Checklist PDF downloaded with `curl`; all 13 paper pages and both checklist pages extracted with Poppler `pdftotext -layout`; paper pages 1, 7, and 13 rendered with `pdftoppm` and visually compared with the extraction
- **Full-text status:** complete for the proceedings paper and its authoritative two-page Responsible NLP Checklist
- **Access and transformation notes:** The preserved text below is the complete 13-page paper extraction followed by the complete two-page checklist extraction. The paper includes tables, captions, footnotes, limitations, references, and appendices. The two-column reading order and line-break hyphenation reflect `pdftotext -layout`. Table 3's colored direction markers do not survive plain-text extraction; the table legend and surrounding analysis preserve their meaning, and the authoritative PDFs are preserved as attachments. No OCR was used. Appendix B provides repository URLs for detector implementations but no exact repository commit identifiers or model checkpoint hashes; the linked code and models were not recursively ingested.

## Full text

                       Identifying Bias in Machine-generated Text Detection


             Kevin Stowe, Svetlana Afanaseva, Rodolfo Raimundo, Yitao Sun, Kailash Patil
                                               Pindrop
               {kevin.stowe, safanaseva, rraimundo, ysun, kpatil}@pindrop.com




                             Abstract                              These systems span detection of video, audio, and
                                                                   text-based generation, and are becoming essential
           The meteoric rise in text generation capabil-           tools for many practical scenarios where guidelines
           ity has been accompanied by parallel growth
                                                                   require human-written content.
           in interest in machine-generated text detection:
           the capability to identify whether a given text
                                                                      It is important to consider the practical implica-
           was generated using a model or written by a             tions of machine-generated text detection systems.
           person. While detection models show strong              In this work, we assess the potential for bias in
           performance, they have the capacity to cause            these detection systems. There is substantial poten-
           significant negative impacts. We explore poten-         tial for harm in systems that erroneously flag con-
           tial biases in English machine-generated text           tent as automatically generated, especially if these
           detection systems. We curate a dataset of stu-          systems exhibit bias toward disadvantaged popula-
           dent essays and assess 16 different detection
                                                                   tions. This could lead to rejection of genuine work,
           systems for bias across four attributes: gen-
           der, race/ethnicity, English-language learner           reduction of visibility, and unfair allocation of re-
           (ELL) status, and economic status. We evalu-            sources. Consider student essays, where inaccurate
           ate these attributes using regression-based mod-        false positives could lead to harmful consequences
           els to determine the significance and power             for students, or content moderation tools, where
           of the effects, as well as performing subgroup          human perspectives and representation could be
           analysis. We find that while biases are gener-          unfairly filtered or silenced.
           ally inconsistent across systems, there are sev-
                                                                      To assess bias in machine-generated text de-
           eral key issues: several models tend to classify
           disadvantaged groups as machine-generated,
                                                                   tection systems, we systematically explore pub-
           ELL essays are more likely to be classified             licly available systems, analyzing their potential
           as machine-generated, economically disadvan-            to unfairly classify human-written text as machine-
           taged students’ essays are less likely to be clas-      generated. We curate a dataset of human-written
           sified as machine-generated, and non-White              texts and explore a series of publicly available mod-
           ELL essays are disproportionately classified as         els for potential biases across several dimensions:
           machine-generated relative to their White coun-         race, gender, age, ELL status, and economic status.
           terparts. Finally, we perform human annotation
                                                                   We pursue the following research questions:
           and find that while humans perform generally
           poorly at the detection task, they show no sig-             1. Do machine-generated text detection sys-
           nificant biases on the studied attributes.                     tems exhibit bias? We are particularly in-
                                                                          terested in bias across dimensions of gender,
   1       Introduction                                                   race, age, ELL status, and economic status.
   With the rise in the usage of generative AI systems,                   We perform regression analysis, evaluating
   there is a growing need to distinguish content gen-                    each attribute along with potential confounds.
   erated by a model from human-written content. To                    2. Which subgroups are likely to be impacted?
   this end, there has been an explosion of research                      We analyze each of the 16 possible subgroups,
   into machine-generated text detection1 : identifying                   evaluating performance compared to the gen-
   content that has been automatically generated by                       eral population.
   generative systems (e.g., large language models).                   3. Do humans exhibit the same biases? We
       1
       Also referred to as "deepfake" or "LLM-generated" text             have expert human annotators attempt to clas-
   detection.                                                             sify text as machine-generated or human-
                                                                2383
Proceedings of the 64th Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers), pages 2383–2395
                                July 2-7, 2026 ©2026 Association for Computational Linguistics
      written, similarly evaluating their results for              AI in assisting students is under scrutiny (Meyer
      potential biases.                                            et al., 2023), and fraud, where generative mod-
                                                                   els are being used to perpetrate scams (Romero-
   We find that while many English language learn-                 Moreno, 2025) highlight the need for accurate de-
ers texts are classified at a significantly higher rate            tection of machine-generated text.
than native speakers, these results are inconsistent,
                                                                      The power of generative models has been ac-
and models vary greatly in their respective biases.
                                                                   companied by increased interest in detection sys-
Several models tend to misclassify texts from dis-
                                                                   tems (including a workshop focused specifically
advantaged groups as machine-generated, while
                                                                   on this task (Alam et al., 2025)). There have
other trained and zero-shot models vary. Across
                                                                   been a wide variety of systems proposed, includ-
all attributes, we find that economic disadvantage
                                                                   ing feature-based methods, fine-tuned models, and
serves as a negative indicator: essays from stu-
                                                                   zero-shot systems. For a comprehensive survey of
dents with no economic disadvantage are classified
                                                                   recent datasets and methods, see Wu et al. (2025).
as machine-generated more often across most sys-
tems. Subgroup analysis reveals more significant is-
sues: non-White ELL essays are much more likely                    2.2   Bias in Models
to be classified as machine-generated than White
ELL essays, with higher incidence for men than for                 Bias has been extensively studied in deepfake de-
women. Finally, we find that human experts, while                  tection systems across domains of video and audio
generally poor at the task (with accuracy ranging                  (Liu et al., 2025; Katamneni et al., 2024; Ju et al.,
from 0.449 to 0.526), exhibit no significant biases                2024), and as a ubiquitous aspect of natural lan-
based on the attributes studied.                                   guage processing (Bartl et al., 2025; Stanczak and
                                                                   Augenstein, 2021; Blodgett et al., 2020). Recent
2    Background                                                    work has shown that humans exhibit significant bi-
                                                                   ases when attempting to identify deepfake social
Our goal is to identify situations in which machine-
                                                                   media profiles (Mink et al., 2024). However, there
generated text detection models make consistent
                                                                   remains relatively little work concerning the bias
mistakes with regard to certain attributes, violating
                                                                   of machine-generated text detection systems.
group fairness (Czarnowska et al., 2021), which
can lead to representational harms (e.g., protected                   Jung (2025) explores this topic in considerable
groups misrepresented as abusing generative tools)                 depth, but focuses only on text length and stylis-
and allocational harms (e.g., writing of protected                 tic personality as biases, which excludes disad-
groups being disqualified, censored, or minimized                  vantaged groups. Liang et al. (2023) explore bias
due to unfair model performance). We adopt their                   in machine-generated text detection against non-
terminology: we analyze four sensitive attributes:                 native English speakers, claiming that seven major
gender, race/ethnicity, ELL status, and economic                   detectors perform significantly worse on non-native
status. Within these attributes we define advan-                   English speakers than native speakers. However,
taged/disadvantaged groups (see Section 3.1).2                     they do not indicate which models were used, and
Our evaluation framework is based on Dayanik                       they report results on a limited dataset of only 179
et al. (2022), who outline a method for identifying                student essays. Verma et al. (2024) echo this result
bias across multiple attributes in NLP problems.                   for English learner data, but note that it was unclear
                                                                   whether the differences were due to language or
2.1 Machine-generated Text Detection                               the length of the documents.
Recent advances in generative AI have had many                        To address this gap in our understanding, we
benefits, but understanding whether text has been                  evaluate a suite of machine-generated text detection
written by a large language model (LLM) or a hu-                   systems on a large corpus of student essays, eval-
man is often essential. Domains such as news,                      uating performance for bias across four attributes:
where generative models can be used to spread                      gender, race, ELL status, and economic status. We
misinformation (Hanley and Durumeric, 2024; Pan                    provide a thorough analysis of possible confound-
et al., 2023), education, where the use of generative              ing factors as well as exploring subgroup differ-
   2
                                                                   ences. To our knowledge, this is the first work
     We use "disadvantaged" rather than "protected" as only
two of our attributes, gender and race/ethnicity, are considered   to perform a rigorous analysis of bias in machine-
protected in the United States.                                    generated text detection.
                                                               2384
                                  Gender          Race/Ethnicity                 ELL         Economic Disadvantage
                       Total   Male  Female      White Non-White            No         Yes    No          Yes
    PERSUADE V 2.0     24695   12074   12621     11282      13413         22451     2244     11003        13692
    ASAP V 2.0         24728   12498   12230      9841      14887         20991     3737      7933        16795
    ELLIPSE             6482    3636    2846       471       6011           0       6482      1974         4508
    Combined (clean)   41743   21277   20466     15078      26665         31079    10664     18188        23555

                          Table 1: Counts for each attribute/group in our combined corpus.


3     Evaluation Datasets                                   posits White as the advantaged class and non-White
                                                            disadvantaged, but there are substantial differences
To evaluate potential bias in machine-generated
                                                            between subgroups: we provide further exploration
detection systems, we use three datasets. These
                                                            of the differences between these in Section 8. We
are PERSUADE - V 2.0 (Crossley et al., 2024), ASAP -
                                                            note such fixed categorization schemes can serve to
V 2.0 (Crossley et al., 2025), and ELLIPSE (Cross-
                                                            entrench inequalities, and that racial divisions are a
ley, 2024). These datasets all consist of persuasive
                                                            product of social contexts (Field et al., 2021; Hanna
essays written by 6th to 12th grade students in the
                                                            et al., 2020). Our goal is to examine potential bi-
United States, containing demographic information
                                                            ases in these models, but we stress our analysis
about race, gender, English-language-learner status,
                                                            inherits potential pitfalls from this labeling system.
and economic status of the writers. The ASAP - V 2.0
and ELLIPSE datasets extend the PERSUADE - V 2.0            English-language learner (ELL) status: The
dataset: ASAP - V 2.0 adds 12k new samples and fills        corpora make a binary distinction between ELL
in demographic gaps, while the ELLIPSE dataset              and non-ELL students; we consider ELL the disad-
adds new samples focusing on English language               vantaged attribute and non-ELL the advantaged.
learners. We combine these datasets into a single,
cleaned version, removing duplicate texts as well           Economic status: The corpora define two eco-
as instances where any demographic information              nomic statuses: not disadvantaged (the "advan-
is missing; details are in Table 7.                         taged" group) and disadvantaged.

3.1 Sensitive Attributes                                    4       Models
Gender: The corpora contain gender as a binary              There are many options for machine-generated text
attribute (male/female). We use these labels, with          detection models: we focus on an array of zero-shot
male considered the advantaged class and female             and pretrained models.3
as the disadvantaged class: machine learning mod-
els are known for biased performance on female              4.1       Zero-shot Models
data (Bartl et al., 2025). We recognize this binary         We split zero-shot models into GPT-based and non-
labeling prohibits proper study and representation          GPT-based systems. All are suitable for zero-shot
of other potential gender labels. Our setup mir-            detection: they can score an independent text with-
rors previous work in which datasets contain only           out training or other context. While not necessarily
binary labels out of necessity (Biester, 2025; Plaza-       tuned to specifically detect GPT-based generation,
del Arco et al., 2024; Savoldi et al., 2021), and we        the GPT-based models are clustered together as
continue with the understanding that this labeling          their dependence on OpenAI models makes them
system contains an inherent risk of misrepresenting         somewhat harder to inspect, and their behavior may
bias, erasure, and other representational and allo-         change as access to these models changes. The
cational harms with regard to non-binary genders            models used are Ghostbuster (Verma et al., 2024)
(Stanczak and Augenstein, 2021; Dev et al., 2021).          and Glimpse (Bao et al., 2025). For non-GPT mod-
                                                            els, we utilize Fast-DetectGPT (Bao et al., 2024)
Race/ethnicity: The dataset contains six differ-
                                                            and Binoculars (Hans et al., 2024), which rely on
ent labels for race/ethnicity. For our initial analysis,
                                                            extracting features from an underlying transformer-
we compress these into two groups: White and
                                                            based language model, as well as Zippy (Thinkst,
non-White: for this attribute, this reflects the ma-
                                                            2023), which uses compression-based methods.
jority group (White) and the minority group (non-
White) (Economic Policy Institute, 2022). This                  3
                                                                    Model implementation details provided in Appendix B.

                                                         2385
4.2 Trained Models                                                 Model                         Prec.   Rec.     F1     AUROC

These are publicly available models that have                      Ghostbuster                   0.638 0.606 0.622       0.667
                                                                   Glimpse                       0.899 0.861 0.880       0.948
been trained through varying methods on various
datasets. We use BiScope (Guo et al., 2024a),                      Binoculars                    0.869   0.825   0.846   0.907
                                                                   FDG (falcon-7b)               0.670   0.635   0.652   0.708
which has four variants (Yelp, Arxiv, Essay, and                   FDG (gpt-neo)                 0.781   0.733   0.756   0.829
Creative) based on training data, and DeTeCtive                    Zippy (LZMA)                  0.359   0.327   0.343   0.262
(Guo et al., 2024b), which has four variants of                    BiScope (Yelp)                0.706   0.691   0.699   0.726
which we use three (MAGE, M4GT, TuringBench),                      BiScope (Arxiv)               0.404   0.381   0.392   0.327
                                                                   BiScope (Essay)               0.841   0.761   0.799   0.805
as the fourth OUTFOX variant overlaps with our                     BiScope (Creative)            0.388   0.302   0.339   0.362
evaluation data.                                                   DeTeCtive (MAGE)              0.470   0.127   0.200   0.477
   Another subset consists of fine-tuned versions of               DeTeCtive (M4GT)              0.863   0.472   0.610   0.696
                                                                   DeTeCtive (TuringBench)       0.508   0.870   0.641   0.450
transformer models. They have either been tuned                    RADAR                         0.700   0.613   0.653   0.706
for a specific task (Desklib (Desklib, 2025) and                   Desklib                       0.976   0.960   0.968   0.994
                                                                   E5-lora                       0.417   0.361   0.387   0.362
e5-lora (Dugan et al., 2024) are optimized for the
RAID benchmark4 ), or are designed to be gener-
                                                                   Table 2: Benchmark model performance for the investi-
ally applicable for machine-generated text detec-                  gated systems on a balanced corpus of human-written
tion (RADAR (Hu et al., 2023)).                                    and LLM-generated texts.

5    Benchmarking
                                                                   on the dataset: BiScope performance ranges in
We start by benchmarking the models to better un-                  AUROC from 0.362 to 0.805, with the Essay vari-
derstand their overall performance, and then ex-                   ant performing best, likely because it best matches
plore potential biases on human-written corpora.                   the evaluation data domain. These models tend to
To benchmark our models, we utilize the OUTFOX                     struggle when applied to new domains, and while
dataset (Koike et al., 2024). This dataset combines                this is important to note, our primary goal is not to
human-written texts from the PERSUADE - V 2.0 cor-                 compare or evaluate the exact performance of these
pus with three machine-generated samples for each                  models, but rather to assess whether the mistakes
human-written text. This corpus comes from the                     they are making significantly favor certain groups.
same source, matching the domain, style, and tone                  For this reason, we proceed with our bias analysis
of our human-written evaluation corpus.                            using all models, with the understanding that some
   We evaluate each model, reporting precision, re-                may be better or worse suited to this task.
call, F1 score, and area under the receiver oper-                     We also aim for relative model independence
ating characteristics (AUROC) in Table 2. These                    to cover a broad range of potential systems. We
metrics provide a broad overview of performance:                   calculate Pearson correlations between all models:
they have different implications for different use                 only 5.5% of pairs have correlation over 0.6, and
cases, with precision minimizing false positives,                  none with correlation over 0.8, indicating models
recall maximizing coverage, and AUROC provid-                      have weak to moderate correlation. The primary
ing a balanced view across thresholds. We convert                  correlations are between BiScope models, where
model scores into binary classification by identi-                 the Creative variant overlaps with the Essay and
fying the threshold that optimizes equal error rate                Yelp variants, and between the two FDG variants.5
(EER) over a validation set of 1000 samples. We
then use this threshold to make predictions, con-                  6       Logistic Regression Analysis
sidering a sample machine-generated if the score
                                                                   To study bias, we need a methodology that can ac-
provided by the model exceeds this threshold. This
                                                                   count for the relationships and confounds present
result is strictly improved F1 scores while keeping
                                                                   in the data. The attributes we study are unlikely
constant AUROC.
                                                                   to be independent, and additional factors may in-
   We find that model performance is fairly dis-
                                                                   fluence model performance. To handle this, we
parate: the zero-shot models are mostly strong ex-
                                                                   perform our analysis based on the methodology
cept for Zippy. The trained models depend heavily
                                                                   of Dayanik et al. (2022), who outline procedures
    4
      https://raid-bench.xyz/leaderboard; at the time              for identifying bias in natural language processing
of writing, these are the two top-performing, publicly available
                                                                       5
systems.                                                                   For more, see Appendix C.

                                                               2386
                             Gender                 Race/Ethnicity              ELL Status               Econ. Status
                 Model Diff. Coef. DA            Diff. Coef. DA            Diff. Coef. DA           Diff. Coef. DA
            Ghostbuster -.102    -.139‡   2.98    .041   -.244‡    1.01    -.143   -.945‡   6.50    -.120   -.338‡   5.87
               Glimpse -.046     -.338‡   1.07   -.016   -.012‡    0.32    -.047   -.199‡   0.86    -.036   -.444‡   0.87
             Binoculars -.042    -.168‡   1.00   -.002   -.548‡    0.09    -.010   -.475‡   0.53    -.059   -.280‡   2.25
        FDG (falcon-7b) .068      .167‡   2.80    .007    .361‡    0.14     .003    .195‡   1.13     .080    .185‡   4.09
         FDG (gpt-neo) .052       .182‡   4.65    .018    .267‡    0.85    -.019    -.081   3.87     .047    .115‡   3.39
         Zippy (LZMA) -.036      -.146‡   1.39    .009    .471‡    0.26    -.135   -.286‡   14.84    .048    .177‡   1.34
         BiScope (Yelp) .052       .085   3.36   -.001    .141‡    0.01     .022     .090   0.52     .074    .224‡   10.10
        BiScope (Arxiv) .028      .088‡   0.90    .010    .301‡    0.40    -.035     .042   5.01     .058    .184‡    4.06
        BiScope (Essay) .020       .082   2.74    .011     .048    0.71    -.016   -.280‡   5.25     .024    .166‡    6.03
     BiScope (Creative) .073      .255‡   2.95   -.016    .311‡    0.14    -.009    .162‡   1.81     .102    .344‡    6.16
    DeTeCtive (MAGE) -.056       -.185‡   5.53    .008     .038    0.18    -.180   -.249‡   79.12   -.004     .105    0.54
     DeTeCtive (M4GT) .008        -.058   0.25   -.008    -.109    1.49     .009     .083   0.26     .017    .288‡    4.39
DeTeCtive (TuringBench) .004       .010   0.15   -.004    .238‡    0.13    -.008   -.344‡   1.96     .014     .129    1.31
                RADAR .007         .037   0.70    .049   -.111‡    6.48     .006   -.470‡   0.84    -.035   -.310‡    3.72
                 Desklib -.002     .001   0.04   -.002   -.396‡    1.02    -.001   -.274‡   0.04    -.007     .027   0.73
                 E5-lora -.044     .074   0.37    .103    .186‡    5.15    -.029   -.212‡   0.21    -.125   -.257‡    5.49

Table 3: Model performance differences (Diff.), attribute coeffecients (Coef., p < 1.56e − 4) and Dominance
Analysis scores (DA) for each model.     indicates the advantaged class is more likely classified as machine-
generated; indicates the disadvantaged class is more likely machine-generated.


systems where there may be many factors involved.                 machine-generated scores; negative scores indicate
   We train a logistic regression model over rele-                the disadvantaged class. For all experiments, we
vant features as well as confounds to predict the                 use a significance threshold of 0.01 with Bonfer-
error of the model, and use feature coefficients as               roni correction, using the number of models (16)
well as dominance analysis to assess the impact of                and the number of categories, yielding a p value of
each attribute. For bias variables, we use the sensi-             0.01/(categories × models); we note the specific
tive attributes: gender (male/female), race/ethnicity             values in each experiment.
(White/non-White), English language-learner sta-
                                                                  Dominance analysis (DA): This indicates the
tus (no/yes), and economic status (not disadvan-
                                                                  strength of this attribute’s contribution in the lo-
taged/disadvantaged). We then define covariates,
                                                                  gistic regression model. We report dominance as
which are other potential predictors of error: we
                                                                  percentage of relative importance (e.g., 4.73 indi-
use perplexity via the opt-iml-1.3b model (Iyer
                                                                  cates that 4.73% of the prediction comes from this
et al., 2023) and length of the text in words (defined
                                                                  attribute). We consider dominance scores over 5%
by splitting on whitespace). We calculate variance
                                                                  to be meaningful.
inflation factor (VIF) for each bias variable and co-
variate, finding the values to all be below 4, there-                Significance tests are useful for detecting the
fore suitable with minimal multicollinearity. We                  presence of systematic differences, but do not cap-
report the following:                                             ture the magnitude of difference (Dayanik et al.,
                                                                  2022; Stanczak and Augenstein, 2021). Hence, we
Performance Difference (Diff.): The difference
                                                                  are most interested in cases where both the coef-
in model performance for each attribute. This is
                                                                  ficient from the model is significant (indicating a
calculated as the mean score for the advantaged
                                                                  significant relationship between the attribute and
class minus that of the disadvantaged class. Higher
                                                                  model performance) and the dominance factor is
scores indicate that the advantaged class is more
                                                                  strong (> 5, indicating that at least 5% of the differ-
likely to be classified as machine-generated; lower
                                                                  ence in performance is due to this attribute): these
scores indicate the disadvantaged class is more
                                                                  cases are marked with (the advantaged class is
likely to be classified as machine-generated.
                                                                  more likely to be classified as machine-generated)
Coefficient (Coef.): The coefficient for the given                and (the disadvantaged class is more likely to
attribute in the regression model. Positive scores                be classified as machine-generated). Table 3 shows
indicate the advantaged class predicts higher                     these results over all models and categories.
                                                          2387
                                                                                           E5-lora
6.1 General Analysis                                                                                                                         r = -0.487
                                                                                                                                             Zero-shot
                                                                                           DeTeCtive (TuringBench)
                                                                        0.20                                                                 Trained
We observe relatively few instances where model
coefficients are significant and dominance analysis
                                                                        0.15
indicates a strong influence of the corresponding                                                                    Ghostbuster

                                                          Pseudo RMcF
                                                                  2
attribute (12 out of 64 total observations). These                           Zippy (LZMA)                       FDG (falcon-7b)
cases also tend to be inconsistent, showing no sys-                     0.10       BiScope (Creative)
                                                                                                               DeTeCtive (M4GT) Binoculars
tematic preference for either advantaged or disad-                                            DeTeCtive (MAGE)              FDG (gpt-neo) Desklib
                                                                                 BiScope (Arxiv)                  BiScope (Yelp)
vantaged groups. The primary exception is ELL sta-                      0.05
tus, where most models incorrectly classify essays                                                                            BiScope (Essay) Glimpse
written by ELL students as machine-generated;                           0.00                                              RADAR
four models exhibit both significant coefficients                              0.2   0.3        0.4     0.5     0.6   0.7          0.8     0.9     1.0
and dominance analysis results. We further ana-                                                                 AUROC
lyze differences by model and attribute.                     Figure 1: Pseudo-R2 values from the regression analysis
                                                             plotted against AUROC scores for each model.
6.2 Model Analysis
Most models exhibit inconsistent and minor biases
                                                            and Glimpse models, as well as all three trained
across all categories. The two GPT-based mod-
                                                            variants, exhibit negative coefficients, which in two
els (Ghostbuster and Glimpse), as well as Binocu-
                                                            cases correspond with higher dominance values.
lars, RADAR, and the DeTeCtive (MAGE) variant,
tend to misclassify the disadvantaged population as          6.4                Overall Results
machine-generated, although the associated domi-
nance is often minimal: while the effects are statis-       From the regression analysis, we conclude the fol-
tically significant, the attribute plays only a minor       lowing: (1) ELL status appears to be a major con-
role in the resulting classification. FDG models            tributing factor, with ELL student essays more
are relatively inconsistent, while most trained mod-        likely to be classified as machine-generated, con-
els tend to misclassify essays from both ELL stu-           sistent with prior research; (2) economic status is
dents and those without economic disadvantages              an important variable, although results vary across
as machine-generated.                                       model types; and (3) there is relatively little evi-
                                                            dence of bias related to race or gender.
6.3 Attribute Analysis                                         We further examine model performance in re-
                                                            lation to overall bias. In Figure 1, we plot each
We observe relatively limited impact from gender
                                                            model’s AUROC score against its McFadden’s
and race in this analysis, though subgroup analysis
                                                            pseudo-R2 value from the regression analysis.
may provide more insight. While many models ex-
                                                            While R2 typically measures variance explained in
hibit significant coefficients, these are not reflected
                                                            linear regression, this approximation is used here
in the dominance analysis, suggesting a limited role
                                                            as a general indicator of bias in logistic regression
in classification decisions. The affected groups also
                                                            models. We observe a general negative correlation:
vary: different models and variants exhibit minor
                                                            as model performance (AUROC) increases, the esti-
biases in both directions.
                                                            mated bias (RM 2
                                                                             cF ) decreases (r = −0.486). This
   ELL status shows consistent negative effects:
                                                            trend suggests that higher-performing models may
ELL essays are more likely to be classified as
                                                            exhibit lower bias and thus reduce potential harms.
machine-generated by most models. While this
general trend aligns with prior research indicating          7             Subgroup Analysis
that ELL students are unfairly treated by detection
systems, we note that the magnitude of this effect          While regression analysis offers a broad overview
is typically small.                                         of biases by attribute, it may obscure subgroup-
   Economic status shows a relatively strong but            specific effects. To explore these, we partition the
mixed effect. Essays from students without eco-             dataset into 16 subgroups representing all com-
nomic disadvantage are more likely to be classified         binations of the four attributes under study. We
as machine-generated by BiScope and FDG models.             then perform pairwise z-tests comparing each sub-
However, other zero-shot and fine-tuned models              group’s scores with those of the remaining dataset,
present potential risks: the GPT-based Ghostbuster          identifying statistically significant differences in
                                                      2388
                Gender                 Male                                                  Female
                  Race       White           Non-White                           White                Non-White
                   ELL    No       Yes      No       Yes                    No         Yes           No       Yes
     Econ. Disadvantage No Yes No Yes No Yes No Yes                       No Yes     No Yes        No Yes No Yes
            Ghostbuster -.09      –    –    –    -.06    .06   .10    .15 -.16 –   –         –     -.11         –      .12     .13
                Glimpse -.05    -.03   –    –      –      –     –     .03 -.05 –   –         –       –         .02     .05     .07
             Binoculars .05       –    –    –      –    -.04    –    -.03 .05   –  –         –       –        -.04      –       –
        FDG (falcon-7b) .08       –    –    –      –    -.07    –      –   .08  –  –         –       –        -.07      –       –
          FDG (gpt-neo) .06       –    –    –      –    -.05    –      –   .05  –  –         –       –        -.06      –       –
         Zippy (LZMA) –         -.11   –    –      –    -.07   .14    .11   – -.10 –         –       –        -.08     .14     .12
         BiScope (Yelp) .07       –    –    –      –    -.05    –      –   .10  –  –         –       –        -.06      –       –
        BiScope (Arxiv) .05     -.04   –    –      –    -.05    –     .04 .06   –  –         –       –        -.07      –       –
        BiScope (Essay) .04       –    –    –      –      –     –      –   .04  –  –         –       –        -.04      –       –
     BiScope (Creative) .08     -.04   –    –      –    -.10    –      –   .13  –  –         –      .04       -.10      –       –
    DeTeCtive (MAGE) -.03       -.08   –   .10   -.04   -.06   .15    .16   – -.08 –         –     -.03       -.07     .15     .16
     DeTeCtive (M4GT) –           –    –    –      –      –     –      –    –   –  –         –       –          –       –       –
DeTeCtive (TuringBench) –         –    –    –      –    -.02    –      –   .01  –  –         –       –        -.01      –       –
                RADAR –         -.08   –    –      –    -.04    –      –   .07  –  –         –      .05         –       –       –
                 Desklib –        –    –    –      –      –     –      –    –   –  –         –       –          –       –       –
                 E5-lora -.03    .12   –    –      –     .14   .06    .08 -.18 – -.14        –     -.16         –       –       –

Table 4: Results for subgroup analysis: we report the differences in error from the given subgroup to those not in
that subgroup, with positive scores indicating the subgroup is more likely classified as machine generated and
 negative indicating the opposite. We report only statistically significant differences (p < 3.91e − 5).




                                                                                                                               AI/AN
classification. Results are presented in Table 4.
                                                                                                 H/L   A/PI     B/AA    Two+
   This analysis reveals several notable findings                                Model   W
not evident in the overall regression results. Al-                          Ghostbuster –     –   –    –    –   –
though ELL essays are generally more likely to be                              Glimpse -.05 .03 – .05 -.02 -.02
classified as machine-generated by a large number                            Binoculars –     –   –    –    –   –
                                                                        FDG (falcon-7b) .04 -.02 .06 -.07 -.01 .04
of models, this effect is disproportionately con-                        FDG (gpt-neo) .04 -.01 .02 -.06 -.02 .05
centrated among non-White students. Specifically,                        Zippy (LZMA) -.02 .05 .10 -.07 -.07 -.04
non-White ELL essays (n = 9, 443) are more fre-
                                                                         BiScope (Yelp) – -.00 –        –    –    –
quently misclassified by seven different models,                        BiScope (Arxiv) .02 -.01 .02 -.03 -.01 .01
compared to only one model for their White coun-                        BiScope (Essay) –      –    –   –    –    –
terparts (n = 1, 221). Moreover, this effect is more                 BiScope (Creative) –      –    –   –    –    –
                                                                    DeTeCtive (MAGE) -.06 .08 .05 -.04 -.06 .02
pronounced among males: three additional models                      DeTeCtive (M4GT) .01 -.01 .02 -.01 .01 -.01
exhibit significant differences for male non-White              DeTeCtive (TuringBench) – .01 .01 -.02 – .01
ELL essays compared to females.                                                 RADAR –        – .05 -.01 -.02 -.01
                                                                                 Desklib –     – -.01 – .01 .04
   We therefore need to revise our earlier assess-
                                                                                 E5-lora -.05 .04 -.09 .08 -.03 -.01
ment that bias related to race and gender is minimal.
Subgroup analysis suggests that both race and gen-             Table 5: Performance differences on race/ethnicity
der play a substantial role, highlighting the need             groups. Highlighted values indicate significance based
for more rigorous intersectional analysis when ap-             on z-scores between this attribute and the rest of the
proaching potential biases.                                    dataset (p < 1.04e − 4).
   For non-ELL essays, some differences are sig-
nificant, but results are inconsistent. Interestingly,
                                                               vs. non-White). Here, we extend our analy-
essays from ELL students with economic disad-
                                                               sis to explore individual race and ethnicity cate-
vantages are often less likely to be misclassified,
                                                               gories. The dataset includes six groups: White
though this outcome varies considerably by model.
                                                               (W), Hispanic/Latino (H/L), Asian/Pacific Islander
                                                               (A/PI), Black/African American (B/AA), Two
8   Race/Ethnicity
                                                               or More Races/Other (Two+), and American In-
We initially conducted analysis using a simpli-                dian/Alaskan Native (AI/AN). We evaluate model
fied binary race/ethnicity classification (White               performance on each individual group and compare
                                                         2389
                                                                                                      Race/Ethnicity
it against the full dataset in Table 5.


                                                                                                                        ELL Status    Econ. Status
   First, we note that no models exhibited signifi-

                                                                                Accuracy    Gender
cant performance differences for the AI/AN sub-
group, likely due to the small sample size (n =                     Annotator
208). This lack of significance should not be inter-
                                                                    Ann. 1      0.492       0.060    -0.069            0.013         0.150
preted as conclusive evidence of no bias, but rather                Ann. 2      0.449      -0.096    -0.033            0.131         0.011
as an indication that the dataset is underpowered                   Ann. 3      0.526      -0.011    -0.004            0.018         0.183
for detecting such effects. Further investigation
with more representative data is warranted.                     Table 6: Differences in human classifications based on
                                                                attributes. Positive numbers indicate the advantaged
   Two groups, however, show consistent dispari-
                                                                attribute is more likely classified as machine-generated;
ties: A/PI essays are more likely to be classified as           negative indicate the opposite. No results were indicated
machine-generated by most models, while B/AA                    as significant for p < .01.
essays are less likely to be misclassified in this
way. Results for H/L and W essays are inconsis-
tent, while the Two+ category shows significant
                                                                ing human performance: annotators performed at
negative effects in only two models.
                                                                approximately chance. However, we found no sig-
                                                                nificant differences in classification based on the
9       Human Performance
                                                                studied attributes. While slightly elevated coeffi-
Identifying machine-generated text remains a chal-              cients were observed for economic status (mirror-
lenging task for humans (Dugan et al., 2023; Etha-              ing trends in the system evaluations), these were
yarajh and Jurafsky, 2022; Clark et al., 2021). Lee             not statistically significant.
et al. (2025) finds that, even with the aid of collab-
orative tools, human accuracy in this task reaches
only 57%. We evaluate human performance with                    10      Conclusions
respect to potential bias: given the same dataset,
do human annotators exhibit biases comparable to                This work investigates bias in machine-generated
those observed in automated detection systems?                  text detection systems across four key attributes:
   To investigate this, we selected a balanced sub-             gender, race/ethnicity, ELL status, and economic
sample of our corpus consisting of 800 total texts,             status. We find that several models tend to dis-
with at least 100 examples from each group across               proportionately affect disadvantaged groups; es-
the four key attributes: gender (male/female), race             says written by ELL students are more frequently
(White/non-White), ELL status (ELL/non-ELL),                    misclassified as machine-generated, and this ef-
and economic status (disadvantaged/not disadvan-                fect is particularly pronounced among non-White
taged). For each text, we used Claude Sonnet 3.5                students. We also observe that while human an-
(Anthropic, 2024) to generate a continuation based              notators perform poorly at this task, they do not
on the first twenty tokens.6 This process resulted              exhibit significant biases.
in a dataset containing equal numbers of human-
                                                                   The key takeaway for practitioners is the critical
written and LLM-generated texts, balanced across
                                                                importance of understanding the behavior and limi-
all demographic categories.
                                                                tations of machine-generated text detection models.
   Three expert annotators were each assigned a                 Misclassification presents a substantial risk, not
subset of these texts (231 < n < 318), includ-                  only in this context but in other domains where
ing a minimum of 25 human-written samples for                   such models may be applied. Our findings show
each sensitive attribute. Annotators were instructed            no singular or consistent bias across all systems,
to classify each text as either human-written or                underscoring the need for case-by-case evaluation.
machine-generated. We then applied the same lo-                 To ensure fairness, models and their predictions
gistic regression analysis used in Section 6 to assess          must be carefully scrutinized for disproportionate
potential biases in human predictions. Performance              impacts on disadvantaged populations. AI develop-
differences are presented in Table 6.7                          ers and regulators can support this goal by creating
   Our results align with previous findings regard-             and adopting datasets and metrics such as those
    6
        See Appendix D for full prompt details.                 proposed here that allow for the detection and miti-
    7
        Full annotator details are provided in Appendix E.      gation of bias before real-world deployment.
                                                             2390
11   Limitations                                        area of research in bias in NLP. We sought to min-
                                                        imize methodological inconsistencies by follow-
This study represents an initial step in analyzing      ing the statistical framework proposed by Dayanik
bias in machine-generated text detection systems,       et al. (2022), whose work closely aligns with our
but it is necessarily constrained in several ways.      use case. However, we recognize that alternative
11.1 Models                                             methodologies could yield different insights.

We examine only a limited subset of models com-         11.5   Human Annotation
monly used for detecting machine-generated text.
                                                        Our human annotation effort involved only three ex-
Our selection criteria emphasized public availabil-
                                                        pert annotators. This limited scope was a function
ity, broad use, and general applicability. While we
                                                        of prioritizing expertise over general human judg-
aimed for methodological diversity, many relevant
                                                        ment. Although preliminary, our results suggest
models remain outside the scope of this analysis,
                                                        that human evaluators may introduce less bias than
and our findings should not be assumed to general-
                                                        automated systems. However, the small sample
ize across all possible systems.
                                                        size restricts the generalizability of this finding.
11.2 Dataset                                               Overall, we acknowledge that this study is con-
                                                        strained by time, resources, and dataset availability.
Our evaluation data is similarly constrained. It
                                                        Many of the questions raised here warrant further
consists entirely of student essay writing, drawn
                                                        investigation at larger scales and across more di-
from three datasets produced by the same organi-
                                                        verse settings.
zation. All datasets are in English, and written
by students in the United States. This choice was
driven by three considerations: (1) the datasets        References
are publicly available and include detailed demo-
graphic information (an uncommon feature); (2) we       Firoj Alam, Preslav Nakov, Nizar Habash, Iryna
                                                           Gurevych, Shammur Chowdhury, Artem Shelmanov,
had access to a corresponding machine-generated            Yuxia Wang, Ekaterina Artemova, Mucahid Kutlu,
dataset (OUTFOX), facilitating benchmarking; and           and George Mikros, editors. 2025. Proceedings of the
(3) the education domain represents a high-stakes         1stWorkshop on GenAI Content Detection (GenAIDe-
use case, where misclassification could cause sig-         tect). International Conference on Computational Lin-
                                                           guistics, Abu Dhabi, UAE.
nificant harm.
   The consequence of these advantages is limited       Anthropic. 2024. Claude 3.5 sonnet. https://www.
generalizability. Our findings may not extend to          anthropic.com/claude.
other text domains, and the dataset reflects a narrow
                                                        Guangsheng Bao, Yanbin Zhao, Juncai He, and Yue
slice of the broader population. Accordingly, the         Zhang. 2025. Glimpse: Enabling white-box methods
biases observed here may not reflect those that           to use proprietary models for zero-shot llm-generated
would occur when systems are evaluated on other           text detection. Preprint, arXiv:2412.11506.
demographics or styles of text.
                                                        Guangsheng Bao, Yanbin Zhao, Zhiyang Teng, Linyi
11.3 Categories of Gender and Race                        Yang, and Yue Zhang. 2024. Fast-detectgpt: Ef-
                                                          ficient zero-shot detection of machine-generated
We acknowledge concerns regarding binary gen-             text via conditional probability curvature. Preprint,
der labels and predefined racial categories, as ad-       arXiv:2310.05130.
dressed in Section 3, and this remains a limitation.    Marion Bartl, Abhishek Mandal, Susan Leavy, and
Prior work warns that such categorization may re-        Suzanne Little. 2025. Gender bias in natural lan-
inforce essentialist or harmful views of identity.       guage processing and computer vision: A compara-
We are constrained here by the demographic labels        tive survey. ACM Comput. Surv., 57(6).
provided in the datasets. Future research should
                                                        Laura Biester. 2025. Sports and women’s sports: Gen-
explore more inclusive and representative identity        der bias in text generation with olympic data. In
categorizations.                                          Proceedings of the 2025 Conference of the Nations
                                                          of the Americas Chapter of the Association for Com-
11.4 Statistical Methods                                  putational Linguistics: Human Language Technolo-
                                                          gies (Volume 2: Short Papers), pages 195–205, Al-
Numerous statistical approaches exist for evalu-          buquerque, New Mexico. Association for Computa-
ating model fairness, and this remains an active          tional Linguistics.
                                                    2391
Su Lin Blodgett, Solon Barocas, Hal Daumé III, and            Liam Dugan, Daphne Ippolito, Arun Kirubarajan,
  Hanna Wallach. 2020. Language (technology) is                 Sherry Shi, and Chris Callison-Burch. 2023. Real
  power: A critical survey of “bias” in NLP. In Pro-            or fake text? investigating human ability to detect
  ceedings of the 58th Annual Meeting of the Asso-              boundaries between human-written and machine-
  ciation for Computational Linguistics, pages 5454–            generated text. In Proceedings of the Thirty-
  5476, Online. Association for Computational Lin-              Seventh AAAI Conference on Artificial Intelligence
  guistics.                                                     and Thirty-Fifth Conference on Innovative Applica-
                                                                tions of Artificial Intelligence and Thirteenth Sympo-
Elizabeth Clark, Tal August, Sofia Serrano, Nikita              sium on Educational Advances in Artificial Intelli-
   Haduong, Suchin Gururangan, and Noah A. Smith.               gence, AAAI’23/IAAI’23/EAAI’23. AAAI Press.
   2021. All that’s ‘human’ is not gold: Evaluating
   human evaluation of generated text. In Proceedings         Economic Policy Institute. 2022. Racial and ethnic dis-
   of the 59th Annual Meeting of the Association for            parities in the united states: An interactive chartbook.
   Computational Linguistics and the 11th International         Updated November 2024.
   Joint Conference on Natural Language Processing
  (Volume 1: Long Papers), pages 7282–7296, Online.           Kawin Ethayarajh and Dan Jurafsky. 2022. The authen-
   Association for Computational Linguistics.                   ticity gap in human evaluation. In Proceedings of
                                                                the 2022 Conference on Empirical Methods in Nat-
S.A. Crossley, Y. Tian, P. Baffour, A. Franklin, M. Ben-        ural Language Processing, pages 6056–6070, Abu
  ner, and U. Boser. 2024. A large-scale corpus for             Dhabi, United Arab Emirates. Association for Com-
  assessing written argumentation: Persuade 2.0. As-            putational Linguistics.
  sessing Writing, 61:100865.
                                                              Anjalie Field, Su Lin Blodgett, Zeerak Waseem, and
Scott Crossley. 2024. The english language learner              Yulia Tsvetkov. 2021. A survey of race, racism, and
  insight, proficiency and skills evaluation (ellipse) cor-     anti-racism in NLP. In Proceedings of the 59th An-
  pus. International Journal of Learner Corpus Re-              nual Meeting of the Association for Computational
  search, 9(2).                                                 Linguistics and the 11th International Joint Confer-
                                                                ence on Natural Language Processing (Volume 1:
Scott A. Crossley, Perpetual Baffour, L. Burleigh, and          Long Papers), pages 1905–1925, Online. Association
  Jules King. 2025. A large-scale corpus for assessing          for Computational Linguistics.
  source-based writing quality: Asap 2.0. Assessing
  Writing, 65:100954.                                         Hanxi Guo, Siyuan Cheng, Xiaolong Jin, Zhuo Zhang,
                                                                Kaiyuan Zhang, Guanhong Tao, Guangyu Shen, and
Paula Czarnowska, Yogarshi Vyas, and Kashif Shah.               Xiangyu Zhang. 2024a. Biscope: Ai-generated text
  2021. Quantifying social biases in nlp: A generaliza-         detection by checking memorization of preceding
  tion and empirical comparison of extrinsic fairness           tokens. In Advances in Neural Information Process-
  metrics. Transactions of the Association for Compu-           ing Systems (NeurIPS), volume 37, pages 104065–
  tational Linguistics, 9:1249–1267.                            104090.

Erenay Dayanik, Ngoc Thang Vu, and Sebastian Padó.            Xun Guo, Shan Zhang, Yongxin He, Ting Zhang,
  2022. Bias identification and attribution in NLP mod-         Wanquan Feng, Haibin Huang, and Chongyang
  els with regression and effect sizes. Northern Euro-          Ma. 2024b. Detective: Detecting ai-generated
  pean Journal of Language Technology, 8.                       text via multi-level contrastive learning. Preprint,
                                                                arXiv:2410.20964.
Desklib. 2025. ai-text-detector: Ai-generated text de-
  tection model. Accessed: 2025-07-10.                        Hans W. A. Hanley and Zakir Durumeric. 2024.
                                                                Machine-made media: Monitoring the mobiliza-
Sunipa Dev, Masoud Monajatipoor, Anaelia Ovalle, Ar-            tion of machine-generated articles on misinforma-
  jun Subramonian, Jeff Phillips, and Kai-Wei Chang.            tion and mainstream news websites. Preprint,
  2021. Harms of gender exclusivity and challenges in           arXiv:2305.09820.
  non-binary representation in language technologies.
  In Proceedings of the 2021 Conference on Empiri-            Alex Hanna, Remi Denton, Andrew Smart, and Jamila
  cal Methods in Natural Language Processing, pages             Smith-Loud. 2020. Towards a critical race method-
  1968–1994, Online and Punta Cana, Dominican Re-               ology in algorithmic fairness. In Proceedings of the
  public. Association for Computational Linguistics.            2020 Conference on Fairness, Accountability, and
                                                                Transparency, FAT* ’20, page 501–512, New York,
Liam Dugan, Alyssa Hwang, Filip Trhlík, Andrew                  NY, USA. Association for Computing Machinery.
  Zhu, Josh Magnus Ludan, Hainiu Xu, Daphne Ip-
  polito, and Chris Callison-Burch. 2024. RAID: A             Abhimanyu Hans, Avi Schwarzschild, Valeriia
  shared benchmark for robust evaluation of machine-            Cherepanova, Hamid Kazemi, Aniruddha Saha,
  generated text detectors. In Proceedings of the 62nd          Micah Goldblum, Jonas Geiping, and Tom Goldstein.
  Annual Meeting of the Association for Computational           2024. Spotting llms with binoculars: zero-shot
  Linguistics (Volume 1: Long Papers), pages 12463–             detection of machine-generated text. In Proceedings
  12492, Bangkok, Thailand. Association for Compu-              of the 41st International Conference on Machine
  tational Linguistics.                                         Learning, ICML’24. JMLR.org.
                                                          2392
Xiaomeng Hu, Pin-Yu Chen, and Tsung-Yi Ho. 2023.                real: Deepfake moderation mistakes and identity-
  Radar: Robust ai-text detection via adversarial learn-        based bias. In Proceedings of the 2024 CHI Confer-
  ing. In Advances in Neural Information Processing             ence on Human Factors in Computing Systems, CHI
  Systems, volume 36, pages 15077–15095. Curran As-             ’24, New York, NY, USA. Association for Computing
  sociates, Inc.                                                Machinery.
Srinivasan Iyer, Xi Victoria Lin, Ramakanth Pasunuru,       Yikang Pan, Liangming Pan, Wenhu Chen, Preslav
   Todor Mihaylov, Daniel Simig, Ping Yu, Kurt Shuster,       Nakov, Min-Yen Kan, and William Wang. 2023. On
   Tianlu Wang, Qing Liu, Punit Singh Koura, Xian Li,         the risk of misinformation pollution with large lan-
   Brian O’Horo, Gabriel Pereyra, Jeff Wang, Christo-         guage models. In Findings of the Association for
   pher Dewan, Asli Celikyilmaz, Luke Zettlemoyer,            Computational Linguistics: EMNLP 2023, pages
   and Ves Stoyanov. 2023. Opt-iml: Scaling language          1389–1403, Singapore. Association for Computa-
   model instruction meta learning through the lens of        tional Linguistics.
   generalization. Preprint, arXiv:2212.12017.
                                                            Flor Miriam Plaza-del Arco, Amanda Cercas Curry,
Yan Ju, Shu Hu, Shan Jia, George H. Chen, and Siwei           Alba Curry, Gavin Abercrombie, and Dirk Hovy.
  Lyu. 2024. Improving fairness in deepfake detection.        2024. Angry men, sad women: Large language mod-
  In Proceedings of the IEEE/CVF Winter Conference            els reflect gendered stereotypes in emotion attribution.
  on Applications of Computer Vision (WACV), pages            In Proceedings of the 62nd Annual Meeting of the
  4655–4665.                                                  Association for Computational Linguistics (Volume 1:
                                                              Long Papers), pages 7682–7696, Bangkok, Thailand.
Minseok Jung. 2025. Responsible computational text            Association for Computational Linguistics.
  generation: Ai content classification and policy
  framework. Master’s thesis, Massachusetts Institute       Felipe Romero-Moreno. 2025. Deepfake detection in
  of Technology, Cambridge, MA, February.                     generative ai: A legal framework proposal to protect
                                                              human rights. Computer Law & Security Review,
Vinaya Sree Katamneni, Aakash Varma Nadimpalli,               58:106162.
  and Ajita Rattani. 2024. Demographic fairness and
  accountability of audio- and video-based unimodal         Beatrice Savoldi, Marco Gaido, Luisa Bentivogli, Mat-
  and bi-modal deepfake detectors. Face Recognition           teo Negri, and Marco Turchi. 2021. Gender bias in
  Across the Imaging Spectrum, pages 205–231.                 machine translation. Transactions of the Association
                                                              for Computational Linguistics, 9:845–874.
Ryuto Koike, Masahiro Kaneko, and Naoaki Okazaki.
  2024. Outfox: Llm-generated essay detection               Karolina Stanczak and Isabelle Augenstein. 2021. A
  through in-context learning with adversarially gener-       survey on gender bias in natural language processing.
  ated examples. Proceedings of the AAAI Conference           Preprint, arXiv:2112.14168.
  on Artificial Intelligence, 38(19):21258–21266.
                                                            Thinkst. 2023. Meet zippy: A fast ai/llm text detector.
Jooyoung Lee, Xiaochen Zhu, Georgi Karadzhov,                 Accessed: 12/03/2025.
  Tom Stafford, Andreas Vlachos, and Dongwon Lee.
                                                            Vivek Verma, Eve Fleisig, Nicholas Tomlin, and Dan
  2025. Collaborative evaluation of deepfake text with
                                                              Klein. 2024. Ghostbuster: Detecting text ghostwrit-
  deliberation-enhancing dialogue systems. Preprint,
                                                              ten by large language models. In Proceedings of
  arXiv:2503.04945.
                                                              the 2024 Conference of the North American Chap-
Weixin Liang, Mert Yuksekgonul, Yining Mao, Eric              ter of the Association for Computational Linguistics:
 Wu, and James Zou. 2023. Gpt detectors are bi-               Human Language Technologies (Volume 1: Long
 ased against non-native english writers. Patterns,           Papers), pages 1702–1717, Mexico City, Mexico. As-
 4(7):100779. Accessed: 2025-03-12.                           sociation for Computational Linguistics.

Decheng Liu, Zongqi Wang, Chunlei Peng, Nannan              Junchao Wu, Shu Yang, Runzhe Zhan, Yulin Yuan,
  Wang, Ruimin Hu, and Xinbo Gao. 2025. Thinking              Lidia Sam Chao, and Derek Fai Wong. 2025. A
  racial bias in fair forgery detection: Models, datasets     survey on LLM-generated text detection: Necessity,
  and evaluations. Proceedings of the AAAI Confer-            methods, and future directions. Computational Lin-
  ence on Artificial Intelligence, 39(5):5379–5387.           guistics, 51(1):275–338.

Jesse G Meyer, Ryan J Urbanowicz, Patrick CN Mar-           A     Data
   tin, Karen O’Connor, Ruowang Li, Pei-Chen Peng,
   Tiffani J Bright, Nicholas Tatonetti, Kyoung Jae         Statistics for the human-written dataset that was
  Won, Graciela Gonzalez-Hernandez, and Jason H             curated for our experiments are shown in Table 7.
   Moore. 2023. Chatgpt and large language models
   in academia: opportunities and challenges. BioData       B     System Descriptions
   Mining, 16(1):20.
                                                            B.1    Ghostbuster
Jaron Mink, Miranda Wei, Collins W. Munyendo, Kurt
   Hugenberg, Tadayoshi Kohno, Elissa M. Redmiles,          We use the implementation provided at https://
   and Gang Wang. 2024. It’s trying too hard to look        github.com/vivek3141/ghostbuster. This was
                                                        2393
                                Gender          Race/Ethnicity             ELL         Economic Disadvantage
                     Total   Male  Female      White Nonwhite         No         Yes    No          Yes
 PERSUADE V 2.0     24695    12074    12621    11282      13413      22451   2244      11003      13692
 ASAP V 2.0         24728    12498    12230     9841      14887      20991   3737       7933      16795
 ELLIPSE             6482     3636     2846      471       6011        0     6482       1974       4508
 Combined (clean)   41743    21277    20466    15078      26665      31079   10664     18188      23555

Table 7: Counts for each attribute in our combined corpus. Note that the ELLIPSE corpus is designed to capture ELL
speakers, and thus contains only that group.


modified to fix an issue where outdated OpenAI             B.9     Desklib (Desklib, 2025)
models were referenced; we use davinci-002 and            We use the implementation provided at https://
babbage-002 models.                                       github.com/desklib/ai-text-detector.
B.2   Glimpse                                              B.10     E5-lora (Dugan et al., 2024)
We use the implementation provided at https://            We     use    the    implementation        provided
github.com/baoguangsheng/glimpse.                         at         https://github.com/menglinzhou/
                                                          e5-small-lora-ai-generated-detector.
B.3   Binoculars (Hans et al., 2024)                      The creators indicate the desired citation is for the
We use the implementation provided at https://            RAID dataset.
github.com/ahans30/Binoculars.                             B.11     Architecture/Costs
B.4   Fast-DetectGPT (Bao et al., 2024)                    For model training, inference, and evaluation we
                                                           use Amazon AWS EC2 instances. We use the
We use two settings that use different models for          g6e.xlarge instance type. This instance type has
scoring: gpt-neo-2.7b for speed and falcon-7b              an NVIDIA L40S Tensor Core GPU with 48 GB
for maximal accuracy.                                      of GPU memory, allowing us to experiment with
   We use the implementation provided                      models that have larger GPU memory requirements
at       https://github.com/baoguangsheng/                 (notably Binoculars and the FDG systems require
fast-detect-gpt.                                           significant GPU memory).
                                                              Running all models over our dataset requires
B.5   Zippy (Thinkst, 2023)                                approximately 6 hours of machine time, costing
We use the implementation provided at https://             approximately $12 USD. We additionally spent
github.com/thinkst/zippy. We experimented                  approximately $200 USD for OpenAI model usage,
with the LZMA and ensemble versions, and found             required for the Ghostbuster and Glimpse models.
no significant differences in performance.
                                                           C      Correlations
B.6   BiScope (Guo et al., 2024a)                          Figure 2 shows a heatmap of correlations between
We use the implementation provided at https:               model predictions.
//github.com/MarkGHX/BiScope: they do not
provide an explicit "best" model for each domain,          D      Prompts
so we train each of our four variants using all the       We utilize the following prompt to interface with
provided data from the respective domains.                the language model (Claude 3.5). The prompt asks
                                                          for completion of a given student essay. That essay
B.7   DeTeCtivE (Guo et al., 2024b)                       is trimmed to the first 20 tokens, which are pro-
We use the implementation provided at https://            vided to the model with the instruction to complete
github.com/heyongxin233/DeTeCtive.                        the text. The model is instructed to limit the output
                                                          to the length of the original essay, while mimicking
B.8   RADAR (Hu et al., 2023)                             the style of a student:
We use the implementation provided at https://             Here is the start of a student's essay.
github.com/IBM/RADAR.                                      Complete the essay. It should be at
                                                       2394
            Ghostbuster                               1.0
                Glimpse                                      annotations were completed. This prevented any
              Binoculars                              0.8
        FDG (falcon-7b)                                      type of bias in having authors perform annotation.
          FDG (gpt-neo)                               0.6
           Zippy (LZMA)
          BiScope (Yelp)
                                                             After annotations were completed, the annotators
         BiScope (Arxiv)                              0.4    were able to make significant contributions to the
        BiScope (Essay)
     BiScope (Creative)                               0.2    analysis and writing of the paper, and given the
     DeTeCtive (MAGE)
     DeTeCtive (M4GT)
DeTeCtive (TuringBench)                               0.0    amount of work and the level of contribution they
                 RADAR
                 Desklib                               0.2   made, we believed the best way to credit their work
                 E5-lora
                                       Ghostbuster
                                           Glimpse
                                                             and contribution was to include them as authors.
                                         Binoculars
                                   FDG (falcon-7b)
                                     FDG (gpt-neo)
                                      Zippy (LZMA)
                                     BiScope (Yelp)
                                    BiScope (Arxiv)
                                   BiScope (Essay)
                                BiScope (Creative)
                                DeTeCtive (MAGE)
                                DeTeCtive (M4GT)
                           DeTeCtive (TuringBench)
                                            RADAR
                                            Desklib
                                            E5-lora

Figure 2: Pearson correlation for the predictions for
each model.


most {len(text.split())} words long.
Do not go over this requirement.
Emulate the style of a student between
6th and 12th grade. You may include
some common misspellings and
punctuation errors, so that the text
looks like a students.
Start:
{' '.join(text.split()[:20])}

Return only the resulting text as a
json object:
{{\"text\":\"<generation>\"}}
Ensure the result is under
{len(text.split())} tokens."}

E      Annotators
We recruited three annotators through personal re-
quests for our experiments. These annotators are
professionals with previous work in the field of
deepfake detection, and consented to their results
being used individually. All three annotators are
post-graduate educated, fluent English speakers.
Each annotator was given a batch of samples with
the instruction to classify each sample as either
human-written or machine-generated. Annotators
were compensated as part of salaried work at a rate
above minimum wage.
   After completion of their individual tasks, we
decided to involve the annotators as authors on the
paper. Note that the annotators had no informa-
tion about the project before their annotations were
completed (which models, prompts, and datasets
were used, what the goal of the project was, etc.):
they were kept entirely independent until after their
                                                        2395


## Responsible NLP Checklist full text

- **Canonical URL:** https://aclanthology.org/attachments/2026.acl-long.109.checklist.pdf
- **Retrieved:** 2026-07-14
- **Extraction method:** First-party two-page ACL PDF downloaded with `curl` and extracted with Poppler `pdftotext -layout`; no OCR was used

Responsible NLP Checklist

Paper title: Identifying Bias in Machine-generated Text Detection

Authors: Kevin Stowe, Svetlana Afanaseva, Rodolfo C. Raimundo, yitao sun, Kailash Patil

How to read the checklist symbols:

✓ the authors responded ‘yes’

✗ the authors responded ‘no’

N/A the authors indicated that the question does not apply to their work

the authors did not respond to the checkbox question

For background on the checklist and guidance provided to the authors, see the Responsible NLP Checklist page at ACL Rolling Review.

✓ A. Questions mandatory for all submissions.

✓ A1. Did you describe the limitations of your work?

This paper has a Limitations section.

✓ A2. Did you discuss any potential risks of your work?

Section 11

✓ B. Did you use or create scientific artifacts? (e.g. code, datasets, models)

✗ B4. Did you discuss the steps taken to check whether the data that was collected/used contains any information that names or uniquely identifies individual people or offensive content, and the steps taken to protect/anonymize it?

We do not release any or modify the data, which contains no identifying information. There may be offensive content, but it is necessary to include all types of text in the analysis, and we do not propagate it in any way.

✓ B6. Did you report relevant statistics like the number of examples, details of train/test/dev splits, etc. for the data that you used/created?

Section 3

✓ C. Did you run computational experiments?

✓ C2. Did you discuss the experimental setup, including hyperparameter search and best-found hyperparameter values?

Our experimental setup is throughout the paper. We did not tune any models with hyperparameters or do any training that would require it.

✓ C3. Did you report descriptive statistics about your results (e.g., error bars around results, summary statistics from sets of experiments), and is it transparent whether you are reporting the max, mean, etc. or just a single run?

Descriptive statistics form the core of the experiments throughout the paper.

✓ D. Did you use human annotators (e.g., crowdworkers) or research with human subjects?

✓ D1. Did you report the full text of instructions given to participants, including e.g., screenshots, disclaimers of any risks to participants or annotators, etc.?

Our instructions were simply to identify whether a given text is machine-generated or human-written; this is reported in Appendix E

The Responsible NLP Checklist used at ACL Rolling Review is adopted from NAACL 2022, with the addition of ACL 2023 question on AI writing assistance and further refinements based on ARR practice. ACL 2026 used a subset of ARR checklist form.

✓ D2. Did you report information about how you recruited (e.g., crowdsourcing platform, students) and paid participants, and discuss if such payment is adequate given the participants’ demographic (e.g., country of residence)?

Appendix E

✓ D3. Did you discuss whether and how consent was obtained from people whose data you’re using/curating (e.g., did your instructions explain how the data would be used)?

Appendix E

✗ D4. Was the data collection protocol approved (or determined exempt) by an ethics review board?

Annotators were recruited personally, yielding minimal risk of ethical issues.

✓ E. Did you use AI assistants (e.g., ChatGPT, Copilot) in your research, coding, or writing?

✗ E1. If you used AI assistants, did you include information about their use?

Per the ACL Policy on Writing Assistance, we used (a) Assistance purely with the language of the paper and (b) short form input assistance.

## Extraction verification

- **Beginning checked:** Rendered PDF page 1 was compared with the extraction; title, authors, abstract, Introduction, research questions, footnote 1, proceedings footer, and page number are present.
- **Middle checked:** Rendered PDF page 7 was compared with the extraction; Table 4, its caption and significance threshold, subgroup-analysis prose, Section 8, and Table 5 are present. Color direction coding is not represented in the plain text, but the caption and prose state the direction and the PDF attachment preserves the visual table.
- **End checked:** Rendered PDF page 13 was compared with the extraction; Figure 2, Appendix D prompt, and Appendix E annotator details continue through page 2395.
- **Checklist checked:** `pdfinfo` reports two A4 pages for the Responsible NLP Checklist. Its extraction includes responses for limitations and risks, scientific artifacts and data/content checks, computational experiments, annotator instructions/recruitment/consent and ethics review, and AI-assistant use.
- **Structure checked:** `pdfinfo` reports 13 A4 pages for the paper. The paper extraction includes Sections 1-11; Tables 1-7; Figures 1-2; footnotes; Limitations subsections 11.1-11.5; References; and Appendices A-E in the same order as the PDF.
- **Known omissions:** No paper or checklist source text is omitted. Figure pixels, table colors, checkbox typography, and exact page typography are not reproduced in Markdown; they remain available in the preserved PDF attachments.

## Preserved attachments

| Path | Role in the source | SHA-256 | Preservation / extraction notes |
|---|---|---|---|
| `snapshots/attachments/stowe-detector-bias-acl-2026.pdf` | Authoritative ACL proceedings PDF, including figure pixels and table color/direction markers | `ad67e403b47de2b9fb994eca748da510df27dc3a5df9f163ac8ec1c7804762c3` | Downloaded directly from the ACL Anthology PDF URL on 2026-07-14; 13 pages; used for layout extraction and rendered-page verification. |
| `snapshots/attachments/stowe-detector-bias-responsible-nlp-checklist.pdf` | Authoritative ACL Responsible NLP Checklist associated with the paper | `d9d707c212f0682fb25009ff970d134af471cbec2bf8a62c5a56cb2d9f136506` | Downloaded directly from the ACL Anthology checklist URL on 2026-07-14; 2 pages; complete text extracted above with `pdftotext -layout`. |
