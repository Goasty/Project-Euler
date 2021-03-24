c0 = int(input('enter value: '))
steps = 0
list_of_values =[]
while c0 != 1:
    if c0%2 == 0:
        c0 = c0 / 2
        steps += 1
    else:
        c0 = 3 * c0 + 1
        steps += 1
print(steps)        
