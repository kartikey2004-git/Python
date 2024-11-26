s = {1,5,32,7,7,8 ,"harry"}
s.add(566)
print(s,type(s))


# Properties of sets

# Sets are unordered
# Sets are unindexed
# There is no way to change items in sets
# Sets cannot comtain duplicate values




# Here are some of the most important set methods in Python:

# In Python, len() can be used with a set to determine the number of elements it contains.


my_set = {1, 2, 3, 4}
print(len(my_set))  # Output: 4


# Even if the set contains duplicate values when it's created, sets only store unique elements. So, duplicates are automatically removed, and len() will reflect the count of unique elements.

# Example with duplicates:

my_set = {1, 2, 2, 3, 4}
print(len(my_set))  # Output: 4 (since duplicates are removed)



# add(): Adds a single element to the set.

my_set = {1, 2, 3}
my_set.add(4)
print(my_set)  # Output: {1, 2, 3, 4}


# update(): Adds multiple elements to the set (can take any iterable like a list, tuple, etc.).
my_set = {1, 2, 3}
my_set.update([4, 5, 6])
print(my_set)  # Output: {1, 2, 3, 4, 5, 6}



# remove(): Removes a specific element from the set. Raises a KeyError if the element is not present.
my_set = {1, 2, 3}
my_set.remove(2)
print(my_set)  # Output: {1, 3}



# discard(): Removes a specific element from the set without raising an error if the element is not present.
my_set = {1, 2, 3}
my_set.discard(2)
print(my_set)  # Output: {1, 3}
my_set.discard(4)  # No error raised




# pop(): Removes and returns an arbitrary element from the set. Raises a KeyError if the set is empty.
my_set = {1, 2, 3}
element = my_set.pop()
print(element)  # Output: (random element from the set)
print(my_set)  # Output: Remaining elements after pop



# clear(): Removes all elements from the set.
my_set = {1, 2, 3}
my_set.clear()
print(my_set)  # Output: set()



# union(): Returns a new set with elements from the set and all others passed (can accept multiple sets).
set1 = {1, 2, 3}
set2 = {3, 4, 5}
result = set1.union(set2)
print(result)  # Output: {1, 2, 3, 4, 5}


# intersection(): Returns a new set containing only the elements that are common between sets.
set1 = {1, 2, 3}
set2 = {2, 3, 4}
result = set1.intersection(set2)
print(result)  # Output: {2, 3}


# difference(): Returns a new set with elements that are in the set but not in the other(s).
set1 = {1, 2, 3}
set2 = {2, 3, 4}
result = set1.difference(set2)
print(result)  # Output: {1}



# symmetric_difference(): Returns a new set with elements in either of the sets but not in both (elements that are not common).
set1 = {1, 2, 3}
set2 = {2, 3, 4}
result = set1.symmetric_difference(set2)
print(result)  # Output: {1, 4}




# issubset(): Checks if all elements of the set are present in another set.
set1 = {1, 2}
set2 = {1, 2, 3}
result = set1.issubset(set2)
print(result)  # Output: True




# issuperset(): Checks if the set contains all elements of another set.
set1 = {1, 2, 3}
set2 = {1, 2}
result = set1.issuperset(set2)
print(result)  # Output: True


# isdisjoint(): Returns True if the sets have no elements in common.
set1 = {1, 2, 3}
set2 = {4, 5, 6}
result = set1.isdisjoint(set2)
print(result)  # Output: True



# 1. copy()
#  Creates a shallow copy of a list, set, or dictionary.

# copy() creates a new object that is a copy of the original object. For sets, it is used to avoid modifying the original set when making changes to a copy.

original_set = {1, 2, 3}
copied_set = original_set.copy()
print(copied_set)  # Output: {1, 2, 3}

# Modifying the copied set
copied_set.add(4)
print(copied_set)      # Output: {1, 2, 3, 4}
print(original_set)    # Output: {1, 2, 3} (Unchanged)



# 2. difference_update()
# Modifies a set by removing elements found in another set.

# difference_update() removes all elements from the original set that are present in the other set(s) passed as arguments. It directly alters the original set (in-place operation) rather than returning a new set.

set_a = {1, 2, 3, 4}
set_b = {3, 4, 5}

set_a.difference_update(set_b)
print(set_a)  # Output: {1, 2} (set_a modified)


# These methods allow you to efficiently manage and manipulate sets in Python!


