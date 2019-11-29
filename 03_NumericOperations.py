# use split() function to split a string based on char(s)
# default split character is a space character
num1, num2 = input("Enter two numbers with a space ").split()

# Are num1 & num2 strings or numerals?
print("Type of num1 is {}".format(type(num1)))

# Can you perform arithmetic operations on strings?
print("Sum of two numbers is: {}".format(num1+num2))


# explicitly convert them to required type
num1 = float(num1)
num2 = float(num2)


# Perform the arithmetic operations
sum = num1 + num2

# +, - : addition, subtraction
# *, / : multiplication, division (true division in Python 3)
# %, ** : modulus, exponentiation
# // (integer division in Python 3)

#   Formatted output
print("{} + {} = {}".format(num1, num2, sum))

# perform other operations below and print output

