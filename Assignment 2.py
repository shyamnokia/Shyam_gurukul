

# # OPERATORS IN PYTHON
# # Write a Program to find maximum of three numbers
#
# num1 = int(input("Enter the First Number : "))
# num2 = int(input("Enter the Second Number : "))
# num3 = int(input("Enter the Third Number : "))
# max = num1 if num1 > num2 and num2 > num3 else num2 if num2 > num3 else num3
# print("Maximum Value is : ", max)

# Flow Control - Exercise

# Write a program to find biggest of given 2 numbers from the keyboard

# n1 = int(input("Enter the First Number : "))
# n2 = int(input("Enter the Second Number : "))
# if n1 > n2:
#     print("Biggest Number is : ", n1)
# else:
#     print ("Biggest Number is : ", n2)

# Write a program to check whether the given number is in between 1 and 10?

# n=int(input("Enter the Number: "))
#
# if n>=1 and n<=10:
#     print("The number n  is in between 1 to 10 ")
# else:
#     print("The number n is not in between 1 to 10")


### ASSIGNMENT ###

# Question 1: Write a Python program that takes two numbers as input from the user and performs the following operations:

# a= int(input("Enter your first number : "))
# b= int(input("Enter your second number : "))
#
# # Addition
# add = a+b
# print("The addition of two numbers is : ", add)
#
# # Subtraction
# sub = a-b
# print("The subtraction of two numbers is : ", sub)
#
# # Multiplication
# mul = a*b
# print("The multiplication of two numbers is : ", mul)
#
# # Division
# div = a/b
# print("The division of two numbers is : ", div)
#
# # Modulus
# mod = a%b
# print("The modulus of two numbers is : ", mod)

## Question 2: Write a Python program that checks whether a given number is even or odd using the modulus operator.

# num = int(input("Enter a number: "))
# if num % 2 == 0:
#     print("Even")
# else:
#     print("Odd")


## Question 3: Write a Python program that takes a number as input from the user and checks if it is positive, negative, or zero.

# num = int(input("Enter a number: "))
# if num > 0:
#     print("Positive Number")
# elif num < 0:
#     print("Negative number")
# else:
#     print("Number equals to zero")

## Question 4: Write a Python program that calculates the grade of a student based on the marks entered by the user.
# The grading scale is as follows:
# 90 and above: A
# 80 - 89: B
# 70 - 79: C
# 60 - 69: D
# Below 60: F

# marks = int(input("Enter the student marks : "))
#
# if marks > 90:
#     print("The student got A grade")
# elif marks >= 80 and marks <= 89:
#     print("The student got B grade")
# elif marks >= 70 and marks <= 79:
#     print("The student got C grade")
# elif marks >= 60 and marks <= 69:
#     print("The student got D grade")
# elif marks < 60:
#     print("The student got F grade")
# else:
#     print("Enter the valid marks")

## Question 5: Write a Python program to create a text file called sample.txt and
# write the sentence "Hello, this is a sample file." to the file.
# Then, read and display the content from the file.

filename = open("sample1.txt", "w")
filename.write("Hello, This is a Sample file")
filename = open("sample1.txt", "r")
content = filename.read()
print(content)


## Question 6: Write a Python program that reads a text file called data.txt and counts the number of words in the file.

# I'm having few doubts on File Handling, Thi exercise i will do it later and submit the changes to git.


## Question 7: Write a Python program to print the numbers from 1 to 10 using a for loop.

# print("Numbers list from 1 to 10")
# for i in range(1,11):
#     print(i)


## Question 8: Write a Python program to display the multiplication table of a number entered by the user using a for loop.

# number = int(input("Enter a number to display its multiplication table: "))
# print(f"Multiplication table for {number}:")
# for i in range(1, 11):
#     result = number * i
#     print(f"{number} x {i} = {result}")















