s = "У лукоморья 123 дуб зеленый 456"
print(s[10])
print(s.index("я"))
print(s.lower().count('у'))
y = s.isalpha()
if y != True:
    print(s.upper())
a = len(s)
if a > 4:
    print(s.lower())
print(s.replace(s[0], 'О'))
