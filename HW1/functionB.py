#@Author
#Student Name: Esin Ece Aydin
#Student ID: 150160151
#Date: 15.03.2019

import matplotlib.pyplot as plt
import numpy as np
import sys
import math

# BELOW INPUT SEQUENCES ARE GIVEN EXAMPLE IN HW.
#1) 0 5 0 3 0 1 2 2 1 0 1 2 3 4
#2) 0 5 0 3 0 2 4 4 2 0 1 2 3 4
#3) 0 5 0 3 0 2 4 4 2 0 2 4 6 8
#4) 0 5 -5 5 -2 2 -2 2 -2 2 -1 1 -1 1 -1 1 -1 1 -1 1 -1

xLowerB = int(sys.argv[1])
xUpperB = int(sys.argv[2])
yLowerB = int(sys.argv[3])
yUpperB = int(sys.argv[4])

#to calculate how many points for x[n] and y[n]
xNumber = xUpperB - xLowerB + 1
yNumber = yUpperB - yLowerB + 1

#x[n] starts at the index 5 and goes till 5+xNumber index
xPlot = sys.argv[5:5+xNumber]
xPlot = map(int, xPlot)
#y[n] starts at the index 5+xNumber and goes till the end.
yPlot = sys.argv[5+xNumber:]
yPlot = map(int, yPlot)

#to obtain mean of a signal
def findMean(sample):
    return sum(sample) / (len(sample)*1.0)

#to obtain standard deviation of a signal
def findSDeviation(sample):
    length = len(sample)
    mean = findMean(sample)
    sum = 0
    for i in range(length):
        sum += (sample[i] - mean)**2
    return math.sqrt(sum/((length-1)*1.0))

#to calculate standard normalized form of a signal
def normalized(sample):
    length= len(sample)
    mean = findMean(sample)
    stdDeviation = findSDeviation(sample)
    normalizePlot = []
    for i in range(length):
        normalizePlot.append( (sample[i]- mean) / stdDeviation )
        print(normalizePlot[i])
    return normalizePlot

#std. normalized form of a xPlot signal
stdNormalX = normalized(xPlot)
#std. normalized form of a yPlot signal
stdNormalY = normalized(yPlot)


#these are variables for specified x-axis' limit
upper = yUpperB
lower = yLowerB

if(xUpperB > yUpperB):
    upper = xUpperB
if(xLowerB < yLowerB):
    lower = xLowerB

x = np.arange(xLowerB, xUpperB+1, 1)
y = np.arange(yLowerB, yUpperB+1, 1)

#plot x-axis
plt.xlim(lower-1,upper+1)

#plot x[n]
plt.stem(x, stdNormalX, 'b', markerfmt='o', label= 'x[n]')
#plot y[n]
plt.stem(y+0.03, stdNormalY, 'g', markerfmt='o', label= 'y[n]')

plt.title('Visualizing standard normalized form of the signals')
plt.xlabel("Time")
plt.ylabel("Sample Value")
plt.legend()
plt.show()
