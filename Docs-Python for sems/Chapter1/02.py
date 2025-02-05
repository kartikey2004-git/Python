# Python Data Types

# Built-in Data Types

# In programming, data type is an important concept.

# Variables can store data of different types, and different types can do different things.

# Mapping Type: workings on loop 



# Text Type:	str
# Numeric Types:	int, float, complex
# Sequence Types:	list, tuple, range
# Mapping Type:	dict

# Boolean Type:	bool
# Binary Types:	bytes
# None Type:	NoneType

# a = () tuple
# b = [] list
# c = {} dict


# Getting the Data Type

# You can get the data type of any object by using the type() function:

# x = 5
# print(type(x))



# for i in range(5):
#     print(i)

# Dictionary stores the key value pair where we can define the all types of data like int , str


# {
#   "name1":"raju",
#   "class":6,
#   "name2": 6.0
# }

# Sets are types which stores similar type of variable

# {
#   "apple", "banana", "cherry"
# }


# x = b"hello"
# print(type(x)) # datatypes bytes binary

# Python Numbers
# There are three numeric types in Python:

# int
# float
# complex



# Variables of numeric types are created when you assign a value to them:

# x = 1    # int
# y = 2.8  # float
# z = 1j   # complex
# print(type(x))
# print(type(y))
# print(type(z))


# Type Conversion

# You can convert from one type to another with the int(), float(), and complex() methods:


# x = 1   
# y = 2.8  
# z = 1j   

# #convert from int to float:
# a = float(x)

# #convert from float to int:
# b = int(y)

# #convert from int to complex:
# c = complex(x)

# print(a)
# print(b)
# print(c)

# print(type(a))
# print(type(b))
# print(type(c))


# Note: You cannot convert complex numbers into another number type.




# Random Number

# Import the random module

# but Python has a built-in module called random that can be used to make random numbers


import random 

# print(random.randrange(1,10))


# print(random.random()) # random floating value generate kr skte hai

# random integer generates
# b = random.randint(1,10)
# print(b)


# Specify a Variable Type
# Python is an object-orientated language

# Casting in python is therefore done using constructor functions



# Python Strings

# Strings in python are surrounded by either single quotation marks, or double quotation marks.


# print("It's alright")
# print("He is called 'Johnny'")
# print('He is called "Johnny"')


# Multiline Strings
# You can assign a multiline string to a variable by using three quotes:

# a = """Lorem ipsum dolor sit amet,
# consectetur adipiscing elit,
# sed do eiusmod tempor incididunt
# ut labore et dolore magna aliqua."""
# print(a)


# a = """hello"""
# print(a)







# Strings are Arrays

# strings in Python are arrays of bytes representing unicode characters.

# a = "hello"
# print(a[0])


# Looping Through a String

# Since strings are arrays, we can loop through the characters in a string, with a for loop.


# for x in "banana":
#   print(x)


# String Length

# To get the length of a string, use the len() function.

# a = " Hello, World!"
# print(len(a))


# Check String

# To check if a certain phrase or character is present in a string, we can use the keyword in.



# txt = "The best things in life are free!"
# print("free" in txt)


# txt = "The best things in life are free!"
# if "free" in txt:
#   print("Yes, 'free' is present.")



# Check if NOT

# To check if a certain phrase or character is NOT present in a string, we can use the keyword not in.



# txt = "The best things in life are free!"
# if "expensive" not in txt:
#   print("No, 'expensive' is NOT present.")


# Python - Slicing Strings

# You can return a range of characters by using the slice syntax.


# Specify the start index and the end index, separated by a colon, to return a part of the string.


# b = "Hello, World!"
# print(b[2:5])


#  The first character has index 0.


# Slice From the Start

# By leaving out the start index, the range will start at the first character:

# b = "Hello, World!"
# print(b[:5])


# Slice To the End

# By leaving out the end index, the range will go to the end:

# b = "Hello, World!"
# print(b[2:])


# Negative Indexing
# Use negative indexes to start the slice from the end of the string:



# b = "Hello, World!"
# print(b[-5:-2])

# Get the characters:

# From: "o" in "World!" (position -5)

# To, but not included: "d" in "World!" (position -2):

# # here ! at index -1 



# Python - Modify Strings

# Python has a set of built-in methods that you can use on strings.

# Upper Case
# The upper() method returns the string in upper case:

# a = "Hello, World!"
# print(a.upper())


# Lower Case

# The lower() method returns the string in lower case:

# a = "Hello, World!"
# print(a.lower())




# Remove Whitespace

# Whitespace is the space before and/or after the actual text, and very often you want to remove this space.

# The strip() method removes any whitespace from the beginning or the end:

# a = " Hello, World! "
# print(a.strip())




# Replace String

# The replace() method replaces a string with another string:

# a = "Hello, World!"
# print(a.replace("l","a"))



# Split String

# The split() method returns a list where the text between the specified separator becomes the list items.

# The split() method splits the string into substrings if it finds instances of the separator

# a = "I am normal person"
# print(a.split(" "))

# Output : ['I', 'am', 'normal', 'person']

# split ke andar parameter jata hai delimeter/separator




# Python - String Concatenation


# To concatenate, or combine, two strings you can use the + operator.

# merge variable a and b into variable c


# a = "Hello"
# b = "World"
# c = a + b
# print(c)


# a = "Hello"
# b = "World"
# c = a + " " + b
# print(c)



# Python - Format - Strings
# String Format


# age = 36
# txt = "My name is John, I am " + age
# print(txt)
#error


# But we can combine strings and numbers by using f-strings or the format() method!

# To specify a string as an f-string

#  simply put an f in front of the string literal, and add curly brackets {} as placeholders for variables and other operations.


# age = 36
# print(f"my name is billu {age}")



# a = 78
# b = 12
# sum = a+b
# print(f"sum of {a} and {b} is {sum} ")


# name = "nikhil"
# work_experince = 4
# videos_made = 35
# print(f"My name is {name} and my work experince is {work_experince} and video that I made {videos_made} videos")


# a = 4
# b = 6
# print(f"sum of {a} and {b} is {a+b}")

# scope open krdiya or placeholders 



# Placeholders and Modifiers
# A placeholder can contain variables, operations, functions, and modifiers to format the value.

# price = 59
# txt = f"The price is {price} dollars"
# print(txt)



# A placeholder can include a modifier to format the value.

# A modifier is included by adding a colon : followed by a legal formatting type, like .2f which means fixed point number with 2 decimals:


# price = 59.0006
# txt = f"The price is {price:.2f} dollars"
# print(txt)



# txt = f"The price is {20 * 59} dollars"
# print(txt)