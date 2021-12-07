import csv

data = []

with open("bright_stars.csv","r")as f:
    csvReader = csv.reader(f)
    for row in csvReader:
        data.append(row)

headers = data[0]
dataset = data[1:]
for datapoint in dataset:
    datapoint[1] = datapoint[1].lower()

dataset.sort(key = lambda dataset:dataset[1])

with open("starsSorted.csv","a+")as f:
    csvWriter = csv.writer(f)
    csvWriter.writerow(headers)
    csvWriter.writerows(dataset)


