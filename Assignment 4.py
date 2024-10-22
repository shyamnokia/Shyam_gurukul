## OOPs Concept from Python
# # Assignments from the Class
#
# # Create a class
# class Car:
#     name = "Creta"
#     company = "Hyundai"
#     model = "2023"
#     colour = "White"
#     transmission = "Manual"
#
# #printing the class
# c1= Car()
# print(c1)
# print("You car belongs to : ", c1.company )
# print(c1.name,c1.company)

# Q1 : Write a Python program to create a class named Car.
# Define attributes like brand, model, and year.
# Create an object of the class and display the details of the car?

# class car:
#     brand = 'Hyundai'
#     model = 'Knight Edition'
#     year = '2024'
#
# my_car = car()
# print(my_car)
# print(car.brand,car.model,car.year)


## Q2 : Create a class Student with attributes name, roll_number, and marks. Define a constructor to initialize these attributes and a method display_info() to print the student's details?

# class Student:
#     def __init__(self, name, roll_number, marks):
#         self.name = name
#         self.roll_number = roll_number
#         self.marks = marks
#
#     def display_info(self):
#         print(f"Student Details:\nName: {self.name}\nRoll Number: {self.roll_number}\nMarks: {self.marks}")
#
# # Creating an object of the Student class
# student1 = Student("Alice", 101, 95)
#
# # Displaying the student's details
# student1.display_info()

## Q3 : Create a class Rectangle with attributes length and breadth.
# Include methods to calculate the area and perimeter of the rectangle.
# Create multiple objects and display the area and perimeter for each?

# class Rectangle:
#     def __init__(self, length, breadth):
#         self.length = length
#         self.breadth = breadth
#
#     def area(self):
#         return self.length * self.breadth
#
#     def perimeter(self):
#         return 2 * (self.length + self.breadth)
#
# # Creating multiple objects of the Rectangle class
# rectangle1 = Rectangle(5, 3)
# rectangle2 = Rectangle(7, 4)
# rectangle3 = Rectangle(10, 6)
#
# # Displaying the area and perimeter for each rectangle
# rectangles = [rectangle1, rectangle2, rectangle3]
#
# for i, rect in enumerate(rectangles, start=1):
#     print(f"Rectangle {i}:")
#     print(f"  Area: {rect.area()}")
#     print(f"  Perimeter: {rect.perimeter()}\n")


## Q4 : Write a class Circle with an attribute radius and methods get_area() and get_circumference().
# These methods should return the area and circumference of the circle, respectively ?

# import math
#
# class Circle:
#     def __init__(self, radius):
#         self.radius = radius
#
#     def get_area(self):
#         return math.pi * (self.radius ** 2)
#
#     def get_circumference(self):
#         return 2 * math.pi * self.radius
#
# # Creating an object of the Circle class
# circle1 = Circle(5)
#
# # Displaying the area and circumference
# print(f"Circle with radius {circle1.radius}:")
# print(f"  Area: {circle1.get_area():.2f}")
# print(f"  Circumference: {circle1.get_circumference():.2f}")

## Q5 : Create Account class with 2 attributes - balance & account no.
# Create methods for debit, credit & printing the balance.

# class Account:
#     def __init__(self, account_no, initial_balance=0):
#         self.account_no = account_no
#         self.balance = initial_balance
#
#     def credit(self, amount):
#         """Add amount to the balance."""
#         if amount > 0:
#             self.balance += amount
#             print(f"Credited: ${amount:.2f}. New balance: ${self.balance:.2f}")
#         else:
#             print("Credit amount must be positive.")
#
#     def debit(self, amount):
#         """Deduct amount from the balance if sufficient funds are available."""
#         if amount > 0:
#             if amount <= self.balance:
#                 self.balance -= amount
#                 print(f"Debited: ${amount:.2f}. New balance: ${self.balance:.2f}")
#             else:
#                 print("Insufficient funds.")
#         else:
#             print("Debit amount must be positive.")
#
#     def print_balance(self):
#         """Print the current balance."""
#         print(f"Account No: {self.account_no}, Current Balance: ${self.balance:.2f}")
#
# # Example usage
# account1 = Account("123456789", 1000)
#
# # Print initial balance
# account1.print_balance()
#
# # Perform credit and debit operations
# account1.credit(200)
# account1.debit(150)
# account1.debit(1200)  # This should show insufficient funds
#
# # Print final balance
# account1.print_balance()



## Q6 : Create a class Employee with an attribute employee_count (class variable) and a class method increment_employee_count() to increase the count whenever a new employee object is created.
# Show the updated employee count after creating new objects.
#
# class Employee:
#     # Class variable to keep track of the number of employees
#     employee_count = 0
#
#     def __init__(self, name):
#         self.name = name
#         Employee.increment_employee_count()
#
#     @classmethod
#     def increment_employee_count(cls):
#         """Increment the employee count."""
#         cls.employee_count += 1
#
#     @classmethod
#     def get_employee_count(cls):
#         """Return the current employee count."""
#         return cls.employee_count
#
# # Example usage
# employee1 = Employee("Alice")
# print(f"Current Employee Count: {Employee.get_employee_count()}")
#
# employee2 = Employee("Bob")
# print(f"Current Employee Count: {Employee.get_employee_count()}")
#
# employee3 = Employee("Charlie")
# print(f"Current Employee Count: {Employee.get_employee_count()}")


