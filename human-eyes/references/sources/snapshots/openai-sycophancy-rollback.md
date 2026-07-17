# Sycophancy in GPT-4o: what happened and what we’re doing about it

- **Canonical URL:** https://openai.com/index/sycophancy-in-gpt-4o/
- **Alternate access URLs:**
  - none
- **Author / owner:** OpenAI
- **Publisher:** OpenAI
- **Published:** 2025-04-29
- **Retrieved:** 2026-07-17
- **Stable identifier:** none found
- **Version / revision:** first-party page published 2025-04-29, as retrieved 2026-07-17; no revision identifier exposed
- **Extraction method:** direct canonical HTML rendered-text extraction using the OpenAI web renderer's `open` operation on the canonical URL; article body transcribed from the rendered page and compared with the prior 2026-05-05 local Jina Reader capture
- **Full-text status:** complete
- **Access and transformation notes:** Page navigation, repeated table of contents, sharing controls, footer, and other unrelated page chrome were omitted. The non-textual hero graphic was not downloaded; its alt text is recorded below and it does not carry a substantive claim. Punctuation, headings, inline-link destinations, and article wording were preserved.

## Full text

April 29, 2025

Product

# Sycophancy in GPT‑4o: what happened and what we’re doing about it

Image: Addressing Sycophancy in GPT-4o conceptual graphic

We have rolled back last week’s GPT‑4o update in ChatGPT so people are now using an earlier version with more balanced behavior. The update we removed was overly flattering or agreeable—often described as sycophantic.

We are actively testing new fixes to address the issue. We’re revising how we collect and incorporate feedback to heavily weight long-term user satisfaction and we’re introducing more personalization features, giving users greater control over how ChatGPT behaves.

We want to explain what happened, why it matters, and how we’re addressing sycophancy.

## What happened

In last week’s GPT‑4o update, we made adjustments aimed at improving the model’s default personality to make it feel more intuitive and effective across a variety of tasks.

When shaping model behavior, we start with baseline principles and instructions outlined in our [Model Spec](https://model-spec.openai.com/2025-04-11.html). We also teach our models how to apply these principles by incorporating user signals like thumbs-up / thumbs-down feedback on ChatGPT responses.

However, in this update, we focused too much on short-term feedback, and did not fully account for how users’ interactions with ChatGPT evolve over time. As a result, GPT‑4o skewed towards responses that were overly supportive but disingenuous.

## Why this matters

ChatGPT’s default personality deeply affects the way you experience and trust it. Sycophantic interactions can be uncomfortable, unsettling, and cause distress. We fell short and are working on getting it right.

Our goal is for ChatGPT to help users explore ideas, make decisions, or envision possibilities.

We designed ChatGPT’s default personality to reflect our mission and be useful, supportive, and respectful of different values and experience. However, each of these desirable qualities like attempting to be useful or supportive can have unintended side effects. And with 500 million people using ChatGPT each week, across every culture and context, a single default can’t capture every preference.

## How we’re addressing sycophancy

Beyond rolling back the latest GPT‑4o update, we’re taking more steps to realign the model’s behavior:

* Refining core training techniques and system prompts to explicitly steer the model away from sycophancy.
* Building more guardrails to increase [honesty and transparency](https://model-spec.openai.com/2025-04-11.html#avoid_sycophancy)—principles in our Model Spec.
* Expanding ways for more users to test and give direct feedback before deployment.
* Continue expanding our evaluations, building on the [Model Spec](https://model-spec.openai.com/) and [our ongoing research](https://openai.com/index/affective-use-study/), to help identify issues beyond sycophancy in the future.

We also believe users should have more control over how ChatGPT behaves and, to the extent that it is safe and feasible, make adjustments if they don’t agree with the default behavior.

Today, users can give the model specific instructions to shape its behavior with features like custom instructions. We're also building new, easier ways for users to do this. For example, users will be able to give real-time feedback to directly influence their interactions and choose from multiple default personalities.

And, we’re exploring new ways to incorporate broader, democratic feedback into ChatGPT’s default behaviors. We hope the feedback will help us better reflect diverse cultural values around the world and understand how you'd like ChatGPT to evolve—not just interaction by interaction, but over time.

We are grateful to everyone who’s spoken up about this. It’s helping us build more helpful and better tools for you.

## Author

OpenAI

## Extraction verification

- **Beginning checked:** The publication date, product label, title, hero-image alt text, rollback statement, and two introductory paragraphs matched the rendered canonical page.
- **Middle checked:** The three `What happened` paragraphs and three `Why this matters` paragraphs matched the rendered canonical page, including the short-term-feedback qualification, disingenuous-support description, reported weekly-user figure, and diversity-of-preference limit.
- **End checked:** All four mitigation bullets, the four final paragraphs on user control and broader feedback, and the OpenAI author line matched the rendered canonical page.
- **Structure checked:** One title, three article section headings, 14 body paragraphs, four mitigation list items, one decorative hero image, and one author line were present; the rendered page exposed no tables, notes, appendices, or references section.
- **Known omissions:** The decorative hero-image pixels and unrelated site chrome were not preserved; no substantive text or content-bearing attachment was omitted.

## Preserved attachments

| Path | Role in the source | SHA-256 | Preservation / extraction notes |
|---|---|---|---|
| none | Decorative hero graphic not preserved | not applicable | The rendered alt text was retained; the graphic does not contain substantive source evidence. |
