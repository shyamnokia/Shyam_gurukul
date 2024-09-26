# ASSIGNMENT 3
## 1.  Write a Python function to find the maximum of three numbers

# def max_num(x,y,z): # Defining new function
#     return max(x,y,z)
#
# num1 = int(input("Enter the first Number : "))
# num2 = int(input("Enter the Second Number : "))
# num3 = int(input("Enter the Third Number : "))
#
# result = max_num(num1,num2,num3)
# print (f"The maximum number of {num1} ,{num2} and {num3} is {result}") # Output : The largest number of 20 ,30 and 40 is 40


# # 2. Write a Python function to multiply all the numbers in a list.

# def multiply_list(numbers):
#     multiplication = 1
#     for num in numbers:
#         multiplication *= num
#     return multiplication
#
# num_list = [8,2,3,-1,7]
# result = multiply_list(num_list)
# print(f"The product of the numbers in {num_list} is {result}.")


## 3. Write a Python program to reverse a string.

# def reverse_string_name(string):
#     return string[::-1]
#
# input_name = "1234abcd"
# reversed_string_name = reverse_string_name(input_name)
# print(f"The reversed string name of the {input_name} is {reversed_string_name}")

## 4. Write a Python function to calculate the factorial of a number (a non-negative integer). The function accepts the number as an argument.

# Define a function named 'factorial' that calculates the factorial of a number 'n'
# def factorial(n):
#     # Check if the number 'n' is 0
#     if n == 0:
#         # If 'n' is 0, return 1 (factorial of 0 is 1)
#         return 1
#     else:
#         # If 'n' is not 0, recursively call the 'factorial' function with (n-1) and multiply it with 'n'
#         return n * factorial(n - 1)
#
# # Ask the user to input a number to compute its factorial and store it in variable 'n'
# n = int(input("Input a number to compute the factorial: "))
#
# # Print the factorial of the number entered by the user by calling the 'factorial' function
# print(factorial(n))


## 5. Write a Python function that takes a list and returns a new list with distinct elements from the first list.
# Sample List :[1,2,3,3,3,3,4,5]
# Unique List : [1, 2, 3, 4, 5]

# def unique_elements(input_list):
#     return list(set(input_list)) # Sets are particularly useful when you need to: Remove duplicates from a collection
#
# # Example usage
# sample_list = [1, 2, 3, 3, 3, 3, 4, 5]
# unique_list = unique_elements(sample_list)
# print(f"Unique List: {unique_list}")


# # 6. Write a Python function that takes a number as a parameter and checks whether the number is prime or not.

# def is_prime(n):
#     """Note : A prime number (or a prime) is a natural number greater than 1 and that has no positive divisors other than 1 and itself."""
#     """Return True if n is a prime number, otherwise False."""
#     if n <= 1:
#         return False
#     for i in range(2, int(n**0.5) + 1):
#         if n % i == 0:
#             return False
#     return True
#
# # Example usage
# number = 17
# result = is_prime(number)
# print(f"The number {number} is prime: {result}.")

## 7. Write a Python program to print the even numbers from a given list.
# Sample List: [1, 2, 3, 4, 5, 6, 7, 8, 9]
# Expected Result: [2, 4, 6, 8]

# Define a function named 'is_even_num' that takes a list 'l' as input and returns a list of even numbers
# def is_even_num(l):
#     # Create an empty list 'enum' to store even numbers
#     enum = []
#     # Iterate through each number 'n' in the input list 'l'
#     for n in l:
#         # Check if the number 'n' is even (divisible by 2 without a remainder)
#         if n % 2 == 0:
#             # If 'n' is even, append it to the 'enum' list
#             enum.append(n)
#
#     # Return the list 'enum' containing even numbers
#     return enum
#
#
# # Print the result of calling the 'is_even_num' function with a list of numbers
# print(is_even_num([1, 2, 3, 4, 5, 6, 7, 8, 9]))

## 8. Write a Python function that accepts a string and counts the number of upper and lower case letters.
# Sample String: 'The quick Brow Fox'
# Expected Output:
# No. of Upper case characters : 3
# No. of Lower case Characters : 12
#
# def count_case(string):
#     upper_count = 0
#     lower_count = 0
#
#     for char in string:
#         if char.isupper():
#             upper_count += 1
#         elif char.islower():
#             lower_count += 1
#
#     return upper_count, lower_count
#
# # Example usage
# input_string = "The quick Brow Fox"
# upper, lower = count_case(input_string)
# print(f"Original String Name is :  {input_string}")
# print(f"Uppercase letters: {upper}, Lowercase letters: {lower}.")

## 9. Write a Python function to sum all the numbers in a list.
# Sample List : (8, 2, 3, 0, 7)
# Expected Output : 20

# def sum_of_all_numbers(nums):
#     total=sum(nums)
#     return total
#
# list_of_numbers = [1,2,3,4,5,6]
#
# total_sum_of_list = sum_of_all_numbers(list_of_numbers)
# print(f" The input list of numbers are : {list_of_numbers}")
# print(f" The total sum of all numbers in list are : {total_sum_of_list}")


## 10. Write a Python function that checks whether a passed string is a palindrome or not.
# Note: A palindrome is a word, phrase, or sequence that reads the same backward as forward, e.g., madam or nurses run

def is_palindrome(s):
    """Check if the given string is a palindrome."""
    # Normalize the string by removing spaces and converting to lowercase
    normalized_str = s.replace(" ", "").lower()
    # Check if the string is equal to its reverse
    return normalized_str == normalized_str[::-1]

# Example usage
input_string = "Python Gurukul training Program"
result = is_palindrome(input_string)
print(f"The string '{input_string}' is a palindrome: {result}.")










