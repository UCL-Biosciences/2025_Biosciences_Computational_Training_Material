# Adapted from https://github.com/UCL-ARC/python-novice-gdp-penguins/blob/main/episodes/data/make_penguin_data.py
# Original licence: CC BY 4.0
# Edits tagged with ### EDIT 2025: 
# - make sure each row has a unique row ID
# - add some empty values
# - add some outliers/weird values 
# - split into 2 datasets

# Running this script with the variables below pointing to the appropriate files will produce the palmer_penguin_data.csv file for use in the lesson.
import random
import pandas as pd
import urllib.request

# Path to the file containing names to assign to the penguins
# Names file sourced from: https://github.com/imsky/wordlists/tree/master, Chicago street names.
name_file = urllib.request.urlopen(
    "https://raw.githubusercontent.com/imsky/wordlists/master/names/streets/chicago.txt"
)
potential_names = name_file.read().decode("utf-8").split("\n")
name_file.close()

# Path to the raw .csv Palmer Penguins data
# Palmer penguin data sourced from https://github.com/allisonhorst/palmerpenguins/tree/main
# citation("palmerpenguins")
# >
# > To cite palmerpenguins in publications use:
# >
# >   Horst AM, Hill AP, Gorman KB (2020). palmerpenguins: Palmer
# >   Archipelago (Antarctica) penguin data. R package version 0.1.0.
# >   https://allisonhorst.github.io/palmerpenguins/. doi:
# >   10.5281/zenodo.3960218.
# >
# > A BibTeX entry for LaTeX users is
# >
# >   @Manual{,
# >     title = {palmerpenguins: Palmer Archipelago (Antarctica) penguin data},
# >     author = {Allison Marie Horst and Alison Presmanes Hill and Kristen B Gorman},
# >     year = {2020},
# >     note = {R package version 0.1.0},
# >     doi = {10.5281/zenodo.3960218},
# >     url = {https://allisonhorst.github.io/palmerpenguins/},
# >   }
penguin_file = urllib.request.urlopen(
    "https://raw.githubusercontent.com/allisonhorst/palmerpenguins/main/inst/extdata/penguins_raw.csv"
)
penguin_data = pd.read_csv(penguin_file)
penguin_file.close()

cols_to_drop = sorted(
    [
        "studyName",
        "Region",
        "Island",
        "Stage",
        "Date Egg",
        "Sex",
        "Sample Number",
        "Comments",
        "Delta 15 N (o/oo)",
        "Delta 13 C (o/oo)",
        "Clutch Completion",
    ]
)

penguin_data.drop(cols_to_drop, axis="columns", inplace=True)

# Drop the Latin species name, but keep the species
penguin_data.loc[:, "Species"] = penguin_data.loc[:, "Species"].str.split(n=1).str[0]
# Convert body mass to SI kg
penguin_data.loc[:, "Body Mass (g)"] /= 1000.0
penguin_data.rename(
    columns={
        "Body Mass (g)": "Mass (kg)",
        "Individual ID": "ID",
    },
    inplace=True,
)

# Drop all rows with NaNs so that the lesson doesn't have to deal with those
# penguin_data.dropna(axis="rows", inplace=True) ### EDIT 2025

# Give remaining penguins names
# with open(name_file) as file:
#     potential_names = [line.rstrip() for line in file]
selected_names = random.sample(range(0, len(potential_names)), penguin_data.shape[0])
selected_names = [potential_names[i] for i in selected_names]
penguin_data["name"] = selected_names

# All headers to lowercase
penguin_data.columns = penguin_data.columns.str.lower()
# Order columns alphabetically, but move ID, name, and species to the front
ordered_columns = sorted(penguin_data.columns)
ordered_columns.remove("id")
ordered_columns.remove("species")
ordered_columns.remove("name")
ordered_columns.insert(0, "id")
ordered_columns.insert(1, "name")
ordered_columns.insert(2, "species")
penguin_data = penguin_data[ordered_columns]

## make ids unique: N + 1:len(penguin_data) + 1
penguin_data["id"] = ['N' + str(i) for i in range(1, len(penguin_data) + 1)]  ### EDIT 2025

# Mix up the dataset so that it doesn't appear ordered (so you can't index slice to get all of one species, for example)
penguin_data = penguin_data.sample(frac=1, axis="rows")

# Introduce some empty values randomly ### EDIT 2025
num_empty = int(0.05 * penguin_data.size)  
for _ in range(num_empty):
    rand_row = random.randint(0, penguin_data.shape[0] - 1)
    rand_col = random.randint(3, penguin_data.shape[1] - 1)  # avoid first 3 cols
    penguin_data.iat[rand_row, rand_col] = None

# Introduce some outliers/weird values randomly ### EDIT 2025
num_outliers = int(0.01 * penguin_data.size)  
for _ in range(num_outliers):
    rand_row = random.randint(0, penguin_data.shape[0] - 1)
    rand_col = random.randint(3, penguin_data.shape[1] - 1)  # avoid first 3 cols
    if penguin_data.columns[rand_col] in [
        "bill length (mm)",
        "bill depth (mm)",
        "flipper length (mm)",
        "mass (kg)",
    ]:
        penguin_data.iat[rand_row, rand_col] = random.uniform(1000, 5000)

# list of funky names to introduce randomly ### EDIT 2025
funky_names = ["@@@!!!", "12345", "Penguin_One", "?????", "   ", "N/A"]

for name in funky_names:
    rand_row = random.randint(0, penguin_data.shape[0] - 1)
    penguin_data.iat[rand_row, 1] = name  # name column

# to show that with code we can re run analysis very easily for different datasets ### EDIT 2025
# Split into 2 datasets
half_index = len(penguin_data) // 2
penguin_data_part1 = penguin_data.iloc[:half_index]
penguin_data_part2 = penguin_data.iloc[half_index:]
# Write to data files
penguin_data_part1.to_csv("penguin_data.csv", index=False)
penguin_data_part2.to_csv("penguin_data_v2_final_v2_finalFINAL.csv", index=False)
