# using Range objects
# Range parameters: start(inclusive), end(exclusive), step value
# observe '0' will not be printed
for i in range(10, 0, -1):
    if i == 14:
        break
    elif i == 9:
        continue
    print(i)
# else block executes if loop terminates normally
# will not execute if exited due to break statement
else:
    print("Executes if loop terminates normally")

print("Loop ended")


# Examples of Ranges
for n in range(10):
    print(n, " ", end="")
print()

for c in "Hello":
    print(c, " ", end="")
print()


# print first 5 numbers that are multiple of 7
print("First few numbers that are multiples")
num = 7
how_many = 5
# range with a step
for n in range(num, num * how_many + 1, num):
    print(n)



# Check if a number is prime
print("Check if a number is prime")
num = 23
for n in range(2, num//2+1):
    if num % n == 0:
        print(num, "is not a prime!")
        break
else:       # executes if loop terminates normally
    print(num, "is prime number!")


# print odd numbers less than 20. Terminate loop if number is 15.
print("\nWhile loop...")
i = 1
while i <= 20:
    if (i % 2) == 0:
        i += 1
        continue

    if i == 15:
        break
    else:
        print("Odd number is: ", i)

    i += 1
else:
    print("normal exit")
