li = []
a = 1
b = 2
c = 0

while c < 4000000:
    c = b + a
    if not c % 2:
        if c not in li:
            li.append(c)
    a = b
    b = c
    continue
print(li)
print(sum(li) + 2)
