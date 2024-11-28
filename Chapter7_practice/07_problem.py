""" 

 For n=3
  *
 ***
*****

  For n=4
   *
  ***
 *****
*******


"""


n = int(input("Enter the number:"))

for i in range(1,n+1):
  print(" " * (n-i),end = "") # for printing spaces in star pattern 
  print("*" * (2*i-1),end = "") # for printing stars in star pattern
  print("\n")

# end = "" ye lagane se print by default koi nayi line add nhi krta hai

