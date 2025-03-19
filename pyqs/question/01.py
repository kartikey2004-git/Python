# 1. Program to swap two numbers using a temporary variable

def swap_numbers(a,b):
  print(f"Befor swapping a = {a} , b = {b}")

  # Swapping using a temporary variable
  temp = a
  a = b 
  b = temp 
  print(f"After swapping: a = {a}, b = {b}")

# Input two numbers
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))


# Call the function to swap numbers
swap_numbers(num1, num2)






# Program to Swapping without using a temporary variable

def swap_numbers(a, b):
    print(f"Before swapping: a = {a}, b = {b}")
    
    a, b = b, a  # Swap the values
    
    print(f"After swapping: a = {a}, b = {b}")

# Input two numbers
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

# Call the function to swap numbers
swap_numbers(num1, num2)






# Program to sum of digits of number


def sum_of_digits(number):
    sum = 0

    while number > 0:
        digit = number % 10
        sum += digit
        number = number // 10

    return sum


# Input a number
num = int(input("Enter a number: "))


result = sum_of_digits(num)
print(f"The sum of digits of {num} is: {result}")






# Program to check leap year


def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


year = int(input("Enter a year: "))


if is_leap_year(year):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")


# Another approach


# Function to check leap year
def is_leap_year(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


year = int(input("Enter a year: "))


if is_leap_year(year):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")
