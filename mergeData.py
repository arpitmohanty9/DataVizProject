from apis import dataParser
import gzip
import time
import json

def parse(path):
    g = gzip.open(path,'rb')
    for l in g:
        yield eval(l)


def getAsinBrandDict(path, asinSet, headersRequired):
    metaAsinDict ={}
    i = 0
    for metadataObject in parse(path):
        if i%100000 == 0:
            print('metaData processed count:', i, " dictCount:", len(metaAsinDict))
        asin = metadataObject['asin']
        if asin in asinSet:
            newObject = {}
            for header in headersRequired:
                if header in metadataObject:
                    newObject[header] = metadataObject[header]
                else:
                    newObject[header] = ''
            metaAsinDict[asin] = newObject
        i += 1
    return metaAsinDict


def addMetaDataToReviewDataFrame(metaAsinDict, reviewDataFrame, metaheaders):
    asins = reviewDataFrame['asin']
    columnsDict = {}
    for header in metaheaders:
        columnsDict[header] = []
    for asin in asins:
        if asin in metaAsinDict:
            for header in metaheaders:
                columnsDict[header].append(metaAsinDict[asin][header])
        else:
            for header in metaheaders:
                columnsDict[header].append('')
    for header in metaheaders:
        reviewDataFrame[header] = columnsDict[header]
    return reviewDataFrame


if __name__ == "__main__":
    st = time.time()
    filePath = "data/reviews_Cell_Phones_and_Accessories_5.json"
    headersRequired = ['asin', 'reviewerID', 'reviewerName', 'helpful', 'reviewText', 'overall', 'unixReviewTime', 'reviewTime']
    reviewDataFrame = dataParser.parse_file_content(filePath, headersRequired)
    asin = reviewDataFrame['asin']
    asinSet = set(asin)
    metaheadersRequired = ['title', 'price', 'imUrl', 'salesRank', 'brand', 'categories']
    asinDict = getAsinBrandDict('data/metadata.json.gz', asinSet, metaheadersRequired)
    reviewDataFrame = addMetaDataToReviewDataFrame(asinDict, reviewDataFrame, metaheadersRequired)
    reviewDataFrame.to_csv('data/reviews_Cell_Phones_with_metadata.csv')
    et = time.time()
    print("Time taken:", et-st)

