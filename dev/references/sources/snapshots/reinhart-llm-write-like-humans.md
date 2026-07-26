# Do LLMs write like humans? Variation in grammatical and rhetorical styles

- **Canonical URL:** https://doi.org/10.1073/pnas.2422455122
- **Alternate access URLs:**
  - https://www.pnas.org/doi/10.1073/pnas.2422455122
  - https://pmc.ncbi.nlm.nih.gov/articles/PMC11874169/
  - https://www.ebi.ac.uk/europepmc/webservices/rest/PMC11874169/fullTextXML
  - https://pmc.ncbi.nlm.nih.gov/articles/PMC11874169/pdf/pnas.202422455.pdf
  - https://pmc.ncbi.nlm.nih.gov/articles/instance/11874169/bin/pnas.2422455122.sapp.pdf
  - https://arxiv.org/abs/2410.16107v2 (version comparison only)
- **Author / owner:** Alex Reinhart, Ben Markey, Michael Laudenbach, Kachatad Pantusen, Ronald Yurko, Gordon Weinberg, and David West Brown
- **Publisher:** Proceedings of the National Academy of Sciences of the United States of America (PNAS)
- **Published:** 2025-02-18 online; issue date 2025-02-25
- **Retrieved:** 2026-07-17
- **Stable identifier:** DOI 10.1073/pnas.2422455122; PMCID PMC11874169; no PMID found in the PMC/Europe PMC record or PubMed DOI search
- **Version / revision:** PNAS version of record, volume 122, issue 8, e2422455122; six-page article plus 22-page Supporting Information, compared with arXiv:2410.16107v2
- **Extraction method:** Publisher-version PDFs downloaded from PubMed Central after completing its client-side SHA-256 proof-of-work challenge; Poppler `pdfinfo`, `pdftotext -layout`, and `pdftoppm` used for page counts, complete embedded-text extraction, and rendered-page checks; Europe PMC full-text XML and PMC HTML cross-checked for identity, structure, figures, tables, footnote, references, and supplementary-file identity
- **Full-text status:** complete
- **Access and transformation notes:** The canonical PNAS PDF endpoint returned HTTP 403 to non-browser `curl`, and the PMC PDF endpoints first returned a proof-of-work interstitial. Both complete final PDFs were then retrieved from PMC. The main and supplement have embedded text layers; no OCR was used. Poppler preserves page order and table text but linearizes two-column layout. The snapshot inserts labelled page-break markers. Figure graphics remain authoritative in the preserved PDFs; captions and all text-bearing table cells are included below. A visual check confirms that Supporting Information Table S2 literally prints `5550,463` for the HAP-E academic word count of Llama 3 8B Instruct, although its printed row total and the column sum imply `550,463`; the source typo is preserved rather than silently corrected. The feature inventories also disagree: Table S4 lists 66 rows including punctuation-inclusive type-token ratio but no time adverbials, while Tables S5-S6 each report 66 result rows including time adverbials but no type-token-ratio result; page 12 contains only an empty continuation header.

## Full text

The complete extracted text of the six-page version-of-record article and the complete 22-page Supporting Information follow. Page furniture, captions, tables, footnotes, acknowledgments, data-availability statement, and references are retained. The preserved PDFs are authoritative for layout and figures.

### Version-of-record article

