# Word Overuse and Alignment in Large Language Models: The Influence of Learning from Human Feedback

- **Canonical URL:** https://arxiv.org/abs/2508.01930
- **Alternate access URLs:**
  - https://arxiv.org/pdf/2508.01930v1
  - https://arxiv.org/html/2508.01930v1
  - https://osf.io/jy48s/
  - https://osf.io/4nvjk/
  - https://github.com/tjuzek/lhf/tree/db52b0ee3eba6c09a4ec17d7f9e45d7d0c1db8ff
  - https://doi.org/10.1007/978-3-032-19096-3_16
- **Author / owner:** Tom S. Juzek and Zina B. Ward
- **Publisher:** arXiv preprint; author/workshop manuscript for BIAS 2025 at ECML PKDD; version of record published by Springer Nature Switzerland in CCIS (2026)
- **Published:** arXiv v1 submitted 2025-08-03; version of record published 2026, pages 243-259
- **Retrieved:** 2026-07-15
- **Stable identifier:** arXiv:2508.01930v1; DOI 10.1007/978-3-032-19096-3_16; OSF DOI 10.17605/OSF.IO/JY48S; supplement OSF DOI 10.17605/OSF.IO/4NVJK; repository commit db52b0ee3eba6c09a4ec17d7f9e45d7d0c1db8ff
- **Version / revision:** complete open arXiv v1 and byte-distinct but substantively equivalent author/workshop manuscript v2.0.0; current supporting repository at commit db52b0ee3eba6c09a4ec17d7f9e45d7d0c1db8ff; direct OSF supplement as retrieved 2026-07-15
- **Extraction method:** Official arXiv v1 PDF and the author-uploaded OSF/GitHub manuscript were downloaded directly; the 16-page author/workshop PDF was converted from its embedded text layer with Poppler `pdftotext -layout`; `pdfinfo`, `pdfimages -list`, and rendered pages 1, 8, and 16 were checked; arXiv HTML structure was compared against the PDF; the complete GitHub repository tree was downloaded at a pinned commit and every tracked file was inventoried; direct OSF supplement files were downloaded and hashed.
- **Full-text status:** complete
- **Access and transformation notes:** The complete open paper text, including captions, references, and the printed appendix, appears below. The authoritative PDFs are preserved unchanged. Plain-text line breaks, multi-column layout, and inline figures are best-effort transformations. The complete repository, including code, data, paper, supplements, images, ODS files, and the 18 MB annotated experimental-item table, is preserved as a tar archive; representative text files and the full tree inventory appear below. The Springer version-of-record landing page and metadata were accessible, but the chapter PDF required subscription access and was not used as the reviewed full text. The authors identify the included PDF as the author/workshop version.

## Full text

### Complete author/workshop paper text

Word Overuse and Alignment in Large Language
Models: The Influence of Learning from Human
                  Feedback

    Tom S. Juzek1[0000−0002−3204−3879] and Zina B. Ward1[0000−0003−0160−6656]⋆

                 Florida State University, Tallahassee FL 32306, USA



        Abstract. Large Language Models (LLMs) are known to overuse cer-
        tain terms like “delve” and “intricate.” The exact reasons for these lexical
        choices, however, have been unclear. Using Meta’s Llama model, this
        study investigates the contribution of Learning from Human Feedback
        (LHF), under which we subsume Reinforcement Learning from Human
        Feedback and Direct Preference Optimization. We present a straightfor-
        ward procedure for detecting the lexical preferences of LLMs that are
        potentially LHF-induced. Next, we more conclusively link LHF to lexi-
        cal overuse by experimentally emulating the LHF procedure and demon-
        strating that participants systematically prefer text variants that include
        certain words. This lexical overuse can be seen as a sort of misalignment,
        though our study highlights the potential divergence between the lexical
        expectations of different populations – namely LHF workers versus LLM
        users. Our work contributes to the growing body of research on explain-
        able artificial intelligence and emphasizes the importance of both data
        and procedural transparency in alignment research.

        Keywords: Computational linguistics · Large Language Models · Align-
        ment · Preference Learning · Lexical Overuse.


1     Introduction
Following the arrival of Large Language Models (LLMs), observers were quick to
note their tendency to overproduce certain lexical entries [1,2,3,4,5,6,7,8,9]. Much
of the discourse centered on Scientific and academic English, focusing on words
such as “delve”, “intricate”, and “realm.” For this reason, we also concentrate
on Scientific English here. While changes in Scientific English over decades and
centuries are well-documented [10,11,12,13], the language shifts following the
introduction of LLMs have been unprecedented, with certain words (like “delve”)
seeing a sudden and dramatic increase in usage.
    Thus, it has been established that certain lexical biases exist in LLMs, with
evidence demonstrating their influence on written language. However, the ques-
tion of why this lexical overrepresentation arises remains open. While some have
⋆
    Conceptualization: TSJ, ZBW (eq.). Code, Methodology: TSJ. Write-up: TSJ, ZBW
    (eq.). GitHub repository: github.com/tjuzek/lhf. Computational setup: 2024 Thelio
    Custom machine, GeForce RTX 3090.

2       T. S. Juzek & Z. B. Ward




Fig. 1. An illustration of the procedure used to identify lexical preferences that are
potentially induced by Learning from Human Feedback (LHF); created with Canva.

pointed to Learning from Human Feedback (LHF) as a significant contributor
to these lexical choices [14,15], conclusive evidence is still missing.
    Learning from Human Feedback is a procedure applied after initial model
training during which human evaluators indicate preferences through A/B test-
ing or ranking. It was first introduced in the form of Reinforcement Learning
from Human Feedback (RLHF; [16,17]), though a more recent and increasingly
popular form of LHF is Direct Preference Optimization (DPO), which aligns
models by directly optimizing for human preferences without relying on rein-
forcement learning [18]. LHF was introduced to align models more closely with
human preferences. Alignment, which reflects “how closely the model’s opinions
or stances mirror those of different social groups” [19], is a major challenge in
AI [20,21,22]. A model is misaligned for a target group when its output does
not align with the group’s opinions, values, and/or expectations. LHF is recog-
nized as a key factor contributing to the success of models like ChatGPT [23].
However, researching the effects of LHF is difficult due to lack of transparency
surrounding the procedures and datasets used in model development [24].
    The present study addresses the potential link between LHF and the lexical
choices of LLMs through a two-step process. First, we introduce a method for
identifying lexical preferences in LLMs that are potentially induced by LHF. This
procedure can aid efforts to mitigate the most extreme cases of lexical overrepre-
sentation (Section 2). Second, we conduct an experiment that emulates the LHF
procedure in order to test whether humans indeed prefer texts containing the
words identified by our initial procedure. This represents an empirical test of the
hypothesis that LHF plays a role in shaping LLMs’ lexical choices (Section 3),

                                            Word Overuse, LLMs, and LHF          3

based on one of Meta’s popular Llama models. While our findings provide evi-
dence for an LHF effect, other contributing factors remain to be systematically
investigated. Finally, we discuss the implications of our study (Section 4) and
its limitations (Section 5).

Related Work
Many studies explore the linguistic behavior of LLMs and their effects on (writ-
ten) human language [1,2,3,4,5,6,7,8], with a few investigating spoken language
[25,26]. Most of this work is situated at the word level, though there is also
research on syntactic behavior [27]. Procedures for identifying LHF-induced
overuse have been proposed [5,9], but these involve a manual component [5,9]
and/or have a different focus [5]. Similar concerns have been raised for other be-
haviors exhibited by LLMs (see the xAI literature; [28,29,30]). Overlap between
human linguistic preferences and model behavior has been shown, though with
a small sample [9]. For non-lexical form (such as boldface or emoji use), it has
been found that even subtle differences in preferences during human preference
training can result in substantial differences in model behavior [31].


2   Procedure to Identify Potentially LHF-Induced Lexical
    Preferences
As a first step, we develop a low-cost procedure to identify lexical preferences in
LLMs that may originate from LHF training. Our approach involves generating
language outputs from both a pre-LHF model and a post-LHF model and then
comparing word usage in the outputs. Here, we use Llama 3.2-3B Base and Llama
3.2-3B Instruct [33] (via the Hugging Face Transformers library [34]). The Llama
family is, to our knowledge, the closest available approximation between models
trained with and without LHF, which for Llama 3 involves Direct Preference
Optimization. At the time of our research, Llama 3.2 was the most recent version
of the Llama model family. While larger variants (11B and 90B) were available,
they primarily added multimodal capabilities; improvements in textual reasoning
abilities were minor [35]. At the time of research, a broader model comparison
would have been difficult: of all the major LLM developers, only Meta had
released both base and instruction-tuned models. Since then, models like OLMo
[36] and Falcon [37] have gained popularity and would now be strong options.
    There are other differences between Llama Base and Llama Instruct [33],
