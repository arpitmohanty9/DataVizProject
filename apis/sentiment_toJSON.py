import os
import pandas as pd
import json

path = '../data/brands_sentiment/'

onlyfiles = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f)) and ".csv" in f]

mainJSON = {}

for file in onlyfiles:
    brand = file.split("_")[0]
    print("Processing ", file)
    filepath = os.path.join(path, file)

    df = pd.read_csv(filepath, index_col=None)

    tempJSON = {}
    tempJSON['positive'] = len(df.loc[df['sentiment'] == 1.0])
    tempJSON['negative'] = len(df.loc[df['sentiment'] == -1.0])
    tempJSON['neutral'] = len(df.loc[df['sentiment'] == 0.0])

    mainJSON[brand] = tempJSON

mainJSON = json.dumps(mainJSON)
with open("../data/sentimentCount.json", "w") as f:
    f.write(mainJSON)