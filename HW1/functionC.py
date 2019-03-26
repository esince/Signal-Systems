#@Author
#Student Name: Esin Ece Aydin
#Student ID: 150160151
#Date: 15.03.2019

import matplotlib.pyplot as plt
import numpy as np
import math
import sys

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
yPlot = sys.argv[5+xNumber:5+ xNumber +yNumber]
yPlot = map(int, yPlot)

def convolution(sample1, sample2):
    numbercov = xNumber+yNumber-1
    z = []
    for i in range(numbercov):
        i1 = i
        sum = 0
        for j in range(len(sample2)):
            if(i1 > 0 and i1 < len(sample1)):
                sum += sample1[i1] * sample2[j]
            i1 = i1 - 1
        z.append(sum)
    return z

z = []
z = convolution(xPlot, yPlot)
print("convolution of the signals =")
print(z)
