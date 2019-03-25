import json
import pandas as pd

def parse_file_content(filePath, headersRequired):
    data = []
    with open(filePath) as fp:
        count = 0
        for line in fp:
            lineObject = json.loads(line)

            newObject = []
            for header in headersRequired:
                if header in lineObject:
                    newObject.append(lineObject[header])
                else:
                    newObject.append('')
            data.append(newObject)
            count += 1
    dataFrame = pd.DataFrame(data, columns=headersRequired)
    return dataFrame


if __name__ == "__main__":
    # Example to use this function
    filePath = "./data/sample_reviews_Electronics_5.json"
    headersRequired = ['reviewerID','reviewerName','helpful','reviewText','overall','unixReviewTime','reviewTime']
    data = parse_file_content(filePath, headersRequired)
    print(data.head())
    print(data.shape)
