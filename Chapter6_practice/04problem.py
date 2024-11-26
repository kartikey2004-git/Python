username = input("Enter your username: ")
# print(len(username))

if(len(username)<10):
  print(f"{username} contains less than 10 characters")
else:
  print(f"{username} contains more than 10 characters")