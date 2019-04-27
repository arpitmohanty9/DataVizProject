import json

filePath = "../data/wordcloud_all.json"
outPutfilePath = "../data/wordcloud_all_sentiment.json"

newData = {}
with open(filePath) as json_file:
    data = json.load(json_file)
    for brand, brandData in data.items():
        newData[brand] = {}
        for word, wordCount in brandData.items():
            newData[brand][word] = {
                "freq": wordCount,
                "sent": wordCount%3
            }
with open(outPutfilePath, 'w') as outfile:
    json.dump(newData, outfile)
