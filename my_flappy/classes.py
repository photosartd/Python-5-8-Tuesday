import pygame

def load_image(path):
    image = pygame.image.load(path)
    return image

class Bird(pygame.sprite.Sprite):
    def __init__(self, center: tuple, win_size: tuple):
        pygame.sprite.Sprite.__init__(self)
        #картинка
        self.image = load_image(r'my_flappy\bird.png')
        #убираем фон
        transparent_color = self.image.get_at((0,0))
        self.image.set_colorkey(transparent_color)
        #задаём прямоугольник объекта
        self.rect = self.image.get_rect()
        self.rect.centerx, self.rect.centery = center 
        self.speedx, self.speedy = 0, 0
        self.win_size = win_size
        self.flying = False
    def update(self):
        if self.flying:
            self.speedy += 0.5
            if self.speedy > 8:
                self.speedy = 8
            if self.rect.bottom < self.win_size[1]: 
                self.rect.y += self.speedy
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            self.flying = True
            self.speedy = -10

class Pipe(pygame.sprite.Sprite):
    def __init__(self, image, win_size: tuple, velocity = 5, top=False, height=250):
        pygame.sprite.Sprite.__init__(self)
        image = pygame.transform.scale(image, (70, height))
        self.image = image
        transparent_color = self.image.get_at((0,0))
        self.image.set_colorkey(transparent_color)
        self.rect = self.image.get_rect()
        if top:
            self.rect.top = 0
        else:
            self.rect.bottom = win_size[1]
        self.rect.x = win_size[0]

        self.velocity = velocity
    def update(self):
        self.rect.x -= self.velocity
        if self.rect.right < 0:
            self.kill()