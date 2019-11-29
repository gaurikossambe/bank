import demoPack.testModule
import demoPack.drawings.myModule
# import demoPack.drawings.myModule as mm
# import demoPack.drawings.Scanner as sc
# from demoPack.drawings import Scanner, myModule
# from demoPack.drawings.myModule import testMod, Box
# from demoPack.drawings import *

# use dir() function to see list of modules loaded
dir()

demoPack.testModule.sampleFunction()

Scanner.testScanner()

b = myModule.Box(2, 3, 5)
print(b.displayBox())

myModule.testMod()

# you can call functions directly, if function names are imported
testMod()


# Use py_compile module to explicitly compile python modules
#import py_compile
#py_compile.compile('07_Looping.py')

