def isprime(x):
    for divisor in range(2,x):
        if x%divisor == 0:
            return False

    return True

def factorise(x):
    primeFactors = []
    divisor = 2
    while x > 1:
        if isprime(divisor):
            if x % divisor == 0:
                x = x / divisor
                primeFactors.append(divisor)
            else:
                divisor += 1
        else:
            divisor += 1
    return primeFactors

factors = factorise(int(input('Give me a number')))
print(factors)
