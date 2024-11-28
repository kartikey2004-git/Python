friends = ["Apple","Orange",5,345.56,False,"Aakash","Rohan"]
# print(friends)

friends.append("Harry")
# print(friends)

l1 =[1,34,562,786,9687,6443,5613,3]
# l1.sort()
# print(l1)
# l1.reverse()
# l1.insert(3,122) # insert krdo 122 at the index 3 list mein
value = l1.pop(3) #  index no 3 se value remove krdega 
a = print(value) # print krega wo value jo  index no 3 se pop huyi hai
print(l1)

# The remove() method removes the first occurrence of the element with the specified value.

# Remove the "banana" element of the fruit list:

fruits = ['apple', 'banana', 'cherry','banana']
fruits.remove("banana")
print(fruits)