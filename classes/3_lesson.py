from sympy import symbols, div

x = symbols('x')

f = -32*pow(x, 3) + 20*pow(x, 2) + 11*x + 3

"""
1. Localize: find [a, b] (Look at the 2-nd point)
"""


"""
2. Decart Theorem

A = 20 = max{|a_i|} (1 <= i <= n)
B = 32 = max{|a_i|} (0 <= i <= n-1)
|a_n|/(|a_n|+ B)  <= |x| <= 1 + A / |a_0|
 3/35==a <= |x| <= 13/8 ==b  ---> x in [3/35, 13/8]
 
 
-32, 20, 11, 3 --- 1 change of sign ---> 1 "+" solve
x ---> -x  --->  2 changes ---> either 2 or 0 negative solves
"""


"""

3. Burade-Furie's Theorem

"""

f_ = f.diff(x)      # -96*x**2 + 40*x + 11
f__ = f_.diff(x)    # 40 - 192*x
f___ = f__.diff(x)  # -192

"""
x = a = 3/35 and x = b = 13/8 put into f, f_, f__, f___
and look at the number of changes of sign:
    for a: +, +, +, -   ---> S(a+0) = 1
    for be: -, -, -, -  --- S(b-0) = 0
    
delta = S(a+0) - S(b-0) = 1 - the number of real solves on [a, b]
"""

"""
4. Shturm's Theorem

f_0 = f

f_1 = f_
f_2 = -Res{f_0/f_1} == -sympy.div(f_0, f_1) = -96*x^2 + 40*x + 11
f_3 = -(91*x/9 + 271/72)
f_4 = 284751/16562

Then the same for a and b as in Burade-Furie's Theorem
And the answer is delta = 2 - 1 = 1
"""
# f_2, a = reduced(f, f_) -- not working(working with REAL PYTHON DEF, probably)
# print(f_2)
f_3 = div(f, f_)       # == (x/3 - 5/72, 91*x/9 + 271/72), the second is what we need, the 1st is int
f_4 = div(f_, f_3[1])  # == (62028/8281 - 864*x/91, -284751/16562)
