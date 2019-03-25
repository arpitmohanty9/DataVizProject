import dataParser
import pandas as pd
import time
import matplotlib.pyplot as mlpp

filePath = "./data/reviews_Electronics_5.json"
headersRequired = ['reviewerID','reviewerName','helpful','reviewText','overall','unixReviewTime','reviewTime']
#data = dataParser.parse_file_content(filePath, headersRequired)
#print(data.head())
#print(data.shape)




#dataFrame = pd.read_csv("./data/ratings_Electronics.csv", header=None)
#dataFrame = dataFrame[:1000]
#dataFrame.to_csv("./data/ratings_Electronics_short.csv", header=False, index=False)



dataFrame = pd.read_csv("./data/ratings_Electronics_short.csv",names=['user','item','rating','timestamp'], header=None)
dataFrame = pd.read_csv("./data/ratings_Electronics.csv",names=['user','item','rating','timestamp'], header=None)
df = dataFrame
#df['year'] = df.apply(lambda x:time.strftime("%Y", int(x['timestamp'])), axis=1)


def getYear(row):
    #print(row['timestamp'])
    ts = time.gmtime(row['timestamp'])
    #print(ts)
    #print(time.strftime("%Y", str('1365811200')))
    #print(time.strftime("%Y", ts))
    return time.strftime("%Y", ts)

def getMonth(row):
    ts = time.gmtime(row['timestamp'])
    return time.strftime("%m", ts)

def getYearMonth(row):
    ts = time.gmtime(row['timestamp'])
    return time.strftime("%Y-%m", ts)

#df.apply(lambda x: print(time.strftime("%Y", int(x['timestamp']))), axis=1)
df['year'] = df.apply(getYear, axis=1)
#df['month'] = df.apply(getMonth, axis=1)
df = df[df.year == '2013']
df['yearMonth'] = df.apply(getYearMonth, axis=1)
df = df.groupby('yearMonth').count().reset_index()
#print(dataFrame.groupby('yearMonth').count().reset_index())
#print(dataFrame.head())
#print(dataFrame.shape)
print(df)
print(df["yearMonth"].values)

#time_length = pd.Series(df["item"].values, df["yearMonth"].values)
#time_length.plot(figsize=(16, 4), color="g")
x = df["yearMonth"].values
y = df["item"].values
mlpp.plot(x, y, marker='o', linestyle='-', color='g', label='Square')
#mlpp.plot()
mlpp.xlabel('Month')
mlpp.xlabel('Review count')
mlpp.show()