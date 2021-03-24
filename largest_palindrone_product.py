#x = 888889
#x = str(x)[::-1]
#print(x)

finallist = []
mylist = []
newlist = []
x = range(100,1000)
somlist = []
otherlist = []
for n in x:
    somlist.append(n)
    otherlist.append(n)

for i in somlist:
    for j in otherlist:
        newlist.append(j * i)
for a in newlist:
    if a == int(str(a)[::-1]):
        finallist.append(a)
    else:continue
finallist.sort()
print(len(finallist))
