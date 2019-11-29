NumList = [10, 3, 667]
AnyElement = ["Ganesh", "43", "Dec"]
intSeq = list(range(1, 10))
print(list(range(10)))

joined_List = NumList + intSeq
AnyElement.sort()
print(AnyElement)
print("Total elements in joined_List are: {}, they are:".format(len(joined_List)), joined_List)


# modify element
intSeq[2] = 111
print("Elements of intSeq after modification: ", intSeq)

# the '*' operator works as a repetition operator on strings
print("List repetion:")
print(NumList * 3)
print(AnyElement[0] * 3)

# the '*' operator works as a multiplication operator on numeric values
print("Value multiplication:")
print(NumList[1] * 3)


# lists once created are copies and do not refer to original lists
# observe that the contents are not modified due to intSeq modification
print("Total elements in joined_List are: {}, they are:".format(len(joined_List)), joined_List)


print("Index of 6 is: ", joined_List.index(6))
print("Value 7 appears", joined_List.count(7), "time(s)")   # how many occurrences


joined_List.append(23)
print("Elements in joined_List after append:", joined_List)

# insert
# non-existent index works like append()
AnyElement.insert(1, 12)
print("After element inserted:", AnyElement)


# Sorting
# use sorted() method to return sorted list; sorts any iterable
# original iterable is not modified
sorted_List = sorted(joined_List, reverse=True)
print("Elements in sorted_List after sorting:", sorted_List)
print("Elements in joined_List(original) after sorting:", joined_List)

# use list.sort() method to sort a list inplace 
# sorts elements of original list
joined_List.sort(reverse=True)
print("Elements in joined_List after sorting:", joined_List)

# Sorting heterogeneous lists results in TypeError
AnyElement.sort()
print(AnyElement)

# reverse the order of elements; modifies inplace
joined_List.reverse()
print("Elements in joined_List are reversed:", joined_List)

# remove
AnyElement.remove('43')
print("After element removed:", AnyElement)

# pop
print("Last element popped is:", AnyElement.pop())    # pops last element by default
print("Element at index 1 popped is:", AnyElement.pop(1))    # pops element at specified index

# empty the list
AnyElement.clear()
print(AnyElement)


# Two dimensional list OR lists within list
twoDList = [[1, 2, 3, 4], ['A', 'B', 'C'], 2, 5, 2]
print("\nFirst element of twoDList:", twoDList[0])
print("Value at index [1][2]:", twoDList[1][2])

print(twoDList[0].index(2))
print(twoDList.index(2))
print(twoDList.index(2, 3))

