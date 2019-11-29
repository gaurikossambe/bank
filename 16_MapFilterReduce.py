###     Map

def square(num):
    return num ** 2

input_list = range(1, 11)

# arithmetics operations can't be performed directly on lists or range objects
print(list(input_list) * 2)   # performs list repetition but not multiplication
print(list(input_list) ** 2)  # can't perform

m1 = map(square, input_list)      # returns a map object
print(type(m1))
print(list(m1))

# pass lambda expressions in place of function
print(list(map((lambda x: x ** 2), input_list)))

# Similar to:
square_list = [x ** 2 for x in input_list]
print(square_list)

# Map using two input lists
input_list2 = range(11, 16)
print(list(map(lambda x, y: x+y, input_list, input_list2)))



###     Filter
def is_it_even(num):
    return num % 2 == 0

print(is_it_even(4))

print(list(filter(is_it_even, range(1, 11))))

# Similar to:
print(list(filter(lambda x: x % 2 == 0, range(1, 11))))
even_nums = [x for x in range(1, 11) if x % 2 == 0]
print(even_nums)



###     Reduce
from functools import reduce

input_list = range(1, 6)
print(reduce(lambda x, y: x+y, input_list))
