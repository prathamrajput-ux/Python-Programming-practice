'''
Program 4.45 Write a program to print the following pattern.
Pass 1- 1 2 3 4 5
Pass 2- 1 2 3 45
Pass 3- 1 2 3 4 5
Pass 4- 1 2 3 45
Pass 5- 1 2 3 4 5

'''

for i in range(1,6):
    print('Pass' , i , '- ' , end = "")

    for j in range(1,6):
        print( j , end = " ")

    print()