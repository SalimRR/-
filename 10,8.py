a = str('Я хочу рабоать в следственном комитете Российской Федерации')
maximum = 0
for index, word in enumerate(a.split()):
    if len(word) > maximum:
        i = index
        maximum = len(word)
print(f'Слово длиной {maximum} находится на позиции {i + 1}')
