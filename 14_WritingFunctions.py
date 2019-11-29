## Function definition
# global variable
totalCount = 0

def getSum(num1, num2=0):
    #global totalCount
#    globals()["totalCount"] = 12344

    totalCount = num1 + num2
    
    def innerFunction():
        # nonlocal totalCount
        totalCount = 100
        
        print("Value of totalCount in innerFunction: ", totalCount)
        
    # call inner function    
    innerFunction()

    print("Value of totalCount in function (after innerFunction call): ", totalCount)

    return totalCount


print("Value of totalCount before getSum function call: ", totalCount)

ret_count = getSum(345, 5)
print("Sum of 15 and 8 is: {} and global var is: {}".format(ret_count, totalCount))


## Higher order functions
def Enclosure(func):
    ret = func(10, 20)
    print("Return value from passed function call is: ", ret)

func_var = getSum
ret_count2 = func_var(12, 34)
print("Sum of 12 and 34 is: ", ret_count2)

# pass function variables to other functions
Enclosure(func_var)


# Note: if there is no explicit return statement in a function,
# it returns None (so make sure to return a value from a function



# If you pass a list to a function, you can modify the contents of it
# but if you assign a new list to it, original list will not be affected
main_lst = [1, 2, 3]

def ListScope(lst):
    lst[0]=4
    print("List contents after modification (inside function): ", lst)

    # will this statement have any effect?
    lst = [10, 20, 30, 40]


print("Initial value: ", main_lst)
ListScope(main_lst)
print("Value after modification: ", main_lst)



## Function with variable number of arguments
def sumNumbers(*args):
    s = 0

    for n in args:
        print("Type: ", type(n), n)
        if type(n) is list:
            for i in n:
                s += i
        if type(n) is int:
            s += n

    return s

l = [10, 20, 30, 456, 45, 13]
result = sumNumbers(l, 100)
print("Sum of numbers is: ", result)


# Function with keyword arguments
def printUserDetails(**kwargs):
    for k, v in kwargs.items():
        print(k, v)


printUserDetails(Scrip = "ACC", O = 1282, H = 1376, L = 1190, C = 1287)
printUserDetails(Name = "Ganesh", Age = 43)





## Lambda expressions

getSum = lambda num1, num2: print(num1 + num2)
s = getSum(12, 45)
print(s)

square = lambda num: num ** 2
print(square(3))

sum = lambda n1, n2: n1 + n2
print(sum(10, 23))

rev = lambda s: s[::-1]
print(rev('Hello'))

