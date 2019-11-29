class Box:
    totalBoxes = 0

    def __init__(self, w, h, b):
        self.width = w
        self.height = h
        self.breadth = b
        self.__setWarning = True       # private variable
        Box.totalBoxes += 1

    def getVolume(self):
        return self.width * self.height * self.breadth

    def displayBox(self):
        return "Width: {}, Height: {}, Breadth: {}".format(
                                        self.width, self.height, self.breadth)

    def setBoxFeatures(self, *args):
        if len(args) == 1:
            self.width = args[0]
        elif len(args) == 2:
            self.width, self.height = args[0:2]
        else:
            self.width, self.height, self.breadth = args[0:3]

    # access private member
    def showWarningStatus(self):
        print("Warning set to:", self.__setWarning)
        
    # private method
    def __privateMethod(self):
        print("In private method")

# Inheritance
class MetalBox(Box):
    def __init__(self, w, h, b, mat):
        super().__init__(w, h, b)
        self.material = mat

    def displayBox(self):
        return "Width: {}, Height: {}, Breadth: {}, Material: {}".format(
                                        self.width, self.height, self.breadth, self.material)


b1 = Box(10, 2, 3)
print("Box volume:", b1.getVolume())
b1.setBoxFeatures(20)
print("Box volume:", b1.getVolume())
print("Box features:", b1.displayBox())
print("Box features:", Box.displayBox(b1))
print("Total number of boxes created: ", Box.totalBoxes)

# can not access private member
print(b1.__setWarning)
b1.__privateMethod()

# access private member through public method
b1.showWarningStatus()


mb1 = MetalBox(w=12, h=3, b=34, mat="Copper")
# or just pass values in the required order
mb1 = MetalBox(12, 3, 34, "Copper")

print("Box volume:", mb1.getVolume())
mb1.setBoxFeatures(20)
print("Box volume:", mb1.getVolume())
print("Total number of boxes created: ", Box.totalBoxes)

# dynamic polymorphism
print("Box features:", mb1.displayBox())

