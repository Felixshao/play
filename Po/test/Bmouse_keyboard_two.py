import os, pygame, random
from pygame.locals import *
from sys import exit
from config.GetProjectPath import get_project_path

path = get_project_path()
background_img_filepath = os.path.join(path, 'img', 'sushiplate.jpg')
pygame.init()
SCREEN_SIZE = (1920, 1080)
screen = pygame.display.set_mode(SCREEN_SIZE, 0, 32)


def event_font():

    font = pygame.font.SysFont('arial', 18)
    font_height = font.get_linesize()
    print(font_height)
    event_text = []
    Fullscreen = False
    while True:

        event = pygame.event.wait()
        event_text = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                      'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't'
                                                                                                                     'a',
                      'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                      'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
                      'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                      'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
                      'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                      'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
                      'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                      'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
                      'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                      'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
                      ]
        num = random.randint(50, len(event_text))
        event_text = event_text[-num:]
        if event.type == QUIT:
            exit()
        if event.type == KEYDOWN:
            if event.key == K_f:
                Fullscreen = not Fullscreen
                if Fullscreen:
                    # 创建一个硬件加速的全屏窗口，FULLSCREEN(全屏窗口)， HWSURFACE(硬件加速，必须和FULLSCREEN一起使用)
                    pygame.display.set_mode((1920, 1080), FULLSCREEN | HWSURFACE, 32)
                else:
                    pygame.display.set_mode((1920, 1080), 0, 32)
        screen.fill((0, 0, 0))
        y = SCREEN_SIZE[1] - font_height
        for text in reversed(event_text):
            x = random.randint(0, SCREEN_SIZE[0])
            screen.blit(font.render(text, True, (0, 255, 0)), (x, y))
            #
            y -= font_height
        pygame.display.update()


def mosue_event():
    """鼠标事件"""

    pygame.display.set_caption('mosue_event')
    background = pygame.image.load(background_img_filepath).convert()

    x, y = 0, 0
    move = {K_LEFT: 0, K_RIGHT: 0, K_UP: 0, K_DOWN: 0}

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
               exit()
            if event.type == KEYDOWN:
                if event.key in move:
                    move[event.key] = 0.2   # 控制移动的速度
            elif event.type == KEYUP:
                if event.key in move:
                    move[event.key] = 0
        x -= move[K_LEFT]
        x += move[K_RIGHT]
        y -= move[K_UP]
        y += move[K_DOWN]
        screen.fill((0, 0, 0))
        screen.blit(background, (x, y))
        pygame.display.update()


if __name__ == '__main__':
    event_font()

