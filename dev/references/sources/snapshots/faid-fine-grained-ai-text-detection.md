# FAID: Fine-Grained AI-Generated Text Detection Using Multi-Task Auxiliary and Multi-Level Contrastive Learning

- **Canonical URL:** https://aclanthology.org/2026.eacl-long.151/
- **Alternate access URLs:**
  - https://aclanthology.org/2026.eacl-long.151.pdf
  - https://aclanthology.org/attachments/2026.eacl-long.151.checklist.pdf
  - https://aclanthology.org/2026.eacl-long.151.checklist.pdf (attempted; returned HTTP 404)
- **Author / owner:** Minh Ngoc Ta, Dong Cao Van, Duc-Anh Hoang, Minh Le-Anh, Truong Nguyen, My Anh Tran Nguyen, Yuxia Wang, Preslav Nakov, and Dinh Viet Sang
- **Publisher:** Association for Computational Linguistics
- **Published:** March 2026
- **Retrieved:** 2026-07-15
- **Stable identifier:** DOI 10.18653/v1/2026.eacl-long.151; ACL Anthology ID 2026.eacl-long.151
- **Version / revision:** EACL 2026 final proceedings version, pages 3275-3296
- **Extraction method:** Official ACL paper and Responsible NLP Checklist PDFs downloaded with `curl`; embedded text layers extracted with Poppler `pdftotext -layout`; page count and PDF metadata checked with `pdfinfo`; paper pages 1, 11, and 22 rendered with `pdftoppm` and compared visually
- **Full-text status:** complete
- **Access and transformation notes:** No OCR was required. The paper extraction contains all 22 pages, including tables, captions, limitations, ethics discussion, references, prompts, and appendices. The two-column text layer is mechanically interleaved in places, and chart labels in Figures 3-5 are represented most reliably in the preserved PDF. The two-page checklist is preserved separately and its text is reproduced after the paper. The user queue title, "FAID: Fine-grained AI-generated Text Detection", omits the subtitle "Using Multi-Task Auxiliary and Multi-Level Contrastive Learning" found in the authoritative PDF.

## Full text

                 FAID: Fine-Grained AI-Generated Text Detection
          Using Multi-Task Auxiliary and Multi-Level Contrastive Learning
               Minh Ngoc Ta1,2 , Dong Cao Van1* , Duc-Anh Hoang1* , Minh Le-Anh1* ,
                     Truong Nguyen1* , My Anh Tran Nguyen1* , Yuxia Wang2,3 ,
                                  Preslav Nakov2 , Dinh Viet Sang1
           1
             BKAI Research Center, Hanoi University of Science and Technology 2 MBZUAI
                          3
                            INSAIT, Sofia University "St. Kliment Ohridski"
                       minh.ta@mbzuai.ac.ae, sangdv@soict.hust.edu.vn

                              Abstract                               Numerous studies have explored multilingual
                                                                  LLM-generated text detection, but most have fo-
        The growing collaboration between humans
                                                                  cused either on binary detection, i.e., human vs.
        and LLMs in generative tasks has introduced
        new challenges in distinguishing between
                                                                  LLM (Wang et al., 2024e,c; Su et al., 2023) or on
        human-written, LLM-generated, and human–                  fine-grained detection limited to English (Abassy
        LLM collaborative texts. In this work, we                 et al., 2024; Koike et al., 2024; Wang et al., 2023;
        collect a multilingual, multi-domain, multi-              Zhang et al., 2024). Moreover, both struggle with
        generator dataset FAIDSet. We further in-                 generalization to unseen domains, languages, and
        troduce a fine-grained detection framework,               LLM generators (Wang et al., 2024d; Li et al.,
        FAID, to classify text into these three cate-             2024).
        gories and to identify the underlying LLM
                                                                     Our work aims to bridge this gap by (i) col-
        family of the generator. Unlike existing bi-
        nary classifiers, FAID is built to capture both           lecting a multilingual, multi-domain, and multi-
        authorship and model-specific characteristics.            generator dataset, FAIDSet, for fine-grained detec-
        Our method combines multi-level contrastive               tion, i.e., identifying a text into three categories:
        learning with multi-task auxiliary classifica-            LLM-generated, human-written, and human–LLM
        tion to learn subtle stylistic cues. By mod-              collaborative, and (ii) introducing a framework
        eling LLM families as distinct stylistic enti-            FAID to improve generalization performance.
        ties, we adapt to address distributional shifts
                                                                     Our dataset FAIDSet1 focuses on the academic
        without retraining on unseen data. Our results
        demonstrate that FAID outperforms several                 field, including paper abstracts, student theses, and
        baselines, particularly improving generaliza-             reports, and contains generation by a variety of
        tion accuracy across unseen domains and new               families of LLMs, e.g., GPT, Gemini, DeepSeek,
        LLMs, offering a potential solution to improve            and Llama (OpenAI, 2024; Gemini Team, 2024;
        transparency and accountability in AI-assisted            DeepSeek-AI, 2025; Dubey et al., 2024).
        writing. Our data and code are available at                  Our detection framework, FAID, treats each
        https://github.com/mbzuai-nlp/FAID
                                                                  LLM as a distinct author, learning specific features
1       Introduction                                              in the hidden space to differentiate different au-
                                                                  thors, instead of classifying based on hand-crafted
LLMs have evolved from an assistant tool to a cre-                stylistic features. We achieve this by optimizing a
ator or initiator, from helping polish papers to initi-           language encoder with multi-level author relation-
ating proposals and drafting essays, while humans                 ship (e.g., the stylistic similarity between texts from
increasingly serve as optimizers and reviewers. In                the same LLM family is greater than that between
such deeply collaborative human–LLM settings,                     a human and an LLM) to capture author-specific
measuring human contribution becomes challeng-                    distinguishable signals of an input text using con-
ing, yet clarifying authorship is critical for account-           trastive learning, along with the task of fine-tuning
ability and transparency, particularly in educational             a classifier to recognize the input text’s origin. This
and academic contexts (Wang et al., 2025). This                   multitask learning process forces the encoder to
work aims to identify human involvement by distin-                reorganize the hidden space so that the representa-
guishing the origin of a given text (in a multilingual            tions of texts by the same authors are distributed
context): (a) fully LLM-generated, (b) fully human-               closer together than those by different authors.
written, or (c) collaboratively produced.                            1
                                                                       https://huggingface.co/datasets/ngocminhta/
    *
        Equal contribution.                                       FAIDSet

                                                             3275
           Proceedings of the 19th Conference of the European Chapter of the Association for Computational Linguistics
                                            Volume 1: Long Papers, pages 3275–3296
                               March 24-29, 2026 ©2026 Association for Computational Linguistics
   In practice, given that generations produced by          In response to these challenges, we collect a new
LLMs from the same company tend to have similar          dataset, FAIDSet, and propose a detection frame-
writing styles due to similar model architecture,        work, FAID, which generalizes well to new do-
training data, and training strategy (see Appendix D     mains, languages, and models, achieving consis-
for more detail), we consider each LLM family            tently high accuracy and reliability.
as an “author.” This can also help the detector
acquire prior knowledge of future LLMs from the          2.1   Fine-Grained AI-generated Text Datasets
same company. Our experiments show that FAID             Many prior studies have explored fine-grained AI-
consistently outperforms other baseline detectors        generated text datasets across various forms of
in both in-domain and out-of-domain evaluations.         human–AI collaboration, e.g., MixSet (Zhang et al.,
Our contributions can be summarized as follows:          2024) and Beemo (Artemova et al., 2025). See Ap-
    • We collect a new multilingual, multi-domain,       pendix A for a discussion of more datasets and
      multi-generator dataset for fine-grained LLM-      detailed information regarding the label space, and
      generated text detection with 83,350 exam-         the coverage of domains, languages, and LLMs for
      ples.                                              each one.
                                                            However, all these studies were limited to En-
    • We propose a detection framework, FAID, to         glish. A substantial gap remains in the availabil-
      improve generalization performance in unseen       ity of large-scale, fine-grained multilingual LLM-
      domains and generators by capturing subtle         generated text detection datasets. To bridge this
      stylistic features in the hidden representation.   gap, we collect a multilingual fine-grained LLM-
    • We show that FAID outperforms baseline de-         generated text detection dataset, which encom-
      tectors, particularly in unseen domains and        passes 83k texts generated by the latest LLMs and
      with unseen generators. Meanwhile, the na-         includes diverse forms of human–LLM collabo-
      ture of FAID allows us to assess the stylistic     rative generations. This dataset can facilitate the
      proximity of a given text to other texts in our    development of more robust and generalizable de-
      database, each labeled with ground-truth au-       tection models that are capable of handling com-
      thorship labels.                                   plex multilingual collaborative scenarios.

2    Background and Related Work                         2.2   Generalization of LLM-Generated Text
                                                               Detection
Advancements in LLMs have fundamentally re-
shaped the process of text production and refine-        A recent study, M4GT-Bench, (Wang et al., 2024d)
ment. Rather than originating every word inde-           has highlighted a persistent challenge for both bi-
pendently, people increasingly assume the role of        nary and fine-grained AI-generated text detection:
post-editors or reviewers, intervening after an LLM      poor generalization to unseen domains, languages,
has generated an initial draft. This collaborative       and generators. Many detection methods have
paradigm extends across diverse domains, includ-         shown a significant drop in performance on out-
ing academic publishing, journalism, education,          of-distribution data, underscoring the difficulty of
and social media, thus making hybrid human–AI            building robust detectors for real-world scenarios
authorship an emerging norm (Cheng et al., 2025;         and evolving LLM outputs.
Lee et al., 2022).                                          Various approaches have been proposed to im-
   Such a shift calls into binary authorship detec-      prove generalization. OUTFOX (Koike et al., 2024)
tion: human vs. AI. Texts can be fully human-            leveraged adversarial in-context learning to dynam-
written, fully AI-generated, or collaborative text       ically generate challenging examples that enhance
(e.g., human-written, AI-polished; AI-generated,         robustness, but still faced limitations in domain
human-edited; and deeply mixed) (Artemova et al.,        transferability and computational efficiency. LLM-
2025). Addressing these concerns requires fine-          DetectAIve (Abassy et al., 2024) adopted fine-
grained authorship detection, even tracing it back       grained classification and incorporated domain-
to a specific LLM family, to assess the extent of hu-    adversarial training to reduce overfitting; however,
man contribution (Hutson, 2025). Ensuring trans-         its generalization to unseen domains and genera-
parent disclosure of LLM involvement is critical to      tors remains limited, and its current version lacks
upholding research integrity and honesty.                multilingual support.
                                                     3276
   SeqXGPT (Wang et al., 2023) focused on                   For inference, their pipeline encoded the input
sentence-level detection by combining log-               text as a hidden vector and used dense retrieval
probabilities with convolutional and self-attention      to match the cluster based on stylistic similarity
mechanisms, thereby helping capture subtle mixed-        against a database of previously indexed training
content signals and improving generalization             features. Additionally, instead of retraining the
across input styles. However, its reliance on            model on new data, they encoded the new data
specific model features and its limited semantic         with the trained encoder to obtain embeddings,
representation constrained the adaptability to new       then added them to the feature database to aug-
generators and domains.                                  ment. This largely improved the generalizability to
   Finally, the DeTeCtive framework (Guo et al.,         unseen domains and new generators.
2024) introduced multi-level contrastive learning to        However, this approach distinguishes only be-
better capture writing-style diversity and enhance       tween two categories of text (human-written vs.
generalizability, especially for out-of-distribution     LLM-generated) while overlooking the increas-
scenarios, but it primarily focused on binary clas-      ingly prevalent class of human–LLM collabora-
sification and did not fully address human–AI col-       tive texts. Our work bridges this gap to enhance
laborative texts.                                        generalization performance in fine-grained LLM-
                                                         generated text detection.
2.3 Contrastive Learning for AI-Generated
    Text Detection                                       3       FAIDSet

