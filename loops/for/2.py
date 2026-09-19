# table from n to n

n = int(input("Enter your number : "))
print("Multiplication table of ", n)
#print('\n')
for i in range(1, n + 1):
    print(f"{n} X {i} = {n*i}")