# Python - Escape Characters

# Escape Character

# To insert characters that are illegal in a string, use an escape character.

# An escape character is a backslash \ followed by the character you want to insert.


# txt = "We are the\tso-called \"Vikings\" from \n the north."
# print(txt)




# capitalize()	Converts the first character to upper case

# count()	Returns the number of times a specified value occurs in a string

# a = "helloo"
# print(a.count("o"))



# find() Searches the string for a specified value and returns the position of where it was found

# a = "helloo cutie"
# print(a.find("e"))



# isalpha()	Returns True if all characters in the string are in the alphabet

# isdigit()	Returns True if all characters in the string are digits

# upper()	Converts a string into upper case

# strip()	Returns a trimmed version of the string


# split()	Splits the string at the specified separator, and returns a list


# replace()	Returns a string where a specified value is replaced with a specified value

# lower()	Converts a string into lower case

# join()	Joins the elements of an iterable to the end of the string


# islower()	Returns True if all characters in the string are lower case


#join

# Joining elements of a list with a space separator


# words = ["Hello", "world", "in", "Python"]


# sentence = " ".join(words)
# print(sentence)  





# Python Booleans

# Booleans represent one of two values: True or False.



# a = 200
# b = 33

# if b > a:
#   print("b is greater than a")
# else:
#   print("b is not greater than a")



# The bool() function allows you to evaluate any value, and give you True or False in return,

# Some values are true


# bool("abc")
# bool(123)
# bool(["apple", "cherry", "banana"])



# Some Values are False

# bool(False)
# bool(None)
# bool(0)
# bool("")
# bool(())
# bool([])
# bool({})



# Python also has many built-in functions that return a boolean value, like the isinstance() function, which can be used to determine if an object is of a certain data type:


# x = 200
# print(isinstance(x, float))