# Write a program to sum the series-1/^2 + 1/ 2^2 + ... 1/n^

n = int(input("Enter you number : "))
s = 0.0
for i in range(1,n+1):
    a = 1.0/(i**2)
    s = s + a
print("Sum of all series is : ",s)