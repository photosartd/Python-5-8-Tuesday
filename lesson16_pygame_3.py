import pygame
import math

width = 500
height = 500
center = 250
x = center
y = center
#Перемещение при нажатии
dc = 3
#скорость переещения при возврате
dv = 3
background_color = (255,255,255)

pygame.init()
win = pygame.display.set_mode((width, height))
yellow = (255,255,0)
red = (255,0,0)
circle_color = yellow
def distance(x, y, center):
    a = x - center
    b = y - center
    summ = a*a + b*b #16 + 9 = 25
    c = math.pow(summ, 0.5)
    return c

dist = distance(246, 247, 250)
print(dist)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    win.fill(background_color)
    #Вот здесь мы всегда будем помещать наш код и логику
    #Цвет

    if distance(x,y,center) > 150:
        circle_color = red
    else:
        circle_color = yellow
        
    pygame.draw.circle(win, circle_color, (x,y), 25)
    #Перемещение по клавишам
    keys = pygame.key.get_pressed()
    #Если кнопка ВЛЕВО нажата
    if keys[pygame.K_LEFT]:
        x -= dc
    elif keys[pygame.K_RIGHT]:
        x += dc
    elif keys[pygame.K_UP]:
        y -= dc
    elif keys[pygame.K_DOWN]:
        y += dc
    else:
        #А что здесь, если хотим вернуть окружность в центр?
            #Перемещения
        if x > center:
            x -= dv
        elif x < center:
            x += dv

        if y > center:
            y -= dv
        elif x < center:
            y += dv
        
            
    pygame.display.update()
    pygame.time.delay(10)