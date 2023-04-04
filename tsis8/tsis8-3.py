# import pygame

# pygame init()

# WIDTH = 500
# HEIGHT = 500
# WHITE = (255, 255, 255)
# BLACK = (0, 0, 0)
# RED = (255, 0 0)
# GREEN = (0, 255, 0)
# BLUE = (0, 0, 255)
# x=250
# y=250
# screen = pygame.display.set_mode((WIDTH, HEIGHT))
# pygame.display.set_caption('Budget Paint')
# done = False
# while not done:
#     for event in pygame.event.get():
#         if event.type == QUIT:
#             pygame.quit()
#         if event.type == pygame.KEYDOWN:
#             if 
        

import pygame

def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    clock = pygame.time.Clock()
    
    radius = 15
    x = 0
    y = 0
    mode = 'blue'
    points = []
    erase = 0
    square = 0
    circle = 1 
    while True:
        
        pressed = pygame.key.get_pressed()
        
        alt_held = pressed[pygame.K_LALT] or pressed[pygame.K_RALT]
        ctrl_held = pressed[pygame.K_LCTRL] or pressed[pygame.K_RCTRL]
        
        for event in pygame.event.get():
            
            # determin if X was clicked, or Ctrl+W or Alt+F4 was used
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w and ctrl_held:
                    return
                if event.key == pygame.K_F4 and alt_held:
                    return
                if event.key == pygame.K_ESCAPE:
                    return
            
                # determine if a letter key was pressed
                if event.key == pygame.K_r:
                    mode = 'red'
                elif event.key == pygame.K_g:
                    mode = 'green'
                elif event.key == pygame.K_b:
                    mode = 'blue'
                elif event.key == pygame.K_e:
                    erase = 1         
                elif event.key == pygame.K_s:
                    square=1 
                    circle =0
                elif event.key == pygame.K_c:
                    square = 0
                    circle = 1
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1: # left click grows radius
                    radius = min(200, radius + 1)
                elif event.button == 3: # right click shrinks radius
                    radius = max(1, radius - 1)
            
            if event.type == pygame.MOUSEMOTION:
                # if mouse moved, add point to list
                position = event.pos
                points = points + [position]
                # points = points[-256:]
                
        screen.fill((0, 0, 0))
        
        # draw all points
        i = 0
        if circle == 1:

            while i < len(points) - 1:
                drawLineBetween(screen, i, points[i], points[i + 1], radius, mode, erase)
                i += 1
        elif circle == 0:
            while i < len(points) - 1:
                drawLineBetween_s(screen, i, points[i], points[i + 1], radius, mode, erase)
                i += 1
                
        if erase == 1:
            screen.fill((0, 0, 0))
            points=[]
            erase=0
        
        pygame.display.flip()
        
        clock.tick(60)

def drawLineBetween(screen, index, start, end, width, color_mode, eraser):
    # c1 = max(0, min(255, 2 * index - 256))
    c1 = 0
    # c2 = max(0, min(255, 2 * index))
    c2 = 255
    
    if color_mode == 'blue':
        color = (c1, c1, c2)
    elif color_mode == 'red':
        color = (c2, c1, c1)
    elif color_mode == 'green':
        color = (c1, c2, c1)

    dx = start[0] - end[0]
    dy = start[1] - end[1]
    iterations = max(abs(dx), abs(dy))
    
    for i in range(iterations):
        progress = 1.0 * i / iterations
        aprogress = 1 - progress
        x = int(aprogress * start[0] + progress * end[0])
        y = int(aprogress * start[1] + progress * end[1])
        pygame.draw.circle(screen, color, (x, y), width)


def drawLineBetween_s(screen, index, start, end, width, color_mode, eraser):
    # c1 = max(0, min(255, 2 * index - 256))
    c1 = 0
    # c2 = max(0, min(255, 2 * index))
    c2 = 255
    
    if color_mode == 'blue':
        color = (c1, c1, c2)
    elif color_mode == 'red':
        color = (c2, c1, c1)
    elif color_mode == 'green':
        color = (c1, c2, c1)

    dx = start[0] - end[0]
    dy = start[1] - end[1]
    iterations = max(abs(dx), abs(dy))
    
    for i in range(iterations):
        progress = 1.0 * i / iterations
        aprogress = 1 - progress
        x = int(aprogress * start[0] + progress * end[0])
        y = int(aprogress * start[1] + progress * end[1])
        pygame.draw.rect(screen, color, pygame.Rect(x, y, width, width))

main()