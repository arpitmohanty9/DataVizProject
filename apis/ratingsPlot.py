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

'''
function to plot line graph for a ratings file 

ratingsFilePath: file path of ratings file
year: year for which graph needs to be plotted
'''
def plotGraph(ratingsFilePath, year):
    df = pd.read_csv(ratingsFilePath, names=['user','item','rating','timestamp'], header=None)
    df['year'] = df.apply(getYear, axis=1)
    df = df[df.year == year]
    df['yearMonth'] = df.apply(getYearMonth, axis=1)
    df = df.groupby('yearMonth').count().reset_index()
    x = df["yearMonth"].values
    y = df["item"].values
    mlpp.plot(x, y, marker='o', linestyle='-', color='g', label='Square')
    mlpp.xlabel('Month')
    mlpp.xlabel('Rating count')
    mlpp.show()

if __name__ == "__main__":
    # Example to use this function
    filePath = "../data/ratings_Electronics_short.csv"
    plotGraph(filePath, '2013')