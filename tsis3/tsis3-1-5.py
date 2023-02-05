def perm(lis, i, leng):
    if i==leng:
        print("".join(lis))
    else:
        for j in range(i, leng):
            lis[i], lis[j] = lis[j], lis[i]
            perm(lis, i+1, leng)
            lis[i], lis[j] =lis[j], lis[i]

d=input()
n=len(d)
lis=list(d)
perm(lis, 0, n)