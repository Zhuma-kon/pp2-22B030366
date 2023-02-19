def sqr(a, b):
    for i in range(a, b):
        yield i**2

a=int(input())
b=int(input())
squares=sqr(a, b)
for i in squares:
    print(i)
