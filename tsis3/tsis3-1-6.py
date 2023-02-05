def rev(st):
    lis=st.split()
    c=0
    for i in lis:
        print(lis[-1-c], end=" ")
        c+=1
st=input()
rev(st)