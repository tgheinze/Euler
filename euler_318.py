__author__ = 'tgheinze'

from decimal import *
from math import *

s9 = 2011

template = []
for i in range(0, s9):
    template.append('9')

s2011 = ''.join(template)


# a = Decimal(2)
# b = Decimal(3)
# c = Decimal(.5)
#
# n = 2018
#
#
#
# prec = 4000
# getcontext().prec = prec
# cont = True
# while cont:
#     x = (a**c + b**c)**(Decimal(2*n))
#     dec = str(x - int(x))[1:2]
#     if dec != '.':
#         print('setting prec')
#         prec += 100
#         getcontext().prec = prec
#         continue
#     num = len(str(int(x)))
#     getcontext().prec = num + s9 + 10
#     x = (a ** c + b ** c) ** (Decimal(2 * n))
#     print(x)
#     dec = str(x-int(x))[2:]
#     #print(dec)
#     i = 0
#     while True:
#         if dec[i] == '9':
#             i += 1
#             continue
#         else: break
#     print(n, '      ', i)
#     #print(len(dec))
#     if dec[0:s9] == s2011:
#         print('n: ', n)
#         cont = False
#         break
#     n += 1

a = Decimal(2)
b = Decimal(6)
c = Decimal(.5)
n = 2000
reset = 50
ans1 = 0
ans = 0
prec = 4000
getcontext().prec = prec
cont = True
while cont:
    print(n)
    x = (a ** c + b ** c) ** (Decimal(2 * n))
    dec = str(x - int(x))[1:2]
    if dec != '.':
        print('resetting prec, length int part is at least', len(str(int(x))))
        prec += 1000
        getcontext().prec = prec
        continue
    num = len(str(int(x)))
    getcontext().prec = num + s9 + 10
    x = (a ** c + b ** c) ** (Decimal(2 * n))
    # print(x)
    dec = str(x - int(x))[2:]
    # print(dec)
    i = 0
    while True:
        if dec[i] == '9':
            i += 1
            continue
        else:
            break
    print(n, '      ', i)
    if i == 0 or i > 2011:
        print("Resetting starting value of n")
        n -= reset
        continue
        # return
    # print(len(dec))
    if dec[0:s9] == s2011:
        print('n: ', n, ' for (p,q) = (', p, ',', q, ')')
        ans += n
        if p == 1: ans1 += 1
        cont = False
        break
    if (2011 - i) > 2:
        n += (2011 - i)
        reset = 2
    else:
        n += 1

print(ans)
print(ans1)

print('-------------------------------------------')


def run(min):
    ans1 = 0
    ans = 0

    for p in range(2, 1006):
        for q in range(p + 1, 2012 - p):
            a = Decimal(p)
            b = Decimal(q)
            c = Decimal(.5)

            n = min
            reset = 50

            prec = 4000
            getcontext().prec = prec
            cont = True
            while cont:
                #print(n)
                x = (a ** c + b ** c) ** (Decimal(2 * n))
                dec = str(x - int(x))[1:2]
                if dec != '.':
                    print('resetting prec, length int part is at least', len(str(int(x))))
                    prec += 1000
                    getcontext().prec = prec
                    continue
                num = len(str(int(x)))
                getcontext().prec = num + s9 + 10
                x = (a ** c + b ** c) ** (Decimal(2 * n))
                # print(x)
                dec = str(x - int(x))[2:]
                # print(dec)
                i = 0
                while True:
                    if dec[i] == '9':
                        i += 1
                        continue
                    else:
                        break
                print(n, '      ', i)
                if i == 0 or i > 2011:
                    print("Resetting starting value of n")
                    n -= reset
                    continue
                    #return
                # print(len(dec))
                if dec[0:s9] == s2011:
                    print('n: ', n, ' for (p,q) = (', p, ',', q, ')')
                    ans += n
                    if p == 1: ans1 += 1
                    cont = False
                    break
                if (2011 - i) > 2:
                    n += (2011 - i)
                    reset = 2
                else:
                    n += 1

    print(ans)
    print(ans1)
    return ans



#run(2000)






