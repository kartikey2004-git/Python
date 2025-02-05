# Python Operators

# Operators are used to perform operations on variables and values.

# print(10 + 5)


# Arithmetic operators
# Assignment operators
# Comparison operators
# Logical operators
# Identity operators
# Membership operators
# Bitwise operators



# Python Arithmetic Operators




# # Input two numbers
# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))

# # Arithmetic Operations
# addition = num1 + num2
# subtraction = num1 - num2
# multiplication = num1 * num2
# division = num1 / num2 
# modulus = num1 % num2 
# exponentiation = num1 ** num2
# floor_division = num1 // num2 

# print(addition)
# print(subtraction)
# print(multiplication)
# print(division)
# print(modulus)
# print(exponentiation)
# print(floor_division)
# # returns only integer value


# Python Assignment Operators

# Assignment operators are used to assign values to variables

# x = 3

# x = 3
# x += 1  # (x = x+1)
# print(x)




# Python Comparison Operators

# Comparison operators are used to compare two values:


# == , != , > , < , >= , <=



# Python Logical Operators

# and 	Returns True if both statements are true

# if(4<6 and 1>1):
#   print("ok")
# else:
#   print("not ok")


# or	Returns True if one of the statements is true

# if(4<6 or 1>1):
#   print("ok")
# else:
#   print("not ok")



# if(not(6>5)):
#   print("ok")
# else:
#   print("not ok")




# Python Identity Operators



# is 	Returns True if both variables are the same object

# but if they are actually the same object, with the same memory location:


# x = ["apple", "banana"]
# y = ["apple", "banana"]
# z = x

# print(x is z)

# returns True because z is the same object as x

# print(x is y)

# returns False because x is not the same object as y, even if they have the same content

# print(x == y)

# to demonstrate the difference betweeen "is" and "==": this comparison returns True because x is equal to y


# is not	Returns True if both variables are not the same object




# Python Membership Operators


# in 	Returns True if a sequence with the specified value is present in the object	


# not in	Returns True if a sequence with the specified value is not present in the object



# Python Bitwise Operators
 

# & 	AND	Sets each bit to 1 if both bits are 1	x & y


# |  	OR	Sets each bit to 1 if one of two bits is 1	x | y



# ^	XOR	Sets each bit to 1 if only one of two bits is 1

# ~	NOT	Inverts all the bits



# print(100 + 5 * 3)
# # BODMAS
# print((6 + 3) - (6 + 3))