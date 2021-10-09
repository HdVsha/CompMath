from sympy import symbols

e = pow(10, -2)

x = symbols('x')

f = pow(x, 3) - x + 1

f_ = f.diff(x)
x_0 = -2
x_1 = x_0 - f/f_

while abs(x_1.subs(x, x_0) - x_0) > e:
    if abs(x_1.subs(x, x_0) - x_0) < e + 0.06:
        f_ = f_
    x_0 = x_1.subs(x, x_0)
    x_1 = x_0 - f/f_

print(float(x_0))