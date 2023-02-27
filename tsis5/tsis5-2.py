import re 
pattern= r'ab{3}|ab{2}'
text=(input())
x=re.search(pattern, text)
print(x)