marks_subject1 = int(input("Enter the marks of subject1 : "))
marks_subject2 = int(input("Enter the marks of subject1 : "))
marks_subject3 = int(input("Enter the marks of subject1 : "))

# Check for total percentage

sum = marks_subject1 + marks_subject2 + marks_subject3

total_percentage = (sum / 300) * 100
if (
    total_percentage > 40
    and marks_subject1 >= 33
    and marks_subject2 >= 33
    and marks_subject3 >= 33
):
    print(f"you are passed with {int(total_percentage)} percent")
else:
    print(
        f"you are failed with {int(total_percentage)} percentage, try again next year!"
    )
