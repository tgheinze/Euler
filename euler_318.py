__author__ = 'tgheinze'

from decimal import *
from math import *

s9 = 2011

template = []
for i in range(0, s9):
    template.append('9')

s2011 = ''.join(template)


a = Decimal(2)
b = Decimal(3)
c = Decimal(.5)

n = 2018



prec = 4000
getcontext().prec = prec
cont = True
while cont:
    x = (a**c + b**c)**(Decimal(2*n))
    dec = str(x - int(x))[1:2]
    if dec != '.':
        print('setting prec')
        prec += 100
        getcontext().prec = prec
        continue
    num = len(str(int(x)))
    getcontext().prec = num + s9 + 10
    x = (a ** c + b ** c) ** (Decimal(2 * n))
    print(x)
    dec = str(x-int(x))[2:]
    #print(dec)
    i = 0
    while True:
        if dec[i] == '9':
            i += 1
            continue
        else: break
    print(n, '      ', i)
    #print(len(dec))
    if dec[0:s9] == s2011:
        print('n: ', n)
        cont = False
        break
    n += 1












