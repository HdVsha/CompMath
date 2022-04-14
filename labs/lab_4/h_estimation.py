import sympy


# Given interval
a = 1
b = 2

# Given accuracy
e = 0.0001

x = sympy.Symbol('x')
y = sympy.Symbol('y')

# f(x,y)
f = pow(y, 2) / pow(x, 2) + 3 / 2 * y / x - 1 / x

# Initial conditions
x_0 = 1
y_0 = 0.5

y_solve = sympy.sqrt(x) - x / 2  # It's exact solution to the given differential equation

N = 0


def runge(func, h):
    x_old = x_0
    y_old = y_0
    while x_old < b:
        p1 = func.subs({x: x_old, y: y_old})
        p2 = func.subs({x: x_old + h / 2, y: y_old + h / 2 * p1})
        p3 = func.subs({x: x_old + h / 2, y: y_old + h / 2 * p2})
        p4 = func.subs({x: x_old + h, y:  y_old + h * p3})
        y_new = y_old + h / 6 * (p1 + 2 * p2 + 2 * p3 + p4)
        y_old = y_new
        x_old += h

    return y_new


while True:
    N += 1  # число разбиений
    h = (b - a) / N  # шаг
    res_1 = runge(f, h / 2)
    res_2 = runge(f, h)
    print(res_1, res_2)
    delta = abs((res_1 - res_2))
    if delta < e:
        print(h)
        break
