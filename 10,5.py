print('Введите любое число:')
n = input()
if all(map(str.isdigit, n)):
    sm = 0
    lst = list(map(int, n))
    for i  in lst:
        if i % 2 != 0:
            sm += i**2
            print(sm)
        else:
            print("Эта цифра чётная!")
