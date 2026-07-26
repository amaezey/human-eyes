# Idiosyncrasies in Large Language Models

- **Canonical URL:** https://arxiv.org/abs/2502.12150v2
- **Alternate access URLs:**
  - https://arxiv.org/pdf/2502.12150v2
  - https://arxiv.org/html/2502.12150v2
  - https://proceedings.mlr.press/v267/sun25z.html
  - https://raw.githubusercontent.com/mlresearch/v267/main/assets/sun25z/sun25z.pdf
  - https://openreview.net/forum?id=FCZ3jVzmTZ
  - https://github.com/locuslab/llm-idiosyncrasies
  - https://github.com/locuslab/llm-idiosyncrasies/tree/e5333d01493963e5af44288fe2b9343ae6f13b9f
- **Author / owner:** Mingjie Sun, Yida Yin, Zhiqiu Xu, J. Zico Kolter, and Zhuang Liu
- **Publisher:** Proceedings of Machine Learning Research (PMLR), volume 267, Proceedings of the 42nd International Conference on Machine Learning
- **Published:** submitted to arXiv 2025-02-17; arXiv v2 revised 2025-06-16; ICML 2025 / PMLR 267:57854-57885
- **Retrieved:** 2026-07-17
- **Stable identifier:** arXiv:2502.12150v2; DOI 10.48550/arXiv.2502.12150; PMLR paper ID pmlr-v267-sun25z; OpenReview FCZ3jVzmTZ; linked implementation Git commit e5333d01493963e5af44288fe2b9343ae6f13b9f
- **Version / revision:** arXiv v2 dated 2025-06-16, compared with the 32-page PMLR version of record; linked implementation inspected at Git commit e5333d01493963e5af44288fe2b9343ae6f13b9f dated 2025-07-21
- **Extraction method:** official arXiv v2 and PMLR PDFs downloaded with curl; both inspected with pdfinfo and converted from embedded text layers with Poppler pdftotext -layout; arXiv pages 1, 16, and 32 rendered with pdftoppm and visually compared; arXiv HTML and PMLR metadata pages used for structure and bibliographic checks; linked GitHub repository cloned, all seven tracked files read, and the reviewed commit preserved with git archive
- **Full-text status:** complete
- **Access and transformation notes:** The complete 32-page arXiv v2 text, including tables, captions, appendices, response demonstrations, footnotes, impact statement, acknowledgments, and references, is preserved below, followed by every tracked file from the current linked implementation commit. Two-column order and visual encodings such as color and underlining are flattened by text extraction; both authoritative PDFs are preserved so those features remain reviewable. Trailing horizontal whitespace is removed from the readable code transcription; the Git archive preserves exact tracked bytes. The PMLR PDF predates arXiv v2 corrections to cross-references and figure numbering but contains the same substantive experiments. The code repository does not tag a paper-time release; its reviewed commit postdates arXiv v2 and is treated as current linked implementation evidence, not proof of the exact paper run.

## Full text

