tup=(True, True, True, True, False, False)
b=0
for i in tup:
    if i==False:
        b+=1
if all(tup):
    print("all True")
else:
    print(f"there is {b} imposter(s) among us")