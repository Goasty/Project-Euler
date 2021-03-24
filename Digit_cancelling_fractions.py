#https://projecteuler.net/problem=33
newlist = []
list_of_sets = []
for denom in range(10,100):
    d_s = denom
    for numer in range(10,denom):
            n_s = (numer)
        if numer % 10 == 0 and denom % 10 == 0:
            continue
            for n in n_s:
                if n in d_s:
                    n_s.pop(n)
                    d_s.pop(n)
                    n_s.join(n_s)
                    d_s.join(d_s)
                    if int(n_s)/int(d_s) == numer/denom:
                        newlist.append([numer,denom])
        #print('{} / {} == {}'.format(numer, denom, numer/denom)
        #print('{} / {} == {}'.format(n_s, d_s, n_s/d_s))
        #print(n_s,d_s)

    print(newlist)

#print(list_of_sets)
#for value in list_of_sets:
