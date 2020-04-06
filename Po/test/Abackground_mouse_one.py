import pygame, os
from pygame.locals import *
from sys import exit
from config.GetProjectPath import get_project_path


path = get_project_path()
background_img_filepath = os.path.join(path, 'img', 'sushiplate.jpg')
mouse_img_filepath = os.path.join(path, 'img', 'fugu.png')

# 初始化pygame，未硬件做准备
pygame.init()
# 新建窗口, 传入参数：分辨率、标志（0代表不用特性）、色深
screen = pygame.display.set_mode((1920, 1080), 0, 32)
# 设置窗口标题
pygame.display.set_caption('Abcakground_mouse_one')
# 加载并转换图像， convert()方法，将图像数据转化为Surface对象，convert_alpha()处理掉透明部分
background = pygame.image.load(background_img_filepath).convert()
mouse = pygame.image.load(mouse_img_filepath).convert_alpha()

# 游戏主循环
while True:
    for event in pygame.event.get():
        # 接收到退出指令后退出游戏
        if event.type == QUIT:
            exit()
    # 画上背景， bit方法，传参：Surface对象，左上角坐标
    screen.blit(background, (0, 0))
    # 获取鼠标位置
    x, y = pygame.mouse.get_pos()
    # 计算光标左上角位置
    x -= mouse.get_width() / 2
    y -= mouse.get_height() / 2
    # 画上光标
    screen.blit(mouse, (x, y))
    # 刷新画面
    pygame.display.update()