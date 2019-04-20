import json
import nltk
import os
import re
import time

import pandas as pd
from nltk.corpus import stopwords

st = time.time()
folder = "../data/brands"

from os import listdir
from os.path import isfile, join

onlyfiles = [f for f in listdir(folder) if isfile(join(folder, f))]

newDict = {}
stopwords = set(stopwords.words('english'))

for file in onlyfiles:
    print("Processing ", file)
    filepath = os.path.join(folder, file)
    data = pd.read_csv(filepath)
    word_list = []
    word_dict = {}
    print("Starting ", file)
    for sentence_orig in data['reviewText']:
        temp_word_list = []
        sentence = re.sub('[^a-zA-Z0-9\n\.\' ]', '', sentence_orig)
        for word in sentence.split():
            temp_word_list.append(word)
            word_list = [word for word, pos in nltk.pos_tag(temp_word_list) if (
                        pos == 'JJ' or pos == 'NN' or pos == 'NNP' or pos == 'RP')]
        for word in word_list:
            word = word.lower()
            if word not in stopwords and len(word) > 1:
                if word not in word_dict:
                    word_dict[word] = 0
                word_dict[word] += 1

    print("Before top words", file)
    maxLength = 100
    topWords = sorted(word_dict, key=word_dict.get, reverse=True)[:maxLength]
    newWordDict = {}
    for word in topWords:
        newWordDict[word] = word_dict[word]
    word_dict = newWordDict

    newDict[file.split('.')[0]] = word_dict

    print("Processed ", file)

wordDictJson = json.dumps(newDict)

outPutfilePath = "../data/wordcloud_all.json"
with open(outPutfilePath, "w") as f:
    f.write(wordDictJson)

et = time.time()
print("time taken:", et - st)
# print(wordDictJson)
