### `Problem 1`: Write a program that will give you in hand monthly salary after deduction on CTC - HRA(10%), DA(5%), PF(3%) and taxes deduction as below:

# > Salary(Lakhs) : Tax(%)
# *   Below 5 : 0%
# *   5-10 : 10%
# *   10-20 : 20%
# *   aboove 20 : 30%

ctc = int(input("Enter your CTC (in Lakh): "))

if ctc < 500000:
    finalSalary = 0.82*ctc
elif ctc < 1000000:
    finalSalary = 0.72*ctc
elif ctc < 2000000:
    finalSalary = 0.62*ctc
elif ctc > 2000000:
    finalSalary = 0.52*ctc

print(round(finalSalary/12, 2))



### `Problem 2`: Write a program that take a user input of three angles and will find out whether it can form a triangle or not.

a1, a2, a3 = int(input("Enter angle 1: ")), int(input("Enter angle 2: ")), int(input("Enter angle 3: "))
if a1>0 and a2>0 and a3>0 and a1+a2+a3 == 180:
    print("Yes, they for a triangle")
else: print("They dont form a triangle")


### `Problem 3`: Write a program that will take user input of cost price and selling price and determines whether its a loss or a profit.

cp, sp = int(input("Enter the cost price: ")), int(input("Enter the selling price: "))
if sp-cp > 0: print("Profit")
else: print("Loss")


### `Problem 4`: Write a menu-driven program -
# 1. cm to ft
# 2. km to miles
# 3. USD to INR
# 4. exit

userInput = int(input("""
1. Press 1 to convert cm to feet
2. Press 2 to convert km to miles
3. Press 3 to convert USD to INR
4. Press 4 to exit
"""))
if userInput == 1:
    cm = float(input("Enter the value in cm: "))
    print("Value in feet is", cm/30.48)
elif userInput == 2:
    km = float(input("Enter the value of km: "))
    print("Value in miles is", km/1.609)
elif userInput == 3:
    usd = float(input("Enter the usd: "))
    print("Value in inr is", usd*95)
else: print("Exited")



### `Problem 5` - Exercise 12: Display Fibonacci series up to 10 terms.
# Note: The Fibonacci Sequence is a series of numbers. The next number is found by adding up the two numbers before it. The first two numbers are 0 and 1. For example, 0, 1, 1, 2, 3, 5, 8, 13, 21. The next number in this series above is 13+21 = 34

f1, f2 = 0, 1
n = int(input("Enter n: "))
print(f1,f2,sep = ", ", end=", ")
for i in range(1,n-1):
    nextNum = f1+f2
    print(nextNum, end=", ")
    f1, f2 = f2, nextNum



### `Problem 6` - Find the factorial of a given number.
# input 5
# outpur 120

num = int(input("Enter the number: "))
res1 = 1
for i in range(1,num+1):
    res1 *= i
print(res1)

# """ OR """

import functools
res2 = functools.reduce(lambda x,y: x*y, [i for i in range(1,num+1)])
print(res2)


### `Problem 7` - Reverse a given integer number.

num = int(input("Enter the number: "))
rev = 0

while num>0:
    last = num%10
    rev = rev*10 + last
    num = num//10

print(rev)



### `Problem 8`: Take a user input as integer N. Find out the sum from 1 to N. If any number if divisible by 5, then skip that number. And if the sum is greater than 300, don't need to calculate the sum further more. Print the final result. And don't use for loop to solve this problem.

N = int(input("Enter the number: "))
sum = 0
i = 1

while i<=N:

    if i%5!=0:
        if sum<300:
            print(i)
            sum+=i
    
    i+=1

print("Final result is", sum)




### `Problem 9`: Write a program that keeps on accepting a number from the user until the user enters Zero. Display the sum and average of all the numbers.

sum = 0
i = 0
while True:
    n = int(input("Enter the number: "))
    if n==0: 
        break

    sum+=n
    i+=1

if i>0:
    print(sum, sum/i)




###`Problem 9`: Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5, between 2000 and 3200 (both included). The numbers obtained should be printed in a comma-separated sequence on a single line.

res = [str(i) for i in range(2000,3201) if i%7==0 and i%5!=0]
print(", ".join(res))



###`Problem 10`: Write a program, which will find all such numbers between 1000 and 3000 (both included) such that each digit of the number is an even number. The numbers obtained should be printed in a space-separated sequence on a single line.

l = []
for i in range(1000,3001):
    numberEven = True
    for j in str(i):
        if int(j)%2 != 0:
            numberEven = False
            break

    if numberEven:
        l.append(str(i))

print(" ".join(l))

""" OR """

l = []
for i in range(2000,3001):
    if all (int(j)%2==0 for j in str(i)):
        l.append(str(i))
print(" ".join(l))


###`Problem 12`:Write a program to print whether a given number is a prime number or not

n = int(input("Enter the number: "))
for i in range(2, int(n**0.5) +1 ): #check till sqrt of the number
    if n%i==0:
        print("Not a prime")
        exit()

print("Prime")


###`Problem 13`:Print all the Armstrong numbers in a given range.
# Range will be provided by the user
# Armstrong number is a number that is equal to the sum of cubes of its digits. For example 0, 1, 153, 370, 371 and 407 are the Armstrong numbers.

low = int(input("Enter lower range: "))
high = int(input("Enter higher range: "))

for i in range(low, high+1):
    if (sum([int(j)**3 for j in str(i)])) == i :
        print(i,end="\t")



###`Problem 11`: A robot moves in a plane starting from the original point (0,0). The robot can move toward UP, DOWN, LEFT and RIGHT with a given steps.
# The trace of robot movement is shown as the following:

# UP 5
# DOWN 3
# LEFT 3
# RIGHT 2
# !

# The numbers after the direction are steps.
# `!` means robot stop there.
# Please write a program to compute the distance from current position after a sequence of movement and original point.
# If the distance is a float, then just print the nearest integer.

verticle = 0
horizontal = 0
while True:
    s = input("Enter the robot path: ")
    if s.strip() == '!':
        break

    direction = s.split()[0].lower()
    steps = int(s.split()[1])

    if direction == "up":
        verticle += steps
    elif direction == "down":
        verticle -= steps
    elif direction == "left":
        horizontal -= steps
    elif direction == "right":
        horizontal += steps

# presentXCord = horizontal
# presentYCord = verticle

print(round((horizontal**2 + verticle**2)**0.5)) #EUCLDEDIAN DISTANCE FROM ORIGIN