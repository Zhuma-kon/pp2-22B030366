def michael(n):
    for i in range(12, n):
        if i % 3==0 and i % 4 ==0:
            yield i

c=int(input())
mike=michael(c)

print(", ".join(str(i) for i in mike))