Contrastive learning has been widely used to im-         We collected a new multilingual, multi-domain,
prove sentence representations by pulling semanti-       and multi-generator LLM-generated text dataset,
cally similar sentences closer together and pushing      FAIDSet. It contains texts generated by LLMs,
dissimilar ones apart. SimCSE treats a sentence          written by humans, and collaborated by both, result-
subjected to dropout noise as a semantically similar     ing in a total of 83,350 examples; see Appendix B
counterpart (i.e., a positive pair) and trains the en-   for more details about FAIDSet.
coder to minimize the distance between the original         FAIDSet covers two domains: student theses
and the noise sentence. It further leverages natural     and paper abstracts, where identifying authorship
language inference pairs, considering entailment         is critical, across two languages (Vietnamese and
pairs as positives and contradiction pairs as hard       English). We collected students’ theses from the
negatives (Gao et al., 2021). It is then trained to      database of Hanoi University of Science and Tech-
maximize the separation between negative pairs in        nology, and paper abstracts from arXiv and Viet-
the embedding space. DeCLUTR (Giorgi et al.,             nam Journals Online2 (VJOL).
2021) constructed positive pairs by extracting dif-         Models and Label Space. We used the follow-
ferent spans from the same texts and by sampling         ing multilingual LLM families to produce LLM
negative pairs from different texts.                     and human–LLM collaborative texts: GPT-4/4o,
   We adopt the same core idea, but reorganize           Llama-3.x, Gemini 2.x, and Deepseek V3/R1. Re-
the latent space by clustering human-written texts       garding the human–LLM collaborative text, we
by writing style, keeping them distant from LLM-         include LLM-polished, LLM-continued, and LLM-
generated texts. Similarly to semantic textual simi-     paraphrased, where the models are requested to
larity tasks, where sentence similarity ranges from      polish or paraphrase inputs while ensuring the ac-
0 to 5 to reflect varying degrees of semantic overlap,   curacy of any figures and statistics.
we incorporate ordinal regression into our frame-           Diverse Prompt Strategies. We generated data
work to model the degree of human involvement,           with diverse tones and contexts while ensuring con-
ranging from 0 (solely LLM) to 1 (fully human).          tent accuracy. Depending on the data source and
                                                         context, we crafted prompts to create varied outputs
   Another work, DeTeCtive (Guo et al., 2024),
                                                         suitable for different real-world scenarios. We gen-
also leveraged contrastive learning and was used
                                                         erated responses with different tones using prompts
for binary detection task. Based on a multi-task
                                                         such as “You are an IT student...” and “...who are
framework, it was trained to learn style diversity
                                                         very familiar with abstract writing...”. See Ap-
using a multi-level contrastive loss, and an auxiliary
                                                         pendix B.2 for the full list.
task of classifying the source of a given text (human
vs. AI) to capture distinguishable signals.                  2
                                                                 https://vjol.info.vn/

                                                     3277
   While FAIDSet does not capture the full natural     4.1   Framework Overview
diversity of in-the-wild LLMs’ outputs, the con-
                                                       Here, we shift the focus to the detector, an encoder-
trolled setup enables us to systematically model
                                                       based model that forms the core of FAID. The
stylistic and collaborative signals across multiple
                                                       detector encodes each text into a high-dimensional
languages and families. This makes FAIDSet both
                                                       embedding space to quantify cross-source simi-
a reproducible training resource and a benchmark-
                                                       larity, enabling the study of both intra- and inter-
ing corpus: it provides reliable supervision for de-
                                                       family relationships. It is trained to capture multi-
veloping detectors while also serving as a testbed
                                                       level similarities between authors by learning a
for assessing generalization to more diverse, un-
                                                       representation space where closely related sources
seen scenarios.
                                                       (e.g., LLMs from the same family) form tighter
   Quality Control. To avoid bad machine-              clusters, while dissimilar ones (e.g., human vs.
generated texts, which can introduce remarkably        LLM) are pushed farther apart.
distinguishable signals, we performed quality con-
                                                          Let Sc be cosine similarity, ϕ(·) be the encoder
trol by randomly sampling 10–20 instances for each
                                                       function, and Pi , Pj , (1 ≤ i ≤ j < 5) be the
domain, source, and LLM generator. Manual in-
                                                       distributions of different text sources. We aim for
spection focused on fluency, coherence, and factual
                                                       the model to encode representations that satisfy the
plausibility. Overall, the generated texts demon-
                                                       following constraint:
strated high linguistic quality, with most outputs
being fluent and logically reasonable. Neverthe-          Ex∈Pi ,y∈Pj [Sc (ϕ(x), ϕ(y))]
less, occasional issues such as repetitive phrasing,
incomplete reasoning, or overuse of formal expres-                    ≥ Ex∈Pi ,y∈Pj+1 [Sc (ϕ(x), ϕ(y))]
sions were observed. In those cases, we adjusted                                                       (1)
the prompts (e.g., by specifying desired length or
style) or refined generation parameters to improve     where P1 corresponds to the distribution generated
diversity and logical consistency. After these ad-     by a particular LLM family, P2 is the distribution
justments, the quality across generators and do-       generated by any LLM, P3 is the distribution of
mains was found to be stable and satisfactory.         collaborative text generated by human and a LLM
                                                       family of P1 , P4 is the distribution of collaborative
4   Methodology                                        text generated by humans and any LLM families,
                                                       and P5 is the distribution of human-written text.
Task Definition Our task is a three-class classifi-       To clarify the rationale for configuring FAID to
cation problem: human-written vs. LLM-generated        expect that the similarity of a text x (from lower-
vs. human–LLM collaborative text detection.            level distributions P1 or P2 ) with samples from P3
   The human–LLM collaborative category in-            is generally greater than or equal to its similarity
volves a range of interactions between humans and      with samples from P4 , consider the following:
LLM systems, such as (a) human-written, LLM-
polished, (b) human-initiated, LLM-continued,             • If x ∈ P1 (x is generated by a particular
(c) human-written, LLM-paraphrased, etc. Given              LLM): Let yLHS be drawn from P3 and yRHS
the growing variety and complexity (e.g., deeply            be drawn from P4 . Naturally, the similarity
mixed text) of collaborative patterns, this is not          Sc (x, yLHS ) is greater than Sc (x, yRHS ). This
exhaustive. Instead, we consolidate all forms of            is because P3 contains texts that share a direct
human–LLM collaboration into a single label to              LLM family origin with x.
maintain practical simplicity and model generaliz-
ability. This reflects real-world usage, where using      • If x ∈ P2 (x is generated by any LLM):
LLM tools to enhance clarity or expression is in-           Here, with yLHS from P3 and yRHS from P4
creasingly common and often ethically acceptable.           as defined above, the similarity Sc (x, yLHS ) is
   Our analysis of the dataset revealed that the            generally expected to be equal to Sc (x, yRHS ).
LLM models within the same family tend to have              Since x can originate from any LLM, it does
similar writing style and text distributions, due to        not inherently possess a stronger connection
their shared training data and architecture (see Ap-        to the specific LLM family in P3 than to
pendix D). Thus, we consider each model’s family            the broader human-LLM collaborations repre-
to be an “author” with a unique writing style.              sented in P4 .
                                                   3278
                  Human-written                                                                 LLaMA          Human




                                                                                                                       Human +
              Human-LLM collaboration                                        Push                                      Deepseek       Pull
                                        Encoder
                                        (XLM-RoBERTa)
                                                                                                                            Push
                                                                                          GPT
                  LLM-generated
                                                                                                              Human


                                                        Text Embeddings             Differentiating Authors Via Contrastive Learning


Figure 1: Training architecture. Leveraging multi-level contrastive learning loss, we fine-tune a language model
(we select XLM-RoBERTa (Vamvas and Sennrich, 2023), see Appendix E) based on the human, human–LLM and
LLM-generated texts, to force the model to reorganize the hidden space, pulling the embeddings within the same
author families closer, and pushing the embeddings from different authors farther. We train an encoder that can
represent text with distinguishable signals to discern the authorship of text.


   This configuration aims to ensure that closeness                 For cases where all samples are human–LLM
in distribution corresponds to higher similarity after            collaborative, two texts created by the same LLM
encoding, thus encouraging the model to discern                   family tend to be more similar than such that in-
fine-grained multi-level relations.                               volve contributions from different LLM families.
                                                                  That is:
4.2 Multi-level Contrastive Learning
Given a dataset with N examples, each example is                  σ(i, j) > σ(i, k), ∀xi = 1, yi,j,k = 1, zi = zj ̸= zk
a text unit (paragraph/segment). The ith record is                                                                  (5)
denoted as Ti . Per record, we assigned three-level                 Combining all, the text representation is learned
labels indicating its source:                                     with the following constraints:
   • xi ∈ {0, 1}: if Ti is a fully LLM-generated                      
                                                                      
                                                                      σ(i, j) > σ(i, k), ∀xi = 0, xi = xj ̸= xk ;
     text, xi = 0, otherwise xi = 1;                                  
                                                                      
                                                                      
                                                                      
                                                                      σ(i, j) > σ(i, k), ∀xi = 0, zi = zj ̸= zk ;
                                                                      
                                                                      
   • yi ∈ {0, 1}: if Ti is a fully human-written                       σ(i, j) > σ(i, k), ∀xi = 1, xi = xj ̸= xk ;
                                                                                                                                             (6)
     text, yi = 0, otherwise yi = 1;                                  
                                                                      σ(i, j) > σ(i, k), ∀xi = 1, yi = yj ̸= yk ;
                                                                      
                                                                      
                                                                      
                                                                      σ(i, j) > σ(i, k), ∀xi = 1, yi,j,k = 1,
   • zi : an indicator of a specific LLM family.                      
                                                                      
                                                                      
                                                                                           zi = zj , zi ̸= zk
   The encoder ϕ(·) represents the text Ti in a d-
dimensional vector space Rd . Then we calculate                      To enforce the similarity constraints outlined
the cosine similarity between two texts Ti and Tj ,               in Eq (6), we build upon the SimCLR framework
denoted by: σ(i, j) = Sc (ϕ(Ti ), ϕ(Tj )).                        (Chen et al., 2020) and introduce a strategy for
   For LLM-generated text, the similarity between                 defining both positive and negative sample pairs,
Ti and another LLM-generated text Tj is greater                   which forms the basis of our contrastive learning
than that with a human-written or collaborative                   loss. Departing from traditional contrastive losses
text Tk :                                                         that rely on a single positive sample, our approach
  σ(i, j) > σ(i, k), ∀xi = 0, xi = xj , xk = 1 (2)                considers a group of positive instances that satisfy
                                                                  specific criteria. The similarity between the anchor
  If xi = 0, then the text is fully LLM-generated.                and the positive samples is computed as the average
For this case, we do not consider yi since                        similarity across this entire positive set. For nega-
LLM-generated text is considered as non-LLM-                      tive samples, we follow the methodology used in
collaboration. We can imply that the similarity                   SimCLR. The resulting contrastive loss, expressed
between two texts written by the same LLM is                      in Eq (7), involves q as the anchor sample, K + as
higher than that of two LLM families. Hence:                      the positive sample set, K − as the negative sample
  σ(i, j) > σ(i, k), ∀xi = 0, zi = zj , zi ̸= zk (3)              set, τ as the temperature parameter, and NK + as
                                                                  the number of positive samples.
   The reverse condition is also true. We can con-
clude that:                                                                                             P                        
                                                                                                                S(q,k)
                                                                                                  exp                  /NK +
  σ(i, j) > σ(i, k), ∀xi = 1, yi = yj , yi ̸= yk (4)                  Lq = − log         P
                                                                                                         k∈K +
                                                                                                    S(q,k)
                                                                                                                 τ P        
                                                                                                                               S(q,k)
                                                                                                                                            (7)
                                                                                   exp        k∈K +   τ
                                                                                                           /NK + + k∈K − exp     τ


                                                            3279
         Human-written

                                                           LLaMA                          Human
                                                                                                                                                         Human


       Human-LLM Collab.                                                                                                                                 LLaMA


                                                                                                                                                       Human+GPT
                              Encoder                  Human+GPT
        LLM-generated         (XLM-RoBERTa)                                                                                 Encoder                         GPT
                                                                                                                            (XLM-RoBERTa)
                                                                                               Deepseek
                                                                                                                                                        Deepseek


          Unseen Data
                                                                                                                                                       Unseen data
                                                             GPT

                                                                                                            Vector                           Dataset
                                                                                                           Database

         (a) Encode Input Texts to Embedding Vectors        (b) Clustering the Input Text by Querying in       (c) Vector Database for Feature Embeddings
                                                          Vector Database with Fuzzy K-Nearest Neighbor


Figure 2: Inference architecture: (a) embed the input text into embedding vector using the fine-tuned encoder,
(b) use Fuzzy kNN to cluster, retrieving which cluster the input text belongs to (see more in Appendix F), (c) the
stored vector database VD was created by saving all embeddings of texts in training and validation sets using the
fine-tuned encoder. If the input text is unseen, we embed it and save it into a temporary vector database VD′ ,
enhancing the generalization of the detector.


   Different constraints yield different sets of pos-                                 This classifier performs binary classification, de-
