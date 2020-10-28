L = [3, 'hello', 7, 4, 'привет', 4, 3, -1]
a ="привет"
if a in L:
    L.remove(a)
else:
    L.append(a)
print(L)

b = L.count(4)
if b > 1:
    L.clear()
    print(L)
