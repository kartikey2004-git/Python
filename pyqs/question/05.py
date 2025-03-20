# Python program to reverse a string using for loop


string = input("Enter a string: ")

reversed_string = ""

for char in string:
    reversed_string = char + reversed_string

print("Reversed string:", reversed_string)


# Python program to reverse a string without using for loop


# Input string
string = input("Enter a string: ")

reversed_string = string[::-1]

print("Reversed string:", reversed_string)


# Python program to count the number of vowels and consonants in a given string


# Input string
string = input("Enter a string: ").lower()

# Initialize counters
vowel_count = 0
consonant_count = 0

# Define vowels
vowels = "aeiou"


for char in string:
    if char.isalpha():
        if char in vowels:
            vowel_count += 1
        else:
            consonant_count += 1

# Output the counts
print(f"Vowels: {vowel_count}")
print(f"Consonants: {consonant_count}")


# Program to check if a given string is a palindrome


# Input string
string = input("Enter a string: ").lower()

# Remove any spaces from the string (optional, for phrases)
string = string.replace(" ", "")

# Check if the string is equal to its reverse
if string == string[::-1]:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")


# Python program to find sum of list elements

list = [1,2,3,4]
n = len(list)

sum = 0

for i in range(n):
    sum = sum + list[i]
print(sum)


# Program to count total odd and even numbers


list1 = [1,2,45,6,6,73,4]

length_list = len(list1)

odd = 0
even = 0

for i in list1:
    if(i % 2 == 0):
        even = even + 1
    else:
        odd = odd + 1

print("Odd numbers count:", odd)
print("Even numbers count:", even)


# Program to search for a number in a list

numbers = [10, 25, 30, 45, 60, 75]

search_num = int(input("Enter a number to search: "))

# Flag
found = False

for num in numbers:
    if num == search_num:
        found = True
        break

if found:
    print(f"{search_num} is present in the list.")
else:
    print(f"{search_num} is not present in the list.")


# Python Program for Linear/Sequential Search


def linear_search(list, search_number):
    length_of_list = len(list)
    for i in range(length_of_list):
        if list[i] == search_number:
            return i
        else:
            return -1


numbers = [10, 25, 30, 45, 60, 75]
search_num = int(input("Enter a number to search: "))

# Perform the search
result = linear_search(numbers, search_num)

if result != -1:
    print(f"{search_num} is present at index {result}.")
else:
    print(f"{search_num} is not present in the list.")