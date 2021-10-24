import csv
from collections import Counter

with open ("SOCR.csv", newline = '')as f:
    r = csv.reader(f)
    fileData = list(r)

fileData.pop(0)
newData = []

for i in range(len(fileData)):
    n = fileData[i][1]
    newData.append(float(n))

data = Counter(newData)
modeRange = {"50-60": 0, "60-70": 0, "70-80": 0}

for height, occurence in data.items():
    if 50 < float(height) < 60:
        modeRange["50-60"] += occurence
    elif 60 < float(height) < 70:
        modeRange["60-70"] += occurence
    elif 70 < float(height) < 80:
        modeRange["70-80"] += occurence

modeR,modeO = 0,0
for range, occurence in modeRange.items():
    if occurence > modeO:
        modeR,modeO = [int(range.split("-")[0]), int(range.split("-")[1])],occurence

mode = float((modeR[0] + modeR[1])/2)
print("Mode is:",mode)
