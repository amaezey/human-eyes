# LLMs in Wikipedia: Investigating How LLMs Impact Participation in Knowledge Communities

- **Canonical URL:** https://arxiv.org/abs/2509.07819
- **Alternate access URLs:**
  - https://arxiv.org/pdf/2509.07819
  - https://arxiv.org/html/2509.07819
  - https://export.arxiv.org/api/query?id_list=2509.07819
- **Author / owner:** Moyan Zhou, Soobin Cho, and Loren Terveen
- **Publisher:** arXiv; manuscript submitted to ACM for PACM on Human-Computer Interaction (CSCW '26)
- **Published:** 2025-09-09
- **Retrieved:** 2026-07-17
- **Stable identifier:** arXiv:2509.07819v1; arXiv-issued DataCite DOI 10.48550/arXiv.2509.07819
- **Version / revision:** v1, submitted 2025-09-09; no later arXiv revision found as of retrieval
- **Extraction method:** official arXiv PDF downloaded with `curl`; PDF metadata and image inventory inspected with Poppler `pdfinfo` and `pdfimages -list`; all 19 pages extracted from the embedded text layer with `pdftotext -layout`; pages 1, 10, and 19 rendered with `pdftoppm` and visually compared; arXiv abstract, export API metadata, and experimental HTML checked for identity, version, and structure
- **Full-text status:** complete
- **Access and transformation notes:** no OCR used; the PDF has no embedded raster images; page headers, footers, column spacing, both tables, quotations, notes, and references through [98] are retained in layout text; form-feed page boundaries are rendered as `--- page break ---`; the arXiv page assigns DataCite DOI 10.48550/arXiv.2509.07819, but the manuscript's ACM reference line contains a placeholder publication DOI and no publication DOI is identified; no source content is omitted

## Full text

                                        LLMs in Wikipedia: Investigating How LLMs Impact Participation in Knowledge
                                        Communities
                                        MOYAN ZHOU, University of Minnesota, USA
                                        SOOBIN CHO, University of Washington, USA
                                        LOREN TERVEEN, University of Minnesota, USA
                                        Large language models (LLMs) are reshaping knowledge production as community members increasingly incorporate them into their
                                        contribution workflows. However, participating in knowledge communities involves more than just contributing content - it is also
                                        a deeply social process. While communities must carefully consider appropriate and responsible LLM integration, the absence of
                                        concrete norms has left individual editors to experiment and navigate LLM use on their own. Understanding how LLMs influence




arXiv:2509.07819v1 [cs.HC] 9 Sep 2025
                                        community participation is therefore critical in shaping future norms and supporting effective adoption. To address this gap, we
                                        investigated Wikipedia, one of the largest knowledge production communities, to understand 1) how LLMs influence the ways editors
                                        contribute content, 2) what strategies editors leverage to align LLM outputs with community norms, and 3) how other editors in
                                        the community respond to LLM-assisted contributions. Through interviews with 16 Wikipedia editors who had used LLMs for their
                                        edits, we found that 1) LLMs affected the content contributions for experienced and new editors differently; 2) aligning LLM outputs
                                        with community norms required tacit knowledge that often challenged newcomers; and 3) as a result, other editors responded to
                                        LLM-assisted edits differently depending on the editors’ expertise level. Based on these findings, we challenge existing models of
                                        newcomer involvement and propose design implications for LLMs that support community engagement through scaffolding, teaching,
                                        and context awareness.

                                        CCS Concepts: • Human-centered computing → Empirical studies in collaborative and social computing.

                                        Additional Key Words and Phrases: Knowledge production, Large Language Models, Human-AI Collaboration, Social Computing

                                        ACM Reference Format:
                                        Moyan Zhou, Soobin Cho, and Loren Terveen. 2026. LLMs in Wikipedia: Investigating How LLMs Impact Participation in Knowledge
                                        Communities. In Proceedings of PACM on Human-Computer Interaction (CSCW ’26). ACM, New York, NY, USA, 19 pages. https:
                                        //doi.org/XXXXXXX.XXXXXXX


                                        1   Introduction
                                        Knowledge production refers to the process of creating, maintaining, and propagating knowledge [2]. The laborious
                                        process has traditionally required contributors to carefully gather, verify, and synthesize information. But the advent of
                                        large language models (LLMs) has transformed this reality, as LLMs enable users to generate fluent and well-structured
                                        content through natural language prompts [8, 74]. Prior work has indicated the usefulness of LLMs as writing assistants
                                        and imagined the potential of LLMs in knowledge production [4, 51, 74, 83].
                                            However, participation in knowledge communities involves more than writing fluent or well-structured paragraphs.
                                        It is also highly epistemic (e.g., factuality, balance) and social [11, 68] (e.g., aligning with norms [6, 12], engaging with
                                        other community members [56, 68]). There is a mismatch between surface-level fluent content produced by LLMs
                                        and the unique epistemic and social needs of knowledge communities, such as knowledge integrity [38]. Furthermore,
                                        Wikipedia, one of the largest knowledge production platforms [5, 68] has not yet reached a consensus or developed
                                        Authors’ Contact Information: Moyan Zhou, zhou0972@umn.edu, University of Minnesota, Minneapolis, Minnesota, USA; Soobin Cho, soobin30@uw.edu,
                                        University of Washington, Seattle, Washington, USA; Loren Terveen, terveen@umn.edu, University of Minnesota, Minneapolis, Minnesota, USA.

                                        Manuscript submitted to ACM


                                        Manuscript submitted to ACM                                                                                                                 1


--- page break ---

2


norms around LLMs [5, 68], which could exacerbate these challenges. As a result, individual editors must interpret,
navigate, and experiment with appropriate and responsible usage of LLMs within the community.
    The tension between surface-level content generation and unique epistemic and social needs raises important
questions about how LLMs are shaping community participation in knowledge communities, critical to support the
credibility and sustainability of these knowledge communities. This is especially true given the rise of LLM-generated
content in new articles observed in Wikipedia [10], indicating that editors have already incorporated LLMs during their
contributions. Our study aims to understand the use of LLMs by knowledge community members. Specifically we ask:



     • RQ1: How does using LLMs influence the ways editors contribute content?
     • RQ2: What strategies do editors leverage to conform to community norms for LLM-assisted contributions?
     • RQ3: How do other editors in the community respond and engage with LLM-assisted contributions?



    Through semi-structured interviews with 16 participants who have used LLMs to edit Wikipedia, we unveil an
expertise-based participation divide between editors. Experienced editors enhance their participation through LLMs, as
they expand the range of their contributions in Wikipedia, leverage strategies to align LLM-generated content with
community norms, and thus receive positive responses from other members. In contrast, LLMs raise the demands for
new editors to participate in the community. LLMs lower the barriers for entry, and new editors tend to rely on LLMs
to fill in their knowledge gaps. However, LLMs compel them to make judgments about AI-generated content, which
requires skills they have not yet developed. This challenges them to produce high quality content, leading to rejections
from others.
    Based on our findings, we discuss how the participation paradox for newcomers, namely lower barriers to entry yet
higher demands to participate, arises from LLM usage, breaking the trajectory of Legitimate Peripheral Participation
(LPP). LLMs interrupt learning pathways for newcomers, thus new editors miss opportunities to gain wiki skills
gradually. At the same time, LLMs blur the boundaries between peripheral and central tasks and push newcomers
from peripheral participants to editorial judges, which requires more central wiki skills. Building on our findings, we
then propose design implications to mitigate the participation gap LLMs can lead to by fostering newcomers’ learning
process and supporting editors with varying expertise in knowledge production platforms.
    We situate our work within the broader empirical HCI/CSCW research on human AI collaboration and communities
of practices [23, 55, 62], particularly work around how tools reshape work [22, 61], how individuals align to norms and
boundaries [34, 39, 41], and how community respond and adapt to technology changes [48, 75]. By examining how
editors integrate LLMs into their practices, we made the following contributions:



     • We surfaced the invisible dynamics of how editors with different levels of experience adopt, adapt, and respond
       to LLMs in knowledge communities in practice;
     • We extend Legitimate Peripheral Participation by demonstrating that LLM usage interrupts newcomers’ traditional
       learning pathway;
     • We informed the design of future LLMs for knowledge communities, highlighting the need for AI tools to scaffold,
       teach, and be context aware to support community participation.

Manuscript submitted to ACM


--- page break ---

LLMs in Wikipedia                                                                                                           3


2     Related Work
2.1    Human AI collaboration in writing
Knowledge production involves writing, summarizing, and drafting information in textual format. To contextualize
this process, we surveyed the literature in the domain of AI-assisted writing and identified patterns of human-AI
collaboration.
    Generative AI supports writing across a wide range of domains, from personal writing such as diary entries [43], to
creative writing including stories [7, 15, 52, 76, 97], fictions [94], metaphors [30], poetry [14], and screenplays [80], as
well as academic writing [21, 52, 54]. As LLMs continue to advance, more domains will leverage their capabilities to
enhance the writing process.
    In academic writing, which closely aligns with our focus on knowledge production, researchers have developed
