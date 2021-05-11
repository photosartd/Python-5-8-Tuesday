import pygame

pygame.init()

#win - Surface
win_size = 700
win = pygame.display.set_mode((win_size,win_size))
background_color = (255,255,255)

class MySpritesGroup(pygame.sprite.Group):
    def __init__(self):
        super().__init__(self)
    def draw_if_pressed(self, screen):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            self.draw(screen)

img = pygame.image.load('crash.png')
class MySprite(pygame.sprite.Sprite):
    def __init__(self, *group):
        super().__init__(*group)
        self.image = img
        self.rect = self.image.get_rect()

group = MySpritesGroup()
sprite = MySprite(group)


clock = pygame.time.Clock()
FPS = 600

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    win.fill(background_color)
    #code
    group.draw_if_pressed(win)
    pygame.display.update()
    clock.tick(FPS)