# calculate the hcf of 2 number

num1 = int(input("Enter your number : "))
num2 = int(input("Enter your number : "))

if (num1>num2):
    dividend = num1 
    divisor = num2


else :
    dividend = num2
    divisor = num1

while (divisor != 0):
    rem = dividend % divisor 
    dividend = divisor
    divisor = rem 

print(f"HCF Of {num1} and {num2} is {dividend}")