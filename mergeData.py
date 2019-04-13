from apis import dataParser
import gzip
import time

def parse(path):
    g = gzip.open(path,'rb')
    for l in g:
        yield eval(l)


def getAsinBrandDict(path, asinSet):
    df ={}
    i = 0
    for d in parse(path):
        if i%100000 == 0:
            print('metaData processed count:',i," dictCount:", len(df))
        if d['asin'] in asinSet and 'brand' in d:
            df[d['asin']] = {'brand': d['brand']}
        i += 1
    return df


def addBrandToReviewDataFrame(asinDict, reviewDataFrame):
    asins = reviewDataFrame['asin']
    brandsColumn = []
    for asin in asins:
        if asin in asinDict:
            brand = asinDict[asin]['brand']
        else:
            brand = ''
        brandsColumn.append(brand)
    reviewDataFrame['brand'] = brandsColumn
    return reviewDataFrame


if __name__ == "__main__":
    st = time.time()
    filePath = "./data/reviews_Cell_Phones_and_Accessories_5.json"
    headersRequired = ['asin', 'reviewerID', 'reviewerName', 'helpful', 'reviewText', 'overall', 'unixReviewTime', 'reviewTime']
    reviewDataFrame = dataParser.parse_file_content(filePath, headersRequired)
    asin = reviewDataFrame['asin']
    asinSet = set(asin)
    asinDict = getAsinBrandDict('data/metadata.json.gz', asinSet)
    reviewDataFrame = addBrandToReviewDataFrame(asinDict, reviewDataFrame)
    reviewDataFrame.to_csv('data/reviews_Cell_Phones_with_brand.csv')
    et = time.time()
    print("Time taken:", et-st)

