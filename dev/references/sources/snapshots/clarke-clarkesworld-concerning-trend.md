# A Concerning Trend

- **Canonical URL:** https://neil-clarke.com/a-concerning-trend/
- **Alternate access URLs:**
  - https://neil-clarke.com/wp-json/wp/v2/posts/3734?_embed=1
  - https://neil-clarke.com/wp-json/wp/v2/media?parent=3734&per_page=100
- **Author / owner:** Neil Clarke
- **Publisher:** Neil Clarke (author's site); post categorised as Clarkesworld Magazine
- **Published:** 2023-02-15; edits dated 2023-02-17 and 2023-02-20
- **Retrieved:** 2026-07-15
- **Stable identifier:** WordPress post 3734
- **Version / revision:** current published post; WordPress `modified` timestamp 2023-02-20T20:04:47; API reports 12 revisions but does not expose them without authentication
- **Extraction method:** direct canonical HTML fetched with `curl`; first-party WordPress REST post and media JSON cross-check; article body parsed with Python 3 and BeautifulSoup 4; all four source images downloaded and visually inspected
- **Full-text status:** complete
- **Access and transformation notes:** The snapshot preserves the complete 19-paragraph WordPress post body, including four image-only paragraphs, while removing site navigation, sidebar, comments, and unrelated page chrome. The three original image alt texts are retained verbatim. The final updated graph has no source alt text; its visible axes and bars are described separately below. Raw HTML, REST JSON, and all four full-resolution source images are preserved as attachments. The unauthenticated revisions endpoint returned HTTP 401, so earlier WordPress revisions were not compared.

## Full text

Since the early days of the pandemic, I’ve observed an increase in the number of spammy submissions to *Clarkesworld*. What I mean by that is that there’s an honest interest in being published, but not in having to do the actual work. Up until recently, these were almost entirely cases of plagiarism, first by replacing the author’s name and then later by use of programs designed to “make it your own.” The latter often results in rather ham-fisted results like this one I received in 2021:

> **Source image alt text:** Sitting on its three years' experience, the fittest Shell was originally the size of more android subliminal observations than any other single subject in the Grandma. Obey three hundred retorts can't even a couple was issued for wages to the apparently that dropped the storage station.
>
> **Preserved image:** `snapshots/attachments/clarke-concerning-trend-plag2.jpg`

These are the same sentences from the original story, “Human Error” by Raymond F. Jones, published in *If (*April 1956).

> **Source image alt text:** During its three years' existence, the first Wheel was probably the subject of more amateur astronomical observations than any other single object in the heavens. Over three hundred reports came in when a call was issued for witnesses to the accident that destroyed the space station.
>
> **Preserved image:** `snapshots/attachments/clarke-concerning-trend-plag1.jpg`

These cases were often easy to spot and infrequent enough that they were only a minor nuisance. Sometimes it would pick up for a month or two, but overall growth was very slow and number of cases stayed low. Anyone caught plagiarizing was banned from future submissions. Some even had the nerve to complain about it. “But I really need the money.”

Towards the end of 2022, there was another spike in plagiarism and then “AI” chatbots started gaining some attention, putting a new tool in their arsenal and encouraging more to give this “side hustle” a try. It quickly got out of hand:

> **Source image alt text:** Graph starts in June 2019 and displays monthly data through February. Minor bars start showing up in April 2020. Mid-21 through Sept 22 are a bit higher, but it starts growing sharply from there out. Where months were typically below 20, it hits 25 in November, 50 in December, over 100 in January, and nearly 350 so far in February 2023.
>
> **Preserved image:** `snapshots/attachments/clarke-concerning-trend-plag3.jpg`

(Note: This is being published on the 15th of February. In 15 days, we’ve more than doubled the total for all of January.)

I’m not going to detail how I know these stories are “AI” spam or outline any of the data I have collected from these submissions. There are some very obvious patterns and I have no intention of helping those people become less likely to be caught. Furthermore, some of the patterns I’ve observed could be abused and paint legitimate authors with the same brush. Regional trends, for example.

What I can say is that the number of spam submissions resulting in bans has hit 38% this month. While rejecting and banning these submissions has been simple, it’s growing at a rate that will necessitate changes. To make matters worse, the technology is only going to get better, so detection will become more challenging. (I have no doubt that several rejected stories have already evaded detection or were cases where we simply erred on the side of caution.)

Yes, there are tools out there for detecting plagiarized and machine-written text, but they are prone to false negatives and positives. One of the companies selling these services is even playing both sides, offering a tool to help authors *prevent* detection. Even if used solely for preliminary scoring and later reviewed by staff, automating these third-party tools into a submissions process would be costly. I don’t think any of the short fiction markets can currently afford the expense.

I’ve reached out to several editors and the situation I’m experiencing is by no means unique. It does appear to be hitting higher-profile “always open” markets much harder than those with limited submission windows or lower pay rates. This isn’t terribly surprising since the websites and channels that promote “write for money” schemes tend to focus more attention on “always open” markets with higher per-word rates.

This might suggest to some that it is in the best interest of a market to have limited submission windows, but I have no doubt that such reprieves would be short-lived. (That, however, might be all some editors need.) Others might seek the safety of solicited submissions or offering private submission opportunities to a narrower set of “known” authors instead of open calls. Editors might even find themselves having to push back on the privacy-minded desire among some authors to provide *less* contact information. Some might resort to blocking submissions from sources that mask their location with a VPN or other services. Taken a step further, others might employ regional bans as a strategy–much as we have seen happen with financial transactions–due to the high percentage of fraudulent submissions coming from those places.

It’s clear that business as usual won’t be sustainable and I worry that this path will lead to an increased number of barriers for new and international authors. Short fiction *needs* these people.

It’s not just going to go away on its own and I don’t have a solution. I’m tinkering with some, but this isn’t a game of whack-a-mole that anyone can “win.” The best we can hope for is to bail enough water to stay afloat. (Like we needed one more thing to bail.)

If the field can’t find a way to address this situation, things will begin to break. Response times will get worse and I don’t even want to think about what will happen to my colleagues that offer feedback on submissions. No, it’s not the death of short fiction (please just stop that nonsense), but it is going to complicate things.

Edit 2/17/2023 — I’ve closed comments on this post. There are plenty of places to have fights about publishing or AI. The world doesn’t need one more.

Edit 2/20/2023 — Submissions spiked this morning–over 50 before noon–so I’ve temporarily closed submissions. Here’s a refreshed version of the above graph:

> **Source image alt text:** none.
>
> **Visual transcription:** Updated June 2019–February 2023 bar chart. The February 2023 bar rises just above 500; the January bar is a little above 100 and the preceding bars retain the earlier low baseline and late-2022 rise. The image supplies no exact February label or underlying data table.
>
> **Preserved image:** `snapshots/attachments/clarke-concerning-trend-shutdown.jpg`

## Extraction verification

- **Beginning checked:** Canonical HTML and WordPress post JSON both begin with the pandemic-era spam description, the paraphraser example, and the paired “Human Error” images in the same order.
- **Middle checked:** Canonical HTML, REST content, and the preserved images agree on the late-2022/February 2023 graph, the 38% statement, the decision to withhold identifying patterns, detector-error cautions, costs, and market comparisons.
- **End checked:** Canonical HTML and REST content both end with the 2023-02-17 comment closure and the 2023-02-20 submission closure followed by the refreshed graph.
- **Structure checked:** The WordPress `content.rendered` field contains 19 `<p>` elements: 15 prose paragraphs and four image-only paragraphs. It contains four images, no article-body links, and no headings. The canonical `<article>` and post JSON match on title, byline, publication date, body order, edits, and images. All four full-resolution images were visually inspected against the source alt text or, for the unlabelled final graph, transcribed directly.
- **Known omissions:** WordPress revision history is inaccessible without authentication. Site chrome and comments are intentionally excluded. No article-body text, image, source alt text, or edit is omitted.

## Preserved attachments

| Path | Role in the source | SHA-256 | Preservation / extraction notes |
|---|---|---|---|
| `snapshots/attachments/clarke-concerning-trend-2026-07-15.html` | Complete canonical rendered page | `9231e15af820bdcfe3834296c0254d36bf9ebd11d22b73b194638025e15fb0f3` | Byte-preserving `curl -L` fetch; includes site chrome plus the single canonical article. |
| `snapshots/attachments/clarke-concerning-trend-wordpress-post-3734-2026-07-15.json` | First-party WordPress post record | `105cabe1ae90768ad08e4244318dfb4d74e95475c21118257e5cccfe48cccfcc` | Complete REST response from post 3734 with `_embed=1`; used to verify post metadata, body structure, and media references. |
| `snapshots/attachments/clarke-concerning-trend-plag2.jpg` | 2021 paraphraser-output excerpt | `0049fc6800a065f9326caca5f9c75fcb72ca95082d63a8760a73182da401dcb3` | Full-resolution 700×382 JPEG downloaded from the source and visually checked against its alt text. |
| `snapshots/attachments/clarke-concerning-trend-plag1.jpg` | Original “Human Error” excerpt | `f9cc7a31129862e45af17999cceee9b9a60d4e199093b9d29e143f69ae562244` | Full-resolution 665×340 JPEG downloaded from the source and visually checked against its alt text. |
| `snapshots/attachments/clarke-concerning-trend-plag3.jpg` | Original June 2019–mid-February 2023 submissions graph | `2afccdc89371b1253c9cbaa50ce85dbf4a73d088b539f680f935620010e628a0` | Full-resolution 998×575 JPEG downloaded and visually checked against its detailed source alt text. |
| `snapshots/attachments/clarke-concerning-trend-shutdown.jpg` | Refreshed graph accompanying the 2023-02-20 update | `62d8803d1a0d1b5f54c49287f5e80fd8c6d5b3f7d4cfcffbe63ebed5619a9cae` | Full-resolution 1026×579 JPEG downloaded and visually inspected; the source supplies no alt text, exact February label, or underlying data. |
