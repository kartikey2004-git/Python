age = int(input("Enter your age:"))

# If statement no 1
if(age%2==0):
    print("a is even")
# End of If statement no 1

# If statement no 2
if age >= 18:
    print("You are above the age of consent")
    print("Good for you")
elif age < 0:
    print("You are entering a invalid negative age")
else:
    print("You are below the age of consent")
# End of If statement no 2

print("End of program")