and evaluated tools to assist with various stages of the writing process. For example, Sparks [31] was implemented to
inspire connections between scientific concepts. A quantitative analysis of 14 million abstracts of published papers over
14 years revealed that at least 10% of 2024 abstracts were likely LLM-assisted, indicated by the suspicious increase in
the usage of certain words [46]. Several studies [1, 79] evaluated the potential of LLMs to conduct literature reviews.
Additionally, Radensky et al. [65] introduced a plan-draft-revise workflow and designed a writing assistant for scientists
to draft blog posts for their research papers.
    Researchers have also investigated how users perceive and interact with these AI tools. Users often perceive
generative AI not merely as a passive writing aid [40], but an idea generator and active collaborator [21, 94] in content
creation. Engagement with LLMs differs significantly depending on the use case. For example, users engage in back and
forth conversations with Sparks for translating concepts, while they use it more independently in longer sessions for
inspiration and perspective taking [31]. Implicit users who were less specific about their goals tended to search for
new ideas, while explicit writers sought precise content to incorporate in their writing [94]. Similarly, ChatGPT was
used to support users’ information seeking behaviors, rather than completing tasks for them [54]. Writers may modify
or directly accept the generated text [95], and doctoral students iteratively interact with GAI assistants in reading,
copying, pasting and shaping content in the writing process [59].
    Building on this body of prior work, we examined how knowledge contributors use and interact with LLMs. Our
findings extend existing research by revealing use cases within the knowledge production process and identifying
similar user behaviors. Most importantly, we found expertise influences their ability to incorporate LLM-generated
content in their own writing. As a result, their participation in the knowledge community is affected.

2.2    Knowledge production in Wikipedia
In Wikipedia, participating in the collaborative knowledge work entails three major aspects: 1) contributing content 2)
engaging with other editors and 3) enforcing norms.

2.2.1 Content. The central component of knowledge work on Wikipedia focuses on the content or knowledge itself.
Rooted in a range of intents such as adding supporting evidence and removing existing information [66], editors perform
insertions, deletions, modifications, and relocations [19, 20]. Such adjustments to articles target different elements in
Wikipedia articles, including texts, links, references, and templates [19, 20]. Yang et al. [92, 93] categorized edit actions
into two larger groups: meaning-preserving edits and meaning-changing edits. While meaning-preserving edits include
modifications such as paraphrasing, spelling/grammar, and relocation, meaning-changing edits contain insertions,
deletions and some level of modifications. Built on 14-label taxonomy from [92], Ruprechter et al. [71, 72] derive 3
                                                                                                   Manuscript submitted to ACM


--- page break ---

4


super-labels: content as modification to actual information on the article page, format without changing of meaning on
text, and WikiCotent such as processing tags and vandalism fighting.
    Multilingual edits across language editions [32] are important for knowledge production, especially on Wikipedia,
because of (1) the nature of more than 300 language editions in Wikipedia [70], and (2) content coverage and language
gaps that contributors aim to bridge [67]. As the quality [70] and quantity of articles across Wikipedia language editions
vary diversely [50, 91], multilingual editors play an essential role in bridging and filling the gaps from one language
edition to another [32, 42, 91].

2.2.2 Community. As editors gain experience on Wikipedia, their focus often shifts from individual content edits to
active engagement with the editor community [11]. The need for coordination increases, as social interactions with
other editors help seek internal consensus [6] (e.g., structure of the page [68]), resolve conflicts [45, 56], especially when
they work on the same articles [68]. Editors engage in social interactions [53] in talk pages and Wikiproject groups
[68]. Though a small group of editors participate in article talk page discussions [44], editors use both article talk pages
and user talk page [45] for diverse purposes, such as requests or suggestions for editing coordination, requests for
information, and references to vandalism [96]. Wikiprojects establish a sense of belonging for editors as they socialize
with other similar-minded editors [24, 68].

2.2.3 Policies and Guidelines. On top of content and community, an editor is expected to follow community norms.
Wikipedia policies and guidelines are community norms that support collaborative work [6] and maintain high quality
content and credibility of Wikipedia [64]. These policies define not only the standards for allowed content (e.g., Neutral
point of view [85], Verifiability [89], Notability [88]), but also prescribe expected behaviors among community members
(e.g., civility, dispute resolution, and no personal attacks) [78]. Butler et al. [12] identified their roles such as signals to
external organizations protecting Wikipedia’s reputation and outside attack. They also represent collective rational
efforts to organize, coordinate for consistent and reliable contributions. By easing the pains of seeking consensus [6],
these rules play an essential role as boundary objects [82] to the daily operation in Wikipedia.
    In summary, content, community, and norms inspire and guide our research questions, as we reflect that participation
in Wikipedia consists of these aspects. They also serve as a basic framework to inform our interview questions, in
correspondence to knowledge contributors’ edits and contribution workflows.

2.3   Tool-assisted editing in Wikipedia
Editors and researchers have developed tools to ease the complexity of contributing to Wikipedia. In this section, we
mainly reviewed semi-automated bots, and noted more recent AI/ML tools.

2.3.1 Semi-automated bots. Bots play a vital role in Wikipedia’s collaborative editing system [25] and have been
extensively studied in the literature [18, 27, 29, 81]. Bots are designed to automate repetitive or large-scale tasks [81],
and most of the early bots are implemented by scripts. For instance, HostBot invites new editors to socialize in Q&A
forums [57, 58]. Huggle and Twinkle fight vandals and unconstructive edits [29]. Rambot adds data into country and city
articles [36]. Zheng et al. [98] classified bots’ roles into 9 categories: generator, fixer, connector, tagger, clerk, archiver,
protector, advisor, and notifier.
    While bots protect and patrol high quality knowledge in Wikipedia [27], they can also cause unintended consequences.
In particular, vandal fighter bots negatively impact newcomers’ retention, as they revert contributions from good faith
editors that may appear suspicious [34, 98]. This reflects a broader dynamic in human bot collaboration. Editors not
Manuscript submitted to ACM


--- page break ---

LLMs in Wikipedia                                                                                                        5


only develop, approve [28], operate, and maintain bots [68, 98], but are also influenced by bots’ behaviors and work
alongside them. For example, human editors check and correct the information by bots [60]. In the context of vandal
fighting, bots detect potential vandals and put them in queues. Editors can then decide and authorize bots to revert
edits and leave warning messages. In more severe cases, bots can notify administrators when users accumulate multiple
warnings [29].
    Because bots closely support the editing process, they are generally well accepted [17]. In fact, they are not viewed
as simple tools, but social actors [26] that shape collaborative outcomes. Through the evolving collaboration dynamics,
humans and bots maintain the values and social structures of Wikipedia together [29].
    Notably, emerging AI/ML powered tools are developed not only to assist content editing, but also to support tasks
related to editing. Some tools [9, 47, 50] focus on multilingual contributions. Some tools are designed to support tasks
related to editing, while others make suggestions or improve content quality. For example, SuggestBot [18] and other
recommendation systems [91] make edit recommendations to editors. ORES [33] evaluates the quality of articles.
Edisum [73] generates informative edit summaries. Wikimedia Foundation recognizes the potential of AI tools, and is
developing strategies to continue invest in AI tools that support the editing process and improve editors’ experience
[84].
    Building on prior work, we identify interaction patterns that differ from observed in traditional bot usage. Unlike
traditional tools that conform to Wikipedia norms, LLMs bypass policies and guidelines and require editors to make
normative decisions, which challenge new editors’ participation.


3     Methods
The researchers collaboratively designed a semi-structured interview protocol, which included 3 sections: 1) general
context about contributions, 2) experience of using LLMs in Wikipedia, and 3) vision for human AI collaboration in
knowledge production. After receiving an exemption from the Institutional Review Board at the University, the first
author conducted pilot studies with two graduate students and refined the interview questions. Data from pilot studies
were excluded from data analysis.


3.1     Recruitment and Participants
We recruited participants through multiple channels. We posted our interview invitation on the WikiMedia project page.
At the same time, we searched for editors who potentially used LLMs and sent invitations to their talk pages or via email
if they had enabled that feature. Lastly, we leveraged snowball sampling, asking referrals from our participants. Editors
who were interested in the interview study filled out a survey about basic usage of LLMs, experience on Wikipedia,
contact and demographic information. We then sent emails to schedule the interview on Zoom, along with a consent
form. Several participants indicated discomfort with video/audio recording. Thus, we offered the option to participate
in the interview through written text (email).
    As a result, we conducted 16 interviews, of which 5 were conducted via email. We began to observe data saturation
after finishing the 13th interview. Thus, we stopped recruiting more participants after completing 16 interviews, which
was consistent with the average sample size for qualitative research at a top HCI conference [13]. Participants did not
receive monetary compensation, and their demographic information along with their expertise in Wikipedia is listed in
Table 1.
                                                                                                Manuscript submitted to ACM


--- page break ---

6


ID     Tenure       # of Edits      Frequency       LLM models           Gender              Age              Race

P01    0-2 years    ~100            monthly         ChatGPT, Gem- Male                       35-44            White/Caucasian
                                                    ini, You.com
P02    2-5 years    10k+            daily           ChatGPT
P03    5+ years     21k+            daily           ChatGPT, Grok        Male                55+              White/Caucasian
P04    5+ years     2k+             weekly          ChatGPT                                  25-34            White/Caucasian
P05    5+ years     50k+            daily           ChatGPT              Male                25-34            White/Caucasian
P06    5+ years     1k+             weekly          ChatGPT              Male                35-44            Avropoid-
                                                                                                              Caucasian/Azerbaijanian
                                                                                                              turkish
