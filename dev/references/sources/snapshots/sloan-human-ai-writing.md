# Writing with the machine

- **Canonical URL:** https://www.robinsloan.com/notes/writing-with-the-machine/
- **Alternate access URLs:**
  - none; the canonical first-party HTML was accessible directly and through a rendered-reader check
- **Author / owner:** Robin Sloan
- **Publisher:** Robin Sloan
- **Published:** May 2016
- **Retrieved:** 2026-07-17
- **Stable identifier:** none found
- **Version / revision:** live first-party HTML retrieved 2026-07-17; HTTP `Last-Modified: Mon, 13 Jul 2026 15:54:04 GMT`; the page exposes no page-specific revision ID
- **Extraction method:** canonical HTML downloaded with `curl`; the complete `<main>` element was inspected and converted to readable Markdown; a rendered-reader view was checked; all three source images were downloaded, hashed, and inspected, including first, middle, and final frames of both animated GIFs
- **Full-text status:** complete
- **Access and transformation notes:** Navigation, newsletter, privacy, and colophon chrome outside `<main>` were excluded. HTML soft hyphens and layout-only thin spaces were removed. Links were retained as Markdown. The three images are preserved byte-for-byte as attachments; concise descriptions below supplement rather than replace them.

## Full text

I made something new: a plugin that provides inline text completions powered by an AI language model.

