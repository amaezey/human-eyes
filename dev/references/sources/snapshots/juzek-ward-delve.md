# Why Does ChatGPT “Delve” So Much? Exploring the Sources of Lexical Overrepresentation in Large Language Models

- **Canonical URL:** https://aclanthology.org/2025.coling-main.426/
- **Alternate access URLs:**
  - https://aclanthology.org/2025.coling-main.426.pdf
  - https://arxiv.org/abs/2412.11385
  - https://arxiv.org/pdf/2412.11385
  - https://github.com/tjuzek/delve
- **Author / owner:** Tom S. Juzek and Zina B. Ward
- **Publisher:** Association for Computational Linguistics
- **Published:** 2025-01
- **Retrieved:** 2026-07-15
- **Stable identifier:** ACL Anthology ID 2025.coling-main.426; arXiv:2412.11385v1; DOI none found
- **Version / revision:** final COLING 2025 proceedings PDF; the paper text is token-identical to arXiv v1 and the repository's `COLING_2025_final_submission_v106.pdf` after removal of version and proceedings-layout markers; supporting code repository inspected at commit `0b7e2ba538bcc51ea538594512ef591ec24a1af1`
- **Extraction method:** official ACL PDF downloaded with `curl`; all 15 pages converted from the embedded text layer with Poppler `pdftotext -layout`; page count and metadata checked with `pdfinfo`; pages 1, 8, and 15 rendered with `pdftoppm` and visually compared; arXiv v1 and repository PDF extracted and token-compared; supporting repository cloned with full history and archived at the reviewed commit
- **Full-text status:** complete
- **Access and transformation notes:** no OCR; line wrapping, column order, page breaks, and end-of-line hyphenation follow Poppler's layout-preserving extraction. Figure pixels remain in the preserved PDFs; all figure and table captions, body sections, acknowledgments, references, and appendices A-G are present in the extraction. The repository is a later supporting-material revision, not evidence that its current code tree is the exact publication-time environment; its README and scripts disclose AI-assisted polishing or refactoring.

## Full text

Why Does ChatGPT “Delve” So Much? Exploring the Sources of Lexical
          Overrepresentation in Large Language Models

                                   Tom S. Juzek and Zina B. Ward*
                                        Florida State University
                                   tjuzek@fsu.edu, zward@fsu.edu



                      Abstract
    Scientific English is currently undergoing rapid
    change, with words like “delve,” “intricate,”
    and “underscore” appearing far more frequently
    than just a few years ago. It is widely assumed
    that scientists’ use of large language models
    (LLMs) is responsible for such trends. We de-
    velop a formal, transferable method to char-
    acterize these linguistic changes. Application
    of our method yields 21 focal words whose
    increased occurrence in scientific abstracts is
    likely the result of LLM usage. We then pose
    “the puzzle of lexical overrepresentation”: why
    are such words overused by LLMs? We fail                 Figure 1: We formalize a procedure for identifying
    to find evidence that lexical overrepresenta-            words whose increasing prevalence is likely the result
    tion is caused by model architecture, algorithm          of LLM usage. Although our focus is Scientific En-
    choices, or training data. To assess whether             glish, the method can be applied across domains and
    reinforcement learning from human feedback               languages.
    (RLHF) contributes to the overuse of focal
    words, we undertake comparative model testing
    and conduct an exploratory online study. While
                                                             Changes in dominant methodological and explana-
    the model testing is consistent with RLHF play-
    ing a role, our experimental results suggest             tory frameworks – such as the rise of mechanical
    that participants may be reacting differently to         philosophy, or the mathematization of scientific
    “delve” than to other focal words. With LLMs             fields – have been accompanied by changes in word
    quickly becoming a driver of global language             usage and syntactic structures as well (Degaetano-
    change, investigating these potential sources            Ortlieb and Teich, 2018; Krielke, 2024). Such
    of lexical overrepresentation is important. We           changes continue through the present (Banks, 2017;
    note that while insights into the workings of
                                                             Leong, 2020).
    LLMs are within reach, a lack of transparency
    surrounding model development remains an ob-                  Over the last two years, however, Scientific En-
    stacle to such research.                                   glish has witnessed increasing usage of certain lex-
                                                               ical items at a seemingly unprecedented pace. Dis-
1 Introduction                                                 cussions on social media (e.g., Koppenburg 2024;
Like all human language, Scientific English                    Nguyen 2024; Shapira 2024) and in academic dis-
has changed substantially over time (Degaetano- course (Gray, 2024; Kobak et al., 2024; Liang
Ortlieb and Teich, 2018; Degaetano-Ortlieb et al., et al., 2024b; Liu and Bu, 2024; Matsui, 2024)
2018; Bizzoni et al., 2020; Menzel, 2022). New dis- have pointed out that words such as “delve,” “in-
coveries have fueled (and perhaps been fueled by) tricate,” and “nuanced” have appeared far more
the introduction of new lexical items into scientific          frequently in scientific abstracts from 2023 and
discourse (Degaetano-Ortlieb and Teich, 2018).                 2024 compared to earlier years. Unlike many pre-
    * Conceptually, both authors contributed equally to this
                                                               vious  changes in Scientific English, these trends do
work. Tom wrote the code to the paper, which can be accessed   not seem  to be explained by changes in the content
at github.com/tjuzek/delve.                                    of science or in wider language use. Instead, it is
                                                            6397
            Proceedings of the 31st International Conference on Computational Linguistics, pages 6397–6411
                        January 19–24, 2025. ©2025 Association for Computational Linguistics
widely assumed that the sharp increase is due to        2   Corpus Analysis: Identification of
the use of large language models (LLMs) like Chat-          Overrepresented Lexical Items
GPT for scientific writing. Evidence supporting
                                                        To probe recent changes in Scientific English, we
this hunch has recently emerged (e.g., Cheng et al.
                                                        used PubMed’s publicly available repository of sci-
2024; Liang et al. 2024a).
                                                        entific abstracts, which focuses on biomedical liter-
    The goals of the present research were twofold.     ature (National Library of Medicine, 2023) (down-
First, we aimed to provide a systematic charac-         loaded through the PubMed API using a Python
terization of this linguistic phenomenon. Some          script (Python Software Foundation, 2024); Snap-
existing work has relied on informal methods to         shot: May 4, 2024; all code on our GitHub). Our
identify words observed to occur more frequently        analysis includes more than 5.2 billion tokens (in-
in AI-generated writing (e.g., Matsui 2024). We         flected forms) from 26.7 million abstracts. To track
developed a method for extracting lexical items         changes in word usage over time, we measured
of interest, described in Section 2, which is rigor-    occurrences per million (opm) of a given token in
ous, reproducible, and transferable to other data       each year. Figure 2 illustrates the usage trajectories
and models. We identified 21 “focal words”: lex-        of some baseline items over time. We focus on
ical items that have recently spiked in Scientific      the period from 1975 to May 2024 as data prior to
English and are overused by ChatGPT-3.5 in scien-       1975 are less extensive.
tific writing tasks, as illustrated in Figure 1.
   Prior research has focused on quantifying such