P07    5+ years     159K+           daily           ChatGPT              Male                45-54            Middle          East-
                                                                                                              ern/Arab
P08    5+ years     12k+            daily           ChatGPT              Non-binary          18-24            Asian
P09    0-2 years    5.3K+           daily           ChatGPT;             Male                25-34            White/Caucasian
                                                    Claude
P10    2-5 years                    monthly         ChatGPT              Male                18-24           Black or African
                                                                                                             American
P11    5+ years     ~10             yearly          ChatGPT
P12    5+ years     55k+            weekly          ChatGPT;             Prefer not to an- 35-44              White/Caucasian
                                                    Claude; Llama        swer
P13    2-5 years    4k+             daily           ChatGPT; Grok        Male                18-24            Bengali
P14    0-2 years    200+
P15    0-2 years    200+
P16    5+ years     83k+            monthly         ChatGPT              Male                35-44            White/Caucasian
Table 1. Participant summary, adopted from [75]. Some fields are left empty due to incomplete responses or participants’ preference.




3.2   Interview Procedure
Consent was acquired from each participant before the interview began. Before the interview, we thanked them for their
participation and noted the privacy considerations - the interview would be recorded only for data analysis purposes;
video is not required; participation would remain anonymous. As each participant fully understood and agreed, we
began the interview and followed the interview protocol.
    First, we briefly introduced the goal of the study. We then asked participants about their contribution process
such as typical tasks, general workflow, and common practices or guidelines to understand the context. Next, we
asked participants to think of a specific use case of LLMs in their contribution, and asked relevant questions such
as interactions with LLMs. Then, we asked them to envision the future for human AI collaboration in knowledge
work and ideal interactions with LLMs. We concluded the interviews by inviting participants to share any additional
information. In the semi-structured interview, we allowed participants to freely share their experiences and asked
follow-up questions.
Manuscript submitted to ACM


--- page break ---

LLMs in Wikipedia                                                                                                                      7


3.3    Data Analysis
Our 11 recorded interviews ranged from 42 minutes 22 seconds to 1 hour 17 minutes 29 seconds, with an average of 1
hour 3 minutes 18 seconds. After transcribing the interviews, we conducted an inductive thematic analysis approach
[16]. We used ATLAS.ti, a popular software for qualitative data analysis. First, the authors open coded three interviews
together to establish a shared standard for open coding. Then, we asynchronously open coded the remaining interviews.
We ended up with 1524 codes, for example, “P05 - LLMs has no sources”.
     After that, the authors collaboratively grouped the codes based on their similarity and relevance in Miro. Themes
and sub-categories emerged through this iterative process, and the authors discussed and reached agreement for the
name of the themes and sub-categories. For example, the code mentioned above was put under the sub-category “no
sources," and the theme “violates Wikipedia policies."

4     Results
Our results surfaced how knowledge contributors leverage and interact with generative AI (see Table 2 for LLM
use cases), showing that LLM usage influences participation in knowledge production communities in three ways:
contributing content, enforcing norms, and other members’ engagement. Across these dimensions, we identified a
participation divide between editors, shaped by differences in expertise.

    Category    Use cases                            Highlights
                Generating examples
                                                     Generating practical examples for theoretical concerns. (P14)
                Providing editing guidance
    Generate                                         I’ve been learning. So, I need a guide... If there is anything that could guide
                Creating articles
                                                     me for better content. (P15)
                Writing codes for articles
                Searching sources
                                                     I think it’s better at searching for those than I am...it is a skill to phrase
    Search      Suggesting images
                                                     your queries in Google and know how to find things. (P04)
                Searching information
                Copyediting                          Google cannot do it. DuckDuckGo cannot do it. But language models are
                                                     quite often able to do it well, and give me the short name of a thing. (P07)
                Formatting                           In the old days, I would have copied this thing, put it into a plain text file,
                                                     changed it to a CSV, uploaded it into R, and written a script. But with
    Refine                                           ChatGPT, I can just post the whole thing to ChatGPT, say I want it in this
                                                     format. (P04)
                Translating                          You use wikitext, like square brackets to link to a page and you use single
                                                     quotation marks to make something bold or italic and all this. Google
                                                     Translate does not understand this wikitext language, but ChatGPT does.
                                                     (P05)
Table 2. Selected LLM Use Cases Reported by Participants. The distinction between generation and refinement lies in whether the
content exists prior to interacting with the LLMs. In generation, LLMs are used to produce new text from scratch. In refinement, editors
input existing content to receive feedback or suggestions for improvement. Copyediting includes grammatical improvements, rephrasing
suggestions for repetitive words or longer description, brainstorming alternative expressions.




4.1    RQ1: Contributing content
Our findings for RQ1 show that experience level mediates how LLM use influences content contribution. For experienced
editors, LLMs extend cognitive capacities, enabling exploration of new topics and improving confidence and quality.
                                                                                                            Manuscript submitted to ACM


--- page break ---

8


In contrast, newcomers often rely on LLMs to fill in their knowledge gaps, as LLMs reduce the barriers to entry and
provide a sense of guidance.

4.1.1 Experienced editors venture into new topics and tasks. LLMs demonstrated the ability to guide editors toward
content they wouldn’t have otherwise considered, by providing useful contextual information without requiring
proactive efforts from the editors. P05 shared: “The articles that I created using AI, I probably would not have created
them." This is especially true when available resources are limited for the exact tasks. P08, who was writing code for
supplementary graphs to improve article quality, didn’t know anyone to consult about troubleshooting his R code,
especially as it might need a long time to fix the bugs. LLMs served as a support tutor, as he reflected:

        “[ChatGPT] is basically the next closest thing to [people who can help]. It brings up different packages that I
        wouldn’t consider...[LLM] definitely directed me to things that I would have never been able to think of on my
        own."

    In this way, LLMs enabled him to engage in tasks he would not have attempted alone. P03 shared a similar anecdote.
As he went down a rabbit hole on fruits and vegetables, LLMs suggested a new section he didn’t even know about and
would not think of:

        “[ChatGPT] suggested a section where I didn’t even know that a specific vegetable had been - a hybrid of
        this vegetable created another one that was not in the article. . . I looked to make sure the information was
        factually correct, and I put that in there."

    For P03, he explored novel topics besides his typical contributions in business articles. The capacity of LLMs to
introduce new, previously overlooked perspectives enhances editors’ creativity and encourages them to venture beyond
their usual domains, most importantly, add the piece of knowledge in Wikipedia.

4.1.2 Experienced editors are exposed to new perspectives. In addition to helping editors move beyond their typical
domains, LLMs extend cognitive capacity by introducing unexpected and insightful perspectives. P08 recounted LLMs
supporting him to reflect on his own text in a different way, for instance, by suggesting what is interesting about his
text:

        “I’m asking LLMs for ideas...“What’s interesting in this big block of text I’ve written?" Honestly, I spent 48
        hours staring at my computer screen writing this article. I’ve kind of bored myself to death with it."

    LLMs could also serve as a simulated average reader, offering pluralistic perspectives that editors find helpful in
evaluating their content. P09 noted, “I regularly ask LLMs...when I want a pluralistic opinion. You want to know what the
average reader would think."

4.1.3 Experienced editors are more confident in unfamiliar areas. This cognitive support, in turn, increased confidence
and satisfication for experienced editors, even in domains they are less familiar with. P03 felt more capable of editing
complex topics such as medical and legal content: “I can digest the information if I don’t understand...and run through
LLMs to simplify for myself." P04 treats LLMs as an additional validation mechanism: “LLMs are a good extra filter to
make sure there’s not something you overlook or mistakes you are making." P08 remembered editing without LLMs took
endless iterations, as he would “write, write, try to get through it," especially when he got stuck. The presence of LLMs
helped him feel satisfied with his work sooner, even improving his sleep routine: “it allows me to feel happy with what
I’ve written earlier...thus allow me to go to bed earlier."
Manuscript submitted to ACM


--- page break ---

LLMs in Wikipedia                                                                                                              9


4.1.4 LLMs enhance contribution quality for experienced editors. Multiple experienced participants observed that the
quality of their contributions has improved. For example, P09 specified that his accuracy on topics where he lacked
in-depth knowledge “had definitely improved." P03 agreed with P09, and shared that fewer post-edit corrections from
other editors signaled quality improvement: “My edits over the past two years - the quality has improved because fewer
people have had to come behind me and clean up."

4.1.5 LLMs lower entry barriers for newcomers. New editors themselves frequently shared that LLMs encouraged them
to edit Wikipedia. For example, P14 described the challenges related to information access in his local context, and how
LLMs helped with research that would otherwise take days:

       “LLMs encourages me to work on Wikipedia...I have to go to libraries to look for information...I must pay for
       the transportation and a lot of other things...Before I go to the library, I’ll check on AI to know more about the
       topic." (P14)

  P01 found that proofreading using LLMs made editing easier, particularly given that English was not his native