itive and negative samples. Based on these sets,                                   termining whether a given text was written by a hu-
contrastive losses are computed at multiple levels.                                man or an LLM. Let the probability of ith sample
As we declared in Eq (7), each inequality in Eq (6)                                with label xi = 0 be pi . To train this component,
is denoted as Lqi ,ε where ε = 1, 5 respectively.                                  we apply a cross-entropy loss function, denoted as
To form Eq (8), we need to add the coefficients                                    Lce , and defined as follows:
α, β, γ, δ, and ζ to maintain the balance of multi-
                                                                                                           N
level relations.                                                                              1 X
                                                                                     Lce = −          xi log pi + (1 − xi ) log (1 − pi )
                                                                                              N
                                                                                                 i=1
            N
            X                                                                                                                         (9)
 Lmcl =             [xi (αLqi ,1 + βLqi ,2 ) +                                         Therefore, the overall loss is computed as:
            i=1
                                                                        (8)
            (1 − xi ) (γLqi ,3 + δLqi ,4 + ζLqi ,5 )]                                                           L = Lce + Lmcl                                       (10)

   Due to the last inequality in Eq (6) only speci-                                4.4 Handling Unseen Data without Retraining
fying a case (yi,j,k = 1), and the other cases con-
                                                                                   Unseen data, whether from an unseen domain or
sidering both values for y, we have ζ = 2γ = 2δ.
                                                                                   an unfamiliar generator, remains a significant chal-
Also, to maintain the equilibrium, we need to keep
                                                                                   lenge even for state-of-the-art LLM-generated text
α + β = γ + δ + ζ. We set γ = δ = 1, then
                                                                                   detection methods, as LLMs continue to improve.
ζ = 2, α = β = 2. This encourages the model
                                                                                   We tried to use the model classifier on its own, but
to capture subtle and detailed features from differ-
                                                                                   we ended up using a vector database along with
ent sources. As a result, it becomes more adept
                                                                                   Fuzzy k-Nearest Neighbors, as illustrated in Fig-
at recognizing variations in writing styles. This
                                                                                   ure 2. The results are given in Appendix F. Specifi-
capability enhances accuracy and strengthens gen-
                                                                                   cally, when dealing with unseen data, we use our
eralizability when detecting LLM-generated text.
                                                                                   model to embed these texts and add them to our
4.3 Multi-Task Auxiliary Learning                                                  existing vector database. Through careful param-
                                                                                   eter tuning, this approach enables our system to
Multi-task learning (Caruana, 1997) allows a model
                                                                                   effectively handle newly encountered unseen data
to learn several tasks concurrently by sharing rel-
                                                                                   without retraining.
evant information across them. This joint learn-
ing process helps the model develop more general                                   5      Experiments
and distinctive features. Therefore, it improves the
model’s generalizability to new data. Building on                                  In this section, we describe the datasets and base-
the previously described contrastive learning frame-                               lines we used, followed by two experiments evalu-
work, we extend the encoder by attaching an MLP                                    ating FAID: (i) classify a text as human, LLM, and
classifier at its output layer.                                                    human–LLM, and (ii) identify specific generators.
                                                                            3280
   Dataset            Detector           Accuracy ↑    Precision ↑   Recall ↑   F1-macro ↑   MSE ↓     MAE ↓
                      LLM-DetectAIve        94.34         94.45       93.79       94.10       0.1888    0.1107
                      T5-Sentinel           93.31         94.92       93.10       93.15       0.2104    0.1101
   FAIDSet
                      SeqXGPT               85.77         85.49       86.02       84.69       0.5593    0.2844
                      FAID                  95.58         95.78       95.33       95.54       0.1719    0.0875
                      LLM-DetectAIve        95.71         95.78       95.72       95.71       0.1606    0.1314
                      T5-Sentinel           94.77         94.70       92.60       93.60       0.1663    0.1503
   LLM-DetectAIve
                      SeqXGPT               81.48         78.72       74.91       76.71       0.3141    0.2255
                      FAID                  96.99         95.29       88.14       91.58       0.1561    0.0754
                      LLM-DetectAIve        94.39         94.25       94.33       94.29       0.3244    0.1789
                      T5-Sentinel           86.68         87.25       87.69       87.38       0.4339    0.2334
   HART
                      SeqXGPT               63.12         64.01       65.27       64.05       1.0057    0.5982
                      FAID                  96.73         97.61       98.05       97.80       0.4631    0.1806

     Table 1: Performance with three labels. The best results are in bold and the second best are underlined.


5.1 Datasets                                               5.2    Baselines
In addition to FAIDSet, for in-domain evaluation,          LLM-DetectAIve: We adapted the method
we used two additional datasets:                           of Abassy et al. (2024) by fine-tuning a
   LLM-DetectAIve (Abassy et al., 2024) encom-             roberta-base sequence classification model. We
passes various domains, including arXiv, Wikihow,          tokenized the input texts using the RoBERTa to-
Wikipedia, Reddit, student essays, and peer re-            kenizer with a maximum sequence length of 256,
views. We augmented the original labels human-             and we trained the model for three-class detection.
written and machine-generated using multiple
                                                          T5-Sentinel: We adapted the T5-Sentinel frame-
LLMs to create a 485,405-example dataset with
                                                          work introduced by Chen et al. (2023) for our three-
two new labels: (i) machine-written then machine-
                                                          class setup. Following the original configuration,
humanized, and (ii) human-written then machine-
                                                          we trained using the AdamW optimizer (batch size
polished.
                                                          128, learning rate 1×10−4 , weight decay 5×10−5 ).
   HART (Bao et al., 2025) has 21,500 examples,
                                                          This allows direct comparison with prior T5-based
including student essays, arXiv abstracts, story
                                                          detectors under our experimental conditions.
writing, and news articles. It covers four categories:
human-written, AI-refined, AI-generated, and hu-           SeqXGPT: We adopted the method of Wang et al.
manized AI-generated texts. The authors further ex-        (2023), who model token-level likelihood patterns
panded the dataset by creating additional instances        from LLM tokenizers for sentence-level detection:
with unbalanced label distributions.                       we updated the tokenizer models to align with our
   To evaluate the generalizability of FAID on un-         dataset’s label space. This adjustment ensures that
seen scenarios, we collected the following data:           the extracted token-level log-probability features
   Unseen domain: We created a dataset consisting          better reflect the model types in our data.
of 150 IELTS essays from Kaggle3 , where all texts
are human-written. We used these essays to gener-          5.3    Human-Only, LLM-Only, or
ate human–LLM collaborative and LLM-generated                     Human-LLM?
texts with the same models with FAIDSet.                   Tables 1 and 2 show the performance of FAID and
   Unseen generators: We selected 150 human-               three baselines in three evaluation settings.
written abstracts from the FAIDSet test set and               As shown in Table 1, FAID consistently achieves
generated data for the remaining labels using three        the best accuracy in (i) in-domain and known gener-
new LLM families: Qwen, Mistral, and Gemma.                ators, (ii) unseen domains, (iii) unseen generators,
   Unseen domain & generators: Based on the                and (iv) unseen domain & generators settings. It
human-written IELTS essays above, we used the              is followed by LLM-DetectAIve for (i) and (iv),
same LLM families as for the unseen generator test         and by T5-Sentinel for (ii) and (iii). Despite be-
set to generate data for the LLM and the human–            ing designed to extract sequence-level features, Se-
LLM labels.                                                qXGPT struggles with texts from advanced models,
   3
     https://www.kaggle.com/datasets/mazlumi/              whose coherent, human-like writing styles reduce
ielts-writing-scored-essays-dataset                        the detectable distinctions.
                                                      3281
  Dataset              Detector              Accuracy ↑     Precision ↑        Recall ↑      F1-macro ↑      MSE ↓      MAE ↓
                       LLM-DetectAIve          52.83              47.31         64.62          53.28          0.4733    0.4722
                       T5-Sentinel             55.56              49.54         66.67          55.34          0.4444    0.4444
  Unseen domain
                       SeqXGPT                 40.60              43.81         31.87          36.72          0.8021    0.7028
                       FAID                    62.78              70.73         71.77          69.46          0.4514    0.4486
                       LLM-DetectAIve          75.71              73.25         75.63          74.30          0.3714    0.2957
                       T5-Sentinel             85.95              85.77         84.59          85.16          0.3648    0.2419
  Unseen generators
                       SeqXGPT                 72.04              60.33         48.94          54.12          0.4590    0.3380
                       FAID                    93.31              92.40         94.44          93.25          0.1691    0.1167
                       LLM-DetectAIve          62.93              66.74         71.17          61.97          0.4479    0.3964
  Unseen domains and   T5-Sentinel             57.07              49.82         66.61          55.45          0.4314    0.4300
  Unseen generators    SeqXGPT                 40.71              47.95         35.21          40.09          0.8753    0.7086
                       FAID                    66.55              74.44         73.57          72.58          0.3939    0.3167

Table 2: Performance with three labels with unseen data. We use the detector trained on FAIDSet and evaluate on
the unseen datasets. The best results are in bold and the second best are underlined.

             Dataset              Detector             Accuracy ↑         Precision ↑     Recall ↑     F1-macro ↑
                                  LLM-DetectAIve          75.96             76.97          76.90           76.53
                                  T5-Sentinel             75.68             79.85          78.40           78.37
             FAIDSet
                                  SeqXGPT                 69.41             68.02          64.20           66.03
                                  FAID                    79.64             83.28          83.52           83.27
                                  LLM-DetectAIve          90.49             90.64          83.52           86.93
                                  T5-Sentinel             81.54             81.37          80.09           81.05
             LLM-DetectAIve
                                  SeqXGPT                 87.12             78.90          76.08           74.41
                                  FAID                    90.89             88.17          86.72           87.37
                                  LLM-DetectAIve          89.00             87.87          86.74           87.15
                                  T5-Sentinel             78.52             77.13          78.34           77.59
             HART
                                  SeqXGPT                 64.70             55.82          45.40           50.75
                                  FAID                    89.96             91.57          86.48           86.67

 Table 3: Accuracy of identifying generators: human, GPT, Gemini, Deepseek, and Llama. The best is in bold.


   FAID further improves generalization perfor-                    Language         Accuracy   Precision     Recall    F1-macro
mance over unseen domains and generators com-                      English           96.41         96.02      95.59     95.77
pared to others as illustrated in Table 2. We can                  Vietnamese        94.42         95.60      94.22     94.76
see that generalizing to (ii) unseen domains and
(iv) unseen domain & generator remains challeng-                   Table 4: Language-wise performance on FAIDSet.
ing, with accuracy of 62.78% and 66.55%, re-
spectively. These results suggest that FAID is an                LLM-DetectAIve achieves results comparable to
effective method for addressing the multilingual              FAID on the test set of its dataset, except that its pre-
fine-grained LLM-generated text detection task,               cision is slightly lower. FAID’s high performance
improving performance by leveraging multi-level               when dealing with text from diverse known genera-
contrastive learning to capture generalizable stylis-         tors in these datasets indicates that it learned unique
tic differences tied to LLM families, rather than             writing patterns and features of different generators
overfitting to surface-level artifacts.                       by leveraging multi-level contrastive learning.

                                                              5.5         Language-wise Performance
5.4 Identifying Different Generators
                                                              Table 4 presents the classification performance of
The goal of FAID is not only to detect whether                FAID on each language of FAIDSet. The results
AI was used to produce the target text, but also              show that FAID achieves consistently strong per-
to identify the specific LLM family, treating the             formance across both subsets. While performance
families as distinct authors. As shown in Table               on English is slightly higher, FAID maintains com-
3, FAID consistently achieves higher performance              petitive accuracy and F1-score on Vietnamese, in-
compared to other baselines in almost all evaluation          dicating that the model does not rely solely on
measures.                                                     high-resource language features.
                                                          3282
5.6 Generalizability to Unseen Human–LLM                    The interactions were open-ended but were
    type of Collaboration                                guided by three types of collaboration commonly
To assess FAID’s robustness to unseen collabora-         encountered in two real-world use cases: writing
tive writing patterns between humans and LLMs,           a paper summary (as an abstract) and writing a
we conducted an additional experiment focusing           passage for their own graduation thesis.Each partic-
on hybrid authorship styles that were not present in     ipant was asked to generate five outputs per model,
the original training dataset.                           yielding a total of 200 real-world text samples. To
   We conducted manual quality control to enhance        ensure authenticity and diversity, the participants
