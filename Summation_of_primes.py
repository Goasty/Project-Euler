#https://projecteuler.net/problem=10

x = 2
list_of_primes = []
while x < 2000000:
    if all(x % prime for prime in list_of_primes):
        list_of_primes.append(x)
        print(x)
    x += 1

print(sum(list_of_primes))
                                                            
