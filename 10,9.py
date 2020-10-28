t = input("Введите свой текст: \n")
ls = []
for i in t:
    if i in '1234567890':
        ls.append(int(i))
print(ls)
print(len(ls))
print(sum(ls))
print(max(ls))
