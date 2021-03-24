#https://projecteuler.net/problem=32
#1,2,3,4,5,6,7,8,9
def pan_test(a,b):
    if len(str(a) + str(b) + str(a * b)) == 9 and set(str(a) + str(b) + str(a * b)) == set('123456789'):
        #print(set(str(a) + str(b) + str(a * b)))
        print(set('123456789'))
        viable_nums.add(a * b)
    else:
        return
viable_nums = set()
for a in range(1,10):
    for b in range(1000,10000):
        pan_test(a,b)
for a in range(10,100):
    for b in range(100,1000):
        pan_test(a,b)
print(viable_nums)
print(sum(viable_nums))
