#https://projecteuler.net/problem=20
x = []
y = []
max = 0
max_list = []
for i in range(1, 101):
    y.append(i)
y.reverse()
#print(y)
t = 1
for m in y:
    t *=m
    x.append(t)
for b in x:
    if b > max:
        max = b
for d in str(max):
    max_list.append(int(d))

print(sum(max_list))
print(max_list)
