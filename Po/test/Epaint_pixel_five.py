# _*_ config: utf-8 _*_

import pygame, os, random
from pygame.locals import *
from sys import exit
from config.GetProjectPath import get_project_path

path = get_project_path()
background_img_filepath = os.path.join(path, 'img', 'sushiplate.jpg')
SCREEN_SIZE = (640, 480)
pygame.init()


def get_color(height):
    """获取颜色"""
    # 设置3原色图像对象
    red_scale_surface = pygame.Surface((640, height))
    green_scale_surface = pygame.Surface((640, height))
    blue_scale_sruface = pygame.Surface((640, height))

    # 绘画3原色矩形条
    for x in range(640):
        c = int((x/640.) * 255)
        red = (c, 0, 0)
        green = (0, c, 0)
        blue = (0, 0, c)
        line_rect = Rect(x, 0, 1, height)
        pygame.draw.rect(red_scale_surface, red, line_rect)
        pygame.draw.rect(green_scale_surface, green, line_rect)
        pygame.draw.rect(blue_scale_sruface, blue, line_rect)
    return red_scale_surface, green_scale_surface, blue_scale_sruface


def color_match():
    """三原色搭配器"""
    screen = pygame.display.set_mode(SCREEN_SIZE, 0, 32)
    fullscreen = False

    red_scale_surface, green_scale_surface, blue_scale_sruface = get_color(80)
    # 初始颜色
    color = [127, 127, 127]
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
        # 填充背景色
        screen.fill((0, 0, 0))
        # 绘画三原色
        screen.blit(red_scale_surface, (0, 0))
        screen.blit(green_scale_surface, (0, 80))
        screen.blit(blue_scale_sruface, (0, 160))
        # 获取鼠标坐标
        x, y = pygame.mouse.get_pos()
        # 判断是否点击鼠标
        if pygame.mouse.get_pressed()[0]:
            for component in range(3):
                # 判断点击的是那种原色
                if (y > component*80) and (y < (component + 1) * 80):
                    # 写入此原色数值
                    color[component] = int((x/639.) * 255)
            pygame.display.set_caption('三原色搭配器，color: {}'.format(tuple(color)))

        # 绘画滚动球位置
        for component in range(3):
            # 获得滚动球位置
            pos = (int((color[component]/255.)*639), component*80+40)
            # 画出滚动球位置,  pygame.draw.circle方法画出圆形，传参：窗口对象、填充景色、圆球位置、半径大小
            pygame.draw.circle(screen, (255, 255, 255), pos, 20)

        # 绘制矩形，pygame.draw.rect绘制矩形方法，传参：窗口对象(或Surface对象)、填充颜色、rect参数((x, y)左上角坐标, (width, height)宽高)
        pygame.draw.rect(screen, tuple(color), (0, 240, 640, 240))
        pygame.display.update()


def gradient_color():
    """颜色渐变"""
    screen = pygame.display.set_mode(SCREEN_SIZE, 0, 32)
    fullscreen = False

    color1 = (221, 90, 20)
    color2 = (96, 130, 51)
    factor = 0.

    def blend_color(color1, color2, factor):
        """混合色"""
        r1, g1, b1 = color1
        r2, g2, b2 = color2
        r = r1 + (r2 - r1) * factor
        g = g1 + (g2 - g1) * factor
        b = b1 + (b2 - b1) * factor
        return int(r), int(g), int(b)

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
        tri = [(0, 120), (639, 100), (639, 140)]
        screen.fill((255, 255, 255))
        # 绘制任意多边形
        pygame.draw.polygon(screen, (0, 255, 0), tri)
        # 绘制圆形
        pygame.draw.circle(screen, (0, 0, 0), (int(factor * 639.0), 120), 10)

        x, y = pygame.mouse.get_pos()
        if pygame.mouse.get_pressed()[0]:
            factor = x / 639.0

        color = blend_color(color1, color2, factor)
        pygame.display.set_caption('渐变色，color: {}'.format(color))
        pygame.draw.rect(screen, color, (0, 240, 640, 240))
        pygame.display.update()


if __name__ == '__main__':
    gradient_color()
    # color_match()



