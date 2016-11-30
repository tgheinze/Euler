# A palindromic number reads the same both ways.
# The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
#
# Find the largest palindrome made from the product of two 3-digit numbers.


def isPalendrome(p):
    x = str(p)
    y = x[::-1]
    if(x == y):
        return True
    else:
        return False

plist = []
for n1 in range(999, 99, -1):
    for n2 in range(999, 99, -1):
        if(n1 > n2): break
        p = n1*n2
        if(isPalendrome(p)): plist.append(p)

print(plist)
plist.sort()
print(plist)
print(len(plist))
if(len(plist) > 0): print(max(plist))




