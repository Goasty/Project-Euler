
import math
size_of_grid = int(input('enter square size'))
number_of_moves = size_of_grid * 2
a = math.factorial(size_of_grid)**2
b = math.factorial(number_of_moves)
#print(a)
#print(b)
print(int(b/a))
