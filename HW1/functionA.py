#@Author
#Student Name: Esin Ece Aydin
#Student ID: 150160151
#Date: 15.03.2019

import matplotlib.pyplot as plt #to plot the values
import numpy as np
import sys #to get input as an argument

# BELOW INPUT SEQUENCES ARE GIVEN EXAMPLE IN HW.
#1) 0 5 0 3   0 1 2 2 1 0   1 2 3 4
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
#y[n] starts at the index 5+xNumber and goes till the end.
yPlot = sys.argv[5+xNumber:]

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
plt.stem(x, xPlot, 'b', markerfmt='o', label= 'x[n]')
#plot y[n]
plt.stem(y+0.03, yPlot, 'g', markerfmt='o', label= 'y[n]')

plt.title('Visualizing two discrete non-periodic signal')
plt.xlabel("Time")
plt.ylabel("Sample Value")
plt.legend()
plt.show()
