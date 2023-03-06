import os
path1="source.txt"
path2="dest.txt"
with open(path1, 'r') as f:
    a=f.read()
with open(path2, 'w') as f1:
    f1.write(a)
