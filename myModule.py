def testMod():
    print("Module name: ", __name__)


class Box:
    design = "3D"

    def __init__(self, w, h, b):
        self.width = w
        self.height = h
        self.breadth = b

    def getVolume(self):
        # self.a = 100      # though it works, not a good thing
        return self.width * self.height * self.breadth

    def displayBox(self):
        return "Width: {}, Height: {}, Breadth: {}".format(
                                        self.width, self.height, self.breadth)
