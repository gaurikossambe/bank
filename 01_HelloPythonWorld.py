# Enter your name when prompted
name = input("Enter your name ")  # this is inline comment text

# what type of variabe input function returns?
# print type of variable
print(type(name))

# Say hello
print("Hello", name, "!", sep=",")      # default is a space
print("Welcome to the world of Python.")


# Can you convert a string to integer?
int_value = int(name)
print("Integer value: ", int_value)
