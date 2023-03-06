import math
import time
def sqrt_delay(n, ms):
    time.sleep(ms/1000)
    d=math.sqrt(n)
    return d

n=int(input())
ms=int(input())
print(sqrt_delay(n, ms))