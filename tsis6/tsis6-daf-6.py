import os
import string
path= r"C:\Users\ilias\OneDrive\Рабочий стол\hello"

for a in string.ascii_uppercase:
    fname=a+'.txt'
    b=0
    b=b+1
    with open(fname, mode='w') as f:
        f.write(f"{b}")