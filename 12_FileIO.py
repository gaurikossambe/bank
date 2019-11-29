# open file handle for writing
# file open modes: r, w, a, r+, w+, a+

f = open("raw_strings.txt", "w")
f.write("First line here.\n")
f.write("and the second line\n")
str_list = ["Some more lines... \n", "This is a new line \n", "created from list of strings\n"]
f.writelines(str_list)
f.close()


# open file for reading
f = open("raw_strings.txt")
# read all the contents of the file into a variable
data = f.read()
for ch in data:
   print(ch)

# contents of the variable
print(data)

# does the readline function return any value?
# if not, why?
data_line = f.readline()
print(data_line, end="")

# open the file again for reading and then read
# every call to readline function returns one line at a time
f = open("raw_strings.txt")
data_line = f.readline()
print(data_line, end="")
data_line = f.readline()
print(data_line, end="")

# read a line at a time using for loop
for line in f:
    print(line, end="")

f.close()


# Writing lists
names_list = ["Manjula", "Prasad", "Ganesh"]
names_f = open("emp_data.txt", "w+")
names_f.write("Names list:\n")

# if you open the file in w+/a+ mode, you can read what you have written 
print("Cursor's current position: ", names_f.tell())
names_f.seek(0)
print(names_f.readline())

# list object is written as a string
names_f.write(str(names_list) + "\n")
count = len(names_list)
names_f.write(str(count))
names_f.close()


names_f = open("emp_data.txt")
emps = names_f.read()
print(emps)

print(type(emps))
names_f.close()


with open("dataFile.txt", mode="w+", encoding="utf-8") as writeFile:
    writeFile.write("This file is created through Python\n")
    writeFile.write("This is the second line of the header\nand the third line and so on...")

with open("dataFile.txt", encoding="utf-8") as readFile:
    print(readFile.readline())

    # reset read cursor and read whole file
    readFile.seek(0)
    print(readFile.read())


# check file attributes
print(readFile.closed)
print(readFile.mode)
print(readFile.name)
