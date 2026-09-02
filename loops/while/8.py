n = int(input("Entyer your number : "))

num = n
x = 0 

while (n>0):
    r = n % 10
    x = x + (r**3)
    n = n // 10

if (x == num):
    print(f"Your number is armstrong number.")

else : 
    print(f"Your number  is  not armstrong number.")