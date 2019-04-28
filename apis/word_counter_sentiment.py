import json

filePath = "../data/wordcloud_all.json"
outPutfilePath = "../data/wordcloud_all_sentiment.json"

def getWordList(filePath):
    wordset = set()
    with open(filePath, encoding="ISO-8859-1") as file:
        for line in file:
            line = line.strip()
            if not (not line or ';' in line):
                #print(line)
                if line not in wordset:
                    wordset.add(line)
    print(wordset)
    print("len:",len(wordset))
    return wordset

negativeWordFile = '../data/negative-words.txt'
positiveWordFile = '../data/positive-words.txt'
print("postive")
positiveWordList = getWordList(positiveWordFile)
pos = ["phone","case","screen","battery","protector","charger","anchor","power"]
positiveWordList.update(pos)
print("negative")
negativeWordList = getWordList(negativeWordFile)
#exit()


newData = {}
with open(filePath) as json_file:
    data = json.load(json_file)
    for brand, brandData in data.items():
        newData[brand] = {}
        for word, wordCount in brandData.items():
            sent = 1
            if word in negativeWordList:
                sent = 0
            elif word in positiveWordList:
                sent = 2
            newData[brand][word] = {
                "freq": wordCount,
                "sent": sent
            }
with open(outPutfilePath, 'w') as outfile:
    json.dump(newData, outfile)

print(json.dumps(newData))
