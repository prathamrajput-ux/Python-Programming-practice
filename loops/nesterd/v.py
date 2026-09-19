'''
0
12
345
6789
'''


count = 0

for row in range(1, 5):
    for column in range(row):
        print(count, end="")
        count += 1
    print()