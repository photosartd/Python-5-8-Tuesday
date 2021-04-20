import pygame
import random
from brick import Platform, Brick
class Circle:
    def __init__(self, radius, color, center, surface):
        self.radius = radius
        self.color = color
        self.x, self.y = center[0], center[1]
        self.surface = surface
        self.diff = 3
        self.is_jumping = False
        self.jump_number = 10
        #на сколько будет изменяться по x и y
        self.diff_x = 0
        self.diff_y = 0
        while self.diff_x == 0 or self.diff_y == 0 or self.diff_x == self.diff_y:
            self.diff_x = random.randint(-3,3)
            self.diff_y = random.randint(-3,3)
    def draw(self):
        pygame.draw.circle(self.surface, self.color, (self.x, self.y), self.radius)
    def move_by_keys(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.x -= self.diff
        elif keys[pygame.K_RIGHT]:
            self.x += self.diff
        elif keys[pygame.K_UP]:
            self.y -= self.diff
        elif keys[pygame.K_DOWN]:
            self.y += self.diff
    def jump(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            self.is_jumping = True
        if self.is_jumping == True:
            if self.jump_number > 0:
                self.y -= 10
                self.jump_number -= 1
            elif self.jump_number <= 0 and self.jump_number > - 10:
                self.y += 10
                self.jump_number -= 1
            else:
                self.is_jumping = False
                self.jump_number = 10

    def collision(self, brick):
        if ((self.y + self.radius >= brick.top and \
             self.y + self.radius < brick.bottom) or \
            (self.y - self.radius <= brick.bottom and \
                 self.y - self.radius > brick.top)) and \
                (brick.left <= self.x <= brick.right):
                self.diff_y = -self.diff_y
                if (isinstance(brick, Brick)):
                    return True
                elif isinstance(brick, Platform):
                    return False
        return False

    def random_movement(self, width, brick, wall):
        self.__wall_collision(wall)
        self.collision(brick)
        self.x += self.diff_x
        self.y += self.diff_y
        if self.x + self.radius >= width or self.x - self.radius <= 0:
            self.diff_x = -self.diff_x
        if self.y + self.radius >= width or self.y - self.radius <= 0:
            self.diff_y = -self.diff_y

    def __wall_collision(self, wall):
        for brick in wall.bricks:
            coll = self.collision(brick)
            if coll:
                wall.bricks.remove(brick)
                if len(wall.bricks) == 0:
                    wall.fill(50,50)        


