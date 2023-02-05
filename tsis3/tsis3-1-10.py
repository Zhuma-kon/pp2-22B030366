def uni(lis):
    lisc=[]
    c=0
    for i in lis:
        c=0
        for x in lisc:
            if i==x:
                c=1
        if c==0:
            lisc.append(i)
    print(lisc)

lis=[1, 2, 3, 1, 3, 5]
uni(lis)
            
