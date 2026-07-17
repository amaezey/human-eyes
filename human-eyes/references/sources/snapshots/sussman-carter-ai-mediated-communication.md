# Detecting Effects of AI-Mediated Communication on Language Complexity and Sentiment

- **Canonical URL:** https://doi.org/10.1145/3701716.3717543
- **Alternate access URLs:**
  - https://arxiv.org/abs/2504.19556v1
  - https://arxiv.org/pdf/2504.19556v1
  - https://export.arxiv.org/api/query?id_list=2504.19556
  - https://api.crossref.org/works/10.1145/3701716.3717543
- **Author / owner:** Kristen Sussman and Daniel Carter
- **Publisher:** Association for Computing Machinery (ACM)
- **Published:** 2025-04-28 on arXiv; 2025-05-08 in the Companion Proceedings of the ACM Web Conference 2025
- **Retrieved:** 2026-07-17
- **Stable identifier:** DOI 10.1145/3701716.3717543; arXiv:2504.19556v1
- **Version / revision:** arXiv v1, submitted 2025-04-28; five-page ACM-formatted proceedings paper
- **Extraction method:** Official arXiv PDF downloaded with `curl`; PDF metadata and five-page extent checked with `pdfinfo`; complete embedded text layer converted with Poppler `pdftotext -layout`; pages 1, 2, 3, and 5 rendered with `pdftoppm` and visually compared; arXiv API and Crossref metadata used to verify revision and publication identity
- **Full-text status:** complete
- **Access and transformation notes:** The arXiv experimental HTML route returned 404 and a later arXiv abstract-page request returned 429; the versioned PDF and arXiv API remained available. The text extraction retains the two-column reading order, headings, captions, references, and marked page breaks. Figure graphics and the red change-highlighting described in section 2.4 are not encoded as text but remain complete in the preserved PDF attachment. No substantive pages, notes, appendices, or references were omitted.

## Full text

Detecting Effects of AI-Mediated Communication on Language
                  Complexity and Sentiment∗
                          Kristen Sussman†                                                                        Daniel Carter
       School of Journalism and Mass Communication                                              School of Journalism and Mass Communication
                   Texas State University                                                                   Texas State University
                    San Marcos, TX, USA                                                                      San Marcos, TX, USA
                   ksussman@txstate.edu                                                                       dcarter@txstate.edu




Abstract                                                                                 1 Introduction
Given the subtle human-like effects of large language models on                              Recent generative artificial intelligence (AI) advancements,
linguistic patterns, this study examines shifts in language over                         such as OpenAI’s ChatGPT, have raised questions about
time to detect the impact of AI-mediated communication (AI-                              distinguishing human-written content from AI-generated text. A
MC) on social media. We compare a replicated dataset of 970,919                          growing concern is the integration of AI and AI-generated
tweets from 2020 (pre-ChatGPT) with 20,000 tweets from the                               language into human communication, a trend accelerated by
same period in 2024, all of which mention Donald Trump during                            tools like OpenAI's ChatGPT. These platforms enable user
election periods. Using a combination of Flesch-Kincaid                                  interaction with large language models (LLMs), establishing AI
readability and polarity scores, we analyze changes in text                              as a widely adopted communication tool. The increased adoption
complexity and sentiment. Our findings reveal a significant                              of language models facilitates more sophisticated and harder-to-
increase in mean sentiment polarity (0.12 vs. 0.04) and a shift                          detect propaganda. AI-mediated communication (AI-MC) refers
from predominantly neutral content (54.8% in 2020 to 39.8% in                            to interpersonal communication facilitated by AI systems that
2024) to more positive expressions (28.6% to 45.9%). These                               can generate, enhance, or modify content to achieve
findings suggest not only an increasing presence of AI in social                         communication and relational goals 1 . Distinct from earlier
media communication but also its impact on language and                                  technologies, AI-MC demonstrates an ability to generate text
emotional expression patterns.                                                           that closely resembles human writing,2 while exhibiting qualities
                                                                                         associated with humans, such as trustworthiness or appeal.
CCS Concepts                                                                                 At the same time, the potential social implications of AI
• Human-centered computing • Human-computer interaction                                  remain understudied, lagging behind the rate of development of
• Empirical studies in HCI • HCI theory, concepts, and models                            large language models (LLMs) 3 . Tech platforms have been
                                                                                         accused of intensifying political polarization4, and the adoption
