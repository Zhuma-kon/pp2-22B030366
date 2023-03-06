import os
print("write a full path to the file")

path=input()
if os.path.exists(path):
    if os.path.isfile(path):
        os.remove(path)
        print("file succesfully deleted")
    else:
        print("such file does not exist")
else:
    print("such file does not exist")