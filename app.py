import gzip

import pandas as pd

def parse(path):
    g = gzip.open(path,'rb')
    for l in g:
        yield eval(l)

def getDF(path):
    i = 0
    df ={}
    for d in parse(path):
        df[i] = d
        i += 1
    return pd.DataFrame.from_dict(df,orient ='index')


df = getDF('reviews_Digital_Music_5.json.gz')


#df.to_excel("MusicLibrary.xlsx")

df['review_len'] = df['reviewText'].apply(len)

df['review_words_count'] = df['reviewText'].str.count(' ') + 1


by_wordcount = df.groupby('overall')['review_words_count'].mean().reset_index()


"""put username and api_key for aplotly account"""
import plotly
plotly.__version__
#plotly.tools.set_credentials_file(username='#######', api_key='################')

import plotly.plotly as py
import plotly.graph_objs as go
data = [go.Bar(
            x = by_wordcount['overall'],
            y = by_wordcount['review_words_count'],
            name = 'average-review-words-count'
)]
layout = go.Layout(
            title ='Average Review words vs Ratings',
            xaxis=dict(
                title = 'Review Ratings',
                tickfont=dict(
                    size=14,
                    color='rgb(107, 107, 107)'
                )
            ),
            yaxis=dict(
                title='Average Review word-count',
                titlefont=dict(
                    size=16,
                    color='rgb(107, 107, 107)'
                ),
                tickfont=dict(
                    size=14,
                    color='rgb(107, 107, 107)'
                )
            )
)
fig = go.Figure(data =data,layout =layout)
py.iplot(fig,filename='review_vs_wordcount')


"""
#distribution of ratings

"""



by_count = df.groupby('overall')['reviewerID'].count().reset_index()
#df.groupby('overall')['review_words_count'].mean().reset_index()

data = [go.Bar(
            x = by_count['overall'],
            y = by_count['reviewerID'],
            name = 'Distribution of reviewers and ratings'
)]
layout = go.Layout(
            title ='Distribution of Ratings',
            xaxis=dict(
                title = 'Ratings',
                tickfont=dict(
                    size=14,
                    color='rgb(107, 107, 107)'
                )
            ),
            yaxis=dict(
                title='Number of reviewers',
                titlefont=dict(
                    size=16,
                    color='rgb(107, 107, 107)'
                ),
                tickfont=dict(
                    size=14,
                    color='rgb(107, 107, 107)'
                )
            )
)
fig = go.Figure(data =data,layout =layout)
py.iplot(fig,filename='reviewercount_vs_ratings')