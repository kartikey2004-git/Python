age = int(input("Enter your age:"))

# If elif else ladder

if age >= 18:
    print("You are above the age of consent")
    print("Good for you")
elif age < 0:
    print("You are entering a invalid negative age")
elif age == 0:
    print("You are entering a zero which is not a valid age ")
else:
    print("You are below the age of consent")

print("End of program")
