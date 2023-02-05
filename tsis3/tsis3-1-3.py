def sol(heads, legs):
    chik=0
    rab=0
    if(heads>=legs):
        print("Incorrect input")
    elif(legs%2!=0):
        print("Incprrect input")
    else:
        rab=legs/2-heads
        chik=heads-rab
        print("Number of chiken:", chik)
        print("Number of rabbits:", rab)

head=int(input())
leg=int(input())
sol(head, leg)