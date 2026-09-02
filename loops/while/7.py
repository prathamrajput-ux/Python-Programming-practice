#the number until -1 is encountered . also count the avg negative, positive

negative = 0
c_negative = 0
positive = 0 
c_positive = 0

print("Enter your number -1 ")
while True:
    n = int(input("Enter your number : "))
    if (n == -1):
        break
    elif (n<0):
        negative = negative + 1 
        c_negative = c_negative + n

    elif(n>0) :
        positive = positive + 1
        c_positive = c_positive + n
if positive > 0 :
    pos_average = float(c_positive)/positive
    print("Average of postive number :",pos_average)    

if negative < 0 :
    neg_average = float(c_negative)/negative
    print("Average of negative number :",neg_average)


