m = float(input('Введите свой рост в m: '))
mkg = float(input('Введите массу своего тела: '))
def info(m, mkg):
    BMI = str('Body mass index')
    print(BMI)
    index= mkg/m**2
    if 16.0<index<19.9:
        print('Вес ниже нормального')
    elif 20.0<index<25.9:
        print('Нормальный вес')
    elif 26.0<index<29.9:
        print('Превышение веса')
    elif 30.0<index<39.9:
        print('Ожирение')
    else:
        print('Что-то пошло не так')

info(m, mkg)
