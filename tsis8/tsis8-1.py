import pygame
import sys
from pygame import * 
import random, time
#preparing code by writing common things
pygame.init()

WIDTH=500
HEIGHT=500
sp=3
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Game')

BLACK=(0, 0, 0)
WHITE=(255, 255, 255)
BLUE=(0, 0, 255)
RED=(255, 0, 0)
YELLOW=(255, 255, 0)
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
        self.rect.move_ip(0, sp)
        if self.rect.bottom>HEIGHT:
            self.rect.top = 0
            self.rect.center=(random.randint(30, 470), 0)
        
    def draw(self, surface):
        lil_s=pygame.Surface((60, 60))
        lil_s.fill(RED)
        # pygame.draw.rect(screen, RED,  self.rect)
        surface.blit(lil_s, self.rect)

class money(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.rect = pygame.Rect(20, 20, 20, 20)
        self.rect.center=(random.randint(30, 470), 0)

    def move(self):
        self.rect.move_ip(0, 10)
        if self.rect.bottom>HEIGHT:
            self.rect.top = 0
            self.rect.center=(random.randint(30, 470), 0)
        
    def draw(self, surface):
        lil_s=pygame.Surface((20, 20))
        lil_s.fill(YELLOW)
        # pygame.draw.rect(screen, RED,  self.rect)
        surface.blit(lil_s, self.rect)

#making an abject of classes made before, also grouping them in groups
P1=player()
E1=enemy()
M1=money()
enemies=pygame.sprite.Group()
enemies.add(E1)
b_account=pygame.sprite.Group()
b_account.add(M1)
all_sprites=pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)
all_sprites.add(M1)
num_m=0
while not done:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    # P1.movement()
    # E1.move()

    screen.fill(WHITE)
    for entity in all_sprites:
        entity.draw(screen)
        entity.move()
    # P1.draw(screen)
    # E1.draw(screen)

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
        num_m+=1
        M1.rect.top = 0
        (x, y)=E1.rect.center
        x1=random.randint(30, 470)
        if x1!=x:
            M1.rect.center=(x1, 0)
        sp+=1
    
    text=font.render(f'Score:{num_m}', True, BLACK)
    screen.blit(text, (350, 30))
    pygame.display.update()
    clock.tick(60)