```text
===== version-of-record PDF page 1 =====

                             RESEARCH ARTICLE          COMPUTER SCIENCES




Do LLMs write like humans? Variation in grammatical and
rhetorical styles
Alex Reinharta,1 ID , Ben Markeyb ID , Michael Laudenbachc ID , Kachatad Pantusena,d ID , Ronald Yurkoa ID , Gordon Weinberga , and David West Brownb ID

Edited by Jeffrey Ullman, Stanford University, Stanford, CA; received November 5, 2024; accepted January 7, 2025


Large language models (LLMs) are capable of writing grammatical text that follows
instructions, answers questions, and solves problems. As they have advanced, it has                            Significance
become difficult to distinguish their output from human-written text. While past
research has found some differences in features such as word choice and punctuation                            As large language models (LLMs)
and developed classifiers to detect LLM output, none has studied the rhetorical styles of                      have grown in power and become
LLMs. Using several variants of Llama 3 and GPT-4o, we construct two parallel corpora                          more widely available, research
of human- and LLM-written texts from common prompts. Using Douglas Biber’s                                     has focused on their ability to
set of lexical, grammatical, and rhetorical features, we identify systematic differences                       complete various tasks and the
between LLMs and humans and between different LLMs. These differences persist                                  biases they exhibit when doing so.
when moving from smaller models to larger ones and are larger for instruction-tuned                            In this study, we instead examine
models than base models. This observation of differences demonstrates that despite                             their writing style in detail. We
their advanced abilities, LLMs struggle to match human stylistic variation. Attention
                                                                                                               show that instruction-tuned
to more advanced linguistic features can hence detect patterns in their behavior not
previously recognized.                                                                                         models, which are trained to
                                                                                                               answer questions and solve
corpus linguistics | large language models | writing style                                                     problems, have a distinct
                                                                                                               noun-heavy, informationally
As large language models (LLMs) have advanced in recent years, from “stochastic parrots”                       dense writing style, even when
to models evidently capable of performing complex tasks, most attention has focused on                         prompted to match the style of
their reasoning performance: solving mathematical problems, writing code, evaluating                           informal speech and writing.
arguments, diagnosing diseases, and so on (1–4). While past research has studied their                         These findings suggest that
mastery of basic grammar and vocabulary (5), there is relatively little research on their                      instruction-tuned models
language performance more generally: their ability to produce readable text in a variety                       generate text that does not align
of styles. Rather than exploring it in detail, commentators discuss the business and                           with genre conventions familiar
communication tasks that might be automated by LLMs with their writing ability, or                             to human audiences, and
consider the dangers of impersonation and misinformation facilitated by LLMs (6–9).
                                                                                                               demonstrate the value of
As more and more writing tasks are automated, such problems appear inevitable.
   However, the impression that LLMs write “like humans” is based primarily on                                 linguistic variables in evaluating
qualitative evaluation of their output, not on thorough linguistic evaluation of their                         the output of LLMs.
text. So far, quantitative comparisons have looked mainly at basic grammar and syntax
(5) or features such as word choice, punctuation, sentence length, and so on, finding
evidence of some differences between human- and LLM-written text (10–14). Other
work has used these features, or language models trained on sample texts, to classify                      Author affiliations: a Department of Statistics and
LLM-written texts with varying degrees of success (15–17). Though not definitive, these                    Data Science, Carnegie Mellon University, Pittsburgh,
                                                                                                           PA 15213; b Department of English, Carnegie Mellon
results suggest there are indeed structural differences between human- and LLM-written                     University, Pittsburgh, PA 15213; c Department of
text.                                                                                                      Humanities and Social Sciences, New Jersey Institute
                                                                                                           of Technology, Newark, NJ 07102; and d Heinz College of
   We used several recent LLMs (OpenAI’s GPT-4o and GPT-4o Mini, and four variants                         Information Systems and Public Policy, Carnegie Mellon
of Meta Llama 3) to generate text from prompts drawn from a large, representative corpus                   University, Pittsburgh, PA 15213
of English, allowing us to directly compare the style of LLM writing to human writing.
We find large differences in grammatical, lexical, and stylistic features, demonstrating
that LLMs prefer specific grammatical structures and struggle to match the stylistic                       Author contributions: A.R., B.M., M.L., G.W., and D.W.B.
                                                                                                           designed research; A.R., K.P., R.Y., and D.W.B. performed
variation present in human communication, particularly as that variation aligns with                       research; A.R., K.P., R.Y., and D.W.B. analyzed data; and
the conventions that structure genres such as academic writing, interactive speech, or                     A.R., B.M., M.L., G.W., and D.W.B. wrote the paper.
journalistic news. In Llama 3, where we are able to compare base models (which produce                     The authors declare no competing interest.
text completions) to instruction-tuned variants (which have been further trained to                        This article is a PNAS Direct Submission.
answer questions and complete tasks specified in prompts), we further see that the                         Copyright © 2025 the Author(s). Published by PNAS.
                                                                                                           This article is distributed under Creative Commons
instruction tuning introduces more extreme grammatical differences, making them easier                     Attribution-NonCommercial-NoDerivatives License 4.0
to distinguish from human writing and introducing features similar to those present in                     (CC BY-NC-ND).
GPT-4o and GPT-4o Mini.                                                                                    1 To whom correspondence may be addressed. Email:
                                                                                                           areinhar@stat.cmu.edu.
   For example, the instruction-tuned LLMs used present participial clauses at 2 to 5
                                                                                                           This article contains supporting information online
times the rate of human text, such as in this sentence from GPT-4o using two present                       at https://www.pnas.org/lookup/suppl/doi:10.1073/pnas.
participles: “Bryan, leaning on his agility, dances around the ring, evading Show’s heavy                  2422455122/-/DCSupplemental.
blows.” They also use nominalizations at 1.5 to 2 times the rate of humans, such as                        Published February 18, 2025.




PNAS     2025     Vol. 122     No. 8    e2422455122                                                   https://doi.org/10.1073/pnas.2422455122                     1 of 6

===== version-of-record PDF page 2 =====

   in this sentence from Llama 3 70B Instruct containing four:                           refused to respond to prompts or gave short, unusable answers; after these were
   “These schemes can help to reduce deforestation, habitat destruc-                     removed, there were n = 8,290 HAP-E texts and n = 9,615 CAP texts with
   tion, and pollution, while also promoting sustainable consumption                     outputs from all LLMs. With two human chunks and six LLM-authored chunks for
   patterns.” On the other hand, GPT-4o uses the agentless passive                       each text, HAP-E comprised n = 66,320 chunks and CAP n = 76,920 chunks.
   voice at roughly half the rate as human texts—but in each case,                       See SI Appendix, Tables S2 and S3 for corpus size and composition.
   the Llama base models use these features at rates more closely                            To extract meaningful features from our corpus for training our classifiers,
   matching humans. This suggests that instruction tuning, rather                        we used Douglas Biber’s tagset of 66 linguistic categories (19, 25, 26), which
   than training the models to write even more like humans, instead                      includes indices of lexical complexity and raw linguistic features ranging from
   trains them in a particular informationally dense, noun-heavy                         the lexical to the grammatical (27, 28). For example, features include mean word
   style, and limits their ability to mimic other writing styles leading                 length, the use of nominalizations (nouns formed from adjectives or verbs, such
                                                                                         as development or robustness), agentless passive voice, hedging phrases (such
   to, in some cases, genre misalignment.
                                                                                         as something like or almost), and clausal coordination. All features are listed
      These results demonstrate the value of attending to linguistic
                                                                                         in SI Appendix, Table S4. Differences between LLM and human use of features
   structure (morphosyntactic, functional, and rhetorical) in order
                                                                                         were tested for statistical significance with the paired Wilcoxon signed-rank test
   to better understand the affordances and outputs of large language                    with Bonferroni multiple comparison correction. All analysis code is available
   models. Since the rise of the Internet and the concurrent develop-                    via the Open Science Framework (29).
   ment of efficient processing architectures, language modeling has                         As a further check of generalizability, we used part of the M4 parallel corpus
   relied on relatively simple linguistic principles (i.e., sequences                    (17) consisting of abstracts from the arXiv preprint service alongside abstracts
   and context windows) as the availability of massive amounts                           generated by GPT-3.5 when prompted with the preprint title. These texts are
   of text allowed models trained on text to rapidly outperform                          from a different LLM (GPT-3.5) and a very distinct genre of writing (academic
   older paradigms based on linguistic theory (18); but linguistic                       abstracts), providing a check on the consistency of results in different genres.
   theory and corpus linguistics can provide better ways to evaluate
   LLM output, just as improved benchmark problems can provide
   better ways to evaluate their reasoning ability. These results also                   Results
   demonstrate the limits of current LLMs in matching human
                                                                                         Classifying Text by Source. A random forest classifier using the
   language, showing that despite their apparent ability, they have
   measurable limitations compared to human authors.                                     Biber features to distinguish between the seven text sources in
                                                                                         HAP-E (human chunk 2 and the six LLMs) achieved a test
                                                                                         accuracy of 66%, compared to an expected accuracy of 14%
   Methods                                                                               from random guessing. The confusion matrix, shown in Fig. 2,
                                                                                         demonstrates that little of the error was due to confusion between
   We created two corpora of parallel human- and LLM-written texts. Each corpus          human texts and the LLMs: Instead, most classification errors
   began with n = 12,000 human-authored English texts from a range of genres,            confused Llama 3 8B and 70B, Llama 3 8B Instruct and 70B
   from spoken word (such as podcast transcripts) to news and magazine articles to       Instruct, or GPT-4o and 4o Mini. Each pair consists of models
   formal academic writing. Language use varies in relation to situational factors
                                                                                         of two different sizes trained on similar data, implying that the size
   such as audience and purpose (19, 20); by including multiple genres, we aimed
                                                                                         difference does not produce dramatically different style. Overall,
   to capture a diverse range of language production. As illustrated in Fig. 1,
   from each text we extracted two consecutive chunks of roughly 500 words (split
                                                                                         only 4.2% of LLM texts were falsely classified as human, and
   at sentence boundaries). The first chunk was provided to each LLM to give it          only 9.8% of human texts were falsely classified as LLMs.
   context and a sample of the writing style. The LLMs were prompted to write 500
   more words in the same style, tone, and diction; their generated text was then        Differences in Style and Vocabulary. Fig. 3 illustrates the large
   compared to the next 500-word chunk of the human text. We used six LLMs:              variation in rate of occurrence of the fifteen most important
   GPT-4o and GPT-4o Mini (21, 22) and Meta Llama 3 8B, 70B, 8B Instruct, and            features (as identified by the random forest) in texts generated
   70B Instruct (23), producing six LLM-authored texts for each human-authored           by LLMs, relative to the rate observed in the human text. All
   text. See SI Appendix for detailed prompt information.
       We constructed the first corpus, the Human–AI Parallel English corpus, from
   six categories of text (academic, news, fiction, spoken word, blogs, and TV/movie
   scripts) (30, 31). The second corpus, the COCA AI Parallel (CAP) Corpus, is drawn                        Llama 3 70B
   from the preexisting Corpus of Contemporary American English (COCA), a large,                                                                              Count
                                                                                                             Llama 3 8B
   representative corpus of over 1 billion words in eight registers: spoken, fiction,
                                                                                                  Llama 3 70B Instruct

                                                                                         Prediction
   magazines, newspapers, academic, blogs, web pages, and TV/movie subtitles                                                                                        1500
   (24). The HAP-E corpus was used for our primary analyses, while CAP was used to                    Llama 3 8B Instruct
                                                                                                                                                                    1000
   evaluate the generalizability of the results to different texts. The LLMs sometimes                          GPT−4o
                                                                                                                                                                    500
                                                                                                            GPT−4o Mini

                                                                                                                Chunk 2

                                                                                                                                  i 4o    t   t
                                                                                                                          k 2 in        uc uc 3 8B 70B
                                                                                                                        un o M T− str str         3
                                                                                                                      Ch T−4 GP B In B In lama ma
                                                                                                                                   8 70     L Lla
                                                                                                                       GP        3  3
                                                                                                                              ma a
                                                                                                                           Lla Llam
                                                                                                                                  True source

                                                                                         Fig. 2. Confusion matrix for a random forest classifying HAP-E texts by their
                                                                                         linguistic and rhetorical features, evaluated on the test set (25% of the HAP-
   Fig. 1. The LLM text generation workflow. Each human text was split into              E corpus, including n = 14,535 human and LLM texts). The block diagonal
   two chunks of roughly 500 words; the first chunk was used to prompt an LLM            structure indicates that most classification errors were between different
   to create text that was compared to the second human chunk.                           versions of the same LLM, rather than between humans and LLMs.




2 of 6   https://doi.org/10.1073/pnas.2422455122                                                                                                                pnas.org

===== version-of-record PDF page 3 =====

                                                                         GPT-4o           Llama 3 70B Instruct                Llama 3 70B
                                   Present participial clauses
                                    ‘That’ clauses as subject
                                            Mean word length
                                                       Adverbs
                                              Nominalizations
                                        Phrasal co-ordination
                                        Clausal co-ordination
                                                   Other nouns
                                                   Downtoners
                                        Attributive adjectives
                                              Demonstratives
                                          Agentless passives
                                  Past participial postnominal
                                                      Inﬁnitives


                      Biber feature
                                       Prepositional phrases

                                                                       GPT-4o Mini        Llama 3 8B Instruct                  Llama 3 8B
                                   Present participial clauses
                                    ‘That’ clauses as subject
                                            Mean word length
                                                       Adverbs
                                              Nominalizations
                                        Phrasal co-ordination
                                        Clausal co-ordination
                                                   Other nouns
                                                   Downtoners
                                        Attributive adjectives
                                              Demonstratives
                                          Agentless passives
                                  Past participial postnominal
                                                      Inﬁnitives
                                       Prepositional phrases
                                                                   ½    1    2    3     ½        1      2    3         ½        1      2    3
                                                                                         Rate (1 = human)
Fig. 3. Rate of Biber feature use by different LLMs, relative to the human usage of each feature, for the top 15 most important features in the HAP-E corpus.
Note the log scale. GPT-4o and GPT-4o Mini show the largest variation from human texts, while the base variants of Llama 3 most closely resemble human
grammar and style. Larger models (Top row) generally show the same stylistic differences as their smaller counterparts (Bottom row), despite performing
better on other benchmark tasks. Triangles indicate statistically significant differences from human usage. SI Appendix, Fig. S1 gives the distribution of paired
differences.



four instruction-tuned models have strong preferences for present                     tuned Llama and GPT-4o models certain words are used at
participial clauses, “that” clauses as subjects, nominalization,                      dramatically higher and lower rates. Table 1 highlights words
and phrasal coordination, which are typical markers of more                           overrepresented in LLM outputs: GPT-4o and 4o Mini use words
informationally dense, noun-heavy style of writing (32). For                          like camaraderie, palpable, tapestry, and intricate at more than
example, GPT-4o uses present participial clauses at 5.3 times                         100 times the rate of humans, such as in the GPT-4o output
the rate of humans (paired Cohen’s d = 1.38), “that” clauses                          phrase “The camaraderie was palpable.” As a result, “tapestry”
as subject 2.6 times as often (d = 0.77), nominalizations 2.1                         appeared in 23% of GPT-4o outputs and “amidst” in 27%
times as often (d = 1.23), and phrasal coordination 1.9 times as                      (SI Appendix, Table S7). Instruction-tuned variants of Llama
often (d = 0.81). (Rates and effect sizes for all 66 features are                     3 also favor words like camaraderie and palpable, as well as
provided in SI Appendix, Tables S5 and S6 and Fig. S1 illustrates                     unease and reminder, though at lower rates than GPT-4o and
paired differences.) There are also signs of local patterns that                      in a much smaller fraction of documents.* Conversely, they use
emerge with specific models: Both GPT-4o models avoid clausal                         certain obscenities more than 100 times less often (SI Appendix,
coordination, while all Llama 3 variants use it more frequently                       Table S8).
than humans; while both GPT-4o models use downtoners (such                               While many words listed in Table 1 may be occasionally
as barely or nearly) more frequently than humans, all Llama 3                         expected in belletristic works of fiction, their pervasiveness across
variants avoid them.                                                                  LLM output in a diverse array of genres is notable. To those
   One might expect larger models to better match human text                          familiar with academic writing, newspapers, or television scripts,
than smaller models (e.g., Llama 70B versus Llama 8B, or GPT-                         these words are largely unexpected, and to experts likely signal an
4o versus GPT-4o Mini), but this does not appear to be the                            overwritten, sentimental, or simply uneven text. The point here is
case in Fig. 3. Also, instruction tuning appears to make the                          not that humans refrain from using these words but that humans
model output less human, not more: The Llama 3 base models                            refrain from using these words in certain genres. In this case,
use features at rates similar to human texts, while GPT-4o and                        words that are unremarkable in fiction are highly conspicuous
Llama 3 instruction-tuned models have much wider variation                            and unconventional when used other genres. As word choice
from feature to feature.                                                              appears most similar to humans for the base models, this suggests
   Similar to past research (14), we find that LLMs also favor
specific vocabulary. Fig. 4 shows the rate of usage for words                         * Some overuse may be artifacts of the generation process; for example, Llama 3
used more than once per million words by humans, comparing                            instruction-tuned variants overuse continuation because their outputs sometimes begin
                                                                                      with “Here is the continuation of the text...” Llama base models have a tendency to repeat
the usage of each LLM to the usage by humans in Chunk 2 of                            themselves, so Llama 3 8B uses Deborah at 52 times the rate of humans largely because
HAP-E. Compared to the base Llama models, in the instruction-                         of a single document repeating it 308 times.




PNAS     2025     Vol. 122            No. 8    e2422455122                                                       https://doi.org/10.1073/pnas.2422455122                      3 of 6

===== version-of-record PDF page 4 =====

   Fig. 4. Rates of word use by different LLMs (per 1,000 words) compared to the human use of each word in chunk 2, in the HAP-E corpus (log scale). Includes
   all words used more than once per million words in chunk 2. Words are lemmatized to group together inflected forms. Words on the diagonal are used equally
   often in human and LLM texts. Dashed blue lines indicate the range between 10× more and 10× less than human use. Note that the instruction-tuned models
   show more variation from the diagonal, indicating more deviation in vocabulary use relative to humans.



   the word choice bias is introduced by the instruction tuning                   even when trained on HAP-E and tested on CAP or vice versa
   process, not simply by bias in the texts composing the training                (SI Appendix, Table S9). Lasso-penalized logistic regression
   sets.                                                                          classifiers attained similar performance for all LLMs except for
      In the GPT-4o models in particular, many of these words                     the Llama base models, which had accuracies around 75%
   connote some form of complex relation among objects (e.g.,                     (SI Appendix, Table S10). Since the lasso regressions only consider
   tapestry, intricate, camaraderie, cacophony, and amidst). Coupled              additive terms, this implies that interactions between the Biber
   with positive items such as vibrant and solace, these words                    features contain relevant signals for the Llama base models.
   together may signal a preference for grandiose, if hollow,                        For both methods, the lower classification accuracy for the
   summative sentences.                                                           Llama base models relative to the GPT-4o and instruction-
                                                                                  tuned Llama models indicates that instruction tuning may lead
                                                                                  to writing that is easier to distinguish from human writing.
   Distinguishing Individual LLMs. When      classifying between
   human-generated text and one specific LLM, rather than com-
   paring all LLMs, our classifiers achieve much higher accuracy.                 Generalization Across Corpora. When each pairwise random
   Typical accuracies achieved by random forests were 93 to 98%                   forest was used to classify arXiv preprints from the M4 corpus,


   Table 1.     Most overrepresented words in LLM-generated texts, relative to human usage rates
                                    GPT-4o                  Llama 3 70B                  Llama 3 8B                  Llama 3                   Llama
          GPT-4o                     Mini                      Instruct                    Instruct                    70B                      3 8B
   Word            Rate     Word               Rate    Word               Rate     Word               Rate     Word            Rate     Word            Rate
   camaraderie 162          camaraderie        171     unease             63       unease             101      bananas         31       deborah         52
   tapestry    155          tapestry           147     palpable           47       continuation        52      paperback       30       rambo           22
   intricate   119          palpable           145     continuation       29       palpable            48      bam             26       matty           20
   underscore 107           grapple            131     shoutout           28       reminder            33      verona          25       goodnight       18
   unspoken    102          intricate          129     intricate          27       pang                29      filth           19       ml              15
   amidst      100          fleeting           124     pang               25       rut                 29      rekall          17       merlin          13
   palpable     95          ignite             122     camaraderie        24       waft                28      denis           14       worcester       11
   solace       95          vibrant             92     policymaker        24       prioritize          27      darry           12       fay             10
   fleeting     84          amidst              90     prioritize         24       grapple             24      ebook           12       missy           10
   unravel      83          cacophony           89     reminder           24       camaraderie         23      janice          12       elisa           10



4 of 6   https://doi.org/10.1073/pnas.2422455122                                                                                                   pnas.org

===== version-of-record PDF page 5 =====

accuracy dropped significantly. Random forests trained on                                                     machine-generated text, zeroing in on specific teachable moments
instruction-tuned LLMs were able to classify M4’s GPT-3.5                                                     in the revision of machine-generated text.
output with greater-than-chance accuracy, but models trained on                                                  As LLMs are increasingly put to work completing diverse
the Llama base outputs attained only 50% accuracy, equal to ran-                                              writing tasks, these results suggest a notable misalignment
dom guessing (SI Appendix, Tables S11 and S12). These results                                                 between generated texts and the contexts in which we put them
demonstrate that instruction-tuned LLMs do have features in                                                   to use. This is another way of saying that LLMs do not vary
common that permit their classification but that generalizability                                             their linguistic output in response to contextual factors in ways
across LLMs or to different registers of text is difficult.                                                   similar to humans. This misalignment affects experts and learners
                                                                                                              differently. For those proficient in a genre—think, a therapist
Discussion                                                                                                    collating notes on a patient or, say, a college graduate writing
                                                                                                              thank-you notes to friends and family—this misalignment is
This study identifies salient differences both between human                                                  likely flagged and the output is appropriately revised. When the
and LLM-generated texts and among various models. The                                                         writer is proficient in the genre, previous experience guides a
features that distinguish between humans and different LLMs                                                   current sense of what a particular document should look like
include present participial clauses, “that” clauses as sentence                                               in order to be successful. For experts, then, LLMs appear a
subject, passive voice, and nominalizations, to name a few.                                                   worthwhile productivity tool, suitable so long as they lend their
These findings corroborate other research that points out the                                                 expertise to further shaping the output.
ways these features produce informationally dense prose (33).                                                    For learners, though, LLMs appear more problematic. Of
Other research links these features to increased lexical diversity in                                         course, using LLMs to learn more about a concept, or help
generated text, as well as human judgments of linguistic mastery                                              generate ideas, is one thing. Using output in a text is a different
(13). Last, prior work found that ChatGPT-4 text evidences                                                    matter, one that may affect a student’s learning trajectories. In this
more nominalizations, and fewer human subjects and epistemic                                                  case, students offload the important cognitive labor of shaping
stance markers (34), findings we see reproduced in our list of                                                a text for a particular audience and purpose to the LLM. Never
distinguishing features.                                                                                      mind that LLMs do not appear to write like humans—when
   A second major finding of this research is the apparently central                                          students offload writing work, they offload opportunities to learn
role of instruction tuning in creating these discrepancies between                                            how to write IMRaD articles, client reports, executive summaries,
human and model general texts. While we do not have access                                                    investment pitches, etc. When LLMs are used in the classroom
to untuned versions of GPT, comparisons between Llama’s base                                                  as writing tools, instructors of all levels and disciplines need to
and tuned models emphasize the degree to which instruction                                                    help students see both the shortcomings of the generated text and
tuning pushes models to produce text that reads unlike a human.                                               avenues for improvement. LLMs are not bad, either technically
This suggests that differences in style are not simply due to the                                             or morally—it is only that instructors must help inculcate in
selection of texts for training the base models, but due to the                                               students the critical perspective of the expert to know what is
instruction-tuning process. Similarly, differences between GPT-                                               working and what is not.
4o and the instruction-tuned Llama variants may be due to                                                        In other contexts, however, overreliance on LLMs could
differences in instruction tuning, either through different human                                             produce output that might be awkward and inauthentic (e.g.,
preferences in rating responses or differences in the tasks (such                                             in a creative genre), confusing (e.g., in instructional material),
as summarization) used to tune the models. (As the instruction                                                or unpersuasive (e.g., in argumentative texts). The current work
tuning processes are not publicly documented, it is not possible                                              thus suggests the importance of LLM practice—both in and out
to determine the cause more precisely.) While instruction tuning                                              of the classroom—informed by human expertise via a continual
has previously been shown to introduce cognitive biases (35), to                                              dialog of creation and revision, where LLM users are more aware
our knowledge, these changes in writing style are not discussed                                               and mindful of the effective uses as well as the limitations of
elsewhere in similar research.                                                                                various LLMs.
   A third major finding of this work is significant success of
Biber’s tagset in modeling and classifying text. This success                                                 Data, Materials, and Software Availability. Textcorpora,computedfeatures,
suggests that varied linguistic perspectives—which, perhaps, are                                              and code to reproduce figures and results have been deposited in Hugging Face
not prioritized during the development and in-house assess-                                                   and Open Science Framework (OSF): Human–AI Parallel English Corpus, DOI:
ments of LLMs—can reveal otherwise tacit information that                                                     10.57967/hf/3770 (30); Human–AI Parallel English Corpus, extracted Biber
distinguishes a text as machine-generated. With the linguistic                                                features, DOI: 10.57967/hf/3792 (27); Human–AI Parallel English Corpus,
perspective offered by pseudobibeR, we built a model that                                                     dependency parse, DOI: 10.57967/hf/3793 (31); COCA-AI Parallel Corpus,
recognizes machine-generated text with relative ease. Our study                                               extracted Biber features, DOI: 10.57967/hf/3794 (28); and Analysis code, DOI:
reveals the clear value of linguistics expertise and functional                                               10.17605/OSF.IO/7MRQN (29).
conceptions of language in both LLM use and development.
   That said, our intention is not to propose another way to                                                  ACKNOWLEDGMENTS. We thank members of the TeachStat Research Group
construct LLM detectors or to police the writing of students                                                  for helpful discussions, the Dietrich College of Humanities and Social Sciences
and learners. Instead, we maintain that this type of comparative                                              at Carnegie Mellon University for use of the Wright Graphics Processing Unit
analysis is useful for identifying differences between human- and                                             (GPU) cluster, and Aadi Menon for exploring suitable prompts.


1.   B. Wang, X. Yue, H. Sun, “Can ChatGPT defend its belief in truth? Evaluating LLM reasoning via           4.   S. A. Lehr, A. Caliskan, S. Liyanage, M. R. Banaji, ChatGPT as research scientist: Probing GPT’s
     debate” in Findings of the Association for Computational Linguistics: EMNLP 2023, H. Bouamor,J.               capabilities as a research librarian, research ethicist, data generator, and data predictor. Proc. Natl.
     Pino, K. Bali, Eds. (Association for Computational Linguistics, Singapore, 2023), pp. 11865–11881.            Acad. Sci. U.S.A. 121, e2404328121 (2024).
2.   J. Huang, K. C. C. Chang, “Towards reasoning in large language models: A survey” in Findings of          5.   T. A. Chang, B. K. Bergen, Language model behavior: A comprehensive survey. Comput. Linguist.
     the Association for Computational Linguistics: ACL 2023, A. Rogers, J. Boyd-Graber, N. Okazaki, Eds.          50, 293–350 (2024).
     (Association for Computational Linguistics, Toronto, Canada, 2023), pp. 1049–1065.                       6.   D. Barman, Z. Guo, O. Conlan, The dark side of language models: Exploring the potential of LLMs
3.   Y. Chen, T. X. Liu, Y. Shan, S. Zhong, The emergence of economic rationality of GPT. Proc. Natl. Acad.        in multimedia disinformation generation and dissemination. Mach. Learn. Appl. 16, 100545
     Sci. U.S.A. 120, e2316205120 (2023).                                                                          (2024).




PNAS        2025         Vol. 122          No. 8        e2422455122                                                                            https://doi.org/10.1073/pnas.2422455122                                        5 of 6

===== version-of-record PDF page 6 =====

    7.  S. Kumar, V. Balachandran, L. Njoo, A. Anastasopoulos, Y. Tsvetkov, “Language generation              18. X. Li, “There’s no data like more data”: Automatic speech recognition and the making of algorithmic
        models can cause harm: So what can we do about it? An actionable survey” in Proceedings of the            culture. Osiris 38, 165–182 (2023).
        17th Conference of the European Chapter of the Association for Computer Linguistic, A. Vlachos, I.    19. D. Biber, Variation Across Speech and Writing (Cambridge University Press, 1988).
        Augenstein, Eds. (Association for Computer Linguistic, Dubrovnik, Croatia, 2023), pp. 3299–3321.      20. C. Miller, Genre as social action. Q. J. Speech 70, 151–167 (1984).
    8. B. Kovács, The Turing test of online reviews: Can we tell the difference between human-written and     21. OpenAI, Hello GPT-4o (2024). https://openai.com/index/hello-gpt-4o/. Accessed 16 October 2024.
        GPT-4-written online reviews? Mark. Lett. 35, 651–666 (2024).                                         22. OpenAI, GPT-4o mini: advancing cost-efficient intelligence (2024). https://openai.com/index/gpt-
    9. T. Hagendorff, Deception abilities emerged in large language models. Proc. Natl. Acad. Sci. U.S.A.         4o-mini-advancing-cost-efficient-intelligence/. Accessed 16 October 2024.
        121, e2317967121 (2024).                                                                              23. Meta, Introducing Meta Llama 3: The most capable openly available LLM to date (2024). https://ai.
    10. R. Tang, Y. N. Chuang, X. Hu, The science of detecting LLM-generated text. Commun. ACM 67,                meta.com/blog/meta-llama-3/. Accessed 16 October 2024.
        50–59 (2024).                                                                                         24. M. Davies, The Corpus of Contemporary American English (COCA). https://www.english-corpora.
    11. L. Fröhling, A. Zubiaga, Feature-based detection of automated language models: Tackling GPT-2,            org/coca/. Accessed 16 October 2024.
        GPT-3 and Grover. PeerJ Comput. Sci. 7, e443 (2021).                                                  25. D. Biber, Dimensions of Register Variation: A Cross-Linguistic Comparison (Cambridge University
    12. A. Muñoz-Ortiz, C. Gómez-Rodríguez, D. Vilares, Contrasting linguistic patterns in human and              Press, 1995).
        LLM-generated news text. Artif. Intell. Rev. 57, 265 (2024).                                          26. D. Biber, S. Conrad, Register, Genre, and Style (Cambridge University Press, 2009).
    13. S. Herbold, A. Hautli-Janisz, U. Heuer, Z. Kikteva, A. Trautsch, A large-scale comparison of human-   27. D. Brown et al., Human-AI parallel corpus, extracted Biber features. Hugging Face. https://doi.org/
        written versus ChatGPT-generated essays. Sci. Rep. 13, 18617 (2023).                                      10.57967/hf/3792. Deposited 3 October 2024.
    14. W. Liang et al., “Monitoring AI-modified content at scale: A case study on the impact of ChatGPT      28. D. Brown et al., COCA-AI parallel corpus, extracted Biber features. Hugging Face. https://doi.org/10.
        on AI conference peer reviews” in Proceedings of the 41st International Conference on Machine             57967/hf/3794. Deposited 30 September 2024.
        Learning, Proceedings of Machine Learning Research, R. Salakhutdinov et al., Eds. (PMLR, 2024),       29. A. Reinhart et al., Do LLMs write like humans? Variation in grammatical and rhetorical styles. Open
        vol. 235, pp. 29575–29620.                                                                                Science Framework. https://doi.org/10.17605/OSF.IO/7MRQN. Deposited 12 December 2024.
    15. J. Q. J. Liu et al., The great detectives: Humans versus AI detectors in catching large language      30. D. Brown et al., Human-AI parallel corpus. Hugging Face. https://doi.org/10.57967/hf/3770.
        model-generated medical writing. Int. J. Educ. Integr. 20, 8 (2024).                                      Deposited 3 October 2024.
    16. E. Mosca, M. H. I. Abdalla, P. Basso, M. Musumeci, G. Groh, “Distinguishing fact from fiction:        31. D. Brown et al., Human-AI parallel corpus, dependency parse. Hugging Face. https://doi.org/10.
        A benchmark dataset for identifying machine-generated scientific papers in the LLM era”                   57967/hf/3793. Deposited 3 October 2024.
        in Proceedings of the 3rd Workshop on Trustworthy Natural Language Processing (TrustNLP               32. L. L. Aull, How Students Write: A Linguistic Analysis (MLA, 2020).
        2023), A. Ovalle et al., Eds. (Association Computer Linguistic, Toronto, Canada, 2023),               33. B. Markey, D. W. Brown, M. Laudenbach, A. Kohler, Dense and disconnected: Analyzing the
        pp. 190–207.                                                                                              sedimented style of ChatGPT-generated text at scale. Writ. Commun. 41, 571–600 (2024).
    17. Y. Wang et al., “M4: Multi-generator, multi-domain, and multi-lingual black-box                       34. F. K. Jiang, K. Hyland, Does ChatGPT argue like students? Bundles in argumentative essays.
        machine-generated text detection” in Proceedings of the 18th Conference of the Eu-                        Appl. Linguist. amae052 (2024).
        ropean Chapter of the Association for Computer Linguistic (Volume 1: Long Papers), Y.                 35. I. Itzhak, G. Stanovsky, N. Rosenfeld, Y. Belinkov, Instructed to bias: Instruction-tuned language
        Graham, M. Purver, Eds. (Association for Computer Linguistic, St. Julian’s, Malta, 2024),                 models exhibit emergent cognitive bias. Trans. Assoc. Comput. Linguist. 12, 771–785
        pp. 1369–1407.                                                                                            (2024).




6 of 6     https://doi.org/10.1073/pnas.2422455122                                                                                                                                                       pnas.org
```

