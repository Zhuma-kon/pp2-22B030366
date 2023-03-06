def gector(st):
    return st==st[::-1]

st=input().strip()

if gector(st):
    print("Palindrome")
else:
    print("Not a palindrom")