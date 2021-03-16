import pygame
import random
from Circle import Circle


pygame.init()

def generate_random_circles(number, win_size, radius, surface):
    circles = []
    for i in range(number):
        circles.append(Circle(radius, 
        random.choices(range(256), k=3), 
        center=random.choices(range(win_size), k=2),
        surface=surface))
    return circles

#win - Surface
win_size = 700
win = pygame.display.set_mode((win_size,win_size))
background_color = (255,255,255)

radius = 25
circle_color = (255,255,0)
center = (250, 250)

circle = Circle(25, circle_color, center, win)
#генерируем 10 кругов
circles_num = 10
circles = generate_random_circles(circles_num, win_size, radius, win)

current_circles_number = 1
#таймер прибытия нового круга
timer = 0
TIME_TO_ADD = 3000

clock = pygame.time.Clock()
FPS = 60

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    win.fill(background_color)
    #code
    #circle.move_by_keys()
    #circle.jump()
    if timer > TIME_TO_ADD:
        timer = 0
        current_circles_number += 1
    if current_circles_number > circles_num:
        current_circles_number = 1
    for i in range(current_circles_number):
        circles[i].random_movement(win_size)
        circles[i].draw()
    
    pygame.display.update()
    timer += clock.tick(FPS)