focal words’ increasing prevalence and estimating
how much recent scientific writing has been pro-
duced with LLM assistance (e.g., Kobak et al. 2024;
Liang et al. 2024b). By contrast, our second goal
was to explore the factors that might contribute
to the phenomenon of lexical overrepresentation:         Figure 2: Selected lexical entries: change over time.
Why does ChatGPT use “delve” (and other focal
words) so frequently when generating scientific               The goal of our corpus analysis was to identify
text? We identified a set of possible factors, char-       words whose recent overuse in scientific writing
acterized in Section 3, and began to assess them.          is likely the result of LLM deployment. Our ap-
We did not find evidence that model architecture           proach involved three steps. First, we determined
or algorithmic decisions play a major role in the          which words were more prevalent in abstracts from
overrepresentation of focal words (Section 5), nor         2024 compared to 2020 (since LLMs were not
that lexical overrepresentation stems from training        widespread pre-2021). We calculated the percent-
or fine-tuning data (Section 4).                           age increase in opm for each token in the database
   LLM training often involves reinforcement learn- between 2020 and 2024. Unsurprisingly, there was
ing based on information about quality outputs             a straightforward explanation for why some words
from human evaluators. We found mixed evidence             spiked in usage during that time. For example,
that reinforcement learning from human feedback “omicron” and “metaverse” were two of the words
(RLHF) contributes to the overrepresentation of our        that showed the largest percentage increase (for
focal words in LLM-generated text. Positive evi- “omicron”, see Figure 2). We only considered in-
dence comes from model testing on Meta’s Llama             creases deemed significant by chi-square tests, of
LLM (Section 5). An exploratory experiment de- which there were about 7300.
scribed in Section 6 is inconclusive, although our            We were interested in isolating words whose
findings indicate that participants became wary of         spike in usage was unexplained. The authors func-
the word “delve” in the first sentence of an abstract      tioned as annotators and independently reviewed
(e.g., ’This article delves into ...’). Since the experi- the list of words that had the highest percentage
ment’s inconclusiveness stems partly from method- change to exclude irrelevant tokens (like year num-
ological issues, we believe a follow-up study is           bers) and words whose spiking had an explanation
warranted. Many important questions about the fu- in terms of scientific advances or world events. In
ture of LLM-driven language change remain (Sec- cases of disagreement, we included the word on
tion 7).                                                   our list. We stopped once we had 50 words whose
                                                        6398
usage spiked without any obvious explanation (see                  Each focal word (a) shows a significant spike in
incl.ods on GitHub). This list contained several of                opm between 2020 and 2024, (b) its spike lacks
the words that had been the focus of online conver-                an obvious explanation, and (c) ChatGPT tends to
sation, including “delve” and “intricate”.                         use it significantly more than humans when writing
   However, a spike without an obvious explana-                    scientific abstracts (Figure 1). Thus, a plausible
tion is not necessarily LLM-induced. For exam-                     explanation for the increasing prevalence of each
ple, the usage of ’mash’ increased tenfold, but it                 focal word in Scientific English is the use of AI.
is not a word that ChatGPT is known to overuse.                       This systematic, three-step method for identi-
The second step of our method involved identify-                   fying focal words is novel. It improves on more
ing words that are overrepresented in AI-generated                 informal ways of identifying AI-associated words,
scientific abstracts compared to human-generated                   and it can be applied to other corpora and LLMs
abstracts. In producing AI-generated abstracts, our                beyond ChatGPT-3.5. (Appendix B reports similar
aim was to imitate the process by which researchers                results for ChatGPT-4.0(-mini).) Future research
might have deployed an LLM in 2022-early 2024                      can use the method to investigate whether the same
(while paying attention to careful prompt formula-                 words are overrepresented in the outputs of differ-
tion (Wei et al., 2022; Zhou et al., 2022)). After                 ent models – or whether there are LLMs that do
some exploration, we ended up with a two-stage                     not exhibit lexical overrepresentation at all.
process: (1) We randomly sampled 10,000 abstracts
from papers published in 2020 from the PubMed                      3     The Puzzle of Lexical
database. Via the API, ChatGPT-3.5 then summa-                           Overrepresentation
rized the associated paper (Prompt: “The following                 A question now presents itself: Why are certain
is an abstract of an article. Summarize it in a cou-               words used so often in AI-generated scientific writ-
ple of sentences.”) (2) The ChatGPT-generated                      ing? We call this “the puzzle of lexical overrepre-
summary was then used to ask ChatGPT-3.5 for a                     sentation.” There are a number of factors that might
corresponding scientific abstract. (Prompt: “Please                be responsible for the overrepresentation of focal
write an abstract for a scientific paper, about 200                words in scientific abstracts generated by ChatGPT.
words in length, based on the following notes.”)                   Importantly, these potential explanations are not
We suspect that the most common way of using                       mutually exclusive: multiple factors may (and prob-
an LLM to generate an abstract back when Chat-                     ably do) contribute.
GPT could not accept paper-length inputs involved
providing important fragments of a paper. We                           1. Initial Training Data Although the focal
used ChatGPT-3.5 for the entirety of our project                          words are overrepresented relative to human-
because if scientific abstracts in our dataset con-                       written abstracts, it is possible that they are not
tain AI-generated language, it is most likely from                        overrepresented relative to the data on which
ChatGPT-3 or ChatGPT-3.5 (Sarkar, 2023).                                  ChatGPT was trained to do next-word predic-
   In total, from 10,000 human abstracts, we gen-                         tion. Perhaps these words are actually being
erated 9,953 AI abstracts. (For a small number,                           used by LLMs with the same frequency as in
ChatGPT would not provide a response, presum-                             their training data.
ably due to topic sensitivity.) We then compared                       2. Fine-Tuning Training Data After LLMs
the word usage in the AI-generated abstracts with                         have been trained on next-word prediction,
word usage in the original abstracts. We only con-                        they are often fine-tuned. For instance, chat-
sidered words for which a chi-square test indicated                       bots are presented with sample dialogues to
a significant difference in opm between the human-                        familiarize them with the structure of a con-
and AI-produced text. This gave us a list of items                        versation. It is possible that something about
overused by ChatGPT.                                                      ChatGPT’s fine-tuning data leads it to favor
   In the third step of our analysis, we returned to                      certain words (e.g., if the focal words are over-
the list of 50 spiking words to ask: Is the word                          represented in the sample dialogues).
also on the ChatGPT-overuse list? If so, then it
became a “focal word” (Figure 3). This gave us a                       3. Architecture Another possibility is that there
list of 21 focal words (Figure 4 and Appendix A).1                        is something about the architecture of LLMs,
                                                                   a given token, the focal word list contains inflected forms
   1
       Since the part-of-speech category is not always clear for   instead of lemmata.
                                                               6399
                  Figure 3: Our method for the systematic identification of focal words.


   or perhaps ChatGPT in particular, that causes            of why ChatGPT has this association.
   them to overuse certain words. Maybe LLMs’
   transformer architecture tends to privilege           6. Reinforcement Learning from Human
   some lexical items over others in an as-yet-             Feedback (RLHF) Human feedback is used
   unrecognized way. (Even if this explanation              in later training stages to give LLMs informa-
   proves correct, the question remains why this            tion about what a quality output looks like. A
   particular set of words is overrepresented.)             human evaluator might rate several potential
                                                            responses, for example, with the model then
4. Choice of Algorithms LLM development in-                 trained with reinforcement learning to pro-
   volves many different algorithms. Tokeniza-              duce responses similar to highly-rated exem-
   tion algorithms, for example, segment an in-             plars. It is possible that this human feedback
   put string into discrete lexical items. It is            encodes a preference for certain words. If re-
   possible that the choice of one algorithm over           sponses containing “delve” and “intricate” are
   others causes lexical overrepresentation. Why            rated more highly by evaluators, it would ex-
   the algorithm does so, and why these particu-            plain why there is overrepresentation of these
   lar words are overused, would then be further            words in model outputs.
   questions.
                                                       7. Other factors This list of potential explana-
