__author__ = 'tgheinze'

t = 1000
for a in range(1, t):
    for b in range(a, t-a):
        c = t - a - b
        if a<b and b<c:
          #print(a,b,c)
          #print(a+b+c)
          if a**2 + b**2 == c**2:
              print('ans = ',a,b,c)
              print(a*b*c)