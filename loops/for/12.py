#calculate the cube of 1 - n

n = int(input("Enter your number : "))

for i in range(1,n+1):
    cube = i ** 3

print(f"the cubhe of {n} is {cube}")