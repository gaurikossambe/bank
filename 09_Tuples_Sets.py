# Tuples
empty_tuple = ()
emp_IDs = 'P873874', "E948573",  46, "P248723"
#emp_IDs = ('P873874', "E948573", 46, "P248723")      # both are fine

# print object types
print(type(empty_tuple))
print(type(emp_IDs))
print(type(emp_IDs[1]) is int)
print(emp_IDs)

# use tuple constructor to create a tuple of letters
# tuple constructor takes only one value
name_tuple = tuple("Ganesh Bhat")
print(type(name_tuple))
print(name_tuple)

# to create a tuple of one string value
names = "Ganesh Bhat",      # remove the comma at the end and see the type of object created
print(type(names))
print(names)


# a list
names_list = ["Ganesh", "Manoj", "Pallavi", "Ravi", "Vijay"]
print((type(names_list)))

# Can not modify a tuple
empty_tuple[0] = "Srividya"


print("Empty tuple:", empty_tuple)
print("tuple from a string:", name_tuple)

# create a tuple from a list
empty_tuple = tuple(names_list) + name_tuple
print(empty_tuple)

# print tuple contents
print("Contents of tuple created from list:")
for el in empty_tuple:
    print(el)

print("Contents of Emp_IDs tuple:")
print(emp_IDs)

print(emp_IDs.index("P248723"))
print(name_tuple.count('h'))
print(len(empty_tuple))
print(max(name_tuple))

# problems with different object types
# heterogeneous elements do not support comparison
print(min(emp_IDs))


all_entries = empty_tuple + emp_IDs
print(type(all_entries))
print(all_entries)


# unpacking tuple
v1, v2 = emp_IDs[0:2]
print(v1, " ", v2)

# if elements are not balanced on both sides
# tuple unpacking throws ValueError
v1, v2 = emp_IDs[0:3]
v1, v2, v3 = emp_IDs[0:2]



# tuple contains list as an element
new_tup = (names_list, "Kumar")
print(new_tup)

# can you modify the elements of the tuple?
new_tup[0] = ["Ramesh", "Maria"]

# can you modify the elements of the list, which is in a tuple?
new_tup[0].append("Maria")
print(new_tup[0])
# you are modifying the same list object
print(names_list)


# Sets
empty_set = set()
empty_set.add(234)
print(empty_set)

numbers = {25, 553, 863, 2, 634}
numbers.remove(863)     # raises LookupError if not found
numbers.discard(863)    # removes if found, no error if not found
print(numbers)

# duplicates will not be added to set
numbers.add(25)
print("Size: ", len(numbers))


emps = ["P12", "E34", "P17", "P12"]
emps_set = set(emps)

# search for exsistance of an element
print("P12" not in emps_set)

# Does not support indexing
print(numbers[1])
print(emps_set[0])

# convet a set to a list and use indexing
emp_list = list(emps_set)
print(emp_list[2])


odd_nums = [23, 553, 79, 91, 13, 7]

# add multiple elements (from a list/tuple/set) to a set
numbers.update(odd_nums)
print(numbers)

# remove the first element
print(numbers.pop())
# create a copy of the set
n1 = numbers.copy()
print(n1)

# empty the set
numbers.clear()
print(numbers)
