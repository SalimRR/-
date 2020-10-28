L = [3, 6, 7, 4, -5, 4, 3, -1]
a = sum(L)
print(a)
if a >  2:
    print(len(L))

b = abs(min(L)-max(L))
if b > 10:
    print(sorted(L))
else:
    print("Разность меньше 10")
