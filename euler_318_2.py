__author__ = 'tgheinze'

from decimal import *
from math import *

#initialize constants
s9 = 2011

template = []
for i in range(0, s9):
    template.append('9')

s2011 = ''.join(template)

#7922816251426433759354395033

a = Decimal(2)
b = Decimal(3)
c = Decimal(.5)
n = 2000
reset = 50
ans = 0
prec = 4000
getcontext().prec = prec

while False:
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
        print('n: ', n, ' for (p,q) = (',a, ',',b, ')')
        ans += n
        break
    if (2011 - i) > 2:
        n += (2011 - i)
        reset = 2
    else:
        n += 1

print(ans)


print('-------------------------------------------')

def getPairs(min):

    ans = []

    for p in range(1, 1006):
        for q in range(p + 1, 2012 - p):
            a = Decimal(p)
            b = Decimal(q)
            c = Decimal(.5)

            n = min

            prec = 50
            getcontext().prec = prec

            e = Decimal(2 * n)

            x = (a ** c + b ** c) ** e
            dec = str(x - int(x))[1:2]
            num = int(x)
            #print(str(x))
            ##print(len(str(num)))
            if dec != '.':
                if len(str(num)) < prec:
                    continue
                else:
                    print("error")
                    return

            #num = len(str(int(x)))
            dec = str(x - int(x))[2:]
            #print(dec)
            i = 0
            while i < len(dec):
                if dec[i] == '9':
                    i += 1
                    continue
                else:
                    break
            #print(n, '      ', i)
            if i > 0:
                #print(a, b, i)
                ans.append((a,b))


    print(ans)
    return ans
pairs = getPairs(10)
print(len(pairs))
print(pairs)
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






