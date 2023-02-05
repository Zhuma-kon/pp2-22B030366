def is_prime(lis):
    c=0
    for x in lis:
        #print(x//2+2)
        c=0
        for i in range(x//2+1):
            if i==0 or i==1:
                pass
            elif x % i==0:
                c+=1
        if c==0:
            print(x)
            
        

lis=[1, 3, 5, 4, 8, 17]
is_prime(lis)