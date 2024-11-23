name = "Harry"
print(len(name))
print(name.endswith("ry"))
print(name.startswith("H"))
print(name.capitalize())



# give me most used string functions in python


# Here are some of the most commonly used string functions in Python:

# len()
# Returns the length of a string.
s = "Hello"
print(len(s))  # Output: 5


# str()
# Converts an object to a string.
num = 123
print(str(num))  # Output: "123"


# lower()
# Converts all characters in a string to lowercase.
s = "HELLO"
print(s.lower())  # Output: "hello"


# upper()
# Converts all characters in a string to uppercase.
s = "hello"
print(s.upper())  # Output: "HELLO"



# strip()
# Removes leading and trailing whitespaces (or specified characters).
s = "  hello  "
print(s.strip())  # Output: "hello"



# replace()
# Replaces occurrences of a substring with another substring.
s = "Hello, world"
print(s.replace("world", "Python"))  # Output: "Hello, Python"


# split()
# Splits a string into a list of substrings based on a delimiter.
s = "apple,banana,orange"
print(s.split(","))  # Output: ['apple', 'banana', 'orange']


# join()
# Joins elements of a list into a single string with a specified separator.
fruits = ['apple', 'banana', 'orange']
print(",".join(fruits))  # Output: "apple,banana,orange"


# find()
# Returns the index of the first occurrence of a substring, or -1 if not found.

s = "hello"
print(s.find("l"))  # Output: 2


# startswith() and endswith()
# Checks if a string starts or ends with a specified substring.

s = "hello"
print(s.startswith("he"))  # Output: True
print(s.endswith("lo"))    # Output: True



# count()
# Returns the number of occurrences of a substring.

s = "hello hello"
print(s.count("hello"))  # Output: 2


# capitalize()
# Capitalizes the first character of the string.
s = "hello"
print(s.capitalize())  # Output: "Hello"


# title()
# Capitalizes the first letter of each word in the string.
s = "hello world"
print(s.title())  # Output: "Hello World"


# isalpha()
# Returns True if all characters in the string are alphabetic.
s = "hello"
print(s.isalpha())  # Output: True


# isdigit()
# Returns True if all characters in the string are digits.
s = "123"
print(s.isdigit())  # Output: True


# These functions are widely used for string manipulation in Python and cover a variety of tasks like searching, formatting, and validating strings.