language: “English is not my native language...I have to proofread it on ChatGPT." More experienced editors agreed
that LLMs lowered the barriers for entry, as P12, P09, P04 and P05 pointed out that LLMs “increase the ability of new
contributors to contribute, as it breaks down a lot of the barriers (P12)."

4.1.6 New editors rely on LLMs to fill in their knowledge gaps. As LLMs are able to lower the technical and linguistic
barriers, newcomers tend to rely on LLMs to fill in their knowledge gaps, often in generating and searching for content.
Editors observed that newcomers may use LLMs to generate content. P04 observed that many newcomers were using
LLMs to draft articles: “There’s an increased expansion...the vast majority of them just write a prompt like, hey, ChatGPT,
can you write a Wikipedia article on this?" Newcomers also leveraged LLMs to search for knowledge around the subject
topics, and specific wiki knowledge. For instance, P10 shared that in order to ensure high quality contribution, he
“use LLMs as my research platform to know more about what I’m looking for." P01 emphasized that he used ChatGPT to
“increase my knowledge around the subjects." He described LLMs as a wise mentor he could learn from.:

       “I take the information and integrate it into my thoughts, like speaking with a wise person..I don’t have the
       luxury of speaking with super intellectuals around myself...I compensate for the gap of knowledge." (P01)

  Similarly, P14 perceived LLMs to be a “school" for him, specifying that LLMs allowed him to “know more about
anything inside my house." He demonstrated this by sharing an example of him deciding to create an article on English
Wikipedia, and asking LLMs “how do I start doing this?" and learned that the articles needed “citations, notability and
other things." LLMs can be a guide for newcomers. P15 reasoned that “I need a guide...If there is anything that could guide
me for better content."


4.2   RQ2: Conforming to community norms
To answer RQ2, our findings showed that editors rely on core content policies and guidelines to navigate the unclear
norms around LLM usage. They recognize that LLMs could violate these standards, indicating that LLM use is situated
within the Wikipedia editing ecosystem. Participants described three strategies to make editorial judgments: evaluation,
verification, and modification. As a result, LLMs challenged new editors, as they had not yet developed skills to make
complex judgments and align to community standards.
                                                                                                      Manuscript submitted to ACM


--- page break ---

10


4.2.1 LLMs fail to align with core Wikipedia content policies. Participants consistently described limitations of LLMs
from the lens of violating core Wikipedia policies, as P02 summarized, “LLM output has many flaws and often violates
Wikipedia policies." The most frequently mentioned concerns were related to the Neutral Point of View (NPOV) [86],
Verifiability [90], and No Original Research (NOR) [87].
     NPOV [86] is defined as “representing all the significant views on a topic fairly and proportionately without editorial
bias.” LLMs often produce language that violates NPOV due to an overly positive or promotional tone. P05 noticed
that LLMs tend to use phrases such as “it’s one of the best” or “there are so many possibilities," which are discouraged
unless supported by reliable citations. He added that such content often contains “puffery peacock terms," especially
when asking LLMs to write something from scratch. P07 agreed with P05, as he observed that LLMs could use English
expressions not typically found in Wikipedia. This aligns with prior work [3], which found that LLMs are limited in
detecting and generating content that conforms to NPOV like a community expert.
     Verifiability [90] refers to the ability of a claim to be proven right or wrong, typically through the presence or
availability of sources. It is compromised when LLMs cite unreliable sources or fabricated sources. P07 criticized a LLM
named Perplexity. While sometimes it “doesn’t give any sources," other times when it gives sources, they would not meet
the Wikipedia standards, for being “unreliable junk commercial websites that are made not for providing correct or verified
information, but just for gathering clicks and showing advertisements."
     LLMs are prone to hallucination, especially for obscure content. This violates NOR [87] which prohibits original
research that finds no reliable or published sources to support. More importantly, LLMs’ tendency to hallucinate
contradicts the very core value of knowledge integrity. P04 specified that LLM-generated content was “not necessarily
accurate" as LLMs “can hallucinate and make up sources." P02 and P03 also mentioned hallucination, as P02 explained
“when the model invents non-existing facts and invents non-existing references to support claims." P08 shared specifically
about LLMs struggling with less common programming languages, noting their limited performance beyond languages
like Python or R.

4.2.2 Participants’ strategies to make editorial judgements. To cope with the risk that LLMs may violate policies and
guidelines, our participants emphasized their responsibility as gatekeepers. P03 stressed, ““even if you have all the tools
available, you are still the last one to make the decision whether this should go in or not." In practice, editors used three
key strategies when working with LLM-generated content: evaluation, verification, and modification.
     Evaluation involved assessing whether LLM suggestions improved the readability and coherence of the content. P08
put it as “make judgement about whether the LLM content makes sense." P02 developed a practice of “evaluating whether
any of the [suggestions] would improve the writing." P09 evaluated the quality in terms of consistency as he “regenerated
the answers to see if it’s consistent, [and] compared the answers of multiple chatbots."
     While evaluation ensures readability and coherence, verification checks the content’s factual accuracy and reliability.
P09 and P04 both stressed “verifying that everything makes sense and is supported by sources (P09)." P07 noted the
necessity to ‘check every word that LLM wrote because of verifiability." He mentioned specific strategies for verification:
reaching out to friends with questions, and cross-referencing terminologies or phrases via web searches.
     Additionally, participants intensively modified the outputs before incorporating them into Wikipedia to align with
Wikipedia’s tone and style. P16 noticed that LLMs tend to be overall more positive, and depicted modification as
neutralizing the tone of the text. P07 would “heavily edit" the output by himself before publishing. P03, P04, and P05
would modify the text to better fit the context, such as “wiki format (P04)" the links and fixing typos in wikitext, as
“ChatGPT could translate the wikilinks or reference wrongly so I have to update and change them (P05)."
Manuscript submitted to ACM


--- page break ---

LLMs in Wikipedia                                                                                                            11


4.2.3 Newcomers as gatekeepers? Being gatekeepers for LLM-generated content requires expertise and wiki knowledge,
specifically around Wikipedia norms and standards. However, this role is high-stakes and unfamiliar to newcomers, as
they have not yet developed these skills. For example, newcomers recognize that they did not know all the guidelines
and principles as P01 pointed out “I am still developing my skills. I’m new to Wikipedia, so I may not know all the guidelines
and principles." P03, an experienced editor, talked about how he made decisions when interacting with LLMs: “I am the
big decider of what I know in my gut what should be in Wikipedia." And he pointed out that editors with many years of
contributions would have the expertise to tell whether materials should be in Wikipedia or not. He then contrasted
editors with different levels of expertise: “I have 20 years of editing right now. So, the tool is much more of an enhancement
to me because I know what’s allowed and not allowed quickly. I can accept or reject a suggested edit...[but] a new user would
go through and just accept, accept, accept the edit." P02 mentioned that “inexperienced editors often lack the ability to
evaluate whether an output is appropriate...This creates problems when inexperienced editors unaware of the limitations of
LLMs rely on them to make contributions without critical examination." This suggests that newcomers lack the ability to
critically evaluate and examine LLM-generated content and may over-rely on LLM outputs, which leads to challenges
in producing high-quality content. This is well documented in an example P15, as a newcomer himself, shared:

      “I was trying to get good content out of it, but it had so many unwanted things as well. As I’m learning, I’m
       not that clear about the content exactly, what should I filter out. Sometimes even if I read it multiple times, I
       do not know whether it is needed or not, or whether the content is good or not, if this particular explanation is
       useful or not. Then after this editor pointed it out, I noticed that’s not what [Wikipedia] wanted." (P15)

4.3   RQ3: Community engagement
To answer RQ3, we found that other editors’ response to LLM-assisted edits further revealed the participation divide
between new and experienced editors. Other editors praise and accept LLM-assisted contributions from experienced
editors, yet call out and reject those made by newcomers. The ability of conforming AI-generated content to standards
leads to difference in other members’ perception on whether the content is AI-generated, resulting in the differences
in the response. Such dynamics may contribute to the overall sensitivity and confusion around LLM usage in the
community.

4.3.1 Other editors responded to newcomers with rejections. New editors faced heightened scrutiny when using LLMs,
as they found themselves in a position where other editors quickly found out that they had used LLMs. P11 recounted
his experience: “As soon as I pushed the article out there as a draft, I got a message from somebody in the community
saying, “oh, it looks like you created this with an LLM and we don’t want that kind of material." He reflected, “I’m glad that
they’re being careful about it, but it’s clear that they’re sensitive." Likewise, P01 was told his contribution was “machine
generated," and P10 was criticized for making “promotional and essay-like articles." P15 shared that another editor quickly
identified his use of ChatGPT, which prompted him to remove all LLM-generated content. As P09 noted, “most of the
poorly written AI content is already removed...In fact, it gets removed pretty quickly," suggesting that contributions flagged
as LLM-generated are assumed to be low quality and are swiftly deleted.

4.3.2 Other editors responded to experienced editors with approval. In contrast, experienced editors often received
positive feedback. P16 shared that one editor praised him for copyediting a section this editor had written, “better than
he had ever seen before." He clarified: “it was chatgpt that had done it." P04 also shared his positive experience: “In general,
LLM-based edits I made are well received. They’re not really received any differently than in my non-LLM based edits." P07
                                                                                                     Manuscript submitted to ACM