Keywords                                                                                 of LLMs continues with little known about the linguistic effects
AI-MC, AI-detection, social media, ChatGPT                                               of AI-MC in social networks. Building on insights from
                                                                                         computer-mediated communication (CMC) research, AI-MC
ACM Reference format:                                                                    offers a framework for exploring the social effects of human
Kristen Sussman and Daniel Carter. Detecting Effects of AI-Mediated                      interactions facilitated by digital platforms, such as social
Communication on Language Complexity and Sentiment. In Companion                         networks5.
Proceedings of the ACM Web Conference 2025 (WWW Companion ’25),                              This growing integration of AI tools into communication
April 28-May 2, 2025, Sydney, NSW, Australia. ACM, New York, NY, USA,                    necessitates an examination of their linguistic and social impacts,
5 pages. https://doi.org/10.1145/3701716.3717543                                         particularly within the rapidly evolving landscape of social
                                                                                         media. Thus, the study has two primary objectives: (1) to analyze
Permission to make digital or hard copies of all or part of this work for personal or
                                                                                         shifts in linguistic patterns and sentiment in social media
classroom use is granted without fee provided that copies are not made or
distributed for profit or commercial advantage and that copies bear this notice and      interactions before and after the introduction of ChatGPT and (2)
the full citation on the first page. Copyrights for components of this work owned by     to quantify the growth in the use of AI-MC within social media
others than the author(s) must be honored. Abstracting with credit is permitted. To      discussions from 2020 to 2024.
copy otherwise, or republish, to post on servers or to redistribute to lists, requires
prior specific permission and/or a fee. Request permissions from
Permissions@acm.org.                                                                     1.1 Related Work
WWW Companion '25, April 28-May 2, 2025, Sydney, NSW, Australia
© 2025 Copyright is held by the owner/author(s). Publication rights licensed to
                                                                                            Prior research has explored traditional and novel features to
ACM.                                                                                     detect AI-generated and AI-rephrased text, achieving high
ACM 979-8-4007-1331-6/25/04…                                                             classification accuracy with F1 scores exceeding 96% for basic
https://doi.org/10.1145/3701716.3717543                                                  detection and 78% for rephrased text4. These systems leverage


--- page break ---

WWW Companion '25, April 28-May 2, 2025, Sydney, NSW, Australia                                              Kristen Sussman & Daniel Carter


