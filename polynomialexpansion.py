"""
 @author    : macab (macab@debian)
 @file      : simplify
 @created   : Friday Mar 15, 2019 01:52:19 IST
"""

from sympy import*

x, y, z = symbols('x y z')
init_printing(use_unicode=True)

#print(simplify(sin(x)**2 + cos(x)**2))


exp = expand((x - 1)**4)  # factor() is opposite to the expand

a = poly(exp, x)
mylist  = []
mylist = a.coeffs()


# print polynomial expansion
print(exp)
# print list of coeff
print(mylist)

