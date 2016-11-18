__author__ = 'tgheinze'

import sys

from pprint import pprint as pp


pp(sys.path)


t = 0


for n in range(1000):
    if not(n%3) or not(n%5):
      #print n
      t += n

print(t)
