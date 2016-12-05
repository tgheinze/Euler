__author__ = 'tgheinze'

from decimal import *
from math import *

#initialize constants
s9 = 2011

template = []
for i in range(0, s9):
    template.append('9')

s2011 = ''.join(template)

#  64**2n   where sqrt(1005)+sqrt(1006) ~= 64
#7922816251426433759354395033    8
#22300745198530623141535718272648361505980416     12

a = Decimal(713)
b = Decimal(720)
c = Decimal(.5)
n = 500
reset = 50
ans = 0
prec = 6000
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
    if i == 0:
        print("Resetting starting value of n")
        n -= reset
        continue
    if dec[0:s9] >= s2011:
        print('n: ', n, ' for (p,q) = (',a, ',',b, ')')
        ans += n
        break
    if (2011 - i) > 20:
        print('increasing n by ', int((2011 - i - 20) / 2))
        n += int((2011 - i - 10) / 2)
        reset = 5
    else:
        n += 1

print(ans)


print('-------------------------------------------')

def getPairs(min):

    ans = []

    for p in range(1, 1006):
        for q in range(p + 1, 2012 - p):

            if p % 100 == 0 and q == p+1: print(p)

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
            if i > 6:
                #print(a, b, i)
                ans.append((p,q))


    print(ans)
    return ans
ppairs = getPairs(12)
print('\n\n\n-------------------------------------------')

#print(ppairs)
print(' ')
#print(len(ppairs))
print('-------------------------------------------')


def run(pairs, start):

    ans = 0

    for pair in pairs:
        p = pair[0]
        q = pair[1]
        a = Decimal(p)
        b = Decimal(q)
        c = Decimal(.5)

        n = start
        reset = 50

        prec = 6000
        getcontext().prec = prec
        while True:
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
            if i == 0:
                print("Resetting starting value of n")
                n -= reset
                continue
            if dec[0:s9] >= s2011:
                print('n: ', n, ' for (p,q) = (', a, ',', b, ')')
                ans += n
                break
            if (2011 - i) > 20:
                print('increasing n by ', int((2011 - i - 20) / 2))
                n += int((2011 - i - 10) / 2)
                reset = 5
            else:
                n += 1

    print(ans)
    return ans



print(run(ppairs, 500))

#print(run([(2,3), (2,1800), (75,588), (154,163), (713,720)], 500))