--- page break ---

12


noted that no one noticed or identified that he had used LLMs, due to extensive post-editing. P09 received a similar
response, as no one complained about his usage of LLMs, and his edits were rarely reverted. However, However, even
experienced editors occasionally faced false accusations, as P03 noted: “being called out wrongly infuriated me." When
the edits seemed to be generated by LLMs, even experienced editors were called out, underscoring the community’s
sensitivity to LLMs.

4.3.3 Overall, the community remains sensitive and confused about LLM uses. The general sensitivity and confusion
around LLMs may stem from a lack of consensus on what it means to use LLMs for editing. P04 remarked that no one
knows exactly what “using LLMs" entails: “it’s so ambiguous...people might assume that [LLM assistance] means you copy
and pasted text from an LLM prompt without any review or understanding." The assumption can lead to mistrust, even
when the content is factually accurate. P09 brought up an observation for editors attacking good edits because they
were known to be generated by LLMs: “I have once seen spiteful comments...other people severely criticized [the article] for
being AI-generated," and he concluded “generally speaking, the vibe around LLMs is poor among other Wikipedia editors."
This suggests that the community cares not only the quality of the content, but also about its origin.

5     Discussion
5.1    The paradox of participation
Our findings reveal a paradox of participation: LLMs simultaneously lower barriers to entry while increasing the
demands of contributing, especially for newcomers who already struggle to engage with the community [34, 58, 77].
We discuss this paradox of participation in three interrelated elements:
      • LLMs interrupt traditional learning pathways for newcomers that support gradual skill acquisition for newcomers.
      • LLMs shift the focus from peripheral tasks to editorial judgment, requiring newcomers to make normative
        decisions before developing core competencies.
      • As a result, LLMs exacerbate a participation divide, enabling experienced editors to thrive while marginalizing
        newcomers.
These dynamics challenge expectations of Legitimate peripheral participation (LPP) [11, 35, 49] and situated learning
[49, 69]. In addition, they reveal nuanced aspects of the second-level digital divide [37] in socio-technical systems in
peer production platforms.

5.1.1 Interrupted learning pathways for newcomers (Situated learning). Before the widespread use of LLMs, learning in
Wikipedia for newcomers followed a gradual and scaffolded path. Legitimate Peripheral Participation (LPP) [11, 49]
states that newcomers start from low-risk and small tasks, and progressively take on more responsibilities. Built on LPP,
situated learning [49, 69] emphasizes that learning is social: individuals gain skills and knowledge through interactions
with other members in collaborative work.
     In Wikipedia, newcomers typically begin with low-stakes tasks such as fixing errors and improve grammars [11].
Through receiving feedback from other community members, the gradual learning pathway to participation enables
newcomers to gain technical skills, understand community norms, and collaborate with others. Given Wikipedia’s
complex norms and standards, this learning pathway is especially important for newcomers to develop normative
understandings of policies and guidelines and gain legitimacy [35, 63].
     However, LLMs disrupt this learning trajectory by enabling new editors to directly contribute to complex tasks.
For new editors, LLMs offer the promise of access to knowledge. For instance, our results show that newcomers have
Manuscript submitted to ACM


--- page break ---

LLMs in Wikipedia                                                                                                         13


increased access to linguistic support (especially for non-native speakers), contextual suggestions (wikitext), and source
search. These affordances enable them to overcome traditional entry barriers, increase confidence, and thus take
on complex tasks such as drafting new articles or synthesizing sources for their initial stages of contributions. As a
result, rather than working toward the more complicated tasks step by step, newcomers now can directly make these
contributions.
  In this way, LLMs accelerate participation. However, they simultaneously shortcut the social situated learning that
Wikipedia had relied on to support newcomers’ participation. LLMs help users perform harder tasks, but they skip the
essential steps to teach users on how to understand Wikipedia norms, and interpret content policies and guidelines.
In exchange for immediate access to support, newcomers miss opportunities to internalize Wikipedia as a social and
epistemic community.

5.1.2 A shift from peripheral tasks to editorial judgment (LPP). While LLMs enable newcomers to bypass low-risk
contributions, they impose new demands, which fundamentally shift the nature of participation. Instead of easing the
learning curve, LLMs thrust newcomers into an unexpectedly high-stakes and unfamiliar role that requires editorial
judgment. Editorial judgment demands deeper understanding of Wikipedia’s social norms, values and culture manifested
in policies and guidelines as gatekeepers [11]. To meet community standards, newcomers are now responsible for
verifying, evaluating, and modifying AI-generated content before publishing it. These responsibilities assume both
epistemic and social maturity.
  Previous AI tools on Wikipedia, such as SuggestBot [18], ORES [33], Vandal Fighter [81], inherently align and
reinforce community norms. In contrast, LLMs delegate the burden of judgment to editors. These judgments are
higher-stake and central to community culture, which are developed after gradual participation. Our findings show
that LLMs interrupt learning pathways for newcomers, which potentially results in further lack of competencies in
making such judgments. Yet, newcomers are challenged to make these normative decisions from the outset, with little
feedback and guidance. As a result, LLMs not only make it harder for newcomers to participate, but also fundamentally
change what participation entails, which challenges our assumptions about participation in communities of practice.

5.1.3 A new participation divide mediated by expertise (Second-level digital divide). While new editors face challenges
for their LLM-assisted contributions, more experienced editors are able to benefit from LLMs. Our findings suggest
that experienced contributors expand their participation through new topics and overcome their writer’s blocks. We
articulate this difference to originate from the level of expertise. More experienced editors are familiar with Wikipedia
policies and guidelines to critically evaluate AI output and adapt AI output to Wikipedia standards. Therefore, their
participation is enhanced.
  This participation divide stems not from access, but from unequal ability to effectively use LLMs. The lack of expertise
to use LLMs responsibly and acceptable to Wikipedia seem to be at the root of the problem. This mirrors the concepts of
the second-level digital divide [37], which specifies the disparity between individuals with different skills and knowledge
to utilize technologies to fully benefit from them, even if the access remains same. As a result, LLMs widen existing gaps
between newcomers and experienced editors in participating in the community from the ability to manage AI outputs.

5.2   Design implications
The paradox is both interesting and novel: LLMs empower newcomers to do more, but also demand more of them.
LLMs enable newcomers to participate, but fail to support legitimate participation. Our results underscore a key insight:
increased access does not guarantee better participation. In communities of practice like Wikipedia, expertise mediates
                                                                                                  Manuscript submitted to ACM


--- page break ---

14


the relationship between access to meaningful contributions. At the same time, LLMs demonstrate potential for positive
uses. For instance, they lower technical barriers, encourage contributions, and enhance participation across domains.
Thus, to account for both the potential and challenges of leveraging LLMs, we propose several design implications.


5.2.1 Scaffold participation through incremental guidance. Good-faith newcomers desire to learn and participate in
communities, but when LLMs flatten complex editorial processes into generated outputs from one simple prompt, they
remove crucial opportunities for learning. Rather than doing the work for newcomers, LLMs should scaffold the process
to guide them, given that scaffolding can lead to improved writing quality [21].
     For example, if an editor asks LLMs to generate a Wikipedia article, the system could decompose the task into
smaller steps, e.g., finding sources, summarizing content, and structuring the article. Instead of directly returning a
complete draft, the LLM could prompt: “Which sources would you consider for this topic?” In doing so, the LLMs act as
facilitators, enabling newcomers to learn through their conversational interactions.


5.2.2 Teach community norms through interactions. In addition to guiding editors to do the work, LLMs should help
them understand how to do it right. This means embedding normative feedback into the interactions. When newcomers
rely on LLMs, the system can serve as a reflective layer that encourages them to evaluate whether their contributions
align with community standards.
     There are several ways LLMs can provide such feedback. LLMs can highlight problematic portions to draw editors’
attention, provide both acceptable and unacceptable examples, and ask guided questions that allow editors to reflect by
themselves. In these ways, LLMs support norm understanding and adaptation, which is a vital element for communities
of practice.


5.2.3 Be aware of and personalize based on user expertise. Finally, context-aware LLMs should account for who is
asking. Expertise matters, especially in online communities. While experienced editors may benefit from direct outputs,
newcomers might need more guardrails. LLMs should adapt their responses accordingly.
     For instance, LLMs can refrain from directly generating content for newcomers, but instead, walking through each
step with newcomers, thus allowing them to learn by doing the actual work. In contrast, LLMs may be a good co-writer
for an experienced editor, with higher degree of freedom in what LLMs produce. Such systems do not aim to restrict
newcomers, but to ensure responsible participation for newcomers.
     We outlined three design implications for future LLM-based assistants in knowledge production communities,
which aligned with WikiMedia Foundation’s strategy regarding AI tools for editors [84], especially in terms of helping
newcomers understand policies and provide feedback to their edits. Our implications respect and are grounded in the
traditional learning pathways stated by Legitimate Peripheral Participation and Situated Learning. Accordingly, we
recommend designing such assistants to guide newcomers through the incremental trajectory from peripheral tasks to
more central and complex contributions. However, our results seem to hint at a new reality where newcomers bypass
peripheral tasks altogether. Newcomers wanted to create articles and LLMs may just be a tool they utilize to achieve
their goals. If not LLMs, they would still start contributing complex tasks from day one. This leaves us to ponder, if this
bypassing behavior is true, how should the community and researchers respond? We leave future research to explore
this emerging dynamic.

