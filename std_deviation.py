import csv
import math
import statistics

with open('Marks.csv',newline = '') as f:
    reader = csv.reader(f)
    file_data = list(reader)

data = file_data[0]

def mean(data):
    totalentries = len(data)
    total = 0
    for marks in data:
        total+=int(marks)
    
    mean = total/totalentries
    return mean

squaredlist = []

for i in data:
    number = int(i)-mean(data)
    number = number**2
    squaredlist.append(number)

sum = 0
for square in squaredlist:
    sum = sum+square

result = sum/(len(data)-1)

standardDeviation = math.sqrt(result)

print('the standardDeviation of the marks are',standardDeviation)

