def prime(lis):
    if lis<2:
        return False
    else:
        for x in range(2, lis):
            if lis % x == 0:
                return False
        return True

lis=[1, 2, 3, 4, 5, 6, 7, 8, 9, 17]
lis=list(filter(lambda x: prime(x), lis))
print(lis)
