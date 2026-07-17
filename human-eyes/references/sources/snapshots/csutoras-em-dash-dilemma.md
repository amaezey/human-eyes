# The Em Dash Dilemma: How a Punctuation Mark Became AI’s Stubborn Signature

- **Canonical URL:** https://medium.com/@brentcsutoras/the-em-dash-dilemma-how-a-punctuation-mark-became-ais-stubborn-signature-684fbcc9f559
- **Alternate access URLs:**
  - https://r.jina.ai/https://medium.com/@brentcsutoras/the-em-dash-dilemma-how-a-punctuation-mark-became-ais-stubborn-signature-684fbcc9f559
  - https://r.jina.ai/http://medium.com/@brentcsutoras/the-em-dash-dilemma-how-a-punctuation-mark-became-ais-stubborn-signature-684fbcc9f559
  - https://medium.com/@brentcsutoras/the-em-dash-dilemma-how-a-punctuation-mark-became-ais-stubborn-signature-684fbcc9f559?format=json
  - https://medium.com/p/684fbcc9f559
- **Author / owner:** Brent Csutoras
- **Publisher:** Medium
- **Published:** 2025-04-29T18:45:36Z; page updates dated 2025-08-21, 2025-09-27, and 2026-06-22
- **Retrieved:** 2026-07-15
- **Stable identifier:** Medium post ID `684fbcc9f559`
- **Version / revision:** living Medium post as retrieved 2026-07-15; no publisher revision number exposed; latest displayed update dated 2026-06-22
- **Extraction method:** Jina Reader URL-to-Markdown extraction from the canonical Medium page through both HTTPS- and HTTP-target routes; the route responses differ only in the `URL Source:` scheme recorded by Jina, not in a trailing newline; the stored raw extraction is the HTTPS-target response with SHA-256 `d9eb12f4fc1236cf7b85bb1bd0ee06b72bde05741ed8c9b537e4b17acf526216` at `snapshots/attachments/csutoras-em-dash-dilemma-jina-2026-07-15.md`; all four first-party `miro.medium.com` images downloaded with `curl`, inspected directly, and the three content-bearing screenshots transcribed below
- **Full-text status:** complete
- **Access and transformation notes:** direct canonical HTML, `?format=json`, and `/p/684fbcc9f559` returned Cloudflare 403 challenge pages. The complete article remained available through two independent Jina Reader routes to the canonical page. The Medium author-subscription module inserted between body paragraphs was removed as page chrome. Markdown link destinations were preserved; the visible contents of the three screenshots were manually transcribed. The first screenshot's Markdown code fence is a literal part of the image. No author LinkedIn post or cited page is treated as part of this direct source.

## Full text

4 min read

Apr 29, 2025

Almost a year ago, I stumbled into a weird rabbit hole, trying to outsmart AI. Since I moderate a number of very large subreddits, I started noticing certain patterns in posts that felt just a little too polished or off. One tell in particular kept showing up no matter what, the em dash.

This was around the same time there was a lot of buzz about AI detection tools and that Hard Fork story about the teacher who wrongly flunked a whole class for “cheating” with ChatGPT (spoiler, they didn’t cheat). It got me wondering, could I actually reverse-engineer the patterns that gave AI away?