![Animated rnn-writer example: a writer requests and accepts inline continuations in Atom](https://www.robinsloan.com/img/rnn-example-1.gif)

Building this felt like playing with Lego, except instead of plastic bricks, I was snapping together conveniently-packaged blocks of human intellect and effort.

One block: a recurrent neural network, fruit of the deep learning boom, able to model and generate sequences of characters with spooky verisimilitude. Snap!

Another block: a powerfully extensible text editor. Snap!

Together: responsive, inline “autocomplete” powered by an RNN trained on a corpus of old sci-fi stories.

If I had to offer an extravagant analogy (and I do) I’d say it’s like writing with a deranged but very well-read parrot on your shoulder. Anytime you feel brave enough to ask for a suggestion, you press `tab`, and …

![Animated rnn-writer example: an initial sentence receives strange inline continuations](https://www.robinsloan.com/img/rnn-example-extra.gif)

If you’d like to try it yourself, the code is now available, in two parts:

* [`torch-rnn-server`](https://github.com/robinsloan/torch-rnn-server?utm_source=Robin_Sloan_sent_me) is a server that runs the neural network, accepts snippets of text, and returns “completions” of that text. In truth, it’s just a couple of tiny shims laid beneath Justin Johnson’s indispensable `torch-rnn` project.
* [`rnn-writer`](https://github.com/robinsloan/rnn-writer?utm_source=Robin_Sloan_sent_me) is a package for the Atom text editor that knows how to talk to `torch-rnn-server` and present its completions to the user. I’m also providing an API for folks who want to try this but don’t feel up to the task of running a local server.

You’ll find instructions for both tools on their respective GitHub pages, and if you have difficulties with either, feel free to open an issue or drop me a line.

Mainly, I wanted to share those links, but as long as I’m here I’ll add a few more things: first a note on motivations, then an observation about the deep learning scene, and finally a link to the sci-fi corpus.

## The vision

From my first tinkerings with the [`torch-rnn`](https://github.com/jcjohnson/torch-rnn?utm_source=Robin_Sloan_sent_me) project, generating goofy/spooky text mimicry on the command line, I was struck—almost overwhelmed—by a vision of typing normally in a text editor and then summoning the help of the RNN with a keystroke. (When I say “help,” I mean: less Clippy, more séance.)

After fumbling around for a few weeks and learning five percent of two new programming languages, I had the blocks snapped together; the RNN trained; the vision realized. And then my first hour playing with it was totally deflating. *Huh. Not as cool as I imagined it would be.*

This is an unavoidable emotional waystation in any project, and possibly a crucial one.

As I’ve spent more time with `rnn-writer`, my opinion has—er—reinflated somewhat. I am just so compelled by the notion of a text editor that possesses a deep, nuanced model of … what? Everything you’ve ever written? Everything written by all your favorite authors? By your nemesis? By everyone on the internet? It’s provocative any way you slice it.

I should say clearly: I am absolutely 100% not talking about an editor that “writes for you,” whatever that means. The world doesn’t need any more dead-eyed robo-text.

The animating ideas here are augmentation; partnership; call and response.

The goal is not to make writing “easier”; it’s to make it harder.

The goal is not to make the resulting text “better”; it’s to make it *different*—weirder, with effects maybe not available by other means.

The tools I’m sharing here don’t achieve that goal; their effects are not yet sufficient compensation for the effort required to use them. But! I think they could get there! And if this project has any contribution to make beyond weird fun, I think it might be the simple trick of getting an RNN off the command line and into a text editor, where its output becomes something you can really *work* with.

## Deep scenius

Like any tech-adjacent person, I’d been reading about deep learning for a couple of years, but it wasn’t until a long conversation earlier this year with an old friend (who is eye-poppingly excited about these techniques) that I felt motivated to dig in myself. And, I have to report: it really is a remarkable community at a remarkable moment. Tracking papers on Arxiv, projects on Github, and threads on Twitter, you get the sense of a group of people nearly tripping over themselves to do the next thing—to push the state of the art forward.

That’s all buoyed by a strong (recent?) culture of clear explanation. My excited friend claims this has been as crucial to deep learning’s rise as the (more commonly-discussed) availability of fast GPUs and large datasets. Having benefited from that culture myself, it seems to me like a reasonable argument, and an important thing to recognize.

Here are a couple of resources I found especially useful:

* For getting acquainted with RNNs, the canonical document is Andrej Karpathy’s essay, [The Unreasonable Effectiveness of Recurrent Neural Networks](http://karpathy.github.io/2015/05/21/rnn-effectiveness/?utm_source=Robin_Sloan_sent_me). It’s a really remarkable example of technical communication—deep and detailed but friendly, even playful.
* Google’s [free deep learning course](https://www.udacity.com/course/deep-learning--ud730) is really very good, and it provided a crucial foundation for me. Structured learning: who knew??
* Ross Goodwin's [Adventures in Narrated Reality](https://medium.com/@rossgoodwin/adventures-in-narrated-reality-6516ff395ba3?utm_source=Robin_Sloan_sent_me) brings RNNs into a creative context and doesn't skimp on technical details. I learned some key tricks from Ross's piece.

## 149,326,361 characters

Most of the energy in the deep learning scene is focused on what I’d call “generic” problems, the solutions to which are very broadly useful to a lot of people: image recognition, speech recognition, sentence translation … you get the idea. Many of these problems have associated benchmark challenges, and if your model gets a better score than the reigning champ, you know you’ve done something worthwhile. These challenges all depend on standard datasets. And these … datasets … are … *extremely* boring.

So, a large part of the work (and fun) of applying the deep learning scenesters’ hard-won technical triumphs to weird/fun objectives is tracking down non-standard, non-boring datasets. For me, decisions about the collection and processing of the text corpus have been more consequential than decisions about the RNN’s design and subsequent training.

The corpus I’ve used most is derived from the Internet Archive’s [Pulp Magazine Archive](https://archive.org/details/pulpmagazinearchive): 150MB of *Galaxy* and *IF Magazine*. It’s very noisy, with tons of OCR errors and plenty of advertisements mixed in with the sci-fi stories, but *wow* there is a lot of text, and the RNN seems to thrive on that. I lightly processed and normalized it all, and the combined corpus—now just a huge text file without a single solitary line break—[is available on the Internet Archive](https://archive.org/details/scifi-corpus).

So, in conclusion:

![Lego spaceship instructions, steps 7 through 11](https://www.robinsloan.com/img/lego-ship-instrux.jpg)

Snap. Snap. Snap!

May 2016, Oakland

## Extraction verification

- **Beginning checked:** The live `<main>` title, opening plugin description, first GIF, Lego analogy, two implementation links, and transition into “The vision” were compared with this snapshot.
- **Middle checked:** The full nine-paragraph “The vision” section and the two-paragraph “Deep scenius” discussion were compared with the rendered page; both GIFs were inspected at their first, middle, and final frames.
- **End checked:** “149,326,361 characters,” all three closing prose paragraphs, the Lego image, “Snap. Snap. Snap!”, and “May 2016, Oakland” were compared with the live page.
- **Structure checked:** The live `<main>` contains one `h1`, three `h2` headings, 33 `p` elements (three image-only), two lists with five total items, three images, eight links, and 1,111 whitespace-separated tokens including the title. The prior Jina-derived body and the live HTML body were text-equivalent after removing Markdown/link packaging and HTML soft-hyphen/layout spacing; the similarity ratio was 0.999387, with the visible differences limited to link-spacing and formatting normalization.
- **Image content checked:** The first 13.19-second, 290-frame GIF begins after the writer types `The`; its inspected middle and final frames show accepted highlighted continuations including “The rings of Saturn glittered while the two men looked at each other.” and “They were enemies, but the servo-robots weren't concerned.” The second 10.70-second, 107-frame GIF begins with “The sun rose over the planet's surface.” and shows strange proposed continuations being accepted, rejected, or edited. The still JPEG shows Lego spaceship assembly steps 7 through 11. These are snapshot-review descriptions, not source prose or measured samples.
- **Known omissions:** none from the article body. Site navigation, footer, newsletter, privacy statement, and colophon outside `<main>` are unrelated page chrome and were intentionally excluded.

## Preserved attachments

| Path | Role in the source | SHA-256 | Preservation / extraction notes |
|---|---|---|---|
| `snapshots/attachments/sloan-human-ai-writing-page-2026-07-17.html` | Authoritative first-party HTML | `de0abef943448371f8808274c8f4cda0898a8d5e6156f47e35ba0e623b797f98` | Complete response body downloaded directly; `<main>` supplied the snapshot text and structure counts. |
| `snapshots/attachments/sloan-human-ai-writing-rnn-example-1.gif` | Primary animated tool demonstration | `b35ecf4e72ddf0025eb0efa2b51946292d0a9c7d27bb15dc4d11059796e89e4f` | Original 640×280, 290-frame, 13.19-second GIF preserved; first, middle, and final coalesced frames inspected. |
| `snapshots/attachments/sloan-human-ai-writing-rnn-example-extra.gif` | Secondary animated tool demonstration | `f4d49452d27820e56bf295ced695d702c95534d6f40b093a097f248b8297390b` | Original 640×280, 107-frame, 10.70-second GIF preserved; first, middle, and final coalesced frames inspected. |
| `snapshots/attachments/sloan-human-ai-writing-lego-ship-instrux.jpg` | Closing visual analogy | `bfed9bced7b593d317aac4d30c6b09b683d13f2cbbedeae0c08832a23acef1e7` | Original 640×624 JPEG preserved and visually inspected; steps 7 through 11 are visible. |
