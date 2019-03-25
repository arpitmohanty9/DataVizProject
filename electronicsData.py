import dataParser
import pandas as pd
import time
import matplotlib.pyplot as mlpp


def getYear(row):
    ts = time.gmtime(row['timestamp'])
    return time.strftime("%Y", ts)

def getMonth(row):
    ts = time.gmtime(row['timestamp'])
    return time.strftime("%m", ts)

def getYearMonth(row):
    ts = time.gmtime(row['timestamp'])
    return time.strftime("%Y-%m", ts)

#filePath = "./data/reviews_Electronics_5.json"
#headersRequired = ['reviewerID','reviewerName','helpful','reviewText','overall','unixReviewTime','reviewTime']
#data = dataParser.parse_file_content(filePath, headersRequired)
#print(data.head())
#print(data.shape)

dataFrame = pd.read_csv("./data/ratings_Electronics.csv",names=['user','item','rating','timestamp'], header=None)
df = dataFrame

df['year'] = df.apply(getYear, axis=1)
df = df[df.year == '2013']
df['yearMonth'] = df.apply(getYearMonth, axis=1)
df = df.groupby('yearMonth').count().reset_index()
x = df["yearMonth"].values
y = df["item"].values
mlpp.plot(x, y, marker='o', linestyle='-', color='g', label='Square')
mlpp.xlabel('Month')
mlpp.xlabel('Rating count')
mlpp.show()