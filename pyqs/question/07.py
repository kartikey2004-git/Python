# Python program to Shifting each list element one step left  in python 


def shift_left(list):
  if len(list) > 0:
    first_element = list.pop(0) 
    list.append(first_element)
  return list


my_list = [1, 2, 3, 4, 5]
shifted_left_list = shift_left(my_list.copy()) 
# Using copy() to preserve original list

print("Original List:", my_list)
print("Shifted Left:", shifted_left_list)





# Python program to Shifting each list element one step right in python 


def shift_right(lst):
    if len(lst) > 0:
        last_element = lst.pop()
        lst.insert(0, last_element)
    return lst

# Example usage
my_list = [1, 2, 3, 4, 5]
shifted_right_list = shift_right(my_list.copy())  # Using copy() to preserve original list

print("Original List:", my_list)
print("Shifted Right:", shifted_right_list)





# # Program to insert a given element in list at given position

# # Dynamic list formation

# a = []
# size = int(input("Enter the size of the list"))

# for i in range(size):
#    val = int(input("Enter the value"))
#    a.append(val)

# print("Original list is: ",a)


# key = int(input("Enter the input to insert: "))
# position = int(input("Enter the position to insert: "))


# a.append(None)