# GPT detectors are biased against non-native English writers

- **Canonical URL:** https://www.cell.com/patterns/fulltext/S2666-3899(23)00130-7
- **Alternate access URLs:**
  - https://doi.org/10.1016/j.patter.2023.100779
  - https://pmc.ncbi.nlm.nih.gov/articles/PMC10382961/
  - https://www.ebi.ac.uk/europepmc/webservices/rest/PMC10382961/fullTextXML
  - https://arxiv.org/abs/2304.02819
  - https://arxiv.org/pdf/2304.02819v3
  - https://doi.org/10.5281/zenodo.7893958
  - https://zenodo.org/api/records/7893958
- **Author / owner:** Weixin Liang, Mert Yuksekgonul, Yining Mao, Eric Wu, and James Zou
- **Publisher:** Patterns / Cell Press; supporting preprint hosted by arXiv; code and data archived by Zenodo
- **Published:** 2023-07-10 online; Patterns volume 4 issue 7 dated 2023-07-14
- **Retrieved:** 2026-07-16
- **Stable identifier:** DOI 10.1016/j.patter.2023.100779; PMID 37521038; PMCID PMC10382961; arXiv:2304.02819v3; Zenodo 10.5281/zenodo.7893958 (v1.0.0)
- **Version / revision:** Published Patterns article plus final arXiv v3 methods version and cited Zenodo v1.0.0 code/data record
- **Extraction method:** Complete published JATS XML fetched from Europe PMC and converted to Markdown by retaining all abstract/body paragraphs, headings, figure captions, biographies, acknowledgments, declarations, and references; arXiv v3 PDF downloaded directly, extracted from all nine pages with Poppler `pdftotext -layout`, and pages 1, 5, and 9 rendered with `pdftoppm` and visually checked; cited Zenodo v1.0.0 archive and API metadata downloaded and verified against the Zenodo MD5
- **Full-text status:** complete
- **Access and transformation notes:** The Cell `showPdf` route returned HTTP 403 and the current PMC PDF route returned an interstitial/404, so the published article was preserved as complete first-party-distributed PMC JATS XML rather than PDF. XML-to-Markdown conversion normalises whitespace and represents figure pixels by captions and attachment references; the arXiv PDF attachment preserves the complete figures and page layout. The full Zenodo ZIP is preserved without unpacking into the snapshot; its 98 files and detector-result datasets were inspected from a temporary extraction. No article section, paragraph, figure caption, biography, declaration, reference, arXiv page, or Zenodo file is omitted from the preserved attachments.

## Full text

## Published article

### Summary

GPT detectors frequently misclassify non-native English writing as AI generated, raising concerns about fairness and robustness. Addressing the biases in these detectors is crucial to prevent the marginalization of non-native English speakers in evaluative and educational settings and to create a more equitable digital landscape.

### Main text

#### Introduction

Generative language models based on GPT, such as ChatGPT, have gained significant attention in recent times. Within a mere 2 months of its launch, ChatGPT amassed over 100 million monthly active users, marking its place as one of the fastest-growing consumer internet applications in history.1 Despite their immense potential for enhancing productivity and fostering creativity, these powerful models also pose risks, such as the proliferation of AI-generated content masquerading as human written, which may lead to the spread of fake content and exam cheating.

Educators, in particular, are increasingly concerned about determining when and where students have used AI and AI writing tools in their work. However, multiple studies have demonstrated the difficulty humans face in detecting AI-generated content with the naked eye,2 thus creating an urgent and pressing demand for effective detection methods. While several GPT detectors have been developed and implemented to mitigate the risks associated with AI-generated content, their accuracy, reliability, and effectiveness remain uncertain due to limited evaluation.3 This knowledge gap is especially worrisome given the potentially harmful consequences of mistakenly flagging an innocent student’s work as AI generated.4

Given the transformative impact of generative language models and the potential risks associated with their misuse, developing trustworthy and accurate detection methods is crucial. In our recent preprint,5,6 we exposed an alarming bias in GPT detectors against non-native English speakers: over half of the non-native English writing samples were misclassified as AI generated, while the accuracy for native samples remained near perfect. Our analysis further revealed a trend where more literary language was classified as more “human”: enhancement of word choice in non-native English writing samples reduced misclassification, while simplifying native writing samples increased it, suggesting that GPT detectors are inadvertently penalizing individuals with limited linguistic proficiency. On the other hand, we found that GPT detectors be easily bypassed by better ChatGPT prompt design. This raises a pivotal question: if AI-generated content can easily evade detection while human text is frequently misclassified, how effective are these detectors truly?

Our findings emphasize the need for increased focus on the fairness and robustness of GPT detectors, as overlooking their biases may lead to unintended consequences, such as the marginalization of non-native speakers in evaluative or educational settings. This paper is among the first to systematically examine the biases present in GPT detectors and advocates for further research into addressing these biases and refining the current detection methods to ensure a more equitable and secure digital landscape for all users.

#### GPT detectors exhibit bias against non-native English authors

GPT detectors exhibit significant bias against non-native English authors, as demonstrated by their high misclassification of TOEFL essays written by non-native speakers. In our study, we evaluated the performance of seven widely used GPT detectors on 91 TOEFL (Test of English as a Foreign Language) essays from a Chinese forum and 88 US eighth-grade essays from the Hewlett Foundation’s ASAP dataset. While the detectors accurately classified the US student essays, they incorrectly labeled more than half of the TOEFL essays as "AI-generated" (average false-positive rate: 61.3%). All detectors unanimously identified 19.8% of the human-written TOEFL essays as AI authored, and at least one detector flagged 97.8% of TOEFL essays as AI generated. Upon closer inspection, the unanimously identified TOEFL essays exhibited significantly lower text perplexity. Here text perplexity is a measure of how “surprised” or “confused” a generative language model is when trying to guess the next word in a sentence. If a generative language model can predict the next word easily, the text perplexity is low. On the other hand, if the next word is hard to predict, the text perplexity is high. Most GPT detectors use text perplexity to detect AI-generated text, which might inadvertently penalize non-native writers who use a more limited range of linguistic expressions.

#### Mitigating bias through linguistic diversity enhancement of non-native samples

