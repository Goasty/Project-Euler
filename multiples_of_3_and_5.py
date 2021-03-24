li = []
num = []
x = range(1,1000)
for n in x:
    num.append(n)
for d in num:
    if not d % 3:
        if d not in li:
            li.append(d)
for d in num:
    if not d % 5:
        if d not in li:
            li.append(d)
print(li)
print(sum(li))
