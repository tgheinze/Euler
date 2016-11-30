__author__ = 'tgheinze'

#What is the largest prime factor of the number 600851475143 ?


n = 600851475143


def primes(min, max):
    plist = [2]
    if 2 >= min: yield 2
    for i in range(3, max + 1, 2):
        for p in plist:
            if i % p == 0 or p * p > i:
                #by this point we've ruled out all the primes up to p, so if i is not prime
                #then it would have to be the product of two primes whose value would exceed i
                break
        if i % p:
            plist.append(i)
            #print('num primes = ', len(plist), ' for i ', i)
            if i >= min: yield i


def factors(number):
    for prime in primes(2, number):
        if number % prime == 0:
            #print('----------> ', number, '    ', prime)
            number /= prime
            yield prime
        if number == 1:
            break



print(max(factors(n)))


i = 2
while i * i < n:
    while n % i == 0:
        n = n / i
    i = i + 1
print(n)


def primes2(max):
    plist = [2]
    r = []
    for x in range(3, max + 1, 2):
        r.append(x)
    for i in r:
        for n in plist:
            if i % n == 0 or n * n > i: break
        if i % n:
            plist.append(i)
    return plist


def factors2(num):
    f = []
    for p in primes2(num):
        if num % p == 0:
            f.append(p)
    return f


print(max(factors2(3517)))
