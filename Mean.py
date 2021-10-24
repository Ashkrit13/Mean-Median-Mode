import csv

with open ("SOCR.csv", newline = '')as f:
    r = csv.reader(f)
    fileData = list(r)

fileData.pop(0)
newData = []

for i in range(len(fileData)):
    n = fileData[i][1]
    newData.append(float(n))

l = len(newData)
total = 0

for x in newData:
    total += x

mean = total/l
print("Mean is: " + str(mean))
