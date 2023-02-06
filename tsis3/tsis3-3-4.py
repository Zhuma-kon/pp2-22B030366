import math
class point: #this class is the representation of an 2d coordinate system


    def __init__(self, x,y):
        self.x=x
        self.y=y
        #x and y are the coordinatees of the point
    def show(self):
        return self.x, self.y
    def move(self):
        print("insert new coordinates:")
        x1=int(input())
        y1=int(input())
        self.x=x1
        self.y=y1
    def dist(self):
        return math.sqrt(self.x**2+self.y**2)
print("insert the coordinates of the point")
A=point(int(input()), int(input()))
while True:
    print("""write the number between 1 to 3 inclusive to determine what function you want to use
or write 4 to end this program""")
    c=int(input())
    if c==1:
        print(A.show())
    elif c==2:
        A.move()
    elif c==3:
        print(A.dist())
    elif c==4:
        break
    else:
        print("there isn't such fucnction, try again")