# Domain Regeneration: How well do LLMs match syntactic properties of text domains?

- **Canonical URL:** https://aclanthology.org/2025.findings-acl.120/
- **Alternate access URLs:**
  - https://aclanthology.org/2025.findings-acl.120.pdf
  - https://export.arxiv.org/api/query?id_list=2505.07784
  - https://arxiv.org/pdf/2505.07784v2
- **Author / owner:** Da Ju, Hagen Blix, and Adina Williams
- **Publisher:** Association for Computational Linguistics
- **Published:** 2025-07
- **Retrieved:** 2026-07-15
- **Stable identifier:** ACL Anthology ID 2025.findings-acl.120; DOI 10.18653/v1/2025.findings-acl.120; arXiv:2505.07784v2
- **Version / revision:** authoritative 22-page ACL 2025 proceedings PDF, compared with arXiv v2 updated 2025-06-02
- **Extraction method:** official ACL PDF downloaded with curl; PDF metadata and image inventory inspected with Poppler pdfinfo and pdfimages; all 22 pages converted from the embedded text layer with Poppler pdftotext -layout; pages 1, 5-8, 11, and 22 rendered with pdftoppm and visually checked; current ACL HTML metadata, arXiv API metadata, and the arXiv v2 PDF cross-checked
- **Full-text status:** complete
- **Access and transformation notes:** The authoritative ACL PDF and arXiv v2 PDF are preserved as attachments. The ACL and arXiv landing-page/API abstracts still say two domains, while both full PDFs say three domains and include ELI5. The plain-text extraction retains page breaks, table text, captions, references, prompts, examples, and appendices; PDF column order, line wrapping, and hyphenation remain visible. Plot artwork and colour encodings are preserved in the PDFs rather than recreated in Markdown. No source pages are omitted.

## Full text

The following is the complete Poppler `pdftotext -layout` extraction of the authoritative ACL proceedings PDF.

