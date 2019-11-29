# create a List of employees 
# each employee information is in a dictionary
emp_List = []

for i in range(2):
    emp = {}          # create a new dictionary object in every iteration
    k, v = input('Employee Name, SID').split()
    emp['name'] = k
    emp['sid'] = v
    emp_List.append(emp)

print(emp_List)


# Stock prices as a dictionary
# value contains a list of OHLC prices
Stocks = {"ACC" : [1234, 1373, 1190, 1267], "RIL" : [934, 973, 890, 967]}
print(Stocks["RIL"])    # value is the whole list
print(Stocks["ACC"][1]) # access element from the list

# stock prices stored as a list of dictionaries
# each element of the list is a dictionary
Stocks = [{"Scrip" : "ACC", "O" : 1234, "H" : 1373, "L" : 1190, "C" : 1267},
            {"Scrip" : "RIL", "O" : 934, "H" : 973, "L" : 890, "C" : 967}]
print(Stocks[1]) # second element of the list
print(Stocks[0]["H"]) # day high price of ACC


# Adding a list into dictionary
addr = ["B-16/63", "GB Road", "Thane", 400615]
userDetails = {"name": "Ganesh", "age": 43, "loc": "Mumbai"}

# Add the list as a value
userDetails["address"] = addr

# print dictionary contents
for user in userDetails:
    print("{}- {}".format(user, userDetails[user]))
print()


# List containing dictionaries
all_Users = [userDetails,
             {"name": "Rajesh", "age": 51, "loc": "Mumbai", "phone": 9987024839,
              "address":["204, Shiv Shakti CHS", "Datta Mandir Rd", "Santacruz", 400071]}]
# print the contents of the list
print("List of users:")
for user in all_Users:
    print(user)


# Dictionary comprehensions
names = ["Ganesh", "Bharat", "Pallavi", "Seema"]
name_len = {len(n): n for n in names}
