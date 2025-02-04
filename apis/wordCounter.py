from apis import dataParser
import re

class WordCounter:

    def __init__(self):
        self.wordDict = {}
        self.wordList = []
        stopwordsText = "poop,i,me,my,myself,we,us,our,ours,ourselves,you,your,yours,yourself,yourselves,he,him,his,himself,she,her,hers,herself,it,its,itself,they,them,their,theirs,themselves,what,which,who,whom,whose,this,that,these,those,am,is,are,was,were,be,been,being,have,has,had,having,do,does,did,doing,will,would,should,can,could,ought,i'm,you're,he's,she's,it's,we're,they're,i've,you've,we've,they've,i'd,you'd,he'd,she'd,we'd,they'd,i'll,you'll,he'll,she'll,we'll,they'll,isn't,aren't,wasn't,weren't,hasn't,haven't,hadn't,doesn't,don't,didn't,won't,wouldn't,shan't,shouldn't,can't,cannot,couldn't,mustn't,let's,that's,who's,what's,here's,there's,when's,where's,why's,how's,a,an,the,and,but,if,or,because,as,until,while,of,at,by,for,with,about,against,between,into,through,during,before,after,above,below,to,from,up,upon,down,in,out,on,off,over,under,again,further,then,once,here,there,when,where,why,how,all,any,both,each,few,more,most,other,some,such,no,nor,not,only,own,same,so,than,too,very,say,says,said,shall"
        self.stopwords = self.getWords(stopwordsText)

    # def getWords(self, text):
    #     words = re.split('[ \'\-\(\)\*":;\[\]|{},.!?]+', text)
    #     return words

    def getWords(self, text):
        words = re.sub('[^a-zA-Z0-9\n\.\' ]', '', text)
        return words

    def buildDict(self, row):
        reviewWords = self.getWords(row['reviewText'])
        for word in reviewWords:
            word = word.lower()
            if word not in self.stopwords and len(word) > 1:
                if word not in self.wordDict:
                    self.wordDict[word] = 0
                self.wordDict[word] += 1

    def buildList(self, row):
        reviewWords = self.getWords(row['reviewText'])
        for word in reviewWords.split(' '):
            word = word.lower()
            if word not in self.stopwords and len(word) > 1:
                if word not in self.wordList:
                    self.wordList.append(word)

    def getWordList(self, dataFrame, maxLength):
        self.wordList = []
        dataFrame.apply(self.buildList, axis=1)
        specific_list = [word for word,pos in nltk.pos_tag(wordList) if (pos == 'VBP' or pos == 'VB' or pos == 'IN' or pos == 'JJ' or pos == 'NN' or pos == 'NNP' or pos == 'RP')]
        self.wordList.extend(specific_list)
        return self.wordList

    def getWordDict(self, dataFrame, maxLength):
        self.wordDict = {}
        dataFrame.apply(self.buildDict, axis=1)
        topWords  = sorted(self.wordDict, key=self.wordDict.get, reverse=True)[:maxLength]
        newWordDict = {}
        for word in topWords:
            newWordDict[word] = self.wordDict[word]
        self.wordDict = newWordDict
        return self.wordDict


    # def buildList(self, row):
    #     reviewWords = self.getWords(row['reviewText'])
    #     for word in reviewWords:
    #         word = word.lower()
    #         if word not in self.stopwords and len(word) > 1:
    #             if word not in self.wordDict:
    #                 self.wordDict[word] = 0
    #             self.wordDict[word] += 1

if __name__ == "__main__":
    filePath = "../data/sample_reviews_Electronics_5.json"
    headersRequired = ['reviewerID', 'reviewerName', 'helpful', 'reviewText', 'overall', 'unixReviewTime', 'reviewTime']
    data = dataParser.parse_file_content(filePath, headersRequired)
    wordDict = WordCounter().getWordDict(data,5)
    print(wordDict)