Manuscript submitted to ACM


--- page break ---

LLMs in Wikipedia                                                                                                                                15


5.3    Limitations and future work
Our study provides an in-depth understanding of how editors interact with LLMs in their knowledge production on
Wikipedia. However, we acknowledge two limitations for our study.
    First, while our qualitative approach enabled us to understand nuanced editor experiences and perceptions, it did
not quantify the prevalence of observed phenomena, which we recognized to be an important question to uncover.
However, our categories and themes for use cases could serve as a foundation for future research. Future research could
utilize our use cases (see Table 2 for LLM use cases) to develop surveys to assess the generalizability and prevalence of
these use cases and interaction patterns.
    Second, our study only focused on editors who have used LLMs in their editing process. This meets our expectations
and addresses our needs as we aim to understand user experience. However, this might introduce bias towards the
confidence level of technology adoptions, and most importantly underrepresented editors who deliberately choose
to not engage with LLMs. Future studies should include perspective from these editors, especially those who initially
chose to use LLMs but later stopped.


6     Conclusion
To address the gap in understanding the impact of adopting generative AI on knowledge contributors’ participation in
communities of practice, we recruited 16 participants who had used LLMs in their editing process from Wikipedia and
conducted semi-structured interviews with them. We asked about their perception, adoption, and interaction with LLMs,
and other editors’ response to their LLM-assisted edits. We found that LLMs introduced a participation divide between
new and experienced editors manifested in contributing content, enforcing norms, and other editors’ engagement. For
newcomers, the paradox of participation indicated that LLMs 1) interrupt their learning pathway, and 2) shift traditional
peripheral tasks into central tasks requiring editorial judgment. This challenge further escalates as experienced editors
are able to enhance their participation by 1) exploring new topics, 2) gaining multiple perspectives and 3) increasing
confidence. We offered design implications to mitigate the participation gap, including scaffolding complex tasks for
newcomers during interaction, educating community norms and standards, and considering expertise as an important
part of context. Our study demonstrates the importance of user experience research in shaping equitable AI integration
in communities of practice, and highlights future opportunities for designing LLM-powered tools that not only support
production but also foster community collaboration.


References
[1] Shubham Agarwal, Gaurav Sahu, Abhay Puri, Issam H Laradji, Krishnamurthy Dj Dvijotham, Jason Stanley, Laurent Charlin, and Christopher Pal.
    2024. LitLLMs, LLMs for Literature Review: Are we there yet? Transactions on Machine Learning Research (2024).
[2] Maryam Alavi and Dorothy E Leidner. 2001. Knowledge management and knowledge management systems: Conceptual foundations and research
    issues. MIS quarterly (2001), 107–136.
[3] Joshua Ashkinaze, Ruijia Guan, Laura Kurek, Eytan Adar, Ceren Budak, and Eric Gilbert. 2024. Seeing like an ai: How llms apply (and misapply)
    wikipedia neutrality norms. arXiv preprint arXiv:2407.04183 (2024).
[4] Marianne Aubin Le Quéré, Hope Schroeder, Casey Randazzo, Jie Gao, Ziv Epstein, Simon Tangi Perrault, David Mimno, Louise Barkhuus, and
    Hanlin Li. 2024. LLMs as research tools: Applications and evaluations in HCI data work. In Extended Abstracts of the CHI Conference on Human
    Factors in Computing Systems. 1–7.
[5] Phoebe Ayers, Charles Matthews, and Ben Yates. 2008. How Wikipedia works: And how you can be a part of it. No Starch Press.
[6] Ivan Beschastnikh, Travis Kriplean, and David McDonald. 2008. Wikipedian self-governance in action: Motivating the policy lens. In Proceedings of
    the International AAAI Conference on Web and Social Media, Vol. 2. 27–35.
[7] Oloff C Biermann, Ning F Ma, and Dongwook Yoon. 2022. From tool to companion: Storywriters want AI writers to respect their personal values
    and writing strategies. In Proceedings of the 2022 ACM Designing Interactive Systems Conference. 1209–1227.
                                                                                                                      Manuscript submitted to ACM


--- page break ---

16


 [8] Michelle Brachman, Amina El-Ashry, Casey Dugan, and Werner Geyer. 2024. How knowledge workers use and want to use LLMs in an enterprise
     context. In Extended Abstracts of the CHI Conference on Human Factors in Computing Systems. 1–8.
 [9] Amit Bronner, Matteo Negri, Yashar Mehdad, Angela Fahrni, and Christof Monz. 2012. Cosyne: Synchronizing multilingual wiki content. In
     Proceedings of the Eighth Annual International Symposium on Wikis and Open Collaboration. 1–4.
[10] Creston Brooks, Samuel Eggert, and Denis Peskoff. 2024. The Rise of AI-Generated Content in Wikipedia. arXiv preprint arXiv:2410.08044 (2024).
[11] Susan L Bryant, Andrea Forte, and Amy Bruckman. 2005. Becoming Wikipedian: transformation of participation in a collaborative online
     encyclopedia. In Proceedings of the 2005 ACM international conference on supporting group work. 1–10.
[12] Brian Butler, Elisabeth Joyce, and Jacqueline Pike. 2008. Don’t look now, but we’ve created a bureaucracy: the nature and roles of policies and rules
     in wikipedia. In Proceedings of the SIGCHI conference on human factors in computing systems. 1101–1110.
[13] Kelly Caine. 2016. Local standards for sample size at CHI. In Proceedings of the 2016 CHI conference on human factors in computing systems. 981–992.
[14] Tuhin Chakrabarty, Vishakh Padmakumar, and He He. 2022. Help me write a poem: Instruction tuning as a vehicle for collaborative poetry writing.
     arXiv preprint arXiv:2210.13669 (2022).
[15] John Joon Young Chung, Wooseok Kim, Kang Min Yoo, Hwaran Lee, Eytan Adar, and Minsuk Chang. 2022. TaleBrush: Sketching stories with
     generative pretrained language models. In Proceedings of the 2022 CHI Conference on Human Factors in Computing Systems. 1–19.
[16] Victoria Clarke and Virginia Braun. 2017. Thematic analysis. The journal of positive psychology 12, 3 (2017), 297–298.
[17] Maxime Clément and Matthieu J Guitton. 2015. Interacting with bots online: Users’ reactions to actions of automated programs in Wikipedia.
     Computers in Human Behavior 50 (2015), 66–75.
[18] Dan Cosley, Dan Frankowski, Loren Terveen, and John Riedl. 2007. SuggestBot: using intelligent task routing to help people find work in wikipedia.
     In Proceedings of the 12th international conference on Intelligent user interfaces. 32–41.
[19] Johannes Daxenberger and Iryna Gurevych. 2012. A corpus-based study of edit categories in featured and non-featured Wikipedia articles. In
     Proceedings of COLING 2012. 711–726.
[20] Johannes Daxenberger and Iryna Gurevych. 2013. Automatically classifying edit categories in Wikipedia revisions. In Proceedings of the 2013
     Conference on Empirical Methods in Natural Language Processing. 578–589.
[21] Paramveer S Dhillon, Somayeh Molaei, Jiaqi Li, Maximilian Golub, Shaochun Zheng, and Lionel Peter Robert. 2024. Shaping human-ai collaboration:
     varied scaffolding levels in co-writing with language models. In Proceedings of the 2024 CHI Conference on Human Factors in Computing Systems.
     1–18.
[22] Tawanna R Dillahunt and Amelia R Malone. 2015. The promise of the sharing economy among disadvantaged communities. In Proceedings of the
     33rd annual ACM conference on human factors in computing systems. 2285–2294.
[23] Thomas Erickson and Wendy A Kellogg. 2000. Social translucence: an approach to designing systems that support social processes. ACM transactions
     on computer-human interaction (TOCHI) 7, 1 (2000), 59–83.
[24] Andrea Forte, Niki Kittur, Vanessa Larco, Haiyi Zhu, Amy Bruckman, and Robert E Kraut. 2012. Coordination and beyond: social functions of
     groups in open content production. In Proceedings of the ACM 2012 conference on Computer Supported Cooperative Work. 417–426.
[25] R Stuart Geiger. 2009. The social roles of bots and assisted editing programs. In Proceedings of the 5th International Symposium on Wikis and Open
     Collaboration. 1–2.
[26] R Stuart Geiger. 2018. The lives of bots. arXiv preprint arXiv:1810.09590 (2018).
[27] R Stuart Geiger and Aaron Halfaker. 2013. When the levee breaks: without bots, what happens to Wikipedia’s quality control processes?. In
     Proceedings of the 9th International Symposium on Open Collaboration. 1–6.
[28] R Stuart Geiger and Aaron Halfaker. 2017. Operationalizing conflict and cooperation between automated software agents in wikipedia: A replication
     and expansion of’even good bots fight’. Proceedings of the ACM on human-computer interaction 1, CSCW (2017), 1–33.
[29] R Stuart Geiger and David Ribes. 2010. The work of sustaining order in Wikipedia: The banning of a vandal. In Proceedings of the 2010 ACM
     conference on Computer supported cooperative work. 117–126.
