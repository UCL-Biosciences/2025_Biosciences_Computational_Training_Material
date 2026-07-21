# Week 2 - Git and Github: Reproducibility, Version Control and Collaboration
## Learning Objectives

- understand what git offers to researchers and what problem(s) it solves
- Set up a git account and start version control for the files from w1
- Make changes and see how history is recorded
- see how you can collaborate with colleagues on a shared repo

## Plan
| Section | Duration |
|---------|----------|
| Intro | 10 mins |
| Exercise 1 | 45 mins |
| Break | 15 mins |
| Exercise 1 (cont.) | 15-30 mins |
| Exercise 2 | 30 mins |
| Break | 15 mins |
| Exercise 2 (cont.) | 15-30 mins |
| Wrap up | 15 mins |

## GitHub

Before getting to GitHub, let's see how a collaboration flow works on MS Word

![image](https://hackmd.io/_uploads/r1n291Wf0.png)

When using git there are a couple of differences.
- changes are grouped and can cover multiple files.
- Each set of changes contain a description that's kept in the history (who made the change, why, what and when).
- You can contribute to any public repository, but only the owners of that repository can accept (merge) these changes.
- The review process happens on a "Pull request".
 
📦 Our repository for today: [`UCL-Biosciences/FIXME202405-arcgit-workshop`](https://github.com/...FIXME/)

## Exercises

We'll break this down into two exercises. First for setting a repo up for managing a project, then for collaboration.

The [first](https://github.com/UCL-Biosciences/Biosciences-Computational-Training/blob/prep-2026/workshops/W2_Reproducibility_Git_Conda/Exercise_1.md) will be done individually. You'll set up a repository, add your files and make some recorded changes.

For the [second exercise](https://github.com/UCL-Biosciences/Biosciences-Computational-Training/new/prep-2026/workshops/W2_Reproducibility_Git_Conda), you'll work in pairs/groups to see how we can use github to collaborate on projects.

## Wrap-up discussion

Now your repo has multiple different datasets in it — does the same code/workflow structure make sense for both?
What would this have looked like over email instead?
Why might a branch + PR be safer than uploading straight to main, even without a conflict?

And crucially, git requires some learning; do you think it will be worth it based on what you've seen so far?!

## What's next?
Now you've got a version-controlled, collaboratively-reviewed project with two analyses sitting in it. But version control on its own doesn't guarantee someone else (or future-you) can actually understand or run what's in there. Next week we'll pick up exactly where this leaves off: making sure the code, data, and environment behind a project are genuinely reproducible — for yourself, for collaborators like the one you just worked with, and for the wider research community — using good research data management, FAIR principles, and our institutional storage systems.


