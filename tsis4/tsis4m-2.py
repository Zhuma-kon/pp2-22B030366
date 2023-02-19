import math
def trap(h, a, b):
    c=h*(a+b)/2
    return c

print("input the height, first value, second value of trapezoid respectively")
h=int(input())
a=int(input())
b=int(input())
print(trap(h, a, b))