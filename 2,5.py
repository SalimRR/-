def func(A1=1, B1=2, C1=3, A2=4, B2=5, C2=6):
    D=A1*B2-A2*B1
    x=(C1*B2-C2*B1)/D
    y=(A1*C2-A2*C1)/D
    C1=A1*x+B1*y
    C2=A2*x+B2*y
    return(C1, C2)