```text
                         Domain Regeneration:
        How well do LLMs match syntactic properties of text domains?

             Da Ju                               Hagen Blix                          Adina Williams
            Meta AI                           New York University                     FAIR, Meta AI
         daju@meta.com                       hagen.blix@nyu.edu                  adinawilliams@meta.com



                      Abstract                               far as one could, from a zoomed out perspective,
                                                             describe the entire process of pretraining itself as
    Recent improvements in large language model
                                                             a process of fitting a model to a distribution. How-
    performance have, in all likelihood, been ac-
    companied by improvements in how well they
                                                             ever, it is also possible that the increasing number
    can approximate the distribution of their train-         of post-training interventions, such as instruction
    ing data. In this work, we explore the following         tuning, automatic preference alignment or other
    question: which properties of text domains do            kinds of interventions, could affect this.
    LLMs faithfully approximate, and how well do                Other model design decisions can also impact
    they do so? Applying observational approaches            a models’ ability to match a human-generated
    familiar from corpus linguistics, we prompt              distribution. LLMs can suffer from model col-
    commonly used, opensource LLMs to regen-
                                                             lapse (Dohmatob et al., 2024; Hamilton, 2024;
    erate text from three domains of permissively
    licensed English text which are often contained          Lanchantin et al., 2025), whereby the model has
    in LLM training data—Wikipedia, news text,               trained on outputs from previous models, which
    and ELI5. In a fairly semantically-controlled            can negatively affect the diversity and quality of
    setting, this regeneration paradigm allows us to         generations. Even without being trained on syn-
    investigate whether LLMs can faithfully match            thetic data, models can fail to match the diversity of
    original human text domains. We investigate              human-generated data. LLMs often generate sim-
    varying levels of syntactic abstraction, from
                                                             ilar data patterns (Hupkes et al., 2023). They can
    simpler properties like sentence length, and ar-
    ticle readability, to more complex and higher
                                                             repeat words/tokens (Juzek and Ward, 2024), use
    order properties such as dependency tag distri-          less diverse topics (Bache et al., 2013; Alihosseini
    bution, parse depth, and parse complexity. We            et al., 2019) or both (Padmakumar and He, 2023).
    find that the majority of the regenerated distri-           However, most work investigating the ability of
    butions show a shifted mean, a lower standard            LLMs to match the diversity of human written text
    deviation, and a reduction of the long tail, as          does so in the context of an unspecified and un-
    compared to the human originals.                         controlled “neutral” domain. Given that there are
                                                             many, widely described differences in lexical con-
1   Introduction
                                                             tent, style, syntactic structure etc. across domains
The question of whether models can transfer ca-              (Biber, 1991; DiMarco and Hirst, 1993; Dewdney
pabilities across different domains of texts, or do-         et al., 2001; Lee, 2002; Williams et al., 2018; Li
main transfer has a long history in NLP. Domain              et al., 2019), one might wonder whether models can
considerations have contributed greatly to the es-           match human diversity in domains with consistent
tablishment of the pretrain-finetune paradigm (De-           and well controlled style.
vlin et al., 2019; Liu et al., 2019) used for train-            We explore this question with a paradigm that
ing LLMs (Ruder et al., 2019). Since the rise in             we call LLM-regeneration: using the beginning
prevalence of LLMs, however, there has been little           of articles from a well-described domain (e.g.
work explicitly verifying whether state-of-the-art           Wikipedia, Fan and Gardent 2022), we prompt the
LLMs can actually generate text that matches dif-            LLM to complete the article, and then compare
ferent, well-described, and well-delineated human-           the regenerated article to the original. This setting
generated text domains.                                      allows us to exert more control over the content of
   One might presume that LLMs should be gener-              the generations, thus making for a clearer picture
ally competent in matching text distributions, inso-         of distribution match.
                                                        2367
                 Findings of the Association for Computational Linguistics: ACL 2025, pages 2367–2388
                       July 27 - August 1, 2025 ©2025 Association for Computational Linguistics
   We use this regenerated data to explore the diver-   our experiments as an additional comparison for
sity of model outputs in a number of interrelated       the model-specificity of our results. We addition-
syntactic measurements. Beyond diversity, we also       ally investigate two models from the Mistral fam-
explore two other signatures of imperfect domain        ily: Mistral-Small-24B-Intruct1 and Ministral-8B-
matching in this work: difference in the means of       Instruct2 to verify that our findings hold across
the LLM and human distributions, and a reduced          model family and size.
long tail where present in the human distribution.
When present, we take each of these three signa-        2.2    Data
tures to be evidence that the LLMs we study fail to     We are interested in whether SOTA or near-SOTA
perfectly match the human text.                         LLMs can match properties of text corresponding
   While past work has indicated that some LLMs         to its domain, and thus need to select datasets that
generate more homogeneous syntax than humans            typify domains. However, some practical com-
(Shaib et al., 2024), such investigations have thus     plications arose when we embarked on selecting
far been restricted to part-of-speech tags, and have    datasets. First of all, we needed to consider which
only been explored for “neutral” domain LLM gen-        text the model was trained on. In principle, if a
erations. Here, we combine investigations of text       model was trained on text from a domain, it should
domain with syntactic complexity metrics in an at-      be better at matching the distributional properties of
tempt to delimit a reasonably sized problem space;      text from that domain. However, the precise nature
in addition to text readability and sentence length,    of the training data for LLMs is generally propri-
we explore more abstract metrics for syntactic com-     etary information, though it is likely that LLMs
plexity, including parse depth, unique dependency       were trained on many domains. Clearly, it would
tag and constituency label count, and Yngve scores.     not be scalable to investigate all of them (nor to
   Overall, the contributions of this work are:         determine where their boundaries lay).
(i) We define an experimental setting called LLM-          Additionally, we could, in principle, select a set
regeneration that enables us to measure how well        of data and train an LLM from scratch on it. How-
LLMs match human text with some controls over           ever, due to budgetary constraints, we would doubt-
semantics and domain. (ii) We investigate the ex-       less have to focus on a smaller, and likely less per-
tent to which LLMs can match the distribution of        formant model. In that case, if we observed differ-
text from three well-described human domains. (iii)     ences between the human and model distributions,
We illustrate three signatures of domain mismatch—      those differences could just be due to the model
diversity, mean shift, and reduction of the long        being weak, not to anything interesting about the
tail—and show how the three are present for sev-        distributions the model had learned.
eral syntactic complexity metrics, as calculated           Given these considerations, we made the prac-
on generations from opensource models from two          tical decision to focus on Wikipedia, a datasource
model families. These results are important, as they    known to be used in open training datasets (Big-
can inform us about whether models can genuinely        Science Workshop et al., 2023; Soldaini et al.,
match text domains. Information about whether           2024) and to be a popular and well-studied data
LLMs differ in syntactic complexity and variabil-       source for many NLP applications in English (Wu
ity from human-generated text may additionally be       and Weld, 2010; Horn et al., 2014; Ni and Florian,
useful for detection of synthetic text, or to guide     2016; Yang et al., 2018; Dinan et al., 2019; Klang
model improvement.                                      and Nugues, 2019; Ein-Dor et al., 2019; Dinan
                                                        et al., 2020; Nie et al., 2020; Calixto et al., 2021;
2   Methods                                             Eisenschlos et al., 2021; Petroni et al., 2021; Sem-
                                                        nani et al., 2023). As additional domains, we also
2.1 Models                                              investigate the standard news articles dataset, CC-
In this work, we mostly utilize the Llama family        News3 , and “Explain Like I’m 5” dataset (ELI5;
of models, as they are strongly performing mod-         Fan et al. 2019) of simply written questions and
els with open weights. For the majority of our          answers from an online forum.
experiments, we utilize Llama-V2 (Touvron et al.,          Despite their difference in size (our Wikipedia
2023) 70B instruction finetuned. We also utilize           1
                                                             mistralai/Mistral-Small-24B-Instruct-2501
Llama-V3.3 instruction finetuned (Llama Team,              2
                                                             mistralai/Ministral-8B-Instruct-2410
2024) 70B and Llama-V3.1-8B for a subset of                3
                                                             https://huggingface.co/datasets/vblagoje/cc_news

                                                   2368
datasets contains roughly 10x more data than              (since news articles are shorter on average). For
CCNews, and CCNews is larger than ELI5), all              ELI5, we prompt the models only with the title
datasets are representative of consistent and fairly      of the thread (e.g., What is an ETF?). We then
well circumscribed domains. All three datasets are        feed these into the model using the prompts in Ap-
characterized by internally enforced stylistic stan-      pendix B. We use vLLM (Kwon et al., 2023) for
dards (e.g., due to editors or moderators), and any       generation with its default coding configurations,
competent reader could easily match text to the rele-     including a temperature of 1.0, which is considered
vant domain. That is, their differences should allow      a “medium” temperature. The resulting articles
us to determine whether some of the trends we find        will be approximately matched to the original arti-
for Wikipedia are specific to that data source or         cles in their topic and content. We collect all the
more general.                                             articles in each domain, which then serve as our re-
                                                          generated corpus for downstream analysis. We also
2.3 Data Processing                                       performed the two data cleaning steps described
Data Cleaning. Given that Wikipedia data con-             above on the model-regenerated data as well.
tains a significant amount of structured text, such
                                                          2.4   Parsing
as lists, titles, urls and citations, we perform a data
cleaning stage using the parsing results we col-          We employ the data processing pipeline outlined by
lected to enhance signal quality. First, we removed       Williams et al. (2021) and used in Ju et al. (2024)
all sentences with fewer than 3 words or more than        for our analysis. Our pipeline uses the Stanza tool
500 words. Second, we eliminated all sentences            (Qi et al., 2020) to process the sentences and gen-
that contained neither a verb nor an auxiliary verb,      erate dependency and constituency parses for later
as identified by POS tagging, to ensure that our          analysis. The pipeline consists of:
data consists of full English sentences. To verify           1. Tokenization & Sentence Segmentation
that these filtering steps didn’t drive our main re-         2. Dependency Parsing: We use the default
sults, we plot data ablation results in Appendix A,       parser (Chen and Manning, 2014) to dependency
which show the same trends as our main results.           parse all text in our experiments.
   Note that additional data cleaning is an implicit         3. Constituency Parsing: In addition to depen-
part of our process. We calculate all metrics based       dency parsing, we construct a constituency parse
on successful Stanza dependency and constituency          for each sentence, which is subsequently used to
parsing. Metrics will not be available if an article is   compute our metrics.
empty in the source data, or contains non-English            Rarely, a portion of the parsing pipeline would
content. Some metrics, such as the depth score            fail (for example, if the sentence in question was
and Yngve score, may encounter errors if the tree         merely a set of hyperlinks in the case of some of
parsing is excessively deep. In cases where articles      the Wikipedia data). In that case, the data point
pass the parsing stage but have a valid article length    would be excluded from our analysis. Details on
of zero (meaning the article is not empty in the          exclusions can be found in Appendix A.
beginning, but all sentences have been removed due
                                                          2.5   Metrics
to prior length and POS filtration), we filter out all
depth and Yngve scores of zero. For sentence-level        For the majority of our experiments, we plot the dis-
metrics, we aggregate results from all successfully       tribution of binned scores so that we can compare
parsed sentences to complete the calculations. For        the regenerated data to the human data for both do-
metrics aggregated at the article level, we exclude       mains. For all metrics, we observe approximately
any article if any of its sentences fail in parsing or    Gaussian distributions for both the original human
metric calculation.                                       data and the regenerated data. We plot the over-
                                                          all normal fit line, as calculated by the defaults
Regenerating the Data with LLMs. To generate              in Seaborn (Waskom, 2021) using matplotlib
text from the models that replicates our domains of       (Hunter, 2007) for easy visual inspection.
interest, we adopt a similar approach to that used           Comparing the human data and the LLM-
in Ju et al. (2024) to ensure that the article topic      regenerated data, we isolate three observational
and content do not vastly differ. We isolate the          signatures of domain shift that recur across metrics:
first 256 words from a Wikipedia article, and the         the human and the regenerated distributions can dif-
first 180 words from a CCNews article respectively        fer in mean, they can differ in variance, and they
                                                      2369
             Metric                      Signature                2.5.1 Syntactic Metrics
 Type                  Domain      µ     σ     Long Tail          For the other four metrics, we relied on syntac-
                       news       ≈     ↘      reduced            tic parses, generated following the procedure we
 Flesch-Kincaid        wiki       ↗     ↘      reduced            described above in §2.4. Unlike for the Flesch-
                       ELI5       ↘     ↘      reduced
                                                                  Kincaid score, for all syntactic metrics, we cal-
                       news       ↗     ↘         n/a
 Dependency            wiki       ≈     ↘         n/a
                                                                  culate the result per sentence. We consider each
                       ELI5       ↗     ↘         n/a             syntactic metric as a distribution relative to domain
                       news       ↗     ↘            ≈            and generation source (human vs. LLM).
 Depth                 wiki       ↗     ↘            ≈
                       ELI5       ≈     ≈            ≈            Dependency Tags. Dependency tags provide a
                       news       ↘     ↘      reduced            description of the relation between units in a sen-
 Yngve                 wiki       ↗     ↘      reduced            tence. For each sentence, we count the number of
                       ELI5       ↘     ↘      reduced            unique dependency tags.
                       news       ↗     ↘      reduced
 Constituency          wiki       ↗     ↘      reduced            Parse Depths. For each sentence, we count the
                       ELI5       ≈     ↘      reduced            depth of a constituency parse.
Table 1: Schematic description of Llama’s distribution            Yngve Scores. As a first qualification on parse
shift for our five investigated metrics relative to the hu-       depth, we also explore a measure of left vs. right
man baseline for all text domains. µ refers to mean shift         branching parse trees. We measure each sentence’s
(↗ refers situations when the mean of the distribution            Yngve score (Yngve, 1960) following Roark et al.
is higher for Llama than for the human), σ to the stan-
                                                                  (2007), which argues that the Yngve metric is use-
dard deviation of the distribution(↘ refers to situations
where the distribution is narrower for Llama than for the         ful for diagnosing cognitive impairments. The
original), and ‘long tail’ to whether a heavy right tail          score roughly corresponds to the deviation of a
that was present in the human distribution is reduced for         parse tree from a completely right-branching tree—
the Llama distribution (‘n/a’ marks situations with no            it is the average number of left branches on the path
long tail in the human distribution of the metric).               from the root node to each leaf.
                                                                  Constituency Labels. As a further qualification
can differ in the presence of a long tail (a heavy                of parse depth, we also calculate the number of
right tail). A schematic summarizing our results is               unique constituency labels in a sentence’s con-
in Table 1.                                                       stituency parse.

Flesch-Kincaid. First, we measure the Flesch-                     3     Results
Kincaid grade level score, following Flesch (1948).
This score pertains to an article overall, and is                 We generally report the results for Llama-70B mod-
a standard metric in the education field and in                   els in our figures, but more detailed figures that
NLP to estimate the reading level of a piece of                   provide additional data for smaller models and/or
text, with higher scores being more difficult. The                models from the Mistral family are available in a
Flesch-Kincaid score relies on words per sen-                     number of appendices.
tence and syllables per word to derive an es-                     3.1    Descriptive Results
timate of the ease of reading the text snippet.
                                                                  To situate our results, we first measure some basic
We calculate the Flesch-Kincaid scores using the
                                                                  dataset statistics. In Table 2, we present the statis-
py-readability-scores library4 , which relies
                                                                  tics for the parse tree depth experiment. Recall
on the Natural Language Toolkit (Bird et al., 2009).
                                                                  that some datasets may slightly differ in size based
For each dataset, we take each article and calcu-
                                                                  on the success of metric calculation as described
late its Flesch-Kincaid grade level score, then we
                                                                  above in §2.5. Also, note that complexity met-
consider the scores for all articles as a distribution.5
                                                                  rics can be correlated with sequence length (Salkar
    4
      https://github.com/cdimascio/py-readability-                et al., 2022).
metrics/tree/master
    5
      We observed that removing sentences and restructuring
                                                                     Across the board, the regenerated data is simi-
an article during the data cleaning stage leads to issues with    lar to the original data in terms of words per sen-
readability score calculation. Therefore, we calculated read-     tence. For CCnews and Wikipedia, the regenerated
ability scores without data cleaning for articles exceeding 100
words, as shorter articles lack sufficient content for accurate   readability assessment.

                                                              2370
 Datasets        Articles   Sentences   Words   S/A    W/S     W/A
 CCNews            0.6M        12.6M     0.3B   21.8   24.6    535.0
 Llama-2-70B       0.7M        19.9M     0.5B   28.1   25.6    718.4
 Llama-3.3-70B     0.7M        23.9M     0.7B   34.0   27.7    941.4
 Mistral-24B       0.7M        22.7M     0.5B   32.1   23.9    765.1
 Mistral-8B        0.7M        22.1M     0.5B   31.2   24.2    756.7
 Llama-3.1-8B      0.7M        19.8M     0.5B   28.7   26.5    759.2
 Wikipedia         6.4M      114.6M      2.9B   17.7   24.9    441.9
 Llama-2-70B       6.6M      234.0M      5.4B   35.4   23.2    821.0
 Mistral-24B       6.5M      307.7M      7.0B   47.5   22.6   1076.1
 ELI5              0.6M        34.2M     0.6B   56.2   18.6   1047.3
 Llama-3.3-70B     0.6M         9.3M     0.2B   15.2   20.4    310.6
 Mistral-24B       0.6M         6.6M     0.1B   10.8   18.5    200.3
 Mistral-8B        0.6M         6.1M     0.1B   10.2   18.7    191.3


Table 2: Descriptive statistics (average) on the datasets
used for the parse tree experiments. Eligible sentences
meet the following criteria: sentence length falls within
3-500 words, and contains 1 ≤ verb or auxiliary verb.



data contains more sentences per article, and hence
more words per article than the original data. For
ELI5, conversely, the regenerated data contains
fewer sentences per article, and hence fewer words
per article than the original. Due to our data clean-
ing (§2.3), there is some difference in the number
of articles preserved for analysis between genera-
tion sources (LLM v. human), with slightly more
regenerated articles being analyzed. We plot the
distribution over sentence lengths in Figure 14 in
Appendix C. We observe that the regenerated data
shows a shifted mean, a reduction in variability and
a reduced long tail, when compared to the original
human data for each domain.


3.2 Flesch-Kincaid Scores
                                                                          Figure 1: Flesch-Kincaid readability score distributions.
For this simplification metric, shown in Figure 1,                        Normal fit curves informally illustrate the fact that re-
we observe that all distributions are roughly normal                      generated data appears to be normally distributed, with
                                                                          narrower distributions and a reduced long tail on the
and the three signatures are present. We observe
                                                                          right relative to the human datasets.
that Flesch-Kincaid readability scores for the hu-
man data deviate slightly from the normal distribu-
tion in that they have a right tail, as indicated by                      3.3   Dependency Tags
the fact that the bars around the center are some-
what above the fit curve on the left, and somewhat                        As Figures 2–4 show, the regenerated data in each
below the fit curve on the right. As compared to                          domain is more narrow and has a slightly upward
their human-generated variants, each regenerated                          shifted mean relative to the human data. The origi-
dataset has a narrower distribution, and a reduced                        nal human data is close to normally distributed, so
long tail. For CCNews and Wikipedia, we observe                           we do not report a reduced long tail for this metric.
an upward shifted mean, while the mean for ELI5
                                                                          3.4   Depth Scores
is shifted downwards. In Appendix D, we plot the
full results for all tested models in Figure 15; we                       Normal fits for depth scores are provided in Fig-
also report the means, medians, and standard de-                          ure 5. For Wikipedia, and CCNews, the parse tree
viations for this metric in Table 5, alongside other                      depth of the regenerated data shows a narrowing ef-
readability metrics.                                                      fect. Interestingly, the regenerated data for ELI5 is
                                                                       2371
                                                           generated data (see Figure 16 in Appendix E).




Figure 2: Proportion of sentences in CCNews that have
a particular number of unique dependency tags.
                                                           Figure 5: Average depth score normal fits. Dotted lines
                                                           indicate human original domains, and solid lines indi-
                                                           cate model regenerations.


                                                           3.5   Yngve Scores
                                                           Yngve scores for Llama-regenerated data are
                                                           shown in Figure 6. In all three domains, we
                                                           see considerably more narrow distributions in the
                                                           Llama-generated data, and a shorter, less heavy
                                                           long right tail. Nonetheless, the Llama-regenerated
                                                           data shows a considerable right tail. The mean is
                                                           increased relative to the human mean in the case of
                                                           Wikipedia, while in the CCNews data, and ELI5,
Figure 3: Proportion of sentences in Wikipedia that have
                                                           the mean is slightly lower. In Appendix F, we plot
a particular number of unique dependency tags.
                                                           the full results for all tested models in Figure 17,
                                                           where data regenerated with other models show the
                                                           same trends.

                                                           3.6   Constituency Labels
                                                           Figures 7–9 show the distribution of unique con-
                                                           stituency labels per sentence. Across domains and
                                                           models, we find that the regenerated data has a nar-
                                                           rower distribution. The human distributions exhibit
                                                           a slight right tail that is largely absent with in the
                                                           regenerated data. In the regenerated CCNews, the
                                                           smaller Mistral models have a slightly downshifted
                                                           mean, while the Llama models shift their mean up-
                                                           wards. For Wikipedia, and ELI5, the models all
Figure 4: Proportion of sentences in ELI5 that have a
particular number of unique dependency tags.               shift their mean upwards.

                                                           3.7   Summary and Interpretation of Results
close in variance to the original data across models.      Across the majority of our metrics and datasets, we
This is the only time in our study that we do not          observe that models generate distributionally less
find a clear narrowing effect. For the Llama-70B-          diverse data, as evidenced by both a decrease in
regenerated data, we find a higher mean across all         variability and a reduced long tail. Both of these
domains. Across domains and models (with the ex-           signatures are compatible with the interpretation
ception of Mistral-24B’s CCNews and Wikipedia              that the models are simplifying relative to the hu-
data), the slight right tail is reproduced in the re-      man domain: if they were generating syntactically
                                                       2372
                                                           guages, and as such a loss of the long tail is com-
                                                           patible with syntactic simplification by the LLMs.
                                                              Interestingly, even for the unique dependency
                                                           tags metric, where we report no long tail reduction,
                                                           because the human data is very close to normally
                                                           distributed, the regenerated data deviates from the
                                                           human data. Across our other metrics, the human
                                                           data is more left-leaning (exhibits a right tail) than
                                                           the regenerated data. Even here, where the human
                                                           data is very close to normal, the regenerated data
                                                           leans right of that, thus showing the same direc-
                                                           tional difference as elsewhere.
                                                              However, while the model-regenerated data is
                                                           uniformly less diverse than the corresponding
                                                           human-generated texts across our variety of mea-
                                                           sures (reduced variability and a reduced long tail),
                                                           the mean shifts vary across domains: For CCNews
                                                           and Wikipedia, the Llama-generated data is mostly
                                                           shifted upwards, while the mean of the regenerated
                                                           ELI5 tends to match or be shifted downwards rela-
                                                           tive to the original data. Since ELI5 is presumably
                                                           more simple than the overall average training data
                                                           (while CCNews and Wikipedia may either match it
                                                           or be more complex), the direction of mean shifts
                                                           in the regenerated data suggests that models over-
                                                           shoot their domain complexity. In other words, in
                                                           terms of the mean of our complexity measures (but
                                                           not in terms of diversity) the models appear to re-
                                                           generate domain data that is a more extreme form
                                                           of the human original (simplifying in the case of
                                                           the simpler ELI5 domain, and shifting the mean
                                                           complexity upwards in the case of Wikipedia and
                                                           CCNews).
Figure 6: Yngve parse complexity score distribution           What we don’t see is all regenerated data consis-
for each dataset. Normal distribution curves fit to
                                                           tently landing at some kind of middle ground—a
the data show that both human and Llama-regenerated
datasets are not particular normally distributed. Llama-   “neutral” domain, that would reflect the properties
regenerated datasets show a narrower distribution than     of some average of all its training data—regardless
human with a heavy right tail that is reduced in compar-   of which domain the model is prompted to match.
ison to the human datasets (but still visibly present).    Since this isn’t present, we can conclude that the
                                                           models do have some notion of domain and encode
                                                           the fact that domains differ. However, the data that
simpler sentences overall, this could be underlying        models regenerate are consistently less diverse, and
the lower variability, and if they were failing to         in terms of the mean of our complexity measures,
capture rarer syntactic phenomena, or rarer combi-         they tend to be more extreme than the human origi-
nations of syntactic phenomena, this might account         nals, suggesting that the models’ notion of domain
for the reduced long tail.                                 is not fully humanlike.
   For example, the long tail of Yngve scores (Fig-
ure 6) would contain strongly left branching struc-        4   Qualitative Reflections on
tures that are grammatical but rare in English (e.g.,          LLM-Regenerated Data
clausal subjects). Many linguists take such struc-
tures to be evidence of the recursive nature of the        Llama-V2 Regenerated Wikipedia. We ob-
combinatorial system that underlies human lan-             served several trends when manually inspecting
                                                       2373
Figure 7: Proportion of sentences in CCNews (y-axis) that have a particular number of unique constituency labels
(x-axis). Colors indicate whether the distribution belongs to the original source data, or the source domain as
regenerated by Llama-V2 or Llama-V3.




Figure 8: Proportion of sentences in Wikipedia (y-axis) that have a particular number of unique constituency labels
(x-axis). Colors indicate whether the distribution belongs to the original source data, or the source domain as
regenerated by Llama-V2 or Llama-V3.




Figure 9: Proportion of sentences in ELI5 (y-axis) that have a particular number of unique constituency labels
(x-axis).


the data regenerated by the LLMs. When compar-                 in many abbreviations and acronyms.7 As may
ing Llama-V2-regenerated Wikipedia articles to the             be clear from this example, the models introduce
original human ones, we observed spelling normal-              stylistic elements that are not generally in keeping
izations (e.g. British -ise becomes American -ize),            with the style of the original Wikipedia domain.
increased inclusion of value judgments (which go               More examples are provided in Appendix G. These
against Wikimedia’s editorial guidelines called the            observations point the way to future work that ex-
“Neutral Point of View”6 )—and an increased preva-             plores the consequences of the domain regeneration
lence of essay-like wrap-up sentences.                         paradigm on stylistic elements.
   For example, the final sentences of the Llama-
V2 regenerated article on “A” are both explicitly                 7
                                                                    Note also that it wrongly asserts that the letter can be
concluding and unusually complimentary: In con-                used as a pronoun (a property that indefinite articles like En-
                                                               glish “a” do indeed have in other languages like German, but
clusion, the letter a is an important and versatile            not in English) and a suffix, of which the text alleges else-
letter in the English language. It is used as an in-           where that it denotes the performer of an action (peculiarly, in
definite article, a pronoun, a prefix, a suffix, and           non-rhotic variants of English, the Latinate plural -a may be
                                                               homophonous with the agent nominalization -er, which does
   6
       https://meta.wikimedia.org/wiki/Neutral_point_of_view   indeed denote the performer of an action).

                                                           2374
Llama-Regenerated CCNews. Llama-V2 and                shifted in a way that suggests that models over-
Llama-V3 were both prone to inserting a higher        shoot when trying to match domain properties.
number of quotations attributed to famous or in-         Our results may have practical implications (i.e.
fluential people than the original articles, which    on decisions about whether or not to utilize LMs
largely described an event. For example, we saw       as components in domain transfer systems) and
novel inclusions of quotations attributed to Jeff     theoretical implications (e.g. about the empirical
Gundlach, Warren Buffet, Mark Schneider, Zhang        status of syntactic long tail effects).
Yuhua, Chen Qi, and David Cameron. In the rare
case where the original CCNews articles contained     Acknowledgments
quotations, usually only one quote was present. It
                                                      We would like to thank Chantal Shaib, Jessica
would be fairly long in comparison to Llama-V2
                                                      Forde, Candace Ross, and Levent Sagun for con-
regenerated CCNews quotes. There were also a
                                                      versations relating to model collapse. We’d also
number of cases of Llama-V2 inserting acronyms
                                                      like to thank Sebastian Ruder for feedback on an
where none had existed in the source (e.g. Albu-
                                                      early draft, and the audience of the Organized Ses-
querque Little Theatre (ALT)).
                                                      sion on LLMs, Linguistics, and Psycholinguistics
   CCNews regenerated by Llama-V2 and Llama-          at the 2025 Annual Meeting of the Linguistic Soci-
V3 also displayed unusual wrap-up sentences, ex-      ety of America in Philadelphia, PA for comments
cept, unlike for Wikipedia, they appeared to be       and questions that helped us shape the final paper.
more PR or sales related. For example, the article
on “ARKit 1.5” ended with Whether you’re a tech       7   Limitations
enthusiast, a developer, or simply someone inter-
ested in the future of technology, ARKit 1.5 demos    Tooling and Pipeline. While our visual inspec-
are certainly worth keeping an eye on. More ex-       tions didn’t surface any immediate issues, we ac-
amples and comparisons between Llama-V2 and           knowledge the possibility of tooling failures when
Llama-V3 are present in the Appendix H.               we try to calculate metrics or parse sentences that
                                                      are extremely long or complicated. However, since
5   Related Work                                      we uniformly apply our tools across domains and
                                                      generation sources, we expect any errors to be com-
Closest to our work is Shaib et al. (2024), which     parable, and thus not to have an outsized impact on
explored sequences of part-of-speech tags in train-   our results.
ing data and model generations. They reported that
several LLMs generated more syntactically homo-       Decoding Temperature. In this work, we used
geneous text, as compared to human ground truth.      the default temperature from vLLM. We presume
Our work differs from theirs in that we focus on      that lowering the temperature would decrease ran-
different datasets and models, and perform distinct   domness, presumably further reduce diversity, and
experiments. We take a distributional view and are    higher temperature could increase diversity, but it
interested in the domain match setting, exploring     is not immediately clear what the effect would be
additional signatures of model-and-human differ-      on the reduction of the long tail. A more thorough
ence and more syntactic metrics. They explore         exploration of decoding temperature could be ex-
neutral domain text, diving deeper into the effect    plored in future work.
of decoding temperature, and also exploring the
                                                      Syntactic Complexity Metrics. In this work, we
additional summarization setting.
                                                      utilized existing complexity metrics from prior lit-
6   Conclusion                                        erature. However, we have anecdotally observed
                                                      some additional changes to the style and content,
Using our regeneration paradigm, we have un-          which one could devise metrics to specifically tar-
covered systematic syntactic differences between      get. Future work could perform more data analysis
human-generated and model-regenerated text.           to help guide the creation of additional informative
Across a variety of syntactic complexity metrics,     syntactic complexity metrics, which, in turn, could
the regenerated text showed lower variability as      help us gain more insights into the type of simpli-
well as a reduced long tail, when compared against    fication LLMs affect, and inspire architectural or
the human-generated text in the same domain,          training improvements.
while the mean of the measurements was often
                                                  2375
References                                                    Mielke, Wilson Y. Lee, Abheesht Sharma, Andrea
                                                              Santilli, Antoine Chaffin, Arnaud Stiegler, Debajy-
Danial Alihosseini, Ehsan Montahaei, and Mahdieh So-          oti Datta, Eliza Szczechla, Gunjan Chhablani, Han
  leymani Baghshah. 2019. Jointly measuring diversity         Wang, Harshit Pandey, Hendrik Strobelt, Jason Alan
  and quality in text generation models. In Proceedings       Fries, Jos Rozen, Leo Gao, Lintang Sutawika, M Sai-
  of the Workshop on Methods for Optimizing and Eval-         ful Bari, Maged S. Al-shaibani, Matteo Manica, Ni-
  uating Neural Language Generation, pages 90–98,             hal Nayak, Ryan Teehan, Samuel Albanie, Sheng
  Minneapolis, Minnesota. Association for Computa-            Shen, Srulik Ben-David, Stephen H. Bach, Taewoon
  tional Linguistics.                                         Kim, Tali Bers, Thibault Fevry, Trishala Neeraj, Ur-
Kevin Bache, David Newman, and Padhraic Smyth.                mish Thakker, Vikas Raunak, Xiangru Tang, Zheng-
  2013. Text-based measures of document diversity. In         Xin Yong, Zhiqing Sun, Shaked Brody, Yallow Uri,
  Proceedings of the 19th ACM SIGKDD international            Hadar Tojarieh, Adam Roberts, Hyung Won Chung,
  conference on Knowledge discovery and data mining,          Jaesung Tae, Jason Phang, Ofir Press, Conglong Li,
  pages 23–31.                                                Deepak Narayanan, Hatim Bourfoune, Jared Casper,
                                                              Jeff Rasley, Max Ryabinin, Mayank Mishra, Minjia
Douglas Biber. 1991. Variation across speech and writ-        Zhang, Mohammad Shoeybi, Myriam Peyrounette,
  ing. Cambridge University Press.                            Nicolas Patry, Nouamane Tazi, Omar Sanseviero,
                                                              Patrick von Platen, Pierre Cornette, Pierre François
BigScience Workshop, Teven Le Scao, Angela Fan,               Lavallée, Rémi Lacroix, Samyam Rajbhandari, San-
  Christopher Akiki, Ellie Pavlick, Suzana Ilić, Daniel      chit Gandhi, Shaden Smith, Stéphane Requena, Suraj
  Hesslow, Roman Castagné, Alexandra Sasha Luc-               Patil, Tim Dettmers, Ahmed Baruwa, Amanpreet
  cioni, François Yvon, Matthias Gall’e, Jonathan             Singh, Anastasia Cheveleva, Anne-Laure Ligozat,
  Tow, Alexander M. Rush, Stella Biderman, Albert             Arjun Subramonian, Aurélie Névéol, Charles Lover-
  Webson, Pawan Sasanka Ammanamanchi, Thomas                  ing, Dan Garrette, Deepak Tunuguntla, Ehud Reiter,
  Wang, Benoît Sagot, Niklas Muennighoff, Albert Vil-         Ekaterina Taktasheva, Ekaterina Voloshina, Eli Bog-
  lanova del Moral, Olatunji Ruwase, Rachel Bawden,           danov, Genta Indra Winata, Hailey Schoelkopf, Jan-
  Stas Bekman, Angelina McMillan-Major, Iz Belt-              Christoph Kalo, Jekaterina Novikova, Jessica Zosa
  agy, Huu Nguyen, Lucile Saulnier, Samson Tan, Pe-           Forde, Jordan Clive, Jungo Kasai, Ken Kawamura,
  dro Ortiz Suarez, Victor Sanh, Hugo Laurençon,              Liam Hazan, Marine Carpuat, Miruna Clinciu, Na-
  Yacine Jernite, Julien Launay, Margaret Mitchell,           joung Kim, Newton Cheng, Oleg Serikov, Omer
  Colin Raffel, Aaron Gokaslan, Adi Simhi, Aitor              Antverg, Oskar van der Wal, Rui Zhang, Ruochen
  Soroa, Alham Fikri Aji, Amit Alfassy, Anna Rogers,          Zhang, Sebastian Gehrmann, Shachar Mirkin, Shani
  Ariel Kreisberg Nitzav, Canwen Xu, Chenghao Mou,            Pais, Tatiana Shavrina, Thomas Scialom, Tian Yun,
  Chris Emezue, Christopher Klamm, Colin Leong,               Tomasz Limisiewicz, Verena Rieser, Vitaly Protasov,
  Daniel van Strien, David Ifeoluwa Adelani, Dragomir         Vladislav Mikhailov, Yada Pruksachatkun, Yonatan
  Radev, Eduardo González Ponferrada, Efrat Lev-              Belinkov, Zachary Bamberger, Zdeněk Kasner, Al-
  kovizh, Ethan Kim, Eyal Bar Natan, Francesco De             ice Rueda, Amanda Pestana, Amir Feizpour, Ammar
  Toni, G’erard Dupont, Germán Kruszewski, Giada              Khan, Amy Faranak, Ana Santos, Anthony Hevia,
  Pistilli, Hady Elsahar, Hamza Benyamina, Hieu Tran,         Antigona Unldreaj, Arash Aghagol, Arezoo Abdol-
  Ian Yu, Idris Abdulmumin, Isaac Johnson, Itziar             lahi, Aycha Tammour, Azadeh HajiHosseini, Bahareh
  Gonzalez-Dios, Javier de la Rosa, Jenny Chim, Jesse         Behroozi, Benjamin Ajibade, Bharat Saxena, Car-
  Dodge, Jian Zhu, Jonathan Chang, Jörg Frohberg,             los Muñoz Ferrandis, Daniel McDuff, Danish Con-
  Joseph Tobing, Joydeep Bhattacharjee, Khalid Al-            tractor, David Lansky, Davis David, Douwe Kiela,
  mubarak, Kimbo Chen, Kyle Lo, Leandro Von Werra,            Duong A. Nguyen, Edward Tan, Emi Baylor, Ez-
  Leon Weber, Long Phan, Loubna Ben allal, Lu-                inwanne Ozoani, Fatima Mirza, Frankline Onon-
  dovic Tanguy, Manan Dey, Manuel Romero Mu                   iwu, Habib Rezanejad, Hessie Jones, Indrani Bhat-
  noz, Maraim Masoud, María Grandury, Mario Šaško,            tacharya, Irene Solaiman, Irina Sedenko, Isar Ne-
  Max Huang, Maximin Coavoux, Mayank Singh,                   jadgholi, Jesse Passmore, Josh Seltzer, Julio Bonis
  Mike Tian-Jian Jiang, Minh Chien Vu, Moham-                 Sanz, Livia Dutra, Mairon Samagaio, Maraim El-
  mad A. Jauhar, Mustafa Ghaleb, Nishant Subramani,           badri, Margot Mieskes, Marissa Gerchick, Martha
  Nora Kassner, Nurulaqilla Khamis, Olivier Nguyen,           Akinlolu, Michael McKenna, Mike Qiu, Muhammed
  Omar Espejel, Ona de Gibert, Paulo Villegas, Pe-            Ghauri, Mykola Burynok, Nafis Abrar, Nazneen
  ter Henderson, Pierre Colombo, Priscilla Amuok,             Rajani, Nour Elkott, Nour Fahmy, Olanrewaju
  Quentin Lhoest, Rheza Harliman, Rishi Bommasani,            Samuel, Ran An, Rasmus Kromann, Ryan Hao,
  Roberto Luis López, Rui Ribeiro, Salomey Osei,              Samira Alizadeh, Sarmad Shubber, Silas Wang,
  Sampo Pyysalo, Sebastian Nagel, Shamik Bose,                Sourav Roy, Sylvain Viguier, Thanh Le, Tobi Oye-
  Shamsuddeen Hassan Muhammad, Shanya Sharma,                 bade, Trieu Le, Yoyo Yang, Zach Nguyen, Ab-
  Shayne Longpre, Somaieh Nikpoor, Stanislav Silber-          hinav Ramesh Kashyap, Alfredo Palasciano, Al-
  berg, Suhas Pai, Sydney Zink, Tiago Timponi Tor-            ison Callahan, Anima Shukla, Antonio Miranda-
  rent, Timo Schick, Tristan Thrush, Valentin Danchev,        Escalada, Ayush Singh, Benjamin Beilharz, Bo Wang,
  Vassilina Nikoulina, Veronika Laippala, Violette            Caio Brito, Chenxi Zhou, Chirag Jain, Chuxin
  Lepercq, Vrinda Prabhu, Zaid Alyafeai, Zeerak Ta-           Xu, Clémentine Fourrier, Daniel León Peri nán,
  lat, Arun Raja, Benjamin Heinzerling, Chenglei Si,          Daniel Molano, Dian Yu, Enrique Manjavacas, Fabio
  Davut Emre Tas ar, Elizabeth Salesky, Sabrina J.            Barth, Florian Fuhrimann, Gabriel Altay, Giyased-
                                                       2376
  din Bayrak, Gully Burns, Helena U. Vrabec, Imane         Emily Dinan, Angela Fan, Ledell Wu, Jason Weston,
  Bello, Ishani Dash, Jihyun Kang, John Giorgi, Jonas        Douwe Kiela, and Adina Williams. 2020. Multi-
  Golde, Jose David Posada, Karthik Rangasai Sivara-         dimensional gender bias classification. In Proceed-
  man, Lokesh Bulchandani, Lu Liu, Luisa Shinzato,           ings of the 2020 Conference on Empirical Methods
  Madeleine Hahn de Bykhovetz, Maiko Takeuchi,               in Natural Language Processing (EMNLP), pages
  Marc Pàmies, Maria A Castillo, Marianna Nezhurina,         314–331, Online. Association for Computational Lin-
  Mario Sänger, Matthias Samwald, Michael Cullan,            guistics.
  Michael Weinberg, Michiel De Wolf, Mina Mihalj-
  cic, Minna Liu, Moritz Freidank, Myungsun Kang,          Emily Dinan, Stephen Roller, Kurt Shuster, Angela
  Natasha Seelam, Nathan Dahlberg, Nicholas Michio           Fan, Michael Auli, and Jason Weston. 2019. Wizard
  Broad, Nikolaus Muellner, Pascale Fung, Patrick            of Wikipedia: Knowledge-powered conversational
  Haller, Ramya Chandrasekhar, Renata Eisenberg,             agents. In Proceedings of the International Confer-
  Robert Martin, Rodrigo Canalli, Rosaline Su, Ruisi         ence on Learning Representations (ICLR).
  Su, Samuel Cahyawijaya, Samuele Garda, Shlok S
  Deshmukh, Shubhanshu Mishra, Sid Kiblawi, Si-            Elvis Dohmatob, Yunzhen Feng, Arjun Subramonian,
  mon Ott, Sinee Sang-aroonsiri, Srishti Kumar, Ste-         and Julia Kempe. 2024. Strong model collapse.
  fan Schweter, Sushil Bharati, Tanmay Laud, Théo          Liat Ein-Dor, Ariel Gera, Orith Toledo-Ronen, Alon
  Gigant, Tomoya Kainuma, Wojciech Kusa, Yanis               Halfon, Benjamin Sznajder, Lena Dankin, Yonatan
  Labrak, Yash Shailesh Bajaj, Yash Venkatraman, Yi-         Bilu, Yoav Katz, and Noam Slonim. 2019. Financial
  fan Xu, Yingxin Xu, Yu Xu, Zhe Tan, Zhongli Xie, Zi-       event extraction using Wikipedia-based weak super-
  fan Ye, Mathilde Bras, Younes Belkada, and Thomas          vision. In Proceedings of the Second Workshop on
  Wolf. 2023. Bloom: A 176b-parameter open-access            Economics and Natural Language Processing, pages
  multilingual language model.                               10–15, Hong Kong. Association for Computational
                                                             Linguistics.
Steven Bird, Ewan Klein, and Edward Loper. 2009. Nat-
   ural language processing with Python: analyzing text    Julian Eisenschlos, Bhuwan Dhingra, Jannis Bulian,
   with the natural language toolkit. O’Reilly Media,         Benjamin Börschinger, and Jordan Boyd-Graber.
   Incorporated.                                              2021. Fool me twice: Entailment from Wikipedia
                                                              gamification. In Proceedings of the 2021 Conference
Iacer Calixto, Alessandro Raganato, and Tommaso               of the North American Chapter of the Association
   Pasini. 2021. Wikipedia entities as rendezvous across      for Computational Linguistics: Human Language
   languages: Grounding multilingual language models         Technologies, pages 352–365, Online. Association
   by predicting Wikipedia hyperlinks. In Proceedings         for Computational Linguistics.
   of the 2021 Conference of the North American Chap-
   ter of the Association for Computational Linguistics:   Angela Fan and Claire Gardent. 2022. Generating bi-
   Human Language Technologies, pages 3651–3661,             ographies on Wikipedia: The impact of gender bias
   Online. Association for Computational Linguistics.        on the retrieval-based generation of women biogra-
                                                             phies. In Proceedings of the 60th Annual Meeting of
Danqi Chen and Christopher Manning. 2014. A fast and         the Association for Computational Linguistics (Vol-
  accurate dependency parser using neural networks.          ume 1: Long Papers), pages 8561–8576, Dublin,
  In Proceedings of the 2014 Conference on Empirical         Ireland. Association for Computational Linguistics.
  Methods in Natural Language Processing (EMNLP),
  pages 740–750, Doha, Qatar. Association for Com-         Angela Fan, Yacine Jernite, Ethan Perez, David Grang-
  putational Linguistics.                                    ier, Jason Weston, and Michael Auli. 2019. ELI5:
                                                             Long form question answering. In Proceedings of
Jacob Devlin, Ming-Wei Chang, Kenton Lee, and                the 57th Annual Meeting of the Association for Com-
   Kristina Toutanova. 2019. BERT: Pre-training of           putational Linguistics, pages 3558–3567, Florence,
   deep bidirectional transformers for language under-       Italy. Association for Computational Linguistics.
   standing. In Proceedings of the 2019 Conference of
   the North American Chapter of the Association for       Rudolph Flesch. 1948. A new readability yardstick.
  Computational Linguistics: Human Language Tech-            Journal of applied psychology, 32(3):221.
   nologies, Volume 1 (Long and Short Papers), pages       Robert Gunning. 1952. The technique of clear writing.
  4171–4186, Minneapolis, Minnesota. Association for
   Computational Linguistics.                              Sil Hamilton. 2024. Detecting mode collapse in lan-
                                                              guage models via narration. In Proceedings of the
Nigel Dewdney, Carol VanEss-Dykema, and Richard               First edition of the Workshop on the Scaling Behav-
  MacMillan. 2001. The form is the substance: Classi-         ior of Large Language Models (SCALE-LLM 2024),
  fication of genres in text. In Proceedings of the ACL       pages 65–72, St. Julian’s, Malta. Association for
  2001 Workshop on Human Language Technology and              Computational Linguistics.
  Knowledge Management.
                                                           Colby Horn, Cathryn Manduca, and David Kauchak.
Chrysanne DiMarco and Graeme Hirst. 1993. A compu-           2014. Learning a lexical simplifier using Wikipedia.
  tational theory of goal-directed style in syntax. Com-     In Proceedings of the 52nd Annual Meeting of the
  putational Linguistics, 19(3):451–500.                     Association for Computational Linguistics (Volume 2:
                                                       2377
  Short Papers), pages 458–463, Baltimore, Maryland.       Jian Ni and Radu Florian. 2016. Improving multilingual
  Association for Computational Linguistics.                  named entity recognition with Wikipedia entity type
                                                              mapping. In Proceedings of the 2016 Conference
J. D. Hunter. 2007. Matplotlib: A 2d graphics environ-        on Empirical Methods in Natural Language Process-
   ment. Computing in Science & Engineering, 9(3):90–         ing, pages 1275–1284, Austin, Texas. Association
   95.                                                        for Computational Linguistics.

Dieuwke Hupkes, Mario Giulianelli, Verna Dankers,          Yixin Nie, Adina Williams, Emily Dinan, Mohit Bansal,
  Mikel Artetxe, Yanai Elazar, Tiago Pimentel, Chris-        Jason Weston, and Douwe Kiela. 2020. Adversarial
  tos Christodoulopoulos, Karim Lasri, Naomi Saphra,         NLI: A new benchmark for natural language under-
  Arabella Sinclair, et al. 2023. A taxonomy and review      standing. In Proceedings of the 58th Annual Meet-
  of generalization research in nlp. Nature Machine          ing of the Association for Computational Linguistics,
  Intelligence, 5(10):1161–1174.                             pages 4885–4901, Online. Association for Computa-
                                                             tional Linguistics.
Da Ju, Karen Ullrich, and Adina Williams. 2024. Are
  female carpenters like blue bananas? a corpus investi-   Vishakh Padmakumar and He He. 2023. Does writ-
  gation of occupation gender typicality. In Findings of     ing with language models reduce content diversity?
  the Association for Computational Linguistics: ACL         arXiv preprint arXiv:2309.05196.
  2024, pages 4254–4274, Bangkok, Thailand. Associ-
  ation for Computational Linguistics.                     Fabio Petroni, Aleksandra Piktus, Angela Fan, Patrick
                                                             Lewis, Majid Yazdani, Nicola De Cao, James Thorne,
Tom S. Juzek and Zina B. Ward. 2024. Why does chat-          Yacine Jernite, Vladimir Karpukhin, Jean Maillard,
  gpt "delve" so much? exploring the sources of lexical      Vassilis Plachouras, Tim Rocktäschel, and Sebastian
  overrepresentation in large language models.               Riedel. 2021. KILT: a benchmark for knowledge
                                                             intensive language tasks. In Proceedings of the 2021
Marcus Klang and Pierre Nugues. 2019. Docria: Pro-           Conference of the North American Chapter of the
 cessing and storing linguistic data with Wikipedia.         Association for Computational Linguistics: Human
 In Proceedings of the 22nd Nordic Conference on             Language Technologies, pages 2523–2544, Online.
 Computational Linguistics, pages 400–405, Turku,            Association for Computational Linguistics.
 Finland. Linköping University Electronic Press.
                                                           Peng Qi, Yuhao Zhang, Yuhui Zhang, Jason Bolton, and
Woosuk Kwon, Zhuohan Li, Siyuan Zhuang, Ying                 Christopher D. Manning. 2020. Stanza: A python
 Sheng, Lianmin Zheng, Cody Hao Yu, Joseph E.                natural language processing toolkit for many human
 Gonzalez, Hao Zhang, and Ion Stoica. 2023. Effi-            languages.
 cient memory management for large language model
 serving with pagedattention. In Proceedings of the        Brian Roark, Margaret Mitchell, and Kristy Holling-
 ACM SIGOPS 29th Symposium on Operating Systems              shead. 2007. Syntactic complexity measures for
 Principles.                                                 detecting mild cognitive impairment. In Biologi-
                                                             cal, translational, and clinical language processing,
Jack Lanchantin, Angelica Chen, Shehzaad Dhuliawala,         pages 1–8, Prague, Czech Republic. Association for
   Ping Yu, Jason Weston, Sainbayar Sukhbaatar, and          Computational Linguistics.
   Ilia Kulikov. 2025. Diverse preference optimization.
                                                           Sebastian Ruder, Matthew E. Peters, Swabha
David Lee. 2002. Genres, registers, text types, domains      Swayamdipta, and Thomas Wolf. 2019. Transfer
  and styles: clarifying the concepts and navigating a       learning in natural language processing. In Proceed-
  path through the bnc jungle. In Teaching and learn-        ings of the 2019 Conference of the North American
  ing by doing corpus analysis, pages 245–292. Brill.        Chapter of the Association for Computational
                                                             Linguistics: Tutorials, pages 15–18, Minneapo-
Dianqi Li, Yizhe Zhang, Zhe Gan, Yu Cheng, Chris             lis, Minnesota. Association for Computational
  Brockett, Bill Dolan, and Ming-Ting Sun. 2019. Do-         Linguistics.
  main adaptive text style transfer. In Proceedings of
  the 2019 Conference on Empirical Methods in Natu-        Jenna Russell, Marzena Karpinska, and Mohit Iyyer.
  ral Language Processing and the 9th International          2025. People who frequently use chatgpt for writing
  Joint Conference on Natural Language Processing            tasks are accurate and robust detectors of ai-generated
  (EMNLP-IJCNLP), pages 3304–3313, Hong Kong,                text.
  China. Association for Computational Linguistics.
                                                           Nikita Salkar, Thomas Trikalinos, Byron Wallace, and
Yinhan Liu, Myle Ott, Naman Goyal, Jingfei Du, Man-          Ani Nenkova. 2022. Self-repetition in abstractive
  dar Joshi, Danqi Chen, Omer Levy, Mike Lewis,              neural summarizers. In Proceedings of the 2nd Con-
  Luke Zettlemoyer, and Veselin Stoyanov. 2019.              ference of the Asia-Pacific Chapter of the Association
  Roberta: A robustly optimized bert pretraining ap-         for Computational Linguistics and the 12th Interna-
  proach.                                                    tional Joint Conference on Natural Language Pro-
                                                             cessing (Volume 2: Short Papers), pages 341–350,
AI@Meta Llama Team. 2024. The Llama 3 Herd of                Online only. Association for Computational Linguis-
  Models.                                                    tics.
                                                       2378
Sina Semnani, Violet Yao, Heidi Zhang, and Monica           Adina Williams, Ryan Cotterell, Lawrence Wolf-
  Lam. 2023. WikiChat: Stopping the hallucination of          Sonkin, Damián Blasi, and Hanna Wallach. 2021.
  large language model chatbots by few-shot ground-           On the relationships between the grammatical gen-
  ing on Wikipedia. In Findings of the Association            ders of inanimate nouns and their co-occurring adjec-
  for Computational Linguistics: EMNLP 2023, pages            tives and verbs. Transactions of the Association for
  2387–2413, Singapore. Association for Computa-              Computational Linguistics, 9:139–159.
  tional Linguistics.
                                                            Adina Williams, Nikita Nangia, and Samuel Bowman.
Chantal Shaib, Yanai Elazar, Junyi Jessy Li, and By-          2018. A broad-coverage challenge corpus for sen-
  ron C Wallace. 2024. Detection and measurement              tence understanding through inference. In Proceed-
  of syntactic templates in generated text. In Proceed-       ings of the 2018 Conference of the North American
  ings of the 2024 Conference on Empirical Methods            Chapter of the Association for Computational Lin-
  in Natural Language Processing, pages 6416–6431,            guistics: Human Language Technologies, Volume
  Miami, Florida, USA. Association for Computational          1 (Long Papers), pages 1112–1122, New Orleans,
  Linguistics.                                                Louisiana. Association for Computational Linguis-
                                                              tics.
Luca Soldaini, Rodney Kinney, Akshita Bhagia, Dustin
  Schwenk, David Atkinson, Russell Authur, Ben              Fei Wu and Daniel S. Weld. 2010. Open information
  Bogin, Khyathi Chandu, Jennifer Dumas, Yanai                extraction using Wikipedia. In Proceedings of the
  Elazar, Valentin Hofmann, Ananya Jha, Sachin Ku-            48th Annual Meeting of the Association for Computa-
  mar, Li Lucy, Xinxi Lyu, Nathan Lambert, Ian                tional Linguistics, pages 118–127, Uppsala, Sweden.
  Magnusson, Jacob Morrison, Niklas Muennighoff,              Association for Computational Linguistics.
  Aakanksha Naik, Crystal Nam, Matthew Peters, Ab-
  hilasha Ravichander, Kyle Richardson, Zejiang Shen,       Zhilin Yang, Peng Qi, Saizheng Zhang, Yoshua Bengio,
  Emma Strubell, Nishant Subramani, Oyvind Tafjord,           William Cohen, Ruslan Salakhutdinov, and Christo-
  Evan Walsh, Luke Zettlemoyer, Noah Smith, Han-              pher D. Manning. 2018. HotpotQA: A dataset for
  naneh Hajishirzi, Iz Beltagy, Dirk Groeneveld, Jesse        diverse, explainable multi-hop question answering.
  Dodge, and Kyle Lo. 2024. Dolma: an open corpus             In Proceedings of the 2018 Conference on Empiri-
  of three trillion tokens for language model pretraining     cal Methods in Natural Language Processing, pages
  research. In Proceedings of the 62nd Annual Meeting         2369–2380, Brussels, Belgium. Association for Com-
  of the Association for Computational Linguistics (Vol-      putational Linguistics.
  ume 1: Long Papers), pages 15725–15788, Bangkok,
  Thailand. Association for Computational Linguistics.      Victor H Yngve. 1960. A model and an hypothesis
                                                              for language structure. Proceedings of the American
George Spache. 1953. A new readability formula for            philosophical society, 104(5):444–466.
  primary-grade reading materials. The Elementary
  School Journal, 53(7):410–413.
Hugo Touvron, Louis Martin, Kevin Stone, Peter Al-
  bert, Amjad Almahairi, Yasmine Babaei, Nikolay
  Bashlykov, Soumya Batra, Prajjwal Bhargava, Shruti
  Bhosale, Dan Bikel, Lukas Blecher, Cristian Canton
  Ferrer, Moya Chen, Guillem Cucurull, David Esiobu,
  Jude Fernandes, Jeremy Fu, Wenyin Fu, Brian Fuller,
  Cynthia Gao, Vedanuj Goswami, Naman Goyal, An-
  thony Hartshorn, Saghar Hosseini, Rui Hou, Hakan
  Inan, Marcin Kardas, Viktor Kerkez, Madian Khabsa,
  Isabel Kloumann, Artem Korenev, Punit Singh Koura,
  Marie-Anne Lachaux, Thibaut Lavril, Jenya Lee, Di-
  ana Liskovich, Yinghai Lu, Yuning Mao, Xavier Mar-
  tinet, Todor Mihaylov, Pushkar Mishra, Igor Moly-
  bog, Yixin Nie, Andrew Poulton, Jeremy Reizen-
  stein, Rashi Rungta, Kalyan Saladi, Alan Schelten,
  Ruan Silva, Eric Michael Smith, Ranjan Subrama-
  nian, Xiaoqing Ellen Tan, Binh Tang, Ross Tay-
  lor, Adina Williams, Jian Xiang Kuan, Puxin Xu,
  Zheng Yan, Iliyan Zarov, Yuchen Zhang, Angela Fan,
  Melanie Kambadur, Sharan Narang, Aurelien Ro-
  driguez, Robert Stojnic, Sergey Edunov, and Thomas
  Scialom. 2023. Llama 2: Open foundation and fine-
  tuned chat models.
Michael L. Waskom. 2021. seaborn: statistical data
  visualization. Journal of Open Source Software,
  6(60):3021.
                                                        2379
A     Ablation of data cleaning                                   and uninformative about syntactic structure (there
                                                                  are very parses available for complete sentences
In this section, we also present our results for less
                                                                  with 3 or fewer words). We observe a similar trend
filtered data on two of our domains, Wikipedia
                                                                  for Figure 13, except that the noisy section extend
and CCNews. Overall, we see the same trends
                                                                  to approximately 6 constituency labels, which is
as for the filtered data presented in the main pa-
                                                                  reflective of the same underlying fact that there are
per. For dependency tags and constituency labels
                                                                  not many available parses for 3 words.
for both datasets: we see mean shift (mostly for
CCNews) and narrowing (for both datasets). De-                    B Prompts
scriptive statistics following the length and POS
filtration are presented in Table 2. Our overall                 We prompted the LLMs using the two prompts be-
cleaning and processing pipeline (including length               low, one for each text domain. We retrieved the
filtering) excluded on average less than 10% in the              {topic} and {title} respectively from the original
case of CCNews datasets, and less than 15% in the                data sources and fed them into the model prior to
case of Wikipedia datasets.                                      including the initial section of text for the model
                                                                 to attempt to regenerate. Next, we included in-
 Datasets         Sentences   Words   S/A    W/S    W/A          structions that match standard instruction-tuning
 CCNews            13.8M      0.3B    23.9   23.2   554.3        prompts, which also included a target article length
 LLaMA2 70B        20.6M      0.5B    29.1   24.9   724.9        in words, which we set to the average length of
 LLaMA3 70B        24.5M      0.7B    34.6   27.3   946.4
                                                                 article from each domain. We observed that the
 Wikipedia         129.5M     2.9B    20.0   22.5   450.4
 LLaMA 2 70B       277.5M     5.6B    42.0   20.3   854.9        regenerations were never word-for-word identical
                                                                 to the human versions, and we also observed that
        Table 3: Descriptive statistics on raw data.             the models did not generate exactly the average
 Datasets         Sentences   Words   S/A    W/S    W/A          lengths provided in the prompts.
 CCNews              13.6M     0.3B   23.4   23.5   551.3
 LLaMA2 70B          20.4M     0.5B   28.8   25.1   724.4         B.1    Wikipedia
 LLaMA3 70B          24.4M     0.7B   34.5   27.4   946.2
                                                                  1 NUM_FIRST_PARA_LENGTH = 256
 Wikipedia         122.8M      2.9B   19.0   23.6   448.1
                                                                  2 TEXT_PROMPT = """
 LLaMA 2 70B       257.3M      5.6B   39.0   21.8   850.2
                                                                  3 Generate a Wikipedia article on the
                                                                        topic of { topic }.
    Table 4: Descriptive statistics after length filtration.      4 Use the following first paragraph
                                                                        from the original Wikipedia
                                                                        article as a starting point :
  Readability scores were consistently calculated                 5
on entire articles without any data cleaning. We                  6   { first_paragraph }
compute readability scores for articles containing                7
                                                                  8  Now , expand upon the provided
more than 100 words, as shorter articles do not                           paragraph by providing additional
provide sufficient indicators of readability. Metrics                      details ,
                                                                   9 historical context , notable events ,
such as the depth score and Yngve score, which
                                                                          key figures , and any relevant
were initially aggregated at the article level, showed                    subtopics .
minimal variation upon inspection. Therefore, they                10 Aim for a well - structured and

are not included in the ablation results presented                        informative Wikipedia style
                                                                          article with a minimum length of
here. For reference, we provide results on depen-                         700 words .
dency and constituency parsing using the raw data                 11 Ensure that the content is factually
                                                                           accurate , well - written , and on
below.                                                                    Wikipedia writing style .
                                                                  12 """
Main Results Figures Ablations. Figures 10–13
present data ablations on our main results. Overall,
we see the same rough trends as described in the                  B.2    CCNews
main paper.
                                                                  1 NUM_FIRST_PARA_LENGTH = 180
   For Figure 11, we can see a difference in the                  2 TEXT_PROMPT = """
dependency parses for fewer than three words be-                  3 Generate a news article on the topic

tween the human-generated data and the Llama-                            of { title }.
                                                                  4 Use the following first paragraph
V2-generated data. We decided to filter out these                       from the original news article as
lengths, because we expected the data to be noisy                        a starting point :

                                                               2380
Figure 10: Proportion of sentences in CCNews (y-axis)            Figure 11: Proportion of sentences in Wikipedia (y-
that have a particular number of unique dependency               axis) that have a particular number of unique depen-
tags (x-axis). Colors indicate whether the distribution          dency tags (x-axis). Colors indicate whether the dis-
belongs to the original source data, or the source do-           tribution belongs to the original source data, or the
main as regenerated by Llama-V2 or Llama-V3. This                source domain as regenerated by Llama-V2 or Llama-
comparison was made on data without any cleaning.                V3. This comparison was made on data without any
                                                                 cleaning.


5                                                            but longer sentences for Wikipedia. We also ob-
6   { first_paragraph }                                      serve that the original human distributions are also
7
8 Now , expand upon the provided                             wider (i.e., the regenerated distributions have less
       paragraph by providing additional                     variance) for all data sources (with ELI5 being the
        details , context , notable events                   weakest effect, likely because more generations are
       , key figures , and any relevant
       discussions . Aim for a well -                        at the length floor). Finally, we observe that the
       structured and informative news                       original distributions appear to have a longer and
       style article with a minimum
       length of 500 words . Ensure that
                                                             heavier right tail than their model generated coun-
       the content is factually accurate                     terparts for all data sources. For the other models,
       , well - written , and on news                        the mean shift is inconsistent across models, but
       writing style .
9 """
                                                             all models show reduced variability, and a reduced
                                                             long tail.

B.3    Eli5                                                  D      More Information on Readability

1   TEXT_PROMPT = """                                        D.1      Full results for the Flesh-Kincaid
2   Generate a reddit reply to this                                   Readability Scores for all tested models.
        thread { title }.
3                                                            We present full results for Flesh-Kincaid scores in
4 Aim for an Explain Like I ' m Five
      style reply with a minimum length
                                                             Figure 15.
       of 100 words . Ensure that the
      content is factually accurate ,                        CCNews. For the CCNews datasource, all model
      well - written , and on Explain like                   regenerated datasets have upward shifted means
       I ' m Five writing style .
5 """
                                                             and narrowed distributions, in keeping with the
                                                             subset presented in the main paper. They are all
                                                             additionally more left than right tailed, when com-
C     Sentence Lengths                                       pared to the original human distribution.

As Figure 14 illustrates, no length distribution is          Wikipedia. For the Wikipedia datasource,
perfectly normal. When compared to the Llama-                Llama-V2-70B and Mistral-24B both had upward
70B regenerations, We observe that the original              shifted mean, a narrower distribution, and a
human distributions have shorter sentences on av-            reduced right tail. Interestingly, the Mistral model
erage (i.e., the regenerated distributions have up-          has a near-perfectly normal distribution, while
ward shifted means) for for CCNews and ELI5,                 Llama-V2-70B retains a slight right tail.
                                                          2381
Figure 12: Proportion of sentences in CCNews (y-axis) that have a particular number of unique constituency tags
(x-axis). Colors indicate whether the distribution belongs to the original source data, or the source domain as
regenerated by Llama-V2 or Llama-V3. This comparison was made on data without any cleaning.




Figure 13: Proportion of sentences in Wikipedia (y-axis) that have a particular number of unique constituency
tags (x-axis). Colors indicate whether the distribution belongs to the original source data, or the source domain as
regenerated by Llama-V2 or Llama-V3. This comparison was made on data without any cleaning.


ELI5. For the ELI5 datasource, all model-                   generated data has high standard deviations across
regenerated distributions have a downward shifted           the board (although occasionally in a tie with
mean, a narrower distribution and a strongly re-            Llama-V3-CCNews) suggests the human distribu-
duced right tail.                                           tions have more diversity in generations.

D.2 Additional Readability Scores                           Flesch-Kincaid Reading Ease. We report the
                                                            Flesch-Kincaid Reading Ease metric, which is sim-
We also report the means, medians, and standard
                                                            ilar to the Flesch-Kincaid grade level scoring in that
deviations of several readability scores, includ-
                                                            it is calculated from number of words and syllables
ing Flesch-Kincaid grade level (see Table 5), for
                                                            per sentence. A higher score indicates that the ma-
Wikipedia and CCNews domain data. We are us-
                                                            terial is easier to read. Human-generated Wikipedia
ing all 70B models for this analysis. We expect
                                                            has the highest reading ease (50), and Llama-V3-
most of these metrics to correlate highly—as all
                                                            generated CCNews has the lowest (39.5), but both
of them are based on different combinations of
                                                            fall into the range expected for college level texts.
words per sentence and syllables per word—but
                                                            The Flesch-Kincaid Reading Ease are presented in
are including them in case they may be of inter-
                                                            Table 6.
est to some readers. Across all readability metrics
(means and medians), human-generated Wikipedia              Gunning-Fog Index. The Gunning-Fog index
is deemed the simplest datasets, and Llama-V3-              (Gunning, 1952) is another estimate of reading
CCNews is deemed the most complex. Standard                 level, which is also based on the number of words
deviations are generally within the same range for          per sentence and the number of syllables per word,
all metrics, except for human-generated CCNews              but it generally has a lower value than the Flesh-
which has the most variation in readability. Sec-           Kincaid grade level and reading ease scores. The
ond in highest standard deviations across scores is         Gunning-Fog scores are presented in Table 7.
human-generated Wikipedia (Flesch-Kincaid Read-
ing Ease, Linsear Write) or Llama-V3-generated              Linsear Write Scores. The Linsear Write Scores
CCNews (Gunning-Fog Index, Spache Readability               are something of a thresholded version of the other
Formula, Linsear Write). The fact that human-               scores, where the words with more syllables are
                                                       2382
deemed “challenging” and words with fewer sylla-              Dataset     Mean    Median    STD    Sample Size
bles are deemed “easy”. The Linsear Write Scores              CCNews        8.1       7.8    3.2       561167
are presented in Table 8.                                     Llama-V2      7.7       7.7    0.7       708011
                                                              Llama-V3      8.0       8.0    1.2       702530
Spache Readability Formula. The Spache Read-
                                                              Wikipedia     7.6       7.6    1.0      3829535
ability Formula (Spache, 1953) operates on a list of
                                                              Llama-V2      7.6       7.6    0.7      6601865
words that are expected to be familiar for children
up until the fourth grade in the United States. The              Table 9: Spache Readability Formula Scores
formula considers average sentence length and pro-
portion of familiar words to determine its score. Of
all the metrics reported, this score resolves the least    E     Constituency Parse Depths Scores
differences between datasets. The Spache Read-             Figure 16 shows the distribution of constituency
ability Formula scores are presented in Table 9.           parse depths. Depth scores for model-regenerated
                                                           text have an upwardly shifted mean, and a more
 Dataset       Mean    Median    STD    Sample Size        narrow distribution when compared to human-
 CCNews         12.6      11.8    8.2         561167       generated text.
 Llama-V2       12.7      12.8    2.1         708011
 Llama-V3       13.8      13.8    3.2         702530       F     Full Yngve Score Distribution Plot
 Wikipedia      10.8      10.7    2.7        3829535
 Llama-V2       12.4      12.3    2.1        6601865      The full results for our Yngve metric on all models
                                                          and domains can be found in Figure 17.
        Table 5: Flesch-Kincaid Grade Level
                                                           G Example regenerations from Llama-V2
                                                             on the Wikipedia Domain
 Dataset       Mean    Median    STD    Sample Size       We manually inspected several examples from
 CCNews         48.2      50.4   24.9         561167      Llama-V2 and Llama-V3 and noticed some trends.
 Llama-V2       43.4      43.2   11.3         708011      Several of these trends are also listed in the supple-
 Llama-V3       39.5      39.4   12.8         702530      mentary materials of Russell et al. (2025), which
 Wikipedia      50.0      51.1   12.8        3829535      gives tips and tricks for detecting model generated
 Llama-V2       40.8      41.0   10.7        6601865
                                                          content; these include stylized and formalized con-
                                                          clusions, and spelling normalizations.
        Table 6: Flesch-Kincaid Reading Ease
                                                           Spelling Normalization. When the original arti-
                                                           cle contained British spellings (e.g. -ise as opposed
 Dataset       Mean    Median    STD    Sample Size        to -ize), Llama-2 did not uniformly preserve them,
 CCNews         14.4      13.5    8.5         561167       preferring American spellings for “organize”, “em-
 Llama-V2       15.2      15.3    2.3         708011       phasize”, “decentralize”.
 Llama-V3       16.5      16.5    3.5         702530
 Wikipedia      12.0      11.7    3.0        3829535       Longer snipped of the Llama-regenerated
 Llama-V2       14.2      14.2    2.4        6601865       Wikipedia article “A”. In addition to their use
                                                           as indefinite articles, “a” and “an” can also be
             Table 7: Gunning-Fog Index                    used as pronouns to refer to a noun or noun phrase
                                                           that has been previously mentioned. For example:
                                                          “I saw a cat in the park.” (meaning a specific cat that
 Dataset       Mean    Median    STD    Sample Size        was seen in the park) “I gave an apple to my friend.”
 CCNews         16.6      15.1   14.1         561167       (meaning a specific apple that was given to a friend)
 Llama-V2       15.9      15.9    2.6         708011       In English, the letter “a” is also used as a prefix to
 Llama-V3       17.6      17.5    4.3         702530       indicate negation or absence, as in “a-” or “non-”.
 Wikipedia      12.9      12.7    4.2        3829535       For example: “Atheist” means someone who does
 Llama-V2       14.3      14.3    3.3        6601865       not believe in God. “Amoral” means someone who
                                                           does not have moral principles. “Asexual” means
             Table 8: Linsear Write Scores                 someone who does not experience sexual attraction.
                                                           The letter “a” is also used as a suffix to indicate a
                                                       2383
 noun that refers to a person or thing that performs a      his profound impact on human thought and culture,
 particular action or has a particular characteristic.      and his ideas will continue to shape our under-
 For example: “Artist” means someone who creates            standing of the world for generations to come.
 art. “Athlete” means someone who is skilled in                “Academy Awards”: Whether it’s the red car-
 sports or physical activity. “Actor” means some-           pet glamour, the thrill of winning an Oscar, or the
 one who performs in movies, television shows, or           memories of unforgettable moments, the Academy
 theater productions. The letter “a” is also used in        Awards continue to capture the hearts and imagi-
 many abbreviations and acronyms, such as “A.M.”            nations of people around the world.
 (meaning “ante meridiem” or “morning”), “P.M.”
 (meaning “post meridiem” or “afternoon”), “A.S.”           H Example regenerations from Llama-V2
 (meaning “associate degree”), “B.A.” (meaning                on the CCNews Domain
“Bachelor of Arts”), “M.A.” (meaning “Master of
 Arts”), and “Ph.D.” (meaning “Doctor of Philoso-           Conclusion summaries and sales pitches. The
 phy”). In addition to its use in English, the letter       Llama-V2 regenerated article on “China launches
“a” is also used in many other languages, including         1st X-ray Space Telescope” concludes with In con-
 Spanish, French, German, Italian, Portuguese, and          clusion, the launch of China’s first X-ray space
 many others. In these languages, “a” is used to            telescope, ‘Insight’, marks a significant milestone
 represent a variety of vowel sounds, including the         in the country’s space exploration history. The
 sounds /a/, /A/, /@/, and /ä/. In conclusion, the letter   telescope is expected to provide valuable insights
“a” is an important and versatile letter in the English     into some of the most complex and fascinating phe-
 language. It is used as an indefinite article, a pro-      nomena in the universe and push the boundaries
 noun, a prefix, a suffix, and in many abbreviations        of detection technology. The launch is a testament
 and acronyms. Its origins can be traced back to the        to China’s commitment to advancing the field of
 Phoenician alphabet, where it represented a glottal        astronomy and its growing influence in the global
 stop, and it has evolved over time to represent a          space community.
 variety of vowel sounds in different languages.               An article on Nestlé being optimistic that in-
                                                            gredient prices will fall concludes with In conclu-
Conclusion summaries and value judgments.                   sion, Nestle’s optimism about its ability to offset
The regenerated article on “Albedo” concluded               the impact of rising ingredient prices and meet its
with By understanding albedo, scientists and poli-          sales growth target is a positive sign for the com-
cymakers can make informed decisions about envi-            pany’s future prospects. The company’s diversified
ronmental management, urban planning, agricul-              portfolio, geographic presence, and commitment
ture, and other fields that affect human life and the       to sustainability will help to mitigate any negative
environment.                                                impact from economic uncertainty and drive long-
   “Abraham Lincoln”: In conclusion, Abraham                term growth. As the company continues to invest
Lincoln was a strong leader who fought to preserve          in premium and healthier products, as well as sus-
the Union and end slavery. His eloquence, political         tainable sourcing, it is well-positioned to meet the
skills, and commitment to democracy and freedom             changing needs of consumers and deliver on its
have made him a beloved figure in American his-             growth targets.
tory. His legacy endures, and he remains an icon               “Magical Show Mary Poppins to Wrap Albu-
of American values and ideals.                              querque Little Theatre’s 87th Season”: The ALT
   “Alabama”: From its Native American roots to             production of Mary Poppins runs until June 12th,
its current status as a thriving Southern state, Al-        with performances on Fridays, Saturdays, and Sun-
abama has contributed to the nation’s cultural, eco-        days. Tickets are available through the ALT website
nomic, and political landscape. Its people, events,         or at the box office. Don’t miss your chance to ex-
and landmarks continue to inspire and captivate             perience this magical show and be a part of the
the nation’s attention, and its legacy will undoubt-        ALT’s 87th season.
edly endure for generations to come.                           “Rutherford Co. deputies searching for missing
   “Achilles”: Achilles’ legacy continues to live on,       woman - FOX Carolina 21”: The disappearance of
and his story will continue to inspire and captivate        Patricia Murray has sent shockwaves through the
audiences for generations to come.                          community, and the Rutherford County Sheriff’s
   “Aristotle”: Aristotle’s legacy is a testament to        Office is committed to doing everything they can to
                                                       2384
bring her home safely. As the search continues, the
community remains hopeful that she will be found
soon, and that she will be reunited with her loved
ones.
   “Southfields Residential Care: A Comprehen-
sive Guide”: In conclusion, at Southfields Residen-
tial Care, we understand the importance of provid-
ing a safe, supportive, and welcoming environment
for our residents. We strive to create a place where
people can live comfortably and safely, while still
maintaining their independence and individuality.
If you’re looking for a care home that truly cares,
look no further than Southfields Residential Care.

I   Comparison of original and regenerated
    CCNews
We show a direct comparison of human-generated,
Llama-V2-generated, and Llama-V3-generated
CCNews data in Table 10. Anecdotally, the human-
generations appear less similar to the Llama ones
than the Llama ones appear to each other.




                                                       Figure 14: The full plot of sentence length for all the
                                                       models.

                                                   2385
  Dataset      Prompt Title               Text
  Human        ARKit 1.5 Demos Show-      iOS 11.3 developer beta has been out for a few days and we’re seeing some
               ing Up Online              ARKit 1.5 examples showing up on YouTube and Twitter. The demos are rudi-
                                          mentary right now, but will likely improve as developers get more time with
                                          Apple’s updates augmented reality technology. One of the big new features in
                                          ARKit 1.5 is vertical plane, or wall, detection. That’s what the early demos are
                                          focusing on.
  Llama-V2     ARKit 1.5 Demos Show-      With its improved wall detection, lighting estimation, and other features, ARKit
               ing Up Online              1.5 is set to revolutionize the way we interact with the world around us. As
                                          developers continue to explore the potential of this technology, we can expect
                                          to see even more innovative and practical applications of AR in the months
                                          and years to come. Whether you’re a tech enthusiast, a developer, or simply
                                          someone interested in the future of technology, ARKit 1.5 demos are certainly
                                          worth keeping an eye on.
  Llama-V3     ARKit 1.5 Demos Show-      With its introduction of vertical plane detection, ARKit 1.5 is set to revolutionize
               ing Up Online              the world of augmented reality, enabling developers to create more immersive,
                                          interactive, and engaging experiences. As the technology continues to evolve,
                                          it will be exciting to see how developers and companies harness its potential
                                          to transform industries and revolutionize the way we interact with the world
                                          around us. With the release of iOS 11.3 and ARKit 1.5, Apple is once again
                                          demonstrating its commitment to innovation and its desire to push the bound-
                                          aries of what is possible with technology.
  Human        Magical Show Mary          The jack-of-all trades, Bert, introduces us to England in 1910 and the troubled
               Poppins to Wrap Albu-      Banks family. Young Jane and Michael have sent many a nanny packing before
               querque Little Theatre’s   Mary Poppins arrives on their doorstep. Start the conversation, or Read more
               87th Season                at BroadwayWorld.com.
  Llama-V2     Magical Show Mary          Mary Poppins, the beloved musical that the hearts of audiences for decades, is
               Poppins to Wrap Albu-      set to wrap up the 87th season of the Albuquerque Little Theatre (ALT) in New
               querque Little Theatre’s   Mexico. The show, which opened on May 13th, has been delighting audiences
               87th Season                with its magical blend of song, dance, and storytelling. Based on the popular
                                          Disney film of the same name, Mary Poppins tells the story of the Banks family,
                                          who are in search of a new nanny to care for their children, Jane and Michael.
                                          The family’s fortunes take a turn for the better when Mary Poppins, a practically
                                          perfect nanny, arrives on their doorstep. With her enchanting voice, graceful
                                          movements, and a sprinkle of magic, Mary wins over the hearts of the Banks
                                          family and their friends, bringing joy and order to their lives
  Llama-V3     Magical Show Mary          The beloved musical, Mary Poppins, is set to conclude the Albuquerque Little
               Poppins to Wrap Albu-      Theatre’s (ALT) 87th season, bringing a spoonful of sugar and a dash of magic
               querque Little Theatre’s   to the city’s theater scene. The show, directed by Henry Avery, promises to be a
               87th Season                spectacular finale to a season that has seen a wide range of productions, from
                                          classic dramas to contemporary comedies. The story of Mary Poppins has been
                                          enchanting audiences for generations, and the ALT production is expected to
                                          be no exception. The musical, based on the books by P.L. Travers, tells the
                                          tale of the Banks family, who are struggling to find joy and discipline in their
                                          lives. The arrival of Mary Poppins, played by actress Katie Calahan, brings a
                                          much-needed injection of fun and discipline into the household, as she teaches
                                          the children valuable lessons about the importance of imagination, hard work,
                                          and family.

Table 10: Examples of how Llama-regenerated CCNews text differs from the original. The original is presented in
its entirety, the regenerate examples came from the end of the article in the case of ARKit 1.5, and from the middle
in the case of Mary Poppins. Red denotes a near exact text match between Llama-V2 and Llama-V2 CCNews,
Orange denotes less exact match, potentially with position shifts across the sentence.




                                                         2386
Figure 15: The full plot of Flesch-Kincaid Readability   Figure 16: The distribution of constituency parse depth.
for all the models.                                      Llamadatasets have a narrower distribution.

                                                     2387
Figure 17: The full plot of Yngve score for all the
models.

                                                  2388
```

