import pygame, os
from pygame.locals import *
from sys import exit
from config.GetProjectPath import get_project_path

path = get_project_path()
background_img_filepath = os.path.join(path, 'img', '小丑.jpg')
pygame.init()
SCREEN_SIZE = (640, 480)


def fullscreen_mode_window():
    """可全屏窗口"""
    screen = pygame.display.set_mode(SCREEN_SIZE, 0, 32)
    Fullscreen = False
    background = pygame.image.load(background_img_filepath).convert()
    pygame.display.set_caption('fullscreen_mode_window')
    while True:

        for event in pygame.event.get():
            if event.type == QUIT:
                exit()
            if event.type == KEYDOWN:
                if event.key == K_f:
                    Fullscreen = not Fullscreen
                    if Fullscreen:
                        screen = pygame.display.set_mode((1920, 1080), FULLSCREEN, 32)   # 切换全屏
                    else:
                        screen = pygame.display.set_mode(SCREEN_SIZE, 0, 32)
        screen.blit(background, (0, 0))
        pygame.display.update()


def switch_mode_window():
    """窗口大小可变窗口"""
    global SCREEN_SIZE
    # 创建一个可改变大小的窗口， 属性：RESIZABLE
    screen = pygame.display.set_mode(SCREEN_SIZE, RESIZABLE, 32)
    background = pygame.image.load(background_img_filepath).convert()
    pygame.display.set_caption('fullscreen_mode_window')
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                exit()
            if event.type == VIDEORESIZE:
                SCREEN_SIZE = event.size
                screen = pygame.display.set_mode(SCREEN_SIZE, RESIZABLE, 32)
                pygame.display.set_caption('window resized to {}'.format(event.size))
        screen_width, screen_height = SCREEN_SIZE
        print(SCREEN_SIZE)
        screen.blit(background, (0, 0))
        # for y in range(0, screen_height, background.get_height()):
        #     for x in range(0, screen_width, background.get_width()):
        #         print(x, y)
        #         screen.blit(background, (x, y))
        pygame.display.update()


if __name__ == '__main__':
    # switch_mode_window()

    for i in range(0, 2):

        print(i)