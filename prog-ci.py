# A = P(1 + R/100)^t

import math

def compound_interest(p,t,r):
    amount = p * (pow((1 + r/100) , t))
    ci = amount - p
    print('Compound interest is: ', ci)
    return ci

p = int(input('Enter Principal amount: '))
t = float(input('Enter time period: '))
r = float(input('Enter rate of interest: '))

compound_interest(p, t, r)