#https://projecteuler.net/problem=25
def main():
    li = []
    fib_list = [1,1]
    count = 2
    while (len(str(fib_list[-1])) < 1000):
        fib_list.append(fib_list[-1] + fib_list[-2])
        count += 1
    print(count)
main()
