total = 0
while True:
    n = input('Введите число или напишите \'Стоп\' для суммирования: ')
    if str(n) == 'Стоп':
        print('Ваша сумма равна: ', total)
        break
            
    else:
        total = total + int(n)
