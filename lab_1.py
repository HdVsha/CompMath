from sympy import *
# from tabulate import tabulate


x = Symbol("x")
f = exp(-1*x * sin(x)) - 3

"""
Graphics
"""

"""
We see that we have symmetrical solutions ==> we use 1 [] and find 1 sol-n x_0 and the second is -x_0
"""

"""
[a;b] = [2,5;4]
"""
a = Float(2.5)
b = Float(4.0)
x_ = (a + b) / 2
e = Float(pow(10, -4))
i = 1

f_A = []
f_B = []
X = []
f_X = []

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
    if f_a * f_x_ < 0:
        b = x_
    else:
        a = x_


# def bisection(a, b, e, f_A, f_B, f_X, X):
#
#     i = 1
#     while abs(a - b) > e:
#         i += 1
#         x_ = (a + b) / 2
#         X.append(x_)
#         f_a = f.subs(x, a)
#         f_A.append(f_a)
#         f_b = f.subs(x, b)
#         f_B.append(f_b)
#         f_x_ = f.subs(x, x_)
#         f_X.append(f_x_)
#         if f_a * f_x_ < 0:
#             b = x_
#         else:
#             a = x_

print(x_)
x_2 = -1 * x_
print(x_2)

# print(tabulate(headers = ["iteration", "f(a)", "f(b)", "f((a+b)/2)"], [f_A,]))


"""
Method of simple iteration
phi = x
"""

phi = -1 * ln(3.)/sin(x)
# print(phi)
# phi = asin(-1 * Float(ln(3.))/x)
x_0 = Float(2.5)
print(phi.diff(x))

"""
We have to check |phi.diff(x_0)| < 1
"""
x_1 = phi.subs(x, x_0)
i = 1
X_1 = []
X_0 = []
phi_ = phi.diff(x)
if abs(phi_.subs(x, x_0)) < 1.:
    print(phi)
    while abs(x_0 - x_1) > e:
        i += 1
        # X_1.append(x_1)
        # X_0.append(x_0)
        print(x_0)
        print(x_1)
        x_0 = x_1
        x_1 = phi.subs(x, x_1)
print(x_0, x_1, i)
print(X_0)
print(X_1)