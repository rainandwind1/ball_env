import pygame
import sys
import os
from PIL import Image
import math
import random
from param import *


class referee():
    def __init__(self, args = None):
        self.time = None
        self.memory = None
        self.red_score, self.blue_score = 0, 0

    def cal_score(self, ball):
        if 210 < ball.rect.y < 310:
            if ball.rect.x <= 100:
                self.blue_score += 1
                return True
            if ball.rect.x >= 1120:
                self.red_score += 1
                return True
        return False


def save_resize_img(img_path, img_path_train, width, height):#(数据存放路径，保留数据路径，改变的宽，高)
    img = Image.open(img_path)
    img = img.resize((width, height), Image.ANTIALIAS)
    img.save(img_path_train)


def draw_background(screen):
    screen.fill(background_color)
    # draw env
    pygame.draw.line(screen, white, (100, 50), (100, 470),  line_width)
    pygame.draw.line(screen, white, (1120, 50), (1120, 470),  line_width)
    pygame.draw.line(screen, white, (610, 50), (610, 470),  line_width)
    pygame.draw.circle(screen, white, (610, 260), 50, line_width)
    pygame.draw.rect(screen, white, (50, 50,  1120, 420), line_width, 50)
    pygame.draw.arc(screen, red, (50, 210, 100, 100), math.radians(90), math.radians(270), line_width)
    pygame.draw.arc(screen, blue, (1070, 210, 100, 100), math.radians(270), math.radians(90), line_width)
    pygame.draw.line(screen, red, (100, 210), (100, 310),  line_width)
    pygame.draw.line(screen, blue, (1120, 210), (1120, 310),  line_width)

def refresh_map(screen, members, referee):
    draw_background(screen)
    score_flag = referee.cal_score(members[-1])
    font =  pygame.font.SysFont('microsoft Yahei',60)
    score_sur = font.render("Score: {} : {}".format(referee.red_score, referee.blue_score), True, (255, 0, 0))
    screen.blit(score_sur, (100, 10))
    if score_flag:
        reset(screen, members)
    for mem in members:
        screen.blit(mem.obj, [mem.rect.x, mem.rect.y])
    pygame.display.update()

 
 
def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()



def button (msg, x, y, w, h, ic, ac, screen, action=None):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if x + w > mouse[0] > x and y + h > mouse[1] > y:
            pygame.draw.rect(screen, ac, (x,y,w,h))
            if click[0] == 1 and action != None:
                action()
        else:
            pygame.draw.rect(screen, ic, (x,y,w,h))
        pygame.draw.rect(screen, ic, (x,y,w,h))
        smallText = pygame.font.SysFont('comicsansms', 20)
        textSurf, textRect = text_objects(msg, smallText)
        textRect.center = ( (x+(w/2)), (y+(h/2)))
        screen.blit(textSurf, textRect)


def reset(screen, members):
    # button("Restart", 590, 240, 150, 60, green, red, screen)
    # pygame.display.update()
    
    members[0].__init__(args = ('./resource/yellow_50.png', 
                    random.uniform(610, 1120), random.uniform(50, 470), 20, 20, 10, 10, 
                    control_unit1))
    members[1].__init__(args = ('./resource/red_50.png', 
                    random.uniform(100, 610), random.uniform(50, 470), 20, 20, 10, 10,
                    control_unit2))
    members[-1].__init__(args = ('./resource/ball_25.png', 
                    597.5, 247.5, 0, 0, 0, 0))
    return