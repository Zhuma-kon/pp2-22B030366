import pygame
from random import randint
import time
pygame.init()
# preparing the code by writing 'sample'
WIDTH = 600
HEIGHT = 600
block=30 #making this block so it will be easier to measure distance


music = r'C:\Users\ilias\OneDrive\Рабочий стол\hello\tsis7\MUSIC_PYGAME\Driftveil City.mp3'
grow = r'C:\Users\ilias\OneDrive\Рабочий стол\hello\tsis7\MUSIC_PYGAME\Mario Coin Sound - Sound Effect.mp3'
shrink = r'C:\Users\ilias\OneDrive\Рабочий стол\hello\tsis7\MUSIC_PYGAME\smb3_bump.wav'

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
PURPLE = (230, 230, 250)

clock = pygame.time.Clock()
fps_sp=5 #fps, we will change it later, so i made another object to work with it

font=pygame.font.SysFont('arial', 36)
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('snek game 2.0')
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
        self.body = [point(x = WIDTH // block // 2, y = HEIGHT // block // 2), point(x = WIDTH // block // 2, y = HEIGHT // block // 2)]
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

class poison(pygame.sprite.Sprite):
    def __init__(self, x, y):
        self.point = point(x, y)

    def draw(self):
        pygame.draw.rect(screen, PURPLE, pygame.Rect(self.point.x * block, self.point.y * block,
                                                     block, block))
class super_food(pygame.sprite.Sprite): #creating new food class with slightly different method and properties 
    def __init__(self, x, y, time):
        self.point = point(x, y)
        self.timer = time

    def draw(self, end_time):
        remaining_time = int(end_time - time.time())
        text1 = font.render(f'{remaining_time}', True, BLACK)
        if remaining_time <= 0:  # modify the condition to check if remaining_time is less than or equal to 0
            global check 
            check = 0
        pygame.draw.rect(screen, RED, pygame.Rect(self.point.x * block, self.point.y * block,
                                                 block, block))

        screen.blit(text1, pygame.Rect(self.point.x * block, self.point.y * block,
                                        block, block))



done = False
snek=snake() #snek, a object of class snake
fud = food(randint(0, WIDTH // block - 1), randint(0,  HEIGHT // block -1)) #fud, the object of class food
poi = poison(randint(0, WIDTH // block - 1), randint(0, HEIGHT // block -1)) #poi the object of class poison
s_fud = super_food(randint(0, WIDTH // block - 1), randint(0,  HEIGHT // block -1), 7)#s_fud, object of the class super_food
dx=0 # dx, dy with them i move snek 
dy=0
score=0 #the main score
score_check = 0 # score that is needed to raise the games speed
count_sp=0 #speed counter with it show the level of the game
check = 0
#music section
pygame.mixer.music.load(music) 
pygame.mixer.music.play(-1)
poisoned = pygame.mixer.Sound(shrink)
eat = pygame.mixer.Sound(grow)

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            # a part of the code to move the snek
                if event.key == pygame.K_UP and dy != 1: #all  of the second conditions are needed to not allow snake go into itself
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
    poi.draw()
    
    if randint(0, 50) == 1 and check == 0: #creating new s_fud randomly so there won't be any errors with timer
        check = 1
        start_time = time.time()
        seconds = 7
        end_time = start_time + seconds
        xy_new = (randint(0, WIDTH // block - 1), randint(0, WIDTH // block - 1))
        if xy_new not in snek.body: #this if makes sure that new s_fud coordinates are not in snek's body
            s_fud = super_food(xy_new, 7)
    if check == 1: # this is for making sure that s_fud won't appear twice
        s_fud.draw(end_time)
    
    #section that handles the snek going thourgh the edges of map
    if snek.body[0].x > (WIDTH // block - 1):
        snek.body[0].x = 0

    elif snek.body[0].x < 0:
        snek.body[0].x = (WIDTH //block - 1)

    elif snek.body[0].y < 0:
        snek.body[0].y = (HEIGHT //block - 1)

    elif snek.body[0].y > (HEIGHT//block - 1) :
        snek.body[0].y = 0

    #section that handles all of the collisions
    if snek.check_collision(fud):
        snek.body.append(point(snek.body[-1].x, snek.body[-1].y))

        pygame.mixer.music.pause()
        eat.play()
    
        x_new = randint(0, WIDTH // block - 1)
        y_new = randint(0, HEIGHT // block - 1)
        if (x_new, y_new) not in snek.body: #this is for c=making sure that fud won't appear in snek
            fud.point.x = x_new
            fud.point.y = y_new
        score+=1
        score_check +=1
        if score_check >= 3:
            fps_sp += 1
            count_sp += 1
            score_check = 0
        pygame.mixer.music.unpause()
        
    if snek.check_collision(s_fud): #no much difference from collision with fud, only some numbers are diffrent, and no making coordinates, cause we did earlier
        snek.body.append(point(snek.body[-1].x, snek.body[-1].y))
        pygame.mixer.music.pause()
        eat.play()
        score+=1
        score_check +=1
        check = 0
        if score_check >= 3:
            fps_sp += 1
            count_sp += 1
            score_check = 0
        pygame.mixer.music.unpause()
        
    if snek.check_collision_body(): #death condition
        screen.fill(RED)
        pygame.display.flip()
        time.sleep(2)
        done=True
    
    if snek.check_collision(poi):
        snek.body.pop()
        pygame.mixer.music.pause()
        poisoned.play()
        
        poi.point.x = randint(0, WIDTH // block - 1)
        poi.point.y = randint(0, HEIGHT // block - 1)
        score-=1
        if int(len(snek.body)) == 0:
            screen.fill(RED)
            pygame.display.flip()
            time.sleep(2)
            done=True
        pygame.mixer.music.unpause()
        

    #section for rendering the text on the screen 
    text_sc = font.render(f'Score:{score}', True, WHITE)
    text_sp = font.render(f'Level:{count_sp}', True, WHITE)
    screen.blit(text_sc, (0, 10))
    screen.blit(text_sp, (0, 40))
    #screen updator
    pygame.display.flip()
    clock.tick(fps_sp)