# Program to find the sum of the squares of the first n natural numbers 

num = int(input("Enter the value of n :"))
sum = 0
for i in range(1, num + 1):
    sum = sum + i*i
print(f"sum of {num} natural numbers is {sum}")




# Program to print the even numbers from 1 to N 

num = int(input("Enter the upto which u want to print the even numbers :"))

for i in range(1,num+1):
    if(i % 2 == 0):
        print(i)



# Program to print sum of  even numbers from 1 to N 


num = int(input("Enter the upto which u want to print the even numbers :"))

sum = 0

for i in range(1,num+1):
    if(i % 2 == 0):
        sum = sum + i
print(sum)







# Program to sum of square of digits of number


def sum_of_digits(number):
    sum = 0

    while number > 0:
        digit = number % 10
        sum += digit**2
        number = number // 10

    return sum


# Input a number
num = int(input("Enter a number: "))


result = sum_of_digits(num)
print(f"The sum of square of  digits of {num} is: {result}")








# Program to sum of square of digits of number


def sum_of_digits(number):
    sum = 0

    while number > 0:
        digit = number % 10
        sum += digit**3
        number = number // 10

    return sum


# Input a number
num = int(input("Enter a number: "))


result = sum_of_digits(num)
print(f"The sum of square of  digits of {num} is: {result}")



