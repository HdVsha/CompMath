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
    x_array = []
    y_array = []
    while x_old < b:
        x_array.append(x_old)
        y_array.append(y_old)
        p1 = func.subs({x: x_old, y: y_old})
        p2 = func.subs({x: x_old + h / 2, y: y_old + h / 2 * p1})
        p3 = func.subs({x: x_old + h / 2, y: y_old + h / 2 * p2})
        p4 = func.subs({x: x_old + h, y:  y_old + h * p3})
        y_new = y_old + h / 6 * (p1 + 2 * p2 + 2 * p3 + p4)
        y_old = y_new
        x_old += h
    x_array.append(x_old)
    y_array.append(y_old)
    print(x_array)
    print(y_array)


h = 0.005
runge(f, h)
