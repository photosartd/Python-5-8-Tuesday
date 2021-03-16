import pygame

pygame.init()
#win - Surface
win = pygame.display.set_mode((500,500))
background_color = (255,255,255)

#Задаём параметры прямоугольника
x_r, y_r = 0, 250
dir_r = 1
#Задаё параметры окружности
x_c, y_c = 250, 0
dir_c = 1

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    #Логика прямоугольника
    if dir_r == 1:
        x_r += 1
    else:
        x_r -= 1

    if x_r > 500:
        dir_r = -1
    elif x_r < 0:
        dir_r = 1
    
    #Логика окружности
    if dir_c == 1:
        y_c += 1
    else:
        y_c -= 1
    
    if y_c > 500:
        dir_c = -1
    elif y_c < 0:
        dir_c = 1

    win.fill(background_color)
    pygame.draw.rect(win, (170, 150, 90), (x_r,y_r,50,50))
    pygame.draw.circle(win, (255,255,0), (x_c, y_c), 25)
    pygame.display.update()

    pygame.time.delay(100)