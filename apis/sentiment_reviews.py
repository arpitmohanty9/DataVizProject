import csv
import os

import nltk
import pandas as pd
from nltk.sentiment.vader import SentimentIntensityAnalyzer

folder = '../data/brands'

from os import listdir
from os.path import isfile, join

onlyfiles = [f for f in listdir(folder) if isfile(join(folder, f))]

for file in onlyfiles:
    print("Processing ", file)
    filepath = os.path.join(folder, file)
    # data = pd.read_csv(filepath)

    df = pd.DataFrame.from_csv(filepath, index_col=None)
    # df2 = pd.DataFrame(data = df['reviewText'],index = None)
    df2 = pd.DataFrame(data=df['reviewText'], index=None)

    default_value = 0
    df2.assign(sentiment=default_value)

    sid = SentimentIntensityAnalyzer()

    for row in df2.itertuples():
        review = df2.at[row.Index, 'reviewText']
        try:
            sentences = nltk.tokenize.sent_tokenize(review)
            sentiment_value = 0
            for sentence in sentences:
                sentiment_score = sid.polarity_scores(sentence)
                if sentiment_score["compound"] == 0.0:
                    sentiment_value += 0.0
                elif sentiment_score["compound"] > 0.0:
                    sentiment_value += 1
                else:
                    sentiment_value -= 1

            if sentiment_value == 0:
                df2.at[row.Index, 'sentiment'] = sentiment_value
            elif sentiment_value > 0:
                df2.at[row.Index, 'sentiment'] = 1
            else:
                df2.at[row.Index, 'sentiment'] = -1
        except Exception as ex:
            pass

    df = df.join(df2.set_index('reviewText'), on='reviewText')

    ofile = '../data/brands_sentiment/' + file.split('.')[0] + '_sentiment.csv'

    export_csv = df.to_csv(ofile, index=None, header=True)