the reliability of our dataset and to ensure the ro-     were encouraged to adjust the prompts iteratively,
bustness of the FAID model. A team of five anno-         to include follow-up clarifications, and to perform
tators, all IT-majored, fluent in English, and aged      light editing, mimicking realistic human–LLM co-
18–25, participated in the annotation process. Each      writing behavior.
annotator was assigned approximately 80 samples,            FAID achieved strong performance, with overall
covering all collaborative writing styles, for a total   accuracy of 88.5%, precision of 85.9%, and re-
of 400 human-reviewed instances across various           call of 89.7%, indicating strong generalizability to
collaboration modes.                                     unseen real-world scenarios despite being trained
   During this manual revision stage, the annotators     only in an in-domain setting.
followed two key quality control principles:
  1. Ensuring logical and informational consis-          6   Conclusion and Future Work
     tency between the outputs and the original
                                                         We presented FAIDSet, a multi-domain, multilin-
     texts, where the output length was controlled
                                                         gual fine-grained LLM-generated text detection
     to be 70–150% of the source length.
                                                         dataset comprising 83k examples, and FAID, a
  2. Improving quality through spelling correction,      framework designed to distinguish between human-
     synonym replacement, and word refinement to         written, LLM-generated, and especially, human–
     ensure natural fluency and stylistic coherence.     LLM collaborative texts in practice.
   FAID was evaluated on this manually curated              FAID integrates multi-level contrastive learning
dataset without further fine-tuning. Despite these       and multi-task auxiliary objectives, treating LLM
samples representing an unseen distribution, the         families as stylistic “authors”, which enables it
model achieved a strong overall accuracy of 84.8%,       to capture subtle linguistic and stylistic cues that
precision of 82.8%, and recall of 85.0% across all       generalize effectively across domains and evolving
collaboration categories. This suggests a strong         generative systems. Moreover, its Fuzzy k-Nearest
generalization capability beyond the data distribu-      Neighbors-based inference and training-free incre-
tions encountered during model development. It           mental adaptation contribute to strong robustness
also highlights FAID’s sensitivity to fine-grained       and adaptability to unseen data.
stylistic blending, where human revision only par-          Our experiments demonstrated that FAID con-
tially conceals the generative footprint of LLMs.        sistently outperforms competitive baselines across
                                                         multiple datasets and settings. Its ability to de-
5.7 Generalizability to Real-World Scenarios             tect nuanced collaborative writing and to adapt to
To further assess FAID’s generalizability beyond         emerging generative models highlights its potential
the controlled benchmark setting, we conducted an        for real-world deployment.
additional user study simulating realistic academic         In future work, we plan to extend FAIDSet to
and professional writing scenarios. The goal was         cover more languages, generators, and domains,
to evaluate whether FAID can maintain detection          particularly low-resource languages and informal
accuracy when applied to authentic, unconstrained        genres such as social media and student writing,
text produced through real interactions with LLMs.       to further enhance cross-lingual and domain ro-
   A group of five volunteers with diverse academic      bustness. We further plan to incorporate adversari-
backgrounds was instructed to engage with four           ally LLM-generated texts as well as more complex
popular AI systems: ChatGPT, Gemini, DeepSeek,           forms of human–LLM collaboration in order to bet-
and Llama 3.1 to generate text resembling authentic      ter capture the evolving dynamics of AI-assisted
student or professional writing.                         text creation.
                                                     3283
Limitations                                              Responsible Use of AI-generated Text Detection.
                                                         FAID is designed to enhance transparency in AI-
While FAID demonstrates strong performance and           assisted writing by enabling the fine-grained detec-
generalization across various domains and LLMs,          tion of AI involvement in text generation. While
several limitations remain. First, although our          this has clear benefits for academic integrity and
dataset is multilingual and multi-domain, it remains     content provenance, we acknowledge the potential
limited in low-resource languages and niche writ-        for misuse. For instance, such tools could be used
ing domains, which may affect performance in             to unfairly penalize individuals in educational or
those contexts. FAIDSet is synthetic by construc-        professional settings based on incorrect or biased
tion. The controlled generation enables causal-          predictions. To mitigate this, we stress that FAID
style analysis, but it under-represents the messy,       is not intended for high-stakes decision-making
tool-chain-specific edits seen in the wild. We miti-     without human oversight.
gate this with diverse prompt paraphrases, manual
spot-checks, and generalization tests to held-out        Bias and Fairness. AI-generated text detection
generators. Second, our framework is based on the        systems may inadvertently encode or amplify bi-
observation that texts produced by LLMs from the         ases present in the training data. FAIDSet has been
same family share similar stylistic features. How-       carefully constructed to include diverse domains
ever, this may break down when a single text is          and languages to reduce such biases. Nonetheless,
influenced by multiple LLMs, e.g., when a human          we encourage ongoing auditing and benchmarking
uses different models for drafting, rewriting, and       of fairness across populations and writing styles,
polishing. In such cases, the resulting style may        and welcome community feedback for further im-
blend traits from multiple LLMs, making it more          provements.
difficult to attribute authorship to a single LLM
                                                         Transparency and Reproducibility. We pro-
family or clearly distinguish collaboration bound-
                                                         mote open research and community contributions,
aries.
                                                         and thus we publish our code and data.
Ethics and Broader Impact
Data Collection and Licenses A primary ethical           References
consideration is the data license. We reused exist-      Mervat Abassy, Kareem Elozeiri, Alexander Aziz,
ing datasets for our research: LLM-DetectAIve,            Minh Ngoc Ta, Raj Vardhan Tomar, Bimarsha Ad-
HART, and IELTS Writing, which have been                  hikari, Saad El Dine Ahmed, Yuxia Wang, Osama
                                                          Mohammed Afzal, Zhuohan Xie, Jonibek Mansurov,
publicly released with clear licenses and well-           Ekaterina Artemova, Vladislav Mikhailov, Rui Xing,
documented terms of use. We adhere to the in-             Jiahui Geng, Hasan Iqbal, Zain Muhammad Mujahid,
tended usage of these datasets.                           Tarek Mahmoud, Akim Tsvigun, Alham Fikri Aji,
                                                          Artem Shelmanov, Nizar Habash, Iryna Gurevych,
Security Implications. FAIDSet streamlines                and Preslav Nakov. 2024. LLM-DetectAIve: A tool
both the creation and the rigorous testing of FAID.       for fine-grained machine-generated text detection. In
                                                          Proceedings of the 2024 Conference on Empirical
By spotting LLM-generated material, FAID helps            Methods in Natural Language Processing: System
preserve academic integrity, flag potential miscon-       Demonstrations, EMNLP ’2024, pages 336–343, Mi-
duct, and protect the genuine contributions of au-        ami, Florida, USA. Association for Computational
thors. More broadly, it supports efforts to prevent       Linguistics.
the misuse of generative technologies, such as cre-      Ekaterina Artemova, Jason S Lucas, Saranya Venkatra-
dential falsification. Detecting LLM-generated con-        man, Jooyoung Lee, Sergei Tilga, Adaku Uchendu,
tent across different languages can be tricky, due         and Vladislav Mikhailov. 2025. Beemo: Benchmark
to the language’s grammar and style. By enabling           of expert-edited machine-generated outputs. In Pro-
                                                           ceedings of the 2025 Conference of the Nations of
robust, multilingual, and multi-generator detection        the Americas Chapter of the Association for Compu-
with accurate results, FAIDSet empowers people             tational Linguistics: Human Language Technologies
everywhere, especially in academic scenarios, to           (Volume 1: Long Papers), NAACL-HLT ’2025, pages
deploy AI responsibly. At the same time, it fosters        6992–7018, Albuquerque, New Mexico. Association
critical digital literacy, giving everyone a clear un-     for Computational Linguistics.
derstanding of both the strengths and the limits of      Guangsheng Bao, Lihua Rong, Yanbin Zhao, Qiji
generative AI.                                             Zhou, and Yue Zhang. 2025. Decoupling content

                                                     3284
  and expression: Two-dimensional detection of AI-          Abhimanyu Dubey, Abhinav Jauhri, Abhinav Pandey,
  generated text. ArXiv preprint, arXiv:2503.00258.           Abhishek Kadian, Ahmad Al-Dahle, Aiesha Letman,
                                                              Akhil Mathur, Alan Schelten, Amy Yang, Angela
Rich Caruana. 1997. Multitask learning. Machine               Fan, et al. 2024. The Llama 3 herd of models. ArXiv
  learning, 28:41–75.                                         preprint, arXiv:2407.21783.
Tuhin Chakrabarty, Philippe Laban, and Chien-Sheng
  Wu. 2025. Can AI writing be salvaged? Mitigating          Liam Dugan, Daphne Ippolito, Arun Kirubarajan,
  idiosyncrasies and improving human-AI alignment             Sherry Shi, and Chris Callison-Burch. 2022. Real
  in the writing process through edits. In Proceed-           or fake text?: Investigating human ability to de-
  ings of the 2025 CHI Conference on Human Factors            tect boundaries between human-written and machine-
  in Computing Systems, CHI ’25, Yokohama, Japan.             generated text. ArXiv preprint, arXiv:2212.12672.
  Association for Computing Machinery.
                                                            Tianyu Gao, Xingcheng Yao, and Danqi Chen. 2021.
Ting Chen, Simon Kornblith, Mohammad Norouzi, and             SimCSE: Simple contrastive learning of sentence em-
   Geoffrey Hinton. 2020. A simple framework for              beddings. In Proceedings of the 2021 Conference
   contrastive learning of visual representations. In         on Empirical Methods in Natural Language Process-
  Proceedings of the 37th International Conference            ing, EMNLP ’2021, pages 6894–6910, Online and
   on Machine Learning, ICML ’20, pages 1597–1607.            Punta Cana, Dominican Republic. Association for
  JMLR.org.                                                   Computational Linguistics.

Yutian Chen, Hao Kang, Vivian Zhai, Liangze Li, Rita        Gemini Team. 2024. Gemini: A family of highly
  Singh, and Bhiksha Raj. 2023. Token prediction              capable multimodal models.  ArXiv preprint,
  as implicit classification to identify LLM-generated        arXiv:2312.11805.
  text. In Proceedings of the 2023 Conference on Em-
  pirical Methods in Natural Language Processing,           John Giorgi, Osvald Nitski, Bo Wang, and Gary Bader.
  EMNLP ’2023, pages 13112–13120, Singapore. As-              2021. DeCLUTR: Deep contrastive learning for un-
  sociation for Computational Linguistics.                    supervised textual representations. ArXiv preprint,
Zihao Cheng, Li Zhou, Feng Jiang, Benyou Wang, and            arXiv:2006.03659.
  Haizhou Li. 2025. Beyond binary: Towards fine-
  grained LLM-generated text detection via role recog-      Xun Guo, Shan Zhang, Yongxin He, Ting Zhang, Wan-
  nition and involvement measurement. In Proceedings          quan Feng, Haibin Huang, and Chongyang Ma. 2024.
  of the ACM on Web Conference 2025, WWW ’25,                 DeTeCtive: Detecting AI-generated text via multi-
  page 2677–2688. ACM.                                        level contrastive learning. In Advances in Neu-
                                                              ral Information Processing Systems, volume 37 of
Hyung Won Chung, Le Hou, Shayne Longpre, Barret               NeurIPS ’2024, pages 88320–88347. Curran Asso-
  Zoph, Yi Tay, William Fedus, Yunxuan Li, Xuezhi             ciates, Inc.
  Wang, Mostafa Dehghani, Siddhartha Brahma, Al-
  bert Webson, Shixiang Shane Gu, Zhuyun Dai,               James Hutson. 2025. Human-AI collaboration in writ-
  Mirac Suzgun, Xinyun Chen, Aakanksha Chowdh-                ing: A multidimensional framework for creative
  ery, Alex Castro-Ros, Marie Pellat, Kevin Robinson,         and intellectual authorship. International Journal
  Dasha Valter, Sharan Narang, Gaurav Mishra, Adams           of Changes in Education.
  Yu, Vincent Zhao, Yanping Huang, Andrew Dai,
  Hongkun Yu, Slav Petrov, Ed H. Chi, Jeff Dean, Ja-        Ryuto Koike, Masahiro Kaneko, and Naoaki Okazaki.
  cob Devlin, Adam Roberts, Denny Zhou, Quoc V. Le,           2024. OUTFOX: LLM-generated essay detection
  and Jason Wei. 2022. Scaling instruction-finetuned          through in-context learning with adversarially gen-
  language models. ArXiv preprint, arXiv:2210.11416.          erated examples. In Proceedings of the 38th AAAI
                                                              Conference on Artificial Intelligence, AAAI ’2024,
