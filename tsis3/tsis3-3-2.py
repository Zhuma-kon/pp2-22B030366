class shape:
    def __init__(self):
        pass
    def area(self):
        return 0
class square(shape):
    def __init__(self, leng):
        self.len=leng

    def area(self):
        return self.len**2

p1=square(int(input()))
print(p1.area())