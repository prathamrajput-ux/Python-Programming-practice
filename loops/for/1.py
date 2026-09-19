# calculkate the avg of the first natural number 

n = int(input("Enter your num : "))
sum = 0
avg = 0 
for i in range(1, n+1 ):
    sum = sum + i
    avg = sum / i

print("Sum of number that you entered from 1 is",sum)
print("Average of number that you entered from 1 is",avg)