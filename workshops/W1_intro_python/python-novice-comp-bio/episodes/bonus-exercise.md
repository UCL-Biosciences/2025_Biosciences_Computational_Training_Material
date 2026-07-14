# Bonus exercise - yay!

It is amazing how often we misuse the word final in research. Final datasets, final documents, final pipelines - do you ever really believe they are genuinely the "final" version?

A common situation is to receive updated data from colleagues after we have performed a lengthy analysis. If you have not used a reusable and reproducible analysis, this means starting from the beginning! If you have done all your analysis with code, re-running the analysis can be very simple.

That is what we will look at in this final exercise.

## Data disaster!
You have done a lengthy analysis and just before you send the results to collaborators, a colleague emails to say "wait! Just found a big error in the original data! Use the attached file instead!". Luckily, all our analysis was done in jupyter notebooks and re-running the analysis should be straight forward. Simply change the file that is loaded at the start  of notebook two (or where ever you load in the data) and run the cells again. It should run all the way through but it is worth checking the output carefully to make sure the data are what you expect, columns have not changed name or data type, etc. 

## Ultimate flexibility 🤸🏻‍♀️
If you want to further test the flexibility of your work, try running a different dataset completely. There are several options in the data folder. This time, you'll need to change a few more things: the file you load, the column names for plots and stats, the name of the output. What else?

## Takeaway
Once you have set up code that works and is written flexibly, it becomes much easier, quicker, and less risky to re-run analysis. This is a huge benefit of using code-based analyses and is a common incentive for wanting to learn to code.

