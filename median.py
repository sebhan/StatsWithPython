import random

array = []
size = 51

for i in range(size):
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
    return arrayMedian, arrayHalf

arrayMedian = median(array)[0]
arrayHalf = median(array)[1]

lowerHalf = array[0:(arrayHalf+1)]
upperHalf = array[arrayHalf:size]

firstQuartile = median(lowerHalf)[0]
thirdQuartile = median(upperHalf)[0]

arrayMean = sum(array)/size

print "Minimum:", "\t", min(array)
print "First quartile:", firstQuartile
print "Median:", "\t", arrayMedian
print "Mean", "\t\t", arrayMean
print "Third quartile:", thirdQuartile
print "Maximum:", "\t", max(array)
