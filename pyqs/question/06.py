# Python program to count frequency of a number 

def freq_num(list,num):
  length_list = len(list)

  count = 0

  for i in range(length_list):
    if list[i] == num:
      count = count + 1

  return count


numbers = [1, 2, 2, 3, 4, 2, 5]
num_to_find = 2
result = freq_num(numbers, num_to_find)
print(f"The number {num_to_find} appears {result} times.")




# Python program to max and min number in python list 


def find_max_min(numbers):
    
    max_num = numbers[0]
    min_num = numbers[0]

    for num in numbers:
        if num > max_num:
            max_num = num
        if num < min_num:
            min_num = num

    return max_num, min_num

# Example list
numbers = [23, 1, 45, 90, -2, 8, 100]

# Get the max and min numbers
max_number, min_number = find_max_min(numbers)

print("Maximum number:", max_number)
print("Minimum number:", min_number)




# Python program to reverse the python list 

my_list = [1, 2, 3, 4, 5]

# Reversing the list using slicing
reversed_list = my_list[::-1]

print("Original List:", my_list)
print("Reversed List:", reversed_list)





# Python program to find the second maximum and second minimum values from a list

numbers = [10,20,30.40,80]

# remove the duplicate elements and sorting the list

# set build an unordered collection of unique elements
unique_numbers = list(set(numbers))

unique_numbers.sort()

# Finding the second minimum and second maximum

if len(unique_numbers) >= 2:
    second_min = unique_numbers[1]
    second_max = unique_numbers[-2]
    
    print("Second Minimum:", second_min)
    print("Second Maximum:", second_max)
else:
    print("Not enough unique elements to find second min and max.")
   



# Python program to search for a key in a dictionary


my_dict = {
    "name": "Kartikey",
    "age": 20,
    "college": "ABES Engineering College",
    "department": "ECE"
}

key_to_search = "age"

if key_to_search in my_dict:
   print(f"'{key_to_search}' found, value: {my_dict[key_to_search]}")
else:
    print(f"'{key_to_search}' not found in the dictionary.")





# Python program to find sum of even and products of odd digits of a number


num = input("Enter a number: ")

# Initialize sum and product
even_sum = 0
odd_product = 1

for digit in num:
    digit = int(digit) 
    if digit % 2 == 0:
        even_sum += digit 
    else:
        odd_product *= digit 

# Output the results
print("Sum of even digits:", even_sum)
print("Product of odd digits:", odd_product)


