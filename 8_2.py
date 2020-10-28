s = str(input(''))
n = 10
def stroka(s, n):
    d = len(s)
    if d > n:
        print(s.upper())
    else:
        print(s)
stroka(s, n)
