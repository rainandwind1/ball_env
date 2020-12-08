import pygame
import sys
import os
from PIL import Image
import math
from param import *

class player(pygame.sprite.Sprite):
    def __init__(self, args = None):
        super(player, self).__init__()
        if args:
            self.img_path, self.pos_x, self.pos_y, self.v_x, self.v_y, self.a_x, self.a_y, self.control_key = args
        self.obj = pygame.image.load(self.img_path)
        self.rect = self.obj.get_rect()
        self.rect.x = self.pos_x
        self.rect.y = self.pos_y

    def move(self):
        keyboard_state = pygame.key.get_pressed()
        self.rect.y += (keyboard_state[self.control_key[1]] - keyboard_state[self.control_key[0]]) * (2 + keyboard_state[self.control_key[4]]*4)
        self.rect.x += (keyboard_state[self.control_key[3]] - keyboard_state[self.control_key[2]]) * (2 + keyboard_state[self.control_key[4]]*4)
        # self.playerrect = self.playerrect.move(player_speed)
        # if self.playerrect.left < 0 or self.playerrect.right > width: player_speed[0] = -player_speed[0]
        # if self.playerrect.bottom > height or self.playerrect.top < 0: player_speed[1] = -player_speed[1]
