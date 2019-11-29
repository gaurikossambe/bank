# Usage of conditional operators
age = 19

if age >= 18:
    print("Go cast your vote!")
elif age >= 5:
    print("Underage! you can't vote.")
else:
    print("Toddler! keep home.")

if age >= 21:
    print("You can contest election.")


if age >= 18 and age < 21:
    print("Wait till 21 to contest election.")

# the above condition can be written using chained comparison operator
if 18 <= age < 21:
    print("Wait till 21 to contest election.")



num1, oper, num2 = input("Enter operation to perform ").split()

# convert input value to integer
# fails if input is a float value
num1 = int(num1)
num2 = int(num2)

# evalutate it to any numeric value based on input
# try with a float input value
num1 = eval(num1)
num2 = eval(num2)

#   Do the arithmetic operations based on operator
# +, -, *, /
if oper == "+":
    print("{} + {} = {}".format(num1, num2, num1+num2))
elif oper == "-":
    print("{} - {} = {}".format(num1, num2, num1 - num2))
elif oper == "*":
    print("{} * {} = {}".format(num1, num2, num1 * num2))
elif oper == "/":
    print("{} / {} = {}".format(num1, num2, num1 / num2))
else:
    print("Enter one of +, -, *, / operators")