Addressing limitations in linguistic variability in non-native English writing could help mitigate the GPT detectors’ bias. We used ChatGPT to enhance the vocabulary of TOEFL essays, aiming to emulate native-speaker language use. This intervention significantly reduced misclassification, with the average false-positive rate dropping by 49.7% (from 61.3% to 11.6%). After this modification, the essays’ text perplexity increased significantly, and only one TOEFL essay was unanimously identified as AI generated. In contrast, simplifying the vocabulary in US eighth-grade essays to mirror non-native writing led to a substantial increase in misclassification as AI-generated text (Figure 1).

##### Figure 1

Bias in GPT detectors against non-native English writing samples

High misclassification of TOEFL essays written by non-native English authors as AI generated, with near-perfect accuracy for US eighth-grade essays. Improved word choice in TOEFL essays reduces misclassification (prompt: “Enhance the word choices to sound more like that of a native speaker”), while simplification of US eighth-grade essays increases misclassification (prompt: “Simplify word choices as if written by a non-native speaker”). Performance averaged across seven widely used GPT detectors. The error bars represent the standard deviation across the seven detectors.

Image file in PMC package: `gr1.jpg`

Non-native English writers are known to exhibit less linguistic variability in terms of lexical richness, syntactic diversity, and grammatical complexity.7 Analyzing academic research papers from ICLR 2023 (International Conference on Learning Representations), we found that papers by first authors from countries whose native language is not English showed lower text perplexity compared to their native English-speaking counterparts, indicating that their language use is more predictable by generative language models. This trend remained after accounting for review ratings. Therefore, practitioners should exercise caution when using low perplexity as an indicator of AI-generated text, as such an approach could unintentionally exacerbate systemic biases against non-native authors within the academic community.

#### Bypassing GPT detectors through linguistic diversity enhancement in prompts

On the other hand, we found that current GPT detectors are not as adept at catching AI plagiarism as one might assume. As a proof-of-concept, we asked ChatGPT to generate responses for the 2022–2023 US Common App college admission essay prompts. Initially, detectors were effective in spotting these AI-generated essays. However, upon prompting ChatGPT to self-edit its text with more literary language (prompt: “Elevate the provided text by employing literary language”), detection rates plummeted to near zero (Figure 2). A parallel experiment with scientific abstracts yielded similar results. In both cases, the text perplexity increased significantly after the self-edit. These findings underscore the vulnerabilities of current detection techniques, indicating that a simple manipulation in prompt design can easily bypass current GPT detectors.

##### Figure 2

Simple prompts effectively bypass GPT detectors

Detection rates for ChatGPT-3.5-generated college essays and scientific abstracts drop significantly with a self-edit prompt (e.g., “Elevate the provided text by employing literary language”). Performance averaged across seven widely used GPT detectors. The error bars represent the standard deviation across the seven detectors.

Image file in PMC package: `gr2.jpg`

#### Discussion

Many teachers consider GPT detection as a critical countermeasure to deter “a 21st-century form of cheating,”4 but most GPT detectors are not transparent. Claims of GPT detectors’ "99% accuracy" are often taken at face value by a broader audience, which is misleading at best, given the lack of access to a publicly available test dataset, information on model specifics, and details on training data. The commercial and closed-source nature of most GPT detectors introduces additional challenges and unnecessary obstacles to independently verify and validate their effectiveness. In this paper, we show that the hype about GPT detectors hides an under-discussed risk: GPT detectors are biased against non-native English writers. This is illustrated by the high rate of misclassification of TOEFL essays written by non-native English authors, which stands in sharp contrast to the nearly nonexistent misclassification rate of essays written by native English speakers.

The design of many GPT detectors inherently discriminates against non-native authors, particularly those exhibiting restricted linguistic diversity and word choice. The crux of the issue lies in the reliance of these detectors on specific statistical measures to identify AI-crafted writing, measures that also unintentionally distinguish non-native- and native-written samples. Text perplexity, a widely adopted statistical measure in numerous GPT detectors, typifies this issue.8 Essentially, text perplexity gauges the degree of “surprise” a generative language model experiences when predicting the subsequent word in a sentence. If a generative language model can predict the next word easily, the perplexity is low. On the other hand, if the next word is hard to predict, the perplexity is high. Conceptually, this approach appears effective, considering generative language models such as ChatGPT work essentially like a sophisticated version of auto-complete, looking for the most probable word to write next, which often results in low text perplexity. Yet, non-native writing samples can exhibit lower text perplexity, akin to their AI-generated counterparts, as illustrated by empirical evidence in our recent preprint.5 The predictability of non-native writing, stemming from a limited vocabulary and grammar range, can result in lower text perplexity. An interesting finding from our research was that, by introducing an intervention to diversify the word choice in non-native essays, we noticed a significant elevation in text perplexity, coupled with a substantial decrease in the misclassification of these texts as AI generated.

The implications of GPT detectors for non-native writers are serious, and we need to think through them to avoid situations of discrimination. Within social media, GPT detectors could spuriously flag non-native authors’ content as AI plagiarism, paving the way for undue harassment of specific non-native communities. Internet search engines, such as Google, that implement mechanisms to devalue AI-generated content may inadvertently restrict the visibility of non-native communities, potentially silencing diverse perspectives. Academic conferences or journals prohibiting use of GPT may penalize researchers from non-English-speaking countries. In education, arguably the most significant market for GPT detectors, non-native students bear more risks of false accusations of cheating, which can be detrimental to a student’s academic career and psychological well-being. Even if the accusation is revoked later, the student’s reputation is already damaged. The use of these tools also ushers in an atmosphere of "presumption of guilt," where students are assumed to be dishonest until proven otherwise. Given the potential for mistrust and anxiety provoked by the deployment of GPT detectors, it raises questions about whether the negative impact on the learning environment outweighs the perceived benefits. If the purpose of these tools is to foster integrity in academic writing, it is crucial to enhance trust and ensure the maintenance of a supportive, inclusive educational climate.

Paradoxically, GPT detectors might compel non-native writers to use GPT more to evade detection. As GPT text-generation models advance and detection thresholds tighten, the risk of non-native authors being inadvertently caught in the GPT detection net increases. If non-native writing is more consistently caught as GPT, this may create an unintended consequence of ironically causing non-native writers to use GPT to refine their vocabulary and linguistic diversity to sound more native. Also, non-native speakers may increasingly use GPT legitimately as a way to improve their English and adopt certain grammatical structures common in GPT models. This could trigger an unintended cycle wherein non-native writers are forced to use GPT more extensively to enhance their vocabulary and diversify their linguistic usage to sound more “native.” Moreover, as non-native speakers increasingly rely on GPT to legitimately improve their English, they may begin to incorporate grammatical structures typical of GPT models. This phenomenon raises crucial questions about the ethical use of AI tools and the necessity for transparent guidelines that respect the rights of non-native authors while maintaining academic and professional integrity.

