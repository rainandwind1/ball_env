import pygame
import sys
import os
from PIL import Image
import math
import random
from param import *
from player import *
from ball import *
from utils import *

def main_process():

    pygame.init()                           # 初始化pygame
    size = width, height                    # 设置窗口大小
    screen = pygame.display.set_mode(size)  # 显示窗口www
    

    Ball = ball(args = ('./resource/ball_25.png', 
                    597.5, 247.5, 0, 0, 0, 0))
    Player1 = player(args = ('./resource/yellow_50.png', 
                    random.uniform(610, 1120), random.uniform(50, 470), 10, 10, 10, 10,
                    control_unit1))
    Player2 = player(args = ('./resource/red_50.png', 
                    random.uniform(100, 610), random.uniform(50, 470), 10, 10, 10, 10, 
                    control_unit2))
    members = [Player1, Player2, Ball]      # game 成员
    Referee = referee()
    clock = pygame.time.Clock()             # 刷新时钟

    
    refresh_map(screen, members, Referee)

    while True:                             # 死循环确保窗口一直显示
        clock.tick(tick_freq)
        for event in pygame.event.get():    # 遍历所有事件
            if event.type == pygame.QUIT:   # 如果单击关闭窗口，则退出
                sys.exit()
        
        # update mem state
        Player1.move()
        Player2.move()
        Ball.move([Player1, Player2])

        # refresh screen
        refresh_map(screen, members, Referee)
    
    pygame.quit()                           # 退出pygame



if __name__ == "__main__":
    # save_resize_img('./resource/red.png', './resource/red_50.png', 50, 50)
    main_process()