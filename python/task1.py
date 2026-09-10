#1
import math

def f(x):
    return (2*x**2+1.2-math.cos(x) )**0.5-1

def znaki(a, b, eps=1e-6, max_iter=1000):   #проверка на знаки границ
    fa, fb = f(a), f(b)
    if fa*fb > 0:
        return 0

    for i in range(1000):
        c=(a+b)/2
        fc = f(c)
        if abs(fc)<eps or (b-a)/2<eps:        #значение функции стало почти нулём
            print(f"\nКорень найден: x = {c:.5f}")
            return c

        if fa*fc < 0:
            b=c
            fb=fc
        else:
            a=c
            fa=fc

    return (a+b)/2

probeg = znaki(0, 1)


#2
import math

def f(x):
    return (2*x**2+1.2-math.cos(x) )**0.5-1

def znaki(a, b, eps=1e-6, max_iter=1000):
    fa = f(a)
    fb = f(b)
    if fa*fb >= 0:
        return 0
    x_0=None #пред значения пока нет

    for k in range(0, 1000):
        xk = a - (fa*(b-a)) / (fb-fa) #новая точка пересечения с осью OX
        fxk = f(xk)

        if fa * fxk < 0:
            b, fb = xk, fxk
        else:
            a, fa = xk, fxk

        if x_0 is not None and abs(xk - x_0) <= eps:
            return xk, k

        x_0 = xk

    return x_0, max_iter

a, b, eps = 0, 1, 1e-6
otv, nomer = znaki(a, b)

print(f"Корень x = {otv:.5f}")
