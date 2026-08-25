# Exercise 1 — Machine Learning in Practice (30 mins)

This is a code-along exercise. Participants to follow along.

## What we're doing and why

Before we talk about LLMs, we're going to run through the core ideas of machine learning on a familiar dataset: the naked mole-rat activity counts from the course data. The goal isn't to learn ML — it's to make the concepts concrete enough that when we say "a language model is trained on text", you know what that actually means.

We'll cover:

**Fitting a model to data.** Given a set of observations, can we find a line (or boundary, or function) that captures the pattern? This is what "fitting" means — adjusting the model until it describes the data well.

**Observed vs predicted.** Once we have a model, we can compare what it predicts to what we actually measured. The gap between them is the error, and minimising that error is what training is doing.

**Iterating to improve performance.** We don't fit a model once and call it done. We try different configurations, different subsets, different parameters, and check each time whether the model does better. This iteration is the "learning" part of machine learning.

**Testing on held-out data.** Here's the critical bit: a model that performs well on the data it was trained on might still be useless. We always hold back some data and test on that — data the model has never seen. If it still performs well, we have evidence it has learnt something general rather than just memorised the training examples.

## From numbers to language

Once we've done this with numbers, we will discuss how the same logic applies to text: given a large collection of documents, a language model learns which words tend to follow which other words. The "held-out test" equivalent is predicting the next word in a sentence the model wasn't trained on. This is, at its core, what an LLM is doing.

That framing will carry us through the rest of the session.
