def min(n):
    while n>=0:
        yield n
        n -=1

n=int(input())
gen=min(n)
for i in gen:
    print(i)