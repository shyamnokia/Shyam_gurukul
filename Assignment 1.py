
### Assignment(Variable and list): ###

# 1.Define a variable as Integer(1) ,Float(1.0) and String(‘1’) and print and return the value and type of variable.

a=1
b=1.0
c='1'
print(a,type(a))
print(b,type(b))
print(c,type(c))

# 2.Redeclare the same variable as another number.(2,2.0 and ‘2’) and share your observation on result.

a=2
b=2.0
c='2'
print(a,type(a))
print(b,type(b))
print(c,type(c))

# 3. Assigning a single value to several variables simultaneously with “=” operators.(a=b=c=10) and print the values of a,b and c.

a=b=c=10
print("a-",a,"b-",b,"c-",c)


# 4.Assign two variables a and b as integer and print the sum of a+b.

a=30
b=40
print(a+b)


# 5.Write a Python program to create a list with five different fruits. eg:fruits = ["apple", "banana", "cherry", "date", "elderberry"]?

fruits = ["apple", "banana", "cherry", "date", "elderberry"]
print(fruits)

# 6. How do you access the second and fourth elements from the list.

print(fruits[1])
print(fruits[3])

# 7.Modify the third element in the list numbers = [10, 20, 30, 40, 50] to 35.

numbers = [10, 20, 30, 40, 50]
numbers[2]=35
print(numbers)


### Tupple ###

# Create a Tuple:
# How do you create a tuple with the following elements: "red", "green", "blue"?

colors = ("red", "green", "blue")
print(colors)

# Access Elements in a Tuple:
# How do you access the first and last elements in the tuple colors = ("red", "green", "blue", "yellow")?

colors = ("red", "green", "blue", "yellow")
print(colors[0])
print(colors[-1])

# Immutable Nature of Tuples:
# What happens if you try to change the second element of the tuple colors = ("red", "green", "blue")?

colors = ("red", "green", "blue")
#colors[1]="orange"
#TypeError: 'tuple' object does not support item assignment

# Tuple Unpacking:
# Given the tuple coordinates = (10, 20, 30), write a Python program to unpack it into three variables x, y, and z.

coordinates = (10, 20, 30)
x,y,z=coordinates
print(x,y,z)

# Check Element in Tuple:
# Write a Python program to check if the element "blue" is present in the tuple colors = ("red", "green", "blue").

colors = ("red", "green", "blue")
print("blue" in colors)

# Tuple Length:
# Write a Python program to find the length of the tuple days = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday")

days = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday")
print(len(days))


### Dictionary ###

# Create a Dictionary:
# Create a dictionary where the keys are student names and the values are their grades. For example:
# python # {"Alice": 85, "Bob": 90, "Charlie": 78}

students={"Alice": 85, "Bob": 90, "Charlie": 78}
print(students)

# Access Dictionary Values:
# How do you access Bob's grade from the dictionary students = {"Alice": 85, "Bob": 90, "Charlie": 78}?

print(students['Bob'])


# Add and Remove Key-Value Pairs:
# Add a new student "David": 92 to the dictionary students = {"Alice": 85, "Bob": 90, "Charlie": 78} and remove "Charlie" from the dictionary.

students['David']=92
print(students)

# Update Dictionary Values:
# Write a Python program to update Bob's grade to 95 in the dictionary students = {"Alice": 85, "Bob": 90, "Charlie": 78}.

students.pop("Charlie")
print(students)
students['Bob']=95
print(students)

# Check if Key Exists in a Dictionary:
# Write a Python program to check if "Alice" is a key in the dictionary students = {"Alice": 85, "Bob": 90, "Charlie": 78}.

print('Alice' in students.keys())

# Dictionary Length:
# Write a Python program to find the number of key-value pairs in the dictionary students = {"Alice": 85, "Bob": 90, "Charlie": 78}.

print(len(students))
















