#https://projecteuler.net/problem=28
def main():
    counter = 0
    gap_size = 1
    four_counter = 4
    total = 0
    for n in range(1, 1001**2 +1):
        if counter == 0:
            total += n
            counter = gap_size
            four_counter -= 1
        elif counter != 0:
            counter -= 1
        if four_counter == 0:
            gap_size += 2
            four_counter = 4
    print(total)
main()
