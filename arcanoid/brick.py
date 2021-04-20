import pygame

class Brick:
    def __init__(self, surface, win_size, color, left, top, width):
        self.surface = surface
        self.win_size = win_size
        self.color = color

        self.left = left
        self.top = top
        self.width = width
        self.right = self.left + self.width
        self.height = self.width / 10
        self.bottom = self.top + self.height

    def draw(self):
        self.rect = (self.left, self.top, self.width, self.height)
        pygame.draw.rect(self.surface, self.color, self.rect, width=1)

class Platform(Brick):
    def __init__(self, surface, win_size, color, left, top, width):
        super().__init__(surface, win_size, color, left, top, width)
        self.diff = 3

    def move_by_keys(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            if self.left <= 0:
                pass
            else:
                self.left -= self.diff
                self.right = self.left + self.width
        elif keys[pygame.K_RIGHT]:
            if self.left + self.width >= self.win_size:
                pass
            else:
                self.left += self.diff
                self.right = self.left + self.width

    def draw(self):
        self.rect = (self.left, self.top, self.width, self.height)
        pygame.draw.rect(self.surface, self.color, self.rect, 1, int(self.height/2))

class Wall:
    def __init__(self, win_size, color, surface):
        self.win_size = win_size
        self.color = color
        self.surface = surface

        self.bricks = []

    def fill(self, n_rows, n_cols):
        #координаты левого верхнего угла кирпича
        top = 0
        left = 0
        #ширина кирпича
        width = int(self.win_size/n_cols)
        for row in range(n_rows):
            left = 0
            for col in range(n_cols):
                brick = Brick(self.surface, self.win_size, self.color, left, top, width)
                self.bricks.append(brick)
                left = left + width
            top = top + width/10

    def draw(self):
        for brick in self.bricks:
            brick.draw()