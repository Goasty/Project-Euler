#https://projecteuler.net/problem=24
from itertools import permutations
vals = list(permutations('0123456789'))
vals =["".join(x) for x in vals]
vals = list(map(int,vals))
final = sorted(vals)
final[:10]
print(final[999999])
