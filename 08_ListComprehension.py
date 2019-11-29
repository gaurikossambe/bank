import math

# List comprehensions
# create a list of characters from a string
l = [letter for letter in 'This is character list']
print(l)

# create a list of elements using expression
evenList = [i*2 for i in range(10)]
print(evenList)

# Extract only even numbers from a list using list comprehension
nums = [23, 456, 56, 213, 5, 24, 82, 983, 34]
even_nums = [number for number in nums if number % 2 == 0]
print("Even numbers extracted:", even_nums)


# square of numbers
l = [num ** 2 for num in range(11)]
print("Squares:", l)


# generate even numbers
evenList = [i*2 for i in range(10)]
print("Even numbers generated: ", end="")
for val in evenList:
    print(val, " ", end="")
print()


# nested list comprehensions
l = [n * 2 for n in [num ** 2 for num in range(11)]]
print("Double of squares:", l)
print()


# list of odd numbers
oddList = [x for x in range(1, 21) if x % 2 != 0]
print(oddList)


# List repetition operator
lst = [1, 2] * 3
print("\nList repetition:", lst)


# Two dimensional lists
# create 4x3 array
twoDimList = [[int(math.pow(x, 2)), int(math.pow(x, 3)), int(math.pow(x, 4))]
              for x in range(1, 5)]
print(twoDimList)
#for val in twoDimList:
#    print(val)


# create an asymetrical array like list
twoDimList = [[int(math.pow(x, 2)) for x in range(1, 5)], 
               [int(math.pow(x, 3)) for x in range(1, 10)], 
               [int(math.pow(x, 4)) for x in range(10, 15)]]
for val in twoDimList:
    print(val)


# A two dimensional (5 rows and 4 columns) list
twoDimList = [[i] * 4 for i in range(5)]
# All elements in a row will have same value as that of i
print("Value at [4][3]:", twoDimList[4][3])
print("Contents of twoDimList:")
print(twoDimList)


print("\nRows and columns arrangement in two dimensional list")
# populate contents
for i in range(5):
    for j in range(4):
        twoDimList[i][j] = "{}-{}".format(i, j)
# print contents
for i in range(5):
    for j in range(4):
        print(twoDimList[i][j], end=", ")
    print()

