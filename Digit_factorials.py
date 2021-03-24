#https://projecteuler.net/problem=34
a = 145
list = []
n_list = []
for i in str(a):
    list.append(int(i))
for b in list:
    for c in range(b,0,-1):
        n_list.append(c)
print(n_list)
