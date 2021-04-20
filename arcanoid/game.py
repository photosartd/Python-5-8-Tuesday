import pygame
import random
from Circle import Circle
from brick import Brick, Platform, Wall
import constants

pygame.init()

#win - Surface
win_size = 700
win = pygame.display.set_mode((win_size,win_size))
background_color = (0,0,0)

brick_color = (127, 178, 67)
#кирпич

#платформа
platform = Platform(win, win_size, brick_color, win_size/2, win_size/2, win_size/10)
#мячик
ball_radius = 15
ball_color = constants.YELLOW
center = (win_size/2, win_size/2)
ball = Circle(ball_radius, ball_color, center, win)
#стена
wall = Wall(win_size, constants.RED, win)
wall.fill(10, 10-)

clock = pygame.time.Clock()
FPS = 600

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    win.fill(background_color)
    #code
    ball.random_movement(win_size, platform, wall)
    ball.draw()
    platform.move_by_keys()
    platform.draw()
    wall.draw()
    
    pygame.display.update()
    clock.tick(FPS)