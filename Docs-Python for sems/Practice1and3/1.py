# x = int(input("enter the no upto which u want to print natural numbers"))

# i = 1
# while i < (x+1):
#   print(i)
#   i+=1 


# reverse order

# i = 10 
# while i > 0:
#   print(i)
#   i-=1



# n = int(input("enter the no"))

# i = 1
# sum = 0
# while i<n:
#   sum = sum + i
#   i+=1
# print(sum)



# n = int(input("enter the number upto which u want to print the even numbers"))

# i=2
# while i<=n:
#   print(i)
#   i+=2




# n = int(input("enter the number upto which u want to print the even numbers"))

# i=2
# sum = 0
# while i<=n:
#   sum = sum+i
#   i+=2
# print(sum)  




# num = int(input("Enter the number u want to print the sum of digits"))


# sum = 0
# while num > 0:
#   a = num % 10
#   sum = sum + a*a*a 
#   num = num // 10

# print(sum)




# n = int(input("enter the number"))
# i = 1
# sum = 0

# while i <= n:
#   sum = sum + i*i
#   i+=1
# print(sum)





i = int(input("Enter number to check for armstrong"))
sum = 0
original = i
while (i>0):
    sum = sum + (i%10)*(i%10)*(i%10)
    i = i//10
if original == sum:
    print("armstrong")
else:
    print("not armstrong")






n = int(input("Enter the number"))
i = n
count = 0
while i > 0:
    i = i// 10
    count +=1

sum = 0 
i = n
while i > 0:
    digit = i % 10
    x = 1
    pro = 1
    while x<=count:
        pro = pro * digit
        x+=1
    sum = sum + pro
    i = i // 10

if(sum == n):
    print("Armstrong number")
else:
    print("not armstrong number")