## Q7 : Create a class Book with attributes title, author, and price.
# Write a constructor that allows the user to either initialize all three attributes or just the title and author (in which case the price should be set to a default value).
# Display the details of the book using an instance method.

# class Book:
#     def __init__(self, title, author, price=9.99):
#         self.title = title
#         self.author = author
#         self.price = price
#
#     def display_details(self):
#         """Display the details of the book."""
#         print(f"Title: {self.title}")
#         print(f"Author: {self.author}")
#         print(f"Price: ${self.price:.2f}")
#
# # Example usage
# book1 = Book("1984", "George Orwell", 14.99)
# book2 = Book("To Kill a Mockingbird", "Harper Lee")  # Default price will be used
#
# # Displaying the details of the books
# print("Book 1 Details:")
# book1.display_details()
#
# print("\nBook 2 Details:")
# book2.display_details()

## Q8 : Write a class TemperatureConverter with an instance method celsius_to_fahrenheit(celsius) that takes a temperature in Celsius and returns its Fahrenheit equivalent.
# Create an object of the class and use the method to convert various temperatures.

# class TemperatureConverter:
#     def celsius_to_fahrenheit(self, celsius):
#         """Convert Celsius to Fahrenheit."""
#         return (celsius * 9/5) + 32
#
# # Creating an object of the TemperatureConverter class
# converter = TemperatureConverter()
#
# # Example temperatures in Celsius to convert
# temperatures_celsius = [0, 20, 37, 100]
#
# # Converting and displaying the temperatures
# for temp in temperatures_celsius:
#     fahrenheit = converter.celsius_to_fahrenheit(temp)
#     print(f"{temp}°C is equivalent to {fahrenheit:.2f}°F")


## Q9 : Create a class Time with attributes hours and minutes.
# Add a method add_time() that takes another Time object, adds its values to the current object, and returns a new Time object with the resulting sum.
#
# class Time:
#     def __init__(self, hours=0, minutes=0):
#         self.hours = hours
#         self.minutes = minutes
#         self.normalize_time()
#
#     def normalize_time(self):
#         """Normalize the time values to ensure minutes are less than 60."""
#         if self.minutes >= 60:
#             extra_hours = self.minutes // 60
#             self.hours += extra_hours
#             self.minutes %= 60
#
#     def add_time(self, other_time):
#         """Add another Time object to the current one and return a new Time object."""
#         total_hours = self.hours + other_time.hours
#         total_minutes = self.minutes + other_time.minutes
#         return Time(total_hours, total_minutes)
#
#     def __str__(self):
#         """Return a string representation of the time in HH:MM format."""
#         return f"{self.hours:02}:{self.minutes:02}"
#
# # Example usage
# time1 = Time(1, 30)  # 1 hour and 30 minutes
# time2 = Time(2, 45)  # 2 hours and 45 minutes
#
# # Adding time1 and time2
# result_time = time1.add_time(time2)
#
# # Displaying the results
# print(f"Time 1: {time1}")
# print(f"Time 2: {time2}")
# print(f"Resulting Time: {result_time}")


## Q10 : Create a class EmployeeSalary with class variables basic_salary and bonus_percentage.
# Write a class method set_bonus_percentage() to change the bonus percentage for all employees.
# Create an instance method calculate_total_salary() to calculate and return the total salary (basic + bonus) for a specific employee.
#
# class EmployeeSalary:
#     # Class variables
#     basic_salary = 50000  # Default basic salary
#     bonus_percentage = 10  # Default bonus percentage
#
#     @classmethod
#     def set_bonus_percentage(cls, new_percentage):
#         """Set a new bonus percentage for all employees."""
#         cls.bonus_percentage = new_percentage
#         print(f"Bonus percentage updated to {cls.bonus_percentage}%")
#
#     def __init__(self, name):
#         self.name = name
#
#     def calculate_total_salary(self):
#         """Calculate the total salary (basic + bonus) for this employee."""
#         bonus_amount = (EmployeeSalary.basic_salary * EmployeeSalary.bonus_percentage) / 100
#         total_salary = EmployeeSalary.basic_salary + bonus_amount
#         return total_salary
#
# # Example usage
# employee1 = EmployeeSalary("Alice")
# employee2 = EmployeeSalary("Bob")
#
# # Displaying total salaries before changing the bonus percentage
# print(f"{employee1.name}'s Total Salary: ${employee1.calculate_total_salary():.2f}")
# print(f"{employee2.name}'s Total Salary: ${employee2.calculate_total_salary():.2f}")
#
# # Change the bonus percentage
# EmployeeSalary.set_bonus_percentage(15)
#
# # Displaying total salaries after changing the bonus percentage
# print(f"{employee1.name}'s Total Salary: ${employee1.calculate_total_salary():.2f}")
# print(f"{employee2.name}'s Total Salary: ${employee2.calculate_total_salary():.2f}")









