# cal the power

num = int(input("Enter your number : "))
m = int(input("Enter the number till power you want ? : "))

result = 1
for i in range(m):
    result = result * num

print(num, "raised to power",m,"is",result)