most notably instruction tuning, optimization for tooling, and safety mitigation.
However, none of these, including instruction tuning [38], are known to contribute
to lexical overrepresentation. LHF remains the most plausible contributor to
shifts in language output. This makes the Llama models well-suited for our
purposes. All technical implementations described in this paper were carried out
in Python 3 ([39]; v3.12.3).
    Although our study focuses on Scientific English, the procedure we present
is transferable to other domains. Here the procedure is applied to abstracts

4      T. S. Juzek & Z. B. Ward

from PubMed from 2020 [40], as this predates the mainstream availability of
LLMs. We randomly sampled 10 000 abstracts and filtered out those with fewer
than 40 words, which resulted in 9 853 abstracts. Each abstract was split in
half by word count (rounding down), and each of the Llama models, Base and
Instruct, were prompted to continue writing based on the initial half of the
abstract (Prompt: ‘Continue the following academic article: \“{first_half} ’).
Models were, if needed, cut off after twice the input length. The generated con-
tinuations were cleaned in order to remove issues such as generation loops (e.g.,
repetitive sentences) and meta-comments (e.g., “Certainly, here is ...”), using
GPT-4o [41,42] (Prompt: ‘The following text is meant to be a continuation of
a scientific abstract. In some of the continuations, however, the AI finishes the
abstract and continues with commentary. Please detect potential switches, and
remove any commentary: \n\n“{input_text}”\n\n Output only the cleaned ab-
stract. If the entire text is commentary, output an empty string.’).

    This process resulted in two corpora of PubMed abstract continuations: one
generated by Llama Base (totaling 2.3m words) and the other by Llama In-
struct (2.2m words). Both corpora were tagged for part-of-speech using spaCy
([43]; v3.8.3, en_core_web_sm v3.8.0, tagging of all data took about 140hrs),
enabling the disambiguation of identical surface forms across word categories
(e.g., “to_PART run_VERB” vs. “a_DET run_NOUN”) and the grouping of
conceptually related forms under a common lemma (“delve” and “delves”). Rel-
ative frequency usage was compared between the two corpora (similar to what
one sees in the Google Ngram Viewer [44]). Here and in Section 3, we focus
on statistically significant differences between Base and Instruct lexical usage,
determined through a chi-square test. The top five items showing an increase
in usage in the Instruct model compared to the Base model are as follows: “nu-
anced_ADJ (+8342%)”, “nuance_VERB (+6301%)”, “firstly_ADV (+4794%)”,
“reliance_NOUN (+3193%)”, “generalizability_NOUN (+3124%)”; also see Ta-
ble 1 for further entries and our GitHub for the full list.

    Our procedure serves as a proof of concept: the identification of lexical items
potentially favored by LHF can be automated. The procedure is validated in
part by the observation that many of the identified words have been discussed
in the literature on the distinctive lexical choices of LLMs [3,4,5,6,7,8,9]. How-
ever, the procedure does not necessarily identify words that are overused by
Llama Instruct relative to human-generated text; the operative comparison is
with Llama Base. Nevertheless, there seems to be considerable overlap between
the words overused by Instruct relative to Base, and the words overused by In-
struct relative to a human baseline. We compared the Llama Instruct outputs to
a human baseline, the actual second halves of the randomly sampled PubMed
abstracts. Almost all (813 out of 814) of the words used significantly more by
Llama Instruct than Llama Base (Table 1) were also used significantly more by
Instruct than in the human baseline. Thus, when it comes to the lexical items
that distinguish LLM-generated text from human-generated text, the procedure
in its current form effectively identifies many of the most extreme cases.

                                            Word Overuse, LLMs, and LHF          5

                Lemma_POS              opm Ll-B opm Ll-I Incr. %
                nuanced_ADJ               0.6      51.4     8342.8
                nuance_VERB               0.6       39      6301.7
                firstly_ADV               2.4      119.2     4794
                reliance_NOUN             1.2      40.1     3193.6
                generalizability_N        2.4      78.5      3124
                underscore_VERB           4.3      124.9    2829.1
                radar_NOUN                0.6      16.4     2590.6
                staffing_NOUN             0.6       13      2033.9
                socioemotional_ADJ        0.6       13      2033.9
                multifacete_VERB          0.6      11.9     1848.3
                flake_NOUN                0.6      10.7     1662.8
                interoceptive_ADJ         0.6      10.7     1662.8
                vocabulary_ADJ            0.6      10.7     1662.8
                theanine_NOUN             0.6      10.7     1662.8
                secondly_ADV              6.1      103.4    1597.8
                finish_NOUN               0.6      10.2      1570
                daa_NOUN                  0.6      10.2      1570
                necessitate_VERB          0.6       9.6     1477.2
                behavioral_NOUN           0.6       9.6     1477.2
Table 1. Lemmata and part-of-speech for the Top 20 words identified using the pro-
cedure described in Section 2. Compared are occurrences-per-million (opm) for Llama
Base (Ll-B) vs. Llama Instruct (Ll-I).




    Assuming such divergences from human-generated text are undesirable and
hence a form of bias (a point to which we will return in Section 4), the procedure
is a method for uncovering lexical biases in LLMs. The degree of such bias ob-
served in LLM outputs suggests that either no robust identification mechanisms
were applied during model development, or existing mechanisms have proven
too weak, which motivates the need for a procedure like ours. Our insights could
also inform the discourse on AI-generated text detection [45,46,47,48], as such
methods often rely on identifying atypical lexical items and distributions.
    The above results are consistent with the hypothesis that LHF is a primary
source of the lexical bias discussed in the literature. However, more conclusive
evidence is needed; and specifically, experimental validation is required to con-
firm that the lexical items whose usage by LLMs we pinpointed as potentially
LHF-induced are indeed preferred by human evaluators, thereby strengthening
the causal link between LHF and LLMs’ lexical choices.


3   Experimental Validation

At the core of the hypothesized link between LHF and LLMs’ lexical choices
is the idea that evaluators exhibit a subtle preference for certain lexical items,
a preference that is in fact so slight that it has obscured this very link. How-
ever, when scaled up, these minor preferences for specific lexical items become

6       T. S. Juzek & Z. B. Ward

entrenched and ultimately manifested in the output generations of LLMs. To
test this hypothesis, we created experimental items consisting of pairs of text
variants. In each pair, one variant exhibits fewer words previously identified as
potentially favored by LHF, while the other exhibits more such words, with all
other factors held as equal as possible, including length and content. This design
aims to isolate the effect of the presence of the lexical items identified above on
evaluator judgments.

3.1   Experimental Setup
Creation of Experimental Items. The ideal test of the hypothesis would
involve creating two random variants of a given abstract, repeating this for tens
of thousands of pairs, collecting human evaluations for all these pairs, and then
analyzing the ratings. The problem, however, is that detecting the hypothesized
subtle effect experimentally under this approach would require an extraordinarily
high number of ratings to achieve statistical significance. Thus, we opted for a
procedure that increases the lexical differences between items, while at the same
time maintaining comparable validity and being less resource-intensive.
    For 50 randomly selected PubMed abstracts from 2020, we prompted GPT-
4o to write summary notes (“The following text is an abstract from a scientific
paper:\n\n{input_text}\n\nSummarize the abstract in keywords, separate key-
words by commas.”; see example on our GitHub). Using these summary notes
as input, we then had Llama Instruct generate 500 abstracts (variants) for each
item (Prompt: ‘Based on the following keywords, write a 100-word abstract for a
scientific journal article: “{line_of_keywords}.” Reply with the abstract only.’),
resulting in a total of 25 000 variants (50 random abstracts * 500 variants). We
used GPT-4o to clean the abstracts (Prompt: ‘The following text contains a
scientific abstract, but sometimes further text:\n\n“ {input_text}”\n\nPlease
remove any irrelevant text, which can include titles, incomplete sentences, even a
comment that an abstract is to follow (\“Abstract: \”). Output only the cleaned
abstract.’). We controlled for length by filtering out candidates that were below
90 or above 110 words. It has been widely recognized that “delve” is an LLM-
associated word [3,5,7,8,9] and a corresponding backlash against it [9]. Thus, we
removed any variants containing any of the 21 most overused ‘AI words’ as dis-
cussed in [9], including words like “realm” and “groundbreaking”. After applying
these filters, our final set contained 8710 variants.
    For these items (also part-of-speech tagged), we calculated a score to measure
a word’s potential to have been favored by LHF (“LHF-Score”). Using the lexical
items identified in Section 2 as potentially promoted by LHF, we assigned a score
to each variant by summing occurrences of these items, weighted by their relative
rate of increase. This weighting reflects the idea that a single usage of a term like
“revolutionize_VERB”, which experienced an increase of +1160%, is probably
more indicative of the influence of LHF than using a term like “of_ADP”, which
saw an increase of only 2%. As such, the score focuses on relative changes: A
100% shift from 1 to 2 occurrences of a given word should be treated the same
as a shift from 1000 to 2000 occurrences in that same token span.

                                            Word Overuse, LLMs, and LHF          7

    The LHF-Score for a sequence is the sum of LHF-Scores for each token (w ).