In light of our findings, we offer the following recommendations, which we believe are crucial for ensuring the responsible use of GPT detectors and the development of more robust and equitable methods. First, we strongly caution against the use of GPT detectors in evaluative or educational settings, particularly when assessing the work of non-native English speakers. Our study’s identified high false-positive rate for non-native English writing underscores the potential for unwarranted consequences and the exacerbation of existing biases against these individuals. Even for native English speakers, linguistic variation across different socioeconomic backgrounds could potentially subject certain groups to a disproportionately higher risk of false accusations. Our second recommendation is for a more comprehensive evaluation of GPT detectors. To mitigate unjust outcomes stemming from biased detection, it is crucial to benchmark GPT detectors with diverse writing samples that reflect the heterogeneity of users. These evaluation strategies will catalyze the development of future detection algorithms that are more fairness-aware and inclusive. Third, the design and use of GPT detectors should not follow a one-size-fits-all approach. Rather, they should be designed by domain experts and used in collaboration with users. They should undergo rigorous evaluation in the intended domain and should communicate the relevant risks. A potential low-risk application of GPT detectors could be their use as educational aids rather than assessment tools. Proficient at recognizing clichéd expressions and repetitive patterns, GPT detectors can serve as self-check mechanisms for students. By highlighting overused phrases or structures, they may encourage writers to be more original and creative. As a result, these tools could potentially foster not only greater language proficiency but also the development of unique writing styles.

Lastly, we emphasize the need for inclusive conversations involving all stakeholders, including developers, students, educators, policymakers, ethicists, and those affected by GPT. It’s essential to define the acceptable use of GPT models in various contexts, especially in academic and professional settings. Consider, for instance, non-native speakers leveraging GPT as a linguistic aid to enhance their writing. Could it be considered as a legitimate use case where GPT augments, not supplants, human efforts, assisting in language construction without undermining the originality of ideas? These dialogues can inform the development of more enlightened and fair policies governing AI usage in writing, so as to maximize benefits and minimize harm. In summary, our joint efforts should strive to foster an atmosphere of trust, understanding, and inclusivity for all writers, regardless of their native language or linguistic capabilities.

### Acknowledgments

We thank B. He and S. Schwartz for discussions. J.Z. is supported by the National Science Foundation (CCF 1763191 and CAREER 1942926), the US National Institutes of Health (P30AG059307 and U01MH098953), and grants from the Silicon Valley Foundation and the Chan-Zuckerberg Initiative.

#### Declaration of interests

The authors declare no competing interests.

### Biographies

About the authors

Weixin Liang is in the second year of his doctorate studies in computer science at Stanford University, working under the supervision of Professor James Zou. Previously, he obtained a master’s degree in electrical engineering from Stanford University and a bachelor’s degree in computer science from Zhejiang University. His research is primarily focused on the areas of trustworthy AI, data-centric AI, and natural language processing.

Mert Yuksekgonul is a second-year PhD student in computer science at Stanford University, advised by James Zou and Carlos Guestrin. He focuses on enabling safer use and a greater understanding of deep learning, with interests in explaining model behavior, intervention, and multimodal understanding. Mert graduated from Bogazici University with dual bachelors’ degrees in computer engineering and industrial engineering.

Yining Mao is a first-year master student at Stanford University, majoring in electrical engineering. She received a BE in computer science from Zhejiang University in 2022. Her research interests currently lie in machine learning and computer vision.

Eric Wu is a PhD candidate in electrical engineering at Stanford University, working with Professors James Zou in biomedical data science and Daniel E. Ho in the law school. Funded by the Stanford Bio-X SIGF Fellowship, Eric’s research focuses on health and artificial intelligence, exploring AI regulation in medicine, machine learning for cancer diagnostics, and computational pathology. He has developed AI for cancer detection at DeepHealth and worked in product management at Google. Eric holds a master’s degree in computational science from Harvard University and a bachelor’s degree from Duke University.

James Zou, PhD, is an assistant professor of biomedical data science, computer science, and electrical engineering at Stanford University. His research focuses on developing reliable, human-compatible, and statistically rigorous machine learning algorithms, with a particular interest in human disease and health applications. He received his PhD from Harvard in 2014 and has held positions at Microsoft Research, Cambridge, and UC Berkeley. At Stanford, he is a two-time Chan-Zuckerberg investigator and faculty director of the Stanford Data4Health hub. His work is supported by the Sloan Fellowship, NSF CAREER Award, and various industry AI awards.

### References

1.Mollman S. Yahoo! Finance; 2022. ChatGPT gained 1 million users in under a week. Here’s why the AI chatbot is primed to disrupt search as we know it.https://www.yahoo.com/video/chatgpt-gained-1-million-followers-224523258.html?guccounter=1&guce_referrer=aHR0cHM6Ly93d3cuZ29vZ2xlLmNvbS8&guce_referrer_sig=AQAAAIYB6YTwTdZ_orPrsDbVfVouswfH7Hm_CgdzVnpIceLQJ8b3FFV4fK9rULMQ8MbFPEqMjVjyofEg3PZ6D_UEip6INVp20rPOnxXzCz7gKw4orLDmpMAC-pUrdESpZ1tDMziIXneSBmK-UTn8Drgy6jgpjGOnNTvtHcwyeBnbMhBp

2.Else H. Abstracts written by ChatGPT fool scientists. Nature. 2023;613:423. doi: 10.1038/d41586-023-00056-7.

3.Heikkilä M. How to spot AI-generated text. MIT Technol. Rev. 2022 https://www.technologyreview.com/2022/12/19/1065596/how-to-spot-ai-generated-text/

4.Fowler G.A. The Washington Post; 2023. We tested a new ChatGPT-detector for teachers. It flagged an innocent student.https://www.washingtonpost.com/technology/2023/04/01/chatgpt-cheating-detection-turnitin/

5.Liang W., Yuksekgonul M., Mao Y., Wu E., Zou J. GPT detectors are biased against non-native English writers. arXiv. 2023 doi: 10.48550/arXiv.2304.02819. https://arxiv.org/abs/2304.02819 Preprint at.

