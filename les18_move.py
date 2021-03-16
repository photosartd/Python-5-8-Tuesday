import pygame

pygame.init()
#win - Surface
win = pygame.display.set_mode((500,500))
background_color = (255,255,255)

x, y = 250, 250

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    x = x + 1
    if x > 500:
        x = 250
    win.fill(background_color)
    pygame.draw.rect(win, (170, 150, 90), (x,y,50,50))
    pygame.display.update()

    pygame.time.delay(10)