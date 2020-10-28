import random
def igra():
    print(str('Введите число от 10 до 20'))
    d = random.randint(10, 20)
    while True:
        c = input("\nВаше число или напишите слово \'Выход\': ")
        if c == 'Выход':
            print('\nВ следующий раз повезёт :(')
            break

        c = int(c)

        if c == d:
            print('Победа, ', d)
            break
        elif c>d:
            print('\nВаше число больше загаданного!')
        elif c<d:
            print('\nВаше число меньше загаданного!')
igra()
