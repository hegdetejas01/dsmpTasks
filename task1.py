### Q1 :- Print the given strings as per stated format.

# **Given strings**
# "Data" "Science" "Mentorship" "Program"
# "By" "CampusX"

# **Output**:
# Data-Science-Mentorship-Program-started-By-CampusX

# Concept- [Seperator and End]

print("Data", "Science", "Mentorship", "Program", sep='-', end='-started-')
print("By", "CampusX", sep='-')



### Q2:- Write a program that will convert celsius value to fahrenheit.

def celciusToFahrenheit(celcius):
    fr = (9/5*celcius) + 32
    return fr
ce = float(input("enter the temp in celcius value: "))
print(celciusToFahrenheit(ce))


### Q3:- Take 2 numbers as input from the user.Write a program to swap the numbers without using any special python syntax.

a,b = int(input("Enter number 1: ")), int(input("Enter number 2: "))
temp = a
a = b
b = temp
print(a,b)



### Q4:- Write a program to find the euclidean distance between two coordinates.Take both the coordinates from the user as input.

x1,y1 = int(input("enter x cord of 1st point: ")), int(input("enter y cord of 1st point: "))
x2,y2 = int(input("enter x cord of 2nd point: ")), int(input("enter y cord of 2nd point: "))
xDiff, yDiff = x2-x1, y2-y1
xDiffSq, yDiffSq = xDiff**2, yDiff**2
sumOfDiffSq = xDiffSq + yDiffSq
ed = sumOfDiffSq**0.5
print(ed)



### Q5:- Write a program to find the simple interest when the value of principle,rate of interest and time period is provided by the user.

p = int(input("Enter principle: "))
t = int(input("Enter time: "))
r = float(input("Enter rate: "))
si = p*t*r/100
print(si)



### Q7:- Write a program to find the sum of squares of first n natural numbers where n will be provided by the user.

import functools
n = int(input("Enter the value of n: "))
res = functools.reduce(lambda x, y : x + y, [i**2 for i in range(1, n+1)])
print(res)


### Q8:- Given the first 2 terms of an Arithmetic Series.Find the Nth term of the series. Assume all inputs are provided by the user.

n = int(input("Enter the n: "))
a1, a2 = int(input("Enter the 1st value: ")), int(input("Enter the 2nd value: "))
nthTerm = a1 + ((n-1)*(a2-a1))
print(nthTerm)



### Q9:- Given 2 fractions, find the sum of those 2 fractions.Take the numerator and denominator values of the fractions from the user.

n1, d1 = int(input("Enter the numerator 1: ")), int(input("Enter the denominator 1: "))
n2, d2 = int(input("Enter the numerator 2: ")), int(input("Enter the denominator 2: "))
nRes = n1*d2 + n2*d1
dRes = d1*d2
print("Result in fraction format - {}/{}\nIn decimal form is {}".format(nRes,dRes, nRes/dRes))



### Q10:- Given the height, width and breadth of a milk tank, you have to find out how many glasses of milk can be obtained? Assume all the inputs are provided by the user.

# Input:
# Dimensions of the milk tank<br>
# H = 20cm, L = 20cm, B = 20cm

# Dimensions of the glass<br>
# h = 3cm, r = 1cm
import math

tankH, tankL, tankB = 20, 20, 20
glassH, glassR = 3, 1 
tankVolume = tankB * tankH * tankL
glassVolume = 3.14 * glassR**2 * glassH
res = math.floor(tankVolume/glassVolume)
print(res)



### Q6:- Write a program that will tell the number of dogs and chicken are there when the user will provide the value of total heads and legs.

# For example:
# Input:
# heads -> 4
# legs -> 12

# Output:
# dogs -> 2
# chicken -> 2

"""
D + C = number of heads
4D + 2C = number of legs
"""

# d = c = 0

# heads = int(input("Enter the number of heads: ")) # D + C
# legs = int(input("Enter the number of legs: ")) # 4D + 2C