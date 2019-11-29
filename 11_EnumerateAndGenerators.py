###     Enumerate
months = ["Apr", "May", "Jun", "Jul",
          "Aug", "Sep", "Oct", "Nov", "Dec", "Jan", "Feb", "Mar"]

# default start value is zero
for (m_no, mon) in enumerate(months):
    print(m_no, mon)

for (m_no, mon) in enumerate(months, start=1):
   print(m_no, mon)



###     Generators
print(int(10e+300))
a = range(int(10e+300))


# List creates all the values at once
# DO NOT EXECUTE THE FOLLOWING LINE IN SPYDER; you can try in command prompt
#i = [x for x in range(int(10e+300))]
#print(i[0])


# Generators doesn't create whole list, instead generates one value for each call
# Generator comprehensions
even_numbers = (x * 2 for x in range(10))
print(next(even_numbers))
print(next(even_numbers))

# two values are already consumed hence following code throws StopIteration exception
for i in range(10):
    print(next(even_numbers))

# new generator object
even_numbers = (x * 2 for x in range(7))
print(next(even_numbers))
print(next(even_numbers))

# generator objects can be assigned to other variables
gen_variable = even_numbers
# both variables pointing to one object
print(next(gen_variable))
print(next(even_numbers))

for i in gen_variable:
    print(i)


# syntax looks like a tuple but its a generator
# use explicit typecast to tuple to make it a tuple
t = (x for x in range(10))
print(type(t))
# if its a generator, get next value using next()
print(t)


# generator function
def cube_gen(num):
    for n in range(1, num+1):
        yield n**3

# create generator object using generator function
cube_obj = cube_gen(10)
print(next(cube_obj))
print(next(cube_obj))

# is this a new object?
cube_obj2 = cube_gen(10)
for value in cube_obj2:
    print(value)

# generator object to variable assignment
# are there two objects? will they retain their values?
cube_obj2 = cube_obj
print(next(cube_obj2))
print(next(cube_obj))


# In Python 3, range function is like generator
#x = range(1, 11)
#for n in x:
#   print(n)
