# Python program to find and print the maximum of three numbers


def find_max_number(a, b, c):
    return max(a, b, c)

# Input three numbers
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))


max_number = find_max_number(num1, num2, num3)
print(f"The maximum number is: {max_number}")




# Another approach


# Function to find the maximum number
def find_max_number(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

# Input three numbers
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))

max_number = find_max_number(num1, num2, num3)
print(f"The maximum number is: {max_number}")






# Program to find the sum of even numbers from 1 to n

def sum_of_even_numbers(n):
    total = 0
    for i in range(2, n + 1, 2):  
        total += i
    return total


n = int(input("Enter a number: "))


result = sum_of_even_numbers(n)
print(f"The sum of even numbers from 1 to {n} is: {result}")





# Another approach 

def sum_of_even_numbers(n):
    # List comprehension
    return sum([i for i in range(1, n + 1) if i % 2 == 0])


n = int(input("Enter a number: "))


result = sum_of_even_numbers(n)
print(f"The sum of even numbers from 1 to {n} is: {result}")




# Program to Print first 10 natural numbers

i = 1
while(i<11):
  print(i)
  i+=1


# Program to Print first n natural numbers


num = int(input("Enter the number upto which you want to print the natural numbers: "))

i = 1
while(i <= num):
  print(i)
  i+=1


# Program to Print first n natural numbers


num = int(input("Enter the number upto which you want to print the natural numbers in reverse order: "))

while(num >= 0):
  print(num)
  num =- 1



# Program to find sum of first n natural numbers

num = int(input("Enter the value of n :"))
sum = 0
for i in range(1, num + 1):
    sum = sum + i
print(f"sum of {num} natural numbers is {sum}")




