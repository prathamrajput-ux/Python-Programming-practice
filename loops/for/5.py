# number is composite number or prime number 
num = int(input("Enter your number : "))

comp = 0

for i in range (1,num):
    if(num%i==0):
        comp = 1
        break

if(comp == 1):
    print("Number is composite  ")


else : 
    print("Number is prime.")
