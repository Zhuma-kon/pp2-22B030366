import re
patt=r"[A-Z][a-z]*"
string="DoItAsITold"
x=re.findall(patt, string)
print(x)