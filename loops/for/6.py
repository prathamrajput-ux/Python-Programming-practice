# while loop untill -1 to check prime and  composite 

prime = 0 
compo = 0 

while True :
    n = int(input("Enter Your Number : "))

    if(n == -1):
        break

    is_compo = 0
    for i in range(2,n):
        if(n%i == 0):
            is_compo = 1
            break

    if(is_compo):
        is_compo += 1

    else :
        prime +=1

print("Total  composite : ", is_compo)
print("Total prime :",prime)