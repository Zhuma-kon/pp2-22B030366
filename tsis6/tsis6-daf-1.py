import os

path = r"C:\Users\ilias\OneDrive\Рабочий стол\hello"
print(os.path.abspath(path))
print("1 for directories, 2 for files, 3 for both")
a= int(input())
if a ==1:
    for s in os.listdir(path):
        if os.path.isdir(os.path.join(path, s)):
            print(s)
elif a==2:
    for s in os.listdir(path):
        if os.path.isfile(os.path.join(path, s)):
            print(s)
elif a==3:
    for s in os.listdir(path):
        if os.path.isdir(os.path.join(path, s)):
            print("dir", s)
        elif os.path.isfile(os.path.join(path, s)):
            print("file", s)
else:
    print("follow the instructions")