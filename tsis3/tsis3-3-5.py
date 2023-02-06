class account:
    
    def __init__(self, owner, balance):
        self.o=owner
        self.b=balance
    def deposit(self):
        print("write down the number of money you wnat to deposite:")
        c=int(input())
        self.b+=c
        print(f"money was succesfully deposited, your balance is:{self.b}")
    def withdraw(self):
        print("write down the number of money you wnat to withdraw:")
        c=int(input())
        if c>self.b:
            print(f"You cannot withdraw more than you have in balance, try again.")
            print(f"Current balance is:{self.b}")
        else:
            print("Money successfully withdrawed")
            self.b-=c
            print(f"Current balance is:{self.b}")

print("write down the name of the owner and his balance")
p1=account(input(), int(input()))
while True:
    print("""Write down what function you need
1-deposit
2-withdraw
3-exit the function""")
    a=int(input())
    if a==1:
        p1.deposit()
    elif a==2:
        p1.withdraw()
    elif a==3:
        break
    else:
        print("There isn't such function, please try again")

