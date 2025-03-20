# Program to check armstrong number


num = int(input("Enter a number: "))


num_digits = len(str(num))

sum_of_powers = 0

temp = num

while temp > 0:
    digit = temp % 10  
    sum_of_powers += digit ** num_digits  
    temp //= 10  

if sum_of_powers == num:
    print(f"{num} is an Armstrong number.")
else:
    print(f"{num} is not an Armstrong number.")






# Program to find the product of digits


number = int(input("Enter a number: "))

product = 1

while number > 0:
    digit = number % 10
    product *= digit
    number //= 10

print(f"The product of the digits is: {product}")







# Program to find the reverse of a given number


number = int(input("Enter a number: "))

reverse = 0

while number != 0:
    digit = number % 10
    reverse = reverse * 10 + digit
    number //= 10

print(f"The reverse of the number is: {reverse}")






# Program to check given no is palindrome or not


number = int(input("Enter a number: "))


original_number = number
reverse = 0

while number > 0:
    digit = number % 10
    reverse = reverse * 10 + digit
    number //= 10

# Check if the original number is equal to the reversed number
if original_number == reverse:
    print(f"{original_number} is a palindrome.")
else:
    print(f"{original_number} is not a palindrome.")




# Program to print all prime numbers within a given range:


# Input range from the user
start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))

print(f"Prime numbers between {start} and {end} are:")

for num in range(start, end + 1):
    # Prime numbers are greater than 1
    if num > 1:
        is_prime = True
        for i in range(2, num):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            print(num)




# Program to calculate the factorial of a number

number = int(input("Enter a number: "))

factorial = 1

if number < 0:
    print("Factorial does not exist for negative numbers.")
elif number == 0:
    print("The factorial of 0 is 1.")
else:
    for i in range(1, number + 1):
        factorial *= i
    print(f"The factorial of {number} is {factorial}.")




# Using recursion

# function ke andar same function ko call krde toh Recursion hota hai


def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

number = int(input("Enter a number: "))

if number < 0:
    print("Factorial does not exist for negative numbers.")
else:
    print(f"The factorial of {number} is {factorial(number)}.")






# Program to print fibonacci series



n = int(input("Enter the number of terms: "))

a, b = 0, 1

if n <= 0:
    print("Please enter a positive integer.")
elif n == 1:
    print(f"Fibonacci series up to {n} term: {a}")
else:
    print("Fibonacci series:")
    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b




# Using recursion


def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

n = int(input("Enter the number of terms: "))

if n <= 0:
    print("Please enter a positive integer.")
else:
    print("Fibonacci series:")
    for i in range(n):
        print(fibonacci(i), end=" ")



# Program to print the multiplication table of a given number

number = int(input("Enter a number: "))

for i in range(1, 11):
    print(f"{number} x {i} = {number * i}")