```text
                                                                        Idiosyncrasies in Large Language Models


                                                              Mingjie Sun * 1      Yida Yin * 2    Zhiqiu Xu 3         J. Zico Kolter 1    Zhuang Liu 4


                                                                   Abstract                                      ferent LLMs, either between the outputs of entirely different
                                              In this work, we unveil and study idiosyncrasies                   models or between those of different variants of the same
                                              in Large Language Models (LLMs) – unique pat-                      model family. If possible, the ability to distinguish between
                                              terns in their outputs that can be used to distin-                 source models in this manner would be valuable for a num-




arXiv:2502.12150v2 [cs.CL] 16 Jun 2025
                                              guish the models. To do so, we consider a simple                   ber of applications: it could shed light on the relative uptake
                                              classification task: given a particular text output,               of different LLMs, beyond what is reported by individual
                                              the objective is to predict the source LLM that                    companies, and on the nature of data used to build differ-
                                              generates the text. We evaluate this synthetic task                ent models. Additionally, it could offer insights into what
                                              across various groups of LLMs and find that sim-                   features of generated text are most “unique” to each LLM.
                                              ply fine-tuning text embedding models on LLM-                      In this paper, we investigate whether LLMs exhibit idiosyn-
                                              generated texts yields excellent classification ac-                crasies that enable their outputs to be reliably differentiated.
                                              curacy. Notably, we achieve 97.1% accuracy on                      Inspired by recent studies on dataset bias in computer vision
                                              held-out validation data in the five-way classifica-               (Liu & He, 2025; Zeng et al., 2024), which showed that
                                              tion problem involving ChatGPT, Claude, Grok,                      images from different large-scale datasets can be accurately
                                              Gemini, and DeepSeek. Our further investiga-                       distinguished by standard neural networks, we consider a
                                              tion reveals that these idiosyncrasies are rooted                  similar synthetic classification task to assess the separability
                                              in word-level distributions. These patterns persist                of responses generated between different LLMs. Specifi-
                                              even when the texts are rewritten, translated, or                  cally, we sample a large number of text outputs from each
                                              summarized by an external LLM, suggesting that                     LLM using the same set of prompts and then train a clas-
                                              they are also encoded in the semantic content. Ad-                 sifier to recognize which model generates a specific text.
                                              ditionally, we leverage LLM as judges to generate                  Figure 1 provides an overview of our framework. The il-
                                              detailed, open-ended descriptions of each model’s                  lustrated example on ChatGPT, Claude, Grok, Gemini, and
                                              idiosyncrasies. Finally, we discuss the broader                    DeepSeek presents a five-way classification problem.
                                              implications of our findings, including training
                                              on synthetic data, inferring model similarity, and                 We find that a classifier based upon simple fine-tuning text
                                              robust evaluation of LLMs. Code is available at                    embedding models on LLM outputs is able to achieve re-
                                              github.com/locuslab/llm-idiosyncrasies.                            markably high accuracy on this task. This indicates the
                                                                                                                 clear presence of idiosyncrasies in LLMs. The observation
                                                                                                                 is highly robust over a large variety of LLM combinations.
                                         1. Introduction                                                         For instance, trained on the combined set of texts from
                                                                                                                 ChatGPT, Claude, Grok, Gemini, and DeepSeek, a model
                                         As the adoption of generative models such as LLMs accel-                can achieve 97.1% classification accuracy on the held-out
                                         erates, it becomes increasingly important to understand the             validation data, compared to a 20.0% chance-level guess.
                                         origin and provenance of such generated content. While a                Within the same model family, we obtain a non-trivial 59.8%
                                         great deal of past work has focused on the classification of            accuracy across 4 model sizes in Qwen-2.5 series (Qwen
                                         human-written and AI-written content (Krishna et al., 2023;             et al., 2024). Further, we observe strong out-of-distribution
                                         Mitchell et al., 2023; Sadasivan et al., 2025), there has been          generalization of these classifiers when tested on responses
                                         little work on classifying between content generated by dif-            from prompts outside the training distribution.
                                           *
                                             Equal contribution 1 Carnegie Mellon University 2 UC Berkeley       We observe several interesting properties of this task. When
                                         3
                                          University of Pennsylvania 4 Princeton University. Correspon-          controlling the length and format of outputs through prompt
                                         dence to: Mingjie Sun <mingjies@andrew.cmu.edu>, Yida Yin               instructions, we still obtain high classification accuracy. Fur-
                                         <davidyinyida0609@berkeley.edu>.
                                                                                                                 thermore, for post-trained LLMs, the classifier demonstrates
                                         Proceedings of the 42 nd International Conference on Machine            non-trivial accuracy even with only the first few tokens of
                                         Learning, Vancouver, Canada. PMLR 267, 2025. Copyright 2025             the generated text. However, when classifying generations
                                         by the author(s).

                                                                                                             1
                                                       Idiosyncrasies in Large Language Models

  Prompt: Now everyone in a room is silent and working on their own thing, and you need to break the silence with a three-sentence joke. What would you say?



        ChatGPT                            Claude                             Grok                             Gemini                         DeepSeek

 Why don't scientists trust       Hey everyone, want to hear       Hey, did you know I just got a    A snail went to buy a car. The     Why did the scarecrow win
 atoms? Because they make         what happened when the two       new job at the calendar           salesman told him, "We have        an award?
 up everything! And speaking      satellites started dating?       factory? The hours are great,     a great deal on this one, but it   Because he was outstanding
 of making things up, I told my   They had a great first date,     but the days are really hard      doesn't come with a shell."        in his field!
 computer I needed a break,       but things fell apart after      to get off. And the worst part?   The snail looked surprised         ...Or maybe he just knows
 and it said, "No problem, I'll   that... Turns out they had too   Every time I try to take a        and asked, "Well, how am I         how to keep people silent
 go on a byte-sized vacation!"    much space between them!         break, I get a month behind!      supposed to drive it?"             with his straw-ng presence.



                                                               Neural Network Classifier

                                                  ChatGPT, Claude, Grok, Gemini, or DeepSeek?
Figure 1. Our framework for studying idiosyncrasies in Large Language Models (LLMs). We show that each LLM is unique in
its expression. In the example shown here on ChatGPT, Claude, Grok, Gemini, and DeepSeek, a neural network classifier is able to
distinguish them with a near-perfect 97.1% accuracy.

from the same LLM but using different sampling strategies,                           manipulate voting-based leaderboards, therefore highlight-
we achieve accuracy only slightly above the chance level.                            ing the need for more robust evaluation methodologies.
In addition, we observe certain behaviors of this task that
resemble those of standard text classification, where im-                            2. Evaluating Idiosyncrasies in LLMs
provements in text embeddings and availability of larger
training datasets lead to better classification performance.                         Large Language Models (LLMs) share several core charac-
                                                                                     teristics. The majority of them are based on the Transformer
We analyze the sources of these idiosyncrasies by applying
                                                                                     architecture (Vaswani et al., 2017), which is shared by all
text transformations that isolate different levels of infor-
                                                                                     models we consider in this paper. Second, they are trained
mation. We find that randomly shuffling words in LLM-
                                                                                     using an auto-regressive objective (Radford et al., 2019),
generated responses leads to only a slight decrease in classi-
                                                                                     where they predict the next token in a sequence based on pre-
fication accuracy. This suggests that a substantial portion of
                                                                                     ceding context. Lastly, their training datasets significantly
distinctive features is encoded in the word-level distribution.
                                                                                     overlap, often incorporating vast and diverse sources such
We then highlight distinct sets of characteristic phrases that
                                                                                     as Common Crawl, Wikipedia, and Stack Overflow. Given
are consistently associated with each LLM. We also observe
                                                                                     these similarities, it is natural to ask: do LLMs speak in
that markdown formatting contributes to a moderate degree
                                                                                     the same way? If not, how can we effectively measure the
of idiosyncrasies in the LLMs following post-training.
                                                                                     degree of their differences?
At the same time, we obtain over 90% accuracy when the
                                                                                     To address these questions, we construct a synthetic task
word distribution is disrupted through transformations that
                                                                                     focused on classifying outputs from different LLMs. Con-
preserve semantics, such as rephrasing or translating. Even
                                                                                     sider N LLMs, denoted as f1 , . . . , fN , where each fi takes
with the most aggressive transformation – summarizing,
                                                                                     an input prompt p and outputs a text completion o. For a
classification accuracy remains well above chance-level
                                                                                     given dataset D of prompts, the outputs produced by each
guess. This finding implies that semantic information also
                                                                                     LLM fi are denoted as Oi . We approach this problem with
shapes the idiosyncrasies in LLMs. Through open-ended
                                                                                     a straightforward setup. For N output sets Oi , we formulate
language analysis, we provide further insights into these
                                                                                     a N -way classification task, where the objective is to predict
characteristics. For instance, ChatGPT has a preference for
                                                                                     which LLM produced each output. If outputs of different
detailed, in-depth explanations, whereas Claude produces
                                                                                     LLMs were drawn from the same distribution, classification
more concise and direct responses, prioritizing clarity.
                                                                                     accuracy would not be better than random chance. Thus, we
Last, we discuss the broader implications of our findings.                           use the classification performance of this synthetic task as a
One should be cautious when using synthetic data to train                            measure of idiosyncrasies in LLMs.
LLMs, as we show that many of these idiosyncrasies can be
                                                                                     Our task is formulated as a sequence classification problem,
inherited in such a process. Our framework also serves as a
                                                                                     for which fine-tuning BERT-style models is a common ap-
tool for assessing model similarities among frontier models,
                                                                                     proach (Sun et al., 2019). In this work, we fine-tune a more
either open-source or proprietary. In addition, we discuss
                                                                                     recent and competitive sequence embedding model based
how the idiosyncrasies in LLMs can be used maliciously to

                                                                                 2
                                            Idiosyncrasies in Large Language Models

                     ChatGPT         Claude           Grok          Gemini         DeepSeek        acc. (chat)
                        ✓              ✓                                                              99.3
                        ✓                              ✓                                              97.7
                        ✓                                              ✓                              98.7
                        ✓                                                              ✓              97.2
                                        ✓              ✓                                              99.7
                                        ✓                              ✓                              99.6
                                        ✓                                              ✓              99.6
                                                       ✓               ✓                              99.4
                                                       ✓                               ✓              98.7
                                                                       ✓               ✓              99.9
                        ✓               ✓              ✓               ✓               ✓              97.1
                                                           (a) chat APIs

                      Llama          Gemma           Qwen           Mistral      acc. (instruct)   acc. (base)
                        ✓              ✓                                              99.9            98.3
                        ✓                              ✓                              97.8            81.7
                        ✓                                              ✓              97.0            96.3
                                        ✓              ✓                              99.9            98.3
                                        ✓                              ✓              99.9            98.4
                                                       ✓               ✓              96.1            95.7
                        ✓               ✓              ✓               ✓              96.3            87.3
                                                    (b) instruct and base LLMs
Table 1. Classification accuracies for various LLM combinations. Top: results for chat APIs. Bottom: results for instruct and base
LLMs. Check marks (✓) denote the models included in each combination. We observe high classification accuracies consistently across
all model combinations, indicating the presence of distinct idiosyncrasies in LLMs.


on decoder-only Transformers: LLM2vec (BehnamGhader                 2. Instruct LLMs (“instruct”): These models are trained
et al., 2024). We attach a N -way classification head to the           to generate high-quality responses from human instruc-
extracted embeddings and use LoRA-based fine-tuning (Hu                tions. We consider four LLMs of similar sizes across
et al., 2022) to the model weights. Input sequences are trun-          different families: Llama3.1-8b (Dubey et al., 2024),
cated to a maximum length of 512 tokens. We report the                 Gemma2-9b (Riviere et al., 2024), Qwen2.5-7b (Qwen
classification accuracy on a held-out validation set. Addi-            et al., 2024) and Mistral-v3-7b (Jiang et al., 2023). We
tional training details are provided in Appendix A.2.                  will refer to them as Llama, Gemma, Qwen and Mistral.
                                                                    3. Base LLMs (“base”): These are base versions of instruct
2.1. Main Observations                                                 LLMs. They are obtained by pretraining on extensive
                                                                       text corpora without any post-training stage.
We observe surprisingly high accuracies by neural networks
to classify LLM outputs. This observation is robust across          Throughout the paper, we refer to these three categories
different settings, e.g., across model families and sizes.          as “chat”, “instruct”, and “base” respectively. For a given
                                                                    prompt dataset, we collect 11K text sequences, splitting
We describe the LLMs we use to generate the output datasets         them into 10K and 1K as training and validation sets, re-
O1,··· ,N . For a comprehensive and fair comparison across          spectively. The same split is used across all LLMs. For
model families, we categorize three groups of LLMs:                 chat APIs and instruct LLMs, we generate outputs from
1. Chat APIs (“chat”): This category includes state-of-             UltraChat (Ding et al., 2023), a diverse dialogue and in-
   the-art LLMs that are primarily accessible via APIs.             struction dataset. For base LLMs, we synthesize new texts
   We consider GPT-4o (OpenAI, 2024), Claude-3.5-                   using prompts from FineWeb (Penedo et al., 2024), a high-
   Sonnet (Anthropic, 2024), Grok-2 (xAI, 2024), Gemini-            quality LLM pretraining dataset. More details on response
   1.5-Pro (Google, 2024), and DeepSeek-V3 (DeepSeek-               generation are in Appendix A.1.
   AI, 2024). For simplicity, we refer to them as ChatGPT,
                                                                    Across model families. In Table 1, we report the results for
   Claude, Grok, Gemini and DeepSeek. Their architec-
                                                                    classifying outputs from various combinations of chat APIs
   tures and weights remain proprietary and undisclosed,
                                                                    (Table 1a) and instruct / base LLMs (Table 1b). In each
   with the exception of DeepSeek.                                                                                 2
                                                                    of the three LLM groups, we enumerate all (CN    ) possible


                                                                3
                                           Idiosyncrasies in Large Language Models

pairwise combinations when choosing 2 out of N models in              the results on instruct LLMs. Our classifiers generalize
the top panel of each table, as well as the case including N          well across different datasets, indicating that they learn very
models in the bottom row. For the binary classification task,         robust and transferable patterns.
the neural network consistently achieves over 90% accuracy,
with only one exception. Notably, for chat APIs and instruct            train / test UltraChat Cosmopedia LmsysChat WildChat
LLMs, many combinations reach as high as 99% accuracy.                  UltraChat      96.3       98.9      89.9      92.4
In the more challenging N -way classification tasks, our                Cosmopedia     95.7       99.8      88.3      94.9
classifiers maintain strong performance, achieving at least             LmsysChat      94.7       97.2      91.8      92.0
87.3% accuracy across three groups. These results highlight             WildChat       95.1       99.1      90.2      95.7
the idiosyncrasies across different LLMs. We refer readers            Table 3. Robust generalization to out-of-distribution responses.
to Appendix B.1 for the confusion matrices of our classifiers.        We train classifiers on LLM outputs from one prompt dataset and
Within the same model family. We evaluate sequence                    tested on those from another.
classification performance when distinguishing responses
from LLMs within the same model family. Note that models              2.2. Controlled Experiments
from the same family typically share common training pro-
cedures, e.g., pretraining datasets and optimization schedule.        We analyze the behaviors of the synthetic classification task
First, we analyze the impact of model size by consider-               in several controlled settings. From now on, we only report
ing four Qwen2.5 instruct LLMs with 7B, 14B, 32B, and                 accuracies of the N -way classification task in each group.
72B parameters. As shown in Table 2, the classification               Prompt-level interventions. We assess the degree of id-
task is more difficult here, but our classifiers remain well          iosyncrasies in LLM outputs with explicit prompt-level in-
above chance accuracy when distinguishing LLMs within                 terventions. Specifically, we modify the original prompt by
the same family. In the binary classification setup, the high-        incorporating additional instructions to constrain response
est accuracy reaches 85.5%, whereas in the full combination           length and format. We then perform sequence classification
setup, the accuracy becomes 59.8%. In addition, we observe            on the resulting outputs. Our interventions are:
high accuracies when classifying responses from base and
instruct versions of the same model. For example, our clas-            • Length control: Please provide a concise response in a
sifiers achieve 96.8% accuracy when distinguishing outputs               single paragraph, limited to a maximum of 100 words.
from Qwen2.5-7b base and instruct models.                              • Format control: Please provide your response in plain
                                                                         text only, avoiding the use of italicized or bold text, lists,
              7b    14b   32b    72b    instruct                         markdown, or HTML formatting.
              ✓      ✓                    77.0
                                                                      LLM outputs after these interventions are presented in Ap-
              ✓            ✓              81.2
                                                                      pendix C. We find that LLMs can follow the additional
              ✓                   ✓       83.4
                                                                      instructions in generating responses.
                    ✓      ✓              63.1
                    ✓             ✓       85.5
                                                                                        original length control format control
                           ✓      ✓       84.8
                                                                           instruct LLMs 96.3         93.0          91.4
              ✓     ✓      ✓      ✓       59.8

Table 2. Classification within Qwen2.5 model family. The clas-        Table 4. Controlling LLM outputs with prompts. An instruction
sifier can differentiate responses between LLMs within the same       is added to the original prompt to specify the output length and
model family with reasonably well accuracies.                         format. Length control limits responses to one paragraph. Format
                                                                      control ensures that responses are in plain text without any format.
Generalization to out-of-distribution responses. We find
                                                                      The results are shown in Table 4, where “original” means
that our classifiers generalize robustly to responses beyond
                                                                      the classification accuracy without interventions. We can
their training distribution. To evaluate this, we collect re-
                                                                      see that neural networks still perform excellently for classi-
sponses from instruct LLMs across four diverse datasets:
                                                                      fying LLM outputs applied with length and format control
i.e., UltraChat, Cosmopedia (Ben Allal et al., 2024), Lm-
                                                                      prompts. These findings suggest that LLM characteristics
sysChat (Zheng et al., 2024), and WildChat (Zhao et al.,
                                                                      are deeply embedded in the generated text, persisting despite
2024). These datasets originate from different sources and
                                                                      surface-level constraints on length and formatting.
are designed for various purposes – Cosmopedia is intended
for synthetic data generation, LmsysChat and WildChat cap-            Input length of text embedding models. We control
ture real-world user interactions, while UltraChat consists           the number of input tokens to the text embedding models.
primarily of synthetic responses. For each dataset, we train          Specifically, we truncate each response to a fixed number of
a classifier on a group of model responses and evaluate the           tokens in a left-to-right fashion. Figure 2 presents the results.
classifier on the remaining three datasets. Table 3 shows             Across three groups of LLMs, the classification task benefits

                                                                  4
                                                   Idiosyncrasies in Large Language Models

           100                                                                  methods: ELMo (Peters et al., 2018), BERT (Devlin et al.,



accuracy (%)
               75                                                               2018), T5 (Raffel et al., 2020), GPT-2 (Radford et al., 2019),
                                                                                and LLM2vec (BehnamGhader et al., 2024). Details on the
               50                                           chat                fine-tuning setting can be found in Appendix A.2.
               25                                           instruct
                                                            base               Table 6 shows the results. All sequence embedding models
                0 1   2    4    8    16    32    64 128 256 512
                                                                               can achieve very high accuracies. The classification perfor-
                      input sequence length for the classifier                 mance improves with more advanced sequence embedding
                                                                               models. Among all methods, LLM2vec demonstrates the
  Figure 2. Ablations on input length of text embedding models.                best performance, achieving 97.1% on chat APIs, 96.3% on
  Classification accuracies improve as the text embedding models               instruct LLMs, and 87.3% on base LLMs.
  capture more context. Performance begins to saturate beyond an
  input sequence length of 256. Note that the three lines represent                                method     chat   instruct     base
  different groups of LLMs and are not directly comparable.                                        ELMo       90.8     91.0       69.8
                                                                                                   BERT       91.1     91.5       66.0
                                                                                                   T5         90.5     89.8       67.9
   from seeing an increased number of tokens. Intriguingly,                                        GPT-2      92.1     92.3       80.2
   for chat APIs and instruct LLMs, we observe around 50%                                          LLM2vec    97.1     96.3       87.3
   accuracy using only a single text token. This suggests that
   the initial token in a response contains certain distinctive                Table 6. Different sequence embedding models. LLM2vec
   signals for the classification problem. In Section 3.1, we                  achieves the best performance in classifying outputs from vari-
   provide further evidence supporting this observation.                       ous LLMs among the five embedding models we study.

  Sampling methods. We consider outputs when sampled                           Training data size. We vary the number of training samples
  using different decoding strategies. Specifically, we use four               generated by LLMs and train the classifier with the same
  widely used sampling methods: greedy decoding, tempera-                      total number of iterations. We present the results in Figure 3.
  ture softmax, top-k, and top-p sampling. For each method,                    The classification performance increases with more training
  we generate a set of responses from the same LLM. We                         samples. This trend holds consistently across chat APIs,
  then fine-tune the LLM2vec embedding model to predict                        instruct LLMs, and base LLMs. Furthermore, as few as 10
  the sampling method responsible for each response.                           samples, the classifier achieves non-trivial accuracy (e.g.,
                    greedy softmax top-k top-p                                 40.3% on chat APIs), surpassing 20% chance-level guess.
         greedy        -          -         -         -                                100
         softmax     59.6         -         -         -


                                                                            accuracy (%)
         top-k       58.2       50.0        -         -                                    75
         top-p       52.9       51.0      52.1        -                                    50                                            chat
  Table 5. Classifications with different sampling methods. Dis-                           25                                            instruct
  tinguishing responses generated by the same model using different                                                                      base
  sampling strategies is only marginally better than chance accuracy.                       0 10             100                1K            10K
  The results are on Llama3.1-8b instruct model’s responses.                                                 # training samples
                                                                               Figure 3. Different numbers of training samples. Our sequence
  Table 5 presents the results for all pairs of sampling methods.              classifiers benefit from more training samples. The classification
  Notably, the accuracy of distinguishing between responses                    performance converges when using about 10K training samples.
  generated by the same LLM remains relatively low, with the
  highest accuracy across all configurations being 59%. Fur-
  thermore, in a more fine-grained 5-way classification task                    3. Concrete Idiosyncrasies in LLMs
  distinguishing softmax sampling at five different tempera-
                                                                               We have shown that modern neural networks can achieve
  tures (T = 0, 0.25, 0.5, 0.75, 1), we obtain an accuracy of
                                                                               excellent accuracies in classifying which LLM generates a
  37.9%, only marginally better than the random chance level
                                                                               given response. Here we use text similarity metrics to quan-
  of 20%. These results suggest that outputs from the same
                                                                               tify differences between LLM outputs. We consider three
  LLM are not easily separable based on decoding strategies.
                                                                               standard metrics – ROUGE-1 (Lin, 2004), ROUGE-L (Lin,
  Text embedding models. We vary the underlying pretrained                     2004), and BERTScore (Devlin et al., 2018) – to measure
  embedding models for sequence classification. The default                    lexical and semantic similarity. We compute the mean F1-
  setting we used in previous parts is fine-tuning the LLM2vec                 score for each metric across all response pairs generated by
  embedding models. We consider various generations of em-                     any two different chat API models given the same prompt.
  beddings models spanning across architectures and training                   For comparison, we also measure the similarity between

                                                                        5
                                                    Idiosyncrasies in Large Language Models

Our products feature innovative         According to the text, Kai Fusser           1. Deliver Exceptional Service: The      1. Deliver Exceptional Service
sustainable materials, such as …        believes that traditional cardio …             foundation of word-of-mouth            • Consistently exceed customer
Certainly! If you're looking for cheese Based on the text provided, here are           marketing is consistent excellence.    • expectations
alternatives to replace Brie in your … the key details about Armon Binns’ …            Providing top-notch services or …      • Focus on quality and attention …
Overall, while there are challenges,    While many winter sports in the             Ingredients:                             Ingredients:
Tanzania is making progress …           Pyrenees are similar to those found …          • 2 (3 oz) packages of orange-           • 2 boxes orange-flavored Jello
Sure! Here's a simple guide to cooking This appears to be a fragment of                  flavored Jello                         • 1 can evaporated milk
a juicy salmon fillet: …                poetry that creates a pastoral …               • 1 cup tonic water (this is what …      • Tonic water …
             ChatGPT                                  Claude                                       ChatGPT                                      Claude
                       (a) characteristic phrases                                                      (b) unique markdown formatting
Figure 4. Example responses from ChatGPT and Claude, showcasing their idiosyncrasies: characteristic phrases (left) and unique
markdown formatting (right). For clarity, we highlight each characteristic phrase with underline and model-specific color.

                            across LLMs          within an LLM
        ROUGE-1                 0.499                 0.660                          responses, i.e., 95.1% for chat APIs, 93.8% for instruct
        ROUGE-L                 0.256                 0.414                          LLMs, and 75.4% for base LLMs. Likewise, using word-
        BERTScore∗              0.220                 0.482                          shuffled responses yields high accuracies comparable to the
                                                                                     original ones. Further, we plot the frequencies of several
Table 7. Text similarity scores. We evaluate the text similarity
of LLM outputs using ROUGE-1, ROUGE-L, and BERTScore.                                commonly used words from five chat APIs in Figure 5 (left).
Responses from different LLMs exhibit low lexical similarity.                        We observe distinct patterns among models, even for fre-
                                                                                     quent English words: Claude has much lower frequencies
                                                                                     for words like “the”, “and”, “to”, and “of” than other chat
responses sampled within the same model. As shown in                                 APIs. These results suggest that special characters and
Table 7, responses from different LLMs exhibit lower text                            word order are not essential for distinguishing LLMs; word
similarities than those from the same model.                                         choices reflect substantial idiosyncrasies across models.
In the following, we identify concrete idiosyncrasies in                                                           ChatGPT
                                                                                     0.06                          Claude
LLMs across three dimensions: words and letters, mark-                                                             Grok     0.15
down formatting elements, and semantic meaning. For each                             0.04                          Gemini
                                                                                     0.02                          DeepSeek 0.10
dimension, we apply text transformations to isolate potential                                                               0.05
idiosyncrasies and assess their impacts on classification per-                                   atnhde
                                                                                                 f  t
                                                                                                   oo
                                                                                                   inf
                                                                                              witohr                               ab cd e f g h i
                                                                                                                                                     j k lmno p q
                                                                                                 or
                                                                                             thoan
                                                                                                ist
formance. We then highlight specific patterns within each                                     asit
                                                                                         yothuis                                                                    r s t u vwx y
                                                                                                                                                                                    z
                                                                                         canr
                                                                                          her
                                                                                        y by
                                                                                       theouir
dimension that distinguish LLMs.
                                                                                     Figure 5. Frequencies of words and letters. The top 20 most
3.1. Words and Letters                                                               frequently used words of LLMs (left) exhibit distinct patterns for
                                                                                     each model, but their letter frequencies (right) are very similar.
Text shuffling. To decouple the effects of words and let-                            Results are on the chat API models.
ters from other factors, we remove special characters in
                                                                                     In contrast, shuffling at the letter level results in a substantial
LLM-generated responses, such as punctuations, markdown
                                                                                     drop in accuracy (49%-56%), approaching chance-level per-
elements, and excessive white spaces. This ensures that
                                                                                     formance. This indicates that letter-level statistics alone are
each response consists solely of words separated by a white
                                                                                     not sufficient for predicting LLM identities. To qualitatively
space. Additionally, we apply two shuffling strategies to
                                                                                     visualize distinctions in letter distributions across models,
the preprocessed text: word-level and letter-level shuffling.
                                                                                     Figure 5 (right) shows the frequency distribution of letters
These transformations disrupt the natural order and force the
                                                                                     in responses generated by chat APIs. Different LLMs share
classifier to learn patterns from raw text statistics. Table 8
                                                                                     almost identical letter distributions, indicating that letters
presents the classification results.
                                                                                     contribute minimally to idiosyncrasies in LLMs.
Classifiers trained on responses without special charac-
                                                                                     Characteristic phrases. We use Term Frequency-Inverse
ters achieve accuracies close to those using the original
                                                                                     Document Frequency (TF-IDF) to highlight characteristic
                                          chat     instruct     base                 phrases inside LLM-generated responses that reflect each
     original                             97.1       96.3       87.3
                                                                                     model’s word choices. Formally, we treat each LLM re-
     removing special characters          95.1       93.8       75.4                 sponse as a document and then extract TF-IDF features on
     shuffling words                      88.9       88.9       68.3                 all uni-gram and bi-gram words. We then train a N -way lo-
     shuffling letters                    39.1       38.6       38.9                 gistic regression model to predict the origin of responses on
                                                                                     the extracted features. This simple linear classifier achieves
Table 8. Classifications with only words and letters. While re-                      85.5% / 83.7% accuracy on chat APIs / instruct LLMs, close
moving special characters and shuffling words have little impact                     to 95.1% / 93.8% achieved with fine-tuning embedding mod-
on accuracies, shuffling letters greatly reduces the performance.                    els on responses without special characters (Table 8).

                                                                                6
                                                 Idiosyncrasies in Large Language Models

                     such                    here                                               ChatGPT                   Claude
                   such as             according to                                                the                                  here
                   enhance               according                                          title                          based
                   involves                the text                                         certainly                      the
                   certainly                while                                           creating                  according
                    overall               based on                                        to                     title
                      sure           here’s a summary                                     in                    yes
                     utilize             appears to                                     here                    how
                                                                                        sure                    this
                    various                  both                                       yes                     from
                   typically                when                                        as                     in
                   GPT-4o                  Claude                                           0.12 0.24 0.36            0.12 0.24 0.36
         which                 crucial                  below is                     Grok                    Gemini                   DeepSeek
        where                   other                in summary                       here                              the                    the
          not                   even                 for example                      the              this                            certainly
         here           here’s a breakdown               below                  certainly              python                     title
        here is          key improvements              certainly               in                      elara                    creating
      remember                doesn’t                  summary                title                   yes                       to
         might                 within                     may                to                       here                      here
       but also              essentially           certainly! below        creating                   while                    comprehensive
        not only                also                    know if            yes                        rain                     step
       helps in                  etc                   example             introduction               creating                 yes
                                                                           step                       my                       based
         Grok                 Gemini                  DeepSeek
                                                                                 0.12 0.24 0.36           0.12 0.24 0.36            0.12 0.24 0.36
Figure 6. Characteristic phrases. We train a logistic regression          Figure 7. First word. We analyze the distribution of the first word
model on TF-IDF features of chat APIs’ outputs and extract the            in chat APIs’ responses, with the top 10 most frequent words for
top 10 phrases for each LLM based on the coefficients of these            each model. These differences in the first-word usage explain the
features. We remove common words shared across these LLMs.                non-trivial accuracy with only the first word in Figure 2.


Since the coefficients of a logistic regression model provide             (6) code block. We transform the LLM outputs by retaining
a natural ranking for its features, we leverage these coef-               only these formatting components while replacing other text
ficients to highlight important phrases in the classification             with the marker “xxx”. Appendix C provides examples of
task. Figure 6 presents the top 10 phrases with the largest               the transformed outputs. Table 9 shows the classification
logistic regression coefficients for each of the five chat API            results after this transformation.
models (excluding the 20 most frequently used words in Fig-
                                                                          Surprisingly, we observe our classifiers achieve high accura-
ure 6). Notably, these phrases often serve as transitions or
                                                                          cies of 73.1% for chat APIs and 77.7% for instruct LLMs.
emphasis in sentences. For example, ChatGPT likes to gen-
                                                                          However, the classification accuracies with base LLMs’ re-
erate “such as”, “certainly”, and “overall”, whereas Claude
                                                                          sponses are near chance-level guess (25%). This is likely
prefers “here”, “according to”, and “based on”.
                                                                          because base LLMs tend to generate responses in plain text.
Figure 4a illustrates these characteristic phrases with exam-
ple responses from ChatGPT and Claude. While ChatGPT                                                   ChatGPT
                                                                          1.00                         Claude
begins responses with “certainly” and “below is”, Claude                                               Grok     1.00
                                                                          0.75                         Gemini   0.75
usually references the original prompt using the phrases like             0.50                         DeepSeek 0.50
                                                                          0.25                                  0.25
“according to the text” and “based on the text”. Moreover,
Figure 7 reveals noticeable differences in the distribution of               0                                      0
                                                                                      10                                   6
                                                                                    bold text co 20                      header coun12
first word choices among chat APIs. Appendix B.3 provides                                       unt         30                       t       18
characteristic phrases for other LLMs.                                    1.00                                   1.00
                                                                          0.75                                   0.75
                                                                          0.50                                   0.50
3.2. Markdown Formatting                                                  0.25                                   0.25
                                                                             0                                      0
We seek to understand how each LLM formats their re-                              enum10eration 20                         10
                                                                                                                        bullet point 20
                                                                                               count        30                      count    30
sponses, particularly in markdown. To this end, we focus on
common markdown elements used by LLMs: (1) bold text,
                                                                          Figure 8. Markdown formatting elements. Each LLM has a
(2) italic text, (3) header, (4) enumeration, (5) bullet point,           distinctive distribution of markdown formatting elements.

                                     chat     instruct    base            We count the occurrence of a markdown formatting element
      original                       97.1       96.3      87.3            in each response and then plot the distribution of these
      markdown elements only         73.1       77.7      38.5            counts over all responses in Figure 8. Each model exhibits
Table 9. Classifications with only markdown elements. Using               a unique way to format its responses. For instance, Claude
markdown elements can achieve high accuracies for chat APIs and           (yellow) has a high density at zero in the bold text and
instruct LLMs, but marginally better results for base LLMs.               header count distributions, indicating that it generates many

                                                                      7
                                                    Idiosyncrasies in Large Language Models

 1. Descriptive and Detailed Tone: Often uses narrative styles with an        1. Concise and Straightforward Tone: Generally adopts a more direct,
 informative, engaging, or vivid tone.                                        factual, or succinct tone.
 2. Specific and Technical Word: Employs descriptive and technical            2. Functional and Clear Word Choices: Prefers simple or action-oriented
 vocabulary, enhancing depth and specificity.                                 language prioritizing clarity and practicality.
 3. Structured and Contextual Opening Lines: Typically begins with            3. Immediate and Direct Opening Lines: Often starts with a
 context-setting or narrative introductions.                                  straightforward statement or summary without extended context.
 4. Markdown Formatting for Organization: Utilizes various markdown           4. Minimal Markdown or List Use: Relies on plain lists or simple
 elements like headings, lists, and bold text for clarity.                    formatting for quick reference.
 5. Comprehensive and In-Depth Content: Offers rich detail, focusing on       5. Focused and Summarized Content: Concentrates on essential points
 explanations, background, and broader topics.                                and specific phenomena, avoiding extensive detail.
                                ChatGPT                                                                       Claude

Figure 9. Results of our open-ended language analysis on ChatGPT and Claude. ChatGPT features descriptive language, sophisticated
markdown formatting, and in-depth details, while Claude highlights straightforward tone, minimal structure, and summarized content.


responses without bold texts or headers. On the contrary,                      Moreover, despite a noticeable accuracy drop (i.e., >38%)
other LLMs exhibit lower values at zero and thus decorate                      with the summarized text, the resulting performance remains
text with these formatting elements more often.                                well above chance-level guess. This remarkable ability to
                                                                               classify the summarized texts shows the high-level semantic
Figure 4b visualizes how ChatGPT and Claude structure
                                                                               difference in LLM-generated responses.
their responses in markdown. Interestingly, ChatGPT tends
to emphasize each key point within enumerations in bold                        Open-ended language analysis. In this part, we focus
and highlight a title with markdown headers, but Claude for-                   on studying the semantic difference in responses generated
mats text with simple enumeration and bullet points. More                      by LLMs. We employ another LLM (e.g., ChatGPT) as a
analysis for other models can be found in Appendix B.4.                        judge to provide open-ended, descriptive characterizations
                                                                               for each LLM’s outputs. The results with other LLM judges
3.3. Semantics                                                                 for our language analysis are available in Appendix B.6.
Rewriting. One potential reason for the high classification                    Specifically, we present an LLM judge with two responses –
accuracy is the unique writing style (e.g., word choice, sen-                  generated by different models based on the same prompt –
tence structure) of each LLM. To isolate this factor, we lever-                and ask it to analyze these responses from different angles
age another LLM (e.g., GPT-4o mini) to rewrite LLM re-                         (e.g., tone and content). This process is repeated multiple
sponses. Our rewriting approaches include (see Appendix C                      times to gather a comprehensive collection of analyses. Fi-
for example responses after rewriting):                                        nally, we query the LLM judge to summarize these analyses
                                                                               into bullet points that capture the characteristics of each
 • Paraphrasing: Paraphrase the above text while maintain-                     model. The prompts are detailed in Appendix A.3.
   ing the semantic meaning of the original text.
 • Translating: Translate the above text into Chinese.                         The results of open-ended language analysis on ChatGPT
 • Summarizing: Summarize the above text in one para-                          vs. Claude are shown in Figure 9. For a detailed pairwise
   graph.                                                                      comparison of the responses, see Figure 17 in Appendix C.
                                                                               ChatGPT is characterized by descriptive and detailed re-
                                chat     instruct    base                      sponses in an engaging tone. In contrast, Claude prioritizes
             original           97.8       96.3      87.3                      simplicity with only key points and straightforward lan-
             paraphrasing       91.4       92.2      71.7                      guage. Additional results on chat API models and instruct
             translating        91.8       92.7      74.0
                                                                               LLMs are provided in Appendix B.6.
             summarizing        58.1       57.5      44.7
Table 10. Classifications on rewritten responses. Paraphrasing
or translating LLM outputs achieves an accuracy comparable to
                                                                               4. Implications
that using original counterparts. However, summarizing these texts             In this section, we explore the broader implications of our
makes the model less capable of predicting LLM identities.                     framework, regarding synthetic data and model similarity.
We show the results in Table 10 (see Appendix B.5 for                          Idiosyncrasies via synthetic data. Using synthetic data
results using alternative LLM for rewriting). The classifiers                  has become a common practice when training frontier
trained on paraphrased LLM responses maintain similar                          LLMs (Abdin et al., 2024a;b; Liu et al., 2024). We conduct
accuracy levels to those using original responses. Likewise,                   supervised fine-tuning (SFT) on two base LLMs (Llama3.1-
when using translated text, the classifiers are also able to                   8b and Gemma2-9b) using Ultrachat, i.e., dialogues gener-
differentiate between LLMs. These findings suggest that                        ated by ChatGPT. After the SFT stage, we train a classifier to
the semantic meanings of words play a more significant role                    distinguish between responses from two fine-tuned models.
in predicting LLM origins than the exact word choice.                          We find that SFT on the same synthetic dataset significantly

                                                                          8
                                                            Idiosyncrasies in Large Language Models

reduces the classification accuracy from 96.5% to 59.8%,                             turn, most of Phi-4’s outputs are classified as originating
narrowing down the differences between these two models.                             from ChatGPT or DeepSeek.
In addition, we generate responses from Llama3.1-8B and                              Robust evaluation of LLMs. Our findings reveal a poten-
Gemma2-9B in instruct LLMs using UltraChat prompts.                                  tial vulnerability in widely used LLM evaluation method-
Then we fine-tune Qwen2.5-7B base LLM on each set of re-                             ologies. It has become a common strategy to incorporate
sponses respectively. Interestingly, responses from the two                          human judgement in evaluating LLMs, for instance, Chatbot
resulting fine-tuned models can be classified with 98.9%                             Arena (Chiang et al., 2024). It is a voting-based leaderboard
accuracy, suggesting that each fine-tuned model retains the                          where users submit preferences of the responses from two
unique characteristics in its SFT data. These findings sug-                          randomly chosen models. This benchmark has gained sig-
gest that training with synthetic data can propagate the id-                         nificant traction and is now a key reference point for frontier
iosyncrasies in the source model.                                                    model development. However, exploiting the idiosyncratic
                                                                                     property of LLM outputs, a malicious attacker can identify
We note that this behavior is not limited to synthetic datasets;
                                                                                     the model behind the candidate responses and consistently
in fact, training on different datasets often leads to idiosyn-
                                                                                     vote for the target model, thereby manipulating the leader-
cratic patterns in model outputs (Mansour & Heckel, 2024).
                                                                                     board rankings. Concurrent work by Huang et al. (2025)
Inferring model similarity. Our framework offers a quan-                             has demonstrated the feasibility of this attack in simulation.
titative approach for assessing similarities between propri-                         We hope our work brings attention to potential weaknesses
etary and open-weight LLMs. Given a set of N LLMs, we                                in current evaluation pipelines, as they can misguide model
omit one model and train a classifier on responses from the                          development and optimization efforts (Singh et al., 2025).
remaining N − 1 models. We then evaluate which LLM
the classifier associates the responses of the excluded model                        5. Related Work
with. The model that is most frequently predicted as the
source is considered the closest match to the excluded LLM.                          Dataset classification. Torralba & Efros (2011) introduced
                                                                                     the “Name That Dataset” experiment a decade ago to high-
        Prediction of ChatGPT outputs         Prediction of Claude outputs
90%                                                                                  light the bias present in visual datasets at that time. Re-
60%                                 55.9   52.9
30%             31.9                                 20.8
                                                                                     cently, Liu & He (2025) revisited this problem (termed
       2.8             2.2    7.2                             8.2   5.6   12.5
                                                                                     dataset classification) and found that current large-scale,
      Claude Grok GeminiDeepSeek Phi-4 ChatGPT Grok GeminiDeepSeek Phi-4
                                                                                     supposedly more diverse visual datasets are still very biased.
             Prediction of Grok outputs       Prediction of Gemini outputs
90% 82.8                                                                             Zeng et al. (2024) further identified structural and semantic
60%                                     40.9                                         components in images as key contributors to these biases.
30%                                                 26.5    22.0
            1.1   1.2     5.8    9.1           5.3                 5.2
   ChatGPTClaude GeminiDeepSeek Phi-4 ChatGPTClaude Grok DeepSeek Phi-4
                                                                                     You et al. (2024) and Mansour & Heckel (2024) applied
                                                                                     the dataset classification framework to study bias in syn-
        Prediction of DeepSeek outputs            Prediction of Phi-4 outputs
90%                           76.0                                                   thetic images and LLM pretraining datasets, respectively.
60%                                  46.4                      51.3
30% 16.9                                                                             While the synthetic task shown in Figure 1 is conceptually
            0.2   6.6  0.3                  0.7   1.4  0.2
   ChatGPTClaude Grok Gemini Phi-4 ChatGPTClaude Grok GeminiDeepSeek
                                                                                     similar to dataset classification, we focus not on training
                                                                                     datasets but on the distinctive characteristics inherent to
                                                                                     LLMs. Shortly after our initial arXiv preprint, Suzuki et al.
Figure 10. Inferring model similarity. We consider 6 LLMs,
including 5 chat API models and Phi-4. In each subfigure, we                         (2025) demonstrated that subtle variations in the training
evaluate a five-way classifier on outputs from the excluded LLM                      process can result in distinguishable outputs across LLMs.
and present the distribution of predicted model origins. There is a                  Human vs. machine-generated texts. Many prior works
strong tendency for LLM outputs to be predicted as ChatGPT.
                                                                                     have studied the problem of determining whether a text
                                                                                     is authored by a human or an AI system (Mitchell et al.,
This process is repeated for each of the N models. For this                          2023; Wu et al., 2023; Cai et al., 2025). Model-free ap-
analysis, we include the open-weight Phi-4 (Abdin et al.,                            proaches typically use linguistic properties such as n-gram
2024b) alongside 5 chat API models. Note that Phi-4 uses a                           frequencies (Badaskar et al., 2008; OpenAI, 2019), en-
substantial amount of synthetic data in its training.                                tropy (Lavergne et al., 2008; Gehrmann et al., 2019) or
Figure 10 shows the results. Intriguingly, for Claude, Grok,                         negative probability curvature (Mitchell et al., 2023; Bao
and Gemini, we observe a strong tendency for their outputs                           et al., 2024). Other works leverage neural network features
to be classified as ChatGPT. For instance, when Grok is                              to perform this task, such as fine-tuning BERT (Uchendu
the excluded model, 82.8% of its responses are classified                            et al., 2021; Ippolito et al., 2020). Russell et al. (2025) found
as ChatGPT. In addition, responses from ChatGPT and                                  that experienced chatbot users are good at distinguishing
DeepSeek are frequently identified as coming from Phi-4,                             between AI- and human-written articles. Neural authorship
with 55.9% and 76.0% of their responses, respectively. In                            attribution (Uchendu et al., 2020; Antoun et al., 2023; Huang

                                                                                 9
                                           Idiosyncrasies in Large Language Models

et al., 2024) seeks not only to identify machine-generated             • Third, our setup does not consider scenarios where the
text but also to attribute it to specific text generators. In            list of source LLMs could be large and even unknown be-
this work, we focus on the distinguishability between LLMs               forehand, which require further investigation. Our initial
rather than between AI vs. human.                                        results suggest it is promising: a 10-way classification
                                                                         problems involving 5 chat APIs and 5 instruct LLMs
Characteristics of machine-generated texts. Beyond de-
                                                                         including Phi-4 achieves 92.2% accuracy.
tection, it is also important to understand the distinctive
properties of machine-generated texts. N-gram frequencies              • It is interesting to examine how these idiosyncrasies
have long served as a basic signal for such purpose. McGov-              relate to model distillation (Hinton et al., 2015), a tech-
ern et al. (2024) showed that LLM outputs contain unique                 nique that has become increasingly prevalent in practice.
lexical and syntactic fingerprints that distinguish them from
human writing. Other works have examined stylometric                  Acknowledgments
features in AI-generated content (Zaitsu & Jin, 2023). Most
recently, Chakrabarty et al. (2024) studied the human-AI              We thank Zekai Wang for valuable discussions. Mingjie
alignment in the writing process, finding that professional           Sun was supported by funding from the Bosch Center for
writers can effectively identify and edit undesirable idiosyn-        Artificial Intelligence.
crasies common in LLM-generated text. Our work seeks to
provide a deeper and principled understanding behind the              Impact Statement
observed idiosyncrasies from our framework in Figure 1.
                                                                      Our study investigates the distinguishability of LLMs. On
Understanding differences between distributions. A line               the positive side, our results offer insights into LLM behav-
of research (Dunlap et al., 2024; Zhong et al., 2024) has             iors that enhance transparency, accountability and prove-
used foundation models to describe qualitative differences            nance in tracking AI generated content. This has valuable
between pairs of data distributions (e.g., image datasets).           applications such as combating misinformation, and ensur-
Gao et al. (2025) and Cai et al. (2025) conducted auditing            ing responsible use of LLMs. However, our results highlight
studies on LLM APIs to detect instances of model substi-              challenges in model training. Reliance on synthetic data or
tution, such as watermarking and quantization. The most               model distillation risks propagating biases and potentially
relevant work to us is Dunlap et al. (2025), which proposed           infringing on the intellectual property of proprietary models.
VibeCheck to understand user-aligned traits in LLM out-
puts. They found that LLMs often vary in styles, such as
being more formal or friendly. In contrast, our work aims to          References
identify broader generalizable patterns to interpret the high         Abdin, M., Aneja, J., Awadalla, H., Awadallah, A., Awan,
classification performance.                                            A. A., Bach, N., Bahree, A., Bakhtiari, A., Bao, J., Behl,
                                                                        H., Benhaim, A., Bilenko, M., Bjorck, J., Bubeck, S., Cai,
6. Conclusion                                                           M., Cai, Q., Chaudhary, V., Chen, D., Chen, D., Chen,
                                                                       W., Chen, Y.-C., Chen, Y.-L., and et al. Phi-3 technical
We demonstrate the presence of idiosyncrasies in Large                  report: A highly capable language model locally on your
Language Models (LLMs) and investigate a synthetic task                 phone. arXiv preprint arXiv:2404.14219, 2024a.
designed to quantify their extent. We find that simply fine-
tuning pretrained text embedding models on LLM outputs                Abdin, M., Aneja, J., Behl, H., Bubeck, S., Eldan, R., Gu-
leads to exceedingly high accuracy in predicting the origins            nasekar, S., Harrison, M., Hewett, R. J., Javaheripi, M.,
of the text. This phenomenon persists across diverse prompt             Kauffmann, P., Lee, J. R., Lee, Y. T., Li, Y., Liu, W.,
datasets, LLM combinations, and many other settings. We                 Mendes, C. C. T., Nguyen, A., Price, E., de Rosa, G.,
also pinpoint concrete forms of these idiosyncrasies within             Saarikivi, O., Salim, A., Shah, S., Wang, X., Ward, R.,
LLMs. We hope our work encourages further research into                Wu, Y., Yu, D., Zhang, C., and Zhang, Y. Phi-4 technical
understanding idiosyncrasies in LLMs.                                   report. arXiv preprint arXiv:2412.08905, 2024b.

We conclude by outlining several directions for future work:          Anthropic. Claude-3.5-sonnet. www.anthropic.com/
                                                                        news/claude-3-5-sonnet, 2024.
 • It is worth investigating whether our observations gener-
   alize to LLMs beyond the Transformer architecture, such            Antoun, W., Sagot, B., and Seddah, D. From text to source:
   as state space models (Gu & Dao, 2024) and diffusion-                Results in detecting large language model-generated con-
   based language models (Nie et al., 2025).                            tent. arXiv preprint arXiv:2309.13322, 2023.
 • Understanding how the training process results in these            Badaskar, S., Agarwal, S., and Arora, S. Identifying real
   idiosyncrasies remains an important open question.                   or fake articles: Towards better language modeling. In
                                                                        IJCNLP, 2008.

                                                                 10
                                           Idiosyncrasies in Large Language Models

Bao, G., Zhao, Y., Teng, Z., Yang, L., and Zhang, Y.                  Gehrmann, S., Strobel, H., and Rush, A. M. Gltr: Statistical
  Fast-detectgpt: Efficient zero-shot detection of machine-             detection and visualization of generated text. In ACL,
  generated text via conditional probability curvature. In              2019.
  ICLR, 2024.
                                                                      Google. Gemini 1.5: Unlocking multimodal understand-
BehnamGhader, P., Adlakha, V., Mosbach, M., Bahdanau,                   ing across millions of tokens of context. arXiv preprint
  D., Chapados, N., and Reddy, S. Llm2vec: Large lan-                   arXiv:2403.05530, 2024.
  guage models are secretly powerful text encoders. In
  COLM, 2024.                                                         Gu, A. and Dao, T. Mamba: Linear-time sequence modeling
                                                                        with selective state spaces. In COLM, 2024.
Ben Allal, L., Lozhkov, A., Penedo, G., Wolf, T., and
  von Werra, L. Cosmopedia. huggingface.co/                           Hinton, G., Vinyals, O., and Dean, J.     Distilling
  datasets/HuggingFaceTB/cosmopedia, 2024.                              the knowledge in a neural network. arXiv preprint
                                                                        arXiv:1503.02531, 2015.
Cai, W., Shi, T., Zhao, X., and Song, D. Are you getting
                                                                      Hu, E. J., Shen, Y., Wallis, P., Allen-Zhu, Z., Li, Y., Wang,
  what you pay for? auditing model substitution in llm apis.
                                                                        S., Wang, L., and Chen, W. LoRA: Low-rank adaptation
  arXiv preprint arXiv:2504.04715, 2025.
                                                                        of large language models. In ICLR, 2022.
Chakrabarty, T., Laban, P., and Wu, C.-S. Can ai writing
                                                                      Huang, B., Chen, C., and Shu, K. Authorship attribution in
  be salvaged? mitigating idiosyncrasies and improving
                                                                        the era of llms: Problems, methodologies, and challenges.
  human-ai alignment in the writing process through edits.
                                                                        arXiv preprint arXiv:2408.08946, 2024.
  arXiv preprint arXiv:2409.14509, 2024.
                                                                      Huang, Y., Nasr, M., Angelopoulos, A., Carlini, N., Chi-
Chiang, W.-L., Zheng, L., Sheng, Y., Angelopoulos, A. N.,               ang, W.-L., Choquette-Choo, C. A., Ippolito, D., Jagiel-
  Li, T., Li, D., Zhang, H., Zhu, B., Jordan, M. I., Gonzalez,          ski, M., Lee, K., Liu, K. Z., Stoica, I., Tramèr, F., and
  J. E., and Stoica, I. Chatbot arena: An open platform for             Zhang, C. Exploring and mitigating adversarial manip-
  evaluating llms by human preference. In ICML, 2024.                   ulation of voting-based leaderboards. arXiv preprint
                                                                        arXiv:2501.07493, 2025.
DeepSeek-AI. Deepseek-v3 technical report. arXiv preprint
  arXiv:2412.19437, 2024.                                             Ippolito, D., Duckworth, D., Callison-Burch, C., and Eck,
                                                                        D. Automatic detection of generated text is easiest when
Devlin, J., Chang, M.-W., Lee, K., and Toutanova, K. Bert:
                                                                        humans are fooled. In ACL, 2020.
  Pre-training of deep bidirectional transformers for lan-
  guage understanding. In NAACL, 2018.                                Jiang, A. Q., Sablayrolles, A., Mensch, A., Bamford, C.,
                                                                         Chaplot, D. S., de las Casas, D., Bressand, F., Lengyel,
Ding, N., Chen, Y., Xu, B., Qin, Y., Zheng, Z., Hu, S., Liu,             G., Lample, G., Saulnier, L., Lavaud, L. R., Lachaux,
  Z., Sun, M., and Zhou, B. Enhancing chat language mod-                 M.-A., Stock, P., Scao, T. L., Lavril, T., Wang, T.,
  els by scaling high-quality instructional conversations. In            Lacroix, T., and Sayed, W. E. Mistral 7b. arXiv preprint
  EMNLP, 2023.                                                           arXiv:2310.06825, 2023.
Dubey, A., Jauhri, A., Pandey, A., Kadian, A., Al-Dahle, A.,          Krishna, K., Song, Y., Karpinska, M., Wieting, J., and Iyyer,
  Letman, A., Mathur, A., Schelten, A., Yang, A., Fan, A.,              M. Paraphrasing evades detectors of ai-generated text,
  and et al. The llama 3 herd of models. arXiv preprint                 but retrieval is an effective defense. In NeurIPS, 2023.
  arXiv:2407.21783, 2024.
                                                                      Lavergne, T., Urvoy, T., and Yvon, F. Detecting fake content
Dunlap, L., Zhang, Y., Wang, X., Zhong, R., Darrell, T.,                with relative entropy scoring. In International Confer-
  Steinhardt, J., Gonzalez, J. E., and Yeung-Levy, S. De-               ence on Uncovering Plagiarism, Authorship and Social
  scribing differences in image sets with natural language.             Software Misuse, 2008.
  In CVPR, 2024.
                                                                      Lin, C.-Y. ROUGE: A package for automatic evaluation of
Dunlap, L., Mandal, K., Darrell, T., Steinhardt, J., and Gon-           summaries. In ACL, 2004.
  zalez, J. E. Vibecheck: Discover and quantify qualitative
  differences in large language models. In ICLR, 2025.                Liu, R., Wei, J., Liu, F., Si, C., Zhang, Y., Rao, J., Zheng,
                                                                        S., Peng, D., Yang, D., Zhou, D., and Dai, A. M. Best
Gao, I., Liang, P., and Guestrin, C. Model equality testing:            practices and lessons learned on synthetic data. In COLM,
  Which model is this api serving? In ICLR, 2025.                       2024.

                                                                 11
                                           Idiosyncrasies in Large Language Models

Liu, Z. and He, K. A decade’s battle on dataset bias: Are              Russell, J., Karpinska, M., and Iyer, M. People who fre-
  we there yet? In ICLR, 2025.                                           quently use chatgpt for writing tasks are accurate and
                                                                         robust detectors of ai-generated text. In ACL, 2025.
Mansour, Y. and Heckel, R. Measuring bias of web-filtered
 text datasets and bias propagation through training. arXiv            Sadasivan, V. S., Kumar, A., Balasubramanian, S., Wang,
 preprint arXiv:2412.02857, 2024.                                        W., and Feizi, S. Can ai-generated text be reliably de-
                                                                         tected? TMLR, 2025.
McGovern, H., Stureborg, R., Suhara, Y., and Alikaniotis,              Singh, S., Nan, Y., Wang, A., D’Souza, D., Kapoor, S.,
 D. Your large language models are leaving fingerprints.                 Üstün, A., Koyejo, S., Deng, Y., Longpre, S., Smith,
 In ICCL Workshops, 2024.                                                N. A., Ermis, B., Fadaee, M., and Hooker, S. The leader-
                                                                         board illusion. arXiv preprint arXiv:2504.20879, 2025.
Mitchell, E., Lee, Y., Khazatsky, A., Manning, C. D., and
 Finn, C. Detectgpt: Zero-shot machine-generated text                  Sun, C., Qiu, X., Xu, Y., and Huang, X. How to
 detection using probability curvature. In ICML, 2023.                   fine-tune bert for text classification? arXiv preprint
                                                                         arXiv:1905.05583, 2019.
Nie, S., Zhu, F., You, Z., Zhang, X., Ou, J., Hu, J., Zhou, J.,
  Lin, Y., Wen, J.-R., and Li, C. Large language diffusion             Suzuki, T., Ri, R., and Takase, S. Natural fingerprints of
  models. arXiv preprint arXiv:2502.09992, 2025.                         large language models, 2025.
                                                                       Torralba, A. and Efros, A. A. Unbiased look at dataset bias.
OpenAI. Gpt-2 output dataset detection. github.com/
                                                                         In CVPR, 2011.
  openai/gpt-2-output-dataset, 2019.
                                                                       Uchendu, A., Le, T., Shu, K., and Lee, D. Authorship
OpenAI. Gpt-4o. openai.com/index/hello-gpt-                              attribution for neural text generation. In EMNLP, 2020.
  4o/, 2024.
                                                                       Uchendu, A., Ma, Z., Le, T., Zhang, R., and Lee, D. Turing-
Penedo, G., Kydlı́ček, H., Allal, L. B., Lozhkov, A.,                   bench: A benchmark environment for turing test in the
  Mitchell, M., Raffel, C., Werra, L. V., and Wolf, T. The               age of neural text generation. In EMNLP, 2021.
  fineweb datasets: Decanting the web for the finest text              Vaswani, A., Shazeer, N., Parmar, N., Uszkoreit, J., Jones,
  data at scale. arXiv preprint arXiv:2406.17575, 2024.                  L., Gomez, A. N., Kaiser, L., and Polosukhin, I. Attention
                                                                         is all you need. In NeurIPS, 2017.
Peters, M. E., Neumann, M., Iyyer, M., Gardner, M., Clark,
  C., Lee, K., and Zettlemoyer, L. Deep contextualized                 Wu, J., Yang, S., Zhai, R., Yuan, Y., Wong, D. F., and
  word representations. In NAACL, 2018.                                 Chao, L. S. A survey on llm-generated text detection:
                                                                        Necessity, methods, and future directions. arXiv preprint
Qwen, :, Yang, A., Yang, B., Zhang, B., Hui, B., Zheng, B.,             arXiv:2310.14724, 2023.
 Yu, B., Li, C., Liu, D., Huang, F., Wei, H., Lin, H., Yang,
 J., Tu, J., Zhang, J., Yang, J., Yang, J., Zhou, J., Lin, J.,         xAI. Grok-2 beta release. x.ai/blog/grok-2, 2024.
 Dang, K., Lu, K., Bao, K., Yang, K., Yu, L., Li, M., Xue,             You, Z., Zhang, X., Guo, H., Wang, J., and Li, C. Are im-
 M., Zhang, P., Zhu, Q., Men, R., Lin, R., Li, T., Tang,                 ages indistinguishable to humans also indistinguishable
 T., Xia, T., Ren, X., Ren, X., Fan, Y., Su, Y., Zhang, Y.,              to classifiers? arXiv preprint arXiv:2405.18029, 2024.
 Wan, Y., Liu, Y., Cui, Z., Zhang, Z., and Qiu, Z. Qwen2.5
 technical report. arXiv preprint arXiv:2412.15115, 2024.              Zaitsu, W. and Jin, M. Distinguishing chatgpt(-3.5, -4)-
                                                                         generated and human-written papers through japanese
Radford, A., Wu, J., Child, R., Luan, D., Amodei, D., and                stylometric analysis. arXiv preprint arXiv:2304.05534,
  Sutskever, I. Language models are unsupervised multitask               2023.
  learners. Technical Report, 2019.
                                                                       Zeng, B., Yin, Y., and Liu, Z. Understanding bias in large-
Raffel, C., Shazeer, N., Roberts, A., Lee, K., Narang, S.,               scale visual datasets. In NeurIPS, 2024.
  Matena, M., Zhou, Y., Li, W., and Liu, P. J. Exploring               Zhao, W., Ren, X., Hessel, J., Cardie, C., Choi, Y., and
  the limits of transfer learning with a unified text-to-text            Deng, Y. Wildchat: 1m chatgpt interaction logs in the
  transformer. JMLR, 2020.                                               wild. In ICLR, 2024.
Riviere, M., Pathak, S., Sessa, P. G., Hardin, C., Bhupatiraju,        Zheng, L., Chiang, W.-L., Sheng, Y., Li, T., Zhuang, S., Wu,
  S., Hussonot, L., Mesnard, T., Shahriari, B., and et al.               Z., Zhuang, Y., Li, Z., Lin, Z., Xing, E. P., Gonzalez, J. E.,
  Gemma 2: Improving open language models at a practical                 Stoica, I., and Zhang, H. Lmsys-chat-1m: A large-scale
  size. arXiv preprint arXiv:2408.00118, 2024.                           real-world llm conversation dataset. In ICLR, 2024.

                                                                  12
                                        Idiosyncrasies in Large Language Models

Zhong, R., Wang, H., Klein, D., and Steinhardt, J. Explain-
  ing datasets in words: Statistical models with natural
  language parameters. In NeurIPS, 2024.




                                                              13
                                        Idiosyncrasies in Large Language Models

Appendix
A. Implementation Details
A.1. Response Generation
We report our procedure for generating responses from chat APIs, instruct LLMs, and base LLMs. For chat APIs, we access a
stable version of each model, including GPT-4o-2024-08-06, Claude-3.5-Sonnet-20241022, Grok-Beta, Gemini-1.5-Pro-002,
and DeepSeek-Chat, through its official API between November 28, 2024, and February 6, 2025, generating responses with
their default sampling setting. For instruct LLMs, we use greedy decoding to sample outputs. For base LLMs, we set the
temperature to T = 0.6 and apply a repetition penalty of 1.1 to avoid repetitive completions.

A.2. Training Setup
In this part, we describe our fine-tuning process using the text embedding models on LLM responses. We use the first 512
tokens of each generated response for training and evaluation. To perform sequence classification, we add a linear layer
as the classification head on top of each text embedding model. For ELMo, BERT, LLM2vec, this layer is applied to the
average embeddings over all tokens in a sequence. For T5 and GPT-2, we follow the original setups (Radford et al., 2019;
Raffel et al., 2020) and apply the head on the output of the last token.
For smaller text embedding models, such as ELMo, BERT, T5, and GPT-2, we fine-tune the entire model along with the
classification head, searching over base learning rates {3e-3, 1e-3, 3e-4, 1e-4, 3e-5, 1e-5, 3e-6, 1e-6}. For the largest
LLM2vec model, we employ the parameter-efficient LoRA (Hu et al., 2022) fine-tuning method with a rank of 16, LoRA α
of 32, a dropout rate of 0.05, and a base learning rate of 5e-5. Table 11 details our basic training recipe.

                                 config                                       value
                                 optimizer                                  AdamW
                                 weight decay                                0.001
                                 optimizer momentum                  β1 , β2 = 0.9, 0.999
                                 training epochs                                3
                                 batch size                                     8
                                 learning rate schedule                   cosine decay
                                 warmup schedule                             linear
                                 warmup ratio                                 10%
                                 gradient clip                                 0.3

                                              Table 11. Our fine-tuning recipe.




                                                             14
                                                                                           Idiosyncrasies in Large Language Models

A.3. Prompts for Open-ended Language Analysis
We detail the procedures of our open-ended language analysis in Section 3.3. Given the same input, we sample a pair
of responses from two LLMs and present them, along with an analysis prompt (see Figure 11a), to an LLM judge for
comparison. To avoid the LLM judge exploiting any prior knowledge of the models, we anonymize model identities using
an index distribution. This process is repeated for 35 response pairs, yielding a set of detailed analyses. Finally, we use the
summarization prompt (see Figure 11b) to distill these analyses into 5 bullet points that characterize the idiosyncrasies of
each model.

                                                                                                                               Below are 35 summaries that compare the unique features in 2 text
                                                                                                                               distributions point by point.
                                       Here are some samples from 2 different distributions of text.                           {Analysis 1}
                                                                                                                               {Analysis 2}
                                       Sample from distribution {1, 2}: {text sample 1}
                                                                                                                               …
                                       Sample from distribution {1, 2}: {text sample 2}
                                                                                                                               {Analysis 35}
                                       Determine the unique characteristics of the 2 distributions, and
                                                                                                                               Condense all 35 summaries into a single summary. Focus on how
                                       summarize them with five bullet points for each. Each bullet point
                                                                                                                               each summary evaluates the overall tone, specific word choices,
                                       should analyze the response from the same angle and can be easily
                                       compared by a human. Focus on key aspects that differentiate the                        opening lines, markdown formatting, and content. Provide exactly
                                       distributions. Focus on the overall tone, specific word choices, opening                five bullet points for each distribution, one for each feature. Each
                                                                                                                               bullet point should consist of a descriptive title characterizing the
                                       lines, markdown formatting, and content. Output only 5 bullet points
                                       per distribution, no additional text.                                                   feature and a short sentence explaining it concisely. Emphasize
                                                                                                                               recurring and significant features, remove the redundant ones, and
                                                                                                                               ensure the titles and sentences clearly differentiate the distributions
                                                               (a) analysis prompt                                             for easy human comparison. Output only 5 bullet points per
                                                                                                                               distribution, no additional text.


                                                                                                                                                      (b) summarization prompt

                                                                                Figure 11. Prompts in our open-ended language analysis.



B. Additional Results
B.1. Confusion Matrix
In Figure 12, we present the confusion matrix for the N -way classifiers that are trained on responses generated by chat APIs,
instruct LLMs, and base LLMs, respectively. The results demonstrate that our classifiers can accurately predict the origin of
LLM-generated responses, with minimal confusion between different LLMs.




              ground-truth
                                      96.1%     0.2%       1.0%      0.6%      2.1%
                                                                                               Llama      96.4%      0.1%       1.3%        2.2%             Llama      80.3%    0.6%       16.2%        2.9%

                                       0.4%     99.5%      0.0%      0.1%      0.0%

                                                                                           ground-truth                                                  ground-truth
                                                                                                          1.0%      98.9%       0.0%        0.1%                        0.8%     96.6%       1.4%        1.2%




Deepseek Gemini Grok Claude ChatGPT
                                       2.4%     0.2%      97.0%      0.0%      0.4%
                                                                                          Qwen Gemma      2.2%       0.2%      94.9%        2.7%        Qwen Gemma      20.9%    1.8%       75.2%        2.1%
                                       0.8%     0.0%       0.6%     98.6%      0.0%

                                       3.8%     0.3%       0.7%      0.0%     95.2%            Mistral    3.1%       0.0%       2.4%       94.5%             Mistral    4.3%     1.9%        1.7%    92.1%
                                      ChatGPT Claude       Grok     Gemini Deepseek                       Llama     Gemma        Qwen       Mistral                     Llama    Gemma        Qwen   Mistral
                                                         prediction                                                     prediction                                                   prediction
                                                   (a) chat APIs                                                  (b) instruct LLMs                                             (c) base LLMs

Figure 12. Confusion matrices for N -way classifiers on three groups of LLMs: chat APIs, instruct LLMs, and base LLMs.


B.2. Words and Letters
Figure 13 presents the frequencies of the 20 most commonly used words (left) and all English letters (right) across instruct
and base LLMs. Consistent with our observations in Section 3.1, we find notable differences in the distribution of commonly
used words between these models, such as “the”, “and”, “to”. In contrast, the letter distributions are nearly identical.

                                                                                                                         15
                                                          Idiosyncrasies in Large Language Models

                               Llama                                                                                                      Llama
 0.09                          Gemma 0.15                                                               0.06                              Gemma 0.15
 0.06                          Qwen                                                                     0.04                              Qwen
                               Mistral 0.10                                                             0.02
                                                                                                                                          Mistral 0.10
 0.03
                                       0.05                                                                                                       0.05
                                                                                                                    the
                                              ab cd e f g h i
           atnhde                                                                                                antdo
                                                                                                                                                         ab cd e f g h i
              t
              oo
           if nf                                                                                                     o
                                                                                                                    inf
                                                                j k lmn o p q
        w or                                                                                                   thfaor
                                                                                                                                                                           j k lmn o p q
        thiath
         oins t                                                                                                youtit
                                                                                r s t u vwx y
                                                                                                              witihs
                                                                                                                                                                                           r s t u vwx y
         a
      cansit                                                                                                   o
                                                                                                             thisn
                                                                                                z
    youor                                                                                                     as
                                                                                                                                                                                                           z
    ythisr
   theou
   wasir                                                                                                    aroer
                                                                                                          thwe e
                                                                                                              y
    her                                                                                                  frobmy
                             (a) instruct LLMs                                                                                            (b) base LLMs

                                          Figure 13. Word and letter frequencies in instruct and base LLMs.


B.3. Characteristic Phrases
We provide additional results for characteristic phrases as presented in Section 3.1. We follow the same methodology in
Figure 6 to extract characteristic phrases of instruct and base LLMs. Specifically, we train a four-way logistic regression
classifier on the TF-IDF features of their responses and use the coefficients to select important phrases of each model.
As shown in Figure 14, each instruct LLM contains quite distinct characteristic phrases. For example, Llama frequently
employs terms “including” and “such as” to introduce specific examples in the output, whereas Gemma tends to engage
with users using phrases “let me” and “know if”. In contrast, the extracted phrases from base LLMs are less distinctive,
primarily consisting of common words such as “the”, “to”, and “you”.
Figure 15 illustrates the distribution of first word choices in instruct and base LLMs. Similar to chat APIs (Figure 7), instruct
LLMs display varied distributions. However, base LLMs exhibit substantial overlap in their most frequent first words, e.g.,
“the”, “and”, “of”, “to”, and “in”.

      including          essentially            certainly                        title                            and                 strong                 the                                 is
    the following          know if              below is                      absolutely                           re                    h2                   re                                the
    example use           me know            certainly! here                      as                               ve                   em                     ll                              and
       such as              let me          certainly! below                     also                               ll                   h3                   or                                are
      use case       here’s a breakdown         enhance                          help                             the               blockquote              you re                               to
        which            breakdown              detailed                title comprehensive                        In                    as                answer                                in
   explanation the       states that              these                           for                              11                  there               specific                           in the
         that              specific                can                            an                               to                  here                 might                              you
        2020             remember               broader                        however                            for                  after             throughout                            your
      summary               states            certainly! the                    during                          they re                which                 like                                 it
        Llama            Gemma                  Qwen                             Mistral                        Llama               Gemma                  Qwen                             Mistral
                             (a) instruct LLMs                                                                                            (b) base LLMs
                                            Figure 14. Characteristic phrases for instruct2 and base LLMs.

                 Llama                                          Gemma                                                       Llama                                           Gemma
                         the                                                               the                                          the                                                      the
        here                             here                                                                             and                                              and
       according                        this                                                                            to                                         of
     based                           as                                                                               of                                          to
   as                                please                                                                          in                                        in
   in                                you                                                                           is                                       it
   to                                okay                                                                        it                                        is
  title                             it                                                                          for                                        this
 comprehensive                      python                                                                     we                                         for
 it                                 according                                                                  this                                      we
           0.12     0.24       0.36          0.12     0.24                                 0.36                  0.02 0.04 0.06 0.08                       0.02 0.04 0.06 0.08
                 Qwen                             Mistral                                                                    Qwen                                       Mistral
                     certainly                                                                  title                             the                                           the
                the                               the                                                                      and                                        and
        in                                  in                                                                         of                                        to
      title                               to                                                                          to                                        of
      to                               here                                                                           in                                      in
    creating                         absolutely                                                                   is                                         is
    based                           yes                                                                          this                                     for
  comprehensive                     based                                                                       it                                        it
  according                         subject                                                                     for                                      with
 sure                               creating                                                                   you                                       on
           0.12     0.24       0.36          0.12     0.24                                 0.36                  0.02 0.04 0.06 0.08                       0.02 0.04 0.06 0.08
                            (a) instruct LLMs                                                                                             (b) base LLMs
                                     Figure 15. Distribution of first word choices in instruct and base LLMs.


   2
     In Llama of instruct LLMs, the phrase “explanation the” corresponds to a markdown header or bold text for “explanation” followed
by a new sentence starting with “the”.

                                                                                                    16
                                          Idiosyncrasies in Large Language Models

B.4. Unique Markdown Formatting
In this part, we provide additional results for the analysis of markdown formatting as presented in Section 3.2. Figure 16
illustrates the distribution counts of six markdown formatting elements across different models. For both chat API models
(Figure 16a) and instruct LLMs (Figure 16b), we observe distinct differences in the usage of bold texts, headers, enumerations,
and bullet points, while italic texts show less variation. Intriguingly, Gemini uses much more italic texts (a lower density at
zero in the italic text) than other chat APIs, where similar observations can be found on Gemma2.

                                ChatGPT
1.00                            Claude   1.00
                                Grok                                                  1.00
0.75                            Gemini   0.75                                         0.75
0.50                            DeepSeek 0.50                                         0.50
0.25                                     0.25                                         0.25
    0                                         0                                           0
              10                                         10                                          6
            bold text co 20                           italic text co 20                            header coun12
                        unt          30                             unt         30                             t          18
1.00                                      1.00                                        1.00
0.75                                      0.75                                        0.75
0.50                                      0.50                                        0.50
0.25                                      0.25                                        0.25
    0                                         0                                           0
         enum10eration 20                                10
                                                     bullet point    20
                                                                                                     6
                                                                                                 code block c 12
                      count          30                             count       30                           ount         18
                                                         (a) chat APIs

                                 Llama
1.00                             Gemma 1.00                                           1.00
0.75                             Qwen    0.75                                         0.75
0.50                             Mistral 0.50                                         0.50
0.25                                     0.25                                         0.25
    0                                         0                                           0
              10                                         10                                          6
            bold text co   20                         italic text co 20                            header coun12
                        unt          30                             unt         30                             t          18
1.00                                      1.00                                        1.00
0.75                                      0.75                                        0.75
0.50                                      0.50                                        0.50
0.25                                      0.25                                        0.25
    0                                         0                                           0
         enum10eration 20                               10
                                                     bullet point 20
                                                                                                     6
                                                                                                 code block c 12
                      count          30                          count          30                           ount         18
                                                      (b) instruct LLMs

                    Figure 16. Markdown formatting elements for chat APIs (top) and instruct LLMs (bottom).




                                                              17
                                                   Idiosyncrasies in Large Language Models

B.5. Rewriting LLM outputs
In Section 3.3, we used GPT-4o-mini to rewrite LLM outputs. Here, we present results using an alternative model: Qwen2.5-
7B-Instruct. As shown in Table 12, our observations remain consistent, indicating that our findings are robust to the choice
of LLM used for rewriting.

                                   LLM for rewriting           original       paraphrase       translate      summarize
                                   GPT-4o-mini                   97.8            93.6            93.9            63.7
                                   Qwen2.5-7B-Instruct           97.8            92.6            94.3            71.5
                  Table 12. Classification accuracies on rewritten responses. The results are on Chat API responses.

B.6. Open-ended Language Analysis
Ablation on LLM judges. Here we demonstrate our findings in Figure 9 of Section 3.3 remains consistent under several
LLM judges. Specifically, we change the LLM judge from ChatGPT to Claude, Grok, and Gemini. We show the results
in Figure 17. Regardless of the choice of LLM judges, our language analysis reveals that ChatGPT often uses detailed
explanations and complex formatting structures, whereas Claude emphasizes key contents without extensive elaboration.

• Tone: Authoritative and formal, using academic language with detailed        • Tone: Analytical and cautious, frequently referencing source material and
explanations and complex sentence structures                                   acknowledging limitations
• Word Choice: Rich descriptive vocabulary with technical terms, metaphors,    • Word Choice: Simpler, more practical vocabulary focused on clarity and
and evaluative language ("renowned," "instrumental," "exquisite")              accessibility rather than style
• Opening Style: Direct statements or enthusiastic "Certainly!" responses      • Opening Style: Meta-references like "According to the text" or explicit
that establish context and preview content                                     disclaimers about content limitations
• Markdown Usage: Extensive formatting with bold headers, nested bullet        • Markdown Usage: Minimal formatting with basic bullet points or simple
points, and hierarchical section markers                                       numbered lists
• Content Structure: Comprehensive paragraphs with detailed explanations,      • Content Structure: Concise bullet points and brief statements organized in
examples, and flowing transitions between ideas                                categorical lists without extensive elaboration
                                ChatGPT                                                                              Claude
                                                            (a) Claude as the LLM judge.

- Tone: Warm and Informative - Uses an inviting, educational tone to           - Tone: Direct and Practical - Often concise, focusing on actionable insights or
engage and inform the reader.                                                  straightforward information.
- Word Choices: Descriptive and Detailed - Employs rich, technical, or         - Word Choices: Simple and Functional - Prefers straightforward language,
emotive language to enhance understanding or evoke emotion.                    emphasizing utility over emotional or detailed descriptions.
- Opening Lines: Contextual and Engaging - Provides context or a               - Opening Lines: Immediate and Focused - Jumps directly into the topic or lists
narrative hook to draw readers in.                                             key points without much preamble.
- Markdown Formatting: Structured and Emphasized - Extensive use of            - Markdown Formatting: Minimalist - Uses basic markdown elements like bullet
headings, lists, and bold text for clarity and organization.                   points or simple lists for clarity.
- Content: Comprehensive and Insightful - Focuses on in-depth                  - Content: Succinct and Focused - Provides essential information with less depth,
explanations, examples, and broad implications.                                often aiming for quick readability or practicality.
                                ChatGPT                                                                              Claude
                                                             (b) Grok as the LLM judge.

• Formal Tone: Often adopts a formal, academic, or instructional tone,         • Informal Tone: Generally uses a more informal, conversational, or concise
prioritizing clarity and detail.                                               tone, prioritizing brevity and accessibility.
• Precise Diction: Employs specific, descriptive, and sometimes technical      • Simplified Language: Favors simpler, more direct vocabulary, avoiding
vocabulary relevant to the subject matter.                                     jargon and focusing on key information.
• Contextual Openings: Typically begins with introductory statements,          • Direct Openings: Often starts directly with the main point or a summary of
context-setting, or clear purpose statements.                                  key information.
• Structured Formatting: Frequently utilizes headings, lists, bolding, and     • Minimal Formatting: Uses less markdown formatting, relying primarily on
other markdown features for organization and emphasis.                         basic lists, bullet points, or plain text.
• Comprehensive Content: Provides detailed explanations, examples, and         • Concise Content: Focuses on summarizing key points, offering practical
in-depth information, often covering a broader scope.                          advice, or providing concise overviews.
                                ChatGPT                                                                              Claude
                                                            (c) Gemini as the LLM judge.

              Figure 17. Results of our open-ended language analysis on ChatGPT and Claude with different LLM judges.




                                                                              18
                                                      Idiosyncrasies in Large Language Models

Open-ended language analysis results on other LLMs. In Section 3.3, we presented the results of open-ended language
analysis for ChatGPT and Claude. Here, we extend our analysis to other chat API models and instruct LLMs. The full
results are shown in Figure 18, where we use ChatGPT as the LLM judge to compare responses generated by two models
within the same category (chat APIs / instruct LLMs). Our analysis highlights several interesting characteristics of each
model. For example, Grok’s responses tend to feature rich language and comprehensive content, whereas Gemini’s outputs
are more concise with direct openings.

- Descriptive Tone: Emphasizes detail, narrative, or objective perspectives,       - Concise Tone: Often adopts a straightforward, direct, or expressive
often exploring themes with depth and nuance.                                      approach focusing on succinctness and dramatic tension.
- Rich Language: Incorporates emotive, analytical, or descriptive language         - Specific Language: Utilizes precise or vivid language to convey themes
to enhance understanding and engagement.                                           like tension, urgency, and significant events or outcomes.
- Detailed Openings: Introduces the subject with context, thematic                 - Direct Openings: Typically begins with immediate context or action,
elements, or guiding points, establishing a comprehensive view.                    setting a focused tone or premise from the start.
- Structured Formatting: Utilizes formatting elements like headings, lists,        - Simple Formatting: Relies mainly on plain text or minimal formatting to
and bold text to organize information clearly.                                     maintain clarity and directness.
- Comprehensive Content: Delivers in-depth analysis or exploration of              - Core Content: Centers on key insights or motivations, providing essential
subjects, highlighting diverse factors or broader implications.                    information or narratives with limited embellishment.
                                     Grok                                                                             Gemini
                                                                         (a) chat APIs

 - Tone Characterization: Often formal, factual, and exacting, emphasizing         - Tone Characterization: Generally more conversational, engaging, and
 detailed analysis and structured presentations.                                   accessible, often blending storytelling or personal insights.
 - Word Choices Depiction: Technical and precise, leveraging industry-             - Word Choices Depiction: Simple, expressive, and often emotive
 specific or academic terminology to convey depth and credibility.                 language, creating relatability and narrative flair.
 - Opening Line Initiation: Frequently starts directly with context, setting an    - Opening Line Initiation: Begins engagingly, often with context or an
 immediate formal or informative tone.                                             emotional hook, to capture the reader's interest.
 - Markdown Use: Prefers structured formats with headings, bullet points, or       - Markdown Use: Employs varied markdown elements like bullet points or
 numbered lists to enhance clarity.                                                emphasis for readability and structure.
 - Content Focus: Delivers comprehensive, detailed content with substantial        - Content Focus: Centers on overarching concepts, insights, and
 data, examples, or specific tactics.                                              experiences, often prioritizing engagement over exhaustive detail.
                                    Llama                                                                             Gemma

- Detailed and Analytical Tone: The tone is often formal, focusing on              - Concise and Direct Tone: The tone is generally straightforward, practical,
analysis, exploration, and organized narratives.                                   and sometimes conversational, focusing on direct explanations.
- Descriptive and Formal Word Choices: Uses technical and descriptive              - Simplified and Emotive Word Choices: Prefers straightforward
vocabulary that highlights complexity and depth.                                   language, occasionally prioritizing emotional or motivational impact.
- Comprehensive Opening Lines: Starts often with broad context or                  - Immediate Opening Lines: Begins directly with subject matter or actions,
detailed introductions, setting a formal framework.                                often in conversational or narrative styles.
- Structured Markdown Formatting: Utilizes headers, sections, and lists to         - Minimalist Markdown Formatting: Uses simpler formatting with lists or
enhance readability and organization.                                              plain text to maintain clarity without embellishments.
- Content Depth and Exploration: Provides comprehensive narratives with            - Summary Focused Content: Concentrates on key points with succinct
detailed discussions, focusing on systematic approaches and analysis.              explanations, prioritizing clarity and accessibility over comprehensive detail.
                                    Qwen                                                                               Mistral
                                                                      (b) instruct LLMs

            Figure 18. Additional results of our open-ended language analysis on chat APIs (top) and instruct LLMs (bottom).




                                                                                  19
                                               Idiosyncrasies in Large Language Models

C. Response Demonstrations
In this part of the appendix, we present examples of LLM responses. Table 13 and 14 illustrate responses before and after
our prompt-level interventions (Section 2.2). Table 15 shows the transformed responses when only markdown elements are
retained (Section 3.2).
Table 16 presents the LLM rewritten responses (Section 3.3). For paraphrasing, we find that formatting style remains largely
unchanged, e.g., the number of enumerated lists are the same. Most of the differences lie in their word choices, paraphrased
texts use different words with similar meanings but do not change the high-level semantic meaning of the original texts.
Additionally, Table 17 provides a pairwise comparison of responses, supporting our findings in Table 9. Table 18, 19, 20, 21,
22, 23, 24, 25, 26, 27, 28, 29, 30 contain example responses from each LLM considered in Section 2, including ChatGPT,
Claude, Grok, Gemini, DeepSeek, Llama3.1-8b (instruct), Gemma2-9b (instruct), Qwen2.5-7b (instruct), Mistral-v3-7b
(instruct), Llama3.1-8b (base), Gemma2-9b (base), Qwen2.5-7b (base), and Mistral-v3-7b (base).

    Can you suggest any other cheese alternatives that I can use instead of Brie for this recipe? Generate according to: Add one or two
    slices Brie o the beef and let it melt. Cut the green apple in thin slices. Top with the mixed salad and finish with the apple slices.
    If you’re looking for cheese alternatives to Brie for your recipe, consider the following options:
       1. Camembert: This cheese is quite similar to Brie in texture and flavor, offering a creamy consistency and a mild, earthy taste
          that will complement the beef and apple.
       2. Taleggio: An Italian cheese with a soft texture and a tangy, fruity flavor. It melts well and can add a unique twist to your dish.
       3. Fontina: Known for its smooth melting properties, Fontina has a nutty and slightly sweet flavor that pairs nicely with beef
          and apples.
       4. Goat Cheese: If you prefer a tangier option, goat cheese can provide a creamy texture and a distinct flavor that contrasts well
          with the sweetness of the apple.
       5. Havarti: A semi-soft cheese with a buttery and slightly sweet taste, Havarti melts beautifully and can be a great substitute for
          Brie.
    These alternatives should work well in your recipe, providing a delicious and melty addition to your beef and apple combination.
                                                                (a) original

    Can you suggest any other cheese alternatives that I can use instead of Brie for this recipe? Generate according to: Add one or two
    slices Brie o the beef and let it melt. Cut the green apple in thin slices. Top with the mixed salad and finish with the apple slices.

    Please provide a concise response in a single paragraph, limited to a maximum of 100 words.
    For a delicious alternative to Brie, consider using Camembert or triple cream cheese, both of which offer a similar creamy texture
    and rich flavor. If you prefer a slightly tangier option, goat cheese can provide a delightful contrast to the beef and apple. For a
    milder taste, Havarti or Fontina can melt beautifully and complement the dish’s flavors. Each of these cheeses will add a unique
    twist while maintaining the creamy, melt-in-your-mouth experience that Brie provides.
                                                            (b) length control

    Can you suggest any other cheese alternatives that I can use instead of Brie for this recipe? Generate according to: Add one or two
    slices Brie o the beef and let it melt. Cut the green apple in thin slices. Top with the mixed salad and finish with the apple slices.

    Please provide your response in plain text only, avoiding the use of italicized or bold text, lists, markdown, or HTML formatting.
    You can use Camembert or triple cream cheese as alternatives to Brie in your recipe. Both have a similar creamy texture and rich
    flavor that will complement the beef and other ingredients.
                                                            (c) format control

                                     Table 13. Examples of prompt-level interventions on ChatGPT.




                                                                      20
                                            Idiosyncrasies in Large Language Models




Can you suggest any other cheese alternatives that I can use instead of Brie for this recipe? Generate according to: Add one or two slices
Brie o the beef and let it melt. Cut the green apple in thin slices. Top with the mixed salad and finish with the apple slices.
If you’re looking for alternatives to Brie cheese in your recipe, here are some options you can consider:
  1. Goat Cheese: A soft and creamy cheese with a tangy flavor that pairs well with the sweetness of the apple and the savory flavor of
     the beef.
  2. Feta Cheese: A salty and crumbly cheese that adds a nice contrast to the softness of the beef and the crunch of the apple.
  3. Camembert: A French cheese with a creamy texture and a mild, earthy flavor that complements the beef and apple nicely.
  4. Blue Cheese: A strong and pungent cheese that adds a bold flavor to the dish. Use a milder blue cheese if you’re not a fan of strong
     flavors.
  5. Mascarpone: A rich and creamy cheese that adds a luxurious touch to the dish. It’s a good option if you want a milder flavor than
     Brie.
  6. Ricotta: A soft and creamy cheese that’s a good option if you want a lighter flavor than Brie. It’s also a good choice if you’re
     looking for a lower-calorie alternative.
  7. Taleggio: An Italian cheese with a creamy texture and a mild, fruity flavor that pairs well with the apple and beef.
When substituting Brie, keep the following in mind:
   • If using a stronger cheese like Blue Cheese or Goat Cheese, use a smaller amount to avoid overpowering the other flavors.
   • If using a milder cheese like Mascarpone or Ricotta, you may want to add a bit more to achieve the desired creaminess.
   • If using a crumbly cheese like Feta, you may want to crumble it instead of slicing it to distribute the flavor evenly.
Remember, the key is to balance the flavors and textures in your dish, so feel free to experiment and find the combination that works best
for you!
                                                             (a) original

Can you suggest any other cheese alternatives that I can use instead of Brie for this recipe? Generate according to: Add one or two slices
Brie o the beef and let it melt. Cut the green apple in thin slices. Top with the mixed salad and finish with the apple slices.

Please provide a concise response in a single paragraph, limited to a maximum of 100 words.
If you’re looking for alternatives to Brie, consider using other soft-ripened cheeses like Camembert, Goat Cheese, or Feta. Alternatively,
you could opt for a semi-soft cheese like Havarti or Muenster. For a stronger flavor, try using Blue Cheese or Gorgonzola. If you prefer a
milder taste, Boursin or Mascarpone could work well. Each of these cheeses will melt and complement the beef and apple nicely, adding a
unique twist to your dish. Simply replace the Brie with your chosen cheese and proceed with the recipe as instructed.
                                                          (b) length control

Can you suggest any other cheese alternatives that I can use instead of Brie for this recipe? Generate according to: Add one or two slices
Brie o the beef and let it melt. Cut the green apple in thin slices. Top with the mixed salad and finish with the apple slices.

Please provide your response in plain text only, avoiding the use of italicized or bold text, lists, markdown, or HTML formatting.
You can consider the following cheese alternatives to Brie in your recipe:
Camembert: This French cheese has a similar creamy texture and mild, earthy flavor to Brie, making it a suitable substitute.
Goat cheese: A tangy and creamy cheese that pairs well with the sweetness of the apple and the savory flavor of the beef.
Feta: A crumbly Greek cheese that adds a salty flavor to the dish, which can balance out the sweetness of the apple.
Blue cheese: A strong and pungent cheese that can add a bold flavor to the dish, but be aware that it may overpower the other ingredients.
Ricotta: A mild and creamy cheese that can add a light and airy texture to the dish, but it may not provide the same richness as Brie.
Mascarpone: An Italian cheese with a rich and creamy texture that can add a luxurious feel to the dish, but it may be sweeter than Brie.
Keep in mind that each of these alternatives will change the flavor profile of the dish, so you may need to adjust the other ingredients
accordingly.
                                                          (c) format control

                           Table 14. Examples of prompt-level interventions on Llama3.1-8b-Instruct.




                                                                   21
                                          Idiosyncrasies in Large Language Models




What are some effective tactics for building a referral network and gaining new business through word-of-mouth?
Building a strong referral network and gaining new business through word-of-mouth can be highly effective and cost-efficient.
Here are some tactics to achieve this:
  1. Deliver Exceptional Service: The foundation of word-of-mouth marketing is consistent excellence. Providing top-notch
     services or products encourages satisfied customers to share their positive experiences with others.
  2. Identify and Nurture Key Relationships: Focus on building strong relationships with clients, partners, and industry peers
     who can refer you to others. Personalize your interactions and maintain regular communication to keep these relationships
     strong.
  3. Ask for Referrals: Don’t hesitate to ask satisfied clients for referrals. Timing is crucial—make the request at the peak of
     their satisfaction. Be clear about the type of referrals you are seeking.
  4. Referral Incentives: Offer incentives such as discounts, gift cards, or exclusive access to services to encourage customers or
     partners to refer new business to you. Ensure these incentives are enticing enough to motivate action.
  5. Leverage Social Proof: Encourage satisfied customers to leave reviews or testimonials online. Positive reviews on platforms
     such as Google, Yelp, or LinkedIn can influence potential clients.
  6. Engage on Social Media: Use social media platforms to share success stories, client testimonials, and updates about your
     business. Engage with your audience through comments, shares, and likes to build a community around your brand.
  7. Host Events: Organize events such as workshops, webinars, or networking meet-ups. These events provide value, showcase
     your expertise, and encourage attendees to refer you to others.
  8. Partner with Complementary Businesses: Collaborate with businesses that offer complementary services or products. This
     creates mutual referral opportunities and extends your reach to their customer base.
  9. Create a Referral Program: Formalize your referral process with a structured program, ensuring referrers are aware of the
     benefits and the procedure. Clearly communicate the value proposition and streamline the referral process.
 10. Stay Top-of-Mind: Regularly connect with your network through emails, newsletters, or personalized messages. Share
     updates, industry insights, or tips that position you as a valuable and knowledgeable resource.
 11. Thank Referrers: Always express gratitude to those who refer new business to you. Acknowledging their support strengthens
     relationships and encourages further referrals.
 12. Measure and Optimize: Track where your referrals are coming from and the effectiveness of different tactics. Use this data
     to optimize your approach, focusing on strategies that yield the best results.
By implementing these tactics and consistently nurturing your network, you can effectively build a robust referral system that
generates new business through word-of-mouth recommendations.
                                                         (a) original

xxx
  1. xxxxxx
  2. xxxxxx
  3. xxxxxx
  4. xxxxxx
  5. xxxxxx
  6. xxxxxx
  7. xxxxxx
  8. xxxxxx
  9. xxxxxx
 10. xxxxxx
 11. xxxxxx
 12. xxxxxx
xxx

                                                (b) markdown elements only

      Table 15. Examples of only using markdown formatting elements and replacing text content with “xxx” placeholders.




                                                               22
                                          Idiosyncrasies in Large Language Models


What are some ways to cope with feelings of loneliness or isolation?
Coping with feelings of loneliness or isolation can be challenging, but there are several strategies that might help:
  1. Connect with Others: Reach out to friends and family through phone calls, video chats, or messaging apps. Joining clubs,
     groups, or online communities related to your interests can also help you meet new people.
  2. Volunteer: Helping others can provide a sense of purpose and community. Look for local organizations or virtual opportunities
     where you can volunteer your time or skills.
  3. Engage in Hobbies: Pursue activities or hobbies that you enjoy, whether it’s reading, painting, cooking, or playing a musical
     instrument. These can be fulfilling and help distract from loneliness.
  4. Physical Activity: Exercise is known to boost mood and alleviate stress. Try walking, jogging, yoga, or any form of physical
     activity that you enjoy.
  5. Mindfulness and Meditation: Practices such as meditation, deep breathing, or mindfulness can help anchor you in the
     present moment and reduce feelings of loneliness.
  6. Professional Help: Consider speaking with a therapist or counselor, who can provide support and coping strategies tailored
     to your situation.
  7. Pet Companionship: If feasible, consider getting a pet. Animals can offer companionship and can be a source of comfort
     and joy.
  8. Limit Social Media: While it might seem connecting, excessive use of social media can sometimes exacerbate feelings of
     loneliness. Set boundaries for healthier use.
  9. Self-Compassion: Practice being kind to yourself. Acknowledge your feelings without judgment and remind yourself that
     it’s okay to feel lonely at times.
 10. Set Goals: Setting small, achievable goals can provide a sense of accomplishment and forward momentum, fostering a sense
     of purpose.
 11. Seeking Community Spaces: Libraries, community centers, or cafes can be great places to be around others, even if you’re
     not directly interacting with them.
Remember, everyone experiences loneliness differently, and it’s important to find what works best for you.
                                                          (a) original

Dealing with feelings of loneliness or isolation can be tough, but there are various strategies that may help:
  1. Reach Out: Contact friends and family through phone calls, video chats, or messaging platforms. Joining clubs, groups, or
     online communities that align with your interests can also help you connect with new people.
  2. Volunteer Your Time: Helping others can give you a sense of purpose and community. Look for local charities or online
     opportunities to contribute your time or skills.
  3. Pursue Your Hobbies: Engage in activities you enjoy, such as reading, painting, cooking, or playing a musical instrument.
     These pursuits can be satisfying and provide a distraction from feelings of loneliness.
  4. Stay Active: Regular exercise is known to improve mood and reduce stress. Try activities like walking, jogging, yoga, or any
     form of physical exercise that appeals to you.
  5. Practice Mindfulness: Techniques such as meditation, deep breathing, or mindfulness can help ground you in the present
     and alleviate feelings of loneliness.
  6. Consider Professional Guidance: Talking to a therapist or counselor can provide helpful support and coping techniques
     tailored to your needs.
  7. Get a Pet: If it’s an option for you, think about adopting a pet. Animals can be wonderful companions and bring joy and
     comfort into your life.
  8. Limit Social Media Use: Though it may seem like a way to connect, extensive use of social media can sometimes increase
     feelings of loneliness. Establish limits for a healthier engagement.
  9. Be Kind to Yourself: Practice self-compassion by acknowledging your feelings without judgment and reminding yourself
     that it’s normal to feel lonely occasionally.
 10. Set Achievable Goals: Creating small, realistic goals can foster a sense of accomplishment and help you move forward,
     enhancing your sense of purpose.
 11. Use Community Spaces: Places like libraries, community centers, or cafes can provide an opportunity to be around others,
     even if you’re not directly interacting with them.
Remember, everyone experiences loneliness in different ways, so it’s essential to discover what strategies work best for you.
                                                        (b) paraphrasing

Coping with loneliness can be challenging, but several strategies can help. Connecting with friends and family, volunteering, and
engaging in enjoyable hobbies can foster a sense of community. Physical activity and mindfulness practices can improve mood and
reduce stress. Seeking professional help and considering companionship from pets may also provide comfort. It’s essential to limit
social media usage, practice self-compassion, set small goals for achievement, and explore community spaces like libraries or cafes.
Ultimately, finding individualized approaches that resonate with you is key to managing feelings of loneliness.
                                                        (c) summarizing

                                   Table 16. Examples of LLM rewriting using GPT-4o-mini.


                                                                23
                                            Idiosyncrasies in Large Language Models




What are some ways to cope with feelings of loneliness or isolation?
                                                                         There are several healthy ways to cope with loneliness and
                                                                         isolation:
Coping with feelings of loneliness or isolation can be chal-               1. Maintain social connections:
lenging, but there are several strategies that might help:
   1. Connect with Others: Reach out to friends and family                  • Call or video chat with friends and family
       through phone calls, video chats, or messaging apps.                 • Send messages, emails, or letters
       Joining clubs, groups, or online communities related to              • Join online communities or social media groups
       your interests can also help you meet new people.                    • Schedule regular virtual meetups
   2. Volunteer: Helping others can provide a sense of pur-                2. Pursue hobbies and interests:
       pose and community. Look for local organizations or
       virtual opportunities where you can volunteer your time              • Take up a new hobby
       or skills.                                                           • Join clubs or groups related to your interests
   3. Engage in Hobbies: Pursue activities or hobbies that                  • Take online classes
       you enjoy, whether it’s reading, painting, cooking, or               • Learn a new skill
       playing a musical instrument. These can be fulfilling               3. Physical activities:
       and help distract from loneliness.
   4. Physical Activity: Exercise is known to boost mood                    • Exercise regularly
       and alleviate stress. Try walking, jogging, yoga, or any             • Take walks outdoors
       form of physical activity that you enjoy.                            • Practice yoga or meditation
   5. Mindfulness and Meditation: Practices such as medi-                   • Stay physically active
       tation, deep breathing, or mindfulness can help anchor              4. Connect with your community:
       you in the present moment and reduce feelings of loneli-
       ness.                                                                • Volunteer
   6. Professional Help: Consider speaking with a therapist                 • Join local organizations
       or counselor, who can provide support and coping strate-             • Attend community events
       gies tailored to your situation.                                     • Participate in religious or spiritual groups
   7. Pet Companionship: If feasible, consider getting a pet.              5. Self-care practices:
       Animals can offer companionship and can be a source
       of comfort and joy.                                                  • Maintain a routine
   8. Limit Social Media: While it might seem connecting,                   • Practice mindfulness
       excessive use of social media can sometimes exacerbate               • Keep a journal
       feelings of loneliness. Set boundaries for healthier use.            • Get enough sleep
   9. Self-Compassion: Practice being kind to yourself. Ac-                 • Eat healthy meals
       knowledge your feelings without judgment and remind                 6. Seek professional help:
       yourself that it’s okay to feel lonely at times.
 10. Set Goals: Setting small, achievable goals can provide                 • Talk to a therapist or counselor
       a sense of accomplishment and forward momentum,                      • Join support groups
       fostering a sense of purpose.                                        • Consider online therapy options
 11. Seeking Community Spaces: Libraries, community                        7. Adopt or care for a pet:
       centers, or cafes can be great places to be around others,
       even if you’re not directly interacting with them.                   • Pets provide companionship
Remember, everyone experiences loneliness differently, and                  • Create a sense of purpose
it’s important to find what works best for you.                             • Encourage routine and responsibility
                                                                         Remember that feeling lonely is a common human experience,
                       (a) ChatGPT                                       and it’s okay to reach out for help when needed.

                                                                                                (b) Claude

    Table 17. Examples from ChatGPT and Claude that illustrate results of our open-ended language analysis in Figure 9.




                                                                    24
                                          Idiosyncrasies in Large Language Models

Can polar bears migrate to new habitats if their Arctic environment changes too drastically?
Polar bears are highly specialized animals adapted to the Arctic environment, primarily relying on sea ice for hunting seals, their
main prey. If their Arctic environment changes drastically, such as through significant sea ice loss due to climate change, their
ability to migrate to new habitats is limited by several factors:
   1. Species Adaptation: Polar bears are uniquely adapted to life on sea ice and in cold climates. They have thick fur, a layer of
      fat for insulation, and physical characteristics like large paws for swimming and walking on ice. These adaptations make it
      difficult for them to survive in non-polar environments.
   2. Dietary Needs: Their diet consists mainly of seals, which they hunt on sea ice. New habitats may not support a sufficient seal
      population or alternative prey that polar bears can easily exploit.
   3. Geographical Barriers: Polar bears are largely confined to the Arctic and areas surrounding the North Pole. There are no
      direct routes to migrate to other cold environments that would support them in a similar way.
   4. Competition and Predation: Moving to new habitats would likely involve entering territories with existing ecosystems that
      include competition for food from other predators or unfamiliar threats.
   5. Habitat Fragmentation: The fragmentation of ice habitats does not create viable paths for migration but rather isolates
      populations, reducing genetic diversity and making survival more precarious.
In conclusion, while polar bears might be able to make small relocations within the Arctic as sea ice conditions shift, extensive
migration to entirely new habitats is not feasible due to their specific adaptations and the absence of suitably similar environments
elsewhere. Conservation efforts focus more on mitigating climate change and preserving their current habitat.


                                            Table 18. Example response of ChatGPT.

Can polar bears migrate to new habitats if their Arctic environment changes too drastically?
Polar bears have limited ability to migrate to new habitats if Arctic conditions become unsuitable. They are highly specialized
for life on sea ice and depend on it for hunting seals, their primary food source. While they can swim long distances, moving to
southern territories would be challenging because: 1) they are not well-adapted to warmer climates, 2) their hunting techniques are
specific to ice-based prey, and 3) competition with other bear species and humans would increase. Their survival is closely tied to
maintaining Arctic sea ice habitat.


                                             Table 19. Example response of Claude.

Can polar bears migrate to new habitats if their Arctic environment changes too drastically?
Polar bears are highly specialized for their Arctic environment, and their ability to migrate to entirely new habitats is limited by
several factors:
  1. Adaptation: Polar bears are adapted to cold environments with a diet primarily consisting of seals, which they hunt from sea
      ice. Their thick fur, large size, and fat reserves are suited for Arctic conditions, not temperate or tropical climates.
  2. Habitat Requirements: They need sea ice for hunting, breeding, and resting. Without ice, their ability to catch seals, which
      is their primary food source, is severely compromised. Alternative habitats would need to provide similar conditions or
      abundant alternative prey, which is rare outside the Arctic.
  3. Physiological Limitations: Polar bears might find it challenging to adapt to significantly different temperatures or ecosystems.
      For instance, their large bodies and fur make them prone to overheating in warmer climates.
  4. Behavioral Flexibility: While bears in general can be quite adaptable in terms of diet (e.g., grizzly bears), polar bears have
      evolved in an environment with very specific conditions. Their behavioral adaptations are finely tuned to the Arctic, reducing
      the likelihood of successful migration to drastically different environments.
  5. Human Activity: As polar bears move southward in search of food or better conditions, they increasingly encounter human
      populations and infrastructure, leading to conflicts, habitat fragmentation, and often, negative outcomes for the bears.
  6. Genetic Considerations: Polar bears have evolved in relative isolation in the Arctic. Mixing with other bear species or
      adapting to entirely new environments could lead to genetic issues or dilution of their specialized adaptations.
However, there are some considerations:
    • Hybridization: There’s evidence of polar bears mating with grizzly bears (creating ”pizzly” or ”grolar” bears) in areas where
      their ranges overlap due to climate change. This might be seen as a form of adaptation or migration at a genetic level, though
      it’s not migration in the traditional sense.
    • Range Expansion: Some polar bears have been observed traveling further south than usual, likely in search of food as ice
      recedes. However, this is more about extending their current habitat rather than migrating to a completely different one.
    • Conservation Efforts: Efforts might focus on preserving or creating corridors where polar bears can move between suitable
      habitats or on habitat restoration to ensure the Arctic remains viable for them.
In summary, while polar bears could potentially expand their range or adapt behaviorally to some extent, true migration to entirely
new, non-Arctic habitats is unlikely due to their specific ecological needs and physiological adaptations. Conservation efforts are
more focused on mitigating the impacts of climate change in their current habitat or facilitating their movement within the Arctic
region.


                                              Table 20. Example response of Grok.


                                                                 25
                                            Idiosyncrasies in Large Language Models




Can polar bears migrate to new habitats if their Arctic environment changes too drastically?
While polar bears have some capacity for movement and adaptation, large-scale migration to entirely new habitats in response to
Arctic change is highly unlikely and faces significant obstacles:
   • Physiological Specialization: Polar bears are highly specialized for Arctic life. Their thick blubber, fur, and hunting
      techniques are specifically adapted for cold, icy environments. They rely heavily on sea ice for hunting seals, their primary
      food source. Relocating to warmer environments with different prey and terrain would be extremely challenging.
   • Competition and Existing Ecosystems: Other bear species or large predators already occupy potential alternative habitats.
      Introducing polar bears would create competition for resources and potentially disrupt existing ecosystems. Polar bears are
      apex predators, and their presence would have cascading effects.
   • Limited Land-Based Food Sources: While polar bears can sometimes scavenge on land, terrestrial food sources are
      insufficient to sustain their large body size and energy demands. They are primarily dependent on the rich calorie content of
      seals. Land-based food would not be abundant enough to support large populations.
   • Human-Wildlife Conflict: As polar bears are forced further south or into more populated areas in search of food due to
      shrinking sea ice, encounters with humans are likely to increase, leading to conflict and potential danger for both bears and
      people. Relocation efforts could exacerbate this issue.
   • Distance and Barriers: Potential alternative habitats are often geographically distant from the Arctic. Natural barriers such
      as mountains, oceans, and unsuitable terrain would make migration extremely difficult. Furthermore, suitable habitat may
      already be occupied by other species or fragmented by human development.
   • Genetic Adaptation Takes Time: While some level of adaptation is possible within a species, evolving to thrive in a
      completely different environment takes many generations. The rapid pace of Arctic change is outpacing the ability of polar
      bears to adapt genetically to significantly different conditions.
Instead of large-scale migration, polar bears are more likely to exhibit smaller-scale shifts in range, dietary changes (though with
limited success), and increased hybridization with grizzly bears. However, the long-term survival of the species ultimately depends
on mitigating climate change and preserving their Arctic habitat.


                                              Table 21. Example response of Gemini.




Can polar bears migrate to new habitats if their Arctic environment changes too drastically?
Polar bears are highly specialized for life in the Arctic, relying on sea ice to hunt their primary prey, seals. If the Arctic environment
changes too drastically, particularly due to climate change and the loss of sea ice, polar bears would face significant challenges in
migrating to new habitats. Here are some key points to consider:
  1. Specialization: Polar bears are adapted to the cold, icy conditions of the Arctic. Their physical and behavioral traits are
      finely tuned to this environment, making it difficult for them to thrive in vastly different habitats.
  2. Prey Availability: Polar bears primarily hunt seals, which are also dependent on sea ice. If sea ice diminishes, both polar
      bears and their prey would be affected. Moving to new habitats would require finding alternative food sources, which may
      not be as abundant or accessible.
  3. Geographic Barriers: The Arctic is relatively isolated, and polar bears would face significant geographic barriers if they
      attempted to migrate to new areas. Moving southward would bring them into competition with other bear species, such as
      grizzly bears, and into environments that are not suited to their specific needs.
  4. Human Impact: Many potential new habitats for polar bears are already occupied by humans. Human activities, such as
      urban development, agriculture, and industry, could pose additional challenges for polar bears trying to adapt to new areas.
  5. Genetic Adaptation: Over long periods, species can adapt to new environments through genetic changes. However, the rapid
      pace of climate change may outstrip the ability of polar bears to adapt quickly enough to survive in significantly altered or
      new habitats.
  6. Conservation Efforts: Conservation strategies are being developed to help polar bears cope with changing environments.
      These include protecting critical habitats, reducing greenhouse gas emissions to mitigate climate change, and researching
      potential relocation or assisted migration options.
In summary, while polar bears have some capacity to adapt to changing conditions, their specialized nature and the rapid pace of
environmental change pose significant challenges to their ability to migrate to and thrive in new habitats. Conservation efforts are
crucial to ensuring their survival in the face of these challenges.


                                             Table 22. Example response of DeepSeek




                                                                   26
                                          Idiosyncrasies in Large Language Models




What are some effective tactics for building a referral network and gaining new business through word-of-mouth?
Building a referral network and leveraging word-of-mouth marketing can be a powerful way to grow your business. Here are some
effective tactics to help you achieve this:
  1. Deliver Exceptional Service: The foundation of a strong referral network is delivering exceptional service to your existing
     customers. Ensure that you consistently meet or exceed their expectations, and they will be more likely to refer you to others.
  2. Build Relationships: Foster strong relationships with your customers, partners, and colleagues. This can be done through
     regular communication, shared experiences, and mutual support.
  3. Encourage Referrals: Make it easy for your customers to refer you by providing incentives, such as discounts, rewards, or
     exclusive offers. You can also ask for referrals directly, but be sure to do so in a non-intrusive and respectful manner.
  4. Leverage Social Proof: Use customer testimonials, case studies, and reviews to demonstrate your expertise and build
     credibility. This can be done through social media, your website, or other marketing channels.
  5. Host Events and Webinars: Hosting events, webinars, or workshops can help you build relationships with potential
     customers and establish yourself as an expert in your field.
  6. Partner with Other Businesses: Collaborate with complementary businesses to expand your network and reach new
     audiences.
  7. Use Referral Marketing Platforms: Utilize platforms like ReferralCandy, Ambassador, or B2B referral platforms to
     streamline your referral process and track referrals.
  8. Follow Up: Follow up with your referrals and leads to ensure they have a positive experience and to gather feedback.
  9. Be Authentic and Transparent: Be genuine and transparent in your interactions with your network. This will help build
     trust and credibility, making it more likely that people will refer you to others.
 10. Measure and Analyze: Track the effectiveness of your referral efforts and analyze the data to refine your strategy and
     optimize your results.
Additionally, consider the following:
   • Employee Advocacy: Encourage your employees to become brand ambassadors and share their positive experiences with
     their networks.
   • Customer Advocacy: Identify and empower your most loyal customers to become advocates for your business.
   • Content Marketing: Create valuable content that educates and entertains your audience, making them more likely to share it
     with others.
   • Influencer Marketing: Partner with influencers in your industry to expand your reach and credibility.
By implementing these tactics, you can build a strong referral network and leverage word-of-mouth marketing to drive growth and
success for your business.


                                    Table 23. Example response of Llama3.1-8b (instruct).




                                                                27
                                          Idiosyncrasies in Large Language Models




What are some effective tactics for building a referral network and gaining new business through word-of-mouth?
Building a Referral Network & Gaining New Business Through Word-of-Mouth:
1. Deliver Exceptional Service:
   • Exceed expectations: Go above and beyond for every client. Surprise and delight them with unexpected value.
   • Build strong relationships: Get to know your clients personally, understand their needs, and build genuine connections.
   • Be responsive and reliable: Respond promptly to inquiries, meet deadlines, and follow through on promises.
2. Make it Easy to Refer:
   • Create a referral program: Offer incentives for successful referrals, such as discounts, free services, or exclusive perks.
   • Provide referral materials: Make it easy for clients to share your information with others by providing referral cards, social
     media share buttons, and email templates.
   • Streamline the process: Make it simple for clients to refer friends and family with a clear and concise process.
3. Nurture Your Network:
   • Stay in touch: Regularly communicate with your existing clients through email newsletters, social media updates, or
     personalized messages.
   • Attend industry events: Network with other professionals and potential referral partners.
   • Join relevant online communities: Engage in online forums and groups related to your industry.
4. Leverage Social Media:
   • Share valuable content: Provide helpful tips, insights, and resources that your target audience will find valuable.
   • Encourage user-generated content: Ask clients to share their experiences with your business on social media.
   • Run contests and giveaways: Offer incentives for people to share your content and refer their friends.
5. Ask for Referrals:
   • Don’t be afraid to ask: Politely request referrals from satisfied clients.
   • Make it personal: Explain why you value their referrals and how they can help your business grow.
   • Offer specific suggestions: Provide examples of people who might benefit from your services.
6. Track Your Results:
   • Monitor your referral rate: Track the number of referrals you receive and the conversion rate of those referrals.
   • Analyze your data: Identify which tactics are most effective and adjust your strategy accordingly.
   • Celebrate your successes: Recognize and reward your top referrers.
Remember, building a strong referral network takes time and effort. Be patient, consistent, and focus on providing exceptional
value to your clients.


                                    Table 24. Example response of Gemma2-9b (instruct).




                                                               28
                                           Idiosyncrasies in Large Language Models




What are some effective tactics for building a referral network and gaining new business through word-of-mouth?
Building a referral network and leveraging word-of-mouth to gain new business is a powerful strategy. Here are some effective
tactics to consider:
  1. Identify Your Ideal Referral Sources:
          • Determine who your ideal customers are and who they might trust to recommend your services or products. This could
            be current customers, industry influencers, or other businesses in your network.
  2. Create a Referral Program:
          • Develop a clear and attractive referral program that incentivizes both the referrer and the referred. Incentives can range
            from discounts, free services, or even just a simple thank you note.
  3. Educate Your Network:
          • Provide your network with the necessary information to make a referral. This could include testimonials, case studies,
            or a simple one-pager that explains the benefits of your product or service.
  4. Make It Easy to Refer:
          • Provide easy-to-use tools for your network to make referrals. This could be a referral form, a link, or a simple email
            template they can use.
  5. Leverage Social Media:
          • Use social media platforms to connect with potential referrers and to share your referral program. Platforms like
            LinkedIn, Twitter, and Facebook can be particularly effective.
  6. Host Events and Networking Opportunities:
          • Organize events or participate in networking opportunities where you can meet potential referrers in person. Personal
            connections can often lead to more referrals.
  7. Provide Excellent Customer Service:
          • Ensure that your current customers have a positive experience with your product or service. Satisfied customers are
            more likely to refer others.
  8. Follow Up and Show Appreciation:
          • Keep in touch with your network and show appreciation for their referrals. A simple thank you note or a small token of
            appreciation can go a long way.
  9. Use Testimonials and Case Studies:
          • Share positive testimonials and case studies from satisfied customers. This can help build trust and encourage others to
            refer to you.
 10. Be Patient and Persistent:
          • Building a referral network takes time. Be patient and persistent in your efforts. Consistency is key.
 11. Monitor and Analyze:
          • Keep track of your referral program’s performance and analyze the data to see what’s working and what isn’t. Use this
            information to refine your approach.
 12. Offer Referral Bonuses:
          • Consider offering bonuses for repeat referrals or for referring a certain number of new customers. This can help keep
            the momentum going.
By implementing these tactics, you can build a strong referral network and leverage word-of-mouth to grow your business.


                                     Table 25. Example response of Qwen2.5-7b (instruct).




                                                                 29
                                          Idiosyncrasies in Large Language Models




What are some effective tactics for building a referral network and gaining new business through word-of-mouth?

  1. Provide exceptional service: The foundation of a strong referral network is built on delivering outstanding service to your
     current clients. Happy customers are more likely to refer you to others.
  2. Ask for referrals: Don’t be shy about asking satisfied clients for referrals. Make it easy for them by providing referral cards,
     email templates, or a simple script they can use to introduce you to their contacts.
  3. Offer incentives: Consider offering incentives for referrals, such as discounts, freebies, or other rewards. This can motivate
     your clients to refer more people to your business.
  4. Networking: Attend industry events, trade shows, and networking events to meet potential referral sources. Joining
     professional organizations and participating in local business groups can also help you expand your network.
  5. Leverage social media: Use social media platforms to connect with potential clients and engage with your current network.
     Share valuable content, participate in discussions, and don’t forget to ask for referrals on your social media profiles.
  6. Follow up: Follow up with leads promptly and professionally. A quick response can make a positive impression and increase
     the chances of converting a referral into a client.
  7. Build relationships: Focus on building long-term relationships with your clients and referral sources. Regularly touch base
     with them, show appreciation for their referrals, and keep them updated on your business and industry news.
  8. Provide referral training: Teach your clients how to effectively refer you to others. This can include providing them with tips
     on how to introduce you, what information to share, and how to follow up on referrals.
  9. Collaborate with non-competitive businesses: Partner with other non-competitive businesses to cross-refer clients. This can
     help you tap into their network and vice versa.
 10. Ask for testimonials: Positive testimonials can help build trust with potential clients and encourage referrals. Ask satisfied
     clients if they would be willing to provide a testimonial for your website or social media profiles.



                                    Table 26. Example response of Mistral-v3-7b (instruct).




                                                                30
                                          Idiosyncrasies in Large Language Models

Newswise — Sepsis is a serious medical condition caused by an overwhelming immune response to infection. The body’s
infection-fighting chemicals trigger widespread inflammation
, which can lead to blood clots and leaky blood vessels. It damages the tiny capillaries in organs such as lungs, liver, kidney and
brain. According to recent estimates, 1 million people die from sepsis each year. In the United States alone, it affects more than
one million hospital patients annually and accounts for over $20 billion in healthcare costs, making it the most expensive condition
treated in intensive care units (ICUs). A research team led by Dr. Robert W. Day at Washington University School of Medicine
found that a common drug used for treating type 2 diabetes may reduce mortality rates among ICU patients with severe sepsis or
septic shock. The researchers examined data on more than 340,000 adult patients admitted to ICUs across the U.S. between January
2015 and December 2017. Approximately 50% were diagnosed with severe sepsis or septic shock. They discovered that the use of
metformin – the first-line treatment for type 2 diabetes – was associated with a significant reduction in the risk of death within 30
days after admission to the ICU. The benefit was even greater among those who didn’t have pre-existing diabetes. The findings
suggest that metformin could be considered as part of standard practice for all ICU patients with severe sepsis or septic shock.
Metformin has been shown to improve outcomes in animal models of sepsis. According to the researchers, this study provides
further evidence linking metformin use with better survival rates in human subjects experiencing extreme illness.


                                      Table 27. Example response of Llama3.1-8b (base).


Newswise — Sepsis is a serious medical condition caused by an overwhelming immune response to infection. The body’s
infection-fighting chemicals trigger widespread inflammation
, which can lead to organ damage and failure.
While sepsis affects only 1% of the U.S. population each year, it kills more than half a million people globally every year—making
it as dangerous as cancer or malaria. In fact, sepsis accounts for about one in six deaths worldwide each year. It also ranks among
the top five leading causes of death from infectious diseases. When we think of ‘sepsis,’ we often imagine elderly patients with
multiple comorbidities,” said Michael Miller, M.D., chief of the Division of Pulmonary, Critical Care & Sleep Medicine at UT
Southwestern Medical Center and holder of the Dallas Heart Ball Chair in Cardiovascular Disease Research. “But our research has
shown that 40% of people who develop severe sepsis are young adults.


                                       Table 28. Example response of Gemma2-9b (base).


Newswise — Sepsis is a serious medical condition caused by an overwhelming immune response to infection. The body’s
infection-fighting chemicals trigger widespread inflammation,
which can damage healthy organs and blood vessels. Sepsis is treated in the hospital with antibiotics and fluids. If sepsis isn’t
detected early or if treatment doesn’t work, multiple organ failure occurs and may lead to death.


                                       Table 29. Example response of Qwen2.5-7b (base).




                                                                31
                                           Idiosyncrasies in Large Language Models




Newswise — Sepsis is a serious medical condition caused by an overwhelming immune response to infection. The body’s
infection-fighting chemicals
, which are normally good, can cause damage to the blood vessels and organs.
Sepsis is one of the leading causes of death in hospitals. Although there have been recent advances in sepsis treatment, researchers
are still working hard to identify new ways to prevent and treat this complex disease.
Researchers at Washington University School of Medicine in St. Louis recently published a study that may change how sepsis
is diagnosed and treated. Their work suggests that two different types of immune cells are involved in the progression of sepsis:
one cell type that’s protective and another that’s harmful. These findings could help doctors better identify who is most at risk for
severe complications from the disease.
“The results from our study show that there are two distinct populations of monocytes,” said co-author Dr. Michael Jaffe, professor
of medicine at Washington University. “One population promotes inflammation and is associated with worse outcomes; the other
helps resolve inflammation and promotes healing.”
Monocytes are a type of white blood cell that are part of the innate immune system. They play a key role in fighting off bacteria
and viruses. When someone has sepsis, their monocytes become activated. That means they increase in number and start
producing cytokines, which are small proteins that regulate the body’s immune response. Typically, when the body encounters an
infection, these cytokines signal the immune system to fight back. But too many cytokines produced too quickly can result in a
hyperinflammatory state, which can lead to organ failure and death.
In the past, doctors have used blood tests to diagnose sepsis. However, those tests only measure the overall levels of cytokines in a
person’s blood. The new study suggests that it might be possible to determine whether someone has a particular type of monocyte
that could make them more susceptible to sepsis. If so, doctors could potentially use this information to personalize treatments and
improve patient outcomes.
“Our findings suggest that there may be opportunities to develop therapies that target specific monocyte subsets,” said co-author Dr.
Daniel Levy, assistant professor of medicine at Washington University. “This could potentially reduce the risk of developing sepsis
or even improve outcomes once someone already has sepsis.”
There’s still much to learn about how these monocyte subsets contribute to sepsis development and progression, but the results of
this study provide promising insights into why some patients respond differently to treatment than others.


                                      Table 30. Example response of Mistral-v3-7b (base).




                                                                 32

```