The LHF-Score for a given token is its increase in percent between Llama Base
(B ) and Llama Instruct (I ), divided by one thousand (for ease of interpretabil-
ity); “opm” stands for occurrences per million and is just the frequency of a token
divided by the total number of tokens (N ), multiplied by one million.
                              n
                              X
            LHF-Score(S) =          LHF-Score(wi )
                              i=1
                           where                            
                             1     opmI (w) − opmB (w)
            LHF-Score(w) =       ·                     × 100
                           1000          opmB (w)
                           where
                           count(w)
                 opm(w) =           × 106                                      (1)
                               N
An LHF-Score was calculated for all 8710 variants generated for the 50 summa-
rized abstracts. For each of the 50 abstracts, we calculated the difference between
the variant with the lowest LHF-Score and the one with the highest LHF-Score.
We then selected the Top 30 abstract pairs with the largest Deltas while ensur-
ing that the pair of variants were length-matched (in two cases, a length match
was difficult, and we took the runners-up). The following hypothetical example
between Sequence 1 and Sequence 2 illustrates how the LHF-Scores were cal-
culated. The LHF-Score Delta is 0.31 (the score is calculated on lemmata and
part-of-speech, which are omitted below for simplicity). A real example can be
found on our GitHub.

(1)   This is an intricate example full of complex words (SUM)
      0.03 0 0 0.36        0.03    0 0 0.2         0     (=0.44)
(2)   This is a baseline example free from these words (SUM)
      0.03 0 0 0         0.03    0    0    0.07 0      (=0.13)

For the 30 selected items, the average LHF-Score for the variants with many of
the lexical items identified in Section 2 is 7.2 (average length: 105 words), and
the average LHF-Score for the variants with the fewest such items is 1.7 (average
length: 104 words). The complete set of experimental item pairs is available on
our GitHub repository. A small number of the words identified by the procedure
above do not seem likely to have been promoted by LHF, such as “radar” (see
Section 5). This introduces noise into the experiment. For instance, one vari-
ant of an abstract might include “radar”, resulting in a higher LHF-Score, even
though the in- or exclusion of such a word is unlikely to affect human preference
between the two variants. Such cases weaken the statistical power of the exper-
iment and increase the risk of a false negative outcome (the beta rate), thereby
favoring the null hypothesis [49]. We anticipate this effect to be minor, however,
given that the majority of lexical items previously identified do seem plausibly
the sort that are potentially promoted by LHF.

8       T. S. Juzek & Z. B. Ward

Participants. We recruited 400 participants (231 female, 169 male; average
age: 30.1 years, standard deviation: 9.8) through Prolific (www.prolific.com).
Tech companies often recruit LHF workers from the Global South [50,51,4,52].
To more closely emulate the process by which LLMs are trained, we recruited
participants from countries in the Global South where English is an official or
widely used language (see Appendix A for a full list of countries). 90% of our
participants were from Africa and 10% were from Southeast Asia. Participants
were compensated at a rate equivalent to an average of $15 per hour.




                   Fig. 2. The rating interface for our experiment.



The Task. The task began with IRB information (full instructions can be found
on our GitHub), followed by an introduction to the task (“In the following, you
will read a series of research summaries, with two alternatives next to each
other. Please express which alternative you overall prefer. Some of the items are
hard, do the best you can!”, with an example as per Figure 2), including an
example to familiarize participants with the process (for general best practices
of experimental design, we followed [53] and [54]). Each participant rated 25
pairs of text variants, consisting of 20 critical item pairs (in random order),
one calibration item at the beginning of the survey (where one variant was
deliberately poor), two randomly interspersed “gotcha” items (which contained
mid-sequence, “This is not a real item, please click on the left button”; cf. [54,55]),
and two randomly interspersed items to assess language proficiency, similar to
the calibration item. For each item, the left-right positioning of the abstracts
was randomly flipped to avoid positional bias [56,57]. We did not include fillers,
as the differences between the variants were subtle, and we were not concerned
that participants would guess the purpose of the study.

Exclusions. To ensure high-quality data, which is crucial for statistical power
[58], we applied exclusions. Only participants who completed 10 or more of the
25 items were included in the analysis (11 participants excluded). Participants
who failed to correctly answer both “gotcha” items were also excluded from

                                               Word Overuse, LLMs, and LHF             9

the analysis (158 participants excluded). The literature reports that (225 ms +
25ms * character length of an item) is a good approximation of the minimum
time physically required to read text [59]. To account for skimming or decisions
made on the basis of reading only part of each abstract, we used a less strict
threshold, excluding only ratings completed in less than 40% of this minimum
time. Participants were warned if they responded more quickly than this. If a
participant fell below this threshold on 5 or more items, all of their ratings
were excluded from the analysis (18 additional participants excluded; many of
the participants who failed the “gotcha” items would also have been excluded
by this speed criterion). After exclusions, we retained 4039 ratings (out of a
maximum of 8000 ratings: 400 participants * 20 ratings each), averaging about
135 ratings per item pair (minimum: 125 ratings). An exclusion rate of 46.8% is
in line with previous work [60,61,62,63,64].


3.2   Analyses

The null hypothesis is that participants’ choices between the high and low LHF-
Score abstracts do not diverge from what one would expect when flipping a fair
coin. The relevant alternative hypothesis is that participants show a preference
for variants containing more of the words identified previously as potentially
promoted by LHF – i.e., variants with a high LHF-score. For categorical, binary
preference data like ours, where observations are tested against an expected
baseline, a chi-square test is an excellent choice [49]. This is our main analysis.
Additionally, we provide descriptives for the 30 item pairs, and we perform a
mixed linear regression analysis to account for random effects. Our model in-
cludes the intercept as a fixed effect and participant and item as random effects.




Fig. 3. (a) Experimental results: Preferences between low LHF-Score variant vs. high
LHF-Score variant, for the 30 items. (b) Participant preferences for pairs with different
LHF-Score Deltas. Each dot represents the mean preference for one of 30 abstract pairs.
High LHF-Score Delta pairs contained "nuanced_ADJ."

10      T. S. Juzek & Z. B. Ward

3.3   Results

Overall, participants exhibited a highly significant preference for variants with
a high LHF-Score over variants with a low LHF-Score (52.4% to 47.6%; χ2 =
9.4, p < 0.01). This trend is consistent across items, as confirmed by the re-
gression model and the low variance observed across items (also see Figure 3).
The mixed-effects model (REML, N = 4038, log-likelihood = −2903.53) re-
vealed a significant intercept (β = 0.524, z = 33.20, p < 0.001), with low vari-
                      2
ance across items (σitem    = 0.006) and low to moderate variance across users
  2
(σuser = 0.104). Based on these findings, we reject the null hypothesis and
accept the alternative hypothesis: participants systematically and significantly
prefer variants containing more of the items identified in Section 2 as words
whose use by LLMs was likely promoted by LHF.
    Although we did not initially intend to analyze abstracts containing any
particular word, we noticed that sentence pairs in which the high RP-Score
abstract contains the adjective “nuanced” had a substantially higher LHF-Score
Delta (Figure 3 (b)). Further, the average preference for the high LHF-Score
variant is markedly lower for items containing “nuanced” (46.6%) compared to
sentence pairs without it (54.5%). It could be that items containing “nuanced”
stuck out to participants, leading them to disprefer those items, similar to what
has been observed with text that includes “delve” [9]. Additional data is needed
to substantiate this interpretation, however.


4     Discussion

It has been well established that Large Language Models output certain words
more frequently than a human baseline [3,4,5,6,7,8,9]. Our research advances the
discourse by addressing the why, providing evidence that Learning from Human
Feedback could be a primary source of this lexical overuse. We have identified
lexical entries that models trained on LHF use considerably more than models
without LHF training and then shown that texts containing many of these words
are preferred to texts with fewer of them.
     Furthermore, there is reason to think that the words used more by Llama
Instruct than by Llama Base are also the sorts of words overused by LLMs com-
pared to humans. To probe this connection to human language use, we extracted
the lexical entries discussed in the academic literature on lexical overrepresenta-
tion [4,5,6,7,8,9]. This resulted in a list of 32 lexical entries (see Appendix A). We
observe that 28 of these are also present in our Llama Base vs. Llama Instruct
list. Thus, almost all of the words that researchers have identified as overrepre-
sented in LLM-generated text compared to human-generated text appear more
in the outputs of Llama Instruct than Llama Base. And as we have shown exper-
imentally, these words are also favored by human evaluators, lending credibility
to the hypothesis that the overuse of certain words by LLMs (relative to human
usage) is at least partly the product of LHF. Our work therefore substantiates
the previously speculative link between lexical overrepresentation and LHF.

                                            Word Overuse, LLMs, and LHF         11

    It remains to be seen whether it is the demographics of the human evaluators
