# from apis 
import dataParser
import json,re,nltk
import time
from nltk.corpus import stopwords

st = time.time()
# filePath = "../data/sample_Cell_Phones_and_Accessories_5.json"
filePath = "../data/Cell_Phones_and_Accessories_5.json"
headersRequired = ['reviewerID', 'reviewerName', 'helpful', 'reviewText', 'overall', 'unixReviewTime', 'reviewTime']
data = dataParser.parse_file_content(filePath, headersRequired)
print("######## data loaded in data frame #########")


# for sentence in data['reviewText']:
#     tokens = nltk.word_tokenize(sentence)
#     print(tokens)

    # tokens = nltk.word_tokenize(sentence)
    # print(tokens)
    # print('*********')
stopwords = set(stopwords.words('english'))

word_list = []
word_dict = {}
for sentence in data['reviewText']:
    temp_word_list=[]
    sentence = re.sub('[^a-zA-Z0-9\n\.\' ]', '', sentence)
    for word in sentence.split():
        temp_word_list.append(word)
    word_list = [word for word,pos in nltk.pos_tag(temp_word_list) if (pos == 'VBP' or pos == 'VB' or pos == 'IN' or pos == 'JJ' or pos == 'NN' or pos == 'NNP' or pos == 'RP')]
    for word in word_list:
        word = word.lower()
        if word not in stopwords and len(word) > 1:
            if word not in word_dict:
                word_dict[word] = 0
            word_dict[word] += 1

#take top 200 words and make the cloud
maxLength = 200
topWords  = sorted(word_dict, key=word_dict.get, reverse=True)[:maxLength]
newWordDict = {}
for word in topWords:
    newWordDict[word] = word_dict[word]
word_dict = newWordDict

# print(word_dict)
# # wordDict = wc.WordCounter().getWordDict(data, 250)
# # print("word count dict created")
wordDictJson = json.dumps(word_dict)
outPutfilePath = "../data/sample_reduced_word_count.json"
f = open(outPutfilePath, "w")
f.write(wordDictJson)
f.close()
et = time.time()
print("time taken:", et-st)
#print(wordDictJson)


