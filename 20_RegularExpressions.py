'''
A digit: \d or [0-9]
Not a digit: \D or [^0-9]
A word: \w  or [a-zA-Z0-9_]
Not a word: \W  or [^a-zA-Z0-9_]
Boundary: \b
Not a boundary: \B
Occurrences:
 three digits: \d{3}
 three to six digits: \d{3,6}
Any space char: \s  or [\f\r\n\t\v]
Not a space: \S     or [^\f\r\n\t\v]

'''

'''
Backspace: \b
Form feed: \f
Carriage return: \r
Tab: \t
Vertical tab: \v
'''

'''
Multiples
One or more: +
zero or more: *
zero or one: ?

'''

'''
OR: use | between patterns/parts of pattern
'''


import re

line = "At TTS, we teach you how to perform data manipulation, " \
       "file processing and visualization using Python."


# checks for existence
found = re.search("\w+ing", line)
if found:
    print("String found")


# find all occurrences
allFinds = re.findall("\w+ing", line)
for s in allFinds:
    print(s)


# find all occurrences with their positions
allFinds = re.finditer("\w+ing", line)
for s in allFinds:
    posTuple = s.span()
    print(posTuple, ": ", line[posTuple[0]:posTuple[1]])


# ^ begins with, $ ends with
allFinds = re.findall(r"^\w*[Aa]\w*", line)
            # try with "\w*[Aa]\w*" (all words containing 'A' or 'a') and "\w*on\.$" (sentence ending with 'on')
for s in allFinds:
    print(s)
    

s = "This contains a backslash \\ char"
print(s)
p = r"\\"
print(re.search(p, s))


# Search and replacement
searchStr = "Employee    id of  Vikram is P350394   and he works in retail banking"

# two ways to pattern searching
# one using re.search function, which we used earlier
# second by compiling a search pattern and applying it on the string
pattern = re.compile("[A-Z]\d{3,6}")
m = pattern.search(searchStr)
print(m.span())


# substitute 
# replace all occurances of one or more spaces with one space
pattern = re.compile(" +")
# if number of occurances is set, those many matches will be replaced
# default is all occurances
searchStr = pattern.sub(" ", searchStr)
print(searchStr)


