# cal the sum opf square of even number between 1 to n

n = int(input("Enter your number : "))

power = 0

for i in range(1,n+1):
    if (i%2==0):
        po = i**2

    else :
        po = 0

power = power + po

print(f"Sum of power of all number less than {n} is {power}")