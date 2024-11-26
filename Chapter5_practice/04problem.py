s = set()
s.add(20)
s.add(20.0)
s.add("20")
print(s)
print(len(s))  # output length of set is 2...

# because 
print(1==1.0) 
# return True

# In Python, the expression 1 == 1.0 returns True because Python's == operator checks for value equality, not strict type equality.

# 1 is an integer.
# 1.0 is a float.
# Despite being different types, both represent the same numeric value. Python will automatically convert the integer to a float for comparison in this case, resulting in 1.0 == 1.0, which is True.

# For strict type comparison, you would use the is operator or check their types explicitly:

# 1 is 1.0 would return False because they are different objects.
# type(1) == type(1.0) would return False because 1 is an int and 1.0 is a float.

