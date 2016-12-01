__author__ = 'tgheinze'

# The sum of the squares of the first ten natural numbers is,
#
# 12 + 22 + ... + 102 = 385
# The square of the sum of the first ten natural numbers is,
#
# (1 + 2 + ... + 10)2 = 552 = 3025
# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.
#
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

max = 100
def getInts(max):
    for i in range(1, max+1):
        yield i

squares = [x**2 for x in getInts(max)]

squaresSum = sum(squares)
sumIntsSquared = sum(getInts(max))**2

print(sumIntsSquared - squaresSum)