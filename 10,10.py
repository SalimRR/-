from random import randint
N = 3
M = 5
lst=[[randint(2, 11) for i in range(N)] for i in range(M)]
for i in lst:
    print()
    for j in i:
        print (j, end=" ")
