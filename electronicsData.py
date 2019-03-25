import dataParser

filePath = "./data/reviews_Electronics_5.json"
headersRequired = ['reviewerID','reviewerName','helpful','reviewText','overall','unixReviewTime','reviewTime']
data = dataParser.parse_file_content(filePath, headersRequired)
print(data.head())
print(data.shape)