import pygame
import os
pygame.init()
WIDTH=500
HEIGHT=500
screen=pygame.display.set_mode((WIDTH, HEIGHT))
done=False
pygame.display.set_caption("Music Player")


#music directory
music_dir= r'C:\Users\ilias\OneDrive\Рабочий стол\hello\tsis7\MUSIC_PYGAME'
songs=os.listdir(music_dir)
pygame.mixer.music.load(os.path.join(music_dir, songs[0]))
song_index=0

#font
font=pygame.font.SysFont('arial', 36)
WHITE=(255, 255, 255)
BLACK=(0, 0, 0)
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done=True
        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_SPACE:
                if pygame.mixer.music.get_busy():
                    pygame.mixer.music.pause()
                else:
                    pygame.mixer.music.unpause()

            elif event.key == pygame.K_RIGHT:
                song_index+=1
                if song_index >= len(songs):
                    song_index=0
                pygame.mixer.music.load(os.path.join(music_dir, songs[song_index]))
                pygame.mixer.music.play(-1)

            elif event.key == pygame.K_LEFT:
                song_index-=1
                if song_index == -1:
                    song_index = len(songs)-1
                pygame.mixer.music.load(os.path.join(music_dir, songs[song_index]))
                pygame.mixer.music.play(-1)
    pygame.mixer.music.play
    screen.fill(BLACK) 
    song_name=font.render(songs[song_index], True, WHITE)
    screen.blit(song_name, (WIDTH/2 - song_name.get_width()/2, HEIGHT/2 - song_name.get_height()/2))
                
    
    pygame.display.flip()
pygame.quit()