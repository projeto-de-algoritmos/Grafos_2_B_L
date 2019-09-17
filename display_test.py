import pygame
 
pygame.init()
screen = pygame.display.set_mode((500, 500))
done = False
color_pack = True
x = 30
y = 30
 
clock = pygame.time.Clock()
 

while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                        color_pack = not color_pack
         
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_UP]: y -= 3
        if pressed[pygame.K_DOWN]: y += 3
        if pressed[pygame.K_LEFT]: x -= 3
        if pressed[pygame.K_RIGHT]: x += 3
         
        screen.fill((0, 0, 0))

        color_line=[]
        x=0
        for i in range(0,17):
                if color_pack:
                        color_line.append((0, 255, 0))
                else:
                        color_line.append((255, 100, 0))

        if color_pack: 
                color = (0, 255, 0)
        else: 
                color = (255, 100, 0)
        x = 150
        y = 100
        pygame.draw.circle(screen, color, (x, y), 5, 5)
        pygame.draw.circle(screen, color, (x+40, y), 5, 5)
        pygame.draw.circle(screen, color, (x-40, y), 5, 5)
        pygame.draw.circle(screen, color, (x+30, y+40), 5, 5)
        pygame.draw.circle(screen, color, (x, y+40), 5, 5)
        pygame.draw.circle(screen, color, (x-50, y+80), 5, 5)
        pygame.draw.circle(screen, color, (x+50, y+80), 5, 5)
        pygame.draw.circle(screen, color, (x, y+80), 5, 5)
        pygame.draw.circle(screen, color, (x+70, y+120), 5, 5)
        pygame.draw.circle(screen, color, (x-70, y+120), 5, 5)
        pygame.draw.circle(screen, color, (x+25, y+120), 5, 5)
        pygame.draw.circle(screen, color, (x-25, y+120), 5, 5)
        
        
        pygame.draw.line(screen, color_line[0], [x,y],[x+30,y+40],1)
        pygame.draw.line(screen, color_line[1], [x+40, y],[x+30,y+40],1)
        pygame.draw.line(screen, color_line[2], [x,y],[x+40, y],1)
        pygame.draw.line(screen, color_line[3], [x-40, y],[x, y],1)
        pygame.draw.line(screen, color_line[4], [x, y],[x-30, y+40],1)
        
        pygame.draw.line(screen, color_line[5], [x-30, y+40],[x-50, y+80],1)
        pygame.draw.line(screen, color_line[6], [x-30, y+40],[x, y+80],1)

        pygame.draw.line(screen, color_line[7], [x+30, y+40],[x-50, y+80],1)
        pygame.draw.line(screen, color_line[8], [x+30, y+40],[x, y+80],1)
        pygame.draw.line(screen, color_line[9], [x+30, y+40],[x+50, y+80],1)

        pygame.draw.line(screen, color_line[10], [x+50, y+80],[x+70, y+120],1)
        pygame.draw.line(screen, color_line[11], [x+50, y+80],[x+25, y+120],1)
        pygame.draw.line(screen, color_line[12], [x, y+80],[x+25, y+120],1)
        pygame.draw.line(screen, color_line[13], [x, y+80],[x-25, y+120],1)
        pygame.draw.line(screen, color_line[14], [x-50, y+80],[x-70, y+120],1)

        pygame.draw.line(screen, color_line[15], [x-40, y],[x-70, y+120],1)

        pygame.display.flip()
        clock.tick(60)

