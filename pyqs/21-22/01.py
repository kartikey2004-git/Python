# Q1 . What will be output of the following code

# i = 0
# while i < 3:
#     print(i)
#     i += 1
# else:
#     print(0)

# # Output : 0,1,2,0



# Q2 . What will be output of the following Python code


# def cube(x):
#   return x*x*x
# x = cube(3)
# print(x)

# Output: 27





# # a = "hello"
# # b = 0
# # c = False 
# # x = b or c
# # print(x)

# # and return first falsy value
# # or return first truthy value


# a = 33
# b = 200

# if b > a:
#   pass



# i = 1
# while i < 6:
#   print(i)
#   i += 1



# i = 1
# while i < 6:
#   print(i)
#   if i == 3:
#     break
#   i += 1



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



# fruits = ["apple", "banana", "cherry"]
# for x in fruits:
#   print(x)


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




# fruits = ["apple", "banana", "cherry"]
# for x in fruits:
#   if x == "banana":
#     continue
#   print(x)




# for x in range(6):
#   print(x)



# for x in range(2, 30, 3):
#   print(x)


# for x in range(6):
#   print(x)
# else:
#   print("Finally finished!")




# for x in range(6):
#   if x == 3: break
#   print(x)
# else:
#   print("Finally finished!")




# adj = ["red", "big", "tasty"]
# fruits = ["apple", "banana", "cherry"]

# for x in adj:
#   for y in fruits:
#     print(x, y)



# def sum(a,b):
#   print(a+b)
#   return a-b

# c = sum(2,4)
# print(c)


# # Arbitrary Arguments

# def my_function(*kids):
#   print("The youngest child is " + kids[2])

# my_function("Emil", "Tobias", "Linux")




# def my_function(child3, child2, child1):
#   print("The youngest child is " + child3)

# my_function(child1 = "Emil", child3 = "Tobias", child2 = "Linus")




# def my_function(**kid):
#   print("His last name is " + kid["lname"])

# my_function(fname = "Tobias", lname = "Refsnes")




# def my_function(country = "Norway"):
#   print("I am from " + country)

# my_function("Sweden")
# my_function("India")
# my_function()
# my_function("Brazil")





# def my_function(food):
#   for x in food:
#     print(x)

# fruits = ["apple", "banana", "cherry"]

# my_function(fruits)






# def my_function(x):
#   return 5 * x

# print(my_function(3))
# print(my_function(5))
# print(my_function(9))



# def my_function(x, /):
#   print(x)

# my_function(3)




# def my_function(x):
#   print(x)

# my_function(x = 3)






# def tri_recursion(k):
#   if(k > 0):
#     result = k + tri_recursion(k - 1)
#     print(result)
#   else:
#     result = 0
#   return result

# print("Recursion Example Results:")
# tri_recursion(6)


# # hold pe h



# x = lambda a : a + 10
# print(x(5))


# x = lambda a, b : a * b
# print(x(5, 6))



# def myfunc(n):
#   return lambda a : a * n

# mydoubler = myfunc(2)

# print(mydoubler(11))

