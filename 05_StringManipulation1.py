# index       0    5  8 10     17     24
sample_str = "This is a python string object"


print("No. of chars in the string is: ", len(sample_str))
print("First char of the string: ", sample_str[0])
print("Last char of the string: ", sample_str[-1])  # very useful

# string repetition operator
print("Hello " * 4)


# slice operator
# extract the word 'python' using string slice
print("Characters between index 10(included) and 16(excluded): '{}'".format(sample_str[10:16]))
# extract whole string
print(sample_str[:])
# start at -3 and end at -1 (not included)
print(sample_str[-3:-1])
# include the last character too
print(sample_str[-3:])


# Use step frequency value of slice operator 
print(sample_str[::1])  # step frequency of 1
print(sample_str[5::2])  # step of 2 chars, starting from index 5

# with a negative step value, start and end positions of the slice should be right to left
print(sample_str[::-1])     # reverse a string
# same as above
print(sample_str[29::-1])     # reverse a string

# 17th character to the beginning
print(sample_str[17::-2])     # reverse a string with 2 chars step


# unicode and char conversions
# using '+' operator on strings;
# both operands must be strings, will be converted, if not
print("Unicode value of 'A': " + str(ord('A')))
print("Char representing unicode 65 is: ", chr(65))


# use a string in for loop to access each char
for c in sample_str:
    print(c, ",", end="", sep=" ")
print("")


# string objects are immutable; cannot modify
# uncomment 2 statements below and execute; understand the error generated.
#sample_str[0] = "t"
#print(sample_str)


# isalnum()		# alpha numeric
print("alphanumeric: ", "P235".isalnum())

# isalpha()
print("alphabet: ", "h3".isalpha())

# isdigit()
print("digit: ", "357".isdigit())

# islower(), isupper()
print("uppercase letter: ", sample_str[0].isupper(), ", lowercase letter: ", "#".islower(), sep="")

# isspace()
print("space: ", "\t".isspace())

# Try it yourself
# print the third last character


# print the no of times char 'd' is found


# print the char found after 'y'

