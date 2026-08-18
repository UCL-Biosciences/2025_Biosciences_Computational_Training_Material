# Week 3 - Reproducibility for Computational Health and Wellbeing
We have seen how code, version control and smooth collaboration can go a long way towards having a robust and flexible system for working on computational projects. Today we focus on a few more concepts and skills that will help organise and manage projects, ultimately leading to better and more reproducible science, and less stress for you!

## Learning Objectives
By the end of today, you can:
- organise a coded, version-controlled project into a predictable, reproducible structure
- capture your environment so the analysis reruns later, on other machines, and by someone else
- document a project so future-you or a collaborator can understand it without hours of digging or emails
- use some key UCL systems for data storage and sharing
- share and archive a project as a citable output — GitHub → Zenodo DOI, data to an appropriate repository
- judge what "reproducible and FAIR enough" looks like for your own work, and leave with one concrete change to make

## Plan
| Section | Duration |
|---|---|
| Intro | 20 mins |
| Exercise 1: Rerun test, Structure rescue, What's in the repo | 75 mins |
| Break | 10 mins |
| Exercise 2: Snapshot it, README + Repo→DOI | 65 mins |
| Wrap-up | 10 mins |

## Introduction

### Making our git repositories fully reproducible, shareable projects.
The files we made in week 1 are now fully managed by git (week 2). Now we'll look at how to make the project as reproducible and shareable possible, making the most of UCL systems. These are habits that transfer to any research you do outside of the training series.

### Participant practice
Let's talk about participant experience of reproducibility using this menti quiz. [Link] and QR code:

<!-- QR code placeholder -->

The questions (mostly in case menti doesn't work):
- Where do you store data at UCL?
- How do you share data with colleagues and collaborators?
- Have you ever received a colleague's code/data and struggled to get it running?
- Have you ever tried to get someone else's published results to reproduce, and hit a wall?
- What are the biggest challenges you've faced when trying to redo an analysis or reproduce some results?

### Discuss responses
Chances are, almost everyone in the room has a story for at least one of these. Lack of reproducibility isn't a rare edge case and it affects us in many ways:
- **Yourself** — you lose time re-figuring-out your own past work, and don't have total confidence in the results.
- **Your collaborators/colleagues** — they can't run what you sent them so repeat the exercise and redo it themselves.
- **The wider scientific community** — code that doesn't run can't be used by others. Results that aren't reproducible have limited scientific value.

Today is about closing that gap with some practical steps that will make it easier to manage a complicated project.

### Today's project
You have two options for today, and either is fine:
- **Your W2 repo** — the notebook, data and outputs from the shared dataset you picked. Tidy, but you already know it works.
- **A real project of your own** — more representative of a real project but less predictable end result!

Whichever you choose, work in it for the whole session so you leave with real progress, not a toy example.

## Exercises

We'll build up a picture of *why* each habit matters as we go, using a running "who does this help?" check — yourself, your collaborators, or the wider community. By the end of the session we'll reveal the full picture, built from your answers.

The [first exercise](Exercises_1.md) covers project organisation. The [second exercise](Exercises_2.md) sharing your project and making sure it is reproducible.

## Wrap-up discussion

Here's the "who does this help?" table, built from what came up in the room today:

| Thing | Helps yourself? | Helps collaborators? | Helps community? |
|---|---|---|---|
| Clear project structure | | | |
| Appropriate data storage plan | | | |
| Environment management (conda) | | | |
| Documentation, metadata, file naming | | | |
| Persistent IDs (ORCID, Zenodo DOI) | | | |

### FAIR-enough, not FAIR-perfect
Nobody's project is perfectly FAIR, and that's fine. The question isn't "have I done everything," it's "what's the one thing that would make the biggest difference to my project right now?"

Using the last menti poll, choose which example from today you're most likely to implement in your work — write the README, snapshot the environment, move data to RDSS, tag a release, or something else entirely. [Link]

## What's next
You now have a version-controlled, reproducible, documented, and citable project. Next week, we take it to UCL's HPC cluster — you'll clone this exact repo, rebuild the environment you just captured, and run the analysis as a proper job on someone else's machine. If today's work holds up, it should be a doddle! Let's see!

- Create a new notebook (create a file with `.ipynb` extension) or create a new python script (a file with `.py` extension)
- Add some code, copy an example from [matplotlib gallery](https://matplotlib.org/stable/gallery/index.html)
