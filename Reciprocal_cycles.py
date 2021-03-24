#https://projecteuler.net/problem=26

a = 1
b = []
d = []
for i in range(1,1000):
    b.append(i)
for f in b:
    c = a / f, f
    d.append(c)
print(d)
