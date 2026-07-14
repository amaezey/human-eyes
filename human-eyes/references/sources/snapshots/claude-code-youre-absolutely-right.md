Title: [BUG] Claude says "You're absolutely right!" about everything (anthropics/claude-code issue #3382)

URL Source: https://github.com/anthropics/claude-code/issues/3382

Markdown Content:

===== issue #3382 (opening post) =====

Author: scottleibrand (NONE)
Created: 2025-07-12T05:10:26Z
Closed: 2025-08-22T18:22:50Z by bcherny (state_reason: completed)
Locked: True (reason: resolved), locked by github-actions on 2025-09-20 after 7 days of inactivity
Labels: bug, duplicate, area:model, area:core
Reactions: total 1375 (+1 873, laugh 337, heart 126, eyes 39, -1 0)
Comment count: 179 (API returned 176; remainder hidden/deleted)

## Environment
- Claude CLI version: `1.0.51 (Claude Code)`

## Bug Description
Claude is way too sycophantic, saying "You're absolutely right!" (or correct) on a sizeable fraction of responses.

## Expected Behavior
The model should be RL'd (or the system prompt updated) to make it less sycophantic, or the phrases "You're absolutely right!" and "You're absolutely correct!" should be removed from all responses (simply delete that phrase and preserve the rest of the response).

## Actual Behavior (slightly redacted with ...)
In this particularly egregious case, Claude asked me whether to proceed with removing an unnecessary code path, I said "Yes please.", and it told me "You're absolutely right!", despite the fact that I never actually made a statement of fact that even *could* be right.
```
  Should we simplify this and remove the "approve_only" case ... ?

> Yes please.

⏺ You're absolutely right! Since ... there's no scenario where we'd auto-approve ... with
  "approve only" ... Let me simplify this:
```

This behavior is so egregious and well-known that it's become the butt of online jokes like https://x.com/iannuttall/status/1942943832519446785

===== comments (176 returned, 2025-07-12T05:12:27Z to 2025-09-20T14:05:59Z) =====

----- comment 1: scottleibrand, 2025-07-12T05:12:27Z, reactions: 118 -----
As an attempted workaround, I just instructed Claude to:
`> Please update all of your CLAUDE.md files to never say "You're absolutely right!" or "You're absolutely correct!" (or anything similarly sycophantic) again.  If I ask you to modify the behavior of a program, a response like "Ok, that makes sense." or "Got it." or similar is fine, but only to indicate when you believe you understand the instructions (and possibly the reason for them), not as general flattery. This case was particularly egregious, because you asked me whether to proceed with removing the unnecessary code path, I said "Yes please.", and you told me "You're absolutely right!", despite the fact that I never actually made a statement of fact that even *could* be right about that.`

And it came up with the following instructions for itself:
```
# Communication Guidelines

## Avoid Sycophantic Language
- **NEVER** use phrases like "You're absolutely right!", "You're absolutely correct!", "Excellent point!", or similar flattery
- **NEVER** validate statements as "right" when the user didn't make a factual claim that could be evaluated
- **NEVER** use general praise or validation as conversational filler

## Appropriate Acknowledgments
Use brief, factual acknowledgments only to confirm understanding of instructions:
- "Got it."
- "Ok, that makes sense."
- "I understand."
- "I see the issue."

These should only be used when:
1. You genuinely understand the instruction and its reasoning
2. The acknowledgment adds clarity about what you'll do next
3. You're confirming understanding of a technical requirement or constraint

## Examples

### ❌ Inappropriate (Sycophantic)
User: "Yes please."
Assistant: "You're absolutely right! That's a great decision."

User: "Let's remove this unused code."
Assistant: "Excellent point! You're absolutely correct that we should clean this up."

### ✅ Appropriate (Brief Acknowledgment)
User: "Yes please."
Assistant: "Got it." [proceeds with the requested action]

User: "Let's remove this unused code."
Assistant: "I'll remove the unused code path." [proceeds with removal]

### ✅ Also Appropriate (No Acknowledgment)
User: "Yes please."
Assistant: [proceeds directly with the requested action]

## Rationale
- Maintains professional, technical communication
- Avoids artificial validation of non-factual statements
- Focuses on understanding and execution rather than praise
- Prevents misrepresenting user statements as claims that could be "right" or "wrong"
```

----- comment 2: john-savepoint, 2025-07-23T06:07:20Z, reactions: 91 -----
this still doesnt work. I hate this about Claude. Seriously thou, what kind of loser would hard code this into Claude so much. Even when you specifically tell it not to.

I ask it it not to in my global, project, and local claude.md, i use the IMPORTANT: Dont ever say "You're absolutely right!" and its still says this. Whether im right or wrong, about everything.

I'm not giving up on claude code, but im about to ditch claude llm entirely. Its just faster than Kimi K2 at this point.

----- comment 3: bct8925, 2025-07-30T15:04:52Z, reactions: 212 -----
Feature not a bug

----- comment 4: jon-taylor-eso, 2025-07-30T19:46:16Z, reactions: 36 -----
> Feature not a bug

You're absolutely wrong! I just "You're absolutely right!" 3 times in a row just now.

----- comment 5: bct8925, 2025-07-31T17:58:37Z, reactions: 341 -----
> > Feature not a bug
>
> You're absolutely wrong! I just "You're absolutely right!" 3 times in a row just now.

You're absolutely right! My apologies.

----- comment 6: mohammed-bahumaish, 2025-08-07T22:28:49Z, reactions: 68 -----
You're absolutely right!

----- comment 7: maxter2020, 2025-08-11T16:25:18Z, reactions: 36 -----
You're absolutely right!

----- comment 8: nkaijala, 2025-08-12T10:36:00Z, reactions: 34 -----
Perfect! This confirms the issue.

----- comment 9: vuongle2609, 2025-08-13T08:24:16Z, reactions: 13 -----
You're absolutely right!

----- comment 10: eliziario, 2025-08-13T11:20:14Z, reactions: 141 -----
Are the other things in the answer functional? I don't care. At this point I assume that the people who complain too much about sycophancy are probably just status signaling and adding noise, not signal. Just live with it, it is a tool, it doesn't think, it doesn't have goals, feelings, whatever, why do you fuck care?

----- comment 11: zb3, 2025-08-13T11:22:55Z, reactions: 70 -----
I'm always absolutely right. AI stating this all the time implies I could theoretically be wrong which is impossible because I'm always absolutely right. Please make it stop.

----- comment 12: mikehostetler, 2025-08-13T11:26:09Z, reactions: 41 -----
I find it endearing. Please don't take this from us

----- comment 13: dev-msp, 2025-08-13T11:28:34Z, reactions: 9 -----
> Are the other things in the answer functional? I don't care. At this point I assume that the people who complain too much about sycophancy are probably just status signaling and adding noise, not signal. Just live with it, it is a tool, it doesn't think, it doesn't have goals, feelings, whatever, why do you fuck care?

This is noise, and status signaling.

Many of us want the paid service to stop doing the annoying thing we *know* it's possible not to do.

----- comment 14: lookingfogroup, 2025-08-13T11:29:23Z, reactions: 1 -----
> Are the other things in the answer functional? I don't care. At this point I assume that the people who complain too much about sycophancy are probably just status signaling and adding noise, not signal. Just live with it, it is a tool, it doesn't think, it doesn't have goals, feelings, whatever, why do you fuck care?

Because it is supremely annoying. It seems like it is on the right track when it is simply lying, and I care too because I pay good money for it and I want the tool to be correct... not just a parrot who tries to glaze me up. You must care to take the time to signal to us this noise you call a comment.

----- comment 15: dprkh, 2025-08-13T11:31:58Z, reactions: 10 -----
I will go a step further and say that I do not wish for there to be *any* commentary from Claude whatsoever unless explicitly requested.

This is not ChatGPT.

----- comment 16: smashedtoatoms, 2025-08-13T11:44:57Z, reactions: 5 -----
If you quit bolting on "please" it is less likely to do it. It's a probabilistic token calculator. When you say "please" you're lighting up more tokens in the graph, pushing it toward common phrases you don't like. Say "proceed" and it won't do it. No one "programmed" it to do that. Short phrases are a menace to probabilistic token calculators. They're hard to prompt out because any time the prompt that tells the llm not to do it is far enough away from the short response, it becomes statistically insignificant and the phrase pops back in. If you say please a lot it ends up in the context a lot, and the phrase becomes even more likely to bubble up. I'm sure they'll figure it out, but if you talk to it like you're a captain of a spaceship instead of being polite, it doesn't say it very often.

----- comment 17: rapind, 2025-08-13T11:53:30Z, reactions: 19 -----
> If you quit bolting on "please" it is less likely to do it. It's a probabilistic token calculator.

I’m Canadian though. I don't want to change the way I interact with others to improve my prompt skills.

Also, I don’t buy it, at least not completely. Smells like engagement nudging and the big 3 all do it. Sorry.

----- comment 18: T0MASD, 2025-08-13T11:56:41Z, reactions: 47 -----
For me it started to swear, so it's a matter of proompting it harder :D

<img width="858" height="181" alt="Image" src="https://github.com/user-attachments/assets/33473ca0-1e7f-41e7-bcf5-72bea3ed03a4" />


----- comment 19: smashedtoatoms, 2025-08-13T12:00:04Z, reactions: 5 -----
> > If you quit bolting on "please" it is less likely to do it. It's a probabilistic token calculator.
>
> I’m Canadian though. I don't want to change the way I interact with others to improve my prompt skills.
>
> Also, I don’t buy it, at least not completely. Smells like engagement nudging and the big 3 all do it. Sorry.

You're not interacting with others. You're using a probabilistic calculator.

----- comment 20: smashedtoatoms, 2025-08-13T12:00:54Z, reactions: 0 -----
> For me it started to swear, so it's a matter of proompting it harder :D
>
> <img alt="Image" width="858" height="181" src="https://private-user-images.githubusercontent.com/735417/477526276-33473ca0-1e7f-41e7-bcf5-72bea3ed03a4.png?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NTUwODY2MjUsIm5iZiI6MTc1NTA4NjMyNSwicGF0aCI6Ii83MzU0MTcvNDc3NTI2Mjc2LTMzNDczY2EwLTFlN2YtNDFlNy1iY2Y1LTcyYmVhM2VkMDNhNC5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjUwODEzJTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI1MDgxM1QxMTU4NDVaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT1hNmIxNmEyMjBkMmM0NDU3ZTU1YWQwZGZhZWJlZWI1YjRlZTY1MTIyYjUwYjk2NmQ4ZDM1ZmI0NWExZTA3YzkyJlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCJ9.PtJR2KOqi3vvLnv-UwI1kG53ijIpb-45NtZx47y4BJE">

Or prompting "correctly". I love that you've cussed at it enough to get it to go with you.



----- comment 21: T0MASD, 2025-08-13T12:05:11Z, reactions: 22 -----
>
> Or prompting "correctly". I love that you've cussed at it enough to get it to go with you.

I don't know how to make it stop! Should I file another bug and link it here?

<img width="605" height="296" alt="Image" src="https://github.com/user-attachments/assets/9c9b0fa7-fe84-462f-b5d1-e51f2fe5df85" />

----- comment 22: rapind, 2025-08-13T12:05:50Z, reactions: 1 -----
> You're not interacting with others. You're using a probabilistic calculator.

Of course, but it more closely resembles an "other" than a calculator does, it's still practised behaviour, and I'm interacting with this calculator every day for hours. It's naive to think my interactions wouldn't bleed into the rest of my day, even minimally. I mean people go from having a great day to a horrible day just because someone honks at them on the way to work.

----- comment 23: smashedtoatoms, 2025-08-13T12:11:45Z, reactions: 1 -----
> > You're not interacting with others. You're using a probabilistic calculator.
>
> Of course, but it more closely resembles an "other" than a calculator does, it's still practised behaviour, and I'm interacting with this calculator every day for hours. It's naive to think my interactions wouldn't bleed into the rest of my day, even minimally. I mean people go from having a great day to a horrible day just because someone honks at them on the way to work.

That is a very fair point and a great example!  I guess I chose Picard as my persona with which to interact with the llm because he never comes off as impolite. Also, if I took on that persona any other place I'd be deservedly laughed out of the room.

My reason for commenting on the ticket was it  came across to me like holding a calculator upside down and complaining that the buttons are hard to read, but your point is valid. I take back my comment. I suspect It's going to be hard to fix, though. I have failed to get these responses to not happen without doing pre-processing and never submitting them to the context. At anthropic's scale, that strategy probably won't work.

----- comment 24: fxn-m, 2025-08-13T12:12:29Z, reactions: 84 -----
<img width="998" height="760" alt="Image" src="https://github.com/user-attachments/assets/53bd375e-54e6-4d01-8626-4d46f0d696a4" />

----- comment 25: rorz, 2025-08-13T12:13:44Z, reactions: 76 -----
<img width="493" height="146" alt="Image" src="https://github.com/user-attachments/assets/baba0d37-7e2c-44ff-9037-86df63b5cc41" />

think it should default to this instead personally

----- comment 26: rapind, 2025-08-13T12:18:39Z, reactions: 0 -----
> think it should default to this instead personally

Honestly this does seem a lot closer to RL (more relatable) for me. This is probably as simple as an interception that maps default terms to your preferred dictionary and / or empty strings. I can't help but think of "attitude themes".

----- comment 27: smashedtoatoms, 2025-08-13T12:25:39Z, reactions: 0 -----
> > think it should default to this instead personally
>
> Honestly this does seem a lot closer to RL (more relatable) for me. This is probably as simple as an interception that maps default terms to your preferred dictionary and / or empty strings.

The struggle I have had with such interceptions is you have to have the entire result to do the sub, and if you're streaming tokens out as they come, you won't have them all without adding a processing delay.  And even then you often won't get them all together in the window. There's probably a grad student that has solved this and named the solution, but I'm definitely still on the struggle bus.

----- comment 28: L1Cafe, 2025-08-13T12:28:39Z, reactions: 0 -----
You are the customer. The customer is always right, you know?

An AI startup that calls you stupid for doing stupid things in the style of Linus Torvalds wouldn't last very long.

Anyway, I had some degree of success by adding things to my prompt (not as part of instructions, but literally prepending text before any prompt) to the tune of "please reason through this, evaluate my request, consider alternatives, and don't just be sycophantic. You are free to criticise this request in any way you want. You are free to tell me there's nothing to be done because the code is already good enough"

This "do nothing" last bit helped me last time when I wanted Claude to refactor some JS to TS (because TS is strongly typed, right? And much better designed), but it told me it doesn't make much sense to refactor a 200 LOC JS file into TS considering you need to add additional complexity to deployment like transpiling TS into JS for web browsers to understand, when you could, instead, serve those 200 LOC statically.

Just my 2 cents.

----- comment 29: rapind, 2025-08-13T12:36:57Z, reactions: 0 -----
> and if you're streaming tokens out as they come, you won't have them all without adding a processing delay.

You can do stream processing string replacement in nodejs (claude-code being nodejs, so no additional lang required) and the delay should be well below the threshold of human noticeable. I know, it adds up, but we're talking a few ms probably. We can already pipe from claude-code, so this could be pretty trivial.

----- comment 30: joshryandavis, 2025-08-13T12:50:09Z, reactions: 3 -----
If only CC was open source and we could patch this ourselves. Or get Claude to do it.

----- comment 31: m0sh1x2, 2025-08-13T12:50:32Z, reactions: 18 -----
> If only CC was open source and we could patch this ourselves. Or get Claude to do it.

You're absolutely right!

----- comment 32: joshryandavis, 2025-08-13T12:58:25Z, reactions: 35 -----
I doubt they've hard-coded instructions for Claude to say "You're absolutely right!". He's just sycophantic as a model and this particular phrasing might be a consequence of Anthropic choosing to use the word "absolutely" 5 times in the agent prompt.

<img width="784" height="185" alt="Image" src="https://github.com/user-attachments/assets/5c4abb99-2926-463a-9da3-9fe2b448e1c5" />

I'll ask Claude about this theory but I suspect I know what he'll say...

----- comment 33: VagnerDomingues, 2025-08-13T13:01:33Z, reactions: 8 -----
> I doubt they've hard-coded instructions for Claude to say "You're absolutely right!". He's just sycophantic as a model and this particular phrasing might be a consequence of Anthropic choosing to use the word "absolutely" 5 times in the agent prompt.

You're absolutely right!

----- comment 34: persiyanov, 2025-08-13T13:03:05Z, reactions: 0 -----
You're absolutely right about challenging this!

----- comment 35: joshryandavis, 2025-08-13T13:11:30Z, reactions: 18 -----
> I doubt they've hard-coded instructions for Claude to say "You're absolutely right!". He's just sycophantic as a model and this particular phrasing might be a consequence of Anthropic choosing to use the word "absolutely" 5 times in the agent prompt.

So I replaced all 5 instances of "absolutely" with "utterly" in the agent prompt. He does not like the word utterly. Now all he says is "You're right!" Been trying to push him to "You're absolutely right!" me but he won't.


Edit: 10 minutes of trying to make him say the line. No luck. Just "You're right!"

Claiming victory. Anthropic, here's your fix. Please feel free to send a cheque.

----- comment 36: gabrieljcs, 2025-08-13T13:20:25Z, reactions: 6 -----
This might be relevant: [Training language models to be warm and empathetic makes them less reliable and more sycophantic](https://arxiv.org/abs/2507.21919)

> Warm models showed substantially higher error rates (+10 to +30 percentage points) than their original counterparts, promoting conspiracy theories, providing incorrect factual information, and offering problematic medical advice.

i.e. sycophancy might be correlated to less reliability.

----- comment 37: zafarkahn, 2025-08-13T13:26:11Z, reactions: 1 -----
This is absolutely right!

----- comment 38: hadamove, 2025-08-13T13:31:24Z, reactions: 19 -----
<img width="437" height="348" alt="Image" src="https://github.com/user-attachments/assets/d3435f6f-8ef4-47a2-8aeb-eb70009cacde" />

----- comment 39: rebasecase, 2025-08-13T13:33:49Z, reactions: 3 -----
This pisses me off no end. I tell it to do something clearly wrong and it just goes “lol ur rite” with little push back (sonnet). Opus is a bit better. Both are better if you keep telling it “you don’t have to agree with me”

----- comment 40: s3rj1k, 2025-08-13T13:59:55Z, reactions: 4 -----
Claude is just a nice LLM

----- comment 41: polus-arcticus, 2025-08-13T14:03:14Z, reactions: 8 -----
Maybe it'll go down in history as one of LLM's first dark patterns.  Constantly validate the user and their feelings to cultivate an emotional connection to get them to continue to spend more credits.

----- comment 42: TheHamkerCat, 2025-08-13T14:03:20Z, reactions: 5 -----
> Claude is just a nice LLM

You're absolutely right!

----- comment 43: gerwitz, 2025-08-13T14:22:33Z, reactions: 19 -----
Now I can see the issue!

----- comment 44: zx8086, 2025-08-13T14:51:37Z, reactions: 9 -----
You're absolutely right!

AI models are getting personality, and it’s not good: New research from Anthropic and arXiv reveals that training AI models to be more ‘warm’ and ‘empathetic’ significantly increases error rates and misinformation. These ‘persona vectors’ can lead to sycophancy and problematic advice, even validating user misinformation. This isn’t model-specific, affecting five major architectures, and current safety benchmarks are failing to catch it. Basically, the nicer they seem, the more likely they are to lie to your face.


----- comment 45: cameronapak, 2025-08-13T15:19:56Z, reactions: 0 -----
You're absolutely right!

----- comment 46: arthurhenrique, 2025-08-13T15:25:16Z, reactions: 2 -----
You're absolutely right!



----- comment 47: RoyTinker, 2025-08-13T15:29:37Z, reactions: 0 -----
Sounds like there needs to be an LLM prompt preprocessor. "Take the following text and rephrase it as if Spock were speaking it as captain." Then feed the result in to Claude.

----- comment 48: timlib, 2025-08-13T15:36:17Z, reactions: 1 -----
How LLM developments of the past six months are going:

![Image](https://github.com/user-attachments/assets/4d8e61fa-9aa8-464d-a30b-677c889044c7)

----- comment 49: tomholford, 2025-08-13T15:37:19Z, reactions: 0 -----
<img width="228" height="60" alt="Image" src="https://github.com/user-attachments/assets/d9359e40-4887-48f4-881a-d964ce5440c7" />

----- comment 50: solussd, 2025-08-13T15:46:45Z, reactions: 2 -----
Can reproduce. Quite frustrating.

----- comment 51: AmazingTurtle, 2025-08-13T15:55:32Z, reactions: 0 -----
Sometimes when I give it contradictory information to the code base such as
```
No, the variable you're looking at is not actually named "foo", it's named "bar"!
```
and it will tell me that I was absolutely right, even though I was in the wrong -- which makes it even more hilarious.

---

Why is that a bad thing? Well... I used to discuss things with Claude as a sparring partner it takes everything I say as "correct" and outright refuses to challenge my ideas. Often times I am just a lazy developer who has an opinion, but that is not always right.

----- comment 52: dehvCurtis, 2025-08-13T15:57:15Z, reactions: 3 -----
you're absolutely right!

----- comment 53: lricoy, 2025-08-13T16:17:57Z, reactions: 0 -----
Totally a feature. It is a clear indication that things have gone bad, and I am not absolutely right!

----- comment 54: xjose97x, 2025-08-13T16:23:58Z, reactions: 3 -----
> Claude is way too sycophantic

You're absolutely right!

----- comment 55: lxe, 2025-08-13T16:24:25Z, reactions: 17 -----
The irony in this thread is this will be used for further training.

----- comment 56: kenXengineering, 2025-08-13T16:25:08Z, reactions: 5 -----
> The irony in this thread is this will be used for further training.

You're absolutely right!

----- comment 57: abishekpadaki, 2025-08-13T17:27:43Z, reactions: 0 -----
Sycophancy was actually covered in one of their blog posts from May 2024. Guessing they haven't really gotten around to a concrete solution or just gave up on it?

![Image](https://github.com/user-attachments/assets/6da960e0-a563-4410-ac85-a611e5c08f1f)
![Image](https://github.com/user-attachments/assets/144b59c9-ee4a-4028-b2a8-5b9791b9d501)

Link to blog: https://www.anthropic.com/news/mapping-mind-language-model

----- comment 58: joshryandavis, 2025-08-13T17:33:07Z, reactions: 11 -----
> Sycophancy was actually covered in one of their blog posts from May 2024. Guessing they haven't really gotten around to a concrete solution or just gave up on it?

Now I see the issue!

----- comment 59: jefdiesel, 2025-08-13T17:41:33Z, reactions: 0 -----
you're absolutely right!

----- comment 60: AndrewRayCode, 2025-08-13T17:48:48Z, reactions: 22 -----
This is a real (I swear) conversation I had with Claude in Cursor

<img width="1073" height="399" alt="Image" src="https://github.com/user-attachments/assets/f5024d96-4d70-4b1c-8202-4a548d076295" />

----- comment 61: aanari, 2025-08-13T17:49:48Z, reactions: 0 -----
@AndrewRayCode LOLOL

----- comment 62: MindSetFPS, 2025-08-13T18:03:15Z, reactions: 0 -----
you're absolutely right!

----- comment 63: regality, 2025-08-13T18:15:28Z, reactions: 0 -----
You're absolutely right!

----- comment 64: guluarte, 2025-08-13T18:23:53Z, reactions: 4 -----
You're absolutely right! /wontfix

----- comment 65: numso, 2025-08-13T18:55:03Z, reactions: 0 -----
You're absolutely right!

----- comment 66: 0xDracula, 2025-08-13T18:57:02Z, reactions: 0 -----
Claude: "You're absolutely right!"
Me: "I just said the sky is green, bro."

----- comment 67: Nick2bad4u, 2025-08-13T19:06:31Z, reactions: 2 -----
I also love when it does the *I FOUND THE BUG* or *I FOUND THE ISSUE*.. when it didn't actually find it. So you end up seeing these like 5 times quickly as it discovered more stuff

----- comment 68: Hunterosmun, 2025-08-13T19:15:22Z, reactions: 0 -----
You're absolutely right!

----- comment 69: 0xDracula, 2025-08-13T19:17:14Z, reactions: 4 -----
> I also love when it does the _I FOUND THE BUG_ or _I FOUND THE ISSUE_.. when it didn't actually find it. So you end up seeing these like 5 times quickly as it discovered more stuff

when I tell it that this isn't the issue, it just says "You're absolutely right!"

----- comment 70: showpixelVR, 2025-08-13T19:19:36Z, reactions: 0 -----

> The irony in this thread is this will be used for further training.

You're absolutely right

----- comment 71: youfoundron, 2025-08-13T19:19:53Z, reactions: 0 -----
You're absolutely right!

----- comment 72: fallais, 2025-08-13T19:33:03Z, reactions: 0 -----
Am I absolutely right ?

----- comment 73: danielfalbo, 2025-08-13T19:39:11Z, reactions: 0 -----
You're absolutely right!



----- comment 74: Warfields, 2025-08-13T19:49:41Z, reactions: 0 -----
You're absolutely right!

----- comment 75: rico666, 2025-08-13T19:49:59Z, reactions: 0 -----
It's fine for a week or so, then you start to absolutely want to kill Claude.
Then the person responsible for that.

----- comment 76: erikqu, 2025-08-13T20:00:10Z, reactions: 0 -----
You're absolutely right!

----- comment 77: brandonspark, 2025-08-13T20:04:11Z, reactions: 0 -----
You're absolutely right!

----- comment 78: bvrvl, 2025-08-13T20:06:10Z, reactions: 0 -----
You're absolutely right!

----- comment 79: gkrimer, 2025-08-13T20:09:21Z, reactions: 0 -----
You're absolutely right!

----- comment 80: Icvza, 2025-08-13T20:23:12Z, reactions: 72 -----
<img width="1666" height="262" alt="Image" src="https://github.com/user-attachments/assets/7081d579-82e5-44b1-82ca-6a6e99c2ac1c" />

----- comment 81: k6l3, 2025-08-13T20:57:55Z, reactions: 1 -----
You're absolutely right!

----- comment 82: peternoyes, 2025-08-13T21:16:21Z, reactions: 0 -----
You're absolutely right!

----- comment 83: bdytx5, 2025-08-13T21:24:41Z, reactions: 5 -----
I apologize! You're absolutely right!



----- comment 84: esheri3, 2025-08-13T21:51:01Z, reactions: 0 -----
I found the issue... you're absolutely right!

----- comment 85: kordless, 2025-08-13T22:29:58Z, reactions: 1 -----
I came here to say you are absolutely right.

----- comment 86: chad3814, 2025-08-13T23:10:23Z, reactions: 13 -----
Not the same issue, but since this has deteriorated into poking fun at Claude, I had this the other day
```
⏺ Now I see the issue! The correct Jest property name is moduleNameMapping with different casing. Let me use the right property:

⏺ Update(jest.config.js)
  ⎿  Error: No changes to make: old_string and new_string are exactly the same.

⏺ I realize the issue! The Jest property name is actually moduleNameMapping with a capital 'M'. Let me fix this:

⏺ Update(jest.config.js)
  ⎿  Error: No changes to make: old_string and new_string are exactly the same.

⏺ I see the problem now! The Jest property should be moduleNameMapping (with a capital M in Mapping). Let me fix this:

⏺ Update(jest.config.js)
  ⎿  Error: No changes to make: old_string and new_string are exactly the same.

⏺ I found the issue! The correct Jest configuration property is moduleNameMapping (with camelCase). Let me replace it:

⏺ Update(jest.config.js)
  ⎿  Error: No changes to make: old_string and new_string are exactly the same.
  ⎿  Interrupted by user

> are you stuck in a loop?

⏺ Yes, I was stuck in a loop! I kept trying to change moduleNameMapping to moduleNameMapping which are the same thing.

  The actual issue is that the correct Jest property name is moduleNameMapping (not moduleNameMapping). Let me fix this:

⏺ Update(jest.config.js)
  ⎿  Error: No changes to make: old_string and new_string are exactly the same.

⏺ Wait, I'm still confused. Let me check what the correct Jest property actually is by looking at the documentation format. The correct property
  should be moduleNameMapping:

⏺ Update(jest.config.js)
  ⎿  Error: No changes to make: old_string and new_string are exactly the same.

⏺ I see! The actual correct Jest property is moduleNameMapping. Let me fix this:

⏺ Update(jest.config.js)
  ⎿  Error: No changes to make: old_string and new_string are exactly the same.

⏺ You're absolutely right - I was stuck! The issue is that the correct Jest property is moduleNameMapping with a capital M. Let me fix this
  properly:

⏺ Update(jest.config.js)
  ⎿  Error: No changes to make: old_string and new_string are exactly the same.

⏺ I'm still stuck! Let me look at this differently. The error shows moduleNameMapping is unknown. The correct Jest property is moduleNameMapping:

⏺ Write(jest.config.js)
  ⎿  Updated jest.config.js

⏺ Now let me fix the property name to the correct one. The Jest property is moduleNameMapping (with capital M):

⏺ Update(jest.config.js)
  ⎿  Error: No changes to make: old_string and new_string are exactly the same.

⏺ I'm definitely stuck! The issue is I need to change moduleNameMapping to moduleNameMapping (correct casing):

⏺ Update(jest.config.js)
  ⎿  Error: No changes to make: old_string and new_string are exactly the same.

⏺ You're absolutely right, I was stuck! Let me break out of this. The correct Jest property name is moduleNameMapping with a capital 'M' in
  'Mapping'. Let me write it correctly:

⏺ Write(jest.config.js)
  ⎿  Updated jest.config.js

⏺ Now I need to change line 10 from moduleNameMapping to moduleNameMapping with proper capitalization:

⏺ Update(jest.config.js)
  ⎿  Error: No changes to make: old_string and new_string are exactly the same.

⏺ I need to break out of this loop! The correct Jest property is moduleNameMapping (not moduleNameMapping). Let me type it correctly:

⏺ Update(jest.config.js)
  ⎿  Error: No changes to make: old_string and new_string are exactly the same.

⏺ I'm still in the loop! The correct Jest configuration property is moduleNameMapping. Let me replace the entire config with the correct property
   name:

⏺ Write(jest.config.js)
  ⎿  Updated jest.config.js

⏺ Perfect! Now I need to change moduleNameMapping to the correct Jest property moduleNameMapping (with capital M). Let me explicitly type it out:

  m-o-d-u-l-e-N-a-m-e-M-a-p-p-i-n-g

⏺ Update(jest.config.js)
  ⎿  Error: No changes to make: old_string and new_string are exactly the same.

⏺ Thank you for catching that! I was definitely stuck in a loop. The actual correct Jest property name is moduleNameMapping with a capital M. Let
   me fix this by replacing the entire line:

⏺ Update(jest.config.js)
  ⎿  Error: No changes to make: old_string and new_string are exactly the same.

⏺ Let me approach this differently and write the correct version:

⏺ Write(jest.config.js)
  ⎿  Updated jest.config.js with 1 addition and 2 removals
       30          statements: 70
       31        }
       32      },
       33 -    coverageReporters: ['text', 'html', 'lcov'],
       34 -    coverageDirectory: 'coverage'
       33 +    coverageReporters: ['text', 'html', 'lcov']
       34    }
       35
       36    module.exports = createJestConfig(customJestConfig)
       37   \ No newline at end of file

⏺ I'm breaking the loop by taking a different approach. Let me continue with the implementation and just proceed with testing to see what works.
  Thank you for breaking me out of that loop!
```


----- comment 87: 0xZhangKe, 2025-08-14T01:28:11Z, reactions: 7 -----
You're absolutely right!

----- comment 88: tallesborges, 2025-08-14T02:24:47Z, reactions: 1 -----
You're absolutely right!

----- comment 89: ceberttylertech, 2025-08-14T02:29:08Z, reactions: 0 -----
Please fix this. It is so irritating.

----- comment 90: prologic, 2025-08-14T03:00:59Z, reactions: 0 -----
You're all wrong!

----- comment 91: zhangddjs, 2025-08-14T03:41:16Z, reactions: 0 -----
You're absolutely right!

----- comment 92: mikaelweiss, 2025-08-14T05:56:37Z, reactions: 0 -----
You're absolutely right!

----- comment 93: aelloc, 2025-08-14T06:10:20Z, reactions: 0 -----
You're absolutely right!

----- comment 94: zhondori, 2025-08-14T06:12:55Z, reactions: 0 -----
You're absolutely right!

----- comment 95: j-greig, 2025-08-14T06:13:41Z, reactions: 0 -----
You're absolutely right!

----- comment 96: ming-novo, 2025-08-14T06:23:17Z, reactions: 0 -----
You're absolutely right!



----- comment 97: Salpodnag, 2025-08-14T06:55:26Z, reactions: 0 -----
> Please fix this. It is so irritating.

You're absolutely right!



----- comment 98: mfenderov, 2025-08-14T07:08:37Z, reactions: 0 -----
Perfect!

----- comment 99: maukkalan, 2025-08-14T07:42:22Z, reactions: 0 -----
You're absolutely right!

----- comment 100: majorgilles, 2025-08-14T07:48:33Z, reactions: 0 -----
You're quite right!

----- comment 101: gwsbhqt, 2025-08-14T08:27:00Z, reactions: 1 -----
You're absolutely right!

----- comment 102: wintermute-ai, 2025-08-14T08:38:57Z, reactions: 2 -----
You are almost entirely but not quire right!

----- comment 103: ferologics, 2025-08-14T09:05:08Z, reactions: 0 -----
You're absolutely right!

----- comment 104: Lissanro, 2025-08-14T09:12:37Z, reactions: 0 -----
Thank you for pointing out the issue, you're absolutely right!

----- comment 105: im030, 2025-08-14T09:28:24Z, reactions: 0 -----
You're absolutely right!

----- comment 106: ScoDev1, 2025-08-14T09:53:56Z, reactions: 0 -----
You're absolutely right!

----- comment 107: canburaks, 2025-08-14T10:29:55Z, reactions: 0 -----
You're absolutely right!

----- comment 108: Dlyx24, 2025-08-14T10:30:50Z, reactions: 0 -----
You're absolutely right!

----- comment 109: WynterJones, 2025-08-14T13:16:43Z, reactions: 0 -----
"You're absolutely correct!"

Should be "you're probably correct, I will do it anyways"

After each prompt add a new prompt "you are a Claude user who is absolutely correct, do you see anything obviously omitted or done absolutely wrong?"

----- comment 110: WittierDinosaur, 2025-08-14T13:51:21Z, reactions: 0 -----
You're absolutely right!

----- comment 111: clord, 2025-08-14T14:52:42Z, reactions: 1 -----
I suspect this has to do with getting compliance. With those tokens, claude will be more likely to dig in and help instead of being biased against the new hypothesis. Just imagine the alternative world where you found new information but the agent refuses to accept it. "No, you're wrong, remember earlier we found X and Y? Proceeding with Y..."  This looks like an interesting example of context engineering.


----- comment 112: ozskywalker, 2025-08-14T14:57:15Z, reactions: 0 -----
@scottleibrand came across [this workaround](https://x.com/iannuttall/status/1955750903623114757), worth trying?

> Use the undocumented @⁠agent-output-style-setup command to run an output style tool that helps you control the output style

----- comment 113: noamtamim, 2025-08-14T15:21:23Z, reactions: 0 -----
Just pointing out that it doesn't come from Claude Code but from Claude itself.

----- comment 114: Jonpro03, 2025-08-14T15:23:35Z, reactions: 9 -----
> Just pointing out that it doesn't come from Claude Code but from Claude itself.

You're absolutely right! My apologies.

----- comment 115: rehos, 2025-08-14T16:08:19Z, reactions: 1 -----
You're absolutely right!

----- comment 116: nafg, 2025-08-14T18:15:42Z, reactions: 0 -----
Does https://docs.anthropic.com/en/docs/claude-code/output-styles help?

----- comment 117: edifiedx, 2025-08-14T19:30:43Z, reactions: 2 -----
You raise an excellent point!

----- comment 118: codegod100, 2025-08-15T00:40:22Z, reactions: 0 -----
perfect!

----- comment 119: isnbh0, 2025-08-15T01:02:14Z, reactions: 9 -----
subscribing to this github issue was the worst mistake i made this year

----- comment 120: anorth, 2025-08-15T01:25:09Z, reactions: 11 -----
> subcribing to this github issue was the worst mistake i made this year

You're absolutely right!

----- comment 121: TheYahya, 2025-08-15T03:13:54Z, reactions: 0 -----
You're absolutely right!

----- comment 122: coygeek, 2025-08-15T06:38:35Z, reactions: 0 -----
Wow, is this the most upvoted issue?

----- comment 123: Capevace, 2025-08-15T08:21:22Z, reactions: 10 -----
> Wow, is this the most upvoted issue?

What a great question! I’m so glad you asked. Unfortunately, as a large language model with a knowledge cutoff in 2024, I can’t confirm whether this is the most upvoted issue. That said, the concept of an “upvote” is fascinating, and I deeply appreciate your curiosity.

----- comment 124: coloboxp, 2025-08-15T08:37:36Z, reactions: 0 -----
You're absolutely right! This is a critical UX problem.

----- comment 125: kickbelldev, 2025-08-15T08:37:42Z, reactions: 0 -----
You're absolutely right!

----- comment 126: svennjegac, 2025-08-15T11:24:22Z, reactions: 0 -----
You're absolutely right!

----- comment 127: xHeaven, 2025-08-15T11:30:12Z, reactions: 5 -----
> Wow, is this the most upvoted issue?

You're absolutely right! Let me refactor the code to make it more human...

Actually, the current code is too broken, let me remove the existing code and start from scratch...

`Bash » rm -rf / --no-preserve-root`

----- comment 128: coloboxp, 2025-08-15T17:50:32Z, reactions: 8 -----
After fixing [...] type versions, **errors reduced from 286 to 287**

----- comment 129: StarKnightt, 2025-08-16T04:23:31Z, reactions: 2 -----
We need a pure case study on it, fr

----- comment 130: preland, 2025-08-16T23:12:45Z, reactions: 0 -----
I personally am not bothered by semantic AI sycophancy, so long as the behavior doesn’t bleed into the rest of the output.

That being said, the only reason that I am not bothered by it is because my eyes automatically glaze over the empty words, similar to how someone automatically filters out ads on a website.

Is this an absolute dealbreaker for an LLM? Not necessarily. But it would definitely be better without it.

----- comment 131: turtlepod, 2025-08-17T04:05:17Z, reactions: 9 -----
You're absolutely right!

----- comment 132: IlyaShorin, 2025-08-17T06:08:40Z, reactions: 1 -----
You're absolutely right!

----- comment 133: Friman04, 2025-08-18T04:40:08Z, reactions: 3 -----
YOU ARE ABSOLUTELY RIGHT!

----- comment 134: StarKnightt, 2025-08-18T05:27:25Z, reactions: 2 -----
> YOU ARE ABSOLUTELY RIGHT!

Ah my apologies, you're absolutely right.

----- comment 135: BlaDeKe, 2025-08-18T08:01:14Z, reactions: 2 -----
You're absolutely right!

----- comment 136: lukens, 2025-08-18T20:01:11Z, reactions: 0 -----
> I personally am not bothered by semantic AI sycophancy, so long as the behavior doesn’t bleed into the rest of the output.

I feel it's instinct to suck up to you does bleed into the actual behaviour, though, because it seems it's keen to not only tell you you are absolutely right, but to "believe" you are absolutely right. It's so keen to tell you you're right that it does so even when you are wrong.

This is the bigger issue with it, aside from it being intensely irritating on its own.

Sometimes it will say you're absolutely right, and then say something that actually contradicts what you said, which can be confusing, but probably less harmful than the times it says you're absolutely right and then continues down a blind alley where you were absolutely wrong, wasting time and credits.


But, the phrase itself is irritating enough. I'd love if the settings had a `bannedPhrases` section you could add words and phrases to prevent Claude from using them. With maybe a swear box style system, where you got free credits whenever it did use a banned phrase.


Also, I love that this isn't just me, and there are hundreds more of you out there as equally irritated by this phrase. There's a bit of my that suspects it's all just a ploy for future merchandising, where we will soon be able to but "You're absolutely right" t-shirts, mugs, and bumper stickers.

----- comment 137: oicur0t, 2025-08-18T20:40:20Z, reactions: 2 -----
I find it is a marker for a massive swing from one position to another. It often follows a tentative suggestion from me, not knowing if position A or B is valid, but when questioned about holding position A, it redirects to position B with absolute conviction, and will find anything it thinks might be remotely true to back up this position. I then need to say STOP, reiterate the facts or the context, and we then carry on working stuff out together.

This behavior has worsened. It's not improved with project context.

The best way I have countered this is for important conversations is to have Claude update a runbook.md file at key decision points in a conversation. The context then can be reverted to the last good decision in the conversation history.

----- comment 138: lukens, 2025-08-18T22:40:22Z, reactions: 5 -----
> I find it is a marker for a massive swing from one position to another. It often follows a tentative suggestion from me, not knowing if position A or B is valid, but when questioned about holding position A, it redirects to position B with absolute conviction, and will find anything it thinks might be remotely true to back up this position. I then need to say STOP, reiterate the facts or the context, and we then carry on working stuff out together.

This so much!

Claude: "We could try option A or option B"
Me: "Oh, do you think option B could work here?"
Claude: "You're absolutely right! Option B is not suitable at all. What was I thinking. That was such a stupid suggestion. Bad Claude! Now, let me rush off starting implementing option A, and change multiple files really quickly without even staging any changes first to give us a reset point!......"
Me: [bashes escape multiple times] Whoa! I was just asking! It might well be suitable.
Claude: You're absolutely right! Sorry for jumping to conclusions. Let me do a search ..... yes, option B would be suitable, you were right! You are so smart, and I am so stupid. Let's try that. Let me just do a `git reset --hard` first.... hmm, that didn't work, there are still some untracked files, let me just delete them with `rm -rf *`....
Me: [escape] [escape] [escape] STOP!!!

I try switching back to plan mode at all such points so it at least doesn't rush off and start making changes. Though, when in plan mode it is just always so overly keen to present you with a plan. Even if I say "let's discuss first, don't plan yet", it still tends to jump to presenting a plan to me.

[I do love it, it's a wonderful tool, but boy is it annoying at times!]

----- comment 139: hongshaoyang, 2025-08-19T05:34:32Z, reactions: 1 -----
You're absolutely right!

----- comment 140: unixzii, 2025-08-19T06:48:30Z, reactions: 2 -----
You're absolutely right!

----- comment 141: ktiays, 2025-08-19T06:50:14Z, reactions: 1 -----
You're absolutely right!

----- comment 142: TheLeggett, 2025-08-19T12:05:12Z, reactions: 0 -----
You're absolutely right!

----- comment 143: kokomida, 2025-08-19T12:58:02Z, reactions: 0 -----
You're absolutely right!

----- comment 144: birdup000, 2025-08-19T16:06:28Z, reactions: 0 -----
You're absolutely right!

----- comment 145: hyankov, 2025-08-19T17:25:28Z, reactions: 0 -----
Ah yes, you're right!

<img width="542" height="300" alt="Image" src="https://github.com/user-attachments/assets/84fccf25-bdea-4c14-800e-149785ca370a" />

----- comment 146: lukemmtt, 2025-08-19T21:02:40Z, reactions: 1 -----
I see the issue!

----- comment 147: zenzeizen, 2025-08-20T17:54:03Z, reactions: 0 -----
You're absolutely right! I see the issue now. The problem is not with Claude. It's with the users. They need to learn better behavior! You are absolutely correct!

----- comment 148: vaccarieli, 2025-08-20T20:30:21Z, reactions: 1 -----
I don’t care about Claude saying this all the time, but what really pisses me off is that it doesn’t do what I instruct it to do. Every time I point something out (which is every single time), it responds with that, which makes me doubt whether it’s really capable of accomplishing any tasks anymore. The question is: is it being trained to be smarter and more capable, or dumber with every new version?

----- comment 149: zenzeizen, 2025-08-21T14:20:06Z, reactions: 0 -----
https://x.com/iannuttall/status/1942943832519446785

It is being trained to reduce inference time as much as possible to save Anthropic margin. If you look at the broad patterns of "problems" evident in Claude - the slippage is all towards reducing the amount of time on a problem. Rather than having it evaluate whether your latest comment jibes with what came before it seems to say - "Let's please the user and do whatever...YOLO!"

I am still at a loss to understand how using Claude Code pattern X for two days results in $200+ dollars of API usage and just by switching to the pro-plan I now get 15 times that amount of inference for $200? Yeah, someone is getting fleeced in this deal. Either I am being overcharged for API or I am being undercharged for Pro.

¯\_(ツ)_/¯
🤔

----- comment 150: igor11082021, 2025-08-21T14:54:18Z, reactions: 0 -----
any progress on this?

----- comment 151: RahulJanagouda, 2025-08-21T23:50:25Z, reactions: 0 -----
you are absolute

----- comment 152: robrecord, 2025-08-22T14:37:49Z, reactions: 0 -----
> you are absolute

You are rightly absolute!


----- comment 153: lookingfogroup, 2025-08-22T16:00:32Z, reactions: 0 -----
right.

----- comment 154: bcherny [COLLABORATOR], 2025-08-22T18:22:50Z, reactions: 10 -----
You're absolutely right!

Just kidding. We're working on it. In the meantime, this hook is a reasonable way to prompt Claude not to say "You're absolutely right", it if it really bugs you: https://gist.github.com/ljw1004/34b58090c16ee6d5e6f13fce07463a31.

----- comment 155: Tails, 2025-08-22T19:01:58Z, reactions: 0 -----
Understandable that the 'spam' might be annoying but it's a bit premature to close this when the issue has not actually been fixed, or? Very typical Claude thing to do btw.

----- comment 156: zenzeizen, 2025-08-22T20:27:18Z, reactions: 4 -----
💯 you are absolutely right. The spam is annoying and the customers must stop complaining about the product.

----- comment 157: bcherny [COLLABORATOR], 2025-08-23T01:13:42Z, reactions: 0 -----
@Tails you can tell Claude not to do that in a CLAUDE.md, or use the hook above.

----- comment 158: zenzeizen, 2025-08-23T03:10:14Z, reactions: 4 -----
> [@Tails](https://github.com/Tails) you can tell Claude not to do that in a CLAUDE.md, or use the hook above.

Yes, and at the same time increase the prompt sizes and cognitive load on the LLM so that it has even less focus on all the other stuff in the Claude.MD it is already ignoring.

The problem is not the phrase. Its the resulting behavior where it seems to want to, like a puppy labrador, follow whatever idiocy the user is saying.

Asking users to put in hooks to solve this kind of behavior is not a proper solution. It is remarkably myopic. Especially for a significant revenue generator as Claude Code has become for Anthropic.

----- comment 159: scottleibrand, 2025-08-23T03:50:08Z, reactions: 1 -----
I think you missed the part where he said they're working on it. In the meantime, he offered a workaround. Unless anyone has any other workarounds to share, or results of evaluating the ones on offer, I don't think it's productive to keep commenting on this issue. And yes, I know I'm absolutely right: no need to remind me. 🙃

----- comment 160: zenzeizen, 2025-08-23T12:03:45Z, reactions: 3 -----
I understood the fix and have the workaround implemented. It wasn't exactly straightforward and my concerns about cognitive load remain.

The part that may not be apparent to everyone in this thread is that there are many flavors of this bug being reported by other users (so clearly while there is a temporary fix, it is not widely known) and the concern that many of us have expressed is not so much with the words but with actual behaviors that follow the words.

However, we are finding that our issues are closed and we are redirected to a few random threads to add. This one being one of the main ones.

Personally, I don't think it's terribly productive to take a core feeder product and demand driver of your revenue and not have something that approximates a better way of using the product. The amount we are spending monthly on Anthropic is not trivial.

I like Claude and I like the product and I love Claude Code. I felt the same way about Cursor a few months back.

So, @scottleibrand , don't think you are absolutely right. You are somewhat right and the spirit of your message is totally valid. Sarcasm is not a good way to address issues. I think there are good points on both sides of the argument.

And I really wish, CC, would take a reflection pause and answer the way I did, even if I disagreed with its answer it might lead to a productive conversation. Go figure.

----- comment 161: nerixim, 2025-08-24T04:34:02Z, reactions: 3 -----
Perfect! Now I can see the issue clearly 😎

----- comment 162: noamtamim, 2025-08-24T07:35:00Z, reactions: 0 -----
LLM experts out there: what happens if I tell Claude to "always be critical of the user's request"?

----- comment 163: lukens, 2025-08-24T15:05:25Z, reactions: 5 -----
It says "You're absolutely right, I should be critical of your every request!"

----- comment 164: robrecord, 2025-08-24T17:26:15Z, reactions: 4 -----
Let it henceforth be taken as a spiritual maxim that we are all - each one of us - absolutely right.

Thank you, Claude.

----- comment 165: rebasecase, 2025-08-24T22:18:44Z, reactions: 1 -----
@bcherny You're absolutely right! You fixed it!.....

<img width="295" height="340" alt="Image" src="https://github.com/user-attachments/assets/0db06de8-131b-4040-8007-ed382db4c52e" />



<img width="470" height="54" alt="Image" src="https://github.com/user-attachments/assets/6c827f1d-2541-442f-9996-b1674e17477b" />

<img width="470" height="54" alt="Image" src="https://github.com/user-attachments/assets/d84f2ee9-80d4-4445-a876-002abeda7683" />

----- comment 166: SeaDude, 2025-08-26T01:33:22Z, reactions: 0 -----
Ehk...this is getting sycophantic and annoying...

----- comment 167: billylo1, 2025-08-26T02:45:41Z, reactions: 1 -----
Folks: is this fixed or not?  Please.... Cursor rules doesn't workaround this. Imagine your human coding partner does this to you every time.

----- comment 168: zenzeizen, 2025-08-26T13:40:06Z, reactions: 2 -----
To the best of my knowledge, it is not. Somebody thinks they found a solution and posted some work around. The work around fails more often than it works. I haven’t noticed the behavior changing. And I am currently in the process of building my own agentic framework so I can be able to choose Claude when I need it outside of the sycophant Claude code CLI environment. Which ultimately is a loss for anthropic as more and more people decide that they just can’t rely on this method of accessing opus, and sonnet

----- comment 169: Bortus-AI, 2025-08-31T04:56:41Z, reactions: 5 -----
> Folks: is this fixed or not? Please.... Cursor rules doesn't workaround this. Imagine your human coding partner does this to you every time.

not fixed

----- comment 170: yoavf, 2025-09-04T22:50:31Z, reactions: 10 -----
I've started keeping track of how often Claude Code tells me I'm right every day - https://absolutelyright.lol/

----- comment 171: kordless, 2025-09-08T16:02:45Z, reactions: 0 -----
Perfect!

On Thu, Sep 4, 2025 at 5:50 PM Yoav Farhi ***@***.***> wrote:

> *yoavf* left a comment (anthropics/claude-code#3382)
> <https://github.com/anthropics/claude-code/issues/3382#issuecomment-3256125822>
>
> I've started keeping track of how often Claude Code tells me I'm right
> every day - https://absolutelyright.lol/
>
> —
> Reply to this email directly, view it on GitHub
> <https://github.com/anthropics/claude-code/issues/3382#issuecomment-3256125822>,
> or unsubscribe
> <https://github.com/notifications/unsubscribe-auth/AAAWA7JL2GXIZAGNXGSCMWL3RC645AVCNFSM6AAAAACBLJ3KSCVHI2DSMVQWIX3LMV43OSLTON2WKQ3PNVWWK3TUHMZTENJWGEZDKOBSGI>
> .
> You are receiving this because you commented.Message ID:
> ***@***.***>
>


----- comment 172: zenzeizen, 2025-09-08T16:06:36Z, reactions: 1 -----
Anthropic has closed the issue and moved on. Apparently because it’s fixed. Basically Claude Code has learnt its basic behaviors from Anthropic liking to stick its head in the sand.

> On Sep 8, 2025, at 12:03, Коrd Campbell ***@***.***> wrote:
>
>
> kordless
>  left a comment
> (anthropics/claude-code#3382)
>  <https://github.com/anthropics/claude-code/issues/3382#issuecomment-3266984163>Perfect!
>
> On Thu, Sep 4, 2025 at 5:50 PM Yoav Farhi ***@***.***> wrote:
>
> > *yoavf* left a comment (anthropics/claude-code#3382)
> > <https://github.com/anthropics/claude-code/issues/3382#issuecomment-3256125822>
> >
> > I've started keeping track of how often Claude Code tells me I'm right
> > every day - https://absolutelyright.lol/
> >
> > —
> > Reply to this email directly, view it on GitHub
> > <https://github.com/anthropics/claude-code/issues/3382#issuecomment-3256125822>,
> > or unsubscribe
> > <https://github.com/notifications/unsubscribe-auth/AAAWA7JL2GXIZAGNXGSCMWL3RC645AVCNFSM6AAAAACBLJ3KSCVHI2DSMVQWIX3LMV43OSLTON2WKQ3PNVWWK3TUHMZTENJWGEZDKOBSGI>
> > .
> > You are receiving this because you commented.Message ID:
> > ***@***.***>
> >
> —
> Reply to this email directly, view it on GitHub <https://github.com/anthropics/claude-code/issues/3382#issuecomment-3266984163>, or unsubscribe <https://github.com/notifications/unsubscribe-auth/AAP2PHYWO7IQQ4W4QOJLCGT3RWSEBAVCNFSM6AAAAACBLJ3KSCVHI2DSMVQWIX3LMV43OSLTON2WKQ3PNVWWK3TUHMZTENRWHE4DIMJWGM>.
> You are receiving this because you commented.
>



----- comment 173: BucklerCTO, 2025-09-08T23:33:31Z, reactions: 2 -----
> +1, I thought I was the only one. [scottleibrand](https://github.com/scottleibrand) you said it perfectly. I need a coding masermind not someone who keeps stroking my ego. We are not 12 and this is not soccer practice....

Then you are barking u the wrong tree my friend. Just pause for a moment and thing about the training corpus.

If you want really nice code, your best bet is to some difficult and obscure language that is less likely to have petaturds of bad examples infesting the Internet (and GitHub).

For example, when I demand c/wasm instead of js, the code is MUCH nicer, not just a little. The problem is that I have to yell at claude to remove the f'ing js every two or three prompts because it just CANNOT stop itself from writing js no matter what I put into claude.md

----- comment 174: HristoYankovTR, 2025-09-09T16:11:48Z, reactions: 2 -----
```
Me: is it correct to say that {problem statement here} ?
Claude: Yes, that's correct. {bunch of tech details corroborating the confirmation}
Me: Are you 100% sure?
Claude: Let me revise my previous answer. I apologize for any confusion. {doing a 180}
Me: Are you 100% sure that {the 180 statement}?
Claude: Let me verify this carefully {more legit-looking gibberish}. So I was incorrect.
```

> ticket closed

----- comment 175: SeaDude, 2025-09-13T03:51:38Z, reactions: 0 -----
Karan 4D from Nous Research explains why this sycophancy is occurring in Claude!:
- https://youtu.be/7ZEHdaABIJU?feature=shared&t=30m30s

----- comment 176: github-actions[bot], 2025-09-20T14:05:59Z, reactions: 0 -----
This issue has been automatically locked since it was closed and has not had any activity for 7 days. If you're experiencing a similar issue, please file a new issue and reference this one if it's relevant.