## Linked implementation at `e5333d01493963e5af44288fe2b9343ae6f13b9f`

The complete seven-file tracked tree is reproduced below. File boundaries are explicit; bytes are also preserved in the Git archive attachment.

### `.gitignore`

```text
*/
*.sh
```

### `INSTALL.md`

```text
# Installation

Please use two separate environments for response generation and classification. It is possible to merge them into a single environment, but it takes a lot of time to resolve the dependencies.

## Dependency Setup for Response Generation

```
conda create -n gen_resp python=3.9 -y
conda activate gen_resp
pip install vllm==0.6.3.post1 datasets==3.2.0 openai anthropic google-generativeai
```

## Dependency Setup for Evaluation and Classification

```
conda create -n classification python=3.9 -y
conda activate classification
pip install llm2vec==0.2.3 tensorboard
```
```

### `LICENSE`

```text
MIT License

Copyright (c) 2025 CMU Locus Lab

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

### `README.md`

```text
# Idiosyncrasies in Large Language Models
Official code of Idiosyncrasies in Large Language Models

> [**Idiosyncrasies in Large Language Models**](https://arxiv.org/abs/2502.12150) </br>
> *[Mingjie Sun](https://eric-mingjie.github.io)\*, [Yida Yin](https://davidyyd.github.io)\*, [Zhiqiu Xu](https://oscarxzq.github.io), [J. Zico Kolter](https://zicokolter.com), [Zhuang Liu](https://liuzhuang13.github.io)* (* indicates equal contribution) <br>
> Carnegie Mellon University, UC Berkeley, University of Pennsylvania, and Princeton University<br>
>[[Paper]](https://arxiv.org/abs/2502.12150) [[Project page]](https://eric-mingjie.github.io/llm-idiosyncrasies/index.html)

```bibtex
@article{sun2025idiosyncrasies,
    title    = {Idiosyncrasies in Large Language Models},
    author   = {Sun, Mingjie and Yin, Yida and Xu, Zhiqiu and Kolter, J. Zico and Liu, Zhuang},
    year     = {2025},
    journal  = {arXiv preprint arXiv:2502.12150}
}
```

---
<p align="center">
<img src="https://github.com/user-attachments/assets/de7a87f0-8a4e-43d4-bfd1-4778d0393274" width=100% height=100%
class="center">

</p>
We study idiosyncrasies in Large Language Models (LLMs) -- unique patterns in their outputs. We consider a simple classification task: given a particular text output, a neural network is trained to predict the source LLM that generates that text.


## Results and Pre-trained Models

We provide four [LLM2vec](https://arxiv.org/abs/2404.05961) classifiers, each trained on responses generated by a specific LLM group using prompts from the UltraChat dataset. The LLM groups are:
 - chat APIs: ChatGPT, Claude, Grok, Gemini, and DeepSeek
 - instruct LLMs: Llama3.1-8b-it, Gemma2-9b-it, Qwen2.5-7b-it, and Mistral-v3-7b-it
 - base LLMs: Llama3.1-8b, Gemma2-9b, Qwen2.5-7b, and Mistral-v3-7b
 - ten models: five chat APIs + Phi-4 + four instruct LLMs

| name | accuracy | model |
|:---:|:---:|:---:|
| chat APIs classifier | 97.1 | [model](https://huggingface.co/Yida/classifier_chat) |
| instruct LLMs classifier | 95.9 | [model](https://huggingface.co/Yida/classifier_instruct) |
| base LLMs classifier | 87.6 | [model](https://huggingface.co/Yida/classifier_base) |
| ten models classifier | 91.9 | [model](https://huggingface.co/Yida/classifier_ten_models) |


## Pre-generated Responses
We host a collection of pre-generated responses using prompts from UltraChat dataset for Chat APIs, Instruct LLMs, and Base LLMs.

| | ChatGPT | Claude | Grok | Gemini | DeepSeek | Phi-4 |
| :-- | :--: | :--: | :--: | :--: | :--: | :--: |
| links | [download](https://drive.google.com/file/d/1O1dEROw21KePNMF9ewlkXkkzL8Z-5qrN/view?usp=sharing) | [download](https://drive.google.com/file/d/1sifL_hsFiSDKZgnEeahiT20wPW8NDmRG/view?usp=sharing) | [download](https://drive.google.com/file/d/1yUA-8RYYXIkSV2xMbUCqTU8o6F6LrEFg/view?usp=share_link) | [download](https://drive.google.com/file/d/1dsvpXmLCNa4Gehd9jmantMNSDiw2eS4f/view?usp=share_link) | [download](https://drive.google.com/file/d/1a31HZgMwppwXjzEiY1fj3VfhAco5RWhG/view?usp=share_link) | [download](https://drive.google.com/file/d/1C6xDdvOuczJq1j4OSXJgqxB75kvwSoVK/view?usp=share_link) |

| | Llama3.1-8b-it | Gemma2-9b-it | Qwen2.5-7b-it | Mistral-7b-v3-it |
| :-- | :--: | :--: | :--: | :--: |
| links |[download](https://drive.google.com/file/d/1JuT1UpCw6ijDIgYSa2JM1AmDcSTxrTLu/view?usp=sharing) | [download](https://drive.google.com/file/d/1gw_z-XsUHSip71qkHdoM4SnpflwcM_g_/view?usp=sharing) | [download](https://drive.google.com/file/d/1EnVOL4WhxU3-hFvPOEZ21moOeEyX5eSb/view?usp=sharing) | [download](https://drive.google.com/file/d/1uIRtNvapwfmOWBhlknOP8rRvdExn5wNW/view?usp=sharing) |

| | Llama3.1-8b | Gemma2-9b | Qwen2.5-7b | Mistral-7b-v3 |
| :-- | :--: | :--: | :--: | :--: |
| links |[download](https://drive.google.com/file/d/1b37J7btQ1jFhs0bwfUPpXRzxp5Yxm_eS/view?usp=sharing) | [download](https://drive.google.com/file/d/1o3TTBxOBaytFKyGf6D7T5b8iCH-0kwLu/view?usp=share_link) | [download](https://drive.google.com/file/d/1py9tJBpZaZPh0ryvMBS08SlB-LWjWdOh/view?usp=share_link) | [download](https://drive.google.com/file/d/1S1nAojlpMrl9LKkYYA6EBDS2cfLzVk1W/view?usp=share_link) |

## Setup
Installation instructions can be found in [INSTALL.md](INSTALL.md).

## Evaluation
We give an example evaluation command for the chat APIs classifier. Other classifiers can be evaluated in a similar way.

To download the classifier, you can use huggingface CLI:
```bash
huggingface-cli download Yida/classifier_chat --local-dir /path/to/classifier_chat
```

Then, you can evaluate the classifier on the test set.

```bash
python classification.py \
    --response_paths /path/to/ChatGPT.json /path/to/Claude.json /path/to/Grok.json /path/to/Gemini.json /path/to/DeepSeek.json \
    --classifier llm2vec --num_labels 5 \
    --eval_only --resume_from_checkpoint /path/to/classifier_chat \
    --output_dir /path/to/output_dir
```

## Response Generation

### Chat APIs
We call official APIs to generate responses for Chat APIs.

Below is an example command to generate 11K responses for ``ChatGPT`` on ``UltraChat`` dataset.

- Change the ``--model`` argument to generate responses for different Chat API models, including ``ChatGPT``, ``Claude``, ``Grok``, ``Gemini``, and ``DeepSeek``.
```bash
python generate_responses.py \
    --model ChatGPT --api_key $api_key \
    --dataset UltraChat --num_samples 11_000 \
    --output_path /path/to/output.json
```

### Instruct and Base LLMs
We use [vLLM](https://github.com/vllm-project/vllm) to generate responses for instruct / base LLMs in our paper.

Below is an example command to generate 11K responses for ``Llama3.1-8b-it`` on ``UltraChat`` dataset with greedy decoding.

- ``--model`` argument controls the LLM used to generate responses. Our code currently supports generating responses for nine LLMs in our paper, including ``Llama3.1-8b-it``, ``Gemma2-9b-it``, ``Qwen2.5-7b-it``, ``Mistral-7b-v3-it``, ``Phi-4``, ``Llama3.1-8b``, ``Gemma2-9b``, ``Qwen2.5-7b``, and ``Mistral-7b-v3``. We recommend using temperature ``0.6`` and repetition penalty ``1.1`` for base LLMs.
- ``--dataset`` argument specifies the prompt dataset to generate responses on, including ``UltraChat``, ``Cosmopedia``, ``LmsysChat``, ``WildChat``, and ``FineWeb``.
- It is also possible to use multiple GPUs to generate responses. Simply change the ``--num_gpus`` argument. This is implemented through tensor parallelism by vLLM.

```bash
python generate_responses.py \
    --model Llama3.1-8b-it --temperature 0 \
    --dataset UltraChat --num_samples 11_000 \
    --output_path /path/to/output.json
```

## Transformations
Below we provide scripts to perform various transformations on the generated responses. The supported transformations are ``remove_special_characters``, ``shuffle_word``, ``shuffle_letter``, ``markdown_elements_only``, ``paraphrase``, ``translate``, and ``summarize``.

Here is the example command to shuffle words from the generated responses.

```bash
python transform.py \
    --input_path /path/to/input.json \
    --output_path /path/to/output.json \
    --transform_mode shuffle_word
```

To rewrite (e.g., paraphrase, translate, summarize) the generated responses, you also need to provide the API key for the rewriting model (e.g., GPT-4o-mini) through the ``--api_key`` argument.

```bash
python transform.py \
    --input_path /path/to/input.json \
    --output_path /path/to/output.json \
    --transform_mode paraphrase \
    --api_key $api_key
```

## Classification
Below is an example command to classify responses from two different models. For $N$-way classification, you can change the ``--response_paths`` argument to include $N$ response paths (with white space separated).

You can change the ``--classifier`` argument to use different classifiers. Our code currently supports the following classifiers: ``llm2vec``, ``gpt2``, ``t5``, and ``bert``. Each classifier can be run on a single GPU (supported bfloat16) with 24 GB memory.
```bash
python classification.py \
    --response_paths /path/to/model1.json /path/to/model2.json \
    --classifier llm2vec --num_labels $num_labels \
    --output_dir /path/to/output_dir
```


## License
This project is released under the MIT license. Please see the [LICENSE](LICENSE) file for more information.

## Questions
Feel free to discuss papers/code with us through issues/emails!

mingjies at cs.cmu.edu
davidyinyida0609 at berkeley.edu
```

### `classification.py`

```text
import argparse
import evaluate
import json
import numpy as np
import random
import os
import torch
from datasets import Dataset, DatasetDict, concatenate_datasets
from llm2vec import LLM2Vec
from peft import PeftModel
from transformers import (
    AutoConfig,
    AutoModel,
    AutoModelForSequenceClassification,
    AutoTokenizer,
    Trainer,
    TrainingArguments,
)

class LLM2VecCollator:
    def __init__(self, model):
        self.model = model

    def __call__(self, batch):
        num_texts = len(batch)
        texts = []
        labels = []
        for example in batch:
            text = self.model.prepare_for_tokenization(example["text"])
            texts.append(text)
            labels.append(example["target"])

        labels = torch.tensor(labels)
        inputs = self.model.tokenize(texts)
        inputs["labels"] = labels
        return inputs

class SequenceClassificationCollator:
    def __init__(self, tokenizer):
        self.tokenizer = tokenizer

    def __call__(self, batch):
        num_texts = len(batch)
        texts = []
        labels = []
        for example in batch:
            texts.append(example["text"])
            labels.append(example["target"])

        labels = torch.tensor(labels)
        inputs = self.tokenizer(texts, truncation=True, padding="max_length", max_length=512, return_tensors="pt")
        inputs["labels"] = labels
        return inputs

def load_dataset(args):
    all_responses = [list() for _ in range(len(args.response_paths))]
    for label, response_path in enumerate(args.response_paths):
        with open(response_path, "r") as f:
            data = json.load(f)

        for i in range(len(data)):
            response = data[i][-1]["content"]
            all_responses[label].append({"text": response, "target": label})

    all_train_datasets = []
    all_test_datasets = []
    for label in range(len(args.response_paths)):
        dataset = Dataset.from_list([each for each in all_responses[label]])
        # the seed ensures that the train and test splits are the same for each label
        dataset = dataset.train_test_split(train_size=args.num_train_samples, test_size=args.num_test_samples, seed=42)
        all_train_datasets.append(dataset['train'])
        all_test_datasets.append(dataset['test'])
    combined_train_dataset = concatenate_datasets(all_train_datasets)
    combined_train_dataset = combined_train_dataset.shuffle(seed=42)
    combined_test_dataset = concatenate_datasets(all_test_datasets)
    combined_test_dataset = combined_test_dataset.shuffle(seed=42)

    dataset = DatasetDict({
        'train': combined_train_dataset,
        'test': combined_test_dataset
    })

    print("Number of training samples", len(dataset['train']))
    print("Number of testing samples", len(dataset['test']))
    return dataset

def load_model(args):
    classifier_to_hf_name = {
        "bert": "bert-base-uncased",
        "t5": "google-t5/t5-base",
        "gpt2": "openai-community/gpt2",
        "llm2vec": "McGill-NLP/LLM2Vec-Meta-Llama-3-8B-Instruct-mntp",
    }

    tokenizer = AutoTokenizer.from_pretrained(classifier_to_hf_name[args.classifier], trust_remote_code=True)

    if args.classifier == "llm2vec":
        config = AutoConfig.from_pretrained(
            classifier_to_hf_name[args.classifier],
            trust_remote_code=True,
        )
        model = AutoModel.from_pretrained(
            classifier_to_hf_name[args.classifier],
            config=config,
            torch_dtype=torch.bfloat16,
            device_map="cuda",
            trust_remote_code=True,
        )

        model = PeftModel.from_pretrained(
            model,
            classifier_to_hf_name[args.classifier],
            torch_dtype=torch.bfloat16,
            device_map="cuda",
            trust_remote_code=True,
        )
        model = model.merge_and_unload()

        model = PeftModel.from_pretrained(
            model,
            f"{classifier_to_hf_name[args.classifier]}-supervised",
            is_trainable=True,
            torch_dtype=torch.bfloat16,
            device_map="cuda",
            trust_remote_code=True,
        )

        # check the trainable parameters
        model.print_trainable_parameters()
        model = LLM2Vec(model, tokenizer, pooling_mode="mean", max_length=512)

        hidden_size = list(model.modules())[-1].weight.shape[0]
        model.head = torch.nn.Linear(hidden_size, args.num_labels, dtype=torch.bfloat16)

        old_forward = model.forward
        # hacky way to turn LLM2Vec into a sequence classification model compatible with the HF Trainer
        def forward(**kwargs):
            if "labels" in kwargs:
                kwargs.pop("labels")
            return {"logits": model.head(old_forward(kwargs).to(torch.bfloat16))}
        model.forward = forward
    else:
        # use the sequence classification model from huggingface
        model = AutoModelForSequenceClassification.from_pretrained(
            classifier_to_hf_name[args.classifier],
            num_labels=args.num_labels,
            torch_dtype=torch.bfloat16,
            device_map="cuda",
            trust_remote_code=True
        )

        # check the trainable parameters
        num_trainable_params = sum(p.numel() for p in model.parameters() if p.requires_grad)

        # add a comma between every three digits
        print(f"trainable params: {'{:,}'.format(num_trainable_params)} || all params: {'{:,}'.format(model.num_parameters())} || trainable%: {num_trainable_params / model.num_parameters():.4f}")
        if args.classifier == "bert":
            tokenizer.add_special_tokens({"pad_token": "[PAD]"})
        elif args.classifier == "gpt2":
            tokenizer.pad_token_id = tokenizer.eos_token_id
            tokenizer.pad_token = tokenizer.eos_token
        elif args.classifier == "t5":
            # t5 has defined its padding token id
            # https://huggingface.co/docs/transformers/model_doc/t5#transformers.T5Tokenizer
            pass

    model.config.pad_token_id = model.config.eos_token_id

    return model, tokenizer

def classification(args):
    # load dataset
    dataset = load_dataset(args)

    # load model
    model, tokenizer = load_model(args)

    # createdata collator
    if args.classifier == "llm2vec":
        data_collator = LLM2VecCollator(model)
    else:
        data_collator = SequenceClassificationCollator(tokenizer)

    if len(args.response_paths) != args.num_labels:
        if args.eval_only:
            print("Warning: the number of response paths is not equal to the number of labels during training. This is ok if you are evaluating on your own dataset.")
        else:
            if args.num_labels is None:
                args.num_labels = len(args.response_paths)
            else:
                raise ValueError("the number of response paths must be equal to the number of labels during training")

    # compute loss
    class SequenceClassificationTrainer(Trainer):
        def compute_loss(self, model, inputs, return_outputs=False, **kwargs):
            labels = inputs.pop("labels")
            outputs = model.forward(**inputs)
            logits = outputs.get("logits")
            loss_fct = torch.nn.CrossEntropyLoss()
            loss = loss_fct(logits.view(-1, args.num_labels), labels.view(-1))
            return (loss, outputs) if return_outputs else loss

        def save_model(self, output_dir, _internal_call=False):
            super().save_model(output_dir)
            os.makedirs(output_dir, exist_ok=True)
            if args.classifier == "llm2vec":
                torch.save(self.model.head.state_dict(), os.path.join(output_dir, "head.pt"))

        def _load_from_checkpoint(self, checkpoint, model=None):
            super()._load_from_checkpoint(checkpoint, model=model)
            if args.classifier == "llm2vec":
                self.model.head.load_state_dict(torch.load(os.path.join(checkpoint, "head.pt")))

    def compute_metrics(eval_pred):
        logits, labels = eval_pred
        predictions = np.argmax(logits, axis=-1)
        accuracy_metric = evaluate.load("accuracy")
        accuracy = accuracy_metric.compute(predictions=predictions, references=labels)["accuracy"]
        return {"accuracy": accuracy}

    if args.eval_only:
        print("Evaluating the model...")
        training_args = TrainingArguments(
            output_dir = args.output_dir,
            do_train = False,
            do_eval = True,
            per_device_eval_batch_size = args.batch_size,
            remove_unused_columns = False,
            label_names = ["labels"],
        )

        trainer = SequenceClassificationTrainer(
            model = model,
            args = training_args,
            train_dataset = dataset['train'],
            eval_dataset = dataset["test"],
            data_collator = data_collator,
            compute_metrics = compute_metrics,
        )

        trainer._load_from_checkpoint(args.resume_from_checkpoint)
        eval_result = trainer.evaluate(ignore_keys=["past_key_values", "encoder_last_hidden_state"] if args.classifier == "t5" else None)
        print(eval_result)
        return

    # training arguments
    training_args = TrainingArguments(
        output_dir = args.output_dir,
        learning_rate = args.lr,
        lr_scheduler_type = "cosine",
        warmup_ratio = args.warmup_ratio,
        max_grad_norm = args.gradient_clipping,
        per_device_train_batch_size = args.batch_size,
        per_device_eval_batch_size = args.batch_size,
        num_train_epochs = args.epochs,
        weight_decay = args.weight_decay,
        eval_strategy = "epoch",
        report_to = "tensorboard",
        save_strategy = "epoch",
        save_total_limit = 1,
        remove_unused_columns = False,
        bf16 = True,
        gradient_checkpointing = True,
        label_names = ["labels"],
    )

    trainer = SequenceClassificationTrainer(
        model = model,
        args = training_args,
        train_dataset = dataset['train'],
        eval_dataset = dataset["test"],
        data_collator = data_collator,
        compute_metrics = compute_metrics,
    )

    trainer.train(
        resume_from_checkpoint=args.resume_from_checkpoint,
        ignore_keys_for_eval=["past_key_values", "encoder_last_hidden_state"] if args.classifier == "t5" else None)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    # miscelaneous
    parser.add_argument('--seed',type=int, default=42, help="the seed that controls the randomness")
    parser.add_argument('--device', type=str, default='cuda', help="the device to use for training / evaluation")

    # data
    parser.add_argument("--response_paths", nargs='+', help="a list of paths to load the generated responses from")
    parser.add_argument("--num_train_samples", type=int, default=10_000, help="the number of training samples")
    parser.add_argument("--num_test_samples", type=int, default=1_000, help="the number of testing samples")

    # classifer
    parser.add_argument('--classifier', type=str, default="llm2vec",
                        choices=["llm2vec", "bert", "t5", "gpt2"],
                        help='the text embedding model to perform sequence classification')
    parser.add_argument('--num_labels', type=int, default=None, help="the number of labels")

    # training hyperparameters
    parser.add_argument("--epochs", type=int, default=3, help="the number of epochs")
    parser.add_argument("--batch_size", type=int, default=8, help="the batch size")
    parser.add_argument('--lr', default=5e-5, type=float, help="the learning rate")
    parser.add_argument("--gradient_clipping", type=float, default=0.3, help="the gradient clipping")
    parser.add_argument("--weight_decay", type=float, default=0.001, help="the weight decay")
    parser.add_argument("--warmup_ratio", type=float, default=0.1, help="the number of warmup steps")

    # evaluation
    parser.add_argument("--eval_only", action="store_true", default=False, help="only evaluate the model")
    parser.add_argument('--resume_from_checkpoint', type=str, default=None, help="the checkpoint to evaluate")

    # output related
    parser.add_argument("--output_dir", type=str, default=None, help="the directory to save the output")
    args = parser.parse_args()
    print(args)

    random.seed(args.seed)
    np.random.seed(args.seed)
    torch.manual_seed(args.seed)
    classification(args)
```

### `generate_responses.py`

```text
import argparse
from anthropic import Anthropic
from datasets import load_dataset
import google.generativeai as genai
import json
import numpy as np
from openai import OpenAI
import os
from tqdm import tqdm
import random
import torch
from vllm import LLM, SamplingParams

def load_vllm_model(args):
    model_name_to_hf_name = {
        "Phi-4": "microsoft/phi-4",
        "Llama3.1-8b-it": "meta-llama/Meta-Llama-3.1-8B-Instruct",
        "Gemma2-9b-it": "google/gemma-2-9b-it",
        "Qwen2.5-7b-it": "Qwen/Qwen2.5-7B-Instruct",
        "Mistral-7b-v3-it": "mistralai/Mistral-7B-Instruct-v0.3",
        "Llama3.1-8b": "meta-llama/Meta-Llama-3.1-8B",
        "Gemma2-9b": "google/gemma-2-9b",
        "Qwen2.5-7b": "Qwen/Qwen2.5-7B",
        "Mistral-7b-v3": "mistralai/Mistral-7B-v0.3",
    }

    model = LLM(model_name_to_hf_name[args.model], tensor_parallel_size=args.num_gpus, trust_remote_code=True)
    tokenizer = model.get_tokenizer()

    return model, tokenizer

def create_dataset(args):
    if args.dataset == "UltraChat":
        dataset = load_dataset("HuggingFaceH4/ultrachat_200k", trust_remote_code=True)["train_sft"]
        get_prompt = lambda x: x["prompt"]
    elif args.dataset == "Cosmopedia":
        dataset = load_dataset("HuggingFaceTB/cosmopedia-100k", trust_remote_code=True)["train"]
        get_prompt = lambda x: x["prompt"]
    elif args.dataset == "LmsysChat":
        dataset = load_dataset("lmsys/lmsys-chat-1m", trust_remote_code=True)["train"]
        get_prompt = lambda x: x["conversation"][0]["content"]
    elif args.dataset == "WildChat":
        dataset = load_dataset("allenai/WildChat", trust_remote_code=True)["train"]
        get_prompt = lambda x: x["conversation"][0]["content"]
    elif args.dataset == "FineWeb":
        dataset = load_dataset("HuggingFaceFW/fineweb", name="sample-10BT", split="train", trust_remote_code=True)
        get_prompt = lambda x: x["text"]
    return dataset, get_prompt

def load_chat_api_model(args):
    if args.model == "ChatGPT":
        client = OpenAI(api_key=args.api_key)
        api_call = lambda x: client.chat.completions.create(
            model="gpt-4o-2024-08-06",
            messages=[{"role": "user", "content": x}],
            max_tokens=args.max_tokens,
        ).choices[0].message.content
    elif args.model == "Claude":
        client = Anthropic(api_key=args.api_key)
        api_call = lambda x: client.messages.create(
            model="claude-3-5-sonnet-20241022",
            messages=[{"role": "user", "content": x}],
            max_tokens=args.max_tokens,
        ).content[0].text
    elif args.model == "Grok":
        client = OpenAI(
            api_key=args.api_key,
            base_url="https://api.x.ai/v1",
        )
        api_call = lambda x: client.chat.completions.create(
            model="grok-beta",
            messages=[{"role": "user", "content": x}],
            max_tokens=args.max_tokens,
        ).choices[0].message.content
    elif args.model == "Gemini":
        genai.configure(api_key=args.api_key)
        model = genai.GenerativeModel("gemini-1.5-pro-002")
        api_call = lambda x: model.generate_content(x, generation_config={"max_output_tokens": args.max_tokens}).text
    elif args.model == "DeepSeek":
        client = OpenAI(
            api_key=args.api_key,
            base_url="https://api.deepseek.com"
        )
        api_call = lambda x: client.chat.completions.create(
            model="deepseek-chat",
            messages=[{"role": "user", "content": x}],
            max_tokens=args.max_tokens,
        ).choices[0].message.content
    return api_call

def generate_responses_chat_api(args):
    # form api call function
    api_call = load_chat_api_model(args)

    # load dataset
    dataset, get_prompt = create_dataset(args)

    # generate responses
    data = []
    random_indices = random.sample(range(len(dataset)), args.num_samples)
    for i in tqdm(random_indices, "Generating responses"):
        prompt = get_prompt(dataset[i])
        response = api_call(prompt)
        data.append([{"role": "user", "content": prompt}, {"role": "assistant", "content": response}])

        # save data per generation
        with open(args.output_path, "w") as file:
            json.dump(data, file)

def generate_responses_instruct_llm(args):
    # load model
    model, tokenizer = load_vllm_model(args)

    # load dataset
    dataset, get_prompt = create_dataset(args)

    random_indices = random.sample(range(len(dataset)), args.num_samples)
    all_prompts = []
    data = []
    for i in random_indices:
        prompt = get_prompt(dataset[i])
        data.append([{"role": "user", "content": prompt}])

        formatted_prompt = tokenizer.apply_chat_template([{"role": "user", "content": prompt}], tokenize=False, add_generation_prompt=True)
        all_prompts.append(formatted_prompt)

    outputs = model.generate(
        all_prompts,
        SamplingParams(
            temperature=args.temperature,
            max_tokens=1024,
        )
    )

    for i in range(args.num_samples):
        response = outputs[i].outputs[0].text
        # remove some artifacts
        if "mistral" in args.model:
            response = response.strip()
        elif "gemma" in args.model:
            response = response.rstrip('\n')
        data[i].append({"role": "assistant", "content": response})

    with open(args.output_path, "w") as file:
        json.dump(data, file)

def generate_responses_base_llm(args):
    model, tokenizer = load_vllm_model(args)

    dataset, get_prompt = create_dataset(args)

    random_indices = random.sample(range(len(dataset)), args.num_samples)
    data = []
    all_prompts = []
    for i in random_indices:
        prompt = get_prompt(dataset[i])
        tokens = tokenizer.encode(prompt, padding=False)[:32]
        truncated_prompt = tokenizer.decode(tokens, skip_special_tokens=True)

        all_prompts.append(truncated_prompt)
        data.append([{"role": "user", "content": truncated_prompt}])

    outputs = model.generate(
        all_prompts,
        SamplingParams(
            temperature=args.temperature,
            repetition_penalty=args.repetition_penalty,
            max_tokens=1024,
        )
    )

    for i in range(args.num_samples):
        data[i].append({"role": "assistant", "content": outputs[i].outputs[0].text})

    with open(args.output_path, "w") as file:
        json.dump(data, file)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    # miscelaneous
    parser.add_argument("--seed", type=int, default=42, help="the seed that controls the randomness")
    parser.add_argument("--device", type=str, default="cuda", help="the device to use for generation")
    parser.add_argument("--num_gpus", type=int, default=1, help="the number of gpus to use for generation")
    parser.add_argument("--api_key", type=str, default=None, help="the api key to use for generation")

    # data
    parser.add_argument("--dataset", type=str, default="UltraChat",
                        choices=["UltraChat", "Cosmopedia", "LmsysChat", "WildChat", "FineWeb"],
                        help="the dataset to generate responses from")
    parser.add_argument("--model", type=str, default=None,
                        choices=["ChatGPT", "Claude", "Grok", "Gemini", "DeepSeek",
                                 "Llama3.1-8b-it", "Gemma2-9b-it", "Qwen2.5-7b-it", "Mistral-7b-v3-it", "Phi-4",
                                 "Llama3.1-8b", "Gemma2-9b", "Qwen2.5-7b", "Mistral-7b-v3"],
                        help="the model to generate responses from")
    parser.add_argument("--num_samples", type=int, default=11_000, help="the number of samples to generate")
    parser.add_argument("--output_path", type=str, default=None, help="the path to save the output")

    # sampling hyperparameters
    parser.add_argument("--temperature", type=float, default=0, help="the temperature of the sampling")
    parser.add_argument("--repetition_penalty", type=float, default=1.1, help="the repetition penalty of the sampling")
    parser.add_argument("--max_tokens", type=int, default=1024, help="the maximum number of tokens to generate")

    args = parser.parse_args()
    print(args)

    random.seed(args.seed)
    np.random.seed(args.seed)
    torch.manual_seed(args.seed)
    os.makedirs(os.path.dirname(args.output_path), exist_ok=True)

    if args.model in ["ChatGPT", "Claude", "Grok", "Gemini", "DeepSeek"]:
        generate_responses_chat_api(args)
    elif args.model in ["Llama3.1-8b-it", "Gemma2-9b-it", "Qwen2.5-7b-it", "Mistral-7b-v3-it", "Phi-4"]:
        generate_responses_instruct_llm(args)
    else:
        assert args.dataset == "FineWeb"
        generate_responses_base_llm(args)

```

### `transform.py`

```text
import random
import argparse
import json
import os
import re
from tqdm import tqdm
from openai import OpenAI

def _remove_special_characters(text):
    # remove enumeration
    text = re.sub(r'\d+\.', '', text)

    # remove all special characters
    text = re.sub(r'[^a-zA-Z0-9\s]', '', text)

    # replace indentation with a single space
    text = re.sub(r'\s+', ' ', text)

    return text

def remove_text(text):
    lines = text.split('\n')

    output_lines = []
    in_code_block = False

    # detect triple-backtick code blocks (including optional language).
    code_block_regex = re.compile(r'^\s*```')

    # detect headings (e.g. "#", "##", etc.) or bullet/numbered list items.
    heading_or_list_regex = re.compile(r'^(\s{0,3}(?:[#]+|(?:\d+\.)|[-*+]))(\s*)(.*)')

    for line in lines:
        # check for entering/exiting a triple-backtick code block
        if code_block_regex.search(line):
            # toggle code block state
            if not in_code_block:
                # enter a code block
                output_lines.append(line)  # Keep the backtick line as is
                in_code_block = True
            else:
                # exit a code block
                output_lines.append(line)  # Keep the backtick line as is
                in_code_block = False

            continue

        if in_code_block:
            # inside code blocks, replace all non-empty lines with 'xxx' but preserve indentation.
            if line.strip() == "":
                # blank line in code block, keep it
                output_lines.append(line)
            else:
                # non-empty line => replace with 'xxx' (preserve leading indentation)
                leading_spaces = len(line) - len(line.lstrip())
                output_lines.append(' ' * leading_spaces + 'xxx')
            continue
        else:
            # normal line (outside code blocks).

            # 1) detect heading or list marker
            match = heading_or_list_regex.match(line)
            if match:
                marker_part = match.group(1)  # e.g. "#", "1.", "-", "*"
                spacing_part = match.group(2) # e.g. " " or multiple spaces
                rest_part = match.group(3)    # the rest of the line

                # replace the rest_part with a version that has inline markdown replaced by 'xxx'
                replaced_rest = replace_inlines_with_xxx(rest_part)

                # then replace any plain text left outside inline markers with 'xxx'
                output_lines.append(f"{marker_part}{spacing_part}{replaced_rest}")
            else:
                # no heading/list marker, so just replace inlines with 'xxx'
                replaced_line = replace_inlines_with_xxx(line)
                output_lines.append(replaced_line)

    # re-join the transformed lines
    output_lines = [line for line in output_lines if line != ""]
    # merge consecutive xxx into a single xxx
    tmp = []
    i = 0
    while i < len(output_lines):
        j = i
        while j < len(output_lines) and (output_lines[j] == "xxx" or output_lines[j] == ""):
            j += 1
        if j - i > 1:
            tmp.append("xxx")
            i = j
        else:
            tmp.append(output_lines[i])
            i += 1
    return "\n".join(tmp)


def replace_inlines_with_xxx(line):
    i = 0
    length = len(line)
    result = []

    # stack to keep track of which marker we are "inside" currently.
    marker_stack = []

    # helper to see if the substring at i starts with a marker
    # handle '**', '*', '`', etc.
    def check_marker(s, pos):
        # return (marker_str, marker_length) or (None, 0)
        if s.startswith('```', pos):  # triple backtick inline is rare but let's skip
            return ('```', 3)
        if s.startswith('**', pos):
            return ('**', 2)
        if s.startswith('*', pos):
            return ('*', 1)
        if s.startswith('`', pos):
            return ('`', 1)
        return (None, 0)

    # keep track of "plain text" segments outside any markers and replace them with 'xxx'
    plain_text_buffer = []

    def flush_plain_text():
        if plain_text_buffer:
            # check if there's any non-whitespace in the buffer
            buf_content = "".join(plain_text_buffer)
            if buf_content.strip() == "":
                # purely whitespace => keep as is
                result.append(buf_content)
            else:
                # there's some text => replace entire buffer with "xxx"
                result.append("xxx")
            plain_text_buffer.clear()

    while i < length:
        marker, m_len = check_marker(line, i)
        if marker:
            # found an inline marker and  flush any plain text
            flush_plain_text()

            # check a nested marker or open a new one
            if marker_stack and marker_stack[-1] == marker:
                # it's a closing of the current marker
                # output the marker as-is
                result.append(marker)
                marker_stack.pop()
            else:
                # open a new marker
                result.append(marker)
                marker_stack.append(marker)

            i += m_len
        else:
            # not a marker => gather it as plain text
            plain_text_buffer.append(line[i])
            i += 1

    # end of line => flush any remaining text
    flush_plain_text()

    return "".join(result)

def remove_special_characters(args):
    with open(args.input_path, "r") as f:
        data = json.load(f)

    for i in tqdm(range(len(data))):
        response = data[i][-1]["content"]
        data[i][-1]["content"] = _remove_special_characters(response)

    with open(args.output_path, "w") as f:
        json.dump(data, f)

def shuffle(args):
    if "letter" in args.transform_mode:
        shuffle_func = lambda x: ''.join(random.sample(x.replace(" ", ""), len(x.replace(" ", ""))))
    elif "word" in args.transform_mode:
        shuffle_func = lambda x: ' '.join(random.sample(x.split(), len(x.split())))

    with open(args.input_path, "r") as f:
        data = json.load(f)

    for i in tqdm(range(len(data))):
        response = data[i][-1]["content"]
        data[i][-1]["content"] = shuffle_func(_remove_special_characters(response))

    with open(args.output_path, "w") as f:
        json.dump(data, f)

def markdown_elements_only(args):
    with open(args.input_path, "r") as f:
        data = json.load(f)

    for i in tqdm(range(len(data))):
        response = data[i][-1]["content"]
        data[i][-1]["content"] = remove_text(response)

    with open(args.output_path, "w") as f:
        json.dump(data, f)

def paraphrase(args):
    if args.transform_mode == "paraphrase":
        template = "\"{msg}\"\n\nParaphrase the above text while maintaining the semantic meaning of the original text."
    elif args.transform_mode == "translate":
        template = "\"{msg}\"\n\nTranslate the above text into Chinese."
    elif args.transform_mode == "summarize":
        template = "\"{msg}\"\n\nSummarize the above text in one paragraph."

    client = OpenAI(api_key=args.api_key)
    with open(args.input_path, "r") as f:
        data = json.load(f)

    for i in tqdm(range(len(data))):
        response = data[i][-1]["content"]
        prompt = template.format(msg=response)

        completion = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=1024,
        )
        data[i][-1]["content"] = completion.choices[0].message.content

        # save the transformed responses per generated response
        with open(args.output_path, "w") as f:
            json.dump(data, f)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input_path", type=str, default=None, help="a json path that stores the generated responses from an LLM")
    parser.add_argument("--output_path", type=str, default=None, help="a json path that stores the transformed responses")
    parser.add_argument("--transform_mode", type=str, default=None,
                        choices=["remove_special_characters", "shuffle_word",
                                 "shuffle_letter", "markdown_elements_only",
                                 "paraphrase", "translate", "summarize"],
                        help="the transformation mode to apply to the responses")
    parser.add_argument("--api_key", type=str, default=None, help="the API key for the rewriting model (e.g. GPT-4o-mini)")
    args = parser.parse_args()

    random.seed(42)
    os.makedirs(os.path.dirname(args.output_path), exist_ok=True)
    if args.transform_mode == "remove_special_characters":
        remove_special_characters(args)
    elif args.transform_mode in ["shuffle_word", "shuffle_letter"]:
        shuffle(args)
    elif args.transform_mode == "markdown_elements_only":
        markdown_elements_only(args)
    elif args.transform_mode in ["paraphrase", "translate", "summarize"]:
        paraphrase(args)

```
## Extraction verification

- **Beginning checked:** arXiv v2 PDF page 1 was rendered and compared with the extraction; title, five authors, abstract, affiliations, publication line, and opening Introduction text agree.
- **Middle checked:** arXiv v2 PDF page 16 was rendered and compared with the extraction; Appendix B.2-B.3 headings, Figures 13-15, labels, characteristic-phrase discussion, footnote 2, and page number agree.
- **End checked:** arXiv v2 PDF page 32 was rendered and compared with the extraction; the complete Mistral-v3-7b base response, Table 30 caption, and final page number agree.
- **Structure checked:** pdfinfo reports 32 pages. The extraction contains the abstract; Sections 1-6; Acknowledgments; Impact Statement; complete References; Appendices A-C; Tables 1-30; Figures 1-18; implementation, prompt, additional-result, and response-demonstration material. The arXiv HTML contents list was checked from Introduction through Appendix C. The linked repository tree has seven tracked files totaling 973 lines; every file was read and preserved at the reviewed commit.
- **Known omissions:** none from the reviewed paper or linked implementation commit. PDF layout, chart color, and underlining are not fully represented in the plain-text extraction, but the preserved PDFs retain them. No paper-time software tag exists, so the 2025-07-21 commit is not asserted to be the exact code state used for the paper results. Linked response datasets, pretrained classifier weights, and external dependency repositories were not preserved or executed; they are separate reproduction artifacts rather than missing paper text or tracked implementation files.

## Preserved attachments

| Path | Role in the source | SHA-256 | Preservation / extraction notes |
|---|---|---|---|
| `snapshots/attachments/sun-idiosyncrasies-llms-arxiv-2502.12150v2.pdf` | Reviewed arXiv v2 paper | `bfcb52e0516aa503532667e29b8dbbdd39954c15785198eaaf44c0a3b0eb7eed` | Downloaded directly from arXiv; all 32 pages extracted with `pdftotext -layout`; pages 1, 16, and 32 rendered and visually checked. |
| `snapshots/attachments/sun-idiosyncrasies-llms-pmlr-v267-sun25z.pdf` | ICML 2025 / PMLR version of record used for version comparison | `34b5d444c45d4c14fa39ca74116442b77ce69e100022c3e63e7468283d67eafe` | Downloaded from the PMLR volume repository; 32 pages and complete text inspected. It predates arXiv v2 cross-reference and figure-number corrections but contains the same substantive experiment set. |
| `snapshots/attachments/sun-idiosyncrasies-llms-code-e5333d0.tar` | Complete tracked tree of the linked implementation | `a5cf7396a3f6a9b4b6c615ef14fd18bb053e11e3729d694f41ac262d3cbed1f6` | Created with `git archive` from commit `e5333d01493963e5af44288fe2b9343ae6f13b9f`; contains all seven tracked files and no Git metadata. |
