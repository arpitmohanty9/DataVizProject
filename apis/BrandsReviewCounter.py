import json
import time
from os import listdir
from os.path import isfile, join

import pandas as pd

mainJSON = dict()


def get_year(row):
    ts = time.gmtime(row['unixReviewTime'])
    return time.strftime("%Y", ts)


def get_month(row):
    ts = time.gmtime(row['unixReviewTime'])
    return time.strftime("%m", ts)


def create_json(brand_name, brand_file):
    global mainJSON
    df = pd.read_csv(brand_file)
    df['year'] = df.apply(get_year, axis=1)
    df2 = pd.DataFrame({'count': df.groupby(['year']).size()}).reset_index()

    tempdict = dict()

    for index, row in df2.iterrows():
        if row['year'] not in tempdict:
            tempdict[row['year']] = row['count']
        else:
            tempdict[row['year']] += row['count']

    mainJSON[brand_name] = tempdict


if __name__ == "__main__":
    filePath = "../data/brands"
    csvfiles = [f for f in listdir(filePath) if isfile(join(filePath, f)) and ".csv" in f]

    for f in csvfiles:
        create_json(f.split(".")[0], join(filePath, f))

    mainJSON = json.dumps(mainJSON)
    with open("../data/yearlyReview.json", "w") as f:
        f.write(mainJSON)