or something about the feedback task they are engaged in that explains why they
favor the sorts of words under discussion here. One notable observation is that
LHF workers tend to be young, and almost all of the words overrepresented in
LLM-generated text relative to human-generated text were already increasing
in usage before the advent of LLMs [8]. Taken together, these facts suggest that
lexical overuse in LLMs might be a form of normal intergenerational language
change [65], albeit an accelerated one, wherein the preferences of younger gener-
ations are propagated in LLMs. This aligns with observations that young people
tend to prefer AI-generated output over human-produced output [66].
    LHF workers are also typically located in the Global South [50,51], whereas
criticism of the increased usage of words like “delve” has predominantly origi-
nated from the Global North. Most of the academic research on the topic, such as
[4,5,6,8,9], has been conducted at institutions based in the Global North. Some
have speculated that the words overrepresented in LLM outputs might be more
common in the dialects of English spoken by these LHF workers [14,15], though
follow-up work has not yet substantiated this conjecture [9].
    It is also possible that it is the nature of the LHF task that is responsible
instead. Perhaps human evaluators, skimming quickly through unfamiliar text,
rely on the presence of certain words as a proxy for quality. It was shown that
human evaluators tend to prioritize style over content [67], which may explain
why evaluators treat certain words as indicative of good outputs. In that case, the
lexical preferences baked into LLMs through LHF might simply be task-driven.
Discriminating between these explanations – that is, determining whether age,
geographic location, dialect, or task features lead LHF workers to favor particular
words – requires future research.


5   Limitations

This work has several limitations. First, our analysis is restricted to Meta’s
Llama. Broader validation would require access to base and instruction-tuned
model variants from other LLM developers (such as OLMo or Falcon). Our anal-
ysis also focuses on English. Expanding this work to other languages would be
valuable. Furthermore, while our dataset contains approximately 2m tokens per
model, future work could scale this up. A likely artifact of the corpus size is the
occasional identification of lexical items that are not commonly cited as overused
by LLMs. For instance, the Instruct model uses the item “radar_NOUN” consid-
erably more often than the Base model (+2590%). A qualitative analysis of the
dataset, however, helps to make sense of this result: several PubMed abstracts in
our sample discuss “radar_NOUN”, and the Instruct model incorporates this into
its continuations, whereas the Base model does not. Thus, scaling our procedure
could improve the results.
    Potential language confounds in the experimental items might have impacted
our results. While we controlled for abstract length, other distinctive linguistic
features of LLM-generated text, such as specific syntactic structures or stylistic

12      T. S. Juzek & Z. B. Ward

elements (e.g., “It’s not about [X], it’s about [Y]” [73]), might correlate with the
presence of the words that we have identified, unknowingly contributing to higher
preference ratings. A qualitative inspection of the item pairs did not reveal any
clear patterns of such confounding features, but the possibility cannot be entirely
ruled out. Furthermore, although our experimental procedure aimed to emulate
the task situation of LHF workers, it did so imperfectly, as we cannot perfectly
simulate their working conditions for both ethical and practical reasons. Lastly,
while our experimental results clearly bear on the existing discourse about lexical
biases, the connection to human language use remains somewhat preliminary.
Further strengthening this connection would yield still further support for the
hypothesis that LHF is at least partly responsible for lexical overuse in LLM
outputs compared to human-generated text.


6    Conclusion

LHF is known to be a useful tool for aligning the outputs of LLMs more closely
with human expectations. Our results, however, suggest that an accidental byprod-
uct of such alignment efforts is lexical overuse. Does the overuse of particular
words by LLMs constitute a failure of alignment? And should developers inter-
vene to reduce the prevalence of these words? The answers to both questions
depend on whose lexical preferences LLMs ought to reflect. Our research sug-
gests that these models are making lexical choices that align with the preferences
and expectations of LHF workers; but these same lexical choices may not satisfy
consumers unhappy with LLMs’ overuse of words like “delve.”
    If intervention is desired, our procedure offers a straightforward way of iden-
tifying potential cases of lexical overuse. While some manual verification is still
needed, the procedure effectively identifies many of the most extreme instances
of potential overuse. Importantly, our findings also highlight one place where
interventions could be targeted: LHF datasets. Different strategies could be em-
ployed. For instance, developers and data scientists could diversify the workforce
of human evaluators providing feedback for LHF [15], or datasets could be ad-
justed post-collection to ensure greater balance.
    While we leave open the question of whether intervention is necessary, we note
a shift in the dynamics of language change: Workers from the Global South are
now influencing the language of language technologies, which are subsequently
deployed globally. In the past, changes have predominantly flowed in the oppo-
site direction [50,68]. However, those who wield this linguistic influence are in
positions of economic precarity rather than positions of power.
    Finally, our research contributes to the growing body of work on explain-
able AI [28,29,30]: Through systematic investigation, meaningful insights into
the workings of artificial neural networks can be gained (see also discussion in
[69]). However, a key difficulty for such research is the lack of transparency sur-
rounding LLM development [24]. This includes lack of process transparency, as
all major tech companies obscure the details of their LHF procedures, arguably
in part to avoid scrutiny of poor working conditions for human evaluators, who

                                              Word Overuse, LLMs, and LHF            13

are frequently underpaid and stressed [70,71,72]. Lack of data transparency re-
mains an issue as well, with many LHF datasets not being publicly available.
These failures of transparency are worrisome in light of the significant impact
that language technology has on global language usage. By facilitating insights
like those presented here, publicizing information about model training can aid
efforts to align LLMs more closely with human expectations.


References

1. Koppenburg, P.: Tweet on 01 April 2024. https://x.com/PKoppenburg/status/
   1774757167045788010, last accessed 2024/08/12
2. Nguyen, J.: Tweet on 30 March 2024. https://x.com/JeremyNguyenPhD/status/
   1774021645709295840, last accessed 2024/08/12
3. Shapira,      P.:   Delving     into   "delve".     https://pshapira.net/2024/03/31/
   delving-into-delve/, last accessed 2024/09/21
4. Gray, A.: ChatGPT "contamination": Estimating the prevalence of LLMs in the
   scholarly literature. arXiv preprint arXiv:2403.16887 (2024)
5. Kobak, D., González Márquez, R., Horvát, E.-Á., Lause, J.: Delving into Chat-
   GPT usage in academic writing through excess vocabulary. arXiv preprint
   arXiv:2406.07016 (2024)
6. Liang, W. et al.: Mapping the increasing use of LLMs in scientific papers. arXiv
   preprint arXiv:2404.01268 (2024)
7. Liu, J., Bu, Y.: Towards the relationship between AIGC in manuscript writing and
   author profiles: Evidence from preprints in LLMs. arXiv:2404.15799 (2024)
8. Matsui, K.: Delving into PubMed Records: Some Terms in Medical Writing Have
   Drastically Changed after the Arrival of ChatGPT. medRxiv (2024)
9. Juzek, T.S., Ward, Z.B.: Why Does ChatGPT "Delve" So Much? Exploring the
   Sources of Lexical Overrepresentation in Large Language Models. In Proceedings
   of the 31st International Conference on Computational Linguistics (pp. 6397-6411).
   https://doi.org/10.48550/arXiv.2412.11385 (2025)
10. Degaetano-Ortlieb, S., Teich, E.: Using relative entropy for detection and analysis
   of periods of diachronic linguistic change. In: Proc. 2nd Joint SIGHUM Workshop,
   pp. 22–33 (2018)
11. Degaetano-Ortlieb, S., Kermes, H., Khamis, A., Teich, E.: An information-theoretic
   approach to modeling diachronic change in scientific English. In: From Data to
   Evidence in English Language Research, pp. 258–281. Brill, Leiden (2018)
12. Bizzoni, Y., Degaetano-Ortlieb, S., Fankhauser, P., Teich, E.: Linguistic variation
   and change in 250 years of English scientific writing: A data-driven approach. Front.
   Artif Intell. 3(73) (2020)
13. Menzel, K.: Medical discourse in Late Modern English: Insights from a multidis-
   ciplinary corpus of scientific journal articles. In: Corpus Pragmatic Studies on the
   History of Medical Discourse, pp. 79–104. John Benjamins, Amsterdam (2022)
14. Hern, A.: TechScape: How cheap, outsourced labour in Africa is shap-
   ing     AI      English.    https://www.theguardian.com/technology/2024/apr/16/
   techscape-ai-gadgest-humane-ai-pin-chatgpt, last accessed 2024/08/12
15. Sheikh, H.: Why does ChatGPT use “Delve” so much? Mystery Solved. https:
   //hesamsheikh.substack.com/p/why-does-chatgpt-use-delve-so-much, last accessed
   2025/01/14

14      T. S. Juzek & Z. B. Ward

16. Christiano, P.F., Leike, J., Brown, T., Martic, M., Legg, S., Amodei, D.: Deep
   reinforcement learning from human preferences. In: Adv. Neural Inf. Process. Syst.
   (30) (2017)
