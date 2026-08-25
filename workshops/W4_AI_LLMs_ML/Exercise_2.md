# Exercise 2 — Using LLMs Well (90 mins)

This exercise has three parts. Each one follows the same structure: you discuss in pairs first, share via Menti, then we discuss some ideas together.

---

## Part A — Benefits and best uses (30 mins)

### Discuss with your partner (10 mins)

Think about your own research and day-to-day work. Where do you think LLMs are genuinely useful? What have you used them for, or what could you imagine using them for?

Try to be specific — not just "writing" but what kind of writing, for what purpose, at what stage.

### Share (5 mins)

Add your ideas to the Menti poll. [Link]

### What we've found works well (15 mins)

Here are some things that LLMs seem to work well for. Discuss them with your partner (focus on ones you did not discuss initially). Feedback to the group which uses are most suitable and how we can improve results.

---

## Part B — Risks and concerns (30 mins)

### Discuss with your partner (10 mins)

LLMs come with a set of well-documented limitations and risks. Which feel most relevant to you as a researcher?

### Share (5 mins)

Add your biggest concern to the Menti poll. [Link]

### What's worth worrying about (15 mins)

Discuss in groups any of these that seem important but did not come up in the initial discussion:
- Data quality and provenance — where did the training data come from, and does it matter?
- Hallucination — LLMs produce confident, plausible-sounding text that can be factually wrong
- Bias — the model reflects patterns in its training data, including their biases
- Intellectual property — Are the authors of the training data properly acknowledged?
- Reproducibility — will the same prompt give the same answer next week? How can a black box process be reproducible?
- Uncertainty — LLMs don't know what they don't know
---

## Part C — Getting the most out of LLMs (30 mins)

Now for something practical. We're going to use an LLM to interpret the clustering results from the exercise earlier in the session.

### Round 1: the bad prompt (10 mins)

Everyone send this exact prompt to an LLM of your choice along with the PCA plot generated earlier:

> **"I built a model to classify animals into groups based on activity. What does this mean biologically?"**

Note what you get back. Then share your output with your partner. Are they the same? Probably not — and that's the first thing worth noticing.

Let's see how similar the responses are; add one observation to the Menti poll: what did your LLM say, in one sentence? [Link]

### What went wrong?

The prompt isn't obviously terrible. But it's missing almost everything the LLM needs to give a useful answer: what organism, what data, what method, what the clusters actually look like, what question you were trying to answer.

### Round 2: improve it (20 mins)

Now try again, using some of the techniques below. You don't have to use all of them — pick what feels most relevant and see what difference it makes.

**Be specific about what you're asking for.** Instead of "what does this mean", try "give me three possible biological interpretations, in plain language, with one caveat for each."

**Give context about who you are and what you're doing.** What organism? What measurement? What question were you trying to answer?

**Specify a format.** A table? A short paragraph? Bullet points?

**Provide the data description.** The dataset is naked mole-rat activity counts — number of activity events per animal per observation session. You found three clusters with average counts of roughly 5, 12, and 22.

**Iterate.** If the first response isn't quite right, follow up. Ask it to be more cautious, or to focus on a specific aspect, or to consider an alternative explanation.

**Set up a project.** If you're using Claude or ChatGPT, try setting up a project with background context about your research area. How does that change the starting point for the conversation?

Share your improved prompt and output with your partner. What made the biggest difference?

Add your answer to the Menti poll: which technique improved your output the most? [Link]

---

## The bigger point

You've just demonstrated the core skill: not generating AI output, but shaping and evaluating it. A better prompt gets you a better starting point, but you still need to assess whether the interpretation is scientifically defensible — and that's a judgement only you can make.

LLMs are a tool. Like any tool, how well they work depends on how well you use them, and on knowing what they're not suited for. Today you've built the foundation for both.