[30] Katy Ilonka Gero and Lydia B Chilton. 2019. Metaphoria: An algorithmic companion for metaphor creation. In Proceedings of the 2019 CHI conference
     on human factors in computing systems. 1–12.
[31] Katy Ilonka Gero, Vivian Liu, and Lydia Chilton. 2022. Sparks: Inspiration for science writing using language models. In Proceedings of the 2022
     ACM Designing Interactive Systems Conference. 1002–1019.
[32] Scott A Hale. 2014. Multilinguals and Wikipedia editing. In Proceedings of the 2014 ACM conference on Web science. 99–108.
[33] Aaron Halfaker and R Stuart Geiger. 2020. Ores: Lowering barriers with participatory machine learning in wikipedia. Proceedings of the ACM on
     Human-Computer Interaction 4, CSCW2 (2020), 1–37.
[34] Aaron Halfaker, R Stuart Geiger, Jonathan T Morgan, and John Riedl. 2013. The rise and decline of an open collaboration system: How Wikipedia’s
     reaction to popularity is causing its decline. American behavioral scientist 57, 5 (2013), 664–688.
[35] Aaron Halfaker, Os Keyes, and Dario Taraborelli. 2013. Making peripheral participation legitimate: reader engagement experiments in wikipedia. In
     Proceedings of the 2013 conference on Computer supported cooperative work. 849–860.
[36] Aaron Halfaker and John Riedl. 2012. Bots and cyborgs: Wikipedia’s immune system. Computer 45, 03 (2012), 79–82.
[37] Eszter Hargittai. 2001. Second-level digital divide: Mapping differences in people’s online skills. arXiv preprint cs/0109068 (2001).
[38] Michael Davis Heather Ford and Marian-Andrei Rizoiu. 2023. Implications of ChatGPT for Knowledge Integrity on Wikipedia. https://meta.
     wikimedia.org/wiki/Research:Implications_of_ChatGPT_for_knowledge_integrity_on_Wikipedia Accessed: 2025-05-01.
Manuscript submitted to ACM


--- page break ---

LLMs in Wikipedia                                                                                                                                     17


[39] Jane Hsieh, Joselyn Kim, Laura Dabbish, and Haiyi Zhu. 2023. " Nip it in the Bud": Moderation Strategies in Open Source Software Projects and the
     Role of Bots. Proceedings of the ACM on Human-Computer Interaction 7, CSCW2 (2023), 1–29.
[40] Fangzhou Jin, Lanfang Sun, Yunqiu Pan, and Chin-Hsi Lin. 2025. High Heels, Compass, Spider-Man, or Drug? Metaphor Analysis of Generative
     Artificial Intelligence in Academic Writing. Computers & Education (2025), 105248.
[41] Charles Kiene, Andrés Monroy-Hernández, and Benjamin Mako Hill. 2016. Surviving an" eternal september" how an online community managed a
     surge of newcomers. In Proceedings of the 2016 CHI Conference on Human Factors in Computing Systems. 1152–1156.
[42] Suin Kim, Sungjoon Park, Scott A Hale, Sooyoung Kim, Jeongmin Byun, and Alice H Oh. 2016. Understanding editing behaviors in multilingual
     Wikipedia. PloS one 11, 5 (2016), e0155305.
[43] Taewan Kim, Donghoon Shin, Young-Ho Kim, and Hwajung Hong. 2024. DiaryMate: Understanding User Perceptions and Experience in Human-AI
     Collaboration for Personal Journaling. In Proceedings of the 2024 CHI Conference on Human Factors in Computing Systems. 1–15.
[44] Aniket Kittur and Robert E Kraut. 2008. Harnessing the wisdom of crowds in wikipedia: quality through coordination. In Proceedings of the 2008
     ACM conference on Computer supported cooperative work. 37–46.
[45] Aniket Kittur and Robert E Kraut. 2010. Beyond Wikipedia: coordination and conflict in online production groups. In Proceedings of the 2010 ACM
     conference on Computer supported cooperative work. 215–224.
[46] Dmitry Kobak, Rita González-Márquez, Emőke-Ágnes Horvát, and Jan Lause. 2024. Delving into ChatGPT usage in academic writing through
     excess vocabulary. arXiv preprint arXiv:2406.07016 (2024).
[47] Narend Kumarana, S Ashwani, and D Vikram. 2011. Wikibhasha: Our experiences with multilingual content creation tool for wikipedia. In
     Proceedings of Wikipedia Conference India, Wikimedia Foundation.
[48] Tzu-Sheng Kuo, Aaron Lee Halfaker, Zirui Cheng, Jiwoo Kim, Meng-Hsin Wu, Tongshuang Wu, Kenneth Holstein, and Haiyi Zhu. 2024. Wikibench:
     Community-driven data curation for ai evaluation on wikipedia. In Proceedings of the 2024 CHI Conference on Human Factors in Computing Systems.
     1–24.
[49] Jean Lave and Etienne Wenger. 1991. Situated learning: Legitimate peripheral participation. Cambridge university press.
[50] Niklas Laxström, Pau Giner, and Santhosh Thottingal. 2015. Content Translation: Computer-assisted translation tool for Wikipedia articles. arXiv
     preprint arXiv:1506.01914 (2015).
[51] Mina Lee, Katy Ilonka Gero, John Joon Young Chung, Simon Buckingham Shum, Vipul Raheja, Hua Shen, Subhashini Venugopalan, Thiemo
     Wambsganss, David Zhou, Emad A Alghamdi, et al. 2024. A design space for intelligent and interactive writing assistants. In Proceedings of the 2024
     CHI Conference on Human Factors in Computing Systems. 1–35.
[52] Mina Lee, Percy Liang, and Qian Yang. 2022. Coauthor: Designing a human-ai collaborative writing dataset for exploring language model capabilities.
     In Proceedings of the 2022 CHI conference on human factors in computing systems. 1–19.
[53] Jun Liu and Sudha Ram. 2011. Who does what: Collaboration patterns in the Wikipedia and their impact on article quality. ACM Transactions on
     Management Information Systems (TMIS) 2, 2 (2011), 1–23.
[54] Teresa Luther, Joachim Kimmerle, and Ulrike Cress. 2024. Teaming up with an AI: Exploring human–AI collaboration in a writing scenario with
     ChatGPT. AI 5, 3 (2024), 1357–1376.
[55] I Scott MacKenzie. 2024. Human-computer interaction: An empirical research perspective. Elsevier Science.
[56] Jim Maddock, Aaron Shaw, and Darren Gergle. 2017. Talking about talk: coordination in large online communities. In Proceedings of the 2017 CHI
     Conference Extended Abstracts on Human Factors in Computing Systems. 1869–1876.
[57] Jonathan T Morgan, Siko Bouterse, Heather Walls, and Sarah Stierch. 2013. Tea and sympathy: crafting positive new user experiences on wikipedia.
     In Proceedings of the 2013 conference on Computer supported cooperative work. 839–848.
[58] Jonathan T Morgan and Aaron Halfaker. 2018. Evaluating the impact of the Wikipedia Teahouse on newcomer socialization and retention. In
     Proceedings of the 14th international symposium on open collaboration. 1–7.
[59] Andy Nguyen, Yvonne Hong, Belle Dang, and Xiaoshan Huang. 2024. Human-AI collaboration patterns in AI-assisted academic writing. Studies in
     Higher Education 49, 5 (2024), 847–864.
[60] Sabine Niederer and José Van Dijck. 2010. Wisdom of the crowd or technicity of content? Wikipedia as a sociotechnical system. New media &
     society 12, 8 (2010), 1368–1387.
[61] Donald A Norman. 1991. Cognitive artifacts. Designing interaction: Psychology at the human-computer interface 1, 1 (1991), 17–38.
[62] Antti Oulasvirta and Kasper Hornbæk. 2016. HCI research as problem-solving. In Proceedings of the 2016 CHI Conference on Human Factors in
     Computing Systems. 4956–4967.
[63] Jennifer Preece and Ben Shneiderman. 2009. The reader-to-leader framework: Motivating technology-mediated social participation. AIS transactions
     on human-computer interaction 1, 1 (2009), 13–32.
[64] Reid Priedhorsky, Jilin Chen, Shyong (Tony) K Lam, Katherine Panciera, Loren Terveen, and John Riedl. 2007. Creating, destroying, and restoring
     value in Wikipedia. In Proceedings of the 2007 ACM international conference on supporting group work. 259–268.
[65] Marissa Radensky, Daniel S Weld, Joseph Chee Chang, Pao Siangliulue, and Jonathan Bragg. 2024. Let’s Get to the Point: LLM-Supported Planning,
     Drafting, and Revising of Research-Paper Blog Posts. arXiv preprint arXiv:2406.10370 (2024).
[66] Dheeraj Rajagopal, Xuchao Zhang, Michael Gamon, Sujay Kumar Jauhar, Diyi Yang, and Eduard Hovy. 2022. One document, many revisions: A
     dataset for classification and description of edit intents. In Proceedings of the Thirteenth Language Resources and Evaluation Conference. 5517–5524.


                                                                                                                          Manuscript submitted to ACM


--- page break ---

18