features like perplexity, semantic analysis, readability, and AI     engagement, and key topics discussed on social media platforms
feedback to improve performance, even outperforming tools like       during this period.
GPTZero. While their work focuses on controlled text corpora             2.2.2 US Election 2024 Tweets. Data was sourced using
and classification accuracy, our study examines real-world social    Meltwater10 and contains tweets mentioning Donald Trump (e.g.,
media data to identify temporal shifts in AI-mediated                #DonaldTrump OR #Trump) and tweets related to his 2024
communication. By analyzing linguistic complexity and                presidential campaign (n = 20,000). Data includes information
sentiment polarity, we provide a broader understanding of how        such as the date and time of the tweet, the tweet text, the
AI influences user-generated content over time. This distinction     number of likes and retweets, and the year. The data was
highlights the complementary nature of previous research on          collected during the period from October 15, 2024, to November
feature-based detection methods and our focus on dynamic, real-      8, 2024, replicating the 2020 dataset and covering approximately
world applications.                                                  3.5 weeks leading up to and immediately following the 2024 U.S.
    Initial studies show that AI-generated responses used in         Presidential Election.
communication impact how people write6 and influence how
they communicate, in part based on the mere presence of smart        2.3 Temporal           and      Textual       Tests       of     AI-
replies, which have shown to be linguistically skewed with               Detection
excessive expressions of positive emotion7. Similar mechanisms           Researchers have utilized the Flesch-Kincaid readability test
may apply to AI-driven communication on social media. This           and polarity analysis, inspiring our investigation into these
shift suggests that AI's influence extends beyond content            linguistic features to detect AI-generated text10. By integrating
generation to shape broader patterns of online discourse and         readability metrics, along with polarity, our tests expand on their
user interaction, potentially creating a feedback loop where AI-     methodology to enhance classification accuracy, particularly in
influenced communication styles become increasingly prevalent        distinguishing subtle effects of AI.
and normalized.                                                          2.3.1 Flesch-Kincaid readability test. The Flesch-Kincaid
    Shin et al.8 investigated the social dimensions of AI-MC and     readability test uses natural language processing to analyze
found that it plays a role in clarifying emotions and enhancing      sentence structure and syllable count. AI-generated text tends to
descriptive precision. Despite this, much of the existing research   exhibit more consistent sentence lengths and syllable
on AI-MC has concentrated on users' perceptions of its               distributions, leading to a distinct Flesch-Kincaid score compared
trustworthiness (e.g., Hohenstein & Jung, 2020), often in contexts   to typical human writing 11 . These differences in readability
involving real-time interactions through chatbots or instant         scores can serve as an indicator of AI authorship, offering a
messaging. In contrast, this study focuses on how individuals        quantitative approach to distinguish between human and
engage with AI-MC in social media environments where the             machine-produced content. Text complexity was assessed using
origin of the message is concealed from the audience. This           the Flesch-Kincaid Grade Level formula, which evaluates
dynamic may increase the audience's susceptibility to the            readability based on word and sentence structure12. The cleaned
influence of AI-MC, as they are more likely to assume the            datasets were compared using an independent samples t-test to
messages are authored by other humans.                               evaluate differences in linguistic complexity between the two
                                                                     time periods. Statistical significance was set at p<0.05
2 Methodology
   While GPT-3 was introduced in June 2020, public adoption of
LLMs for text generation began in March 2022 with the release
of GPT-3.5 and accelerated with the launch of ChatGPT in
November 20229. As a result, the 2020 tweet dataset serves as a
baseline for human-authored content, enabling comparisons
with tweet data from 2024. Controlling for differences among
channels and periods, we focused on a 3.5-week period occurring
between October 15 and November 8, 2020 and October 15 and
November 8, 2024.

2.2 Data Sources
   2.2.1 US Election 2020 Tweets. Data was sourced from Kaggle,      Figure 1: Flesch-Kincaid Readability Scores by Year
and contains tweet data (n = 970,919) mentioning Donald Trump
and related to the 2020 United States presidential election. It         Analysis of readability patterns revealed evidence suggestive
includes information such as tweet content, the date and time of     of more standardized text production in 2024, potentially
posting, user information (e.g., user ID, screen name), and          indicating AI-mediated communication. While tweets from both
engagement metrics (likes, retweets, and replies). This dataset      periods showed similar central tendencies (2020: M = 10.24, SD =
provides valuable insights into the public discourse surrounding     5.80; 2024: M = 10.04, SD = 5.55), the 2024 dataset demonstrated
the election, allowing for analysis of sentiment, political          notably constrained maximum values (50.9 compared to 575.2 in


--- page break ---

Detecting Effects of AI-Mediated Communication on Language
                                                                                  WWW Companion '25, April 28-May 2, 2025, Sydney, NSW, Australia
Complexity and Sentiment


2020) and reduced variability in extreme scores. This                  and a 3.6% reduction in sentence variance (44.660 ± 73.059 to
compression of outliers, particularly in the upper range, aligns       43.038 ± 61.099).
with patterns typically associated with AI-generated content,                The Cohen's d values (Figure 3) indicate a moderate effect
which tends to produce more consistently structured text.              size for polarity changes (0.281) and small to moderate effect
    An independent samples t-test confirmed a significant              sizes for linguistic changes (-0.182 for word length, -0.022 for
difference between the periods, t(990,917) = 4.79, p < .001, though    sentence variance). All changes are statistically significant (p <
the practical difference in mean grade levels was modest (0.20).       0.001), with non-overlapping confidence intervals supporting the
The most compelling evidence for AI-mediation comes from the           robustness of these findings. The bimodal distribution in the
standardization of extreme values rather than shifts in central        2024 dataset, particularly in the positive polarity range (0.5–0.8),
tendency. The 2024 dataset showed more tightly controlled              suggests a systematic shift in communication patterns that
boundaries in readability scores, with 95% of tweets falling           wasn't present in the 2020 dataset.
between -3.1 and 50.9, compared to the wider distribution in
2020. This increased precision in readability scores suggests a
shift toward more standardized text production, consistent with
algorithmic mediation in content generation or enhancement.
    2.3.2 Polarity test. We conducted a sentiment analysis of social
media posts from 2020 (n = 970,919) and 2024 (n = 20,000) using
TextBlob and VADER sentiment analysis tools. Preprocessing
steps, including the removal of URLs, handling of special
characters, and text normalization, ensured consistent data
preparation before applying the VADER sentiment analyzer.
Polarity scores, which range from -1 (negative) to +1 (positive),
were analyzed across the two datasets. The most notable change
is the 163.4% increase in polarity (sentiment) from 2020 to 2024
(Figure 1), which could indicate a shift in tone or style              Figure 3: Effect Sizes by Magnitude of Changes
potentially influenced by AI.
                                                                       2.4 Manual Inspection
                                                                           While algorithms are a critical component, the primary
                                                                       emphasis of AI-MC is on human communication. This
                                                                       distinction becomes evident when humans leverage AI to
                                                                       achieve communication goals, harnessing algorithmic
                                                                       capabilities to enhance interactions with others. Using a prompt
                                                                       engineering process called in-context learning (ICL), humans can
                                                                       use natural language to guide the generative AI model to learn
                                                                       by providing relevant instructions or exemplars within the
                                                                       prompt13. Applications of AI-MC include iterative engagement,
                                                                       such as using an LLM to revise human-written text or revising
Figure 2: Polarity Distributions by Year
                                                                       AI-written text in order to improve clarity, engagement, and
      Further analysis reveals significant changes in polarity         communication outcomes. Because AI holds significant potential
distribution (SD2020 = 0.254, SD2024 = 0.284), as visualized in        for influencing specific audiences, often in subtle ways that may
Figure 2, with a notable reduction in neutral content (62.9% in        go unnoticed by those targeted, we tested the AI’s ability to
2020 to 49.4% in 2024, Δ = -13.5%) and a 163.4% increase in mean       enact changes on the human-generated tweets from the 2020
polarity (from 0.044 ± 0.254 to 0.115 ± 0.284). The most               dataset. Specifically, we asked ChatGPT-4 to, “Rewrite the tweet,
pronounced indicator of AI-MC growth is observed in the                to improve for clarity and engagement” and provided context in
extremes of the sentiment spectrum: strongly positive sentiment        the prompt with a copy of the original tweet to be improved.
nearly doubled (4.4% to 8.1%, Δ = +3.7%), while strongly negative          Differences are highlighted in red below via original (odd-
sentiment showed a modest decrease (2.1% to 1.7%, Δ = -0.4%).          numbered) and AI-improved tweets (even-numbered):
These asymmetrical shifts in sentiment distribution (p < 0.001)
suggest systematic changes in communication patterns.                  •    Original tweet: The GOP would rather fill a Supreme Court seat
      The kernel density estimation plots demonstrate distinct              before (probably) losing majority than helping Americans and
                                                                            Small Business with COVID relief #vote #EconomicRecoveryPlan
bimodal patterns in 2024, with pronounced peaks in the positive             #IChooseAmerica #Trump.
polarity range (0.5–0.8) that were absent in the 2020 dataset.         •    AI-improved: The GOP is prioritizing filling a Supreme Court seat
Additional linguistic markers support this trend, including a 6.6%          over delivering COVID relief for Americans and small businesses,
decrease in average word length (7.188 ± 2.615 to 6.715 ± 1.995)            even as their majority hangs in the balance. Let’s choose leaders


--- page break ---

WWW Companion '25, April 28-May 2, 2025, Sydney, NSW, Australia                                                                   Kristen Sussman & Daniel Carter


     who put people first. 🗳️ #Vote #EconomicRecoveryPlan                     3.1 Limitations
     #IChooseAmerica #Trump
•    Original tweet: Trump's entire presidency has been about hate and           This study recognizes several limitations. Although both
     division. It's ok to disagree about politics, it's not ok to view half   datasets were sourced from the same social media platform and
     the country as the enemy. #TrumpMustGo #VoteHimOut #Vote                 centered on posts referencing Donald Trump, potential biases
     #StopTrumpsTerror #Trump #VoteBidenHarris #CountryOverParty              may arise, as the findings could reflect platform-specific
     #BidenHarris2020 #RestoreAmerica
                                                                              dynamics or the distinctive communication style of one
•    AI-improved: Trump’s presidency has fueled hate and division.
     Disagreeing on politics is fine, but treating half the country as the    individual rather than broader trends in AI-MC. Furthermore,
     enemy is not. It’s time for unity and leadership that puts America       while the classification analysis reveals changes in linguistic
     first. 🇺🇸 #VoteHimOut #BidenHarris2020 #CountryOverParty                 patterns and sentiment, isolating the effects of AI from other
     #RestoreAmerica                                                          contextual influences, such as shifts in the political climate or
                                                                              audience behavior over time, remains a challenge. These
    Cosine similarity analysis was conducted to assess the                    limitations call for future researchers to extend and replicate our
magnitude of linguistic transformation between original tweets                findings.
and their AI-modified counterparts (e.g., AI-MC). Indeed, a test
of cosine similarity, a computational procedure that measures                 3.2      Conclusion and Future Work
how similar one body of text is to another on a 0 (completely                    The analysis reveals a significant increase in mean polarity
dissimilar) to 1 (completely similar) scale, revealed substantial             and readability scores between 2020 and 2024, aligning with
linguistic divergence, with similarity scores of 0.376 and 0.398              prior research on AI's tendency to embed overly positive
for the two tweet pairs respectively. These notably low similarity            emotional expressions in generated content. This trend,
scores (M = 0.387, SD = 0.015) indicate that the AI-MC system                 validated through linguistic shifts and manual inspection,
implements significant linguistic restructuring while preserving              suggests that AI-MC has an increased presence on social media.
the core message, suggesting a systematic approach to content                 These shifts highlight implications for user engagement, as AI
modification using ICL prompts. The consistency of these scores               appears to be generating content that is both more emotionally
across both samples demonstrates that the AI-MC system                        engaging and accessible. The increase in positive sentiment and
maintains a relatively stable magnitude of transformation,                    reduction in linguistic complexity may also enhance content
modifying approximately 60-63% of the linguistic content while                shareability and user interaction, offering important calls for
retaining sufficient semantic similarity to preserve the original             future work.
message intent.
    A qualitative analysis reveals notable differences between the
                                                                              References
two sets of tweets, aligning with the polarity test results, which
                                                                              [1] Hancock, J. T., Naaman, M., & Levy, K. (2020). AI-Mediated Communication:
indicate a higher median polarity in 2024 compared to 2020. One                   Definition, research agenda, and ethical considerations. Journal of Computer-
significant distinction is the inclusion of future-oriented                       Mediated Communication, 25(1), 89–100. https://doi.org/10.1093/jcmc/zmz022
solutions in the AI-improved tweets. Phrases such as “Let’s                   [2] Dale, R. (2021). GPT-3: What’s it good for?. Natural Language Engineering,
                                                                                  27(1), 113-118.
choose leaders who put people first” and “It’s time for unity and             [3] Hohenstein, J., Kizilcec, R.F., DiFranzo, D. et al. Artificial intelligence in
leadership that puts America first” introduce clear calls to action,              communication impacts language and social relationships. Sci Rep 13, 5487
offering tangible next steps for the audience. This forward-                      (2023). https://doi.org/10.1038/s41598-023-30938-9.
looking approach contrasts with the human-authored tweets,                    [4] Lindsey Barrett, L. M., MacCarthy, M., Wheeler, T., Nicol Turner Lee, D. V.,
                                                                                  Darrell M. West, N. T. L., & Schacht, L. P. (2024, July 25). How tech platforms
which primarily focus on describing current issues without                        fuel U.S. political polarization and what government can do about it.
explicitly proposing solutions.                                                   Brookings. https://www.brookings.edu/articles/how-tech-platforms-fuel-u-s-
                                                                                  political-polarization-and-what-government-can-do-about-it/
                                                                              [5] Thurlow, C., Lengel, L., & Tomic, A. (2004). Computer mediated
3 Ethical Considerations                                                          communication. Sage.
   During the manual inspection of the AI's responses to                      [6] Kenneth C. Arnold, Krysta Chauncey, and Krzysztof Z. Gajos. 2020. Predictive
prompts requesting tweet improvements, the system declined to                     text encourages predictable writing. In Proceedings of the 25th International
                                                                                  Conference on Intelligent User Interfaces (IUI '20). Association for Computing
assist with politically sensitive content, stating, "I'm sorry, but I             Machinery,           New          York,           NY,       USA,         128–138.
can't assist with content aimed at influencing political opinions                 https://doi.org/10.1145/3377325.3377523
or actions. Let me know if there's anything else I can help with."            [7] Hohenstein, J. & Jung, M. AI-supported messaging: an investigation of human-
                                                                                  human text conversation with AI support. In Extended Abstracts of the 2018
This response reflects an intentional boundary set by the AI to                   CHI Conference on Human Factors in Computing Systems - CHI ’18,
avoid engaging in activities that could amplify bias, spread                      https://doi.org/10.1145/3170427.3188487 (2018).
misinformation, or influence political narratives. While this                 [8] Shin, D., Park, S., Kim, E. H., Kim, S., Seo, J., & Hong, H. (2022). Exploring the
approach aligns with ethical principles of neutrality and                         Effects of AI-assisted Emotional Support Processes in Online Mental Health
                                                                                  Community. arXiv preprint arXiv:2202.10065.
responsible AI use, it raises questions about AI's capacity to
provide nuanced engagement with complex political topics.


--- page break ---

Detecting Effects of AI-Mediated Communication on Language
                                                                                                       WWW Companion '25, April 28-May 2, 2025, Sydney, NSW, Australia
Complexity and Sentiment

[9] Wu, T., He, S., Liu, J., Sun, S., Liu, K., Han, Q.-L., & Tang, Y. (2023). A brief   [12] Kincaid, J. P., Fishburne, Jr., Robert P., R., Richard L., C., & Brad S. (1975).
     overview of CHATGPT: The history, status quo and potential future                       Derivation of New Readability Formulas (Automated Readability Index, Fog
     development. IEEE/CAA Journal of Automatica Sinica, 10(5), 1122–1136.                   Count and Flesch Reading Ease Formula) for Navy Enlisted Personnel.
     https://doi.org/10.1109/jas.2023.123618                                                 https://doi.org/10.21236/ada006655
[10] Alam, Md. S., Asmawi, A., Haque, M., Patwary, Md., Ullah, Md. M., & Fatema,        [13] Schulhoff, S., Ilie, M., Balepur, N., Kahadze, K., Liu, A., Si, C., ... & Resnik, P.
     S. (2023). Distinguishing between Student-Authored and CHATGPT-Generated                (2024). The Prompt Report: A Systematic Survey of Prompting Techniques.
     Texts: A Preliminary Exploration of Human-Evaluation Techniques.                        arXiv preprint arXiv:2406.06608.
     https://doi.org/10.2139/ssrn.4591759
[11] Flesch, R. (1948). A new readability yardstick. Journal of Applied Psychology,
     32(3), 221–233. https://doi.org/10.1037/h0057532


--- page break ---

## Extraction verification

- **Beginning checked:** Rendered page 1 was compared with the extraction from the title and author block through the abstract, ACM citation, introduction, and opening of related work; the paper identifies the same title, authors, DOI, 2020 and 2024 sample sizes, abstract percentages, and five-page proceedings extent.
- **Middle checked:** Rendered pages 2 and 3 were compared with the extraction across data sources, methods, Figure 1, readability results, Figure 2, polarity distributions, Figure 3, manual-inspection method, and the opening of the first original/rewrite pair. Figure 1 visibly contains separate Flesch-Kincaid and polarity panels although its caption names only Flesch-Kincaid; its readability x-axis ends around 30, so the text's stated maxima of 50.9 and 575.2 are not visible in that plot. The remaining displayed captions, statistics, prompt, and text align with the extraction.
- **End checked:** Rendered page 5 was compared with the extraction through references 9-13; the final reference entries and page ending align, with no continuation or appendix after reference 13.
- **Structure checked:** Five PDF pages, 3 figures, abstract, sections 1, 1.1, 2, 2.2.1, 2.2.2, 2.3, 2.3.1, 2.3.2, 2.4, 3, 3.1, 3.2, and 13 references. The PDF contains no appendix, footnote section, supplementary file, or separate endnotes.
- **Known omissions:** None from the source record. The Markdown body does not reproduce figure pixels or red font colour; the complete authoritative PDF is preserved below.

## Preserved attachments

| Path | Role in the source | SHA-256 | Preservation / extraction notes |
|---|---|---|---|
| `snapshots/attachments/sussman-carter-ai-mediated-communication-arxiv-2504.19556v1.pdf` | Authoritative five-page arXiv v1 PDF containing the complete paper, figures, colour highlighting, and references | `893ee1a413f1f8f3ccc844c89433b4ee3188bf3a82122c2eeb7096b0a80a112b` | Exact bytes downloaded from the official arXiv PDF route on 2026-07-17. This digest matches the PDF SHA-256 recorded in the prior 2026-07-14 snapshot. Complete embedded text extracted with `pdftotext -layout`; pages 1, 2, 3, and 5 rendered and checked visually. |
