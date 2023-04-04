import pygame
from random import randint
import time
pygame.init()
# preparing the code by writing 'sample'
WIDTH = 600
HEIGHT = 600
block=30 #making this block so it will be easier to measure distance

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

clock = pygame.time.Clock()
fps_sp=5 #fps, we will change it later, so i made another object to work with it

font=pygame.font.SysFont('arial', 36)
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('snek game')
#making class point so it will be easier to determine the coordinates
class point(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.x=x
        self.y=y
        self.rect = pygame.Rect(self.x * block, self.y * block, block, block)

#making classes snake and food and all of methods we will need
class snake(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.body = [point(x = WIDTH // block // 2, y = HEIGHT // block // 2)]
    #method to draw the snake, head is red and ither body parts are blue
    def draw(self):
        head = self.body[0]
        pygame.draw.rect(screen, RED, pygame.Rect(head.x*block, head.y*block,
                                                  block, block))
        for body in self.body[1:]:
            pygame.draw.rect(screen, BLUE, pygame.Rect(body.x*block, body.y*block, 
                                                       block, block))
    #method to move snake, we move its head and then give its previos coordinates for other body parts, and so on
    def move(self, dx, dy):
        for id in range(len(self.body)-1, 0, -1):
            self.body[id].x = self.body[id-1].x
            self.body[id].y = self.body[id-1].y
        self.body[0].x += dx
        self.body[0].y += dy

    #because snake does not have rectangle in its properties i made a function to check its collision with food, it works only when their centers are in one coordinate. but it is not a problem for us
    def check_collision(self, food):
        if food.point.x != self.body[0].x:
            return False
        if food.point.y != self.body[0].y:
            return False
        return True
     
    def check_collision_body(self): #i couldn't check the collision with just check_collision, so i made another function 
        for body in self.body[2:]:
            if self.body[0].x == body.x and self.body[0].y ==body.y:
                return True
        return False

class food(pygame.sprite.Sprite):
    def __init__(self, x, y):
        self.point = point(x, y)

    def draw(self):
        pygame.draw.rect(screen, YELLOW, pygame.Rect(self.point.x * block, self.point.y * block,
                                                     block, block))


done = False
snek=snake() #snek, a object of class snake
fud = food(randint(0, WIDTH // block - 1), randint(0,  HEIGHT // block -1)) #fud, the object of class food
dx=0
dy=0
score=0
count_sp=0
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            # a part of the code to move the snek
                if event.key == pygame.K_UP and dy != 1: #all the second conditions are needed to not allow snake go into itself
                    dx, dy = 0, -1
                elif event.key == pygame.K_DOWN and dy != -1:
                    dx, dy = 0, 1
                elif event.key == pygame.K_RIGHT and dx != -1:
                    dx, dy = 1, 0
                elif event.key == pygame.K_LEFT and dx != 1:
                    dx, dy = -1, 0
    screen.fill(BLACK)
    snek.draw()
    snek.move(dx, dy)
    fud.draw()
    if snek.body[0].x > (WIDTH // block - 1):
        snek.body[0].x = 0

    elif snek.body[0].x < 0:
        snek.body[0].x = (WIDTH //block - 1)

    elif snek.body[0].y < 0:
        snek.body[0].y = (HEIGHT //block - 1)

    elif snek.body[0].y > (HEIGHT//block - 1) :
        snek.body[0].y = 0

    if snek.check_collision(fud):
        snek.body.append(point(snek.body[-1].x, snek.body[-1].y))

        fud.point.x = randint(0, WIDTH // block - 1)
        fud.point.y = randint(0, HEIGHT // block - 1)
        score+=1
        if score % 3 == 0:
            fps_sp += 1
            count_sp += 1
        
    
    if snek.check_collision_body(): #death condition
        screen.fill(RED)
        time.sleep(2)
        done=True

    text_sc = font.render(f'Score:{score}', True, WHITE)
    text_sp = font.render(f'Level:{count_sp}', True, WHITE)
    screen.blit(text_sc, (0, 10))
    screen.blit(text_sp, (0, 40))
    
    pygame.display.flip()
    clock.tick(fps_sp)