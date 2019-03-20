import time
from statistics import variance

#file_path = "oneAndHalfMeter.txt"
#file_path = "threeMeter.txt"
#file_path = "fourAndHalfMeter.txt"
#file_path = "sixMeter.txt"
#file_path = "sevenAndHalfMeter.txt"
file_path = "nineMeter.txt"

file = open(file_path, 'r') 
print(file)
data = []
for line in file:
    fields = line.split()
    rowdata = map(float, fields)
    data.extend(rowdata)
'''
print(sum(data)/len(data))
print(variance(data))
'''
for x in data:
    i = (x-80.3853427896)**2
    i+= i
print(i/len(data))
    