17. Ziegler, D.M., Stiennon, N., Wu, J., Brown, T.B., Radford, A., Amodei, D., Chris-
   tiano, P., Irving, G.: Fine-tuning language models from human preferences. arXiv
   preprint arXiv:1909.08593 (2019)
18. Rafailov, R. et al.: Direct preference optimization: Your language model is secretly
   a reward model. In: Adv. Neural Inf. Process. Syst. (36) (2024)
19. He, Z., Guo, S., Rao, A., Lerman, K.: Whose Emotions and Moral Sentiments Do
   Language Models Reflect? arXiv preprint arXiv:2402.11114 (2024)
20. Bender, E.M., Gebru, T., McMillan-Major, A., Shmitchell, S.: On the dangers of
   stochastic parrots: Can language models be too big? In: Proc. 2021 ACM Conf. on
   Fairness, Accountability, and Transparency, pp. 610–623 (2021)
21. Santurkar, S., Durmus, E., Ladhak, F., Lee, C., Liang, P., Hashimoto, T.: Whose
   opinions do language models reflect? In: Int. Conf. on Machine Learning (ICML),
   pp. 29971–30004 (2023)
22. Durmus, E. et al.: Towards measuring the representation of subjective global opin-
   ions in language models. arXiv preprint arXiv:2306.16388 (2023)
23. Ouyang, L. et al.: Training language models to follow instructions with human
   feedback. In: Adv. Neural Inf. Process. Syst. (35), 27730–27744 (2022)
24. Bommasani, R. et al.: On the opportunities and risks of foundation models. arXiv
   preprint arXiv:2108.07258 (2021)
25. Geng, M., Chen, C., Wu, Y., Chen, D., Wan, Y., Zhou, P.: The impact of
   large language models in academia: from writing to speaking. arXiv preprint
   arXiv:2409.13686 (2024)
26. Yakura, H., Lopez-Lopez, E., Brinkmann, L., Serna, I., Gupta, P., Rahwan, I.:
   Empirical evidence of large language model’s influence on human spoken communi-
   cation. arXiv preprint arXiv:2409.01754 (2024)
27. Zamaraeva, O., Flickinger, D., Bond, F., Gómez-Rodríguez, C.: Comparing LLM-
   generated and human-authored news text using formal syntactic theory. arXiv
   preprint arXiv:2506.01407 (2025)
28. Sculley, D. et al.: Hidden technical debt in machine learning systems. In: Adv.
   Neural Inf. Process. Syst. (28) (2015)
29. Zhao, H. et al.: Explainability for large language models: A survey. ACM Trans-
   actions on Intelligent Systems and Technology 15(2), 1–38 (2024)
30. Cambria, E. et al.: XAI meets LLMs: A survey of the relation between explainable
   AI and large language models. arXiv preprint arXiv:2407.15248 (2024)
31. Zhang, X., Xiong, W., Chen, L., Zhou, T., Huang, H., Zhang, T.: From lists to
   emojis: How format bias affects model alignment. arXiv:2409.11704 (2024)
32. Erdocia, I., Migge, B., Schneider, B.: Language is not a data set—Why overcoming
   ideologies of dataism is more important than ever in the age of AI. J. Sociol. (2024)
33. Dubey, A. et al.: The LLaMA 3 herd of models. arXiv:2407.21783 (2024)
34. Wolf, T. et al.: Transformers: State-of-the-Art Natural Language Processing. arXiv
   preprint arXiv:1910.03771 (2020)
35. Hugging        Face      Team:       Open       LLM        Leaderboard.      (2024).
   https://huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard
36. Allen Institute for AI. (2024). OLMo 2. https://allenai.org/olmo
37. Technology Innov. Inst. (2024). Falcon 3. https://falconllm.tii.ae/falcon3/index.html
38. Juzek, T.S., Ward, Z.B.: Supplementary materials for "Word overuse and alignment
   in large language models: The influence of learning from human feedback". OSF,
   https://osf.io/4nvjk https://doi.org/10.17605/OSF.IO/4NVJK (2025)

                                               Word Overuse, LLMs, and LHF             15

39. Python Software Foundation: Python 3. https://www.python.org/, accessed 2024
40. National Library of Medicine: PubMed Database. https://pubmed.ncbi.nlm.nih.
   gov/, last accessed 2024/11/24
41. Achiam, J. et al.: GPT-4 technical report. arXiv preprint arXiv:2303.08774 (2023)
42. OpenAI: OpenAI Python API. Version 1.57. https://platform.openai.com/docs/,
   last accessed 2025/01/18
43. Montani, I., Honnibal, M., Boyd, A., Van Landeghem, S., Peters, H.: explo-
   sion/spaCy: v3.7.2: Fixes for APIs and requirements. Zenodo. https://doi.org/10.
   5281/zenodo.10009823 (2023)
44. Google: Google Books Ngram Viewer. https://books.google.com/ngrams/, last ac-
   cessed 2025/01/02
45. Lavergne, T., Urvoy, T., Yvon, F.: Detecting fake content with relative entropy
   scoring. Pan 8(4), pp. 27–31 (2008)
46. Chakraborty, S. et al.: On the possibilities of AI-generated text detection. arXiv
   preprint arXiv:2304.04736 (2023)
47. Mitchell, E., Lee, Y., Khazatsky, A., Manning, C.D., Finn, C.: DetectGPT: Zero-
   shot machine-generated text detection using probability curvature. In: Int. Conf. on
   Machine Learning (ICML), pp. 24950–24962 (2023)
48. Huang, Y. et al.: MAGRET: Machine-generated Text Detection with Rewritten
   Texts. In: Proc. COLING 2025, pp. 8336–8346 (2025)
49. Haslwanter, T.: An Introduction to Statistics with Python. Springer, CH (2016)
50. Kwet, M.: Digital colonialism: US empire and the new imperialism in the Global
   South. Race Class 60(4), 3–26 (2019)
51. Perrigo, B.: Exclusive: OpenAI used Kenyan workers on less than $2 per hour to
   make ChatGPT less toxic. Time Magazine (18) (2023)
52. Rohde, F. et al.: Broadening the perspective for sustainable artificial intelligence:
   Sustainability criteria and indicators for Artificial Intelligence systems. Curr. Opin.
   Environ. Sustain. (66), 101411 (2024)
53. Cowart, W.: Experimental Syntax. Sage, Thousand Oaks (1997)
54. Berinsky, A.J., Margolis, M.F., Sances, M.W.: Separating the shirkers from the
   workers? Making sure respondents pay attention on self-administered surveys. Am.
   J. Polit. Sci. 58(3), 739–753 (2014)
55. Maniaci, M.R., Rogge, R.D.: Caring about carelessness: Participant inattention
   and its effects on research. J. Res. Pers. (48), 61–83 (2014)
56. Friedman, H.H., Herskovitz, P.J., Pollack, S.: The biasing effects of scale-checking
   styles on response to a Likert scale. In: Proc. Amer. Stat. Assoc. Conf. on Survey
   Research Methods (792), pp. 792–795 (1994)
57. Chyung, S.Y., Kennedy, M., Campbell, I.: Evidence-based survey design: The use
   of ascending or descending order of Likert-type response options. Perform. Improv.
   57(9), 9–16 (2018)
58. Mahowald, K., Graff, P., Hartman, J., Gibson, E.: SNAP judgments: A small N
   acceptability paradigm (SNAP) for linguistic acceptability judgments. Language
   92(3), 619–635 (2016)
59. Häussler, J., Juzek, T.: Hot topics surrounding acceptability judgement tasks. In:
   Featherston, S., Hörnig, R., Steinberg, R., Umbreit, B., Wallis, J. (eds.) Linguistic
   Evidence 2016: Empirical, Theoretical, and Computational Perspectives. University
   of Tübingen, Tübingen. https://doi.org/10.15496/publikation-19039 (2017)
60. Downs, J.S., Holbrook, M.B., Sheng, S., Cranor, L.F.: Are your participants gaming
   the system? Screening Mechanical Turk workers. In: Proc. SIGCHI Conf. on Human
   Factors in Computing Systems, pp. 2399–2402 (2010)

16      T. S. Juzek & Z. B. Ward

61. Zhu, D., Carterette, B.: An analysis of assessor behavior in crowdsourced preference
   judgments. In: SIGIR 2010 Workshop on Crowdsourcing for Search Evaluation, pp.
   17–20 (2010)
62. Kazai, G., Kamps, J., Milic-Frayling, N.: Worker types and personality traits in
   crowdsourcing relevance labels. In: Proc. 20th ACM Int. Conf. on Information and
   Knowledge Management, pp. 1941–1944 (2011)
63. Thomas, K.A., Clifford, S.: Validity and Mechanical Turk: An assessment of ex-
   clusion methods and interactive experiments. Comp. Hum. Behav. (77), 184–197
   (2017)
