d = {}
# method for creating a empty dictionary

marks = {
  "Harry": 100,
  "Shubham":56,
  "Rohan": 23,
}

# print(marks.items())
# print(type(marks.items()))

# print(marks.keys())
# print(marks.values())

# marks.update({"Harry":99,"Renuka":34})
# print(marks)

print(marks.get("Harry")) # prints none if key is not present
print(marks["Harry"]) # returns error if key is not present



# Here are some common Python dictionary methods:

# dict.clear()
# Removes all elements from the dictionary.
my_dict = {"a": 1, "b": 2}
my_dict.clear()
print(my_dict)  # Output: {}


# dict.copy()
# Returns a shallow copy of the dictionary.
# A shallow copy occurs when you copy the reference of an object to a new variable. 
my_dict = {"a": 1, "b": 2}
new_dict = my_dict.copy()
print(new_dict)  # Output: {'a': 1, 'b': 2}



# dict.fromkeys(keys, value)
# Creates a new dictionary from a given sequence of keys with all values set to a specified value.
keys = ["a", "b", "c"]
new_dict = dict.fromkeys(keys, 0)
print(new_dict)  # Output: {'a': 0, 'b': 0, 'c': 0}



# dict.get(key, default=None)
# Returns the value for the specified key if the key is in the dictionary. Otherwise, it returns the default value (or None if no default is provided).
my_dict = {"a": 1, "b": 2}
print(my_dict.get("a"))       # Output: 1
print(my_dict.get("c", 0))    # Output: 0



# dict.items()
# Returns a view object that displays a list of dictionary's key-value pairs.
my_dict = {"a": 1, "b": 2}
print(my_dict.items())  # Output: dict_items([('a', 1), ('b', 2)])



# dict.keys()
# Returns a view object that displays a list of all the keys in the dictionary.
my_dict = {"a": 1, "b": 2}
print(my_dict.keys())  # Output: dict_keys(['a', 'b'])


# dict.pop(key, default)
# Removes the specified key and returns the corresponding value. If the key is not found, returns the default value (or raises KeyError if no default is provided).
my_dict = {"a": 1, "b": 2}
print(my_dict.pop("a"))  # Output: 1
print(my_dict)           # Output: {'b': 2}



# dict.popitem()
# Removes and returns the last key-value pair as a tuple. Raises KeyError if the dictionary is empty.
my_dict = {"a": 1, "b": 2}
print(my_dict.popitem())  # Output: ('b', 2)
print(my_dict)            # Output: {'a': 1}



# dict.setdefault(key, default=None)
# Returns the value of the specified key. If the key does not exist, inserts the key with the specified default value.
my_dict = {"a": 1, "b": 2}
print(my_dict.setdefault("c", 0))  # Output: 0
print(my_dict)  # Output: {'a': 1, 'b': 2, 'c': 0}




# dict.update([other])
# Updates the dictionary with elements from another dictionary or from an iterable of key-value pairs.
my_dict = {"a": 1, "b": 2}
my_dict.update({"b": 3, "c": 4})
print(my_dict)  # Output: {'a': 1, 'b': 3, 'c': 4}




# dict.values()
# Returns a view object that displays a list of all the values in the dictionary.
my_dict = {"a": 1, "b": 2}
print(my_dict.values())  # Output: dict_values([1, 2])



# These methods allow you to manipulate and interact with dictionaries in Python efficiently.


