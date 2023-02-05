def palin(st):
    a=0
    for x in st:
        if x!=st[-1-a]:
            return False
        a+=1
    return True
st=input()

if palin(st)==True:
    print("Palindrome!")
else:
    print ("Not palindrome... :(")
