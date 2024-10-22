
## Assignment 1: Static Methods
# Create a class MathOperations that contains:
# A static method add_numbers that takes two arguments and returns their sum.
# A static method multiply_numbers that takes two arguments and returns their product."
#
# class MathOperations:
#     @staticmethod
#     def add_numbers(a, b):
#         """Return the sum of two numbers."""
#         return a + b
#
#     @staticmethod
#     def multiply_numbers(a, b):
#         """Return the product of two numbers."""
#         return a * b
#
# # Example usage
# num1 = 5
# num2 = 3
#
# sum_result = MathOperations.add_numbers(num1, num2)
# product_result = MathOperations.multiply_numbers(num1, num2)
#
# print(f"The sum of {num1} and {num2} is: {sum_result}")
# print(f"The product of {num1} and {num2} is: {product_result}")

## Assignment 2: Class Methods

# Create a class Person that keeps track of the number of people created. The class should have:
# A class variable count to count instances of the class.
# A class method get_count that returns the current count.
#
# class Person:
#     # Class variable to keep track of the number of people created
#     count = 0
#
#     def __init__(self):
#         """Increment the count whenever a new Person object is created."""
#         Person.count += 1
#
#     @classmethod
#     def get_count(cls):
#         """Return the current count of Person instances."""
#         return cls.count
#
# # Example usage
# person1 = Person()
# person2 = Person()
# person3 = Person()
#
# # Getting the current count of Person instances
# print(f"Number of Person instances created: {Person.get_count()}")


## Assignment 3: Using Both Static and Class Methods
#
# Create a class TemperatureConverter with the following:
# A static method celsius_to_fahrenheit that converts Celsius to Fahrenheit.
# A class method info that returns a message about temperature conversions.

# class TemperatureConverter:
#     @staticmethod
#     def celsius_to_fahrenheit(celsius):
#         """Convert Celsius to Fahrenheit."""
#         return (celsius * 9/5) + 32
#
#     @classmethod
#     def info(cls):
#         """Return information about temperature conversions."""
#         return "This class provides methods to convert temperatures between Celsius and Fahrenheit."
#
# # Example usage
# celsius_temp = 25
# fahrenheit_temp = TemperatureConverter.celsius_to_fahrenheit(celsius_temp)
# conversion_info = TemperatureConverter.info()
#
# print(f"{celsius_temp}°C is equivalent to {fahrenheit_temp:.2f}°F.")
# print(conversion_info)


## Assignment 4: Single Inheritance

# Create two classes:
# Animal with a method sound that prints "Animal sound".
# Dog that inherits from Animal and overrides the sound method to print "Bark".

# class Animal:
#     def sound(self):
#         """Print the sound made by the animal."""
#         print("Animal sound")
#
# class Dog(Animal):
#     def sound(self):
#         """Override the sound method to print the dog's sound."""
#         print("Bark")
#
# # Example usage
# animal = Animal()
# animal.sound()  # Output: Animal sound
#
# dog = Dog()
# dog.sound()     # Output: Bark


## Assignment 5: Multiple Inheritance

# Create two classes:
# Bird with a method fly that prints "Flying".
# Fish with a method swim that prints "Swimming".
# A class Duck that inherits from both Bird and Fish.

# class Bird:
#     def fly(self):
#         """Prints the flying action of the bird."""
#         print("Flying")

# class Fish:
#     def swim(self):
#         """Prints the swimming action of the fish."""
#         print("Swimming")
#
# class Duck(Bird, Fish):
#     def quack(self):
#         """Prints the quacking sound of the duck."""
#         print("Quack")
#
# # Example usage
# duck = Duck()
# duck.fly()    # Output: Flying
# duck.swim()   # Output: Swimming
# duck.quack()  # Output: Quack

 ## Assignment 6: Abstract Class

# Use the abc module to create an abstract class Shape that contains:
# An abstract method area().
# Two concrete classes Circle and Rectangle that inherit from Shape and implement the area method.

