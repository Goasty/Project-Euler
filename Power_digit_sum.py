#https://projecteuler.net/problem=16

def main():
    iteration = []
    x = str(2 ** 1000)
    #print(x)
    for i in x:
        iteration.append(int(i))
    print(sum(iteration))
main()