Alexis Conneau, Kartikay Khandelwal, Naman Goyal,             pages 21258–21266, Vancouver, Canada.
  Vishrav Chaudhary, Guillaume Wenzek, Francisco
  Guzmán, Edouard Grave, Myle Ott, Luke Zettle-             Laida Kushnareva, Tatiana Gaintseva, German Magai,
  moyer, and Veselin Stoyanov. 2020. Unsupervised             Serguei Barannikov, Dmitry Abulkhanov, Kristian
  cross-lingual representation learning at scale. In Pro-     Kuznetsov, Eduard Tulchinskii, Irina Piontkovskaya,
  ceedings of the 58th Annual Meeting of the Asso-            and Sergey Nikolenko. 2024. AI-generated text
  ciation for Computational Linguistics, ACL ’2020,           boundary detection with RoFT. ArXiv preprint,
  pages 8440–8451, Online.                                    arXiv:2311.08349.
DeepSeek-AI. 2025. DeepSeek-V3 technical report.
  ArXiv preprint, arXiv:2412.19437.                         Mina Lee, Percy Liang, and Qian Yang. 2022. CoAu-
                                                              thor: Designing a human-AI collaborative writing
Matthijs Douze, Alexandr Guzhva, Chengqi Deng,                dataset for exploring language model capabilities.
 Jeff Johnson, Gergely Szilvasy, Pierre-Emmanuel              In Proceedings of the 2022 CHI Conference on Hu-
 Mazaré, Maria Lomeli, Lucas Hosseini, and Hervé              man Factors in Computing Systems, CHI ’22, New
 Jégou. 2025. The Faiss library. ArXiv preprint,              Orleans, LA, USA. Association for Computing Ma-
 arXiv:2401.08281.                                            chinery.

                                                        3285
Yafu Li, Qintong Li, Leyang Cui, Wei Bi, Zhilin Wang,         International Workshop on Semantic Evaluation, Se-
  Longyue Wang, Linyi Yang, Shuming Shi, and Yue              mEval ’2024, pages 2057–2079, Mexico City, Mex-
  Zhang. 2024. MAGE: Machine-generated text detec-            ico. Association for Computational Linguistics.
  tion in the wild. In Proceedings of the 62nd Annual
  Meeting of the Association for Computational Lin-        Yuxia Wang, Jonibek Mansurov, Petar Ivanov, Jinyan
  guistics (Volume 1: Long Papers), ACL ’2024, pages         Su, Artem Shelmanov, Akim Tsvigun, Osama Mo-
  36–53, Bangkok, Thailand. Association for Compu-           hammed Afzal, Tarek Mahmoud, Giovanni Puccetti,
  tational Linguistics.                                      Thomas Arnold, Alham Aji, Nizar Habash, Iryna
                                                             Gurevych, and Preslav Nakov. 2024d. M4GT-Bench:
Yinhan Liu, Myle Ott, Naman Goyal, Jingfei Du, Man-          Evaluation benchmark for black-box machine-
  dar Joshi, Danqi Chen, Omer Levy, Mike Lewis,              generated text detection. In Proceedings of the 62nd
  Luke Zettlemoyer, and Veselin Stoyanov. 2019.              Annual Meeting of the Association for Computational
  RoBERTa: A robustly optimized BERT pretraining             Linguistics (Volume 1: Long Papers), ACL ’2024,
  approach. ArXiv preprint, arXiv:1907.11692.                pages 3964–3992, Bangkok, Thailand. Association
                                                             for Computational Linguistics.
Dominik Macko, Robert Moro, and Ivan Srba. 2025. In-
  creasing the robustness of the fine-tuned multilingual   Yuxia Wang, Jonibek Mansurov, Petar Ivanov, Jinyan
  machine-generated text detectors. ArXiv preprint,          Su, Artem Shelmanov, Akim Tsvigun, Chenxi White-
  arXiv:2503.15128.                                          house, Osama Mohammed Afzal, Tarek Mahmoud,
                                                             Toru Sasaki, Thomas Arnold, Alham Fikri Aji,
OpenAI. 2024. GPT-4o system card. ArXiv preprint,            Nizar Habash, Iryna Gurevych, and Preslav Nakov.
  arXiv:2410.21276.                                          2024e. M4: Multi-generator, multi-domain, and
                                                             multi-lingual black-box machine-generated text de-
Shoumik Saha and Soheil Feizi. 2025. Almost AI, al-          tection. In Proceedings of the 18th Conference of
  most human: The challenge of detecting AI-polished         the European Chapter of the Association for Com-
  writing. ArXiv preprint, arXiv:2502.15666.                 putational Linguistics (Volume 1: Long Papers),
                                                             EACL ’2024, pages 1369–1407, St. Julian’s, Malta.
Jinyan Su, Terry Zhuo, Di Wang, and Preslav Nakov.
   2023. DetectLLM: Leveraging log rank information        Yuxia Wang, Artem Shelmanov, Jonibek Mansurov,
   for zero-shot detection of machine-generated text. In     Akim Tsvigun, Vladislav Mikhailov, Rui Xing, Zhuo-
   Findings of the Association for Computational Lin-        han Xie, Jiahui Geng, Giovanni Puccetti, Ekaterina
   guistics, EMNLP ’2023, pages 12395–12412, Singa-          Artemova, Jinyan Su, Minh Ngoc Ta, Mervat Abassy,
   pore. Association for Computational Linguistics.          Kareem Ashraf Elozeiri, Saad El Dine Ahmed El Et-
                                                             ter, Maiya Goloburda, Tarek Mahmoud, Raj Vardhan
Jannis Vamvas and Rico Sennrich. 2023. Towards un-           Tomar, Nurkhan Laiyk, Osama Mohammed Afzal,
  supervised recognition of token-level semantic dif-        Ryuto Koike, Masahiro Kaneko, Alham Fikri Aji,
  ferences in related documents. In Proceedings of           Nizar Habash, Iryna Gurevych, and Preslav Nakov.
  the 2023 Conference on Empirical Methods in Natu-          2025. GenAI content detection task 1: English and
  ral Language Processing, EMNLP ’2023, Singapore.           multilingual machine-generated text detection: AI
  Association for Computational Linguistics.                 vs. human. In Proceedings of the 1st Workshop on
Liang Wang, Nan Yang, Xiaolong Huang, Binxing                GenAI Content Detection, GenAIDetect, pages 244–
  Jiao, Linjun Yang, Daxin Jiang, Rangan Majumder,           261, Abu Dhabi, UAE.
  and Furu Wei. 2024a. Text embeddings by weakly-          Zijie Zeng, Shiqi Liu, Lele Sha, Zhuang Li, Kaixun
  supervised contrastive pre-training. ArXiv preprint,       Yang, Sannyuya Liu, Dragan Gašević, and Guan-
  arXiv:2212.03533.                                           liang Chen. 2024. Detecting AI-generated sentences
                                                              in human-AI collaborative hybrid texts: Challenges,
Liang Wang, Nan Yang, Xiaolong Huang, Linjun Yang,
                                                              strategies, and insights. In Proceedings of the Thirty-
  Rangan Majumder, and Furu Wei. 2024b. Multilin-
                                                             Third International Joint Conference on Artificial
  gual E5 text embeddings: A technical report. ArXiv
                                                              Intelligence, IJCAI ’24, Jeju, Korea.
  preprint, arXiv:2402.05672.
                                                           Zijie Zeng, Lele Sha, Yuheng Li, Kaixun Yang, Dra-
Pengyu Wang, Linyang Li, Ke Ren, Botian Jiang, Dong
                                                              gan Gašević, and Guanliang Chen. 2023. Towards
  Zhang, and Xipeng Qiu. 2023. SeqXGPT: Sentence-
                                                              automatic boundary detection for human-AI collab-
  level AI-generated text detection. In Proceedings of
                                                              orative hybrid essay in education. ArXiv preprint,
  the 2023 Conference on Empirical Methods in Nat-
                                                              arXiv:2307.12267.
  ural Language Processing, EMNLP ’2023, pages
  1144–1156, Singapore. Association for Computa-           Qihui Zhang, Chujie Gao, Dongping Chen, Yue Huang,
  tional Linguistics.                                        Yixin Huang, Zhenyang Sun, Shilin Zhang, Weiye
                                                             Li, Zhengyan Fu, Yao Wan, and Lichao Sun. 2024.
Yuxia Wang, Jonibek Mansurov, Petar Ivanov, Jinyan           LLM-as-a-Coauthor: Can mixed human-written and
  Su, Artem Shelmanov, Akim Tsvigun, Osama Mo-               machine-generated text be detected? In Findings
  hammed Afzal, Tarek Mahmoud, Giovanni Puccetti,            of the Association for Computational Linguistics,
  and Thomas Arnold. 2024c. SemEval-2024 task 8:             NAACL ’2024, pages 409–436, Mexico City, Mex-
  Multidomain, multimodel and multilingual machine-          ico. Association for Computational Linguistics.
  generated text detection. In Proceedings of the 18th

                                                       3286
Appendix                                                      • LLM-paraphrased: Texts that were initially
                                                                written by a human and then reworded by an
A     Some Current Datasets on                                  LLM system to express the same meaning
      AI-generated Texts                                        using different phrasing, possibly altering sen-
                                                                tence structure or word choice while preserv-
We review existing datasets for AI-generated text
                                                                ing the original message.
detection and summarize their key characteristics
in Table 5. While many of these datasets provide              By mixing prompts across these categories, we
fine-grained labels and cover multiple text gener-        generate a balanced corpus that mitigates over-
ators, all are monolingual and limited to English.        fitting to any one prompt pattern and better reflects
This limitation highlights a critical gap in current      the diversity of real user queries.
resources and motivates the construction of a new
multilingual, multi-domain, and multi-generator           C     Experimental Details and Real-World
dataset for AI-generated text detection, which is               Use Cases
essential for developing methods that generalize to
real-world, cross-lingual scenarios.                      C.1    Experimental Setup
                                                          Unless noted otherwise, we use a batch size of
B     FAIDSet Statistics and Analysis                     64, the AdamW optimizer with a learning rate of
                                                          2×10−5 and weight decay of 10−4 , 50 epochs, and
B.1    Statistics                                         2000 warm-up steps. For the fuzzy kNN compo-
Our FAIDSet includes 83,350 examples, which are           nent, we set top-K to 20, and we use a temperature
divided into three subsets: train, validation, and        of 0.7.
test, with the ratios shown in Table 6. The dataset
                                                          C.2    Computational Cost
also comprises various sources of human-written
text, as described in Table 7.                            We run all experiments on a single NVIDIA A100
                                                          (40 GB). The total wall-clock training time for
B.2    Diverse Prompt Strategies                          FAID on FAIDSet is approximately 5 hours.
                                                             In our setup using FAISS (Douze et al., 2025)
In order to avoid biasing our generated corpora
                                                          with CPU inference, the average query latency is
toward some style or topic, we use a broad set
                                                          approximately 5ms for FAIDSet with 83k embed-
of prompt templates when synthesizing LLM-
                                                          dings on a standard server (Intel Xeon CPU, 64GB
generated and human–LLM collaborative texts. By
                                                          RAM). When performing with Fuzzy KNN, it takes
varying prompt structures, content domains, and
                                                          some small period of time to process, and thus the
complexity, we ensure that the resulting outputs
                                                          total average time for inference is 10ms.
cover a wide variety of writing patterns, vocabu-
lary, and rhetorical devices. This diversity helps our    C.3    Real-world Management of Vector
detector generalize more effectively to real-world               Database
inputs.
                                                          For FAIDSet, our entire training and validation
   Concretely, we use five prompts for LLM-
                                                          embedding store requires approximately 200 MB,
generated texts in Table 8 and several categories
                                                          which is easily handled by standard server disks.
of human–LLM collaborative texts in Tables 9, 10,
                                                            For larger datasets, we believe the system re-
and 11, consecutively:
                                                          mains scalable:
    • LLM-polished: Texts that a human initially              • FAISS supports disk-based indices and opti-
      wrote and then lightly refined by an LLM sys-             mized search methods to keep memory usage
      tem to improve grammar, clarity, or fluency               low even with millions of vectors.
      without altering the core content or intent.
                                                              • Modern servers with hundreds of GB of disk
    • LLM-continued: Texts where a human wrote                  are sufficient for storing large embedding
      an initial portion (e.g., a sentence or para-             banks, and the use of CPU-only inference
      graph), and an LLM generated a continuation               (since Fuzzy KNN is GPU-free) makes the
      that attempts to follow the original style, tone,         architecture cost-effective for deployment in
      and intent.                                               resource-constrained environments.
                                                      3287
Dataset                       Languages   Label Space                     Domains                  Generators             Size
                                                                          Email
                                          Human-written, AI-polished      News
                                                                                                   GPT-4
