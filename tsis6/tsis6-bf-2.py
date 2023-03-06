st=input().strip()
b=0
c=0
for s in st:
    if s>='A' and s<='Z':
        b+=1
    elif s>='a' and s<='z':
        c+=1
print("num of uppercase:", b, "\nnum of lowercase:", c)
