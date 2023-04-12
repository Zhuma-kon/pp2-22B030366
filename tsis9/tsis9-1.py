import pygame
import sys
from pygame import * 
import random, time
#preparing code by writing common things
pygame.init()

WIDTH=500
HEIGHT=500
sp=60
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Game 2.0')

BLACK=(0, 0, 0)
WHITE=(255, 255, 255)
BLUE=(0, 0, 255)
RED=(255, 0, 0)
YELLOW=(255, 255, 0)
SILVER=(192, 192, 192)
GOLDEN=(153, 101, 21)
done=False
clock=pygame.time.Clock()
font=pygame.font.SysFont('arial', 36)

#creating classes
class player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.rect=pygame.Rect(60, 60, 55, 55)
        self.rect.center=(250, 400)
    
    def move(self):
        pressed=pygame.key.get_pressed()
        if self.rect.left>=0: 
            if pressed[K_LEFT]:
                self.rect.move_ip(-5, 0)
        if self.rect.right<WIDTH :
            if pressed[K_RIGHT]:
                self.rect.move_ip(5, 0)
                
    def draw(self, surface):
        lil_s=pygame.Surface((60, 60))
        pygame.draw.rect(lil_s, WHITE, pygame.Rect(20, 20, 20, 20))
        # s.fill()
        surface.blit(lil_s, self.rect)


class enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # pygame.draw.rect(screen, RED, pygame.get_rect(x, y, 60, 60))
        self.rect = pygame.Rect(55, 55, 55, 55)
        self.rect.center=(random.randint(40, WIDTH-40), 0)
    def move(self):
        self.rect.move_ip(0, 7)
        if self.rect.bottom>HEIGHT:
            self.rect.top = 0
            self.rect.center=(random.randint(30, 470), 0)
        
    def draw(self, surface):
        lil_s=pygame.Surface((60, 60))
        lil_s.fill(RED)
        # pygame.draw.rect(screen, RED,  self.rect)
        surface.blit(lil_s, self.rect)

class money(pygame.sprite.Sprite):
    def __init__(self, nom):
        super().__init__()
        self.nominal = nom
        self.rect = pygame.Rect(20, 20, 20, 20)
        self.rect.center=(random.randint(30, 470), 0)

    def move(self):
        self.rect.move_ip(0, 10)
        if self.rect.bottom>HEIGHT and self.nominal !=3 and self.nominal !=5:
            self.rect.top = 0
            self.rect.center=(random.randint(30, 470), 0)
        
    def draw(self, surface):
        colour = YELLOW
        if self.nominal == 3:
            colour = SILVER
        if self.nominal == 5:
            colour = GOLDEN
        lil_s=pygame.Surface((20, 20))
        lil_s.fill(colour)
        # pygame.draw.rect(screen, RED,  self.rect)
        surface.blit(lil_s, self.rect)
def Mn_appear(Mn, E1) :
        Mn.rect.top = 0 
        (x, y)=E1.rect.center
        x1=random.randint(30, 470)
        if x1!=x:
            M3.rect.center=(x1, 0)
#making an abject of classes made before, also grouping them in groups
P1=player()
E1=enemy()
M1=money(1)
M3=money(3)
M5=money(5)

enemies=pygame.sprite.Group()
enemies.add(E1)
b_account=pygame.sprite.Group()
b_account.add(M1)
b_account.add(M3)
b_account.add(M5)
all_sprites=pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)
all_sprites.add(M1)
all_sprites.add(M3)
all_sprites.add(M5)
num_m=0
spawn_coin = pygame.USEREVENT + 1
pygame.time.set_timer(spawn_coin, 10000)
while not done:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(WHITE)
    
    for entity in all_sprites:
        entity.draw(screen)
        entity.move()


#colliding cases
    if pygame.sprite.spritecollideany(P1, enemies):
        screen.fill(RED)
        pygame.display.update()
        for entity in all_sprites:
            entity.kill() 
        time.sleep(1)
        pygame.quit()
        sys.exit()
        
    
    if pygame.sprite.spritecollideany(P1, b_account):
        for Mn in b_account:
            if pygame.sprite.collide_rect(P1, Mn):
                if Mn.nominal == 1:
                    num_m+=1
                    Mn.rect.top = 0
                    (x, y)=E1.rect.center
                    x1=random.randint(30, 470)
                    if x1!=x:
                        M1.rect.center=(x1, 0)
                    sp+=1
                if Mn.nominal == 3:
                    num_m+=3
                    Mn.rect.bottom = HEIGHT
                if Mn.nominal == 5:
                    num_m+=5
                    Mn.rect.bottom = HEIGHT

    if random.randint(1, 100) == 30 and M3.rect.bottom >= HEIGHT:
        Mn_appear(M3, E1)
    if random.randint(1, 300) == 10 and M5.rect.bottom >= HEIGHT:
        Mn_appear(M5, E1)
        
        
    text=font.render(f'Score:{num_m}', True, BLACK)
    screen.blit(text, (350, 30))
    pygame.display.update()
    clock.tick(sp)