MixSet                                    Human-initiated, -continued     Game reviews,
                              English                                                              Llama 2               3,600
(Zhang et al., 2024)                      AI-written, human-edited        Paper abstracts,
                                                                                                   Dolly
                                          Deeply-mixed text               Speech,
                                                                          Blog
                                                                          arXiv abstracts,         GPT-4o
                                          Human-written                   Reddit posts,            Mistral 7B
DetectiAIve                               AI-generated                    Wikihow,                 Llama 3.1 8B
                              English                                                                                  487,996
(Abassy et al., 2024)                     Human-written, AI-polished      Wikipedia articles,      Llama 3.1 70B
                                          AI-written, AI-humanized        OUTFOX essays,           Gemini
                                                                          Peer reviews             Cohere
                                                                                                   Llama 2
                                                                                                   Llama 3.1
                                                                          Generation,
                                          AI-generated, AI-humanized                               GPT-4o
                                                                          Rewrite,
Beemo                                     Human-written                                            Zephyr
                              English                                     Open QA,                                      19,256
(Artemova et al., 2025)                   AI-generated                                             Mixtral
                                                                          Summarize,
                                          AI-written, human-edited                                 Tulu
                                                                          Closed QA
                                                                                                   Gemma
                                                                                                   Mistral
                                          Human-written, AI-continued                              Llama 2
M4GT                                                                      Peer review,
                              English     Human-written                                            GPT-4                33,912
(Wang et al., 2024d)                                                      OUTFOX
                                          AI-generated                                             GPT-3.5
                                                                          Recipes,
                                                                                                   GPT-2,
Real or Fake                              Human-written                   Presidential Speeches,
                              English                                                              GPT-2 XL              9,148
(Dugan et al., 2022)                      Human-initiated, AI-continued   Short Stories,
                                                                                                   CTRL
                                                                          New York Times
                                                                          Short Stories,
RoFT-chatgpt                                                              Recipes,
                              English     Human-initiated, AI-continued                            GPT-3.5-turbo         6,940
(Kushnareva et al., 2024)                                                 New York Times,
                                                                          Presidential Speeches
Co-author                                                                 Creative writing,
                              English     Deeply-mixed text                                        GPT-3                 1,447
(Zeng et al., 2024)                                                       New York Times
                                          Human-initiated, AI-continued
TriBERT
                              English     Deeply-mixed text               Essays                   ChatGPT              34,272
(Zeng et al., 2023)
                                          Human-written
                                                                                                   GPT-4o
LAMP
                              English     AI-generated, human-edited      Creative writing         Claude 3.5 Sonnet     1,282
(Chakrabarty et al., 2025)
                                                                                                   Llama 3.1 70B
                                                                                                   GPT-4o
APT-Eval                                                                                           Llama 3.1 70B
                              English     Human-written, AI-polished      Based on MixSet                               11,700
(Saha and Feizi, 2025)                                                                             Llama 3.1 8B
                                                                                                   Llama 2 7B
                                                                                                   GPT-3.5-turbo
                                          Human-written
                                                                                                   GPT-4o
                                          Human-written, AI-polished
HART                                                                                               Claude 3.5 Sonnet
                              English     AI-generated, AI-humanized                                                    16,000
(Bao et al., 2025)                                                                                 Gemini 1.5 Pro
                                          AI-generated text
                                                                                                   Llama 3.3 70B
                                          AI-generated, human-edted
                                                                                                   Qwen 2.5 72B
                                          Human-written                                            DeepSeek v2
LLMDetect                                 Human-written, AI-polished                               Llama 3 70B
                              English                                                                                   64,304
(Cheng et al., 2025)                      Human-written, AI-extended                               Claude 3.5 Sonnet
                                          AI-generated                                             GPT-4o
                                                                                                   Qwen 2.5
ICNALE corpus                                                                                      Llama 3.1 8B/70B
                              English     Human-written                   Essays                                        67,000
(Macko et al., 2025)                                                                               Llama 3.2 1B/3B
                                                                                                   Mistral Small

                        Table 5: English fine-grained AI-generated text detection datasets overview.




                                                              3288
    Subset       Human     LLM       Human–LLM              This reinforces the hypothesis that text length is
                                       collab.            not only model-dependent but also family-coherent,
    Train         14,176   12,076          32,091         with Gemini models forming a distinct cluster.
    Validation     3,038    2,588           6,876
    Test           3,038    2,588           6,879         D.2   Text Distribution between LLMs within
                                                                the Same Family
Table 6: Number of examples per label in subsets in the
FAIDSet dataset.                                          We performed N-gram frequency analysis on re-
                                                          sponses generated by three models within the Gem-
       Source                       Human Texts           ini family: Gemini 2.0, Gemini 2.0 Flash, and
       arXiv abstracts                    2,000
                                                          Gemini 1.5 Flash using 500 texts from the arXiv
       VJOL abstracts                     2,195           abstract dataset. Figure 5 highlights overlapping
       HUST theses (English)              4,898           high-frequency tokens and similar patterns in word
       HUST theses (Vietnamese)          11,159
                                                          usage and phrase structure among the three models.
Table 7: Statistics of human-written text’s origins in       Despite minor differences in architectural speed
FAIDSet.                                                  (e.g., Flash vs. regular) or release chronology,
                                                          the N-gram distributions show minimal diver-
                                                          gence. Frequently used tokens, such as domain-
D    Analysis on Similarity across Models                 specific terms and transitional phrases, appeared
     and Model Families                                   with nearly identical frequencies. This suggests
                                                          that these models share similar decoding strategies
To assess the stylistic and semantic consistency          and training biases, likely due to shared pretraining
of AI-generated texts, we conducted a comprehen-          corpora and optimization techniques resulting in
sive analysis across multiple perspectives, includ-       highly consistent stylistic patterns.
ing N-gram distributions, text length patterns, and          These intra-family similarities support treating
semantic embedding visualizations. This allowed           model variants within a family as a unified author-
us to study the similarities within and across model      ing entity when performing analysis or authorship
families, leading to a robust understanding of AI         attribution.
“authorship” characteristics.
                                                          D.3   Embedding Visualization and Semantic
D.1 Text Distribution between LLM Families                      Cohesion
We analyzed the distribution of text length, mea-         To explore semantic alignment in detail, we vi-
sured by both word and character counts, across           sualized the embeddings generated by an unsu-
outputs from five LLMs: Llama-3.3-70B-Instruct-           pervised SimCSE XLM-RoBERTa-base model on
Turbo (Dubey et al., 2024), GPT-4o-mini (Ope-             texts from two model families, Gemini and GPT,
nAI, 2024), Gemini 2.0, Gemini 2.0 Flash-Lite,            using PCA to project the high-dimensional embed-
and Gemini 1.5 Flash (Gemini Team, 2024). Using           dings into a lower-dimensional space for analysis.
2,000 arXiv prompt seeds, each model generated a             As shown in Figure 4, Gemini model embed-
single output, and we plotted the resulting length        dings form tight, overlapping clusters, indicating
distributions.                                            a high degree of semantic cohesion and internal
   The results are shown in Figure 3, where we            consistency among their outputs. This clustering
can observe that clear family-level patterns emerge.      behavior remains stable across both sample sizes of
Gemini models consistently produce shorter, more          2,000 texts, suggesting that the observed patterns
compact outputs, whereas Llama and GPT mod-               are not driven by sampling artifacts. In contrast,
els exhibit greater variance and a stronger ten-          GPT-4o/4o-mini embeddings occupy a distinct re-
dency toward longer completions. Despite differ-          gion of the embedding space, exhibiting greater dis-
ences across versions (e.g., Gemini 2.0 vs. Gem-          persion and noticeably less overlap with the Gemini
ini 1.5 Flash), Gemini outputs remain tightly clus-       clusters.
tered in both word and character counts, indicating          Overall, this visualization confirms that the Gem-
a shared generation strategy and strong stylistic         ini family not only shares stylistic features, but
consistency within the family. In contrast, Llama         also demonstrates strong semantic coherence, ef-
and GPT distributions show greater dispersion and         fectively distinguishing it from models belonging
inter-model variability.                                  to other families at a deeper conceptual level.
                                                      3289
 Student Thesis                                                                     Paper Abstract


                                                                                    • Assume the role of a researcher with experience in writing abstracts for
                                                                                      scientific papers. Write a short paragraph of approximately 150-200 words
                                                                                      based on the topic conveyed by the provided file name. Start directly with
 • You are a university student majoring in computer science. Please briefly          the topic, presenting it clearly, objectively, and in a concise academic style.
   summarize the main idea of the following paragraph. After that, rewrite the        Use correct spelling and grammar, and write in a scholarly tone. Topic name:
   paragraph based on this content. Write naturally in an academic style. The
   rewritten paragraph should be approximately the same length in characters
   as the original. The original text is:                                           • You are a computer scientist who is very familiar with abstract writing for
                                                                                      your works, based on the title. Craft a concise word_count-word abstract
 • In clear, structured prose, draft the section for a thesis titled , cite some      for a paper titled       , summarizing the problem statement, methodology,
   related works you mentioned in the passage, and highlight the contribution.        key findings, and contributions. The original text:             . Compose a
   The original text is:         . Please begin by briefly summarizing the main       word_count-word abstract for the paper            , ensuring it includes moti-
   idea of the paragraph to ensure full comprehension and retention of all            vation, approach, results, and implications for future research.
   essential content. Then, rewrite the paragraph in a formal academic style,
   consistent with a university-level thesis. The rewritten section should read     • Act like a senior researcher acting as a peer reviewer. Your task is to analyze
   naturally, be coherent within the context of an academic paper, and have           and then rewrite the provided abstract to improve its structure and clarity.
   approximately the same character length as the original.                           Deconstruct the abstract: First, examine the original text and break it down
                                                                                      into four key components: What is the core problem being addressed?; What
 • Assume the role of a senior software engineer. Your task is to process a para-     is the proposed solution or methodology?; What were the key results of the
   graph from a computer science thesis using a two-step method. Firstly, you         experiments?; What is the main contribution or impact of this work? After
   must summarize by deconstruction, which involves analyzing the original            that, you must reconstruct the information from the components using only
   text and providing a structured summary by identifying its primary purpose,        the data from your deconstructed points, and synthesize a new, cohesive
   key input parameters, and main outcomes. Secondly, rewrite the paragraph           abstract of approximately 150-200 words. Original abstract:             .
   based on the structured summary. The new version must be technically
   precise, unambiguous, and logically structured, making it easy for another       • You are a research scientist specializing in the sub-field suggested by the
   engineer to understand. The original text is:       .                              paper’s title. Your task is to generate a plausible abstract based only on the
                                                                                      title. Based on the title, first generate a bulleted list of the likely components
 • You are a research scientist preparing a paper for a top-tier computer science     this paper would cover: the specific problem it probably addresses, the
   conference. The original text is:         . For the following paragraph from       methodology it might propose, the kind of results one would expect, and
   a thesis draft, you have to summarize the core contribution, which can be          its potential impact or contribution to the field. After that, weave these
   earned by beginning with providing a concise, one-sentence summary that            hypothesized points into a compelling and professional abstract of 150-200
   captures the main scientific contribution or key finding of the paragraph.         words. Write it as if you were the author, confidently presenting your work.
   Then, rewrite the paragraph for publication by using the summary as a guide,       Paper title:
   ensuring it is written in a formal, objective, and precise tone suitable for a
   peer-reviewed publication. Ensure the rewritten text is information-dense        • You are a technical writer for a prestigious AI research blog. Your goal
   yet easy for a fellow researcher to follow.                                        is to rewrite a standard academic abstract to make it more impactful and
                                                                                      highlight its core breakthrough for a broader technical audience. First, read
 • You are a university student majoring in computer science. You need to             the original abstract and identify the single most important takeaway or
   extract the main idea by writing a summary of the paragraph’s main idea.           the core breakthrough of the paper and summarize this in one sentence.
   Rewrite the paragraph based on the content you have summarized. The                Second, rewrite the abstract to be approximately 150-200 words in length.
   rewritten text should be in a formal academic style, read naturally, be coher-     Start with a strong opening sentence that directly states the problem or the
   ent, and have approximately the same character length as the original. The         breakthrough you identified. Then, briefly explain the methodology and
   original paragraph is:                                                             results, always connecting them back to why they are important. The tone
                                                                                      should be highly professional but more engaging than a typical arXiv abstract.
                                                                                      Preserve all technical terms and citations accurately. Paper title:          .
                                                                                      Original abstract:        .



             Table 8: List of diverse prompt templates used to generate FAIDSet – Label: LLM-generated.


