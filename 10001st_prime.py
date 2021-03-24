#https://projecteuler.net/problem=7
def main():
    number_prime_to_find = 10001
    x = 2
    list_of_primes = []
    while(len(list_of_primes) < number_prime_to_find):
        if all(x % prime for prime in list_of_primes):
            list_of_primes.append(x)
        x += 1
    print(list_of_primes)
    print(list_of_primes[-1])
main()
