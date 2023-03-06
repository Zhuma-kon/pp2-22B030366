import os

path = r"C:\Users\ilias\OneDrive\Рабочий стол\hello"
if os.path.exists(path):
    d, f = os.path.split(path)

    print(d)
    print(f)
else:
    print("path does not exist")