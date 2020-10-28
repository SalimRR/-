a = ()
def proverka(a):
    """Здесь идет проверка числа на четность"""
    help(proverka)
    a = int(input('Введите целое число a:'))
    if a%2 == 0:
        print('Значение "a" четное')
    else:
        print('Значение "a" нечетное')
proverka(a)