### Supporting Information

```text
===== Supporting Information PDF page 1 =====

1




2    Supporting Information for
3    Do LLMs write like humans? Variation in grammatical and
4    rhetorical styles
5    A. Reinhart, B. Markey, M. Laudenbach, K. Pantusen, R. Yurko, G. Weinberg, and D. W. Brown

6    Alex Reinhart.
7    E-mail: areinhar@stat.cmu.edu



8    This PDF file includes:
9        Supporting text
10       Fig. S1
11       Tables S1 to S12
12       SI References




     A. Reinhart, B. Markey, M. Laudenbach, K. Pantusen, R. Yurko, G. Weinberg, and D. W. Brown   1 of 22

===== Supporting Information PDF page 2 =====

13    Supporting Information Text
14    Construction of Corpora. For this study, we created two parallel corpora. The construction of each corpus was
15    accomplished by:

16         1. assembling 12,000 human-authored texts in English representing a range of registers (or types);

17         2. selecting roughly the first 1,000 words of each text (where that span does not cross a section or chapter
18            boundary);

19         3. splitting each string into approximately 500-word chunks (with the split-point being a sentence boundary as
20            determined by a spaCy dependency parse);

21         4. passing the first chunk to six different LLMs and prompting the models to generate 500 more words of text in
22            the same style, similar to the method used by (1);

23         5. discarding all texts that contain a non-response or a nonsense response (like a string of punctuation) from any
24            of the six LLMs.

25    The resulting corpora, then, contain the first chunk of human-authored text (the “germinal” text used for the LLM
26    prompt) and seven variations of the second chunk: the original (human-authored) continuation of the first chunk, and
27    continuations generated by six different LLMs. This workflow is illustrated in Figure TODO of the main text. The
28    figure also highlights the alignment of the second, parallel chunks, which enable comparisons between the writing of
29    humans and LLMs, as well as comparisons among the writing produced by the LLMs, themselves.
30       The first of our parallel corpora uses the Corpus of Contemporary American English (COCA) as the source
31    of its human-authored text and is called the COCA AI Parallel (CAP) corpus. As noted above, we wanted data
32    representative of a broad range of sources and registers. COCA is a monitor corpus with over 1 billion words and
33    balanced among eight registers: spoken, fiction, magazines, newspapers, academic journals, blogs, other web pages,
34    and TV/movie subtitles (2). For our dataset, we filtered for texts containing a minimum of approximately 1,250
35    words, then randomly sampled 1,500 documents from each register to create a corpus of 12,000 texts.
36       Though its breadth and representativeness make COCA valuable for this task, it does have a key limitation: to
37    allow distribution of otherwise copyrighted material, COCA alters the text by removing 10 words every 200 words.∗
38    This produces gaps and incomplete sentences in each 500-word chunk that might affect sentence parsing and feature
39    extraction. For this reason, we constructed a second corpus, which is meant to approximate COCA’s composition.
40       The resulting dataset, the Human AI Parallel English (HAP-E) corpus, is drawn from six (as opposed to COCA’s
41    eight) text-types:†

42         • Academic: samples were drawn from a 40,000+ document corpus of open-access academic articles published
43           by Elsevier.

44         • News: samples were drawn from a 100,000+ document corpus of news articles published online by U.S.-based
45           news organizations.

46         • Fiction: samples were drawn from novels and short stories in the public domain and available on Project
47           Gutenberg.

48         • Spoken: samples were drawn from a corpus of 100,000 podcast transcriptions. (Note that COCA’s spoken
49           text-type comes from transcriptions of unscripted news shows.)

50         • Blogs: samples were drawn from a corpus of 681,288 posts from blogger.com.

51         • Television and Movie Scripts: samples were drawn from two different corpora of scripts, some of which
52           were converted using OCR.

53    The sampling and processing of the HAP-E corpus followed the same five steps described at the beginning of this
54    section. The word counts of the HAP-E and CAP corpora can be found in the Appendix, Tables S2 and S3.
     ∗ See https://www.corpusdata.org/limitations.asp for details on the procedure.
     † The data can be accessed from https://huggingface.co/datasets/browndw/human-ai-parallel-corpus.



      2 of 22                           A. Reinhart, B. Markey, M. Laudenbach, K. Pantusen, R. Yurko, G. Weinberg, and D. W. Brown

===== Supporting Information PDF page 3 =====

55     LLM text generation. We used multiple versions of GPT-4o (3, 4) and Meta Llama 3 (5) to generate the parallel LLM
56     texts, shown in Table S1. We chose these LLMs because they are popular, available within a reasonable budget,
57     and generally considered to perform very well. Meta Llama 3 is available in both base models, which provide text
58     completion, and instruction-tuned variants that use additional human feedback to optimize the models to follow
59     instructions and answer questions; recent GPT variants are only available in instruction-tuned form. Llama 3’s
60     availability in both forms allows us to observe the effects of instruction tuning.
61        Instruction-tuned LLMs were given the following prompt, followed by the first chunk of human text:

62              In the same style, tone, and diction of the following text, complete the next 500 words, generate exactly
63              500 words, and note that the text does not necessarily end after the generated words:

64     Base Llama 3 variants without instruction tuning were simply given the first chunk of text. In each case, the LLMs
65     generated roughly 500 words of additional output, continuing where the first chunk finished. This could be compared
66     directly to the second chunk of human text. GPT-4o text was generated using OpenAI’s Batch API using its default
67     settings; Llama 3 text was generated on a local GPU cluster using the vLLM package for Python, version 0.5.5 (6).
68        As some LLMs refused to complete some prompts, or returned short, unusable answers, we removed responses
69     shorter than 100 words, producing 8,290 HAP-E texts and 9,615 COCA texts with valid responses from all LLMs.
70     Word counts in HAP-E and CAP by text-type are shown in Tables S2 and S3.
71        We designed this procedure for creating parallel data because our aims are focused more on description than they
72     are on detection. Compared to other methods that only prompt LLMs with a title or topic (e.g. 7), this approach
73     gives the LLMs roughly 500 words of context so they can adapt their output and its style to the human text.

74     Feature extraction. To extract meaningful features from our corpus for training our classifiers, we used Douglas
75     Biber’s tagset of 66 linguistic categories, gleaned from the many works Biber has authored and co-authored (8–10).
76     Biber’s tagset includes indices of lexical complexity (e.g., mean word length), but many more are raw linguistic
77     features ranging from the lexical (e.g., thinking verbs) to the grammatical (e.g., adjectives before a noun). For
78     example, features include:

79         • Nominalizations (nouns formed by adding suffixes to verbs or adjectives, such as “justification”, “development”,
80           “robustness”)

81         • Agentless passive voice (such as “The model was fitted”)

82         • Hedging phrases (such as “at about”, “something like”, “almost”)

83         • Phrasal coordination (such as using “and” to coordinate between noun phrases)

84         • Clausal coordination (such as using “and” at the beginning of clauses).

85     A full list of features is provided in Table S4. Combined, these variables give a stylistic sense of how these texts read.
86     These stylistic profiles, in turn, can enrich our understandings of the affordances and limitations of LLMs as they are
87     currently developed and trained.
88        To tag the texts, we used the pseudobibeR package for R, which counts Biber features present in dependency-parsed
89     texts.‡ pseudobibeR has proven effective at reproducing results similar to those of other studies that use Biber’s
90     tagset (11, 12). Once tagged, we counted the rate of occurrence of each feature per 1,000 words of text. These rates
91     served as the features for our analysis.
92        Corpus linguists studying language use and variation have regularly turned to counts of morphosyntactic and lexical
93     features as the basis for their quantitative analysis, an approach which dominates the field (8, 13–15). Biber’s tagset
94     offers a compelling approach to studies of linguistic variation: because linguistic features both routinely co-occur
95     and are sensitive to context (11), analysis of feature groupings that vary across sources lends insight into the salient
96     distinctions between the stylistic profiles of human and LLM texts. We chose this tagset to represent this perspective,
97     but also because it has been validated by a considerable amount of scholarship (16, 17). Of course, other foundational
98     corpus-based studies have used different feature sets or “bag-of-words” methods, generating word frequency lists to
99     investigate keywords, or for instance, markers of stance in academic writing (18, 19), Instead, Biber’s morphosyntactic
100    tagset presents a more robust method for analyzing register and genre, capturing a wide range of linguistic functions.
      ‡ Available on the Comprehensive R Archive Network (CRAN) and at https://github.com/browndw/pseudobibeR



       A. Reinhart, B. Markey, M. Laudenbach, K. Pantusen, R. Yurko, G. Weinberg, and D. W. Brown                        3 of 22

===== Supporting Information PDF page 4 =====

101   Statistical analysis. To compare the rate of feature use between human and LLM texts, we compared each LLM’s
102   rate of use with the human chunk 2 usage. Table S5 shows the usage (per 1,000 tokens) of each feature in human
103   text, and the LLM usage scaled relative to the human usage of each feature. To scale these differences relative to
104   the typical variation in usage across texts, we calculated the difference between the LLM and human rates for each
105   individual text, then calculated the Cohen’s d effect size by dividing the mean difference by the standard deviation of
106   the differences. These effect sizes are shown in Table S6. Typically, d ≤ 0.5 is considered a small effect, 0.5 < d ≤ 0.8
107   is considered medium, 0.8 < d ≤ 1.3 is large, and d > 1.3 is very large (20). Differences were tested for significance
108   using the paired Wilcoxon signed-rank test.

109   Classification. To evaluate whether the features described above are sufficient to distinguish between human- and
110   LLM-written text, we randomly split the HAP-E documents into a training set (75%) and a test set (25%), stratifying
111   by document category.
112      First, we fit a random forest to classify the source of each of the texts using the Biber features. This is a seven-class
113   classification task (human and six LLMs). This random forest identified the features most important for distinguishing
114   between sources; these top features are used for visualizations of feature variations by source. This was fit using the
115   ranger package (21) with its default settings.
116      Next, we trained a random forest for each pairwise human vs. LLM training task: human vs. GPT-4o, human
117   vs. Llama 3 8B, and so on. For comparison, we also fit lasso-penalized logistic regression models using the same set
118   of Biber features. We used the performance of the lasso models to benchmark and provide context to the random
119   forest models. Since we only account for linear additive contributions of the Biber features in the lasso models,
120   any noticeable improvements in performance of the random forests are due to the flexibility of tree-based models
121   in capturing the presence of non-linear interactions. All lasso logistic regression models were fit using the glmnet
122   package with the one-standard-error regularization penalty selected with 10-fold cross-validation (22). Accuracies of
123   the random forest and lasso models on the test set are shown in Tables S9 and S10.
124      Finally, we used these models to classify text from the M4 parallel corpus (7). We focus on its arXiv GPT-3.5
125   dataset, which includes both real abstracts of preprints posted on arXiv and text generated by GPT-3.5 when
126   prompted to write an abstract based on the preprint’s title. This provides an external test set, generated on a different
127   task with a different model, to evaluate the generalizability of our classifiers. The accuracies on this test set are
128   shown in Tables S11 and S12.
129      Detection has been a particular emphasis since the release of ChatGPT and similar LLMs for understandable
130   reasons (23, 24). While our work involves similar classification tasks, we use classification not as an end in and of
131   itself, but rather as method for helping us understand how LLMs write: how the text that they produce compares to
132   the writing humans produce and how the text produced by one LLM compares to that produced by another.




      4 of 22             A. Reinhart, B. Markey, M. Laudenbach, K. Pantusen, R. Yurko, G. Weinberg, and D. W. Brown

===== Supporting Information PDF page 5 =====

                                    Model         Version        Context   Instruct?
                                    GPT-4o Mini   2024-07-18       128K    Yes
                                    GPT-4o        2024-08-06       128K    Yes
                                    Llama 3       8B                 8K    No
                                    Llama 3       8B-Instruct        8K    Yes
                                    Llama 3       70B                8K    No
                                    Llama 3       70B-Instruct       8K    Yes


                        Table S1. Large language models used to generate text completions.




A. Reinhart, B. Markey, M. Laudenbach, K. Pantusen, R. Yurko, G. Weinberg, and D. W. Brown   5 of 22

===== Supporting Information PDF page 6 =====

                                     Table S2. Word counts in the HAP-E corpus, by source

                                        acad         blog          fic         news         spok          tvm
          Author                                                                                                        Total
                                     (n = 1227)   (n = 1526)   (n = 1395)   (n = 1322)   (n = 1721)   (n = 1099)

          Human

              Chunk 1                  602,878      748,901      674,437      644,896      833,699      598,157     4,102,968
              Chunk 2                  602,683      749,052      675,595      646,030      832,797      591,704     4,097,861

          ChatGPT

              GPT-4o                   633,884      826,590      759,461      708,375      969,210      606,059     4,503,579
              GPT-4o Mini              690,828      916,433      837,527      771,324    1,036,125      678,429     4,930,666

          Llama Base

              Llama 3 70B              510,942      731,889      651,557      572,423    1,098,698      502,012     4,067,521
              Llama 3 8B               544,845      735,068      740,610      510,671    1,083,953      525,037     4,140,184

          Llama Instruction-Tuned

              Llama 3 70B Instruct     580,579      735,501      641,982      627,299      934,911      453,559     3,973,831
              Llama 3 8B Instruct     5550,463      679,884      599,000      568,703      836,531      448,874     3,683,455

          Total                      4,717,102    6,123,318    5,580,169    5,049,721    7,625,924    4,403,831    33,500,065




6 of 22              A. Reinhart, B. Markey, M. Laudenbach, K. Pantusen, R. Yurko, G. Weinberg, and D. W. Brown

===== Supporting Information PDF page 7 =====

                                         Table S3. Word counts in the CAP corpus, by source

                               acad         blog          fic         mag          news         spok          tvm         web
 Author                                                                                                                                  Total
                            (n = 1221)   (n = 1071)   (n = 1372)   (n = 1293)   (n = 1188)   (n = 1334)   (n = 1006)   (n = 1130)

 Human

     Chunk 1                  594,011      521,050      669,470      629,726      579,755      651,956      497,733      549,341     4,693,042
     Chunk 2                  593,875      521,493      671,400      630,126      580,208      651,013      497,900      549,736     4,695,751

 ChatGPT

     GPT-4o                   646,061      578,298      754,715      696,988      640,690      734,320      562,464      609,670     5,223,206
     GPT-4o Mini              710,560      631,028      830,929      759,785      697,919      793,067      608,491      664,693     5,696,472

 Llama Base

     Llama 3 70B              634,881      517,613      739,502      681,171      583,279      747,996      464,058      570,922     4,939,422
     Llama 3 8B               625,065      527,628      729,348      686,137      553,703      736,093      462,948      550,569     4,871,491

 Llama Instruction-Tuned

     Llama 3 70B Instruct     607,677      525,063      637,822      632,915      561,171      694,292      406,103      549,999     4,615,042
     Llama 3 8B Instruct      554,642      480,391      597,560      572,409      514,765      624,254      409,802      508,688     4,262,511

 Total                      4,966,772    4,302,564    5,630,746    5,289,257    4,711,490    5,632,991    3,909,499    4,553,618    38,996,937




A. Reinhart, B. Markey, M. Laudenbach, K. Pantusen, R. Yurko, G. Weinberg, and D. W. Brown                                          7 of 22

===== Supporting Information PDF page 8 =====

      Table S4. Lexical, grammatical, and rhetorical features detected by pseudobibeR, adapted from (8, Appendix II).

          Feature                  Description                                Examples
          Past tense               Verbs in past tense                        I ran far.
          Perfect aspect           Verbs in perfect aspect                    I have written this sentence.
          Present tense            Verbs in present tense.                    the duck walks quickly
          Place adverbials         Adverbs and adverbial phrases de-          above, beside, outdoors
                                   scribing place
          First-person pro-                                                   I, we, our
          nouns
          Second-person pro-                                                  you, your
          nouns
          Third-person pro-        (excluding it)                             he, she, they, their
          nouns
          Pronoun it                                                          it, its, itself
          Demonstrative pro-       Pronouns replacing nouns                   That is an example sentence.
          nouns
          Indefinite pronouns                                                 anybody, nothing, someone
          Pro-verb ‘do’
          ‘Wh-’ questions          Direct who, what, when, where, and         When are you leaving?
                                   why questions
          Nominalizations          Nouns ending in -tion, -ment, etc.         justification, development, robustness
          Gerunds                  Participial forms functioning as nouns
          Other nouns              All other nouns
          Agentless passives       Agentless passive voice                    The model was fitted
          ‘By-’ passives           Passive voice with agent                   The task was done by Steve
          ‘Be’ as main verb        Use of “be” forms as main verb
          Existential ‘there’      “There” used to assert something           There is a feature in this sentence
                                   exists
          ‘That’ verb comple-                                                 I said that he went
          ments
          ‘That’ adjective com-                                               I’m glad that you like it
          plements
          ‘Wh-’ clauses            Clauses beginning with ‘wh-’ words         I believed what he told me
                                   (who, what, when, ...)
          Infinitives              Uninflected verb preceded by to            she tried to explain
          Present participial      Adverbial clauses used as present          Stuffing his mouth with cookies, Joe
          clauses                  participles                                ran out the door
          Past participial         Adverbial clauses used as past partici-    Built in a single week, the house
          clauses                  ples                                       would stand for fifty years
          Past participial post-   Reduced relative past participial          The solution produced by this process
          nominal                  clauses
          Present participial      Reduced relative present participial       The event causing this decline
          postnominal              clauses
          ‘That’ clauses as        ‘That’ relative clauses in subject posi-   the dog that bit me
          subject                  tion
          ‘That’ clauses as        ‘That’ relative clauses in object posi-    the dog that I saw
          object                   tion
          ‘Wh-’ relatives as       ‘Wh-’ relatives in subject position        the man who likes popcorn
          subject
          ‘Wh-’ relatives as       ‘Wh-’ relatives in object position         the man who Sally likes
          object
          Pied-piping relative     Relative clauses moved in sentence         the manner in which he was told
          clauses                  by ‘wh-’ questions


8 of 22                A. Reinhart, B. Markey, M. Laudenbach, K. Pantusen, R. Yurko, G. Weinberg, and D. W. Brown

===== Supporting Information PDF page 9 =====

                                Table S4. Lexical, grammatical, and rhetorical features (cont’d)

       Feature                    Description                                 Examples
       Sentence relatives                                                     Bob likes fried mangoes, which is the
                                                                              most disgusting thing I’ve ever heard
                                                                              of
       Because                    Causative adverbial subordinator            because
       Though                     Concessive adverbial subordinators          although, though
       If, unless                 Conditional adverbial subordinators         if, unless
       Other adverbial sub-                                                   since, while, whereas
       ordinators
       Prepositional
       phrases
       Attributive adjectives                                                 the big horse
       Predicative adjec-                                                     the horse is big
       tives
       Adverbs                    Total adverbs
       Type-token ratio           Type-token ratio, including punctuation
       Mean word length           Average word length in characters,
                                  excluding punctuation
       Conjuncts                                                              consequently, furthermore, however
       Downtoners                                                             barely, nearly, slightly
       Hedges                                                                 at about, something like, almost
       Amplifiers                                                             absolutely, extremely, perfectly
       Emphatics                                                              a lot, for sure, really
       Discourse particles                                                    sentence-initial well, now, anyway
       Demonstratives             “That”, “this”, “these”, or “those” used    That is the feature
                                  as determiners
       Possibility modals                                                     can, may, might, could
       Necessity modals                                                       ought, should, must
       Predictive modals                                                      will, would, shall
       Public verbs               Verbs indicating speaking or announc-       assert, declare, mention, predict,
                                  ing                                         swear
       Private verbs              Verbs expressing a personal intellec-       assume, believe, doubt, presume,
                                  tual state                                  understand
       Suasive verbs              Verbs indicating persuasion                 command, insist, propose
       ‘Seem’ and ‘appear’        Used as verbs
       Contractions                                                           can’t, won’t
       ‘That’ deletion            ‘That’ omitted as subordinator              I think [that] he went
       Stranded preposi-          Preposition at the end of sentence or       she is the candidate that I was think-
       tions                      clause rather than before its object        ing of
       Split infinitives          Infinitive with adverb between to and       he wants to convincingly prove that...
                                  the verb
       Split auxiliaries                                                      they were apparently shown to...
       Phrasal co-ordination      Pairs of nouns, verbs, adjectives, or       The nouns and verbs are coordinated
                                  adverbs connected by a coordinating
                                  conjunction
       Clausal co-ordination      Sentence clauses coordinated by a           The sentence was long, but I read it
                                  conjunction                                 anyway
       Synthetic negation                                                     no answer is good enough
       Analytic negation                                                      that isn’t good enough




A. Reinhart, B. Markey, M. Laudenbach, K. Pantusen, R. Yurko, G. Weinberg, and D. W. Brown                             9 of 22

===== Supporting Information PDF page 10 =====

10 of 22
                                                                                             Table S5. Biber features distinguishing human- and LLM-written text in HAP-E
                                                                                             Rate per 1,000 tokens; LLM rates relative to human Chunk 2. Blue indicates higher-than-human usage, red indicates lower. Ordered by feature importance for the
                                                                                             seven-class classification task.

                                                                                                                                                  Human                     GPT              Llama 3 Instruct    Llama 3 Base




A. Reinhart, B. Markey, M. Laudenbach, K. Pantusen, R. Yurko, G. Weinberg, and D. W. Brown
                                                                                                         Feature                            Chunk 1    Chunk 2     GPT-4o Mini    GPT-4o        8B       70B       8B      70B    Importance
                                                                                                         Present participial clauses             1.7        1.7           481%      527%     224%       261%     94%     102%         1,715.1
                                                                                                         ‘That’ clauses as subject               2.1        2.1           331%      263%     180%       173%     64%      68%         1,387.2
                                                                                                         Mean word length                        4.5        4.4           114%      116%     101%       103%     99%     100%         1,070.4
                                                                                                         Adverbs                                67.9       71.8            86%       82%      73%        75%    102%     102%           916.0
                                                                                                         Nominalizations                        14.6       14.6           209%      214%     145%       151%     88%      91%           808.9
                                                                                                         Phrasal co-ordination                   6.7        6.1           144%      194%     187%       170%     92%      97%           776.0
                                                                                                         Clausal co-ordination                  11.2       12.4            63%       59%     141%       127%    120%     116%           727.3
                                                                                                         Other nouns                           254.9      240.6            97%      103%      91%        95%     91%      94%           725.5
                                                                                                         Downtoners                              1.9        1.9           155%      118%      60%        57%     68%      73%           712.8
                                                                                                         Attributive adjectives                 46.7       43.8           140%      150%     100%       104%     79%      83%           677.7
                                                                                                         Demonstratives                          6.2        6.5           137%      133%      77%        80%     75%      80%           675.9
                                                                                                         Agentless passives                      7.7        7.8            51%       53%      96%        89%    101%      98%           664.4
                                                                                                         Past participial postnominal            1.6        1.5           257%      235%      75%        75%    129%     131%           633.7
                                                                                                         Infinitives                            15.9       16.5            87%       83%     140%       132%    120%     113%           614.9
                                                                                                         Prepositional phrases                 101.0       98.0           118%      118%     100%       100%     87%      90%           581.2
                                                                                                         Emphatics                               8.6        9.2            75%       68%      97%        98%     76%      75%           545.9
                                                                                                         Existential ‘there’                     1.9        2.1            59%       71%      42%        42%    108%     109%           527.3
                                                                                                         Possibility modals                      5.3        5.7           144%      104%     111%       116%     99%      99%           521.1
                                                                                                         Past tense                             37.5       41.9            77%       83%      91%        83%    115%     111%           519.0
                                                                                                         ‘That’ verb complements                 2.1        2.5            70%       55%     144%       114%    159%     147%           503.4
                                                                                                         Contractions                           16.9       18.1            63%       60%     141%       139%    142%     129%           497.7
                                                                                                         Other adverbial subordinators           5.9        6.2           136%      118%     114%       107%     82%      89%           496.6
                                                                                                         ‘Be’ as main verb                      29.0       30.0            61%       63%     107%       100%    108%     101%           494.3
                                                                                                         Public verbs                            5.8        6.8            53%       63%      65%        67%    119%     112%           466.1
                                                                                                         Present participial postnominal         1.4        1.3           293%      243%     125%       124%    101%     113%           451.0
                                                                                                         Predicative adjectives                  5.8        6.2            84%       90%     140%       131%    169%     154%           450.8
                                                                                                         Suasive verbs                           2.9        3.2            98%      116%      89%        90%    141%     137%           449.6
                                                                                                         Analytic negation                       8.5        9.7            73%       61%      80%        78%    113%     107%           439.6
                                                                                                         Third-person pronouns                  26.2       29.8            91%       91%     108%       104%    123%     120%           436.8
                                                                                                         Private verbs                          16.0       18.1            91%       85%     122%       113%    128%     126%           435.9
                                                                                                         Perfect aspect                          7.5        7.2            62%       60%     121%       111%     96%      92%           434.2
                                                                                                         Pro-verb ‘do’                           2.9        3.2            25%       26%      60%        59%    115%     109%           430.8

===== Supporting Information PDF page 11 =====

A. Reinhart, B. Markey, M. Laudenbach, K. Pantusen, R. Yurko, G. Weinberg, and D. W. Brown
                                                                                                                   Table S5. Biber features distinguishing human- and LLM-written text in HAP-E (cont’d)

                                                                                                                                    Human                     GPT              Llama 3 Instruct   Llama 3 Base
                                                                                             Feature                         Chunk 1     Chunk 2    GPT-4o Mini     GPT-4o        8B       70B       8B     70B   Importance
                                                                                             Present tense                       57.2        58.3           82%        76%      99%      100%     119%     116%        418.9
                                                                                             Amplifiers                           2.0         2.1           63%        46%      40%       45%      85%      85%        412.6
                                                                                             Pronoun ‘it’                        12.5        13.2           88%        92%     105%      105%     108%     105%        412.0
                                                                                             Gerunds                              3.0         3.0          156%       152%     119%      124%      83%      86%        402.9
                                                                                             First-person pronouns               34.0        35.3           81%        62%     111%      108%     136%     127%        393.4
                                                                                             Because                              1.2         1.5           19%        20%      38%       38%     121%     105%        387.9
                                                                                             Split auxiliaries                    3.4         3.4           91%        77%     126%      118%      98%      92%        379.4
                                                                                             Time adverbials                      3.7         3.7           77%        79%      68%       70%     115%     119%        366.0
                                                                                             Though, although                     0.5         0.5           65%       129%      21%       28%      83%      90%        361.2
                                                                                             Place adverbials                     3.4         3.4          146%       144%     101%       99%     118%     128%        353.9
                                                                                             Demonstrative pronouns               5.5         6.1           55%        50%      71%       76%      99%      97%        350.8
                                                                                             Predictive modals                    5.1         5.6           72%        57%      95%      106%     118%     111%        345.4
                                                                                             Indefinite pronouns                  3.2         3.3           73%        77%      84%       83%     156%     149%        323.5
                                                                                             by-passives                          0.9         0.9           56%        63%     118%      107%     113%     103%        314.9
                                                                                             Synthetic negation                   1.2         1.3           36%        51%      36%       36%      93%      91%        311.8
                                                                                             ‘Wh-’ questions                      1.3         1.4           89%        56%     141%      137%     140%     132%        306.1
                                                                                             If, unless                           2.2         2.6           78%        60%      58%       62%     117%     111%        305.1
                                                                                             ‘Seem’ and ‘appear’                  0.7         0.7          131%       179%     140%      128%      99%     105%        290.3
                                                                                             Necessity modals                     1.1         1.3          105%        78%      51%       54%     143%     137%        286.7
                                                                                             Conjuncts                            2.1         2.3          110%        96%      97%      116%      99%     104%        281.2
                                                                                             Second-person pronouns              14.9        15.7           63%        52%      77%       81%     118%     110%        277.3
                                                                                             Stranded prepositions                0.8         0.9           66%        66%     111%      114%      87%      81%        266.5
                                                                                             ‘Wh-’ relatives as subject           2.3         2.1           70%        66%     109%      102%     106%     103%        259.1
                                                                                             Sentence relatives                   1.0         1.0           50%        51%     104%      117%     101%      92%        251.7
                                                                                             ‘Wh-’ clauses                        1.7         1.9           75%        66%      90%       78%     126%     122%        247.1
                                                                                             Discourse particles                  1.1         1.0           60%        60%      89%       91%     146%     140%        181.9
                                                                                             Hedges                               1.1         1.3           50%        63%      62%       67%      89%      92%        181.1
                                                                                             Past participial clauses             0.3         0.3          273%       307%     158%      150%      59%      71%        171.7
                                                                                             ‘That’ deletion                      0.7         0.8           75%        66%      75%       73%     134%     151%        169.8
                                                                                             Pied-piping relative clauses         0.6         0.6           59%        56%      38%       43%      50%      54%        164.5
                                                                                             ‘That’ clauses as object             0.6         0.6           65%        56%      66%       60%      93%      90%        118.3
                                                                                             ‘That’ adjective complements         0.3         0.4           80%        51%     121%      106%     148%     139%        107.6
                                                                                             Split infinitives                    0.2         0.3           79%        94%     110%      104%      44%      49%         94.9
                                                                                             ‘Wh-’ relatives as object            0.3         0.3           20%        13%       8%       13%      61%      62%         62.5



11 of 22

===== Supporting Information PDF page 12 =====

12 of 22
                                                                                                       Table S5. Biber features distinguishing human- and LLM-written text in HAP-E (cont’d)

                                                                                                                        Human                     GPT              Llama 3 Instruct   Llama 3 Base
                                                                                             Feature             Chunk 1     Chunk 2    GPT-4o Mini     GPT-4o        8B       70B       8B    70B   Importance




A. Reinhart, B. Markey, M. Laudenbach, K. Pantusen, R. Yurko, G. Weinberg, and D. W. Brown

===== Supporting Information PDF page 13 =====

                                    Table S6. Effect sizes of features in LLM writing
                                      Paired Cohen’s d relative to human chunk 2

                                                 GPT               Llama 3 Instruct     Llama 3 Base
      Feature                           GPT-4o Mini     GPT-4o       8B        70B        8B     70B    Importance
      Present participial clauses               1.37       1.38     0.44       0.56     -0.03    0.01      1,715.1
      ‘That’ clauses as subject                 1.03       0.77     0.35       0.33     -0.22   -0.20      1,387.2
      Mean word length                          1.98       2.24     0.14       0.45     -0.19    0.01      1,070.4
      Adverbs                                  -0.43      -0.53    -0.77      -0.77      0.04    0.05        916.0
      Nominalizations                           1.18       1.23     0.49       0.59     -0.15   -0.12        808.9
      Phrasal co-ordination                     0.44       0.81     0.61       0.53     -0.05   -0.02        776.0
      Clausal co-ordination                    -0.54      -0.59     0.47       0.36      0.21    0.18        727.3
      Other nouns                              -0.10       0.10    -0.38      -0.24     -0.09   -0.18        725.5
      Downtoners                                0.33       0.11    -0.26      -0.29     -0.19   -0.18        712.8
      Attributive adjectives                    0.91       1.09    -0.01       0.10     -0.41   -0.37        677.7
      Demonstratives                            0.39       0.32    -0.24      -0.21     -0.25   -0.21        675.9
      Agentless passives                       -0.59      -0.56    -0.04      -0.13      0.01   -0.02        664.4
      Past participial postnominal              0.65       0.55    -0.13      -0.13      0.13    0.14        633.7
      Infinitives                              -0.24      -0.30     0.51       0.47      0.22    0.16        614.9
      Prepositional phrases                     0.77       0.68    -0.01       0.02     -0.46   -0.09        581.2
      Emphatics                                -0.31      -0.39    -0.03      -0.02     -0.23   -0.26        545.9
      Existential ‘there’                      -0.27      -0.19    -0.37      -0.39      0.03    0.05        527.3
      Possibility modals                        0.38       0.04     0.08       0.13     -0.01   -0.01        521.1
      Past tense                               -0.41      -0.29    -0.12      -0.27      0.19    0.16        519.0
      ‘That’ verb complements                  -0.23      -0.35     0.22       0.08      0.26    0.22        503.4
      Contractions                             -0.49      -0.50     0.35       0.38      0.29    0.24        497.7
      Other adverbial subordinators             0.41       0.21     0.13       0.07     -0.18   -0.11        496.6
      ‘Be’ as main verb                        -0.94      -0.83     0.11       0.00      0.09    0.02        494.3
      Public verbs                             -0.48      -0.37    -0.34      -0.34      0.13    0.10        466.1
      Present participial postnominal           0.65       0.52     0.10       0.10      0.01    0.06        451.0
      Predicative adjectives                   -0.18      -0.11     0.32       0.28      0.24    0.23        450.8
      Suasive verbs                            -0.02       0.12    -0.07      -0.07      0.16    0.10        449.6
      Analytic negation                        -0.35      -0.51    -0.23      -0.27      0.09    0.05        439.6
      Third-person pronouns                    -0.14      -0.13     0.10       0.05      0.24    0.23        436.8
      Private verbs                            -0.17      -0.26     0.29       0.20      0.28    0.27        435.9
      Perfect aspect                           -0.42      -0.43     0.16       0.09     -0.03   -0.07        434.2
      Pro-verb ‘do’                            -0.63      -0.62    -0.30      -0.33      0.06    0.04        430.8
      Present tense                            -0.40      -0.50    -0.01       0.00      0.28    0.27        418.9
      Amplifiers                               -0.25      -0.38    -0.33      -0.38     -0.07   -0.09        412.6
      Pronoun ‘it’                             -0.17      -0.11     0.06       0.06      0.06    0.04        412.0
      Gerunds                                   0.38       0.35     0.11       0.15     -0.09   -0.09        402.9
      First-person pronouns                    -0.32      -0.62     0.15       0.12      0.35    0.30        393.4
      Because                                  -0.50      -0.50    -0.34      -0.35      0.08    0.02        387.9
      Split auxiliaries                        -0.08      -0.20     0.17       0.13     -0.01   -0.06        379.4
      Time adverbials                          -0.21      -0.19    -0.26      -0.26      0.07    0.06        366.0
      Though, although                         -0.13       0.09    -0.32      -0.28     -0.05   -0.03        361.2
      Place adverbials                          0.35       0.33     0.01      -0.01      0.11    0.17        353.9
      Demonstrative pronouns                   -0.50      -0.56    -0.28      -0.26     -0.01   -0.03        350.8
      Predictive modals                        -0.28      -0.43    -0.03       0.04      0.11    0.08        345.4
      Indefinite pronouns                      -0.22      -0.18    -0.11      -0.12      0.19    0.20        323.5
      by-passives                              -0.21      -0.17     0.06       0.03      0.04    0.01        314.9
      Synthetic negation                       -0.37      -0.27    -0.33      -0.34     -0.02   -0.04        311.8
      ‘Wh-’ questions                          -0.06      -0.25     0.16       0.16      0.11    0.10        306.1


A. Reinhart, B. Markey, M. Laudenbach, K. Pantusen, R. Yurko, G. Weinberg, and D. W. Brown                      13 of 22

===== Supporting Information PDF page 14 =====

                               Table S6. Effect sizes of features in LLM writing (cont’d)

                                                GPT               Llama 3 Instruct     Llama 3 Base
      Feature                          GPT-4o Mini     GPT-4o        8B        70B          8B    70B    Importance
      If, unless                              -0.16       -0.30   -0.29       -0.27     0.09      0.06        305.1
      ‘Seem’ and ‘appear’                      0.12        0.27    0.12        0.09     0.00      0.02        290.3
      Necessity modals                         0.02       -0.10   -0.22       -0.22     0.14      0.12        286.7
      Conjuncts                                0.07       -0.03   -0.02        0.09    -0.01      0.02        281.2
      Second-person pronouns                  -0.39       -0.49   -0.21       -0.20     0.11      0.07        277.3
      Stranded prepositions                   -0.16       -0.16    0.04        0.05    -0.04     -0.07        266.5
      ‘Wh-’ relatives as subject              -0.21       -0.23    0.04        0.01     0.03      0.01        259.1
      Sentence relatives                      -0.26       -0.25    0.02        0.06     0.00     -0.03        251.7
      ‘Wh-’ clauses                           -0.17       -0.24   -0.06       -0.14     0.11      0.10        247.1
      Discourse particles                     -0.20       -0.20   -0.04       -0.04     0.14      0.04        181.9
      Hedges                                  -0.22       -0.16   -0.15       -0.13    -0.04     -0.02        181.1
      Past participial clauses                 0.33        0.36    0.11        0.10    -0.09     -0.07        171.7
      ‘That’ deletion                         -0.11       -0.16   -0.10       -0.11     0.09      0.11        169.8
      Pied-piping relative clauses            -0.16       -0.17   -0.23       -0.21    -0.17     -0.17        164.5
      ‘That’ clauses as object                -0.13       -0.17   -0.12       -0.15    -0.02     -0.03        118.3
      ‘That’ adjective complements            -0.06       -0.16    0.05        0.02     0.09      0.06        107.6
      Split infinitives                       -0.05       -0.02    0.02        0.01    -0.15     -0.13         94.9
      ‘Wh-’ relatives as object               -0.25       -0.27   -0.28       -0.26    -0.10     -0.10         62.5




14 of 22          A. Reinhart, B. Markey, M. Laudenbach, K. Pantusen, R. Yurko, G. Weinberg, and D. W. Brown

===== Supporting Information PDF page 15 =====

                                                             GPT-4o                          Llama 3 70B Instruct                           Llama 3 70B
                  Present participial clauses
                   ‘That’ clauses as subject
                           Mean word length
                                      Adverbs
                             Nominalizations
                       Phrasal co-ordination
                       Clausal co-ordination
                                  Other nouns
                                  Downtoners
                       Attributive adjectives
                             Demonstratives
                         Agentless passives
                 Past participial postnominal




 Biber feature
                                     Inﬁnitives
                      Prepositional phrases

                                                         GPT-4o Mini                          Llama 3 8B Instruct                            Llama 3 8B
                  Present participial clauses
                   ‘That’ clauses as subject
                           Mean word length
                                      Adverbs
                             Nominalizations
                       Phrasal co-ordination
                       Clausal co-ordination
                                  Other nouns
                                  Downtoners
                       Attributive adjectives
                             Demonstratives
                         Agentless passives
                 Past participial postnominal
                                     Inﬁnitives
                      Prepositional phrases
                                                  -4    -2       0         2       4    -4        -2      0         2       4    -4        -2       0         2       4
                                                                      Standardized rate difference (LLM - human)

Fig. S1. Boxplots of paired differences between features for LLM and human writing following the same chunk 1, standardized by the standard deviation of the paired
differences. Some features show very little overlap: for instance, with GPT-4o and GPT-4o Mini, the mean word length of the LLM-generated text is almost always longer than
the mean word length in the corresponding human chunk 2.




A. Reinhart, B. Markey, M. Laudenbach, K. Pantusen, R. Yurko, G. Weinberg, and D. W. Brown                                                                     15 of 22

===== Supporting Information PDF page 16 =====

Table S7. Most overrepresented words in LLM-generated texts (by frequency), ordered by fraction of outputs containing each
word

             GPT-4o             GPT-4o Mini       Llama 3 70B Instruct   Llama 3 8B Instruct     Llama 3 70B         Llama 3 8B
      Word            Rate   Word          Rate   Word           Rate    Word           Rate   Word        Rate   Word        Rate

      amidst          27%    amidst        27%    reminder       12%     reminder       15%    bananas      8%    deborah         4%
      tapestry        23%    tapestry      24%    prioritize      5%     unease          6%    bam          6%    goodnight       3%
      intricate       14%    vibrant       20%    pang            4%     prioritize      5%    denis        3%    matty           3%
      underscore      14%    ignite        20%    palpable        4%     pang            4%    darry        2%    ml              2%
      unspoken        11%    intricate     17%    unease          4%     continuation    4%    paperback    2%    rambo           2%
      camaraderie     11%    palpable      15%    policymaker     3%     palpable        4%    verona       2%    merlin          1%
      solace          10%    fleeting      15%    intricate       3%     waft            2%    rekall       2%    missy           1%
      unravel         10%    camaraderie   13%    continuation    2%     rut             2%    filth        1%    elisa           1%
      fleeting         9%    grapple       12%    shoutout        2%     grapple         2%    janice       1%    fay             1%
      palpable         9%    cacophony      7%    camaraderie     1%     camaraderie     1%    ebook        1%    worcester       1%




16 of 22               A. Reinhart, B. Markey, M. Laudenbach, K. Pantusen, R. Yurko, G. Weinberg, and D. W. Brown

===== Supporting Information PDF page 17 =====

                Table S8. Most underrepresented words in LLM-generated texts, relative to human usage rates

           GPT-4o             GPT-4o Mini          Llama 3 70B Instruct    Llama 3 8B Instruct       Llama 3 70B           Llama 3 8B
    Word            Rate   Word             Rate   Word           Rate    Word             Rate   Word          Rate    Word        Rate

    i.e.       0.0026      extremely   0.0034      yep           0.0075   anyways        0.0097   jeez          0.040   bingo       0.033
    blah       0.0063      spokesman   0.0059      fucking       0.0075   analyse         0.011   donnie        0.042   scorch      0.040
    fuck       0.0079      i.e.        0.0095      horrible      0.0077   somebody        0.012   alexithymia   0.046   been        0.043
    fucking    0.0083      unhappy      0.010      ok             0.011   characterise    0.013   frampton      0.048   abt         0.043
    asshole    0.0093      bitch        0.012      fuckin         0.013   fuck            0.014   y’all         0.048   bananas     0.043
    nasty       0.011      fucking      0.012      amid           0.015   obviously       0.014   analogous     0.053   pham        0.043
    chum        0.013      kg           0.013      fortunately    0.017   ok              0.014   carotenoid    0.053   ie          0.045
    shit        0.014      fuck         0.014      i.e.           0.018   fuckin          0.014   mussel        0.053   monstrous   0.045
    ok          0.014      visa         0.015      obviously      0.018   blah            0.015   que           0.053   pow         0.045
    and/or      0.016      ter          0.016      amongst        0.019   yep             0.016   whatsapp      0.053   unquote     0.045




A. Reinhart, B. Markey, M. Laudenbach, K. Pantusen, R. Yurko, G. Weinberg, and D. W. Brown                                              17 of 22

===== Supporting Information PDF page 18 =====

Table S9. Random forest pairwise classification accuracy, distinguishing each LLM from human text. Training accuracy based
on out-of-bag error

                                                          Trained on HAP-E           Trained on CAP
                            LLM                        Training   Test on CAP   Training   Test on HAP-E

                            GPT-4o

                                GPT-4o                  98.3%          98.4%     98.9%            97.4%
                                GPT-4o Mini             98.7%          98.2%     99.2%            97.5%

                            Llama Instruct

                                Llama 3 70B Instruct    94.5%          93.5%     94.6%            91.8%
                                Llama 3 8B Instruct     95.5%          95.3%     96.1%            94.1%

                            Llama Base

                                Llama 3 70B             93.0%          94.6%     95.8%            89.1%
                                Llama 3 8B              94.0%          93.6%     95.6%            89.4%




18 of 22            A. Reinhart, B. Markey, M. Laudenbach, K. Pantusen, R. Yurko, G. Weinberg, and D. W. Brown

===== Supporting Information PDF page 19 =====

              Table S10. Lasso pairwise classification accuracy, distinguishing each LLM from human text

                                                          Trained on CAP           Trained on HAP-E
                          LLM                        Training   Test on HAP-E   Training   Test on CAP

                          GPT-4o

                              GPT-4o                  95.9%            95.3%     96.5%          95.3%
                              GPT-4o Mini             96.7%            96.3%     96.9%          96.2%

                          Llama Instruct

                              Llama 3 70B Instruct    91.1%            90.7%     92.1%          90.2%
                              Llama 3 8B Instruct     92.4%            91.8%     92.9%          91.9%

                          Llama Base

                              Llama 3 70B             77.2%            73.2%     75.6%          75.3%
                              Llama 3 8B              77.6%            73.8%     76.3%          75.3%




A. Reinhart, B. Markey, M. Laudenbach, K. Pantusen, R. Yurko, G. Weinberg, and D. W. Brown                 19 of 22

===== Supporting Information PDF page 20 =====

           Table S11. Random forest accuracy when trained on HAP-E and classifying M4 arXiv data.

                                                              Acc.            Acc.
                               Model
                                                          (in-sample)   (out-of-sample)

                               ChatGPT

                                   GPT 4o                     98.22%           70.63%
                                   GPT 4o Mini                98.73%           60.77%

                               Llama Instruction-Tuned

                                   Llama 3 70B Instruct       95.33%           68.20%
                                   Llama 3 8B Instruct        96.20%           65.60%

                               Llama Base

                                   Llama 3 70B                92.43%           51.17%
                                   Llama 3 8B                 93.56%           51.85%




20 of 22      A. Reinhart, B. Markey, M. Laudenbach, K. Pantusen, R. Yurko, G. Weinberg, and D. W. Brown

===== Supporting Information PDF page 21 =====

                Table S12. Random forest accuracy when trained on CAP and classifying M4 arXiv data.

                                                                  Acc.            Acc.
                                   Model
                                                              (in-sample)   (out-of-sample)

                                   ChatGPT

                                       GPT 4o                     98.76%           70.68%
                                       GPT 4o Mini                99.04%           65.27%

                                   Llama Instruction-Tuned

                                       Llama 3 70B Instruct       95.35%           59.27%
                                       Llama 3 8B Instruct        96.60%           57.95%

                                   Llama Base

                                       Llama 3 70B                95.53%           50.92%
                                       Llama 3 8B                 95.39%           51.48%




A. Reinhart, B. Markey, M. Laudenbach, K. Pantusen, R. Yurko, G. Weinberg, and D. W. Brown             21 of 22

===== Supporting Information PDF page 22 =====

133   References
134    1. X Yang, et al., DNA-GPT: Divergent n-gram analysis for training-free detection of GPT-generated text in The
135       Twelfth International Conference on Learning Representations. (2024).
136    2. M Davies, The Corpus of Contemporary American English (COCA) (2008).
137    3. OpenAI, Hello GPT-4o (2024).
138    4. OpenAI, GPT-4o mini: advancing cost-efficient intelligence (2024).
139    5. Meta, Introducing Meta Llama 3: The most capable openly available LLM to date (2024).
140    6. W Kwon, et al., Efficient memory management for large language model serving with PagedAttention in
141       Proceedings of the ACM SIGOPS 29th Symposium on Operating Systems Principles. (2023).
142    7. Y Wang, et al., M4: Multi-generator, Multi-domain, and Multi-lingual Black-Box Machine-Generated Text
143       Detection in Proceedings of the 18th Conference of the European Chapter of the Association for Computational
144       Linguistics (Volume 1: Long Papers), eds. Y Graham, M Purver. (Association for Computational Linguistics, St.
145       Julian’s, Malta), pp. 1369–1407 (2024).
146    8. D Biber, Variation across Speech and Writing. (Cambridge University Press), (1988).
147    9. D Biber, Dimensions of Register Variation: A Cross-Linguistic Comparison. (Cambridge University Press),
148       (1995).
149   10. D Biber, S Conrad, Register, Genre, and Style. (Cambridge University Press), (2009).
150   11. EB DeJeu, DW Brown, DocuScope, multi-dimensional analysis, and student writing in Corpora and Rhetorically
151       Informed Text Analysis: The diverse applications of DocuScope, eds. DW Brown, DZ Wetzel. (John Benjamins),
152       pp. 42–78 (2023).
153   12. B Markey, DW Brown, M Laudenbach, A Kohler, Dense and disconnected: Analyzing the sedimented style of
154       ChatGPT-generated text at scale. Writ. Commun. 41, 571–600 (2024).
155   13. V Brezina, Statistics in Corpus Linguistics: A Practical Guide. (Cambridge University Press), (2018).
156   14. K Hyland, Discliplinary Discourses: Social Interactions in Academic Writing. (Longman), (2000).
157   15. S Wallis, Statistics in Corpus Linguistics Research: A New Approach. (Routledge), (2021).
158   16. E Friginal, Twenty-five years of Biber’s Multi-Dimensional Analysis: introduction to the special issue and an
159       interview with Douglas Biber. Corpora 8, 137–152 (2013).
160   17. JA Hardy, U Römer, Revealing disciplinary variation in student writing: A multi-dimensional analysis of the
161       Michigan Corpus of Upper-level Student Papers (MICUSP). Corpora 8, 183–207 (2013).
162   18. LL Aull, Z Lancaster, Linguistic markers of stance in early and advanced academic writing: A corpus-based
163       comparison. Writ. Commun. 31, 151–183 (2014).
164   19. K Hyland, Stance and engagement: A model of interaction in academic discourse. Discourse Stud. 7, 173–192
165       (2005).
166   20. J Cohen, Statistical Power Analysis for the Behavioral Sciences. (Routledge), 2nd edition, (1988).
167   21. MN Wright, A Ziegler, ranger: A fast implementation of random forests for high dimensional data in C++ and
168       R. J. Stat. Softw. 77, 1–17 (2017).
169   22. J Friedman, T Hastie, R Tibshirani, Regularization paths for generalized linear models via coordinate descent. J.
170       Stat. Softw. 33, 1–22 (2010).
171   23. JQJ Liu, et al., The great detectives: humans versus AI detectors in catching large language model-generated
172       medical writing. Int. J. for Educ. Integr. 20, 8 (2024).
173   24. T Waltzer, C Pilegard, GD Heyman, Can you spot the bot? Identifying AI-generated writing in college essays.
174       Int. J. for Educ. Integr. 20 (2024).




      22 of 22           A. Reinhart, B. Markey, M. Laudenbach, K. Pantusen, R. Yurko, G. Weinberg, and D. W. Brown
```

