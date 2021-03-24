#https://projecteuler.net/problem=36
y = []
a = []
x = 1
while x < 1000000:
    if x == int(str(x)[::-1]):
        y.append(x)
    x +=1
print(y)
for z in y:
    if int(bin(z)[2:]) == int(str(bin(z)[2:])[::-1]):
        a.append(z)
print(sum(a))
