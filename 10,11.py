from random import randint
N = 3
lst=[[randint(1, 9) for i in range(N)] for i in range(N)]
for i in lst:
    print()
    for j in i:
        print (j, end=" ")
