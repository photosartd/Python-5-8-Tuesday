import pygame
from classes import Bird, Pipe 
'''
Один из способов создать меню в игре - это создать ещё один цикл для меню 
внутри основного игрового цикла, который будет выполняться при нажатии
на какую-то кнопку (в данном примере нужно нажать escape). При нажатии на кнопку будет вызываться 
функция menu, которая будет исполняться до того, пока мы снова не нажмём escape и не выйдем 
из внутреннего бесконечного цикла.
'''
pygame.init()

clock = pygame.time.Clock()
fps = 60

win_size = 700
win = pygame.display.set_mode((win_size,win_size))
background_color = (255,255,255)


pipe_image = pygame.image.load(r'my_flappy\pipe.png')
pipe_image = pygame.transform.scale(pipe_image, (70, 200))
pipe_image_rotated = pygame.transform.flip(pipe_image, False, True)

bird = Bird(center=(250,350), win_size=(win_size, win_size))
# pipe = Pipe(pipe_image, win_size=(win_size, win_size))
# pipe_top = Pipe(pipe_image_rotated, win_size=(win_size, win_size), top=True)
bird_group = pygame.sprite.Group()
pipe_group = pygame.sprite.Group()
bird_group.add(bird)
# pipe_group.add(pipe)
# pipe_group.add(pipe_top)

last_pipe_x = 499

'''
Инициализация шрифта
'''
font0 = pygame.font.SysFont('arial', 64)
red = (255,0,0)
'''
Функция отрисовки текста. Передаём туда (в таком же порядке)
строку текста, шрифт, его цвет, surface, на которой хотим его отображать и
координаты x, y левого верхнего угла.
'''
def draw_text(text, font, color, frame, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x,y)
    frame.blit(textobj, textrect)  

menu_color = (0,0,0)
def menu(win):
    #цикл меню
    running = True
    while running:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
        win.fill(menu_color)
        draw_text('Menu', font0, red, win, 320, 320)
        pygame.display.update()

background_img = pygame.image.load(r'my_flappy\background.png')
background_img = pygame.transform.scale(background_img, (win_size, win_size))

run = True

while run:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                menu(win)
    clock.tick(fps)
    win.blit(background_img, (0,0))
    #code

    hits = pygame.sprite.spritecollide(bird, pipe_group, True)
    if hits:
        run = False

    if last_pipe_x != 499:
        last_pipe_x = pipe_group.sprites()[-1].rect.x

    if last_pipe_x < win_size - 200:
        pipe0_bottom = Pipe(pipe_image, win_size=(win_size, win_size))
        pipe0_top = Pipe(pipe_image_rotated, win_size=(win_size, win_size), top=True)
        pipe_group.add(pipe0_bottom, pipe0_top)
        last_pipe_x = pipe0_top.rect.x
    bird_group.update()
    pipe_group.update()
    bird_group.draw(win)
    pipe_group.draw(win)
    pygame.display.update()
