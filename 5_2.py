a = int()
b = int()
def maximal(a, b):
    """Напишите целочисленные значения a и b"""
    help(maximal)
    a = int(input('Введите целое число для а: '))
    b = int(input('Введите целое число для b: '))
    if a > b:
        print('max = ', a)
    elif b>a:
        print('max = ', b)
    else:
        print('a не может быть равно b')
maximal(a, b)

