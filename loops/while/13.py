#reverse number
num = int(input("Enter Your Number : "))
print("Your reverse number is :")
while(num != 0):
    n = num % 10
    print(n,end= " ")
    num = num // 10

