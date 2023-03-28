import pygame
import datetime

pygame.init()

WIDTH = 820
HEIGHT = 820
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Mickey Clock')

clock_image = pygame.image.load(r'C:\Users\ilias\OneDrive\Рабочий стол\hello\tsis7\mickey clock\clock.png')
minute_hand_image = pygame.image.load(r'C:\Users\ilias\OneDrive\Рабочий стол\hello\tsis7\mickey clock\right.png')
second_hand_image = pygame.image.load(r'C:\Users\ilias\OneDrive\Рабочий стол\hello\tsis7\mickey clock\left2.png')


minute_hand_center = minute_hand_image.get_rect().center
second_hand_center = second_hand_image.get_rect().center


minute_hand_pos = (120, 130)
second_hand_pos = (430, 410)
minute_hand_rot = 0
second_hand_rot = 0

clock = pygame.time.Clock()

done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    now = datetime.datetime.now()
    minute = now.minute
    second = now.second

    minute_hand_rot = -6 * minute
    second_hand_rot = -6 * second

    minute_hand_rotated = pygame.transform.rotate(minute_hand_image, minute_hand_rot)
    second_hand_rotated = pygame.transform.rotate(second_hand_image, second_hand_rot)

    screen.blit(clock_image, (0, 0))
    screen.blit(minute_hand_rotated, minute_hand_pos)
    screen.blit(second_hand_rotated, second_hand_pos)

    pygame.display.update()
    clock.tick(60)

pygame.quit()