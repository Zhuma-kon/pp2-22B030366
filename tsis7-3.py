import pygame
pygame.init()
WIDTH=500
HEIGHT=500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('A circle game')

music=r'C:\Users\ilias\OneDrive\Рабочий стол\hello\tsis7\MUSIC_PYGAME\Driftveil City.mp3'
pygame.mixer.music.load(music)
pygame.mixer.music.play(-1)

x=250
y=250
done=False

clock=pygame.time.Clock()
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done=True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN and y<=HEIGHT-25:
                y+=20
            elif event.key == pygame.K_UP and y>=25:
                y-=20
            elif event.key == pygame.K_RIGHT and x<=WIDTH-25:
                x+=20
            elif event.key == pygame.K_LEFT and x>=25:
                x-=20
    
    screen.fill((0, 0, 0))
    pygame.draw.circle(screen, (255, 0, 0), (x, y), 25)
    pygame.display.update()
    clock.tick(60)
pygame.quit()