64. Daniel, F., Kucherbaev, P., Cappiello, C., Benatallah, B., Allahbakhsh, M.: Quality
   control in crowdsourcing: A survey of quality attributes, assessment techniques, and
   assurance actions. ACM Comput. Surv. 51(1), 1–40 (2018)
65. Labov, W.: Principles of Linguistic Change, vol. 3: Cognitive and Cultural Factors.
   Wiley, Hoboken (2011)
66. Young, J. et al.: The Role of AI in Peer Support for Young People: A Study of
   Preferences for Human-and AI-Generated Responses. In: Proc. CHI Conf. on Human
   Factors in Computing Systems, pp. 1–18 (2024)
67. Wu, M., Aji, A.F.: Style Over Substance: Evaluation Biases for Large Language
   Models. In Proc. COLING 2025, pp. 297–312. Association for Computational Lin-
   guistics, Abu Dhabi, UAE. https://aclanthology.org/2025.coling-main.21/ (2025)
68. hMensa, P.A.: Artificial intelligence and the future of sociolinguistic research: An
   African contextual review. J. Socioling. (2024)
69. Templeton, A.: Scaling monosemanticity: Extracting interpretable features from
   Claude 3 Sonnet. Anthropic (2024)
70. Toxtli, C., Suri, S., Savage, S.: Quantifying the invisible labor in crowd work. Proc.
   ACM Hum.-Comput. Interact. 5 (CSCW2), 1–26 (2021)
71. Roberts, J.: The Precarious Human Work Behind AI. https://www.accel.ai/
   anthology/2023/5/22/jyzu7sbpzyxufu5l1ekidxj0g7jafh, last accessed 2023
72. Novick, M.: A.I.’s Dirty Secret: It’s Powered by Digital Sweatshops. https:
   //change-links.org/a-i-s-dirty-secret-its-powered-by-digital-sweatshops/, last ac-
   cessed 2023
73. Jim       the      AI      Whisperer:       How        One       Sentence      Pattern
   Can       Expose        AI      Writing.      Medium.         https://generativeai.pub/
   how-to-spot-ai-writing-with-one-sentence-pattern-8aa5b3ec5a63, accessed 2024/12


A     Appendix

Permitted Countries: Bangladesh, Belize, Botswana, Cameroon, Ethiopia,
Fiji, Gambia, Ghana, Guyana, Indonesia, Kenya, Liberia, Malawi, Malaysia,
Mauritius, Micronesia, Montserrat, Namibia, Nigeria, Pakistan, P. N. G., Philip-
pines, S. Africa, Sri Lanka, Swaziland, Tanzania, Uganda, Zambia, Zimbabwe.
Words from overuse literature: advancements, aligns, boasts, commendable,
comprehending, crucial, delve, delved, delves, delving, emphasizing, garnered,
groundbreaking, intricacies, intricate, invaluable, meticulous, meticulously, no-
table, noteworthy, pivotal, potential, realm, showcases, showcasing, significant,
strategically, surpasses, surpassing, underscore, underscores, underscoring.


### Direct OSF supplementary analysis (complete text)

# AI-Associated Words: Frequency Analysis of Instruction Tuning Datasets vs Baseline Scientific English

## Overview

The literature, when stating that overused words are not present in the training data, has yet to separately analyze data used for pre-training (training Large Language Models on vast amounts of text data) and data used for instruction tuning (training LLMs on data that makes them more useful as chat assistants). It was shown that for the domain of Scientific English, overused words (such as *delve* and *intricate*) are not present in likely pre-training data. This leaves open the possibility that these words are introduced into the models during instruction tuning.


## Datasets

Thus, as a sanity check, we analyzed three popular instruction tuning datasets:

