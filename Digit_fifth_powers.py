#https://projecteuler.net/problem=30
cap = 355000
list_of_5ths = []
for number in range(2, cap):
    str_number = str(number)
    total = 0
    for digit in str_number:
        total += int(digit)**5
    if total == number:
        list_of_5ths.append(number)
print(sum(list_of_5ths))
