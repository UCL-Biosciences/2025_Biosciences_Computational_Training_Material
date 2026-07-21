# Week 2 - Git and Github: Reproducibility, Version Control and Collaboration
Last week we saw how code can make our work efficient, robust and repeatable. This week we will look at how we can extend reproducible practice to address a range of common problems, most importantly improving our "computational health and wellbeing". We will look at why we should care about version control and collaborative practice, and how git and github can support that.

## Learning Objectives
Participants will be able to:
- understand what git offers to researchers and what problem(s) it solves
- Set up a git account and start version control for the files from w1
- Make changes and see how history is recorded
- see how you can collaborate with colleagues on a shared repo

## Plan
| Section | Duration |
|---------|----------|
| Intro | 15 mins |
| Exercise 1 | 45 mins |
| Break | 15 mins |
| Exercise 1 (cont.) | 15-30 mins |
| Exercise 2 | 30 mins |
| Break | 15 mins |
| Exercise 2 (cont.) | 15-30 mins |
| Wrap up | 15 mins |

## Introduction

### Version control and collaboration - why bother with git?
Today is about version control and collaborating on shared projects. We start by talking through some relevant challenges we face as researchers and how we might be able to solve them.

### Participant practice
Let's talk about participant experience of version control and collaboration using this menti quiz. [Link](https://www.menti.com/albhakdq3wb9) and QR code:

<img width="200" height="200" alt="qr code for menti - version control and collab" src="https://github.com/user-attachments/assets/f1a91718-202e-426d-a784-06a30dca7796" />

The questions (mostly in case menti doesn't work):
- How do you manage version control in your day-to-day work?
- What challenges do you face related to version control?
- What do you do to manage collaboration on shared files?
- What problems arise when collaboration isn’t smooth?

### Discuss responses
What did the participants say? How many challenges do we face? And how many of them have effective, accessible solutions?

Research code and analysis rarely gets done once and left alone. When you come back to it months later, a collaborator needs to touch it, or a supervisor or reviewer asks "what exactly did you do here?", you encounter two major sets of problems:
- **You lose track of your own work over time** — the final_v2_ACTUALLY_FINAL.py problem. No way to see what changed, why, or to safely revert. Can be difficult and time-consuming to pick out parts of an earlier version.
- **Multiple people can't work on the same thing without collisions** — overwritten files, no record of who did what, no way to review new changes by a colleague.

### Git

Before getting to GitHub, let's see how a collaboration flow works on MS Word

![image](https://hackmd.io/_uploads/r1n291Wf0.png)

When using git there are a couple of differences.
- changes are grouped and can cover multiple files.
- Each set of changes contain a description that's kept in the history (who made the change, why, what and when).
- You can contribute to any public repository, but only the owners of that repository can accept (merge) these changes.
- The review process happens on a "Pull request".

Benefits of using git:
- Version control – easily revisit earlier versions and see changes
- Collaboration – organise work by multiple people on a single document
-	Builds on the traceable, reusable coding discussion last week. Also feeds into FAIR and reproducible science, as we will discuss later.

## Exercises

We'll break this down into two exercises. First for setting a repo up for managing a project, then for collaboration. Participants will use the same files from last week - same data, code and outputs. "Your own data" refers to your files from last week.

The [first](https://github.com/UCL-Biosciences/Biosciences-Computational-Training/blob/prep-2026/workshops/W2_Reproducibility_Git_Conda/Exercise_1.md) will be done individually. You'll set up a repository, add your files and make some recorded changes.

For the [second exercise](https://github.com/UCL-Biosciences/Biosciences-Computational-Training/new/prep-2026/workshops/W2_Reproducibility_Git_Conda), you'll work in pairs/groups to see how we can use github to collaborate on projects.

## Wrap-up discussion

Now your repo has multiple different datasets in it — does the same code/workflow structure make sense for both?
What would this have looked like over email instead?
Why might a branch + PR be safer than uploading straight to main, even without a conflict?

And crucially, git requires some learning; do you think it will be worth it based on what you've seen so far?!

## What's next?
Now you've got a version-controlled, collaboratively-reviewed project with two analyses sitting in it. But version control on its own doesn't guarantee someone else (or future-you) can actually understand or run what's in there. Next week we'll pick up exactly where this leaves off: making sure the code, data, and environment behind a project are genuinely reproducible — for yourself, for collaborators like the one you just worked with, and for the wider research community — using good research data management, FAIR principles, and our institutional storage systems.


