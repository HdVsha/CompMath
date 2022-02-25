"""

By now we have computed I_1 (by using method of fraction into 2 integrals and using Taylor's formula)
We found that delta = pow(10, -6)/4  (10^-6 /4)

"""
from sympy import Symbol, ln, Float, solve

a = Float(pow(10, -6) / 4)  # - that is our delta
b = 1

x = Symbol('x')
f = ln(1 + pow(x, 2/3)) / x


def find_extremums(func, arg):
    dy = func.diff(arg)
    extremums = solve(dy, arg)

    return extremums


"""
For every method we will have different h
"""



f_1 = f.diff(x)  # This is the first derivative of f
f_2 = f_1.diff(x)  # This is the second
f_4 = f_2.diff(x).diff(x)  # This is the 4th

# m1 = maximum(f_1, x, domain=Interval(a, b))   - This func will not succeed as there are no extremums
'''
That is why We will use Runge's Method of Assessment and the same h (will see)
'''

h = 0.00001


def aver_rectangle(f, h, a):

    n = int((b - a) / h)
    res = 0
    for i in range(n):
        res += (h * f.subs(x, (a + h/2) + i*h))
    return res


def right_rectangle(f, h, a):

    n = int((b - a) / h)
    res = 0
    for i in range(n):
        res += (h * f.subs(x, a + i * h))
    return res


def trapezoidal(f, a, b, h):
    n = int((b - a) / h)
    result = 0.5*f.subs(x, a) + 0.5*f.subs(x, b)
    for i in range(n):
        result += f.subs(x, a + i*h)
    result *= h
    return result


def simpsons(f, a, b, h):

    tmp_sum = float(f.subs({x: a})) + \
              float(f.subs({x: b}))
    n = int((b - a) / h)
    for step in range(n):
        if step % 2 != 0:
            tmp_sum += 4 * float(f.subs({x: a + step * h}))
        else:
            tmp_sum += 2 * float(f.subs({x: a + step * h}))

    return tmp_sum * h / 3

# print(aver_rectangle(f, h, a))  I_h = 1.23362
# print(aver_rectangle(f, 2*h, a))  I_2h = 1.23353
# Then the delta / 2 is definitely < epsilon (thus we choose this h for every other method, bc it suits well)

# print(right_rectangle(f, h, a))  I_h = 1.23354

# print(trapezoidal(f, a, b, h))  I_h = 1.23366

# print(simpsons(f, a, b, h))  I_h = 1.23345