5. Context Priming A well-known strength of               tions is not exhaustive. Many other choices
   LLMs is sensitivity to genre. Their outputs            – e.g., parameter settings, including tempera-
   are highly dependent on the domain and style           ture, Top K – might influence lexical overrep-
   requested by the prompt. Perhaps there is              resentation in LLM outputs.
   something about being asked to write scien-
   tifically that causes ChatGPT to overuse the      Apportioning responsibility for lexical overrepre-
   focal words. That is, maybe ChatGPT as- sentation to these factors is not straightforward.
   sociates scientific writing in particular with    The puzzle of lexical overrepresentation arises in
   words like “delve” and “intricate.” This expla- part because LLMs are to some extent “black boxes”
   nation, if correct, raises the further question   (Knight, 2017; Sculley et al., 2015). Pending
                                                  6400
              Figure 4: Occurrences per million words in PubMed abstracts for our 21 focal words.


further advances in LLM explainability or inter-          Arxiv abstracts (accessed 4 Aug 2024; contains
pretability (e.g., Templeton 2024), we may struggle       data from 1986 onwards, averaged over all years),
to understand many aspects of their behavior. An          the Leipzig Corpus Collective (Goldhahn et al.
additional obstacle, however, is that many aspects        2012; the English LCC contains mostly news texts
of LLM construction are closely-guarded secrets.          and transcriptions, data from 2005 onwards; pre-
Information that would help discriminate between          processed snapshot from a previous project), and
the potential explanations above is not public, even      Wikipedia articles and discussions (Foundation
for open source models. For instance, we do not           2024, accessed 4 Aug 2024). The results are pre-
know exactly what data LLMs are trained on (rele-         sented in Appendix B. The opm of the focal words
vant to #1 above), which fine-tuning steps there are      in our ChatGPT-3.5-generated abstracts far exceeds
(#2), what genres the models are exposed to during        their opm in the four datasets examined.
training (#5), and who the human evaluators are
(#6). In the remaining sections we pursue several
indirect ways of probing potential explanations of          Second, we conducted a similar analysis for var-
the puzzle of lexical overrepresentation.                ious varieties of English using the International
4 Searching for Overrepresentation in                    Corpus of English (ICE; Kirk and Nelson 2018).
                                                         Although ICE is relatively small compared to the
    Possible Training Data
                                                         other datasets (the subcorpora for most varieties
Our focal words are overrepresented in text gen- contain about one million words), we do not find
erated by ChatGPT compared to earlier PubMed             evidence that the focal words are especially preva-
abstracts. Other research indicates that such words      lent in any particular variety of English (see Ap-
also appear less frequently in related datasets in the   pendix G). This suggests that the overrepresenta-
pre-LLM era (Liang et al., 2024b,a; Gray, 2024). tion of focal words in ChatGPT’s outputs is prob-
Although we do not know exactly what data LLMs           ably not due to an overrepresentation of a certain
have been trained on, these results cast doubt on        variety of English in its training data. It has been hy-
the hypothesis that ChatGPT is using words like          pothesized that LLMs might frequently use words
“delve” and “surpass” frequently because they oc- like “delve” because they are more common in va-
cur frequently in its training data.                     rieties of English spoken by human evaluators who
   To further demonstrate that the focal words are       provide fine-tuning data, such as Nigerian English
probably not overrepresented in the training data, (Hern, 2024). Our initial analysis of ICE does not
we analyzed several additional datasets, namely: support this hypothesis.
                                                      6401
5   Model Choices: Architecture and                      2-Chat is considerably less “surprised” by AI-
    Algorithms                                           generated abstracts, in which the focal words are
                                                         overrepresented. This suggests the overuse of focal
Could choices about model architecture or algo-
                                                         words might be driven by some factor that differs
rithms be responsible for the puzzle of lexical over-
                                                         between the models. Given that model architec-
representation? To probe this, we would ideally
                                                         ture and many algorithms are held constant across
build an LLM ourselves and test the impact of each
                                                         Llama 2-Base and Llama 2-Chat, our findings sug-
potential factor on the prevalence of focal words.
                                                         gest that these factors are not the primary causes of
This requires vast resources, however, and is be-
                                                         lexical overrepresentation. Instead, they indicate
yond most researchers’ capabilities, including our
                                                         that fine-tuning and RLHF – which differ between
own. A more feasible alternative would be to in-
                                                         the models – might be important contributors.
vestigate a model that has several released variants
                                                            These results are necessarily limited. We can-
– e.g., different versions of the same model using
                                                         not claim definitively that the observed difference
different optimization algorithms. Such a model
                                                         between the models is driven by the prevalence
must also be queryable with respect to information-
                                                         of focal words rather than some other feature of
theoretic measures like entropy (Shannon, 1948).
                                                         AI-generated text. Moreover, most of our paper is
To our knowledge, no LLM offers such fine-grained
                                                         concerned with ChatGPT rather than Llama. The
releases.
                                                         difficulty is that there are no models of ChatGPT
   The closest we could find is the comparison be-
                                                         (v.3 or above) that can be queried in the described
tween Llama 2-Base (Llama-2-7b-hf) and Llama
                                                         fashion. We think Llama is a useful approximation.
2-Chat (Llama-2-7b-chat-hf; Touvron et al. 2023).
We used the Llama 2 models because they are more
similar to ChatGPT-3.5 than Llama 3 (Chiang et al.       6   RLHF: An Experimental Approach
2024; but Llama 3 produces similar results; Ap-          Our model testing with Llama suggested that RLHF
pendix D). The main difference between these two         might contribute to lexical overrepresentation. This
versions of Llama is that Llama 2-Chat includes          hypothesis has intuitive plausibility: when human
fine-tuning and RLHF, whereas Llama 2-Base does          evaluators assess alternative answers to a query,
not. Llama models can also be queried for per-word       perhaps they are exhibiting a preference for an-
entropy (Jurafsky and Martin, 2024).                     swers containing certain words. Since LLMs are
                           n                             trained to align their answers with human prefer-
                       1X
         Hp-w ent = −         p(xi ) log p(xi )    (1) ences, they would learn to use those words more
                       L
                          i=1                            frequently (Christiano et al., 2017; Ziegler et al.,
   By comparing the two models’ per-word entropy         2019). To further investigate this potential explana-
for human- and AI-generated abstracts, we could          tion, we conducted an exploratory online study in
assess which was more “surprised” by abstracts           which participants indicated whether they preferred
with an overrepresentation of focal words. Any           scientific abstracts that contained our focal words.
difference between the models provides evidence             Materials. We randomly sampled shorter
about the source of lexical overrepresentation. We       PubMed abstracts (70-100 words) from the year
provided our sample of 10,000 human-written ab- 2020 and, with Python and using the OpenAI API,
stracts to both versions of Llama 2, followed by the     used ChatGPT-3.5 to rewrite them with and with-
abstracts rewritten by ChatGPT-3.5 (see Section 2). out focal words. (Shorter abstracts were used to
The results are presented in Table 1.                    keep stimuli of a manageable length for partici-
                                                         pants.) For the focal-word abstracts, the prompt in-
               Llama 2-Base Llama 2-Chat                 cluded four randomly selected words from our list
    Human           1.616               1.051            of 21 focal words. An example prompt is: “Please
    AI              1.633               0.886            write a 100-word abstract for the following sci-
Table 1: Per-word entropy for human abstracts com-       entific paper, using words such as ’delves,’ ’un-
pared to ChatGPT-generated abstracts. Higher values of   derscores,’ ’surpasses,’ and ’emphasizing’: [SUM-
entropy mean that the model is more “surprised.”         MARY].” (The summary was generated via the
                                                         procedure described in Section 2.) The script in-
   We observe that Llama 2-Base is slightly less         structed ChatGPT to generate and revise an abstract
“surprised” by human-written text, while Llama           until it contained at least three focal words. For the
                                                      6402
no-focal-word abstracts, we used a similar prompt: participant failed one of the attention checks, their
“Please write a 100-word abstract for the following     data were disregarded. Participants were warned
scientific paper, making sure not to use words such     if they were proceeding unrealistically fast (0.25
as [list of blockwords]: [SUMMARY].” The block- * (225 ms + 25ms * character length of an item)),
words included the 21 focal words plus another 21 and items with excessively fast rating times were
words identified using the methodology described        excluded from our analysis (following the method-
in Section 2. The script prompted ChatGPT to gen- ology from Häussler and Juzek 2017). We also
erate and revise an abstract until it contained none    excluded data from participants who completed
of the blockwords.                                      less than 10 out of the 20 items. After exclusions,
   We created 200 items, each consisting of one         we analyzed a total of 1822 ratings, with 1215 rat-
abstract with focal words and one without (for the      ings for distractor items and 607 ratings for critical
same paper). We manually filtered out a handful         items, resulting in each critical item receiving an
of ungrammatical or nonsensical abstracts. Con- average of 20.2 ratings (stdev: 3.4). Given the study
siderably more than half of the abstracts with focal    compensation, the high exclusion rate came as a
words included “delve” in the first sentence; we        surprise.
call items containing these abstracts “delve-initial”      Analysis. Our original plan was to test all 30 crit-
items. To compile a bank of 30 critical items, we       ical items together in a chi-square analysis against
selected the 15 delve-initial items and the 15 other    the distractor items (an approximation of random
items with the smallest difference in length be- choices), to assess whether participants preferred
tween the abstracts with and without focal words. abstracts containing focal words. These results are
(We capped delve-initial items at 50% to prevent        reported below. However, during the generation of
participants from detecting the study’s purpose.) the abstracts, we noticed the aforementioned excess
We also constructed 30 pairs of distractor items        of delves in the first sentence and split the critical
in the same manner as the critical items, except        items into delve-initial items and other items. A
both abstracts were generated using the no-focal- lower N per condition and a higher-than-expected
word prompt. A full list of experimental items          exclusion rate left us considerably below the origi-
can be found on Github, and two examples are in         nally estimated sample size from a pre-study power
Appendix G.                                             analysis. Thus, we added an exploratory mixed-
   Participants. We used Prolific (prolific.com) to     effects logistic regression model, with rating as the
recruit participants. Public information about the      dependent variable and condition as the indepen-
human evaluators employed to provide feedback           dent variable, including items as a random effect
in RLHF is limited (Ouyang et al., 2022; Perrigo, (rating condition + (1 | item_id)). Distractor items
2023), so we recruited 201 participants from In- served as the intercept condition. For delve-initial
dia (140 male, 61 female). Average age was 31.3         items and other items, a preference for the focal-
years (stdev: 10.6). We also collected data on self- word abstract was encoded with 0, and a preference
assessed English proficiency and first languages        for the no-focal-word abstract with 1. For the dis-
(see our GitHub). Participants were compensated         tractor items, there are two no-focal-word abstracts,
at an average rate of $15 per hour.                     randomly encoded as 0 or 1.
   Task and Exclusions. The study began with               Results. Contrary to our expectations, when
IRB information, followed by task instructions, and     all critical items are analyzed together, there is a
then the items. An image of the interface can be        slight preference for the no-focal-word abstracts.
found in Appendix E. Participants evaluated 20          However, this overall difference between all criti-
items in total, indicating which abstract they pre- cal items and distractor items is not significant in
ferred out of the two presented. The first item was     a chi-square test (p = 0.174). The follow-up analy-
a calibration item, followed by (in random order) 5     sis suggests that this outcome might be driven by
critical items, 10 distractor items, 2 items checking   the delve-initial items, as Figure 5 illustrates. In
language abilities, and 2 attention checks (“This       the logistic regression model, we observe that the
is not a real item, please click on the left button” coefficient for the distractor items, represented by
inserted in the middle of the text). Thus, the propor- the intercept condition, is 0.500 (rounded to the
tion of critical items was 25%. Each time an item       third digit). This indicates that participants did
was displayed, it was randomly determined which         not exhibit a significant preference between the
abstract was displayed on the left vs. right. If a      distractor item abstracts, validating our methodol-
                                                     6403
ogy (Appendix F). The analysis also shows that            plain why participants preferred the abstracts with-
delve-initial items differed significantly from the       out focal words in the delve-initial items (which
distractors (p = 0.023), with a coefficient of 0.082,     coincides with a general downturn in sentiment
indicating that for the delve-initial items, partici-     towards LLMs; cf. Leiter et al. 2024), though we
pants preferred the abstracts without focal words.        would like to see these results confirmed with a
Participants exhibited a slight but non-significant       larger sample.
preference for abstracts with focal words for the            Having split the critical items in two, a higher N
other critical items (coefficient = -0.017; p = 0.651).   is needed to draw any conclusions about RLHF as
The group variance was small (0.003), indicating          a source of lexical overrepresentation, particularly
that most of the variability in the ratings was due to    given that we would expect a preference for focal-
the fixed effects. The model converged successfully       word abstracts to be subtle. The study warrants
(log-likelihood = -1324.9522, mean group size =           a follow-up. We believe that forcing ChatGPT to
30.4). A Wald test to determine whether delve-            use certain words when generating abstracts was
initial items and the other items differed from each      suboptimal. For example, if an abstract does not
other was statistically significant (p = 0.03, Wald       initially convey anything about exceeding or out-
Test Statistic: 4.77).                                    performing, then a rewritten abstract that includes
   In looking at the responses for each individual        the focal word ’surpasses’ will naturally be worse
item, we consider a preference for the focal-word         than the no-focal-word baseline. We suspect that
or no-focal-word abstract of a given pair to be ro-       generating critical items in a different way would
bust if a random outcome falls outside the margin         yield clearer results.
of error, and marginal otherwise (illustrated for the
distractors in Appendix F). This analysis shows a         7   Discussion and Concluding Remarks
slight difference between delve-initial items and
the other critical items: participants exhibit a pref-     It has been observed that LLMs overuse certain
erence for the no-focal-word abstract in more of           lexical items, a fact even acknowledged by OpenAI
the delve-initial items, and a preference for the          (OpenAI, 2024). Our work formalized this find-
focal-word abstract in more of the other items.            ing and identified 21 focal words whose usage has
                                                           spiked in scientific abstracts and that are overused
                                                           by ChatGPT-3.5. These results provide additional
                                                           evidence that recent changes to Scientific English
                                                           are partly driven by LLMs. Our work also explored
                                                           possible explanations of the puzzle of lexical over-
                                                           representation. We failed to find evidence that train-
                                                           ing data, model architecture, or algorithm choices
                                                           play a role. However, model testing with Llama
                                                           was consistent with the hypothesis that RLHF con-
                                                           tributes to overuse of particular words by ChatGPT.
                                                           Our experimental results suggest that human evalu-
                                                           ators may treat “delve” differently from other focal
                                                           words.
Figure 5: Experimental results: Preferences between           Future research should further probe the impact
focal-word and non-focal-word abstracts in delve-initial   of each factor canvassed in Section 3 on lexical
and other items.                                           overrepresentation. (This includes model choices
                                                           and training data; despite our negative results, we
   What explains the difference between delve- suspect that these factors do influence the lexical
initial and the other critical items? We suspect that      choices of LLMs.) We would especially like to
some participants became or were already sensi- see further work on the role of RLHF. Unfortu-
tive to the occurrence of “delve.” Participants were       nately, there are several obstacles to such research,
probably disproportionately young people with an           particularly the lack of procedural and data trans-
affinity for technology, and so more likely to be fa- parency surrounding LLM development (Longpre
miliar with the discourse surrounding AI language          et al., 2024). Moreover, it seems that companies
use. Wariness about the word “delve” might ex- building LLMs often solicit feedback from workers
                                                        6404
who are underpaid, stressed, and under time pres- the opacity of LLMs, there are ways of probing
sure (Toxtli et al., 2021; Roberts, 2022; Novick, their behavior and internal workings. Understand-
2023). It is difficult to simulate these conditions       ing LLMs’ linguistic behavior is complicated by
ethically in a research environment. Many online          their complexity and by secrecy and other indus-
recruitment platforms, including Prolific, rightly        try practices, as mentioned above. Nevertheless,
require decent compensation.                              our work indicates that the puzzle of lexical over-
    Although it complicates further study, we think       representation is tractable. Indirect investigative
this economic reality lends plausibility to RLHF as       methods can help us explain LLMs’ linguistic be-
a source of lexical overrepresentation. Rushed hu- havior.
man evaluators might base their evaluations on the           Such research is important because we need to
presence of particular words rather than on content, better understand how LLMs are changing lan-
as the former is easier and quicker to evaluate than      guage. Almost all of our 21 focal words were al-
the latter. If certain words are treated as a proxy for   ready increasing in usage in the years leading up to
quality, that could explain their overrepresentation      the release of ChatGPT, suggesting that LLMs may
in LLM outputs. (We suspect, however, that Scien- accelerate language change (Matsui 2024; also see
tific English in particular played a minor role in the    Geng et al. 2024 and Yakura et al. 2024). With the
training of LLMs. It seems more likely that human         increasing prevalence of AI-generated text in many
evaluators rated academic writing in general, with        areas of life, LLMs are arguably influencing the
their preferences shaping LLMs’ scientific writing        language usage even of people who do not them-
through overspill.) This mechanism coheres with           selves interact with these models. Our findings also
our impression that a major social consequence of         show that lexical overrepresentation remains a fea-
LLMs is the decoupling of form and content. Many          ture of current iterations of ChatGPT (Appendix B),
of us take fluency or style as a signal of quality        indicating that the phenomenon is here to stay.
content (McNamara et al. 2010, and in an L2 con-             Still, it is difficult to predict just how AI will
text Kim and Crossley 2018). Because LLMs are             shape language in the future. Discussions on so-
masterful at generating fluid text in just about any      cial media and in academic discourse, plus our
style, this heuristic is radically undermined by the      exploratory findings for items with “delve,” indi-
increasing ubiquity of LLM-generated text. The            cate that there is some public awareness of LLMs’
irony is that, if our hypothesis about RLHF proves        overuse of particular words. This awareness could
correct, this heuristic has shaped model training as      influence future rounds of RLHF, leading to a re-
well. LLMs may be undercutting the very same              alignment of AI and human preferences. At the
heuristic that has shaped their own lexical prefer- same time, the language of today – lexical over-
ences.                                                    representations and all – will become the training
    It would be interesting to apply our method           data for the models of tomorrow, raising concerns
for identifying focal words to alternative datasets. about model degradation over time (Alemoham-
Although we drew abstracts exclusively from               mad et al., 2023; Briesch et al., 2023; Hataya et al.,
PubMed, future work could examine whether the             2023; Shumailov et al., 2023).
same focal words have been spiking in scien-                 One thing is certain: through LLMs, tech compa-
tific disciplines besides biomedicine, in domains         nies are having a global impact on language usage.
beyond Scientific English, and in non-English- We believe this strengthens the case for broader so-
language corpora. The method could also be used           cietal debate about the power and responsibilities
to probe lexical overrepresentation in LLMs other         of these companies. Moreover, our speculations
than ChatGPT. Our impression is that ChatGPT and          about how the feedback of rushed and underpaid
Llama overuse many of the same words, but a sys- workers might contribute to lexical overrepresen-
tematic investigation is needed. Finally, additional      tation compound ethical worries about the poor
work on the quirks of LLM-generated language              working conditions of tech companies’ employees
could look beyond the word level (Ortmann et al., in the Global South (Kwet, 2019; Gray, 2024; Ro-
2021). A virtue of our formalized approach to iden- hde et al., 2024). There are thus both moral and
tifying focal words is that it can be extended in         non-moral reasons to apply greater scrutiny to how
these and any number of other ways to better un- human feedback is collected and used in the train-
derstand how LLMs are driving linguistic change.          ing of LLMs.
    More generally, our research shows that despite
                                                       6405
Acknowledgments                                              Wikimedia Foundation. 2024. Wikipedia dump. Ac-
                                                               cessed: 4 August 2024.
Many thanks to Gordon Erlebacher, Grady Ward,
Olmo Zavala Romero, and participants in FSU’s                Mingmeng Geng, Caixi Chen, Yanru Wu, Dongping
SC Artificial Intelligence Seminar for their valuable          Chen, Yao Wan, and Pan Zhou. 2024. The impact of
                                                               large language models in academia: from writing to
input on this project. This research was supported             speaking. arXiv preprint arXiv:2409.13686.
by the FSU College of Arts and Sciences Start-up
Fund.                                                        Dirk Goldhahn, Thomas Eckart, Uwe Quasthoff, et al.
                                                               2012. Building large monolingual dictionaries at
                                                               the leipzig corpora collection: From 100 to 200 lan-
                                                               guages. In LREC, volume 29, pages 31–43.
References
Sina Alemohammad, Josue Casco-Rodriguez, Lorenzo             Andrew Gray. 2024. Chatgpt" contamination": estimat-
   Luzi, Ahmed Imtiaz Humayun, Hossein Babaei,                 ing the prevalence of llms in the scholarly literature.
   Daniel LeJeune, Ali Siahkoohi, and Richard G Bara-          arXiv preprint arXiv:2403.16887.
   niuk. 2023. Self-consuming generative models go
   mad. arXiv preprint arXiv:2307.01850.                     Ryuichiro Hataya, Han Bao, and Hiromi Arai. 2023.
                                                               Will large-scale generative models corrupt future
David Banks. 2017. The extent to which the passive             datasets? In Proceedings of the IEEE/CVF Interna-
  voice is used in the scientific journal article, 1985–       tional Conference on Computer Vision, pages 20555–
  2015, functional linguistic, 4 (12), 2-17.                   20565.

Yuri Bizzoni, Stefania Degaetano-Ortlieb, Peter              Jana Häussler and Tom Juzek. 2017. Hot topics sur-
  Fankhauser, and Elke Teich. 2020. Linguistic vari-           rounding acceptability judgement tasks. In S. Feath-
  ation and change in 250 years of english scientific          erston, R. Hörnig, R. Steinberg, B. Umbreit, and
  writing: A data-driven approach. Frontiers in Artifi-        J. Wallis, editors, Proceedings of Linguistic Evidence
  cial Intelligence, 3:73.                                     2016: Empirical, Theoretical, and Computational
                                                               Perspectives. University of Tübingen, Tübingen.
Martin Briesch, Dominik Sobania, and Franz Rothlauf.
 2023. Large language models suffer from their own           Alex Hern. 2024. TechScape: How cheap, outsourced
 output: An analysis of the self-consuming training            labour in Africa is shaping AI English. Accessed:
 loop. arXiv preprint arXiv:2311.16822.                        2024-08-12.
Huzi Cheng, Bin Sheng, Aaron Lee, Varun Chaudhary,           Dan Jurafsky and James H. Martin. 2024. Speech and
  Atanas G Atanasov, Nan Liu, Yue Qiu, Tien Yin                Language Processing. Online draft. 3rd ed. draft,
  Wong, Yih-Chung Tham, and Ying-Feng Zheng.                   Feb 3, 2024 release.
  2024. Have ai-generated texts from llm infiltrated
  the realm of scientific writing? a large-scale analysis    Minkyung Kim and Scott A Crossley. 2018. Modeling
  of preprint platforms. bioRxiv, pages 2024–03.               second language writing quality: A structural equa-
                                                               tion investigation of lexical, syntactic, and cohesive
Wei-Lin Chiang, Lianmin Zheng, Ying Sheng, Anasta-
                                                               features in source-based and independent writing. As-
  sios Nikolas Angelopoulos, Tianle Li, Dacheng Li,
                                                               sessing Writing, 37:39–56.
  Hao Zhang, Banghua Zhu, Michael Jordan, Joseph E.
  Gonzalez, and Ion Stoica. 2024. Chatbot arena: An
                                                             John Kirk and Gerald Nelson. 2018. The international
  open platform for evaluating llms by human prefer-
                                                               corpus of english project: A progress report. World
  ence. Preprint, arXiv:2403.04132.
                                                               Englishes, 37(4):697–716.
Paul F Christiano, Jan Leike, Tom Brown, Miljan Mar-
  tic, Shane Legg, and Dario Amodei. 2017. Deep              Will Knight. 2017. The dark secret at the heart of ai.
  reinforcement learning from human preferences. Ad-
  vances in neural information processing systems, 30.       Dmitry Kobak, Rita González Márquez, Emőke-Ágnes
                                                              Horvát, and Jan Lause. 2024. Delving into chatgpt
Stefania Degaetano-Ortlieb, Hannah Kermes, Ashraf             usage in academic writing through excess vocabulary.
   Khamis, and Elke Teich. 2018. An information-              arXiv preprint arXiv:2406.07016.
   theoretic approach to modeling diachronic change
   in scientific english. In From data to evidence in        Patrick Koppenburg. 2024.   Tweet on 01 april
  English language research, pages 258–281. Brill.             2024.    https://x.com/PKoppenburg/status/
                                                               1774757167045788010. Accessed: 2024-08-12.
Stefania Degaetano-Ortlieb and Elke Teich. 2018. Us-
   ing relative entropy for detection and analysis of pe-    Marie-Pauline Krielke. 2024. Cross-linguistic depen-
   riods of diachronic linguistic change. In Proceedings      dency length minimization in scientific language:
   of the second joint SIGHUM workshop on compu-              Syntactic complexity reduction in english and ger-
   tational linguistics for cultural heritage, social sci-    man in the late modern period. Languages in Con-
   ences, humanities and literature, pages 22–33.             trast, 24(1):133–163.
                                                         6406
Michael Kwet. 2019. Digital colonialism: Us empire          OpenAI. 2024. Tweet on 08 april 2024. https://x.
  and the new imperialism in the global south. Race &         com/ChatGPTapp/status/1777221658807521695.
  Class, 60(4):3–26.                                          Accessed: 2024-08-12.

Christoph Leiter, Ran Zhang, Yanran Chen, Jonas Be-         Katrin Ortmann, Adam Roussel, and Stefanie Dipper.
  louadi, Daniil Larionov, Vivian Fresen, and Stef-           2021. Computational Historical Linguistics: Annota-
  fen Eger. 2024. Chatgpt: A meta-analysis after              tions, Tools & Corpora. Ruhr-Universität Bochum.
  2.5 months. Machine Learning with Applications,
                                                            Long Ouyang, Jeffrey Wu, Xu Jiang, Diogo Almeida,
  16:100541.
                                                              Carroll Wainwright, Pamela Mishkin, Chong Zhang,
                                                              Sandhini Agarwal, Katarina Slama, Alex Ray, et al.
Alvin Ping Leong. 2020. The passive voice in scientific
                                                              2022. Training language models to follow instruc-
  writing through the ages: A diachronic study. Text &
                                                              tions with human feedback. Advances in neural in-
  Talk, 40(4):467–489.
                                                              formation processing systems, 35:27730–27744.
Weixin Liang, Zachary Izzo, Yaohui Zhang, Haley Lepp,       Billy Perrigo. 2023. Exclusive: Openai used kenyan
  Hancheng Cao, Xuandong Zhao, Lingjiao Chen, Hao-            workers on less than $2 per hour to make chatgpt less
  tian Ye, Sheng Liu, Zhi Huang, et al. 2024a. Moni-          toxic. Time Magazine, 18:2023.
  toring ai-modified content at scale: A case study on
  the impact of chatgpt on ai conference peer reviews.      Python Software Foundation. 2024. Python 3.
  arXiv preprint arXiv:2403.07183.
                                                            Jennafer Roberts. 2022. The precarious human work
Weixin Liang, Yaohui Zhang, Zhengxuan Wu, Haley               behind ai. Blog post.
 Lepp, Wenlong Ji, Xuandong Zhao, Hancheng Cao,
 Sheng Liu, Siyu He, Zhi Huang, et al. 2024b. Map-          Friederike Rohde, Josephin Wagner, Andreas Meyer,
 ping the increasing use of llms in scientific papers.         Philipp Reinhard, Marcus Voss, Ulrich Petschow,
 arXiv preprint arXiv:2404.01268.                              and Anne Mollen. 2024. Broadening the perspec-
                                                               tive for sustainable artificial intelligence: sustainabil-
Jialin Liu and Yi Bu. 2024. Towards the relationship           ity criteria and indicators for artificial intelligence
   between aigc in manuscript writing and author pro-          systems. Current Opinion in Environmental Sustain-
   files: evidence from preprints in llms. arXiv preprint      ability, 66:101411.
   arXiv:2404.15799.                                        Sujan Sarkar. 2023.  AI Industry Analysis: 50
                                                              Most Visited AI Tools and Their 24B+ Traf-
Shayne Longpre, Robert Mahari, Anthony Chen, Naana            fic Behavior. https://writerbuddy.ai/blog/
  Obeng-Marnu, Damien Sileo, William Brannon,                 ai-industry-analysis. Accessed: 2024-08-12.
  Niklas Muennighoff, Nathan Khazam, Jad Kabbara,
  Kartik Perisetla, et al. 2024. A large-scale audit of     David Sculley, Gary Holt, Daniel Golovin, Eugene
  dataset licensing and attribution in ai. Nature Ma-         Davydov, Todd Phillips, Dietmar Ebner, Vinay
  chine Intelligence, 6(8):975–987.                           Chaudhary, Michael Young, Jean-Francois Crespo,
                                                              and Dan Dennison. 2015. Hidden technical debt in
Kentaro Matsui. 2024. Delving into pubmed records:            machine learning systems. Advances in neural infor-
  Some terms in medical writing have drastically              mation processing systems, 28.
  changed after the arrival of chatgpt. medRxiv, pages
  2024–05.                                                  Claude Elwood Shannon. 1948. A mathematical theory
                                                              of communication. The Bell system technical journal,
Danielle S McNamara, Scott A Crossley, and Philip M           27(3):379–423.
  McCarthy. 2010. Linguistic features of writing qual-
  ity. Written communication, 27(1):57–86.                  Philip Shapira. 2024. Delving into "delve". Accessed:
                                                              2024-09-21.
Katrin Menzel. 2022. Medical discourse in late modern
                                                            Ilia Shumailov, Zakhar Shumaylov, Yiren Zhao,
  english: Insights from a multidisciplinary corpus of
                                                               Yarin Gal, Nicolas Papernot, and Ross Anderson.
  scientific journal articles. In Corpus pragmatic stud-
                                                               2023. The curse of recursion: Training on gen-
  ies on the history of medical discourse, pages 79–104.
                                                               erated data makes models forget. arXiv preprint
  John Benjamins.
                                                               arXiv:2305.17493.
National Library of Medicine. 2023. PubMed Database.        Adly Templeton. 2024. Scaling monosemanticity: Ex-
  https://pubmed.ncbi.nlm.nih.gov/. Accessed:                 tracting interpretable features from claude 3 sonnet.
  2024-08-12.                                                 Anthropic.
Jeremy Nguyen. 2024. Tweet on 30 march 2024.                Hugo Touvron, Louis Martin, Kevin Stone, Peter Al-
   https://x.com/JeremyNguyenPhD/status/                      bert, Amjad Almahairi, Yasmine Babaei, Nikolay
   1774021645709295840. Accessed: 2024-08-12.                 Bashlykov, Soumya Batra, Prajjwal Bhargava, Shruti
                                                              Bhosale, et al. 2023. Llama 2: Open founda-
Michael Novick. 2023. A.i.’s dirty secret: It’s powered       tion and fine-tuned chat models. arXiv preprint
  by digital sweatshops. Blog post.                           arXiv:2307.09288.
                                                        6407
Carlos Toxtli, Siddharth Suri, and Saiph Savage. 2021.    A    List Of Focal Words
  Quantifying the invisible labor in crowd work. Pro-
  ceedings of the ACM on human-computer interaction,
  5(CSCW2):1–26.                                              Word               opm      opm           Incr.
                                                                                 2020    2024             %
Jason Wei, Xuezhi Wang, Dale Schuurmans, Maarten
   Bosma, Fei Xia, Ed Chi, Quoc V Le, Denny Zhou,             delves             0.21    14.38       6697.14
   et al. 2022. Chain-of-thought prompting elicits rea-       delved             0.12     2.90       2240.47
   soning in large language models. Advances in neural        delving            0.12     2.38       1816.83
   information processing systems, 35:24824–24837.            showcasing         0.59     8.79       1396.03
Hiromu Yakura, Ezequiel Lopez-Lopez, Levin                    delve              0.58     8.50       1374.92
  Brinkmann, Ignacio Serna, Prateek Gupta, and Iyad           boasts             0.11     1.15        918.18
  Rahwan. 2024. Empirical evidence of large language          underscores        4.50    45.19        903.61
  model’s influence on human spoken communication.
                                                              comprehending      0.56     5.58        898.95
  arXiv preprint arXiv:2409.01754.
                                                              intricacies        0.60     5.22        772.85
Denny Zhou, Nathanael Schärli, Le Hou, Jason Wei,             surpassing         1.37    10.50        667.48
  Nathan Scales, Xuezhi Wang, Dale Schuurmans,                intricate          6.22    44.22        611.24
  Claire Cui, Olivier Bousquet, Quoc Le, et al. 2022.
  Least-to-most prompting enables complex reason-             underscoring       2.70    17.17        536.94
  ing in large language models. arXiv preprint                garnered           2.44    13.13        437.19
  arXiv:2205.10625.                                           showcases          0.82     4.31        422.45
                                                              emphasizing        8.30    41.27        397.12
Daniel M Ziegler, Nisan Stiennon, Jeffrey Wu, Tom B
  Brown, Alec Radford, Dario Amodei, Paul Chris-              underscore         7.42    36.40        390.65
  tiano, and Geoffrey Irving. 2019. Fine-tuning lan-          realm              2.25    10.85        381.10
  guage models from human preferences. arXiv                  surpasses          0.85     3.96        367.55
  preprint arXiv:1909.08593.                                  groundbreaking     0.87     3.75        330.42
                                                              advancements      12.49    47.17        277.59
                                                              aligns             1.55     5.68        266.97

                                                                      Table 2: Our 21 focal words.



                                                          B    Analysis Of Further Corpora and
                                                               GPT-4o
                                                         We used the same summaries from the sample of
                                                         10,000 abstracts and used a Python script to gener-
                                                         ate abstracts using GPT-4o-mini, which were then
                                                         analyzed as per Section 2. The system’s role was
                                                         set as ’You are a world-leading scientist.’ and the
                                                         prompt was the same as that used with GPT-3.5.
                                                         The results are very similar, with a few excep-
                                                         tions: ’boasts’ is no longer overused; ’delve’ is
                                                         still overused, but to a lesser extent; and the usage
                                                         of ’underscore’ has increased significantly. These
                                                         differences could be artifacts of the methodology
                                                         (the GPT-4-generated abstracts are based on the
                                                         same GPT-3.5 summaries used in Section 2), the
                                                         consequence of active intervention, RLHF workers
                                                         responding to overuse, and/or other factors. We
                                                         also conducted a spot-check with a prompt speci-
                                                         fying the role ’You are a helpful assistant.’ using
                                                         GPT-4o. For each role, we generated 500 abstracts
                                                         and analyzed them. There was no noticeable differ-
                                                         ence with GPT-4o-mini.
                                                      6408
       Word                 ChatGPT       ChatGPT            Arxiv         LCC       Pubmed           Wiki
                                  3.5       4o-mini
       of                    45624.84      42622.65      42842.72      27363.47     38634.99      23116.18
       and                   38889.24      32537.79      26395.28      28488.53     39469.96      21149.63
       the                   63174.05      55111.23      72009.63      59324.62     52139.05      53379.32
       data                    978.91       1075.59       2484.20        418.29      1734.75        142.81
       results                4074.64       3307.32       2352.13        244.52      1722.07         95.37
       i                        32.21         61.17        414.03       4715.42       214.82       8041.61
       year                     78.50         61.77         37.58       1076.29       217.25        397.61
       patients               4416.82       3936.56         48.97        131.48      4775.73         23.04
       advancements            319.37        407.59         22.54          2.56        15.53          1.11
       aligns                    6.71         19.99          6.68          1.32         1.89          0.90
       boasts                    5.37          0.61          0.43         14.11         0.16          1.48
       comprehending             6.71          7.27          1.77          0.37         0.99          0.31
       delve                    19.46         18.17          4.07          2.23         0.98          1.21
       delves                  183.17         23.01          3.20          0.79         0.32          0.53
       delved                    6.71          0.61          0.30          0.61         0.18          0.38
       delving                   8.72          0.61          0.72          0.76         0.24          0.61
       emphasizing             138.21        367.61         10.21          2.82         9.92          2.64
       garnered                 20.80        173.21          4.09          4.34         2.74          4.61
       groundbreaking           38.92         17.56          2.47          5.91         1.02          2.26
       intricate               163.04        316.14         17.87          4.79         6.22          2.13
       intricacies              15.43         27.25          1.98          1.24         0.68          0.68
       realm                    10.74         54.51         11.53          9.22         2.27          8.46
       showcases                28.85          4.24          3.19          4.65         1.05          1.46
       showcasing               30.19         58.14          5.89          5.42         0.75          1.65
       surpasses                 4.03          4.24         11.16          1.14         1.04          0.40
       surpassing                5.37         17.56          7.61          1.66         1.51          1.42
       underscore               18.12       1365.08          5.17          1.53         7.91          0.72
       underscores              60.39       1048.94          4.95          1.90         4.91          0.90
       underscoring             10.06        313.71          2.57          0.66         3.15          0.20

Table 3: Occurrences per million for selected baseline words and our 21 focal words. Results are averaged across all
given years of the corpus.


C     Examples Of Critical Items                            and TSCI recovery.
C.1    A delve-initial item                                No-focal-word abstract: This study explores
Focal-word abstract: This study delves into the         the impact of maintaining mean arterial blood pres-
impacts of maintaining mean arterial blood pres- sure (MABP) at 80mm Hg during prehospital and
sure (MABP) at a specific level during the prehos- initial hospital treatment on long-term neurological
pital and initial hospital phases of treatment for pa- outcomes in patients with TSCI. Results showed
tients with traumatic spinal cord injury (TSCI). The    a significant correlation between higher MABP
results show a strong correlation between maintain- levels and improved outcomes, with the strongest
ing MABP at 80 mm Hg and improved long-term             impact observed in the prehospital and operating
neurological outcomes. Specifically, prehospital        room phases. The benefits of maintaining MABP
and operating room levels had the greatest effect, at 80mm Hg were also observed in the first 2 days
while maintaining MABP at 80 mm Hg during the           in the NICU. These findings highlight the crucial
first 2 days in the neurointensive care unit (NICU) role of MABP management in minimizing neuro-
was also beneficial. These findings surpass previ- genic shock-induced damage and emphasize the
ous knowledge and highlight the advancements in         importance of maintaining adequate blood pressure
comprehending the relationship between MABP             in TSCI patients.
                                                     6409
C.2    A non delve-initial item                           values than human text.
Focal-word abstract: This paper showcases a                8b            Llama 3-Base         Llama 3-Chat
novel approach for targeting and disrupting c-di-          Human            1.862                1.174
GMP signaling pathways in bacteria. By utiliz-             AI               1.928                1.165
ing a c-di-GMP-sequestering peptide (CSP), the
researchers have developed a method to bind and            8b           Llama 3.1-Base       Llama 3.1-Chat
inhibit c-di-GMP, a key bacterial second messen-           Human            1.854                1.731
ger. Through structure-based mutations, a more             AI               1.838                1.653
powerful and compact variant of the CSP has been
created, effectively preventing biofilm formation
in Pseudomonas aeruginosa. This advancement               E     The Rating Interface
holds promise for controlling bacterial behaviors
mediated by c-di-GMP and could have implications
for the development of new antibacterial strategies.
The results of this study highlight the potential of
CSP as a tool for delving into the intricate mecha-
nisms of c-di-GMP signaling.
   No-focal-word abstract: A novel approach
has been devised for blocking c-di-GMP signal-
ing pathways, a crucial mechanism in bacterial cell
functioning. The technique employs a c-di-GMP-
sequestering peptide (CSP) that exhibits strong
affinity for c-di-GMP and effectively inhibits its sig-       Figure 6: The rating interface for our experiment.
naling. Through targeted mutations, a potent, short-
ened variant of CSP has been developed, demon-            F     Ratings For The Distractor Items
strating efficient inhibition of biofilm formation in
Pseudomonas aeruginosa. This innovative method
provides a highly promising strategy for targeting c-
di-GMP and holds potential for combating various
bacterial infections. Further studies could focus
on developing more potent and specific CSP vari-
ants to fully comprehend and utilize the role of
c-di-GMP in regulating bacterial functions.

D     Per-word Entropy for various Llama
      Models                                              Figure 7: The experimental results for individual dis-
                                                          tractor items.
We validate our results for various Llama models.
We use the latest versions available on 28 August
2024. We intend to extend our analysis to the larger, G Analysis of the International Corpus of
70bn parameter models. However, due to quota                 English
restrictions, we are unable to perform these calcula-
tions at this time. We expect that the results will be   An analysis of the Englishes of the world can be
similar and plan to include them once the account        found in Figure 8.
limitations are resolved.
   All models show a drop in average per-word en-
tropy for human input when comparing base mod-
els to chat models, with a more pronounced drop
observed for AI input. Most models show lower
entropy values for human text with the base model
compared to AI text. This pattern reverses in the
chat models, where AI text shows lower entropy
                                                      6410
Figure 8: Word frequencies for selected lexical items across various English variants.




                                        6411


## Extraction verification

- **Beginning checked:** rendered ACL PDF page 1 matched the title, authors, abstract, Figure 1, Introduction opening, footnote, and proceedings footer in the extraction.
- **Middle checked:** rendered ACL PDF page 8 matched the end of the online-study results, Figure 5, and the opening of Section 7 in the extraction.
- **End checked:** rendered ACL PDF page 15 matched Appendix G and Figure 8 in the extraction.
- **Structure checked:** 15 PDF pages; Sections 1-7; Figures 1-8; Tables 1-3; acknowledgments; complete references; Appendices A-G. The official ACL text contains 11,557 comparison tokens after layout-marker normalization, exactly matching both arXiv v1 and the repository's v106 PDF.
- **Known omissions:** none from the paper. Full upstream corpora are not redistributed in the supporting repository; that repository says they must be rebuilt from PubMed, arXiv, and Wikipedia. The archived repository tree preserves the released code, notebooks, focal-word inclusion sheet, filtered ratings, experimental items, and small PubMed samples, but not the hundreds-of-gigabytes analysis corpora or a complete publication environment.

## Preserved attachments

| Path | Role in the source | SHA-256 | Preservation / extraction notes |
|---|---|---|---|
| `human-eyes/references/sources/snapshots/attachments/juzek-ward-delve-coling-2025.pdf` | Authoritative final paper | `8ac94feadb43077cc294abb0f208d2bece1c16652bcafbfbd47a1720e2da86ed` | Downloaded directly from ACL Anthology; all 15 pages extracted; pages 1, 8, and 15 rendered and visually checked. |
| `human-eyes/references/sources/snapshots/attachments/juzek-ward-delve-arxiv-2412.11385v1.pdf` | Preprint version of the same work | `17f6dcf1a4ae8366c01b7f88b742623fbd5333f04f8ce0a4425779f04e595eea` | Downloaded directly from arXiv; 15 pages; text token-identical to the final ACL PDF after layout-marker normalization. |
| `human-eyes/references/sources/snapshots/attachments/juzek-ward-delve-code-0b7e2ba.tar.gz` | Complete supporting-code repository tree at reviewed commit | `8558922aa8a60b8406c17939f0a9f8541209c34ba69cc036669155ea945051bf` | Deterministic `git archive` gzip of all 39 tracked files at commit `0b7e2ba538bcc51ea538594512ef591ec24a1af1`; includes the v106 paper PDF, code, notebook outputs, experimental materials, filtered ratings, and small data samples. |
