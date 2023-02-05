def histo(nums):
    for x in nums:
        for i in range(x):
            print('*', end='')
        print()

nums=[]
a=int(input())
for x in range(a):
    b=int(input())
    nums.append(b)
histo(nums)