D.4 Conclusion                                                                          Each transformer-based encoder was fine-tuned
The consistency observed across N-gram distribu-                                     on FAIDSet training data and then used to predict
tions, text length patterns, and semantic embed-                                     labels on the two evaluation splits. Table 12 sum-
dings among Gemini models substantiates our deci-                                    marizes the accuracy, F1-macro, Mean Squared
sion to treat each LLM family as an author. These                                    Error (MSE), and Mean Absolute Error (MAE) for
models demonstrate coherent writing styles, shared                                   each model under both conditions.
lexical preferences, and tightly clustered seman-                                    Base model comparison. We first evaluated
tic representations, hallmarks of unified author-                                    three popular monolingual models: RoBERTa-base,
ship. Conversely, inter-family comparisons show                                      Flan-T5-base, and e5-base-v2 using the same train-
clear separability, emphasizing the distinctiveness                                  ing and evaluation splits. RoBERTa-base (Liu et al.,
of each LLM family’s writing behavior.                                               2019) and e5-base-v2 (Wang et al., 2024a) achieved
                                                                                     the most balanced trade-off between classification
E     Model Selection for Detector
                                                                                     accuracy and regression error (MSE, MAE), while
In order to identify the best encoder for our classifi-                              Flan-T5-base (Chung et al., 2022) lagged slightly
cation task, we evaluated each candidate model on                                    in F1-macro. These results indicate that a stronger
both known generators (in the FAIDSet test data)                                     encoder backbone yields more robust performance,
and the new unseen-generators test set, which is                                     motivating the exploration of multilingual variants
introduced in Section 3.                                                             for further gains.
                                                                               3290
 Student Thesis                                                                       Paper Abstract


                                                                                      • You are a researcher who has been assigned the task of polishing the para-
 • You are a university student majoring in computer science who has been
                                                                                        graph below, which is excerpted from an undergraduate thesis. Improve
   assigned the task of polishing the paragraph below, which is excerpted from
                                                                                        the paragraph to make it clearer, more coherent, and more precise, while
   an undergraduate thesis. Improve the paragraph to make it clearer, more
                                                                                        maintaining the original author’s academic tone and writing style. Do not
   coherent, and more precise, while maintaining the original author’s academic
                                                                                        rephrase any reference materials, figure labels, or citations—preserve them
   tone and writing style. Do not rephrase any reference materials, figure labels,
                                                                                        exactly as they appear in the original paragraph. The original text:      .
   or citations preserve them exactly as they appear in the original paragraph.
   The original text:        .
                                                                                      • You are a scientist who is very familiar with abstract writing and refining
                                                                                        the written abstract. Improve the coherence, precision, and formal tone
 • You are a meticulous academic editor with a specialization in computer
                                                                                        of this draft abstract without introducing new content. Provide only the
   science theses. Your task is to polish the following paragraph for conciseness
                                                                                        polished version, without any introductory or explanatory text. The original
   and impact. Focus on eliminating redundant words and phrases, replacing
                                                                                        text:       .
   weak verb constructions with stronger, more active verbs, and ensuring
   each sentence contributes directly and efficiently to the paragraph’s central
   point. The core technical meaning, all specific terminology, citations, and        • Improve the clarity and conciseness of this abstract paragraph while main-
   references to figures must be preserved precisely. The original text:         .      taining all original findings and terminology. Provide only the polished
                                                                                        version, without any introductory or explanatory text. The original text:
                                                                                               .
 • Assume you are an IT student who is refining your work to make it more
   complete. Refine the following section excerpt for grammar, clarity, and aca-
   demic style while preserving its original meaning and terminology. Provide         • You are a program chair for a leading academic conference, skilled at identi-
   only the polished version, without any introductory or explanatory text. The         fying impactful research. Your task is to polish the following arXiv abstract
   original text:       .                                                               to maximize its impact and make its core contribution immediately appar-
                                                                                        ent. Focus on sharpening the opening sentence to act as a compelling hook.
                                                                                        Rephrase and reorder sentences as needed to clearly convey the main findings
 • Act as a PhD candidate reviewing a section of an undergraduate thesis. Your
                                                                                        and highlight the significance of the work. All original terminology, data,
   primary goal is to enhance the logical flow and argumentative coherence
                                                                                        and citations must be strictly preserved. Provide only the polished version
   of the paragraph below. Revise the text to ensure that sentences connect
                                                                                        as a single, continuous paragraph. The original text:         .
   seamlessly with clear transitions. The paragraph should build a coherent
   argument from the opening sentence to the conclusion. Do not introduce new
   information or alter the original technical content, terminology, or references.   • You are a meticulous editor for a top-tier scientific journal, such as Nature or
   Your focus is solely on restructuring the existing information to create a           Science. Your objective is to polish the following arXiv abstract to enhance
   stronger, more persuasive, and logical narrative. The original text:          .      its technical precision and information density. Scrutinize every word to
                                                                                        ensure it is the most accurate choice. Refine phrasing to eliminate any
                                                                                        ambiguity and, where supported by the text, replace qualitative descriptions
 • You are a fourth-year IT student who is refining your work to make it more
                                                                                        with more specific, quantitative statements. The goal is a text where every
   complete. Enhance the academic tone, coherence, and logical flow of this
                                                                                        clause delivers critical information efficiently. Do not alter the scientific
   thesis section without altering technical content. The original text:    .
                                                                                        findings, technical terms, or citations. The original text:         .



              Table 9: List of diverse prompt templates used to generate FAIDSet – Label: LLM-polished.


Multilingual variants. We next evaluated                                                 Based on these experiments, we selected the
XLM-RoBERTa-base (Conneau et al., 2020) and                                            unsupervised SimCSE XLM-RoBERTa-base
Multilingual-e5-base (Wang et al., 2024b). Both                                        model for our final system.
models benefit from cross-lingual pretraining,
which in our setting improves the representation                                       F      Ablation Study
of the diverse linguistic patterns present in
FAIDSet. Notably, XLM-RoBERTa-base yields                                              F.1      The Need to Use a Vector Database
a substantial improvement across all evaluation                                        We first applied the trained model to classify the
metrics, indicating that its multilingual training                                     input text and observed a substantial performance
enhances generalization even when applied to                                           drop of 15–30% when evaluated on unseen data.
predominantly monolingual inputs.                                                      This degradation underscores the model’s limited
                                                                                       ability to generalize beyond its training distribu-
Contrastive learning with SimCSE. Finally, we                                          tion and its sensitivity to distributional shifts. To
incorporated contrastive learning via SimCSE (Gao                                      address this issue, we decided to integrate a vector
et al., 2021) to refine sentence embeddings. We                                        database that stores dense embeddings of all ex-
evaluated supervised (trained on NLI data) and                                         amples, including both labeled instances and unla-
unsupervised (trained on the Wikipedia corpus)                                         beled data encountered during inference. By index-
SimCSE variants applied to RoBERTa-base. The                                           ing and retrieving semantically similar examples
unsupervised variant outperformed its supervised                                       during inference, the vector database serves as a
counterpart, aligning with prior findings that unsu-                                   flexible, scalable memory module that helps bridge
pervised SimCSE produces stronger semantic en-                                         the gap between the training and test distributions.
coders. Based on these results, we applied unsuper-                                    This retrieval-based mechanism enhances the clas-
vised SimCSE to XLM-RoBERTa-base (Vamvas                                               sifier’s robustness to domain shifts and unseen gen-
and Sennrich, 2023), achieving the highest accu-                                       erators by grounding predictions in stylistically and
racy and lowest error rates.                                                           semantically related examples.
                                                                                 3291
 Student Thesis                                                                     Paper Abstract


 • You are a university student majoring in computer science who has been
   assigned the task of continuing the content of the paragraph below, which is     • You are a researcher who has been assigned the task of continuing the content
   excerpted from an undergraduate thesis. Please continue the text naturally,        of the paragraph below, which is excerpted from an undergraduate thesis.
   striving to mimic the tone and writing style of the given paragraph to avoid       Please continue the text naturally, striving to mimic the tone and writing
   any inconsistency in expression, while ensuring clarity and coherence in an        style of the given paragraph to avoid any inconsistency in expression, while
   academic style. Do not rephrase the reference materials, figure labels, or         ensuring clarity and coherence in an academic style. Do not rephrase the
   citations-preserve them exactly as they appear in the original paragraph. The      reference materials, figure labels, or citations-preserve them exactly as they
   original text:        .                                                            appear in the original paragraph. The original text:

 • You are an IT student who is writing your graduation thesis. Continue to         • You are a scientist who is very familiar with abstract writing. Add some con-
   write the section from file name          thesis excerpt for approximately         cise concluding sentences to this partial abstract that highlight implications
   word_count words, maintaining formal academic structure and style. Do              for future research. Do not rephrase the reference materials, figure labels, or
   not rephrase the reference materials, figure labels, or citations—preserve         citations-preserve them exactly as they appear in the original paragraph. The
   them exactly as they appear in the original paragraph. The original text:          original text:        .
          .
                                                                                    • Continue the abstract by writing a closing statement that underscores the
 • Act like an IT student who is writing your graduation thesis. Extend the           study’s contributions and potential applications. Do not rephrase the ref-
   section by adding supporting detailed information for a thesis on            .     erence materials, figure labels, or citations-preserve them exactly as they
   Do not rephrase the reference materials, figure labels, or citations—preserve      appear in the original paragraph. The original text:       .
   them exactly as they appear in the original paragraph. The original text:
          .                                                                         • You are a research scientist continuing the draft of a paper’s abstract. The
                                                                                      provided text introduces the core problem or context. Your task is to continue
 • You are a computer science researcher meticulously documenting your work.          the abstract by providing a concise description of the proposed methodology
   Your task is to continue the paragraph starting with the sentence below.           or approach. Detail the key techniques, model architecture, or experimental
   The continuation must elaborate on the underlying mechanism, process, or           setup used to address the problem, ensuring the description is plausible for a
   rationale implied by the initial statement, effectively answering the how or       paper titled         . The continuation must seamlessly connect to the initial
   why. The completed paragraph should be logically sound and consistent              text to form a single, coherent paragraph. Provide only the new text. Paper
   with the topic of a thesis titled       . Maintain a formal academic tone          title:       , initial text:      .
   and provide only the continuation as a single, seamless paragraph. Initial
   sentence:        .                                                               • You are the lead author of a scientific paper summarizing your work. The
                                                                                      text below already outlines the problem and methodology. Your task is to
 • You are a final-year IT student analyzing your research findings for your          continue the abstract by presenting the key results and findings. Report
   graduation thesis. Continue the paragraph that begins with the key statement       on the primary outcomes, important performance metrics, or significant
   below by providing an analytical extension. Your writing should focus on           observations derived from your experiments. The results must be specific,
   comparing the statement to existing work, contrasting it with alternative          quantitative where possible, and logically follow from the described method.
   approaches, or discussing its broader implications within the context of           The output must integrate smoothly with the initial text to form a single,
   the thesis titled         . Ensure the analysis is coherent and maintains a        cohesive paragraph. Initial text:        .
   scholarly tone. Initial statement:       .



            Table 10: List of diverse prompt templates used to generate FAIDSet – Label: LLM-continued.


   Specifically:                                                                        We encoded each example using the penultimate
                                                                                     layer of our classification model, then applied clus-
    • Robust Domain Adaptation: New inputs are                                       tering within the vector database to assign soft
      matched against a broad, continuously grow-                                    or hard cluster labels corresponding to the three
      ing repository of embeddings, allowing the                                     classes. The results are shown in Table 13, where
      classifier to leverage analogous instances from                                we can see:
      related domains without full retraining.
                                                                                          • Traditional algorithms show reasonable per-
    • Generator-Independent Coverage: As                                                    formance on held-out known generators, but
      novel text generators emerge, their embed-                                            degrade notably on unseen generators.
      dings populate the database; retrieval naturally
      adapts to new styles or patterns by finding the                                     • Fuzzy C-Means leverages membership de-
      closest existing vectors.                                                             grees to handle overlapping distributions, im-
                                                                                            proving both measures by 4% over k-Means,
F.2 Clustering Algorithm Selection                                                          with smaller degradation on unseen data.
To improve our detector’s robustness against un-
                                                                                          • Fuzzy KNN combines local neighbor infor-
seen domains and generators, we evaluated four
                                                                                            mation with fuzzy membership, achieving the
clustering strategies in our vector database. Each
                                                                                            best overall performance.
