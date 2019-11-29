# dictionary to store user information
# dictionaries use buckets to store information
userDetails = {"name": "Ganesh", "age": 43}
print(userDetails)

# add new entries
userDetails["loc"] = "Mumbai"

# empty dictionary declaration
userDetails = {}
# populate dictionary entries
for i in range(3):
    key = input("Enter parameter ")
    value = input("Enter value ")
    userDetails[key] = value

print(userDetails)


# user details used in the example below
userDetails = {"name": "Ganesh", "age": 43, "loc" : "Mumbai"}
print(userDetails)

# retrieve
print("User Name: ", userDetails["name"])

# entry will be updated or added based on whether key exists or not
# update
userDetails["location"] = "Thane"

# add new entry (key-value pair)
userDetails["phone"] = "9869484858"

print(userDetails)


# get all keys
# Value can be found out by entering the key..but vice versa is not possible
# i.e. Value does not know which key is holding it..but key knows which value it holds
print(type(userDetails.items()))
print(userDetails.keys)
for k in userDetails.keys():
    print(k, ": ", userDetails[k])

# get all values
print(userDetails.values())



# check for existence
print("loc as key exists:", "loc" in userDetails)
print("address as key exists:", "address" in userDetails)


# iterate through all key-value pairs
for key, value in userDetails.items():
    print("{}: {}".format(key, value))


# returns the value. If not found, returns message
print(userDetails.get("contact", "Contact doesn't exists. Check if its stored as phone"))


# remove key-value pair
del userDetails["phone"]
print("phone entry deleted.")

print(userDetails)

# returns keys by default
print("Contents of userDetails")
for user in userDetails:
    print("{}- {}".format(user, userDetails[user]))


# clears the dictionary
userDetails.clear()
print("Contents of userDetails after clear")
for user in userDetails:
    print(user)

