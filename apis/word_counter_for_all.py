import os
import pandas as pd
import json, re, nltk
import time
from nltk.corpus import stopwords

st = time.time()
folder = "../data/brands"

from os import listdir
from os.path import isfile, join

onlyfiles = [f for f in listdir(folder) if isfile(join(folder, f))]

newDict = {}
stopwords = set(stopwords.words('english'))

for file in onlyfiles:
    filepath = os.path.join(folder, file)
    data = pd.read_csv(filepath)
    word_list = []
    word_dict = {}
    for sentence_orig in data['reviewText']:
        temp_word_list = []
        try:
            sentence = re.sub('[^a-zA-Z0-9\n\.\' ]', '', sentence_orig)
            for word in sentence.split():
                temp_word_list.append(word)
                word_list = [word for word,pos in nltk.pos_tag(temp_word_list) if (pos == 'VBP' or pos == 'VB' or pos == 'IN' or pos == 'JJ' or pos == 'NN' or pos == 'NNP' or pos == 'RP')]
            for word in word_list:
	            word = word.lower()
	            if word not in stopwords and len(word) > 1:
	                if word not in word_dict:
	                    word_dict[word] = 0
	                word_dict[word] += 1
        except Exception as ex:
            print(sentence_orig)
            print(file)  # take top 50 words and make the cloud
maxLength = 50
topWords = sorted(word_dict, key=word_dict.get, reverse=True)[:maxLength]
newWordDict = {}
for word in topWords:
    newWordDict[word] = word_dict[word]
word_dict = newWordDict

newDict[file.split('.')[0]] = word_dict

wordDictJson = json.dumps(newDict)

outPutfilePath = "../data/wordcloud_all.json"
f = open(outPutfilePath, "w")
f.write(wordDictJson)
f.close()
et = time.time()
print("time taken:", et - st)
# print(wordDictJson)
