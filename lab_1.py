from sympy import *

def func(x, x_):
    return (100*(x - x_)/x),x -x_

x = Symbol("x")

"""
Graphics
"""

"""
We see that we have symmetrical solutions ==> we use 1 [] and find 1 sol-n x_0 and the second is -x_0
"""

"""
1.[a;b] = [2,5;4]
"""

e = Float(pow(10, -4))
i = 1

f_A = []
f_B = []
X = []
f_X = []
# f = exp(-1*x * sin(x)) - 3
f = x + ln(x)


def bisection(a, b, e, f_A, f_B, f_X, X, f):
    x_ = (a + b) / 2
    i = 0
    while abs(a - b) > e:
        i += 1
        x_ = (a + b) / 2
        X.append(x_)
        f_a = f.subs(x, a)
        f_A.append(f_a)
        f_b = f.subs(x, b)
        f_B.append(f_b)
        f_x_ = f.subs(x, x_)
        f_X.append(f_x_)
        if i ==1:
            print("Iteration", "|", "x_", "|", "f(a)", "|", "f(b)", "|", "f((a+b)/2)")
        print(f"{i}",f"|", f"{x_}", "|", f"{f_a}", "|", f"{f_b}", "|", f"{f_x_}" )
        if f_a * f_x_ < 0:
            b = x_
        else:
            a = x_
    return x_, f_A, f_B, f_X, X


# res = bisection(0.2, 1., e, f_A, f_B, f_X, X, f)
# x_ = res[0]
# print(f"Конечный результат = {x_}")
# print(f"Абсолютная погрешность: {func(0.567143, x_)[1]}")
# print(f"Относительная погрешность: {func(0.567143, x_)[0]}")
# x_2 = -1 * x_
# print(x_2)


"""
second func
2. a) [a;b] = [-1.5, -1.]
   b) [-1., -0.5]
   c) [0.5, 1.]
first func 
1. [a;b] = [0.2, 1.]
"""
# f = 2.*pow(x, 5) - 5.*pow(x, 4) + 15.*pow(x, 2) - 7
# print()
# res = bisection(-1.5, -1., e, f_A, f_B, f_X, X, f)
# print(res[0])
# res = bisection(-1., -0.5, e, f_A, f_B, f_X, X, f)
# print(res[0])
# res = bisection(0.5, 1., e, f_A, f_B, f_X, X, f)
# print(res[0])
"""
Method of simple iteration
phi = x
"""

phi = -exp(x)

"""
We have to check |phi.diff(x_0)| < 1
"""
x_0 = Float(0.000000001)
x_1 = phi.subs(x, x_0)
X_1 = []
X_0 = []
phi_ = phi.diff(x)


def msi(x_0, X_0, X_1, phi, e):
    i = 0
    x_1 = phi.diff(x).subs(x, x_0)
    if abs(x_1) < 1.:
        while abs(x_0 - x_1) > e:
            i += 1
            X_1.append(x_1)
            X_0.append(x_0)
            if i == 1:
                print("Iteration", "|", "x_n+1 = phi(x_n)", "|", "x_n")
            print(f"{i}", "|", f"{x_1}", "|", f"{x_0}")
            x_0 = x_1
            x_1 = phi.subs(x, x_1)
    return x_0, X_0, X_1


# res = msi(x_0, X_0, X_1, phi, e)
# x_ = res[0]
# print(f"Конечный результат = {x_}")
# print(f"Абсолютная погрешность: {func(0.567143, x_)[1]}")
# print(f"Относительная погрешность: {func(0.567143, x_)[0]}")


"""
Newton's method
"""

f_ = f.diff(x)
f__ = f_.diff(x)

x_0 = 0.3


def newton(x_1, x_0, f, f_):
    i = 0
    print(f"x0 = {x_0}")
    while abs(x_1.subs(x, x_0) - x_0) > e:
        i += 1
        if i ==1:
            print("Iteration", "|", "x0", "|", "f(x0)", "|", "f'(x_0)")
        print(f"{i}",f"|", f"{x_0}", "|", f"{f.subs(x, x_0)}", "|", f"{f_.subs(x, x_0)}" )
        x_0 = x_1.subs(x, x_0)
        x_1 = x_0 - f / f_
    return x_0


def mod_newton(x_1, x_0, f, f_):
    i = 0
    x_tmp = x_0
    flag = True
    while abs(x_1.subs(x, x_0) - x_0) > e:
        i+=1
        if abs(x_1.subs(x, x_0) - x_0) < e + 0.006:
            flag = False
        if i ==1:
            print("Iteration", "|", "x0", "|", "f(x0)", "|", "f'(x_0)")
        print(f"{i}",f"|", f"{x_0}", "|", f"{f.subs(x, x_0)}", "|", f"{f_.subs(x, x_0)}" )
        x_0 = x_1.subs(x, x_0)
        if flag:
            x_1 = x_0 - f / f_
        else:
            x_1 = x_0 - f / f_.subs(x, x_tmp)
    return x_0


print(f"F(x0)*F''(x0) = {f.subs(x, 0.3)*f__.subs(x, 0.3)}")
print()
# print(mod_newton(x_1, x_0, f, f_))
x_ = newton(x_1, x_0, f, f_)
print(f"Конечный результат = {x_}")
print(f"Абсолютная погрешность: {func(0.567143, x_)[1]}")
print(f"Относительная погрешность: {func(0.567143, x_)[0]}")

# print(f"F(x0)*F''(x0) = {f.subs(x, -0.7)*f__.subs(x, -0.7)}")
x_0=-0.7
x_1 = x_0 - f/f_

# print(newton(x_1, x_0, f, f_))
# print(mod_newton(x_1, x_0, f, f_))

x_0=0.5
x_1 = x_0 - f/f_

# print(newton(x_1, x_0, f, f_))
# print(mod_newton(x_1, x_0, f, f_))


def secant(a, b, f, e, max) -> Float:
    """
    return: root of f(x) = 0
    """
    i = 0
    while abs(a - b) >= e and i < max:
        a = b - (b - a) * f.subs(x, b) / (f.subs(x, b) - f.subs(x, a))
        b = a - (a - b) * f.subs(x, a) / (f.subs(x, a) - f.subs(x, b))
        i = i + 1
        if i ==1:
            print("Iteration", "|", "a", "|", "b", "|", "f(a)", "|", "f(b)")
        print(f"{i}",f"|", f"{a}", "|", f"{b}", "|", f"{f.subs(x, a)}", "|", f"{f.subs(x, b)}" )
    return b
# print()
# print("[-1.5, -1] ", secant(-1.5, -1., f, e, 100))
# print("[-1, -0.5] ",secant(-1., -0.5, f, e, 100))
# print("[0.5, 1] ",secant(0.5, 1., f, e, 100))