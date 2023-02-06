class shape:
    def __init__(self):
        pass
    def area(self):
        return 0
class rectangle(shape):
    def __init__(self, leng, width):
        self.len=leng
        self.wid=width

    def area(self):
        return self.len*self.wid

p1=rectangle(int(input()), int(input()))
print(p1.area())