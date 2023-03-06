import os
path = r"C:\Users\ilias\OneDrive\Рабочий стол\hello\tssi3"

with open(path, "r") as f:

    b=0
    for s in f:
        b+=1
    b+=1
    print(b)