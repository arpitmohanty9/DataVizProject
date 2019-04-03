from apis import dataParser
from apis import wordCounter as wc

#filePath = "./data/reviews_Electronics_5.json"
filePath = "./data/sample_reviews_Electronics_5.json"
headersRequired = ['reviewerID', 'reviewerName', 'helpful', 'reviewText', 'overall', 'unixReviewTime', 'reviewTime']
data = dataParser.parse_file_content(filePath, headersRequired)
data['reviewText'] = ['hello I am a manager and team lead', 'you are team lead']
wordDict = wc.WordCounter().getWordDict(data)
print(wordDict)

