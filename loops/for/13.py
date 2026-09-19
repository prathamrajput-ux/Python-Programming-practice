#calculate the cube of 1 - n and calculate the sum of all number

n = int(input("Enter your number : "))
sum = 0
for i in range(1,n+1):
    cube = i ** 3
    sum = sum + cube
print(f"the cube of {n} is {cube}")
print(f"the sum  of  cube of 1 to {n} cube is {sum}")