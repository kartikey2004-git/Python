s = {1,5,32,7,7,8 ,"harry"}
s.add(566)
print(s,type(s))


# Here are some of the most important set methods in Python:

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




# These methods allow you to efficiently manage and manipulate sets in Python!