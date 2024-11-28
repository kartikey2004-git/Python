n = int(input("Enter the number upto which u want to print factorial of:"))

product = 1
for i in range(1,n+1):
  product = product * i
  i+=1


print(f"factorial of {n} is {product}")


# 5! = 1*2*3*4*5

# range varies from 1 to n+1 
# ya keh skte hai starts from 1 and chalegi toh n+1 kyuki woh number bhi multiply mein aana chahiye