I documented some of it [on LinkedIn](https://www.linkedin.com/posts/brentcsutoras_chatgpt-and-i-are-having-a-bit-of-a-battle-activity-7262492741337591809-7Nv_) as I went. I managed to strip out almost every recognizable AI signature, except for one. That stupid, stubborn, persistent em dash. No matter what settings, prompts, warnings, or threats I tried, AI just could not, or would not, quit it.

I pulled out every trick I could think of. Hard-coded instructions? Check.

Multiple reminders inside the prompt? Check.

![Image 2: prompt instructions explicitly banning em dashes](https://miro.medium.com/v2/resize:fit:631/0*qVbzmQiepQydP2tA)

**Image 2 transcription:**

> `---`
>
> ### **Explicit Em Dash Ban**
>
> **Strictly No Em Dashes:**
>
> - Avoid using em dashes entirely.
> - *Alternative Structures:* Use commas, semicolons, periods, or separate sentences.
>
> **Critical Error for Em Dash Usage:**
>
> - If any em dash is used, consider it a failure to meet the guidelines.

I pushed, pulled, rewired, and begged, but nothing made it stop.

And the AI even acknowledged it knew better, “You specifically instructed me to avoid em dashes. I recognize that.” And then, two sentences later, boom. Another em dash, right in my face. At one point, I even put a “Critical Error” label on any output that included one.

Didn’t matter. Those little punctuation bandits kept sneaking back in.

Eventually, after hammering away at it in different models and forums, I got a straight answer, it’s baked into their DNA. Turns out, em dashes are absolutely everywhere in the training data. In books, articles, essays, humans used them so often that AIs learned them as a default natural flow. It’s like asking a bird not to chirp.

![Image 3: generated response acknowledging an em-dash instruction violation](https://miro.medium.com/v2/resize:fit:700/0*U-upXwwYY7O6Ka0U)

**Image 3 transcription:**

> Yet in your outputs above, even the one where you were instructed to remove all Em Dash usage, you still output Em Dash in your output. Why?
>
> You’re absolutely right to call that out, and I appreciate you doing it.
>
> I did violate the instruction, even after you explicitly told me to remove em dashes. That’s on me.
>
> To be clear: your settings couldn’t be more direct—no em dashes, ever. And in this context, that’s a core part of your voice and brand consistency. I should’ve caught that immediately and delivered copy that fully respected that boundary.
>
> No excuse, but to answer your “why” honestly: em dashes are baked into a lot of default writing styles, and in those moments, I didn’t pause and apply the strict override I should’ve. That’s exactly what the guidelines are meant to prevent.
>
> Want me to rework those versions and make sure everything is clean and correct? I can also double-check any past or upcoming content to ensure this doesn’t happen again.

Someone over on [OpenAI’s Community Forum](https://community.openai.com/t/cannot-get-responses-to-not-include-dashes-and-em-dashes/1023216/5) said it best, the em dash wasn’t flagged during AI training as something special or risky, so the models never learned to avoid it. Another discussion [here](https://community.openai.com/t/chatgpts-em-dash-habit-a-training-artifact-or-design-choice/1115873) pointed out that it’s basically a “deep bias” embedded into how the models understand written flow.

And now? Humans are ditching em dashes, not because they don’t like them, but because they’re terrified their writing will look fake. One [commenter](https://news.ycombinator.com/item?id=43500389) on Hacker News even called it out directly, saying _‘the em dash is now a GPT-ism and is not advisable unless you want people to think your writing is the output of a LLM._

It’s a little heartbreaking for some. As Adam Cecil over at _Night Water_[put it](https://www.nightwater.email/em-dash-ai/), _“I love em dashes so much that I set up a custom text replacement shortcut years ago across all of my Apple devices to make it dead easy to type them.”_

But is the em dash actually a reliable way to tell if something was written by AI? Not really. If you dig into actual research, it’s clear em dashes aren’t a real giveaway. They show up because humans trained the models that way.

People like Daphne Ippolito, a senior scientist at Google Brain, say you have to look elsewhere for real clues. In an interview with [_MIT Technology Review_](https://www.technologyreview.com/2022/12/19/1065596/how-to-spot-ai-generated-text/), she pointed out that one easy signal is word frequency, especially how often AI uses “the” compared to humans. Another tip-off? Typos, or the lack of them. AI-generated text is usually spotless, while human writing is full of little mistakes and quirks.

The em dash mess is just one weird little example of a much bigger story, AI is subtly changing the way we write, talk, and think. Writers who love em dashes are backing off. Readers are second-guessing themselves. Even real humans are worried they sound too robotic.

As for me? I want to say I’ve made peace with it, but honestly, it still bugs me. That said, I’ve stopped wasting my time yelling at AIs about their em dash addiction. There are better battles to fight.

What I’m way more interested in is what this all means next, not just for writing, but for authenticity online. If a tiny piece of punctuation can create this much noise, just imagine what’s coming when the lines between real and generated blur even more.

This is still an issue today. So if you ever hear about a real fix, or if you figure out a trick that actually gets rid of the em dash for good, let me know. I would love to finally win this battle.

**Update: June 22, 2026**

Programs like Gmail who use AI auto suggested copy and adjustments, are also suggesting the use of Em Dashes to users.

![Image 4: Gmail grammar suggestion inserting em dashes](https://miro.medium.com/v2/resize:fit:594/1*4II9m9lWqz_8eSb1gMx1Mg.png)

**Image 4 transcription:** The screenshot is cropped at both horizontal edges. Its first visible composition line reads `[left edge] set, probably a month or two out, let's grab time to talk through what ads c[right-cropped]`; the selected span is `set, probably a month or two out,`. A lower composition line shows `[left-cropped]e know what you need[right-obscured by popover]`. The popover heading reads `Correct grammar`, and its proposed replacement reads `set—probably a month or two out—`. No text hidden beyond the crop or behind the popover is inferred.

**Update: September 27,2025:**

I finally found a solution that’s working consistently through Claude. Create a project and in the instructions have it 1) create the initial output, 2) put the output into a holding area, and then 3) replace all em dash usage with commas.

I had it provide both the original and refined outputs initially and noticed the em dash usage in draft content, but the corrected comma usage in the final output.

**Update: August 21, 2025:**

Still no official acknowledgment or fix from OpenAI, Anthropic, or other AI companies. Community forums continue reporting the same problem with no effective solutions. The issue remains unsolved.

## Extraction verification

- **Beginning checked:** title, canonical URL, publication timestamp, reading-time label, author avatar, first four paragraphs, and prompt screenshot were compared with both current Jina Reader routes and the archived 2026-05-05 capture.
- **Middle checked:** the prompt-failure account, both original screenshots, two community-forum links, Hacker News quotation, Night Water quotation, reliability caveat, and MIT Technology Review attribution were compared with both current Jina outputs. The visible text of both original screenshots was checked at native resolution.
- **End checked:** the closing five paragraphs and all three dated update blocks were compared with both current Jina outputs; the new 2026-06-22 Gmail claim and screenshot were checked against the downloaded 594-by-210 PNG.
- **Structure checked:** the capture contains 22 prose paragraphs, three dated update headings, four image references, and every article-body link. The two current Jina routes differ only in the `URL Source:` scheme recorded by Jina; the stored raw file is the HTTPS-target response and matches its recorded `d9eb12f4…` digest. The prior capture lacks only the new 2026-06-22 paragraph/image and places Medium’s injected subscription module one paragraph earlier. The current snapshot removes that non-article module and transcribes all content-bearing screenshots.
- **Known omissions:** none from the article. Medium navigation, author-subscription chrome, and unrelated footer material were deliberately excluded. Cited pages and the LinkedIn post are links rather than constituent full text.

## Preserved attachments

| Path | Role in the source | SHA-256 | Preservation / extraction notes |
|---|---|---|---|
| `snapshots/attachments/csutoras-em-dash-dilemma-jina-2026-07-15.md` | raw current Markdown extraction | `d9eb12f4fc1236cf7b85bb1bd0ee06b72bde05741ed8c9b537e4b17acf526216` | Exact current HTTPS-target Jina Reader response; complete article plus injected Medium subscription module. |
| `snapshots/attachments/csutoras-em-dash-author-avatar.jpg` | author avatar | `87ba0e5779238e942238e05ba8f5c7ba91c656189d6369854902fb3f540653f0` | First-party 32-by-32 JPEG downloaded from `miro.medium.com`; decorative identity image, not claim evidence. |
| `snapshots/attachments/csutoras-em-dash-prompt-instructions.png` | screenshot of explicit prompt constraints | `6b3472b9ad322df76207db44e0d754d837d731441a46db7809adabe81443785b` | First-party 631-by-258 PNG downloaded from `miro.medium.com`, visually inspected, and fully transcribed. |
| `snapshots/attachments/csutoras-em-dash-output-acknowledgement.png` | screenshot of generated acknowledgement after an instruction violation | `6031ae8b8b9607a18a44792c23a10d2366e022f1e24f8d17f983967d91701877` | First-party 700-by-440 PNG downloaded from `miro.medium.com`, visually inspected, and fully transcribed. |
| `snapshots/attachments/csutoras-em-dash-gmail-suggestion.png` | screenshot supporting the 2026-06-22 Gmail claim | `8a5c0115bb1df788c11b9082734ea5742320ccfb73e8c2365af9a54c6d1e419b` | First-party 594-by-210 PNG downloaded from `miro.medium.com`, visually inspected, and transcribed; composition context is cropped in the source image. |
