# _*_ config: utf-8 _*_

import pygame, os, random
from pygame.locals import *
from sys import exit
from config.GetProjectPath import get_project_path


path = get_project_path()
background_img_filepath = os.path.join(path, 'img', 'sushiplate.jpg')
SCREEN_SIZE = (640, 480)
pygame.init()


def font_set():
    """使用字体模块，设置字体"""
    screen = pygame.display.set_mode(SCREEN_SIZE, 0 ,32)
    pygame.display.set_caption('font_set')
    background = pygame.image.load(background_img_filepath).convert()
    fullscreen = False

    # 设置字体样式和大小，传参：字体格式（用font.get_fonts()方法查看本地存在的字体，或下载字体传入字体路径）和大小
    font = pygame.font.Font('simsun.ttc', 20)
    # 使用render方法写入内容，传参：内容、是否开启锯齿、字体颜色、字体背景色(不传参可背景为空白)
    x_scroolbar = font.render(u"这是一个横向滚动条", True, (0, 0, 255))
    y_scroolbar = font.render(u"这是一个纵向滚动条", True, (255, 0, 0))
    # 设置文字初始位置
    hor_x = 640
    hor_y = 0
    ver_x = 640 - y_scroolbar.get_width()
    ver_y = 480

    while True:

        for event in pygame.event.get():
            if event.type == QUIT:
                exit()
            if event.type == KEYDOWN:
                if event.key == K_f:
                    fullscreen = not fullscreen
                    if fullscreen:
                        screen = pygame.display.set_mode(SCREEN_SIZE, FULLSCREEN, 32)
                    else:
                        screen = pygame.display.set_mode(SCREEN_SIZE, 0, 32)
        screen.blit(background, (0, 0))

        # 控制文字滚动速度
        hor_x -= 0.05
        ver_y -= 0.05
        if hor_x < -x_scroolbar.get_width():
            hor_x = 640
        if ver_y < -y_scroolbar.get_height():
            ver_y = 480
        # 绘制文字
        screen.blit(x_scroolbar, (hor_x, hor_y))
        screen.blit(y_scroolbar, (ver_x, ver_y))
        pygame.display.update()


if __name__ == '__main__':
    font_set()