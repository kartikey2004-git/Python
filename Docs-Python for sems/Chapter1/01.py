

print("Hello, World!")

# Python is a popular programming language. It was created by Guido van Rossum, and released in 1991.

# Python is an interpreted programming language


# Indentation refers to the spaces at the beginning of a code line.

# Where in other programming languages the indentation in code is for readability only, the indentation in Python is very important.


# Python uses indentation to indicate a block of code.

# Python Variables

#  variables are created when you assign a value to it

# x = 5
# y = "hi"

# comments in python

#This is a comment
#written in
#more than just one line


"""
This is a comment
written in
more than just one line
"""

# Variables

# Variables are containers for storing data values.

# x = 5
# y = "John"
# print(x,y)
# print(y)


# x = 4 # int datatype
# x = "Sally" # x is now of type str

# x = 4
# print(type(x))
# # type : type is used to define the datatype of a variable
# # <class 'int'>

# # Type Casting is used to change datatype of a variable
# x = str(3)
# print(type(x))

# x = str(3)    # x will be '3'
# y = int(3)    # y will be 3
# z = float(3)  # z will be 3.0


# Get the Type

# You can get the data type of a variable with the type() function.

# x = 5
# y = "John"
# print(type(x))
# print(type(y))


# Single or Double Quotes?

# x = "John"
# # is the same as
# x = 'John'


# python is Case-Sensitive
# x = 4
# X = 5
# # python variable are mutablewe can change the values
# print(x,X)


# Variable Names

# A variable can have a short name (like x and y) or a more descriptive name (age, carname, total_volume).


# Rules for Python variables

# A variable name must start with a letter or the underscore character

# A variable name cannot start with a number


# A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )


# Variable names are case-sensitive (age, Age and AGE are three different variables)


# A variable name cannot be any of the Python keywords.

# _x = 5 valid
# 1x = 5 not valid
# x9 = 5 valid
# myvar = "John" valid
# my_var = "John" valid
# _my_var = "John"
# myVar = "John"
# MYVAR = "John"
# myvar2 = "John"  valids

# 2myvar = "John" not valid
# my-var = "John" invalid
# my var = "John" invalid




# Casing
# variables ko likhna ka tarika

# # Camel Case
# myVariableName = "John"

# # Pascal Case
# MyVariableName = "John"

# # Snake Case
# my_variable_name = "John"




# Many Values to Multiple Variables

# Python allows you to assign values to multiple variables in one line:


# x, y, z = 2 , "Banana",9
# print(x)
# print(y)
# print(z)

#  Make sure the number of variables matches the number of values, or else you will get an error.

# not enough values to unpack

# One Value to Multiple Variables
# x = y = z = "Orange"
# print(x)
# print(y)
# print(z)


# Unpack a Collection

# Python allows you to extract the values into variables. This is called unpacking.


# fruits =["apple", "banana", "cherry",2]

# x,y,z,v = fruits
# print(x)
# print(y)
# print(z)
# print(v)


# Python - Output Variables
# The Python print() function is often used to output variables.

# output variables return nhi krte hai value but input variable return krte hai

# x= 5
# y = print(x)
# print(y)

# x = "Python"
# y = "is"
# z = "awesome"
# print(x, y, z)

# You can also use the + operator to output multiple variables:

# x = "Python "
# y = "is "
# z = 2
# print(x + y , z)

# can only concatenate str (not "int") to str  


# x = "5"
# y = "10"
# print(x + y)


# x = 5
# y = "John"
# print(x + y)

# x = "5"
# y = "John"
# print(x,y) 
# # by default single line space rehta hi hai


# Python - Global Variables

# Global Variables

# Variables that are created outside of a function (as in all of the examples in the previous pages) are known as global variables.

# Global variables can be used by everyone, both inside of functions and outside.



# x = "awesome"
# print(x)

# def myfunc():
#    # concept of local variable
#   print("Python is " + x)

# myfunc()




# If you create a variable with the same name inside a function, this variable will be local, and can only be used inside the function. The global variable with the same name will remain as it was, global and with the original value.



# x = "awesome"

# def myfunc():
#   x = "fantastic" 
#   # local variable ki variable preference over global variable
#   print("Python is " + x)

# myfunc()

# print("Python is " + x)



# The global Keyword

# Normally, when you create a variable inside a function, that variable is local, and can only be used inside that function.


# To create a global variable inside a function, you can use the global keyword.


# def myfunc():
#   global x
#   x = "fantastic"
  

# myfunc()

# print("Python is " + x)



# use the global keyword if you want to change a global variable inside a function.

# x = "awesome"

# def myfunc():
#   global x
#   x = "fantastic"

# myfunc()

# print("Python is " + x)