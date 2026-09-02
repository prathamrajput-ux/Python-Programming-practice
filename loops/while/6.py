#the number until -1 is encountered . also count the negative, positive and zeros

positive = 0
negative = 0
zero = 0

print("Enter -1 to stop the program")

while (True):
    n = int(input("Enter your number : "))
    if (n==-1):
        print("You entered -1")
        break
    elif (n==0):
        zero = zero + 1 

    elif (n<0):
        positive = positive + 1

    else :
        negative = negative + 1

print("total number of zeroes is : ", zero)
print("total number of positive number is : ",positive)
print("total number of negative number is : ",negative)