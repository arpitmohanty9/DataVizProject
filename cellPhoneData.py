from apis import dataParser
from apis import wordCounter as wc
import json
import time

st = time.time()
filePath = "./data/reviews_Cell_Phones_and_Accessories_5.json"
#filePath = "./data/sample_reviews_Electronics_5.json"
headersRequired = ['reviewerID', 'reviewerName', 'helpful', 'reviewText', 'overall', 'unixReviewTime', 'reviewTime']
data = dataParser.parse_file_content(filePath, headersRequired)
print("data loaded in data frame")
wordDict = wc.WordCounter().getWordDict(data, 250)
print("word count dict created")
wordDictJson = json.dumps(wordDict)
outPutfilePath = "./data/sample_reviews_cell_phones_word_count.json"
f = open(outPutfilePath, "w")
f.write(wordDictJson)
f.close()
et = time.time()
print("time taken:", et-st)
#print(wordDictJson)


