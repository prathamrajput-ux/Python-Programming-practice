'''
              1
            1 2 1
          1 2 3    2 1 
        1 2 3 4 3  2  1
      1 2 3 4 5 4  3 2 1
'''

n = 5
for i in range(1,n+1):
    for j in range(n,1,-1):
        print(" ",end = '')
    for k in range(1,i+1):
        print(j,end = " ")
    for l in range(i-1,0,-1):
        print(l,end= " ")
    print()