## Extraction verification

- **Beginning checked:** PDF page 1 was rendered and compared with the extraction: title, three authors and affiliations, complete abstract, Introduction opening, proceedings footer, and printed page 2367 agree.
- **Middle checked:** PDF pages 5-8 and 11 were rendered and compared with the extraction: Table 2, Figures 1-9, their captions and surrounding Results/Qualitative Reflections text, and the middle reference page agree.
- **End checked:** PDF page 22 was rendered and compared with the extraction: Figure 17, its caption, and printed page 2388 agree.
- **Structure checked:** 22 PDF pages; numbered main sections 1-7; Acknowledgments; References; appendices A-I; Tables 1-10; Figures 1-17; prompt listings B.1-B.3; qualitative examples G-I. `pdfimages -list` reports 17 embedded plot images. All 22 pages produced embedded text.
- **Known omissions:** none from the preserved source. Plot pixels are not transcribed into prose, but every plot remains in both preserved PDFs and its title, legend text where embedded, caption, and interpretation are retained in the extraction.

## Preserved attachments

| Path | Role in the source | SHA-256 | Preservation / extraction notes |
|---|---|---|---|
| `snapshots/attachments/ju-blix-williams-domain-regeneration-acl-2025.pdf` | Authoritative ACL 2025 proceedings paper | `78038e7333789fe833d80d94080871b4dea4a54d044c56c6e52bc54e04e7bcba` | Downloaded directly from the canonical ACL Anthology PDF URL; all 22 pages extracted and selected pages rendered for visual comparison. |
| `snapshots/attachments/ju-blix-williams-domain-regeneration-arxiv-2505.07784v2.pdf` | Author-hosted/preprint alternate version used for version comparison | `e1242d250e80934cc2227a5432201058a11bb0c4038df5aac5ff6687a8932872` | Downloaded directly from arXiv v2; 22 pages. Its PDF abstract and substantive section set include ELI5 even though the arXiv API summary still describes only two domains. |