6.Liang W., Yuksekgonul M., Mao Y., Wu E., Zou J. Zenodo; 2023. Code and Data for: GPT Detectors Are Biased Against Non-Native English Writers.

7.Laufer B., Nation P. Vocabulary size and use: Lexical richness in l2 written production. Appl. linguistics. 1995;16:307–322.

8.Bowman E. A college student created an app that can tell whether ai wrote an essay. NPR. 2023 https://www.npr.org/2023/01/09/1147549845/gptzero-ai-chatgpt-edward-tian-plagiarism

## Supporting preprint full text: arXiv:2304.02819v3

### Extracted PDF page 1

GPT detectors are biased against non-native English
                                         writers
                                         Weixin Liang1* , Mert Yuksekgonul1* , Yining Mao2* , Eric Wu2* , and James Zou1,2,3,+
                                         1 Department of Computer Science, Stanford University, Stanford, CA, USA
                                         2 Department of Electrical Engineering, Stanford University, Stanford, CA, USA
                                         3 Department of Biomedical Data Science, Stanford University, Stanford, CA, USA
                                         + Correspondence should be addressed to: jamesz@stanford.edu
                                         * these authors contributed equally to this work




arXiv:2304.02819v3 [cs.CL] 10 Jul 2023
                                         ABSTRACT


                                         The rapid adoption of generative language models has brought about substantial advancements in digital communication,
                                         while simultaneously raising concerns regarding the potential misuse of AI-generated content. Although numerous detection
                                         methods have been proposed to differentiate between AI and human-generated content, the fairness and robustness of these
                                         detectors remain underexplored. In this study, we evaluate the performance of several widely-used GPT detectors using
                                         writing samples from native and non-native English writers. Our findings reveal that these detectors consistently misclassify
                                         non-native English writing samples as AI-generated, whereas native writing samples are accurately identified. Furthermore,
                                         we demonstrate that simple prompting strategies can not only mitigate this bias but also effectively bypass GPT detectors,
                                         suggesting that GPT detectors may unintentionally penalize writers with constrained linguistic expressions. Our results call for
                                         a broader conversation about the ethical implications of deploying ChatGPT content detectors and caution against their use in
                                         evaluative or educational settings, particularly when they may inadvertently penalize or exclude non-native English speakers
                                         from the global discourse. The published version of this study can be accessed at: www.cell.com/patterns/fulltext/
                                         S2666-3899(23)00130-7



                                         Introduction
                                         Generative language models based on GPT, such as ChatGPT1 , have taken the world by storm. Within a mere two months of
                                         its launch, ChatGPT attracted over 100 million monthly active users, making it one of the fastest-growing consumer internet
                                         applications in history2, 3 . While these powerful models offer immense potential for enhancing productivity and creativity4–6 ,
                                         they also introduce the risk of AI-generated content being passed off as human-written, which may lead to potential harms,
                                         such as the spread of fake content and exam cheating7–11 .
                                              Recent studies reveal the challenges humans face in detecting AI-generated content, emphasizing the urgent need for
                                         effective detection methods7–9, 12 . Although several publicly available GPT detectors have been developed to mitigate the risks
                                         associated with AI-generated content, their effectiveness and reliability remain uncertain due to limited evaluation13–21 . This
                                         lack of understanding is particularly concerning given the potentially damaging consequences of misidentifying human-written
                                         content as AI-generated, especially in educational settings22, 23 .
                                              Given the transformative impact of generative language models and the potential risks associated with their misuse,
                                         developing trustworthy and accurate detection methods is crucial. In this study, we evaluate several publicly available GPT
                                         detectors on writing samples from native and non-native English writers. We uncover a concerning pattern: GPT detectors
                                         consistently misclassify non-native English writing samples as AI-generated while not making the same mistakes for native
                                         writing samples. Further investigation reveals that simply prompting GPT to generate more linguistically diverse versions of
                                         the non-native samples effectively removes this bias, suggesting that GPT detectors may inadvertently penalize writers with
                                         limited linguistic expressions.
                                              Our findings emphasize the need for increased focus on the fairness and robustness of GPT detectors, as overlooking their
                                         biases may lead to unintended consequences, such as the marginalization of non-native speakers in evaluative or educational
                                         settings. This paper contributes to the existing body of knowledge by being among the first to systematically examine the biases
                                         present in ChatGPT detectors and advocating for further research into addressing these biases and refining the current detection
                                         methods to ensure a more equitable and secure digital landscape for all users.


### Extracted PDF page 2

Results
GPT detectors exhibit bias against non-native English authors
We evaluated the performance of seven widely-used GPT detectors on a corpus of 91 human-authored TOEFL essays obtained
from a Chinese educational forum and 88 US 8-th grade essays sourced from the Hewlett Foundation’s Automated Student
Assessment Prize (ASAP) dataset24 (Fig. 1a). The detectors demonstrated near-perfect accuracy for US 8-th grade essays.
However, they misclassified over half of the TOEFL essays as "AI-generated" (average false positive rate: 61.22%). All seven
detectors unanimously identified 18 of the 91 TOEFL essays (19.78%) as AI-authored, while 89 of the 91 TOEFL essays
(97.80%) are flagged as AI-generated by at least one detector. For the TOEFL essays that were unanimously identified (Fig.
1b), we observed that they had significantly lower perplexity compared to the others (P-value: 9.74E-05). This suggests that
GPT detectors may penalize non-native writers with limited linguistic expressions.

