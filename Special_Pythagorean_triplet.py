#https://projecteuler.net/problem=9

a = 0
b = 0
c = 0
d = 1000
for c in range(d):
    for b in range(c):
        for a in range(b):
            if a**2 + b**2 ==c**2:
                if a + b + c == d:
                    print(a*b*c)
