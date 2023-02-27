import re
patt=r"[A-Z][a-z]+"
txt="Acccccssdd4FppppSs33Rsssss"
x=re.findall(patt, txt)
print(x)