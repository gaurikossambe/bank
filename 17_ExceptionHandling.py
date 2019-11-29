i, j = 10, 0
div = 0

def exceptTest(p, q):
    try:
        div = p / q
        print("Result: ", div)
    except ZeroDivisionError as ze:
        print(str(ze))

    except:
        print("Generic exception")

    finally:
        q = 1

    return p, q


i, j = exceptTest(i, j)

print("i={}, j={}".format(i,j))



class MyValueError(ValueError):
    def __init__(self, msg, minCap):
        super().__init__(msg)
        self.minimum = minCap


def setVehicleCapacity(cap):
    if (capacity <= 100):
        raise MyValueError('Capacity error!', 100)
    else:
        print("Vehicle capacity set to:", cap)
    
# Raising exceptions
capacity = int(input("Enter vehicle capacity "))
try:
    setVehicleCapacity(capacity)
except MyValueError as err:
    print(str(err), "Minimum required: ", err.minimum)
