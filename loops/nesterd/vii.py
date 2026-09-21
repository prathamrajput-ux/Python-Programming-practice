'''
     1 
    2 2
   3 3 3
  4 4 4 4
 5 5 5 5 5 
'''

n = 5
for i in range(1,N+1):
    for k in range(n,i,-1):
        print("",end = ' ')
    for j in range(1,i+1):
        print(i,end =" ")
    print()