# sum of series - 1 + 1/2 +...+1/n

n = int(input("Enter the number : "))
s = 0.0
for i in range(1,n+1):
    a = 1.0/i
    s = s+a

print(f"The sum opf series 1+1/2+..+{1/n} is {str(s)}")