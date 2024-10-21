"""

Example call:

python data_prep/prep_names_dataset.py

"""

import random
import pandas as pd

seed = 42

def read_file(file):
    with open(file, 'r', encoding='utf8') as f:
        return f.read().splitlines()

boys = read_file("./data/first_boys.txt")
girls = read_file("./data/first_girls.txt")
# pd.read_csv("first_girls.txt", header=None, names=["female"])['female'].to_list()

def sample_name(sex):
    if sex == 0:
        return random.choice(boys)
    else:
        return random.choice(girls)

names = pd.read_csv("./data/last.txt", header=None, names=["last"]).sample(
    1000, random_state=seed
)

names["sex"] = names.apply(lambda x: random.choice([0, 1]), axis=1)
names["first"] = names["sex"].apply(lambda x: sample_name(x))
names["middle"] = names["sex"].apply(lambda x: sample_name(x))

names = names[["first", "middle", "last"]]

names.to_csv("./data/names.csv", index=False, header=True)