[67] Miriam Redi, Martin Gerlach, Isaac Johnson, Jonathan Morgan, and Leila Zia. 2020. A taxonomy of knowledge gaps for wikimedia projects (second
     draft). arXiv preprint arXiv:2008.12314 (2020).
[68] Yuqing Ren, Haifeng Zhang, and Robert E Kraut. 2023. How did they build the free encyclopedia? a literature review of collaboration and coordination
     among Wikipedia editors. ACM Transactions on Computer-Human Interaction 31, 1 (2023), 1–48.
[69] Joanne Roberts. 2014. Community and the dynamics of spatially distributed knowledge production: the case of Wikipedia. In The social dynamics of
     innovation networks. Routledge, 179–200.
[70] Dwaipayan Roy, Sumit Bhatia, and Prateek Jain. 2022. Information asymmetry in Wikipedia across different languages: A statistical analysis. Journal
     of the Association for Information Science and Technology 73, 3 (2022), 347–361.
[71] Thorsten Ruprechter, Tiago Santos, and Denis Helic. 2020. On the relation of edit behavior, link structure, and article quality on wikipedia. In
     Complex Networks and Their Applications VIII: Volume 2 Proceedings of the Eighth International Conference on Complex Networks and Their Applications
     COMPLEX NETWORKS 2019 8. Springer, 242–254.
[72] Thorsten Ruprechter, Tiago Santos, and Denis Helic. 2020. Relating Wikipedia article quality to edit behavior and link structure. Applied Network
     Science 5 (2020), 1–20.
[73] Marija Šakota, Isaac Johnson, Guosheng Feng, and Robert West. 2024. Edisum: Summarizing and explaining wikipedia edits at scale. arXiv e-prints
     (2024), arXiv–2404.
[74] Yijia Shao, Yucheng Jiang, Theodore A Kanell, Peter Xu, Omar Khattab, and Monica S Lam. 2024. Assisting in writing wikipedia-like articles from
     scratch with large language models. arXiv preprint arXiv:2402.14207 (2024).
[75] C Estelle Smith, Bowen Yu, Anjali Srivastava, Aaron Halfaker, Loren Terveen, and Haiyi Zhu. 2020. Keeping community in the loop: Understanding
     wikipedia stakeholder values for machine learning-based systems. In Proceedings of the 2020 CHI Conference on Human Factors in Computing Systems.
     1–14.
[76] Ingibergur Stefnisson and David Thue. 2018. Mimisbrunnur: AI-assisted authoring for interactive storytelling. In Proceedings of the AAAI Conference
     on artificial Intelligence and Interactive Digital entertainment, Vol. 14. 236–242.
[77] Igor Steinmacher, Marco Aurelio Graciotto Silva, Marco Aurelio Gerosa, and David F Redmiles. 2015. A systematic literature review on the barriers
     faced by newcomers to open source software projects. Information and Software Technology 59 (2015), 67–85.
[78] Bongwon Suh, Gregorio Convertino, Ed H Chi, and Peter Pirolli. 2009. The singularity is not near: slowing growth of Wikipedia. In Proceedings of
     the 5th international symposium on wikis and open collaboration. 1–10.
[79] Xuemei Tang, Xufeng Duan, and Zhenguang G Cai. 2024. Are LLMs Good Literature Review Writers? Evaluating the Literature Review Writing
     Ability of Large Language Models. arXiv preprint arXiv:2412.13612 (2024).
[80] Yuying Tang, Haotian Li, Minghe Lan, Xiaojuan Ma, and Huamin Qu. 2025. Understanding Screenwriters’ Practices, Attitudes, and Future
     Expectations in Human-AI Co-Creation. arXiv preprint arXiv:2502.16153 (2025).
[81] Milena Tsvetkova, Ruth García-Gavilanes, Luciano Floridi, and Taha Yasseri. 2017. Even good bots fight: The case of Wikipedia. PloS one 12, 2
     (2017), e0171774.
[82] Raphael Velt, Steve Benford, and Stuart Reeves. 2020. Translations and boundaries in the gap between HCI theory and design practice. ACM
     Transactions on Computer-Human Interaction (TOCHI) 27, 4 (2020), 1–28.
[83] Azmine Toushik Wasi, Mst Rafia Islam, and Raima Islam. 2024. Llms as writing assistants: Exploring perspectives on sense of ownership and
     reasoning. In Proceedings of the Third Workshop on Intelligent and Interactive Writing Assistants. 38–42.
[84] Wikimedia. 2025. Strategy/Multigenerational/Artificial intelligence for editors. https://meta.m.wikimedia.org/wiki/Strategy/Multigenerational/
     Artificial_intelligence_for_editors Accessed: 2025-05-06.
[85] Wikipedia. 2024. Wikipedia:Neutral point of view. https://en.wikipedia.org/wiki/Wikipedia:Neutral_point_of_view Accessed: 2025-04-24.
[86] Wikipedia. 2024. Wikipedia:Neutral point of view. https://en.wikipedia.org/wiki/Wikipedia:Neutral_point_of_view Accessed: 2025-04-30.
[87] Wikipedia. 2024. Wikipedia:No original research. https://en.wikipedia.org/wiki/Wikipedia:No_original_research Accessed: 2025-04-30.
[88] Wikipedia. 2024. Wikipedia:Notability. https://en.wikipedia.org/wiki/Wikipedia:Notability Accessed: 2025-04-24.
[89] Wikipedia. 2024. Wikipedia:Verifiability. https://en.wikipedia.org/wiki/Wikipedia:Verifiability Accessed: 2025-04-24.
[90] Wikipedia. 2024. Wikipedia:Verifiability. https://en.wikipedia.org/wiki/Wikipedia:Verifiability Accessed: 2025-04-30.
[91] Ellery Wulczyn, Robert West, Leila Zia, and Jure Leskovec. 2016. Growing wikipedia across languages via recommendation. In Proceedings of the
     25th International Conference on World Wide Web. 975–985.
[92] Diyi Yang, Aaron Halfaker, Robert Kraut, and Eduard Hovy. 2016. Edit categories and editor role identification in Wikipedia. In Proceedings of the
     Tenth International Conference on Language Resources and Evaluation (LREC’16). 1295–1299.
[93] Diyi Yang, Aaron Halfaker, Robert Kraut, and Eduard Hovy. 2016. Who did what: Editor role identification in Wikipedia. In Proceedings of the
     international AAAI conference on web and social media, Vol. 10. 446–455.
[94] Daijin Yang, Yanpeng Zhou, Zhiyuan Zhang, Toby Jia-Jun Li, and Ray Lc. 2022. AI as an Active Writer: Interaction strategies with generated text in
     human-AI collaborative fiction writing. In Joint Proceedings of the ACM IUI Workshops, Vol. 10. CEUR-WS Team, 1–11.
[95] Kaixun Yang, Mladen Raković, Zhiping Liang, Lixiang Yan, Zijie Zeng, Yizhou Fan, Dragan Gašević, and Guanliang Chen. 2025. Modifying AI,
     enhancing essays: How active engagement with generative AI boosts writing quality. In Proceedings of the 15th International Learning Analytics and
     Knowledge Conference. 568–578.
[96] Taha Yasseri, Robert Sumi, András Rung, András Kornai, and János Kertész. 2012. Dynamics of conflicts in Wikipedia. PloS one 7, 6 (2012), e38869.
Manuscript submitted to ACM


--- page break ---

LLMs in Wikipedia                                                                                                                                19


[97] Ann Yuan, Andy Coenen, Emily Reif, and Daphne Ippolito. 2022. Wordcraft: story writing with large language models. In Proceedings of the 27th
     International Conference on Intelligent User Interfaces. 841–852.
[98] Lei Zheng, Christopher M Albano, Neev M Vora, Feng Mai, and Jeffrey V Nickerson. 2019. The roles bots play in Wikipedia. Proceedings of the ACM
     on Human-Computer Interaction 3, CSCW (2019), 1–20.




                                                                                                                      Manuscript submitted to ACM


--- page break ---

## Extraction verification

- **Beginning checked:** rendered PDF page 1 matched the title, three authors, abstract, keywords, placeholder ACM reference, and opening of section 1 in the extraction.
- **Middle checked:** rendered PDF page 10 matched section 4.2.1, the promotional-tone, source-quality, fabrication, and hallucination findings, and the opening of the evaluation, verification, and modification strategies in section 4.2.2.
- **End checked:** rendered PDF page 19 matched the final two references, [97] and [98], and the manuscript footer.
- **Structure checked:** 19 PDF pages; sections 1-6; subsections 2.1-2.3, 3.1-3.3, 4.1-4.3, 5.1-5.3; three research questions; participant Table 1; use-case Table 2; limitations and conclusion; references through [98]; 19 explicit page-boundary markers in this snapshot.
- **Known omissions:** none.

## Preserved attachments

| Path | Role in the source | SHA-256 | Preservation / extraction notes |
|---|---|---|---|
| none | Official PDF was re-fetched and verified during the refresh; the complete embedded text is preserved above | `ceab9a00f3eb70815f40e0ab859e0a812374e58e8505092a0110755faaabb99b` | PDF bytes matched the hash recorded in the prior snapshot; no separate attachment was added because the complete source text is preserved in this snapshot |
