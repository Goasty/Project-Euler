#https://projecteuler.net/problem=23
def divisors(n):
    start = 1
    divisors = []
    while start < n:
        if n % start == 0:
            divisors.append(start)
        start += 1
    return(sum(divisors))

def main():
    count = 1
    list_of_abundant_number = []
    while count < 28123:
        if divisors(count) >= count:
            list_of_abundant_number.append(count)
        count += 1
        #print(count)
    #print(list_of_abundant_number)
    number_list = []
    for i in range(1,28124):
        number_list.append(i)
        
    for Number in list_of_abundant_number:
        for NUmber in list_of_abundant_number:
            total = Number + NUmber
            #print(total)
            if total in number_list:
                number_list.remove(total)
    print(number_list)
    print(sum(number_list))
main()
