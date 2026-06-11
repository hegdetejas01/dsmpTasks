# Task 3 

### `Problem 1` - Print the following pattern. Write a program to use for loop to print the following reverse number pattern.

# 5 4 3 2 1
# 4 3 2 1
# 3 2 1
# 2 1
# 1

for i in range(1,6):
    for j in range(6-i,0,-1):
        print(j, end=" ")
    print()


### `Problem 2`: Print the following pattern.

# *
# * *
# * * *
# * * * *
# * * * * *
# * * * *
# * * *
# * *
# *

for i in range(1,6):
    for j in range(1,i+1):
        print("* ", end= " ")
    print()

for i in range(1,5):
    for j in range(5-i,0,-1):
        print("* ", end = " ")
    print()



### `Problem 3`:Write a program to pring the following pattern

#     *
#   * * *
# * * * * *

### `Problem 4`:Write a program to print the following pattern

# 1
# 2 1
# 3 2 1
# 4 3 2 1
# 5 4 3 2 1

for i in range(1,6):
    for j in range(1,i+1):
        print(j, end=" ")
    print()


### `Problem 5`: Write a Python Program to Find the Sum of the Series till the nth term:

# 1 + x^2/2 + x^3/3 + … x^n/n
# n will be provided by the user

# n = int(input("Enter the value of n: "))
# x = int(input("Enter the value of x: "))
# s = 1.0

# if n>2:
#     for i in range(2,n+1):
#         s += x**i/i
# elif n == 2:
#     s += x**2/2

# print(s)



# Problem 6

# x = int(input("Enter the value of X : "))
# n = 7
# s = 0

# for i in range(1, n+1): #calculates till n-1 i.e 6th term, but it will be thr 7th term because s is initialised to 1st term
#     s += (((x-1)/x)**i)/i

# print(s)



### `Problem 7` - Find the sum of the series upto n terms.

# Write a program to calculate the sum of series up to n term. For example, if n =5 the series will become 2 + 22 + 222 + 2222 + 22222 = 24690. Take the user input and then calculate. And the output style should match which is given in the example.

# n = int(input("Enter the value of n: "))
# s = 0

# def getNum(i):
#     digit = '2'
#     return(int(digit*i))

# for i in range(1,n+1):
#     addFactor = getNum(i)
#     print(addFactor)
#     s += addFactor

# print(s)



###`Problem 8`: Write a program to print all the unique combinations of 1,2,3 and 4

# Output

# 1 2 3 4
# 1 2 4 3
# 1 3 2 4
# 1 3 4 2
# 1 4 2 3
# 1 4 3 2
# 2 1 3 4
# 2 1 4 3
# 2 3 1 4
# 2 3 4 1
# 2 4 1 3
# .
# .
# and so on

nums = [1, 2, 3, 4]
for i in nums:
    for j in nums:
        for k in nums:
            for l in nums:
                # Ensure each digit is used only once
                if i != j and i != k and i != l and j != k and j != l and k != l:
                    print(i, j, k, l)




### **Problem 11:** Create Short Form from initial character

# Given a string create short form ofthe string from Initial character. Short form should be capitalised.

# sentence = input("Enter the string: ").strip().split()
# shortForm = ''
# for word in sentence:
#     shortForm += word[0]

# print(shortForm.upper())




###`Problem 12`: Append second string in the middle of first string

# campusx
# data

# Output:
# camdatapusx

# string1 = input("Enter first string: ")
# string2 = input("Enter second string: ")
# indexToInsert = len(string1)//2
# res = string1[:indexToInsert] + string2 + string1[indexToInsert:]
# print(res)





### ``Problem 13``:Given string contains a combination of the lower and upper case letters. Write a program to arrange the characters of a string so that all lowercase letters should come first.

# Input: 
# str1 = PyNaTive

# Expected Output:
# yaivePNT

# s = input("Enter the string: ")
# u = [i for i in s if i.isupper()]
# l = [i for i in s if i.islower()]
# print("".join(l+u))



### `Problem 14:`Take a alphanumeric string input and print the sum and average of the digits that appear in the string, ignoring all other characters.

# Input:
# hel123O4every093

# Output:
# Sum: 22
# Avg: 2.75

# s = input("Enter the string: ")
# tot = [int(i) for i in s if i.isnumeric()]
# print("Sum:",sum(tot))
# print("Avg:",sum(tot)/len(tot))



### `Problem 15:` Removal of all characters from a string except integers

# Given:
# str1 = 'I am 25 years and 10 months old'

# Expected Output:
# 2510

# s = input("Enter the string: ")
# num = [i for i in s if i.isnumeric()]
# print("".join(num))





### `Problem 16`: Check whether the string is Symmetrical.

# **Statement:** Given a string. the task is to check if the string is symmetrical or not. A string is said to be symmetrical if both the halves of the string are the same.

# Input:
# khokho

# Output:
# The entered string is symmetrical

# s = input("Enter the string: ")
# mid = len(s)//2
# if s[:mid] == s[mid:]:
#     print("Symnetric")
# else: print("Not symnettric")




### `Problem 17`: Reverse words in a given String
# **Statement:** We are given a string and we need to reverse words of a given string.

s = input("Enter the string: ").strip().split()
s = s[::-1]
print(" ".join(s))








