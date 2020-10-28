from doctest import testmod
def func(x):
    """
    Чему равен Х?
    >>> func(4)
    512
    
    >>> func(3)
    145
    >>> func(2)
    32
    
    """
    x = int(input(''))
    if x > 0:
        return round(x**4 + 4**x) 

testmod(verbose = True)
