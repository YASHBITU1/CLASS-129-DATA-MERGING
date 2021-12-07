import csv 

data2 =[]
data1 = []

with open("dataset1.csv","r")as f:
    csvReader = csv.reader(f)
    for row in csvReader:
        data1.append(row)

with open("bright_stars.csv","r")as f:
    csvReader = csv.reader(f)
    for row in csvReader:
        data2.append(row)

headers1 = data1[0]
dataset1 = data1[1:]

headers2 = data2[0]
dataset2 = data2[1:]

header = headers1 + headers2

dataset = []

for index,row in enumerate(dataset1):
    dataset.append(dataset1[index]+dataset2[index])

with open("merged.csv","a+")as f:
    csvWriter = csv.writer(f)
    csvWriter.writerow(header)
    csvWriter.writerows(dataset)
