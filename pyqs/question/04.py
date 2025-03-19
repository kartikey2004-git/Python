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



