from random import randint
N = 3
M = 5
lst=[[randint(2, 11) for i in range(N)] for i in range(M)]
for i in lst:
    print()
    for j in i:
        print (j, end=" ")
kol=0 #количество одинаковых элементов равно нулю
num_str=0# индекс строки
for i in range(M): #цикл по всем элементам матрицы
    for j in range(N):
        kol_new=lst[i].count(lst[i][j])# подсчитываю кол-во определённого [i][j] символа в i-строке
        if kol_new>kol: # если больше, то
            kol=kol_new # заменить максимальное число
            num_str=i   # и запомнить индекс строки в которой сейчас находимся
print()
print("Номер строки: ", num_str)
