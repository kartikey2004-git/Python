a = (1,2,3,4,5,45,False,"Rohit","Shivam")
print(a)

# Return the number of times the value  appears in the tuple:
no = a.count(45)
print(no)

# Tuples in Python are immutable, so they have fewer methods compared to lists. 
# Here are some common tuple methods and operations:

# count(value)
# Returns the number of times a specified value appears in the tuple.
my_tuple = (1, 2, 3, 2, 2)
print(my_tuple.count(2))  # Output: 3


# index(value)
# Returns the index of the first occurrence of the specified value.
my_tuple = (1, 2, 3, 2)
print(my_tuple.index(2))  # Output: 1


# Common tuple operations (although not methods):
# Concatenation (+)
# Combines two or more tuples to create a new tuple.
tuple1 = (1, 2)
tuple2 = (3, 4)
result = tuple1 + tuple2  # Output: (1, 2, 3, 4)


# Repetition (*)
# Repeats a tuple a specified number of times.
my_tuple = (1, 2)
result = my_tuple*3  # Output: (1, 2, 1, 2, 1, 2)


# Membership operator (in)
# Checks if an item exists in a tuple.
my_tuple = (1, 2, 3)
print(2 in my_tuple)  # Output: True


# Unpacking
# Assign tuple values to multiple variables.
my_tuple = (1, 2, 3)
a, b, c = my_tuple
print(a, b, c)  # Output: 1 2 3


# Slicing
# Access a subset of tuple elements.
my_tuple = (1, 2, 3, 4, 5)
print(my_tuple[1:4])  # Output: (2, 3, 4)


# Since tuples are immutable, methods like append(), remove(), or sort() are not available for tuples.



# In Python, tuples are ordered collections of elements, and you can use slicing to extract specific parts of a tuple.

# 1. Length of a tuple:
# You can find the length of a tuple using the len() function, which returns the number of elements in the tuple.


my_tuple = (10, 20, 30, 40, 50)
length = len(my_tuple)
print(length)  # Output: 5


# 2. Slicing a tuple:
# Slicing allows you to extract a portion of the tuple. The syntax for slicing is:


# tuple[start:stop:step]
# start: The index to start slicing from (inclusive).
# stop: The index to end slicing (exclusive).
# step: The step to take between elements (optional).

my_tuple = (10, 20, 30, 40, 50)

# Slice from index 1 to 4
slice1 = my_tuple[1:4]  # Output: (20, 30, 40)

# Slice from the beginning to index 3
slice2 = my_tuple[:3]   # Output: (10, 20, 30)

# Slice from index 2 to the end
slice3 = my_tuple[2:]   # Output: (30, 40, 50)

# Slice the whole tuple with a step of 2
slice4 = my_tuple[::2]  # Output: (10, 30, 50)


# 3. Minimum and Maximum of a tuple:
# You can use the min() and max() functions to get the smallest and largest values in a tuple of comparable elements.


my_tuple = (10, 20, 30, 40, 50)
minimum = min(my_tuple)  # Output: 10
maximum = max(my_tuple)  # Output: 50


# Combining slicing with min() and max():
# You can also slice a tuple and then find the min or max of the sliced portion.


my_tuple = (10, 20, 30, 40, 50)

# Slice and find min and max of the slice
slice1 = my_tuple[1:4]  # Output: (20, 30, 40)
minimum_in_slice = min(slice1)  # Output: 20
maximum_in_slice = max(slice1)  # Output: 40



# Length: Use len().
# Slicing: Use tuple[start:stop:step] to get a portion of the tuple.
# Min and Max: Use min() and max() to find the smallest and largest elements, either on the full tuple or a slice of it.