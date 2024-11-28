number = int(input("Enter the number:"))

for i in range(2,number):
  if(number % i) == 0 :
    print(f"{number} is not prime number")
    break
else:
  print(f"{number} is prime no")

# programming logic basically kya hai ki sabse pehle humne ek number input kraya hai 
# phir ek for loop in range starts from 2 because 2 is the smallest prime no to stop n

# agar number kisi bhi integer se divide ho jata hai and remainder zero aata hai toh wo prime number nhi hai
# wrna prime number hai
