import random
def game(num):
    print("Take a guess")
    a=int(input())
    if a==num:
        print("Congrats!!")
    elif a<num:
        print("Your guess is too low.")
        game(num)
    else:
        print("Your guess is too high.")
        game(num)
        

num=random.randint(1, 20)
print("Hello what's your name?")
name=input()
print(f"Well {name} let's play game")
game(num)