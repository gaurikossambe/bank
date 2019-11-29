import sys
import numbers


'''
Here is an example of multi-line comment.
The following print function uses sys module to
format and display python version information
'''

# generate formatted output in Python 3
print("{} on {}".format(sys.version, sys.version_info))


# Find the type of variables
# print integer variable type
v1 = 10
print("type of v1: ", type(v1))
v2 = 3.493682
print("type of v2: ", type(v2))
s = "Variable types in Python"
print("type of s: ", type(s))


# write code blocks in Python using indentation
# Is variable v2 a subclass of Number type?
if issubclass(type(v2), numbers.Number):
    print("\tThis is part of if block.")
    print("\tYou can write any number of lines of code as part of a block")
    print("\tby ensuring they are properly indented.")
    # all lines of the block are aligned together


# following lines are part of the outer block
# crete a boolean variable
v3 = True
# generate formated output by supplying multiple arguments to print function
print("type of v3: ", type(v3), "and its value is: ", v3)

# or use format function of str
# specify position of variables in {} to refer to a specific variable
print("Value of variable 3 is: {2} and variable 1 is: {0}".format(v1, v2, v3))
# unused parameters in format are ignored

# you can split the strings to better manage formatting, if needed
print("Value of variable 3 is: {}".format(v3), "and variable 2 is: {}".format(v2))

b = None    # create a variable as a placeholder but won't have any value


# Rounding of digits of a floating point value
print("Variable v2 rounded off to two decimal places: {}".format(round(v2, 2)))


# variable values are copied at the time of assignment
name1 = "Pallavi"
name2 = "Raju"
name3 = 3543
name3 = name2
name2 = name1

print(name1)
print(name2)
# name3 retains the value 'Raju' even after name2 gets a new value later
print(name3)
