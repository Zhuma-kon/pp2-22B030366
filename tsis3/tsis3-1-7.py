def pair_3(listc):
    c=0
    for x in listc:
        if x==3:
            c+=1
        else:
            c=0
        if c==2:
            return True
    return False

a=int(input())
listc=[]
for x in range(a):
    b=int(input())
    listc.append(b)

ans= pair_3(listc)
print(ans)