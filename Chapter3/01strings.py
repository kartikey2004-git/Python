# string is data type in python(single, double,triple quoted string)
name = "harry"
# strings are immutable

#indexing of strings(indexing starts from 0 to n-1)
# Python strings are "immutable" which means they cannot be changed after they are created

# Slicing in string
nameshort = name[0:3] 
print(nameshort) 
character1 = name[1]
print(character1)
# start from index 0 all the way till 3 excluding 3
# also we have a study of negative indexes 


print(name[:4]) # is same as print(name[0:4])
print(name[1:]) # is same as print(name[1:5])
print(name[1:5])



## slicing with skip values(step values)
word = "amazing"
print(word[1:6:2])

goat = "kingkohli"
print(goat[1:9:2])
