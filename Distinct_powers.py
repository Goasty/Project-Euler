#https://projecteuler.net/problem=29
list = []
for i in range(2,101):
    for p in range(2, 101):
        list.append(i**p)
list = sorted(set(list))
print(len(list))
