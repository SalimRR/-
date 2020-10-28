import math
def primer1():
    x = int(input('Введите х: '))
    y = int(input('Введите y: '))
    z = (x+((2+y)/x**2))/(y+(1/(math.sqrt(x**2 + 10))))
    print(z)
primer1()



def primer2():
    c =  int(input('0<=x<= 360 градусов: '))
    y = int(input('Введите y: '))
    x = math.radians(c)
    q = 2.8*math.sin(x) + math.fabs(y)
    print(q)
primer2()
