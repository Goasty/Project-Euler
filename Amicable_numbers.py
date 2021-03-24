#https://projecteuler.net/problem=21
def divisors(n):
    start = 1
    divisors = []
    while start < n:
        if n % start == 0:
            divisors.append(start)
        start += 1
    return(divisors)

def main():
    cap = 10000
    num = 1
    list_of_amicable_num = []
    while num < cap:
        list_of_divisors = divisors(num)
        sum_of_divisors_of_num = sum(list_of_divisors)
        list_of_divisors_of_new_num = divisors(sum_of_divisors_of_num)
        sum_of_divisors_of_new_num = sum(list_of_divisors_of_new_num)
        if sum_of_divisors_of_new_num == num and sum_of_divisors_of_num < cap and num < cap and num > sum_of_divisors_of_num:
            list_of_amicable_num.append(num)
            list_of_amicable_num.append(sum_of_divisors_of_num)
        num += 1
    print(list_of_amicable_num)
    print(sum(list_of_amicable_num))
main()
