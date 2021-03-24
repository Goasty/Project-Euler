#https://projecteuler.net/problem=6

sqs = []
ssq = []
a = []
r = range(1,101)

for ss in r:
    ssq.append(ss**2)
    sqs.append(ss)
print(sum(ssq))
print((sum(sqs))**2)
print((sum(sqs))**2-sum(ssq))
