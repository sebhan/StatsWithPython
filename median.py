import random

array = []

for i in range(5):
    array.append(random.random())

array = sorted(array)

def median(array):
    arrayLength = len(array)
    arrayHalf = arrayLength/2.0
    if arrayLength % 2 == 0:
        arrayHalf = int(arrayHalf)
        arrayMedian = (array[arrayHalf] + array[arrayHalf-1])/2.0
    else:
        arrayHalf = int(arrayHalf-0.5)
        arrayMedian = array[arrayHalf]
    return arrayMedian

print "Median:", median(array)
print "Minimum:", min(array)
print "Maximum:", max(array)
