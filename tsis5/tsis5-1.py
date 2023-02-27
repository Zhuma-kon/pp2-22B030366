import re 
pattern= r'ab*'
text=(input())
print(re.search(pattern, text))