#
# from abc import ABC, abstractmethod
# import math
#
# class Shape(ABC):
#     @abstractmethod
#     def area(self):
#         """Calculate the area of the shape."""
#         pass
#
# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius
#
#     def area(self):
#         """Calculate the area of the circle."""
#         return math.pi * (self.radius ** 2)
#
# class Rectangle(Shape):
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#
#     def area(self):
#         """Calculate the area of the rectangle."""
#         return self.width * self.height
#
# # Example usage
# circle = Circle(5)
# rectangle = Rectangle(4, 6)
#
# print(f"Area of the circle: {circle.area():.2f}")
# print(f"Area of the rectangle: {rectangle.area()}")

## Assignment 7: Encapsulation

# Create a class BankAccount that uses encapsulation:
# Private attributes _balance.
# Public methods deposit() and withdraw() that modify _balance safely.
#
# class BankAccount:
#     def __init__(self, initial_balance=0):
#         self._balance = initial_balance  # Private attribute
#
#     def deposit(self, amount):
#         """Deposit a specified amount to the account."""
#         if amount > 0:
#             self._balance += amount
#             print(f"Deposited: ${amount:.2f}. New balance: ${self._balance:.2f}")
#         else:
#             print("Deposit amount must be positive.")
#
#     def withdraw(self, amount):
#         """Withdraw a specified amount from the account."""
#         if amount > 0:
#             if amount <= self._balance:
#                 self._balance -= amount
#                 print(f"Withdrawn: ${amount:.2f}. New balance: ${self._balance:.2f}")
#             else:
#                 print("Insufficient funds.")
#         else:
#             print("Withdrawal amount must be positive.")
#
#     def get_balance(self):
#         """Return the current balance."""
#         return self._balance
#
# # Example usage
# account = BankAccount(1000)
#
# # Display initial balance
# print(f"Initial balance: ${account.get_balance():.2f}")
#
# # Deposit and withdraw
# account.deposit(200)
# account.withdraw(150)
# account.withdraw(1200)  # This should show insufficient funds
#
# # Display final balance
# print(f"Final balance: ${account.get_balance():.2f}")

## Assignment 8: Polymorphism with Method Overriding

# Create two classes Cat and Dog with a method speak().
# The Dog class should implement speak() to print "Woof".
# The Cat class should implement speak() to print "Meow".

# class Dog:
#     def speak(self):
#         """Print the sound a dog makes."""
#         print("Woof")
#
# class Cat:
#     def speak(self):
#         """Print the sound a cat makes."""
#         print("Meow")
#
# # Example usage
# dog = Dog()
# cat = Cat()
#
# dog.speak()  # Output: Woof
# cat.speak()  # Output: Meow

## Assignment 9: Polymorphism with Method Overloading

# Create a class Calculator with a method add() that:
# Can accept 2 or 3 arguments and returns their sum.
# Hint: Use default parameters to handle method overloading in Python.
#
#
# class Calculator:
#     def add(self, a, b, c=0):
#         """Return the sum of two or three numbers."""
#         return a + b + c
#
# # Example usage
# calculator = Calculator()
#
# # Adding two numbers
# sum_two = calculator.add(5, 10)
# print(f"Sum of 5 and 10: {sum_two}")  # Output: 15
#
# # Adding three numbers
# sum_three = calculator.add(5, 10, 15)
# print(f"Sum of 5, 10, and 15: {sum_three}")  # Output: 30


## Assignment 10: Multilevel Inheritance

# Create three classes:
# LivingBeing with a method breathe() that prints "Breathing".
# Mammal that inherits from LivingBeing and adds a method walk() that prints "Walking".
# Human that inherits from Mammal and adds a method think() that prints "Thinking".

#
# class LivingBeing:
#     def breathe(self):
#         """Prints the breathing action of a living being."""
#         print("Breathing")
#
# class Mammal(LivingBeing):
#     def walk(self):
#         """Prints the walking action of a mammal."""
#         print("Walking")
#
# class Human(Mammal):
#     def think(self):
#         """Prints the thinking action of a human."""
#         print("Thinking")
#
# # Example usage
# human = Human()
#
# # Calling methods from the classes
# human.breathe()  # Output: Breathing
# human.walk()     # Output: Walking
# human.think()    # Output: Thinking