algorithm was tasked with grouping text samples
into human-written, AI-generated, and human–                                           Given its superior ability to adapt to novel do-
LLM collaborative categories, using both known-                                      mains and generators through weighted neighbor
generator data (held out from training) and entirely                                 voting and soft cluster assignments, we adopt
unseen generator data. For evaluation, we used                                       Fuzzy k-Nearest Neighbors as the clustering com-
accuracy and F1-macro score.                                                         ponent in our overall architecture.
                                                                               3292
  Student Thesis                                                                       Paper Abstract


                                                                                    • You are a researcher with paraphrasing the following paragraph, which has
                                                                                      been extracted from the abstract of a science paper in the computer science
• You are an academic writing tutor. Your task is to perform a deep paraphrase        domain. Paraphrase the given abstract content while preserving its original
  of the following thesis excerpt. The goal is to create a version with significant   meaning and context. Maintain clarity, coherence, and an academic tone.
  structural and lexical differences from the original, while rigorously preserving   Do not paraphrase: References, figure labels, and citations should remain
  the precise meaning, nuance, and all technical information. Focus on altering       unchanged. The original text:
  sentence construction and rephrasing ideas in a completely fresh way. All
  specific technical terms, citations, and figure labels must remain unchanged. • Rephrase this abstract in formal academic English, maintaining all original
  The tone must remain formal and scholarly. The original text:             .         citations and technical accuracy. Do not paraphrase: References, figure labels,
                                                                                      and citations should remain unchanged. The original text:             .
• You are a Computer Science Student tasked with paraphrasing the following
  paragraph, which has been extracted from the thesis of an undergraduate • You are an expert scientific editor tasked with reframing an abstract to maxi-
  student. Paraphrase the given thesis content while preserving its original          mize its immediate impact. Perform a structural paraphrase on the following
  meaning and context. Maintain clarity, coherence, and an academic tone.             text. First, identify the core components of the abstract (Problem, Method,
  Do not paraphrase: References, figure labels, and citations should remain           Results, Contribution) internally. Then, rephrase and reorder these components
  unchanged. The original text:           .                                           to lead with the main Contribution or Result, followed by the problem it solves
                                                                                      and the method used. This inverted structure should create a fresh and com-
• Paraphrase the following thesis section in a clear academic tone, preserving        pelling narrative while preserving all original information. Strict requirements:
  citations and technical terms exactly. Do not paraphrase: References, figure        All technical terms, data, and citations must be preserved exactly. The original
  labels, and citations should remain unchanged. The original text:            .      text:         .

• You are a senior researcher mentoring a student on their thesis. Paraphrase the • Paraphrase this abstract paragraph to enhance clarity and flow, ensuring all
  following paragraph with the primary goal of improving clarity and directness.    technical terms and citations remain intact. Do not paraphrase: References, fig-
  Untangle convoluted sentences and rephrase the content using a more straight-     ure labels, and citations should remain unchanged. The original text:              .
  forward structure. The aim is to express the same technical information in a
  way that is easier for a reader to parse, without losing any nuance or academic • You are a senior scientist adapting a specialized abstract for a broader scientific
  rigor. Do not alter or rephrase technical terminology, citations, or references   audience. Your task is to paraphrase the following text to make it more
  to figures. The original text:         .                                          accessible to researchers in adjacent fields, without sacrificing technical rigor.
                                                                                    Rephrase the abstract by substituting hyper-specific jargon with more widely
• Reword this thesis excerpt to improve readability and maintain its scholarly      understood technical equivalents, but only if the precise meaning is retained.
  voice, keeping all references unchanged. Do not paraphrase: References, figure    The goal is for a researcher from a different subfield to quickly grasp the core
  labels, and citations should remain unchanged. The original text:          .      concepts. Strict requirements: The abstract’s original meaning, key findings,
                                                                                    and data must be perfectly preserved. All citations and figure references must
                                                                                    remain unchanged. The original text:



           Table 11: List of diverse prompt templates used to generate FAIDSet – Label: LLM-paraphrased.




                                                                              Known Generators                                    Unseen Generators
  Model                                            #. Params
                                                                   Acc ↑     F1-macro ↑ MSE ↓             MAE ↓        Acc ↑     F1-macro ↑ MSE ↓             MAE ↓
  RoBERTa-base                                        125M         80.09         76.22         0.7328      0.3778      73.45         69.10        0.8901      0.4320
  FLAN-T5-base                                        248M         80.19         75.77         0.7783      0.3947      72.80         68.55        0.9123      0.4467
  e5-base-v2                                          109M         81.53         77.90         0.8023      0.4086      74.21         70.15        0.8804      0.4392
  Multilingual-e5-base                                278M         91.41         90.82         0.3436      0.1732      85.32         84.50        0.5102      0.2543
  XLM-RoBERTa-base                                    279M         91.90         90.63         0.2345      0.1190      86.75         85.20        0.4125      0.2104
  Sup-SimCSE-RoBERTa-base                             279M         81.22         78.88         0.7102      0.3619      74.00         71.30        0.8420      0.4251
  UnSup-SimCSE-RoBERTa-base                           279M         82.19         79.38         0.7156      0.3637      75.10         72.40        0.8305      0.4207
  UnSup-SimCSE-XLM-RoBERTa-base                       279M         92.12         91.75         0.1904      0.0958      87.45         86.90        0.3507      0.1802

       Table 12: Model selection on known vs. unseen generators. The best results in each column are in bold.




                                                                      Known Generators                         Unseen Generators
                        Algorithm
                                                                   Accuracy ↑ F1-macro ↑                    Accuracy ↑ F1-macro ↑
                        k-Nearest Neighbors (KNN)                      90.52                90.21               85.37                84.95
                        k-Means                                        88.13                87.48               80.22                79.81
                        Fuzzy k-Nearest Neighbors                      95.18                95.05               93.31                93.25
                        Fuzzy C-Means                                  92.67                92.31               90.04                89.53

Table 13: Comparison of clustering algorithms on known vs. unseen generators. The best results are shown in bold.



                                                                                 3293
                                   (a) word length distribution across five LLMs




                                 (b) character length distribution across five LLMs

Figure 3: Text length distributions in words and characters across Llama-3.3, GPT-4o/4o-mini, Gemini 2.0, Gemini
2.0 Flash-Lite, and Gemini 1.5 Flash.




                                                       3294
                                            (a) 2D embedding space




                                            (b) 3D embedding space

Figure 4: Visualizations showing clustering behavior of Gemini model family (Gemini 2.0, Gemini 2.0 Flash-Lite,
Gemini 1.5 Flash) and GPT-4o/4o-mini using 2D and 3D embeddings with sample size of 2,000 texts.




                                                    3295
                                (a) Top 3-grams of Gemini 2.0 (500 samples).




                              (b) top 3-grams of Gemini 2.0 Flash (500 samples)




                               (c) top 3-grams of Gemini 1.5 Flash (500 samples)

Figure 5: Top 20 most common trigrams from Gemini 2.0, Gemini 2.0 Flash-Lite, Gemini 1.5 Flash using 500
sample prompts.



                                                    3296


## Preserved Responsible NLP Checklist text

```text
Responsible NLP Checklist
Paper title: FAID: Fine-grained AI-generated Text Detection using Multi-task Auxiliary and Multi-level
Contrastive Learning
Authors: Minh Ngoc Ta, Dong Cao Van, Duc-Anh Hoang, Minh Le-Anh, Truong Nguyen, My Anh Tran
Nguyen, Yuxia Wang, Preslav Nakov, Dinh Viet Sang
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
        8
✓ B. Did you use or create scientific artifacts? (e.g. code, datasets, models)
□
 ✓ B1. Did you cite the creators of artifacts you used?
 □
        8
  ✓ B2. Did you discuss the license or terms for use and/or distribution of any artifacts?
  □
        8
  ✓ B3. Did you discuss if your use of existing artifact(s) was consistent with their intended use, provided
  □
        that it was specified? For the artifacts you create, do you specify intended use and whether that is
        compatible with the original access conditions (in particular, derivatives of data accessed for research
        purposes should not be used outside of research contexts)?
        8

  □ B4. Did you discuss the steps taken to check whether the data that was collected/used contains any
  N/A


        information that names or uniquely identifies individual people or offensive content, and the steps
        taken to protect/anonymize it?
        (left blank)

  ✓ B5. Did you provide documentation of the artifacts, e.g., coverage of domains, languages, and
  □
        linguistic phenomena, demographic groups represented, etc.?
        3; 5.1; Appendix A

  ✓ B6. Did you report relevant statistics like the number of examples, details of train/test/dev splits, etc.
  □
        for the data that you used/created?
        5.1; Appendix B
The Responsible NLP Checklist used at ACL Rolling Review is adopted from NAACL 2022, with the addition of ACL 2023
question on AI writing assistance and further refinements based on ARR practice.
✓ C. Did you run computational experiments?
□
 ✓ C1. Did you report the number of parameters in the models used, the total computational budget
 □
       (e.g., GPU hours), and computing infrastructure used?
       Appendix E

 ✓ C2. Did you discuss the experimental setup, including hyperparameter search and best-found
 □
       hyperparameter values?
       Appendix C, Appendix E, Appendix F

 ✓ C3. Did you report descriptive statistics about your results (e.g., error bars around results, summary
 □
       statistics from sets of experiments), and is it transparent whether you are reporting the max, mean,
       etc. or just a single run?
       5
 ✓ C4. If you used existing packages (e.g., for preprocessing, for normalization, or for evaluation, such
 □
       as NLTK, SpaCy, ROUGE, etc.), did you report the implementation, model, and parameter settings
       used?
       3, 5, Appendix E, Appendix F

✓ D. Did you use human annotators (e.g., crowdworkers) or research with human subjects?
□
 ✓ D1. Did you report the full text of instructions given to participants, including e.g., screenshots,
 □
       disclaimers of any risks to participants or annotators, etc.?
       5.6, 5.7, Appendix C

 □ D2. Did you report information about how you recruited (e.g., crowdsourcing platform, students)
 N/A


       and paid participants, and discuss if such payment is adequate given the participants’ demographic
       (e.g., country of residence)?
       Authors annotated all, we did not recruit annotators externally.

 ✓ D3. Did you discuss whether and how consent was obtained from people whose data you’re
 □
       using/curating (e.g., did your instructions explain how the data would be used)?
       5

 □ D4. Was the data collection protocol approved (or determined exempt) by an ethics review board?
 N/A


       (left blank)

 ✓ D5. Did you report the basic demographic and geographic characteristics of the annotator population
 □
       that is the source of the data?
       5, Appendix C

✓ E. Did you use AI assistants (e.g., ChatGPT, Copilot) in your research, coding, or writing?
□
 ✗
 □ E1. If you used AI assistants, did you include information about their use?
       We used GitHub Copilot and Cursor solely for code optimization, which had no impact on our
       research findings and therefore was not mentioned.
```

## Extraction verification

- **Beginning checked:** Paper page 1 was rendered and compared with the title, author list, affiliations, abstract, Introduction opening, footnotes, and proceedings footer in the extraction.
- **Middle checked:** Paper page 11 was rendered and compared with the continuation of the references and page number 3285 in the extraction. Results tables, Sections 5.6-5.7, and the Limitations and Ethics sections on nearby pages were also checked directly in the extracted text.
- **End checked:** Paper page 22 was rendered and compared with Figure 5, its three Gemini trigram panels, caption, and final page number 3296. Both checklist pages were extracted and checked against the official checklist rendering.
- **Structure checked:** `pdfinfo` reports 22 A4 paper pages and 2 A4 checklist pages. The extraction includes Sections 1-6, Limitations, Ethics and Broader Impact, references, Appendices A-F, Tables 1-13, Figures 1-5, prompt tables, notes, and captions.
- **Known omissions:** None. Raster chart labels are preserved in the authoritative paper PDF; the text layer retains their captions but does not expose every plotted label reliably.

## Preserved attachments

| Path | Role in the source | SHA-256 | Preservation / extraction notes |
|---|---|---|---|
| `human-eyes/references/sources/snapshots/attachments/faid-eacl-2026.pdf` | Authoritative EACL 2026 paper | `aa260aa1faaaac6ba216eef9a34c64f9c4a726b7017bc7df257530b3524364e9` | Downloaded directly from ACL Anthology; all 22 pages extracted with `pdftotext -layout`; pages 1, 11, and 22 rendered for visual comparison. |
| `human-eyes/references/sources/snapshots/attachments/faid-eacl-2026-checklist.pdf` | Official Responsible NLP Checklist | `de26bb0352bb51cc9d433dbbab737abb6dfdf13d03f0fc4dba9076b14a46f7db` | Downloaded from the ACL attachments path; both pages extracted with `pdftotext -layout` and reproduced above. |