1. [aya English Instruct (2024)](https://huggingface.co/datasets/CohereLabs/aya_dataset)
2. [Dolly (2023)](https://huggingface.co/datasets/databricks/databricks-dolly-15k)
3. [OASST1 English (2023)](https://huggingface.co/datasets/OpenAssistant/oasst1)

There are more instruction tuning datasets. Our focus is on datasets that consist of human preferences. any other datasets are AI-generated. Next, we combined these into a single dataset for analysis (0.7 million tokens). There are other instruction tuning datasets available, but many of them include AI-generated content and were therefore excluded from this analysis.

As a baseline, we used all PubMed abstracts from the year 2020 (337.6 million tokens), i.e. data from prior to the release of ChatGPT. Both datasets were part-of-speech tagged using the same methodology as described in the main paper. All analyses were performed on base forms (lemmas).

## Analysis

We used the list of 34 overused words identified in Galpin et al. (2025). Of these, 29 occurred in the PubMed 2020 dataset and were included in our analysis here.

PubMed 2020 abstracts serve as the baseline. We measured the relative change in normalized frequencies (occurrences per million words; *opm*) in the combined instruction dataset. A chi-square test was performed for each word to test for statistically significant differences, this test is well suited to the data structure.

## Expectations

This is a cross-domain comparison, so substantial differences are to be expected, regardless of whether instruction tuning contributes to lexical overuse.

If the instruction tuning datasets were not a significant source of lexical overuse in academic texts (H0), we would expect exactly that: notable variation when comparing instruction data to a human-authored baseline (PubMed abstracts), with some words appearing considerably more often, and others considerably less.

However, if instruction tuning is a source of lexical overuse in academic English as produced by LLMs (H1), we would expect a clear majority of the words in question to appear significantly more often in the instruction tuning datasets than in the human baseline.

## Results

The table below lists the part-of-speech-tagged base form (lemma), the percentage change between PubMed and instruction tuning datasets, opm values for each, and whether the difference is statistically significant.

| Lemma_POS           | Change (%) | OPM (PubMed) | OPM (Instruct) | Significant |
|---------------------|------------|--------------|----------------|-------------|
| underscore_NOUN     | 3496.88    | 0.08         | 2.77           | TRUE        |
| showcase_NOUN       | 1338.75    | 0.19         | 2.77           | TRUE        |
| realm_NOUN          | 458.88     | 2.23         | 12.46          | TRUE        |
| showcase_VERB       | 426.37     | 3.16         | 16.62          | TRUE        |
| notable_ADJ         | 333.50     | 14.06        | 60.94          | TRUE        |
| intricacy_NOUN      | 323.16     | 0.65         | 2.77           | FALSE       |
| intricate_ADJ       | 285.30     | 5.03         | 19.39          | TRUE        |
| delve_VERB          | 262.48     | 0.76         | 2.77           | FALSE       |
| comprehend_VERB     | 154.68     | 2.72         | 6.92           | FALSE       |
| strategically_ADV   | 73.18      | 1.60         | 2.77           | FALSE       |
| align_VERB          | 24.30      | 18.94        | 23.54          | FALSE       |
| advancement_NOUN    | 17.83      | 21.16        | 24.93          | FALSE       |
| emphasize_VERB      | -30.12     | 37.66        | 26.31          | FALSE       |
| surpass_VERB        | -32.82     | 4.12         | 2.77           | FALSE       |
| noteworthy_ADJ      | -36.77     | 4.38         | 2.77           | FALSE       |
| comprehending_ADJ   | -50.00     | 0.01         | 0.00           | FALSE       |
| underscore_VERB     | -56.90     | 12.85        | 5.54           | FALSE       |
| invaluable_ADJ      | -58.32     | 3.32         | 1.38           | FALSE       |
| potential_ADJ       | -63.97     | 476.63       | 171.73         | TRUE        |
| crucial_ADJ         | -78.82     | 104.62       | 22.16          | TRUE        |
| pivotal_ADJ         | -87.18     | 21.61        | 2.77           | TRUE        |
| significant_ADJ     | -89.92     | 934.09       | 94.17          | TRUE        |
| potential_NOUN      | -92.12     | 333.79       | 26.31          | TRUE        |
| groundbreaking_ADJ  | -96.88     | 0.09         | 0.00           | FALSE       |
| commendable_ADJ     | -98.55     | 0.20         | 0.00           | FALSE       |
| boast_VERB          | -98.65     | 0.22         | 0.00           | FALSE       |
| meticulously_ADV    | -99.43     | 0.52         | 0.00           | FALSE       |
| meticulous_ADJ      | -99.85     | 2.01         | 0.00           | FALSE       |
| garner_VERB         | -99.89     | 2.63         | 0.00           | FALSE       |

An illustration of the results can be found in the figure below.

## Discussion

We find no conclusive evidence that words overused by AI are also overused in human-created instruction tuning datasets. Accordingly, we interpret this as suggesting that the overuse is unlikely to originate in human-written instruction tuning data.

## References

Galpin, R., Anderson, B., & Juzek, T. S. (2025, May). *Exploring the Structure of AI-Induced Language Change in Scientific English*. In *The International FLAIRS Conference Proceedings* (Vol. 38).

## Visualization

![Illustration_of_overused_words_for_instruction_data_vs_baseline](instruction.jpg)


### Repository supplement: `A2_abstract_and_ai_keywords.tex` (complete text)

```tex
\textbf{Example of Abstract and AI-Generated Keywords for Summary} \\

Example of original PubMed abstract: ``Using a life course theory perspective, this qualitative descriptive study explored how Hispanic adolescent fathers view fatherhood, and how their perception of parenthood is shaped by critical life events. Hispanics are one of the largest ethnic groups, as well as one of the populations that is overrepresented in adolescent births in the United States. Despite this, Hispanic adolescent fathers are understudied and underrepresented in research. Participants were recruited from a community-based fatherhood program. Semi-structured interviews were conducted with Hispanic fathers, ages 16 years to 23 years. Participants conveyed their grief over fragmented family relationships and limited interactions with their own father. Some lived in hostile environments where they frequently experienced racism, discrimination, and neighborhood violence. The cumulative impact of these events resulted in substance use and emotional distress. Becoming a father was a sentinel event that helped resolve negative perceptions about fatherhood. Fatherhood also motivated participants towards a more productive, meaningful life.'' \\

\noindent AI-generated keywords: ``Hispanic, adolescent fathers, fatherhood, life course theory, qualitative descriptive study, critical life events, underrepresented, community-based program, semi-structured interviews, grief, family relationships, racism, discrimination, neighborhood violence, substance use, emotional distress, sentinel event, positive perceptions, meaningful life.''
```

### Repository supplement: `A3_LP_Score_example.tex` (complete text)

```tex
\textbf{A Full Example of High- and Low-LP-Score Variants} \\

For readability, words with an LP-score of $>$0.1 are highlighted in boldface, but part-of-speech is omitted. All items in both forms, with and without part-of-speech, can be found on our GitHub. \\

\noindent An example with a high LP-score: ``In a transgenic mouse model of melanoma, we \textbf{investigated} the effects of glutamine supplementation on tumour growth and survival under conditions of nutrient deprivation. Glutamine supplementation enhanced tumour growth, but when combined with a BRAF inhibitor, reduced tumour growth and increased survival. Metabolomic analysis revealed increased $\alpha$KG levels, \textbf{leading} to hypomethylation and H3K4me3 demethylation, promoting oncogenic pathways. Dietary intervention and \textbf{targeted} therapy \textbf{strategies} \textbf{targeting} these \textbf{epigenetic} modifications hold \textbf{promise} for melanoma treatment. \textbf{Furthermore}, \textbf{our} results \textbf{suggest} that glutamine supplementation may promote tumour growth, \textbf{potentially} through its role in $\alpha$KG synthesis, \textbf{highlighting} the \textbf{need} for \textbf{nuanced} nutritional approaches in cancer treatment.'' (100 words, LP-score:\ 12.6) \\

\noindent The following is the counterpart with a low LP-score: ``This study \textbf{employed} a transgenic mouse model of melanoma to \textbf{investigate} the effects of glutamine supplementation on tumour growth and survival under conditions of nutrient deprivation. The model was treated with a BRAF inhibitor, a common \textbf{targeted} therapy for melanoma. Metabolomic analysis revealed increased $\alpha$KG levels, \textbf{indicative} of glutamine metabolism, and associated with tumour growth and survival. Transcriptome analysis showed alterations in \textbf{epigenetic} marks, including hypomethylation and H3K4me3 modifications, in response to glutamine supplementation. These changes were correlated with activation of oncogenic pathways and improved tumour growth. Dietary intervention with glutamine also demonstrated enhanced tumour growth and survival in the model.'' (101 words, LP-score:\ 2.1) \\
```

### Repository supplement: `A4_IRB_instructions.tex` (complete text)

```tex
\textbf{IRB instructions} \\

``You are about to take part in a study whose goal it is to investigate language preferences. Your task will be to express a preference when presented with two choices. \\

\noindent Your participation is your free, rescindable choice. You will not be exposed to any known risks or uncertainties, there are not any known benefits, either. You can leave this study at any time, without specifying reasons.

\noindent Note:\ We do remove bad actors during the study and exclude their ratings from our analyses. For this, we collect the IP addresses -only of bad actors- and store these for about 24 hours.

\noindent We collect basic demographic information (age, gender, region, English proficiency) but your participation is anonymous and published data does not contain any identifiable information. Anonymised data will be published on Github.

\noindent Estimated time for completion is about 15 minutes. Payment will be delivered through the recruitment platform. The exact payment amount will be based on the rate previously agreed upon via the recruitment platform.

\noindent If you any questions or concerns, contact the Principal Investigator: [PI info omitted].

\noindent [Institutional Review Board info omitted] is overseeing this research. The [omitted] is a group of people who perform official independent review of research studies before studies begin to ensure that the rights and welfare of participants are protected. If you have questions about your rights or wish to speak with someone other than the research team, you may contact: [Institutional Review Board info omitted] \\

\noindent \textit{I have read and considered the presented information. I confirm that I understand the purpose of the research. I understand that I may contact the Principal Investigator at any time and can withdraw my participation without prejudice.}

\noindent \textit{By clicking the right-arrow button, I indicate my willingness to participate in this study.}''\\
```


### Supporting repository README (complete text)

# Word Overuse and Alignment in Large Language Models: The Influence of Learning from Human Feedback

This repository contains code and data for our paper: **"Word Overuse and Alignment in Large Language Models: The Influence of Learning from Human Feedback"**

## Overview
Large Language Models (LLMs) are known to overuse certain words, such as *delve* and *intricate*. This project investigates whether Learning from Human Feedback (LHF) contributes to this phenomenon. We introduce a method for identifying potentially LHF-induced lexical preferences and critically, we conduct an experimental study to test our hypothesis. Our experimental findings are consistent with the hypothesis that Learning from Human Feedback influences the lexical choices of Large Language Models.

## Citation

If you use this code or data, a citation is appreciated (though not required; see the licence).

The version of record is the Springer CCIS chapter (2026); an open preprint is available at arXiv:2508.01930.

```bibtex
@inbook{juzek-ward-2026-word,
  title     = {Word Overuse and Alignment in Large Language Models: The Influence of Learning from Human Feedback},
  author    = {Juzek, Thomas Stephan and Ward, Zina B.},
  booktitle = {Machine Learning and Principles and Practice of Knowledge Discovery in Databases},
  publisher = {Springer Nature Switzerland},
  year      = {2026},
  pages     = {243--259},
  doi       = {10.1007/978-3-032-19096-3_16}
}
```

## Contents
- **Paper:** The paper can be found under [bias2025_v_2_0_0.pdf](https://github.com/tjuzek/lhf/blob/main/bias2025_v_2_0_0.pdf); some of the procedures are explained in more detail in the paper, and if this is the case, pointers are given. Background, methodology, results, and conclusions are discussed in detail the paper.
- **Code:** These are the scripts used for our work. pipeline.md will talk you through the code step by step.
- **Data:** The data analysed in the paper, most importantly the raw data of the experiment.

## Licence

- **Code** (`code/`): MIT No Attribution (MIT-0). See [`LICENSE`](LICENSE). Use it freely, no attribution required.
- **Data** (`data/`, `appendices/`): CC0 1.0 Universal (public domain dedication). See [`LICENSE-DATA`](LICENSE-DATA).

External datasets and third-party resources retain their original licences.


### Contact

Our websites have our contact details:

- [Tom Juzek](https://mll.fsu.edu/person/tom-juzek)
- [Zina Ward](https://zinabward.com/)

The included paper PDF is the author/workshop version (version of record © Springer, CCIS 2026), separate from the code and data licences above.

## AI Assistance

Some of the code was written with the assistance of GitHub Copilot (marked as such in the code). Repository polished with Claude Code.

### Supporting repository pipeline (complete text)

# Instructions for reproducing our results

**N.B.:** In the `.py` files, you often need to adjust file paths and add API tokens. This is marked at the beginning of the scripts.


## Step 1: Download and process PubMed data

To get started, in `0_get_human_data`, we need to download the PubMed dataset (`download_dataset.py`), extract the abstracts from it (`extract_abstracts.py`), and pre-process the abstracts (`process_pubmed_files.py`). POS-tag the corpus using `pos_tag.py` in `1_postag`.


## Step 2: Sample abstracts from 2020

Next, we sample `n` abstracts from 2020 using `sample_human_abstracts.py` in `2_sample`.


## Step 3: Generate AI-continuations

Let Llama continue abstracts using `llama_write_oop.py` in `3_llama_abstracts`. Clean the abstracts with `remove_bases_repetitions.py` and `gpt_clean_abstracts.py`. The base model just continues, which is fine, so `gpt_clean_abstracts.py` will not remove much from it. However, the instruct model drifts off, with meta comments and reflections, so `gpt_clean_abstracts.py` is necessary for the instruct output.

At this point, use the POS-tagging script again on the cleaned base vs instruct output. Once this is done, in `4_find_focal_words`, use `brute_force_div.py` to detect differences in (POS-tagged) word usage. Reviewing the list in `change_reversed.tsv` (found in `data/focal_words`), we can already see many potentially LHF-induced items. The file `buzzwords.ods` was counter-checked against human 2020 vs. 2024 usage, compared to base vs. instruct over-usage. This is the automated procedure to assist in identifying LHF-induced items.


## Step 4: Experimental validation of LHF connection

The next step in the paper is to generate experimental items to validate the LHF connection. We sampled 50 human abstracts from 2020. Notably, Llama is not good at rewriting passages but performs better when writing from relatively elaborate notes. So, our approach is as follows:

- Have GPT generate high-quality notes based on the human abstracts using `create_notes.py` in `5_experimental_items`.
- Use `llama_writes_abstracts.py` to generate multiple abstract variants from the notes. The output file is too large for GitHub, but an example is available in `data/experimental_items/`.
- Clean the Llama-generated abstracts using `gpt_clean_abstracts.py`, which produces `50_sample_2020_ai_abstracts_cleaned.tsv`.
- Annotate the abstracts with `annotate_len_filter_abstracts.py`. This script performs two tasks:
  1. POS-tags the Llama abstract variants.
  2. Calculates the "buzziness" score for each abstract, across all variants.

The "buzziness" score is based on `change_reversed.tsv`, as explained in the paper. For the experiment, we need abstract pairs: one variant with few buzzwords and another with many. Having multiple variants helps us find pairs with a strong contrast.

To facilitate manual checking, we separate the items using `separate_items.py`, then apply `get_min_max.py` and select the 30 items with the highest min-max contrast. These are listed in `items.ods`.


## Step 5: Running the experiment

There are different ways to run the experiment. We used a custom-made, self-hosted website with a LAMP stack, so rerunning the experiment is non-trivial. Since details vary on one's implementation (which OS, which provider, etc.), we just give the code, which is in `6_website`.


## Step 6: Analysing experimental results

The experimental results are stored in `/data/experimental_results`, and the scripts in `/code/7_analysis` are used for analysis and plotting.

Technically, we start with `filter_data.py`, which generates `ratings.tsv` (already provided in the repository).

### Supporting repository complete file inventory at the reviewed commit

```text
CITATION.cff
LICENSE
LICENSE-DATA
README.md
appendices/A1_instruction_tuning.md
appendices/A2_abstract_and_ai_keywords.tex
appendices/A3_LP_Score_example.tex
appendices/A4_IRB_instructions.tex
appendices/instruction.jpg
bias2025_v_2_0_0.pdf
code/0_get_human_data/download_dataset.py
code/0_get_human_data/extract_abstracts.py
code/0_get_human_data/process_pubmed_files.py
code/1_pos_tag/pos_tag.py
code/2_sample/sample_human_abstracts.py
code/3_llama_abstracts/gpt_clean_abstracts.py
code/3_llama_abstracts/llama_write_oop.py
code/3_llama_abstracts/remove_bases_repetitions.py
code/4_find_focal_words/brute_force_div.py
code/5_create_experimental_items/annotate_len_filter_abstracts.py
code/5_create_experimental_items/create_notes.py
code/5_create_experimental_items/gpt_clean_abstracts.py
code/5_create_experimental_items/llama_write_abstracts.py
code/5_create_experimental_items/separate_items.py
code/6_website/button1.jpg
code/6_website/button7.jpg
code/6_website/done.php
code/6_website/favicon.ico
code/6_website/index.html
code/6_website/intro.php
code/6_website/rating.php
code/6_website/readme.txt
code/6_website/submit_demographics.php
code/6_website/submit_rating.php
code/6_website/submit_user.php
code/7_analysis/chi_squ.py
code/7_analysis/filter_data.py
code/7_analysis/plot_new.py
code/7_analysis/regression_analysis.py
data/experimental_items/50_sample_2020_ai_abstracts_annotated.tsv
data/experimental_items/50_sample_2020_ai_keywords.txt
data/experimental_items/EXAMPLE_50_sample_2020_ai_abstracts.tsv
data/experimental_items/EXAMPLE_50_sample_2020_ai_abstracts_cleaned.tsv
data/experimental_items/human_abstracts_50_sample_2020.txt
data/experimental_items/items.ods
data/experimental_results/filtered_ratings.tsv
data/experimental_results/item_tracker.tsv
data/experimental_results/problematic_users.tsv
data/experimental_results/ratings.tsv
data/focal_words/buzzwords.ods
data/focal_words/change_reversed.tsv
data/llama_abstracts/EXAMPLE_output_llama_base.tsv
data/llama_abstracts/EXAMPLE_output_llama_base_post_processed.tsv
data/llama_abstracts/EXAMPLE_output_llama_instruct.tsv
data/llama_abstracts/EXAMPLE_output_llama_instruct_post_processed.tsv
data/llama_pos_tagged/EXAMPLE_output_pos_llama_base.txt
data/llama_pos_tagged/EXAMPLE_output_pos_llama_instruct.txt
data/pubmed_non_processed/readme.txt
data/pubmed_pos_tagged/readme.txt
data/pubmed_processed/readme.txt
data/sample/EXAMPLE_human_abstracts_100_sample_2020.txt
data/sample/human_abstracts_50_sample_2020.txt
pipeline.md
```

The preserved repository attachment is the complete downloaded tree at the reviewed commit. Binary and large structured files are not transcribed into Markdown; their exact bytes remain in that archive.

## Extraction verification

- **Beginning checked:** Rendered page 1 was compared with the extracted title, authors, abstract, keywords, and opening of section 1; the title, author identities, abstract, and opening text agree.
- **Middle checked:** Rendered page 8 was compared with the extracted participant, task, and exclusion text and Figure 2 caption; the 400-participant description, 25-pair task structure, no-filler statement, and exclusion opening agree. The direct OSF `instruction.jpg` was also rendered and checked against the supplemental result table.
- **End checked:** Rendered page 16 was compared with references 61-73 and Appendix A; all 73 references terminate before the appendix, and the permitted-country and 32-word lists agree.
- **Structure checked:** Both open PDFs report 16 pages. The arXiv HTML contains the title, sections 1-6, Related Work, subsections 3.1-3.3, References, Appendix, one numbered data table plus one equation-layout HTML table, four figure elements, 73 bibliography items, and 41 paragraph containers; the PDF text contains the same substantive sequence. `pdfimages -list` identified the three substantive raster images on pages 2, 8, and 9. The complete repository inventory contains 63 files. Before form-feed normalization, the transcribed author/workshop extraction contains 747 lines, 6,940 words, and 49,103 bytes; the arXiv extraction contains 749 lines, 6,945 words, and 50,702 bytes, with the additional tokens limited to the arXiv version stamp. Beginning, middle, and end checks found no missing substantive section.
- **Known omissions:** The subscription-gated Springer typeset chapter PDF was unavailable. No substantive content is omitted from the complete open author manuscript, direct supplement, or preserved repository. The snapshot does not inline binary images, ODS workbooks, the 18 MB annotated TSV, or every code/data byte because their exact complete bytes are preserved in attachments; the full repository inventory above identifies them.

## Preserved attachments

| Path | Role in the source | SHA-256 | Preservation / extraction notes |
|---|---|---|---|
| `attachments/juzek-ward-word-overuse-alignment-arxiv-2508.01930v1.pdf` | Official open arXiv v1 paper | `262a579f73540250013cac8fb737d4c772392329c45c1c87f3a82300ca62d47c` | Preserved unchanged; all 16 pages have an embedded text layer; compared with the author/workshop manuscript. |
| `attachments/juzek-ward-word-overuse-alignment-author-workshop-v2.0.0.pdf` | Author-uploaded open workshop manuscript | `20b3d313d055ade030c3cf6bee1aeb08ea40c1281a46e6e3371e7571d5fbd71f` | Preserved unchanged; source for the complete text above and page-render checks. |
| `attachments/juzek-ward-word-overuse-alignment-repository-db52b0e.tar.gz` | Complete supporting repository at pinned commit | `8b98b98605cd038f681c9f938a72196f3b0da4ebf30a0de42c3dac730a563aa6` | Complete 63-file tree preserved, including source code, raw and filtered ratings, focal-word table, 30 experimental pairs, supplements, images, and the included paper. |
| `attachments/juzek-ward-word-overuse-alignment-osf-4nvjk-A1-instruction-tuning.md` | Direct OSF supplementary instruction-tuning analysis | `3ef89d492d0ef42fadf0a1fe8176dd4babff11d5f8fd0e5f70e71e658cb10c75` | Preserved unchanged and reproduced completely above. |
| `attachments/juzek-ward-word-overuse-alignment-osf-4nvjk-instruction.jpg` | Direct OSF supplement visualization | `baf6ea933a9fbb8e33dec30a0189e3935e7c7186c4d3763b9fea4a192da94912` | Preserved unchanged and visually checked against the supplementary table. |