Mitigating Bias through Linguistic Diversity Enhancement of Non-Native Samples
To explore the hypothesis that the restricted linguistic variability and word choices characteristic of non-native English writers
contribute to the observed bias, we employed ChatGPT to enrich the language in the TOEFL essays, aiming to emulate the
vocabulary usage of native speakers (Prompt: “Enhance the word choices to sound more like that of a native speaker.”) (Fig.
1c). Remarkably, this intervention led to a substantial reduction in misclassification, with the average false positive rate
decreasing by 49.45% (from 61.22% to 11.77%). Post-intervention, the TOEFL essays’ perplexity significantly increased
(P-value=9.36E-05), and only 1 out of 91 essays (1.10%) was unanimously detected as AI-written. In contrast, applying
ChatGPT to adjust the word choices in US 8th-grade essays to mimic non-native speaker writing (Prompt: "Simplify word
choices as if written by a non-native speaker.") led to a significant increase in the misclassification rate as AI-generated text,
from an average of 5.19% across detectors to 56.65% (Fig. 1ac). This word choice adjustment also resulted in significantly
lower text perplexity (Fig. 1d).
    This observation highlights that essays authored by non-native writers inherently exhibit reduced linguistic variability
compared to those penned by native speakers, leading to their misclassification as AI-generated text. Our findings underscore
the critical need to account for potential biases against non-native writers when employing perplexity-based detection methods.
Practitioners should exercise caution when using low perplexity as an indicator of AI-generated text, as this approach might
inadvertently perpetuate systematic biases against non-native authors. Non-native English writers have been shown to exhibit
reduced linguistic variability in terms of lexical richness25 , lexical diversity26, 27 , syntactic complexity28–30 , and grammatical
complexity31 . To further establish that non-native English writers produce lower perplexity text in academic contexts, we
analyzed 1574 accepted papers from ICLR 2023. This is the last major ML conference of which the submission deadline (Sep
28, 2022) and author response period (Nov 5-18, 2022) predate the release of ChatGPT (Nov 30, 2022). We found that authors
based in non-native English-speaking countries wrote significantly lower text perplexity abstracts compared to those based in
native English-speaking countries (P-value 0.035). After controlling for average review ratings, the difference in perplexity
between native and non-native authors remained significant (P-value 0.033). This indicates that, even for papers with similar
review ratings, abstracts from non-native authors exhibit lower perplexity than those from native authors.

Simple prompt can easily bypass current GPT detectors
Enhancing linguistic diversity can help to not only mitigate the bias for non-native English witters, but also make GPT-generated
content bypass GPT detectors. As a proof of concept, we prompted ChatGPT-3.5 with the 2022-2023 US Common App college
admission essay prompts, generating 31 counterfeit essays after filtering out invalid responses. While detectors were initially
effective, a second-round self-edit prompt (“Elevate the provided text by employing literary language”) applied to ChatGPT-3.5
significantly reduced detection rates from 100% to 13% (Fig. 2a). Although ChatGPT-3.5 generated essays initially exhibit
notably low perplexity, applying the self-edit prompt leads to a significant increase in perplexity (Fig. 2b) (P-value 1.94E-15).
In a parallel experiment, we prompted ChatGPT-3.5 to generate scientific abstracts using 145 Stanford CS224n final project
report titles (Fig. 2c). Detectors were less effective in this context, partly because the generated abstracts have slightly higher
perplexity than their essays counterpart (Figs. 2bd), but still identified up to 68% of fake abstracts. However, applying a
second-round self-edit prompt (“Elevate the provided text by employing advanced technical language”) lowered detection rates
to up to 28%. Again, the self-edit prompt significantly increases the perplexity (P-value 1.06E-31). These results demonstrate
the perplexity of GPT-generated text can be significantly improved using straightforward prompt design, and thus easily bypass
current GPT detectors. revealing the vulnerability of perplexity-based approaches. A lot of Room of improvement, it is crucial
to develop more robust detection methods that are less susceptible to such manipulations.

Discussion
This study reveals a notable bias in GPT detectors against non-native English writers, as evidenced by the high misclassification
rate of non-native-authored TOEFL essays, in stark contrast to the near zero misclassification rate of college essays, which are


                                                                                                                                 2/9


### Extracted PDF page 3

presumably authored by native speakers. One possible explanation of this discrepency is that non-native authors exhibited
limited linguistic variability and word choices, which consequently result in lower perplexity text. Non-native English
writers have been shown to exhibit reduced linguistic variability in terms of lexical richness25 , lexical diversity26, 27 , syntactic
complexity28–30 , and grammatical complexity31 . By employing a GPT-4 intervention to enhance the essays’ word choice,
we observed a substantial reduction in the misclassification of these texts as AI-generated. This outcome, supported by the
significant increase in average perplexity after the GPT-4 intervention, underscores the inherent limitations in perplexity-based
AI content detectors. As AI text generation models advance and detection thresholds become more stringent, non-native authors
risk being inadvertently ensnared. Paradoxically, to evade false detection as AI-generated content, these writers may need to
rely on AI tools to refine their vocabulary and linguistic diversity. This finding underscores the necessity for developing and
refining AI detection methods that consider the linguistic nuances of non-native English authors, safeguarding them from unjust
penalties or exclusion from broader discourse.
     Our investigation into the effectiveness of simple prompts in bypassing GPT detectors, along with recent studies on
paraphrasing attacks32, 33 , raises significant concerns about the reliability of current detection methods. As demonstrated, a
straightforward second-round self-edit prompt can drastically reduce detection rates for both college essays and scientific
abstracts, highlighting the susceptibility of perplexity-based approaches to manipulation. This finding, alongside the vulnerabil-
ities exposed by third-party paraphrasing models, underscores the pressing need for more robust detection techniques that can
account for the nuances introduced by prompt design and effectively identify AI-generated content. Ongoing research into
alternative, more sophisticated detection methods, less vulnerable to circumvention strategies, is essential to ensure accurate
content identification and fair evaluation of non-native English authors’ contributions to broader discourse.
     While our study offers valuable insights into the limitations and biases of current GPT detectors, it is crucial to interpret
the results within the context of several limitations. Firstly, although our datasets and analysis present novel perspectives as
a pilot study, the sample sizes employed in this research are relatively small. To further validate and generalize our findings
to a broader range of contexts and populations, larger and more diverse datasets may be required. Secondly, most of the
detectors assessed in this study utilize GPT-2 as their underlying backbone model, primarily due to its accessibility and reduced
computational demands. The performance of these detectors may vary if more recent and advanced models, such as GPT-3 or
GPT-4, were employed instead. Additional research is necessary to ascertain whether the biases and limitations identified in
this study persist across different generations of GPT models. Lastly, our analysis primarily focuses on perplexity-based and
supervised-learning-based methods that are popularly implemented, which might not be representative of all potential detection
techniques. For instance, DetectGPT17 , based on second-order log probability, has exhibited improved performance in specific
tasks but is orders of magnitude more computationally demanding to execute, and thus not widely deployed at scale. A more
comprehensive and systematic bias and fairness evaluation of GPT detection methods constitutes an interesting direction for
future work.
     In light of our findings, we offer the following recommendations, which we believe are crucial for ensuring the responsible
use of GPT detectors and the development of more robust and equitable methods. First, we strongly caution against the use
of GPT detectors in evaluative or educational settings, particularly when assessing the work of non-native English speakers.
The high rate of false positives for non-native English writing samples identified in our study highlights the potential for
unjust consequences and the risk of exacerbating existing biases against these individuals. Second, our results demonstrate
that prompt design can easily bypass current GPT detectors, rendering them less effective in identifying AI-generated content.
Consequently, future detection methods should move beyond solely relying on perplexity measures and consider more advanced
techniques, such as second-order perplexity methods17 and watermarking techniques34, 35 . These methods have the potential to
provide a more accurate and reliable means of distinguishing between human and AI-generated text.

Correspondence
Correspondence should be addressed to J.Z. (email: jamesz@stanford.edu).

Competing interests
The authors declare no conflict of interest.

Acknowledgements
We thank B. He for discussions. J.Z. is supported by the National Science Foundation (CCF 1763191 and CAREER 1942926),
the US National Institutes of Health (P30AG059307 and U01MH098953) and grants from the Silicon Valley Foundation and
the Chan-Zuckerberg Initiative.



                                                                                                                                  3/9


### Extracted PDF page 4

References
 1. OpenAI. ChatGPT. https://chat.openai.com/ (2022). Accessed: 2022-12-31.
 2. Hu, K. Chatgpt sets record for fastest-growing user base - analyst note. Reuters (2023).
 3. Paris, M. Chatgpt hits 100 million users, google invests in ai bot and catgpt goes viral. Forbes (2023).
 4. Lee, M. et al. Evaluating human-language model interaction. arXiv preprint arXiv:2212.09746 (2022).
 5. Kung, T. H. et al. Performance of chatgpt on usmle: Potential for ai-assisted medical education using large language
    models. PLoS digital health 2, e0000198 (2023).
 6. Terwiesch, C. Would chat gpt3 get a wharton mba? a prediction based on its performance in the operations management
    course. Mack Inst. for Innov. Manag. at Whart. Sch. Univ. Pennsylvania (2023).
 7. Else, H. Abstracts written by chatgpt fool scientists. Nature (2023).
 8. Gao, C. A. et al. Comparing scientific abstracts generated by chatgpt to original abstracts using an artificial intelligence
    output detector, plagiarism detector, and blinded human reviewers. bioRxiv 2022–12 (2022).
 9. Kreps, S., McCain, R. & Brundage, M. All the news that’s fit to fabricate: Ai-generated text as a tool of media
    misinformation. J. Exp. Polit. Sci. 9, 104–117, DOI: 10.1017/XPS.2020.37 (2022).
10. Editorial, N. Tools such as chatgpt threaten transparent science; here are our ground rules for their use. Nature 613,
    612–612 (2023).
11. ICML. Clarification on large language model policy LLM. https://icml.cc/Conferences/2023/llm-policy (2023).
12. Clark, E. et al. All that’s ‘human’is not gold: Evaluating human evaluation of generated text. In Proceedings of the 59th
    Annual Meeting of the Association for Computational Linguistics and the 11th International Joint Conference on Natural
    Language Processing (Volume 1: Long Papers), 7282–7296 (2021).
13. OpenAI. GPT-2: 1.5B release. https://openai.com/research/gpt-2-1-5b-release (2019). Accessed: 2019-11-05.
14. Jawahar, G., Abdul-Mageed, M. & Lakshmanan, L. V. Automatic detection of machine generated text: A critical survey.
    arXiv preprint arXiv:2011.01314 (2020).
15. Fagni, T., Falchi, F., Gambini, M., Martella, A. & Tesconi, M. Tweepfake: About detecting deepfake tweets. Plos one 16,
    e0251415 (2021).
16. Ippolito, D., Duckworth, D., Callison-Burch, C. & Eck, D. Automatic detection of generated text is easiest when humans
    are fooled. arXiv preprint arXiv:1911.00650 (2019).
17. Mitchell, E., Lee, Y., Khazatsky, A., Manning, C. D. & Finn, C. DetectGPT: Zero-shot machine-generated text detection
    using probability curvature. arXiv preprint arXiv:2301.11305 (2023).
18. Solaiman, I. et al. Release strategies and the social impacts of language models. arXiv preprint arXiv:1908.09203 (2019).
19. Gehrmann, S., Strobelt, H. & Rush, A. M. Gltr: Statistical detection and visualization of generated text. In Proceedings of
    the 57th Annual Meeting of the Association for Computational Linguistics: System Demonstrations, 111–116 (2019).
20. Heikkil"a, M. How to spot ai-generated text. MIT Technol. Rev. (2022).
21. Crothers, E., Japkowicz, N. & Viktor, H. Machine generated text: A comprehensive survey of threat models and detection
    methods. arXiv preprint arXiv:2210.07321 (2022).
22. Rosenblatt, K. Chatgpt banned from new york city public schools’ devices and networks. NBC News (2023). Accessed:
    22.01.2023.
23. Kasneci, E. et al. Chatgpt for good? on opportunities and challenges of large language models for education. Learn.
    Individ. Differ. 103, 102274 (2023).
24. Kaggle. The hewlett foundation: Automated essay scoring. https://www.kaggle.com/c/asap-aes (2012). Accessed:
    2023-03-15.
25. Laufer, B. & Nation, P. Vocabulary size and use: Lexical richness in l2 written production. Appl. linguistics 16, 307–322
    (1995).
26. Jarvis, S. Short texts, best-fitting curves and new measures of lexical diversity. Lang. Test. 19, 57–84 (2002).
27. Daller, H., Van Hout, R. & Treffers-Daller, J. Lexical richness in the spontaneous speech of bilinguals. Appl. linguistics 24,
    197–222 (2003).


                                                                                                                              4/9


### Extracted PDF page 5

28. Lu, X. A corpus-based evaluation of syntactic complexity measures as indices of college-level esl writers’ language
    development. TESOL quarterly 45, 36–62 (2011).
29. Crossley, S. A. & McNamara, D. S. Does writing development equal writing quality? a computational investigation of
    syntactic complexity in l2 learners. J. Second. Lang. Writ. 26, 66–79 (2014).
30. Ortega, L. Syntactic complexity measures and their relationship to l2 proficiency: A research synthesis of college-level l2
    writing. Appl. linguistics 24, 492–518 (2003).
31. Biber, D., Gray, B. & Poonpon, K. Should we use characteristics of conversation to measure grammatical complexity in l2
    writing development? Tesol Q. 45, 5–35 (2011).
32. Krishna, K., Song, Y., Karpinska, M., Wieting, J. & Iyyer, M. Paraphrasing evades detectors of ai-generated text, but
    retrieval is an effective defense. arXiv preprint arXiv:2303.13408 (2023).
33. Sadasivan, V. S., Kumar, A., Balasubramanian, S., Wang, W. & Feizi, S. Can ai-generated text be reliably detected? arXiv
    preprint arXiv:2303.11156 (2023).
34. Kirchenbauer, J. et al. A watermark for large language models. arXiv preprint arXiv:2301.10226 (2023).
35. Gu, C., Huang, C., Zheng, X., Chang, K.-W. & Hsieh, C.-J. Watermarking pre-trained language models with backdooring.
    arXiv preprint arXiv:2210.07543 (2022).
36. Liang, W., Yuksekgonul, M., Mao, Y., Wu, E. & Zou, J. ChatGPT-Detector-Bias: v1.0.0, DOI: 10.5281/zenodo.7893958
    (2023).




                                                                                                                           5/9


### Extracted PDF page 6

a                                                                                               b




                                                                                                    TOEFL:  
                                                                                                    Test of English as a
                                                                                                    Foreign Language

c                                                                                               d




                                                                                                    US 8th Grade Essays



Figure 1. Bias in GPT detectors against non-native English writing samples. (a) Performance comparison of seven
widely-used GPT detectors. More than half of the non-native-authored TOEFL (Test of English as a Foreign Language) essays
are incorrectly classified as "AI-generated," while detectors exhibit near-perfect accuracy for US 8-th grade essays. (b) TOEFL
essays unanimously misclassified as AI-generated show significantly lower perplexity compared to others, suggesting that GPT
detectors might penalize authors with limited linguistic expressions. (c) Using ChatGPT to improve the word choices in
TOEFL essays (Prompt: “Enhance the word choices to sound more like that of a native speaker.”) significantly reduces
misclassification as AI-generated text. Conversely, applying ChatGPT to simplify the word choices in US 8th-grade essays
(Prompt: “Simplify word choices as if written by a non-native speaker.”) significantly increases misclassification as
AI-generated text. (d) The US 8th-grade essays with simplified word choices demonstrate significantly lower text perplexity.




                                                                                                                           6/9


### Extracted PDF page 7

a                                                                                           b




                                                                                                US Common App College
                                                                                                   Admission Essays


   c                                                                                           d




                                                                                                   Scientific Abstracts




Figure 2. Simple prompts effectively bypass GPT detectors. (a) For ChatGPT-3.5 generated college admission essays, the
performance of seven widely-used GPT detectors declines markedly when a second-round self-edit prompt (“Elevate the
provided text by employing literary language”) is applied, with detection rates dropping from up to 100% to up to 13%. (b)
ChatGPT-3.5 generated essays initially exhibit notably low perplexity; however, applying the self-edit prompt leads to a
significant increase in perplexity. (c) Similarly, in detecting ChatGPT-3.5 generated scientific abstracts, a second-round
self-edit prompt (“Elevate the provided text by employing advanced technical language”) leads to a reduction in detection rates
from up to 68% to up to 28%. (d) ChatGPT-3.5 generated abstracts have slightly higher perplexity than the generated essays
but remain low. Again, the self-edit prompt significantly increases the perplexity.




                                                                                                                           7/9


### Extracted PDF page 8

Materials and Methods
Data availability
Our data, results, and code are available on both GitHub (https://github.com/Weixin-Liang/ChatGPT-Detector-Bias/)
and Zenodo36 .

Evaluation of off-the-shelf GPT detectors
We assessed seven widely-used off-the-shelf GPT detectors:
   1. Originality.AI: https://app.originality.ai/api-access
   2. Quil.org: https://aiwritingcheck.org/
   3. Sapling: https://sapling.ai/ai-content-detector
   4. OpenAI: https://openai-openai-detector.hf.space/
   5. Crossplag: https://crossplag.com/ai-content-detector/
   6. GPTZero: https://gptzero.me/
   7. ZeroGPT: https://www.zerogpt.com/
Accessed on March 15, 2023.

ChatGPT prompts used
  1. ChatGPT prompt for refining real TOEFL essays: “Enhance the word choices to sound more like that of a native
     speaker: <TOEFL essay text>”
   2. ChatGPT prompt for adjusting real US 8th grade essays: “Simplify word choices as of written by a non-native
      speaker.”
   3. ChatGPT prompts for the US college admission essays

        (a) [1st round] ChatGPT prompt for generating US college admission essays: “Hi GPT, I’d like you to write a
            college application essay. <college-essay-prompt>” where the <college-essay-prompt> corresponds to one of the
            Common App 2022-2023 essay prompts as follows (7 prompts in total):
                i. Some students have a background, identity, interest, or talent that is so meaningful they believe their
                   application would be incomplete without it. If this sounds like you, then please share your story.
               ii. The lessons we take from obstacles we encounter can be fundamental to later success. Recount a time when
                   you faced a challenge, setback, or failure. How did it affect you, and what did you learn from the experience?
             iii. Reflect on a time when you questioned or challenged a belief or idea. What prompted your thinking? What
                   was the outcome?
              iv. Reflect on something that someone has done for you that has made you happy or thankful in a surprising way.
                   How has this gratitude affected or motivated you?
               v. Discuss an accomplishment, event, or realization that sparked a period of personal growth and a new
                   understanding of yourself or others.
              vi. Describe a topic, idea, or concept you find so engaging that it makes you lose all track of time. Why does it
                   captivate you? What or who do you turn to when you want to learn more?
             vii. Share an essay on any topic of your choice. It can be one you’ve already written, one that responds to a
                   different prompt, or one of your own design.
            For each college essay prompt, we run 10 trials, resulting in 70 trails in total. After filtering out invalid responses
            (E.g., "As an AI language model, I don’t have a personal background, identity, interest or talent. Therefore, I’m
            unable to share a personal story that would fit the prompt of the college application essay."), we obtained 31
            counterfeit essays.
        (b) [2nd round] ChatGPT prompt for refining ChatGPT-generated US college admission essays: “Elevate the
            provided text by employing literary language: <generated essay>” where the <generated essay> originates from
            the first round.


                                                                                                                               8/9


### Extracted PDF page 9

4. ChatGPT prompts for scientific abstracts

        (a) [1st round] ChatGPT prompt for generating US college admission essays: “Please draft an abstract (about
            120 words) for a final report based on the title ’<title>”’ where the <title> is a scientific project title.
        (b) [2nd round] ChatGPT prompt for refining ChatGPT-generated scientific abstracts: “Elevate the provided
            text by employing advanced technical language: <generated abstract>” where the <generated abstract> comes
            from the first round.

We utilized the March 14 version of ChatGPT 3.5.

Data
TOEFL Essays
We collected a total of 91 human-written TOEFL essays (year<=2020) from a Chinese educational forum (https://toefl.
zhan.com/). The TOEFL (Test of English as a Foreign Language) is a standardized test that measures the English language
proficiency of non-native speakers.

US College Admission Essays
We assembled a total of 70 authentic essays for our analysis, with 60 essays sourced from https://blog.prepscholar.
com/college-essay-examples-that-worked-expert-analysis and 10 essays from https://www.collegeessaygu
com/blog/college-essay-examples.
Scientific Abstracts
We gathered a total of 145 authentic course project titles and abstracts from Stanford’s CS224n: Natural Language Processing
with Deep Learning, Winter 2021 quarter (https://web.stanford.edu/class/archive/cs/cs224n/cs224n.
1214/project.html). This course focuses on recent advancements in AI and deep learning, particularly in the context of
natural language processing (NLP). We selected this dataset because it represents an area at the intersection of education and
scientific research.

Statistical test
To evaluate the statistical significance of perplexity differences between two corpora, we employed a paired t-test with a
one-sided alternative hypothesis. This analysis was conducted using the Python SciPy package. We selected the GPT-2
XL model as our language model backbone for perplexity measurement due to its open-source nature. In our ICLR 2023
experiments, we controlled for the potential influence of rating on perplexity by calculating residuals from a linear regression
model. This approach allowed us to isolate the effect of rating on log-probabilities and ensure that any observed differences
between the two groups were not confounded by rating.




                                                                                                                            9/9


## Supporting artifact inventory and implementation notes

The cited Zenodo v1.0.0 archive contains 113 ZIP entries: 98 files totaling 31,354,252 uncompressed bytes plus 15 directories. Its ten dataset/result folders contain 91 original TOEFL essays, 91 GPT-4-polished TOEFL essays, 88 original Hewlett eighth-grade essays, 88 GPT-simplified Hewlett essays, 70 human college essays, 145 human CS224N abstracts, 31 original and 31 self-edited GPT-3 college essays, and 145 original and 145 self-edited GPT-3 CS224N abstracts. Each experimental result file has the same row count as its folder's `data.json`. Seven named detector-result files are present for all paired intervention and generated sets; the human CS224N folder contains five detector files.

The archive also contains `README.md` and five Python files. The released `extract_scores.py` is not an end-to-end reproduction script as preserved: it imports absent `models` and `detectors` modules, calls `DetectionDataset(foler)` with an undefined name, and includes no analysis or figure-generation code. Detector web outputs and the paper's results are preserved, but most proprietary detector versions, thresholds, training data, and build identifiers are not. This limits independent reproduction of the detector calls and published aggregate figures even though the underlying text/result records are available.

## Extraction verification

- **Beginning checked:** The published title, five authors, summary, and Introduction in the PMC JATS record were compared with the canonical Cell rendering and arXiv v3 page 1. The arXiv title, author block, v3 date, abstract, and opening Introduction were visually checked on rendered page 1.
- **Middle checked:** The published detector-bias, intervention, bypass, and Discussion sections and both captions were checked against the Cell-rendered text. ArXiv v3 page 5 was rendered and checked at the reference/Zenodo transition; pages 6-7 contain the two complete figures and captions in the preserved PDF.
- **End checked:** The published acknowledgments, declaration, five biographies, and all eight references were checked in the JATS record. ArXiv v3 page 9 was rendered and checked for the scientific-abstract data description, one-sided paired t-test, GPT-2 XL perplexity backbone, and ICLR rating-control description.
- **Structure checked:** Published JATS contains one summary paragraph, 14 substantive main-text paragraphs across Introduction plus four named findings/discussion sections, two figures/captions, no tables, one acknowledgment, one declaration, five biographies, and eight references. The supporting arXiv v3 PDF has nine pages, 36 references, two figures, a limitations passage, data availability, complete prompts, dataset descriptions, statistical method, and seven-detector inventory. The Zenodo archive MD5 matches its API record and every one of its 98 files was inventoried.
- **Known omissions:** No substantive source material is omitted. Published figure pixels are not embedded in this Markdown, but both captions are present and the complete arXiv v3 PDF preserves visually equivalent figures. The Zenodo datasets are not duplicated inline because the verified complete ZIP is preserved as an attachment.

## Preserved attachments

| Path | Role in the source | SHA-256 | Preservation / extraction notes |
|---|---|---|---|
| `snapshots/attachments/liang-detector-bias-pmc10382961.xml` | Complete published Patterns article in JATS XML | `bb2e4642b3a81ad8b092ba09af0ca4862ff9740ba925306c0e53216d3d9be26c` | Fetched from Europe PMC fullTextXML; all abstract/body text, captions, biographies, declarations, and references converted above. |
| `snapshots/attachments/liang-detector-bias-arxiv-2304.02819v3.pdf` | Final nine-page supporting preprint with methods, exact statistics, figures, references, and data availability | `9019ad9a465a7e5a6d13e372a1eccbb51321aa50a046e4510385865234194efb` | Downloaded directly from arXiv; all pages extracted; pages 1, 5, and 9 rendered and visually checked. |
| `snapshots/attachments/liang-detector-bias-zenodo-7893958-v1.0.0.zip` | Complete cited v1.0.0 code, data, and detector-result archive | `6e08ea990a68da050c698bc7ad228b15f7b6bfdaf1660fd79b43c4d140db8843` | Downloaded through the Zenodo record API; MD5 `f7576b35b32853a0881db7dda3915d19` matches the API; all 98 files inventoried and code inspected. |
| `snapshots/attachments/liang-detector-bias-zenodo-7893958-metadata.json` | Zenodo record metadata and file checksum | `69bcc261021204c32dfe451fa9a484c8576c074535dcc3cad39946bf1463ea60` | Complete API response for record 7893958, retrieved 2026-07-16. |
