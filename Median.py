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
newData.sort()

if l %2 == 0:
    median1 = float(newData[l//2])
    median2 = float(newData[l//2-1])
    median = (median1 + median2)/2

else:
    median = newData[l//2]

print("Median is: " + str(median))
