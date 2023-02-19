def ev(n):
    for i in range(n):
        if i%2==0:
            yield i

c=int(input())
ev1=ev(c)
print(type(ev1))
print(','.join(str(b) for b in ev1))