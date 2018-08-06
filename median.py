import random

array = []

for i in range(500):
    array.append(random.random())

arrayLength = len(array)
arrayHalf = arrayLength/2.0
array = sorted(array)

if arrayLength % 2 == 0:
    arrayHalf = int(arrayHalf)
    arrayMedian = (array[arrayHalf] + array[arrayHalf-1])/2.0
else:
    arrayHalf = arrayHalf-0.5
    arrayMedian = array[arrayHalf]
    
print array,"\n"
print "Median:", arrayMedian
print "Minimum:", min(array)
print "Maximum:", max(array)
