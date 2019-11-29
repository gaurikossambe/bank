sample_str = "  This is a python string object "

# search related functions
# count()	# number of occurrences of a substring
# index()   # index of substring; error if not found
# find()	# index of substring; -1 if not found
print("Character 'd' found ", sample_str.count("d"), " time(s)")
print("Index of first occurrence of chars 'st': ", sample_str.index("st"))

# will generate ValueError
print("Index of first occurrence of char 'd' using index(): ", sample_str.index("d"))
# not found, hence returns -1
print("Index of first occurrence of char 'd' using find(): ", sample_str.find("d"))


# to remove the white spaces
# these functions do not modify the original string
# lstrip(), rstrip(), strip()
print("-" + sample_str.lstrip() + "-")
# original string is not modified
print("-" + sample_str + "-")
# trim from both sides
print("-" + sample_str.strip() + "-")


# these functions do not modify the original string
# upper(), lower()
sample_str = sample_str.upper()     # assign the return value to modify the original object
print("-" + sample_str + "-")
print(sample_str.lower())

# remove spaces and convert to lower case letters
sample_str = sample_str.strip().lower()

# capitalize()		# first letter upper
sample_str = sample_str.capitalize()
print(sample_str)


# split(), join()
# create a list of tokens/words from a string based on split charater/word
words = sample_str.split(" ")
print(words)

# join list of strings using a glue character/string
print("-".join('ABC'))
print(" ".join(words))


sample_str = sample_str.replace("python", "anaconda")
print(sample_str)

# does sample_str contains a string 'conda'?
print("conda" in sample_str)


# replace()
# first two occurances of a are replaced with 'an'
print(sample_str.replace("a", "an", 2))

sample_str=sample_str.replace("New string", "", 2)

print(sample_str)
print(id(sample_str))

new_str = ". String concatenation will create a new string."
print(id(new_str))
sample_str = sample_str + new_str

# after concatenation, object id changes
print(id(sample_str))

# replace function returns a new string object (id changes)
sample_str = sample_str.replace("String", "This is a new string, and")
print(id(sample_str))
print(sample_str)

