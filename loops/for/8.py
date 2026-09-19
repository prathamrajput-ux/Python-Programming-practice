# leap year from interval

n = int(input("Enter your year from where you want to check :"))
m = int(input("Enter your year upto where you want to check"))

for i in range(n,m):
    if(i%4==0):
        print(i,end=" ")