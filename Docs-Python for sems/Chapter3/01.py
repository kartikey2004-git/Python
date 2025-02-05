# Python If ... Else

# Python Conditions and If statements

# Equals: a == b
# Not Equals: a != b
# Less than: a < b
# Less than or equal to: a <= b
# Greater than: a > b
# Greater than or equal to: a >= b



# a = 33
# b = 4
# if b > a:
#   print("ok")



# Elif


# The elif keyword is Python's way of saying "if the previous conditions were not true, then try this condition".



# a = 33
# b = 33
# if b > a:
#   print("b is greater than a")
# elif a == b:
#   print("a and b are equal")


# Else


# The else keyword catches anything which isn't caught by the preceding conditions.


# a = 200
# b = 33
# if b > a:
#   print("b is greater than a")
# elif a == b:
#   print("a and b are equal")
# else:
#   print("a is greater than b")



# age = int(input("Enter your age: "))

# if(age<18):
#   print("fuck off")
# elif(age == 18):
#   print("tu bhi maa chuda voter card bnva nibbe")
# else:
#   print("sex krlo")



# a = 200
# b = 33
# c = 500
# if a > b and c > a:
#   print("Both conditions are True")



# a = 200
# b = 33
# c = 500
# if a > b or a > c:
#   print("At least one of the conditions is True")



# a = 33
# b = 200
# if not a > b:
#   print("a is NOT greater than b")


# Nested If

# x = 41

# if x > 10:
#   print("Above ten,")
#   if x > 20:
#     print("and also above 20!")
#   else:
#     print("but not above 20.")


# The pass Statement


# if statements cannot be empty, but if you for some reason have an if statement with no content, put in the pass statement to avoid getting an error.


# a = 33
# b = 200

# if b > a:
#   pass



# Python While Loops


# while loops
# for loops


# The while Loop

# With the while loop we can execute a set of statements as long as a condition is true.


# i = 1
# while i < 6:
#   print(i)
#   i+=1 # increment operator


# Note: remember to increment i, or else the loop will continue forever.


# The while loop requires relevant variables to be ready, in this example we need to define an indexing variable, i, which we set to 1.


# The break Statement


# With the break statement we can stop the loop even if the while condition is true:


# i = 1
# while i < 6:
#   print(i)
#   if i == 3:
#     break
#   i += 1


# The continue Statement

# With the continue statement we can stop the current iteration, and continue with the next:


# i = 0
# while i < 6:
#   i += 1
#   if i == 3:
#     continue
#   print(i)


# i = 1
# while i < 6:
#   print(i)
#   i += 1
# else:
#   print("i is no longer less than 6")




# Python For Loops


# A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).


# This is less like the for keyword in other programming languages, and works more like an iterator method as found in other object-orientated programming languages.

# With the for loop we can execute a set of statements, once for each item in a list, tuple, set etc.



# fruits = ["apple", "banana", "cherry"]
# for index in fruits:
#   print(index)


# The for loop does not require an indexing variable to set beforehand.



# for x in "banana":
#   print(x)

  

# fruits = ["apple", "banana", "cherry"]
# for x in fruits:
#   print(x)
#   if x == "banana":
#     break



# fruits = ["apple", "banana", "cherry"]
# for x in fruits:
#   if x == "banana":
#     break
#   print(x)




# fruits = ["apple", "banana", "cherry","dudu"]
# for x in fruits:
#   if x == "banana":
#     continue
#   print(x)



# The range() Function

# The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and ends at a specified number.



# for x in range(1,7,2):
#   print(x)


# Note that range(6) is not the values of 0 to 6, but the values 0 to 5.



# for x in range(6):
#   print(x)
# else:
#   print("Finally finished!")




# Note: The else block will NOT be executed if the loop is stopped by a break statement.




# for x in range(6):
#   if x == 3: 
#     break
#   print(x)
# else:
#   print("Finally finished!")




# adj = ["red", "big", "tasty"]
# fruits = ["apple", "banana", "cherry"]

# for x in adj:
#   for y in fruits:
#     print(x, y)



# for x in [0, 1, 2]:
#   pass