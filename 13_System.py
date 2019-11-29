import sys, os, os.path, subprocess, glob

# file and directory level operations
os.rename("emp_data.txt", "newEmps.txt")
os.remove("dataFile.txt")
print(os.getcwd())
os.mkdir("subDir")
os.chdir("subDir")
print(os.getcwd())
os.chdir("..")
os.rmdir("subDir")


print(sys.platform)
print(sys.version)

os.rename("07_Lists.py", "07_Lists1.py")

# Check if file/path exists
print(os.path.exists("C:\\Users\\TrgDev\\PycharmProjects\\TrainingDemo\\BNP_Demos\\07_Lists1.py"))

# Path components of a file
names = os.path.split("C:\\Users\\TrgDev\\PycharmProjects\\TrainingDemo\\BNP_Demos\\07_Lists1.py")
print(names)


# Execute a sub process
subprocess.run("C:\\Windows\\System32\\Notepad.exe")


# File search
names = list(glob.glob('C:\\Windows\\System32\\*.exe'))
print(names)