## Extraction verification

- **Beginning checked:** Main PDF page 1 was rendered and compared with the extracted title, byline, dates, abstract, significance statement, and opening body text. Supporting Information page 1 was rendered and checked for the title, author list, contents list, and page count.
- **Middle checked:** Main PDF page 3 was rendered and compared with Figure 3, its caption, the top-feature discussion, effect sizes, and vocabulary findings. Supporting Information pages 6 and 11 were rendered and compared with Table S2 and the continuation of Table S5; the source's literal `5550,463` typo was confirmed visually.
- **End checked:** Main PDF page 6 was rendered and checked for references 7-35 and the final page marker. Supporting Information page 22 was rendered and checked for SI references 1-24 and the final page marker.
- **Structure checked:** `pdfinfo` reports six main-paper pages and 22 Supporting Information pages. The main paper contains four figures, Table 1, one substantive footnote, discussion, data availability, acknowledgments, author contributions, competing interests, and 35 references. The supplement contains Supporting Information text, Figure S1, Tables S1-S12, and 24 SI references; all were checked in the extraction. Table S4's 66-row inventory and the 66 result rows in Tables S5-S6 disagree on type-token ratio versus time adverbials, and the otherwise empty page 12 preserves a continuation header. PMC HTML and Europe PMC XML independently name the same supplement and complete article structure.
- **Known omissions:** none. Decorative journal marks and vector/raster figure pixels are not duplicated as text, but the complete final PDFs are preserved and every figure caption and text-bearing table is present in the extraction.

## Preserved attachments

| Path | Role in the source | SHA-256 | Preservation / extraction notes |
|---|---|---|---|
| `snapshots/attachments/reinhart-llm-write-like-humans-pnas-2025.pdf` | Six-page PNAS version-of-record article | `da8a700d15d355b555a8b471d166549ba2c02ad4b800d182ed1a3f879ef9d7a8` | Downloaded from PMC; complete embedded text extracted with `pdftotext -layout`; pages 1, 3, and 6 rendered and visually checked. |
| `snapshots/attachments/reinhart-llm-write-like-humans-pnas-2025-supplement.pdf` | 22-page Supporting Information with Supporting text, Fig. S1, Tables S1-S12, and SI references | `c3324d639b410d5f2640f44e5167405f58a422f5a58e26bbc825628ddac8e86a` | Downloaded from PMC; complete embedded text extracted with `pdftotext -layout`; pages 1, 6, 11, and 22 rendered and visually checked. |
