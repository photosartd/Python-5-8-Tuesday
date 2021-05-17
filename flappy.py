import pygame

pygame.init()

win_size = 700
win = pygame.display.set_mode((win_size,win_size))
background_color = (255,255,255)


class Tube(pygame.sprite.Sprite):
    def __init__(self, *group):
        super().__init__(group)
        self.image = pygame.image.load('tube.png')
        self.rect = self.image.get_rect()
        self.rect.x = 350
        self.rect.y = 350
    def update(self):
        self.rect.x += 1

player = Tube()
group = pygame.sprite.Group()
group.add(player)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
                
    win.fill(background_color)
    #code
    group.draw(win)
    group.update()
    pygame.display.update()
