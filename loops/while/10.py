'''Program 4.24 Write a program to read a character until a * is encountered. Also count the
number of uppercase, lowercase, and numbers entered by the users.'''



num = 0
lower  = 0
upper = 0 



while True : 
    a = input("enter your character. To exit enter * : ")

    if a == '*':
        break

    elif (a >= '0' and a <= '9') :
        num = num + 1

    elif ( a >= 'a' and a <= 'z'):
        lower = lower + 1

    elif ( a >= 'A' and a <= 'Z') :
        upper = upper + 1


print("You enter total digit : ",num)
print("you enter total upper case : ",upper)
print("you enter total lower case", lower)
