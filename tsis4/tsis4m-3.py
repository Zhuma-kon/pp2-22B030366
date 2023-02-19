import math
def area(a, b):
    c=(a* b**2)/(4 * math.tan(math.pi / a))
    return c

a=int(input())
b=int(input())
n=area(a, b)
print(n)