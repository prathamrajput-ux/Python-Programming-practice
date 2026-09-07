#Write a program to enter a number and the calculate the sum of its digits.

sum  = 0 

num = int(input('Enumter your number : '))

while (num != 0) :
    rem =  num % 10 
    sum = num + rem
    num = num/10

print("Sum of your  digit",sum)