# Perplexity, burstiness, and statistical AI detection

- **Canonical URL:** https://gptzero.me/news/perplexity-and-burstiness-what-is-it/
- **Alternate access URLs:**
  - https://gptzero.ghost.io/news/ghost/api/content/posts/slug/perplexity-and-burstiness-what-is-it/?key=214964ff1db1759572e87d5dc4&include=authors,tags
- **Author / owner:** Edward Tian / GPTZero
- **Publisher:** GPTZero
- **Published:** 2023-03-01T00:07:00.000-05:00
- **Retrieved:** 2026-07-15
- **Stable identifier:** Ghost post 64aa3ff8ad12370001cbc4be; UUID c2c9760b-4ff6-4aa1-9eb6-50ab81ed609d
- **Version / revision:** updated 2025-10-13T21:09:00.000-04:00
- **Extraction method:** first-party Ghost Content API HTML field converted to Markdown; direct HTML and rendered-page text cross-checked
- **Full-text status:** complete
- **Access and transformation notes:** Public Ghost API returned the complete ten-paragraph article body, one figure, and four body links. HTML tags were converted to Markdown while preserving the text, link destinations, figure URL, and caption. Navigation, sharing controls, author biography, recommendations, and footer were excluded as page chrome. The figure pixels were not copied because the caption identifies it as a television screenshot that supplies no substantive claim; its source URL is preserved below.

## Full text

In January, we released GPTZero’s first AI detection model publicly for everyone. The demand was deafening — with seven million views and half million users in the first week, GPTZero was called Hero of the Week on UK radio, internationally covered, in Japan, France, Australia and over thirty countries, even landing a feature on the front page of the NYT.

The thesis was simple — build a model that is efficient and effective, and make it accessible to every person who needs it. To do so, the original GPTZero model applied a ‘statistical approach’, leveraging academic research in natural language processing to convert written words to numbers for calculation.

Today, the first principles from GPTZero’s original detection model is still being applied widely. These methods are efficient — leveraging numerical analysis instead of deep text analysis. They are the least computationally expensive of AI detection methods. Additionally, they are actually the main applications behind dozens of other [AI detector](https://gptzero.me/) apps including ZeroGPT, Copyleaks, Originality, and Writer[dot]AI. They remain effective — and as such act as one of the [seven ‘indicators’](https://gptzero.me/technology) of the upgraded GPTZero detection model, alongside our novel text search and [deep learning](https://gptzero.me/news/deep-learning-model-updates/) detection approaches.

![Figure 1: Anderson Cooper asking what is perplexity and burstiness](https://storage.ghost.io/c/93/d8/93d84efe-2017-4168-9591-b749ab8330d5/content/images/2023/07/Screen-Shot-2023-07-07-at-10.59.41-PM.png)

*Figure 1: Anderson Cooper asking what is perplexity and burstiness*

**What is Perplexity and Burstiness**

The statistical layer of GPTZero’s AI detection model is composed of a ‘perplexity’ and ‘burstiness’ calculation — together they form the first layer for GPTZero’s AI detection.

You can interpret the perplexities per sentence as a measure of how likely an AI model would have chosen the exact same set of words as found in the document. One aspect of GPTZero’s algorithm uses an AI model similar to language models like ChatGPT to measure the perplexity of the given document.

We’ve trained the AI model to identify when the input text looks very similar to something written by a language model. For example, the sentence, “Hi there, I am an AI _” would most likely be continued by an AI model with the word “assistant”, which would have low perplexity. On the other hand, if the next word that followed was “potato”, then that sentence would have much higher perplexity, and also a greater likelihood of being written by a human. Over the course of hundreds of words, these probabilities compound to give us a clear picture of the origin of this document. There isn’t an absolute scale for perplexity, but generally, a perplexity above 85 is more likely than not from a human source. Here’s a guide with more technical definitions of this measure:

[Perplexity in Language Models. Evaluating language models using the… | by Chiara Campagnola | Towards Data Science](https://towardsdatascience.com/perplexity-in-language-models-87a196019a94)

Burstiness, on the other hand, is a measure of how much writing patterns and text perplexities vary over the entire document. As humans, we have a tendency to vary our writing patterns. Philosophically, our short-term memory activates, and dissuades us from writing similar things twice. Conversely, language models have a significant ‘AI-print’ where they write with a very consistent level of AI-likeness. While a person could easily write an AI-like sentence by accident, people tend to vary their sentence construction and diction throughout a document.

On the other hand, models formulaically use the same rule to choose the next word in the sentence, leading to low burstiness. Compared to other statistical methods for AI detection, burstiness is a key factor unique to GPTZero detector, allowing our models to evaluate long-term-context, and perform better with additional inputs.

## Extraction verification

- **Beginning checked:** The title, byline, publication date, and first three body paragraphs were compared across the first-party Ghost API, direct page HTML, and rendered page. The rendered article begins with the same January-release paragraph and preserves the same paragraph order.
- **Middle checked:** The figure, its caption, the bold “What is Perplexity and Burstiness” subheading, the statistical-layer description, and the two perplexity paragraphs were compared across all three routes. The `assistant` / `potato` example, no-absolute-scale qualification, `above 85` statement, and technical-definition link all match.
- **End checked:** Both burstiness paragraphs were compared across the API, direct HTML, and rendered page. The last sentence on long-term context and additional inputs is present and no article text follows it.
- **Structure checked:** The first-party API HTML has ten `p` elements, one `figure`, and four body `a` elements. The direct page and rendered page preserve the same article sequence. There are no tables, footnotes, appendices, or formal references; one paragraph is a link to a cited technical explainer.
- **Known omissions:** Non-article page chrome and the non-substantive figure pixels. The figure URL and caption are preserved. No substantive article text is omitted.

## Preserved attachments

| Path | Role in the source | SHA-256 | Preservation / extraction notes |
|---|---|---|---|
| none | not applicable | not applicable | The complete substantive article text, link destinations, figure URL, and figure caption are preserved in this snapshot. |
