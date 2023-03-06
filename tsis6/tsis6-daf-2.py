import os

path = r"C:\Users\ilias\OneDrive\Рабочий стол\hello"

if os.path.exists(path):
    if os.access(path, os.R_OK):
        print("you can read it")
    else:
        print("you can't read it")
    if os.access(path, os.W_OK):
        print("you can write into it")
    else:
        print("you can't write into it")
    if os.access(path, os.X_OK):
        print("you can execute it")
    else:
        print("you can't execute it")
else:
    print("file you are looking for does not exists, therefore it is not R,W,x")