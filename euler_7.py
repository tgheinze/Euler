#What is the 10 001st prime number?

def primes(halt):
    end = halt
    i = 3
    plist = [2]
    end -= 1
    yield 2
    while end > 0:
        for p in plist:
            if i % p == 0 or p * p > i:
                #by this point we've ruled out all the primes up to p, so if i is not prime
                #then it would have to be the product of two primes whose value would exceed i
                break
        if i % p:
            plist.append(i)
            end -= 1
            yield i
        if end == 0: break
        else: i += 2

p = [p for p in primes(10001)]

print(len(p))
#print(p)
print(p[len(p)-1])

