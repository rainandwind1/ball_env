import pygame
import sys
import os
from PIL import Image
import math
from param import *

class ball(pygame.sprite.Sprite):
    def __init__(self, args = None):
        super(ball, self).__init__()
        if args:
            self.img_path, self.pos_x, self.pos_y, self.v_x, self.v_y, self.a_x, self.a_y = args
        self.direction_x, self.direction_y = 0, 1
        self.obj = pygame.image.load(self.img_path)
        self.rect = self.obj.get_rect()
        self.rect.x = self.pos_x
        self.rect.y = self.pos_y
         
    def move(self, members):
        for player in members:
            #print(pygame.sprite.collide_rect(player, self))
            if pygame.sprite.collide_rect(player, self) == 1:
                keyboard_state = pygame.key.get_pressed()
                self.a_x, self.a_y = player.a_x, player.a_y
                self.v_x, self.v_y = player.v_x, player.v_y
                self.direction_x = keyboard_state[player.control_key[3]] - keyboard_state[player.control_key[2]]
                self.direction_y = keyboard_state[player.control_key[1]] - keyboard_state[player.control_key[0]]
        # print(self.direction_x, self.direction_y, self.v_x, self.v_y)
        self.rect.x = self.rect.x + self.direction_x * self.v_x - self.direction_x * 0.5 * self.a_x 
        self.rect.y = self.rect.y + self.direction_y * self.v_y - self.direction_y * 0.5 * self.a_y
        self.v_x -= self.a_x
        self.v_y -= self.a_y
        if self.v_x <= 0:
            self.v_x = 0
            self.a_x = 0
        if self.v_y <= 0:
            self.v_y = 0
            self.a_y = 0
