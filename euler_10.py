# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
#
# Find the sum of all the primes below two million.

from functools import reduce

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

ans = reduce((lambda x, y: x + y), primes(2, 2000000))

print(ans)