#!/usr/bin/env python
#coding: utf-8
import pygame
import random
from pygame.locals import *
import os
import sys
import math
from Tyokobo import Object
 
 
SCR_RECT = Rect(0, 0, 640, 480)
 
class PyAction:
    def __init__(self):
        pygame.init()
        screen = pygame.display.set_mode(SCR_RECT.size)
        pygame.display.set_caption("zibanyan and tyokobo")
        
        p1 = Object()
    	x = p1.randx()
 
        y = p1.randy()
     
     
        sysfont = pygame.font.SysFont(None, 30)
        hello2 = sysfont.render("power", True, (0,0,0))
        hello3 = sysfont.render("clear", True, (0,0,0))
 
 
        # �摜�̃��[�h
    	Zibanyan.left_image = load_image("C:\Users\sakamoto\Desktop\pythongame\zibanyan.png", -1)                     # ������
    	Zibanyan.right_image = pygame.transform.flip(Zibanyan.left_image, 1, 0)  # �E����
    	Tyokoboimage = load_image("C:\Users\sakamoto\Desktop\pythongame\yokobo.png", -1)  
    	Medal = load_image("C:\Users\sakamoto\Desktop\pythongame\medal.png", -1)
    	Uisu = load_image("C:\Users\sakamoto\Desktop\pythongame\uisu.png", -1)
 
    	self.all = pygame.sprite.RenderUpdates()
    	Zibanyan.containers = self.all
    	Zibanyan()
         
        # ���C�����[�v
    	clock = pygame.time.Clock()
    	add = 1
    	count = 0
    	add_point = 0;
    	tyokobo_count = 0;
    	ran = random.randint(1,100)
    	ran_u = random.randint(1,100)
 
	ran_x = random.randint(100,300)
 
 
	count_m = 0
    	count_t = 0
    	count_u = 0

    	dele    = 64
 
        while True:
            clock.tick(60)
            self.update()
            self.draw(screen)
            screen.blit(Tyokoboimage, (0,5))
            screen.blit(hello2, (20,5))
            pygame.draw.line(screen, (0,0,0), (85,15), (300 + add_point,15), 8)
             
 
 
            if math.fabs(x+ran - zibax) < 20  and math.fabs(y +ran + add  - zibay) < 60:
	    	    count_m = 1
                    add_point = 5
 
            if math.fabs(x - zibax) < 20  and math.fabs(y + add  - zibay) < 60:
                    count_t = 1
                    add_point = 10
 
    #uisu
            if math.fabs(x+ran_x - zibax) < 20  and math.fabs(y +ran_u + add  - zibay) < 60:
                    count_u = 1
                    add_point = -50
         
            if count_m == 0 and  count_t == 0 and count_u ==0:      
                    screen.blit(Tyokoboimage, (x,y + add))
                    screen.blit(Medal, (x+ran,y+ran + add ))
                    screen.blit(Uisu, (x+ran_x,y+ran_u + add ))
         
            if count_m == 0 and count_t == 1 and count_u ==0:
                    screen.blit(Medal, (x+ran,y+ran + add ))
                    screen.blit(Uisu, (x+ran_x,y+ran_u + add ))
 
 
            if count_t == 0 and count_m == 1 and count_u ==0:
                    screen.blit(Tyokoboimage, (x,y + add))
                    screen.blit(Uisu, (x+ran_x,y+ran_u + add ))
         
            if  count_u ==1 and count_m == 0 and count_t == 0:
                    screen.blit(Medal, (x+ran,y+ran + add ))
                    screen.blit(Tyokoboimage, (x,y + add))
 
            if  count_u ==1 and count_m == 0 and count_t == 1:
                    screen.blit(Medal, (x+ran,y+ran + add ))
 
 
            if  count_u ==1 and count_t == 0 and count_m == 1:
                    screen.blit(Tyokoboimage, (x,y + add))
     
            if  count_u ==0 and count_t == 1 and count_m == 1:
                    screen.blit(Uisu, (x+ran_x,y+ran_u + add ))

 
            if count_m == 1 and  count_t == 1 and count_u ==1:  
                    screen.blit(hello3, (50,240))
                     
            pygame.display.update()
            self.key_handler()
            add += 0.5
 
    def update(self):
        """�X�v���C�g�̍X�V"""
        self.all.update()
     
    def draw(self, screen):
        """�X�v���C�g�̕`��"""
        screen.fill((255,255,255))
        self.all.draw(screen)
     
    def key_handler(self):
        """�L�[���͏���"""
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN and event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
 
class Zibanyan(pygame.sprite.Sprite):
    MOVE_SPEED = 5.0  # �ړ����x
    JUMP_SPEED = 8.0  # �W�����v�̏����x
    GRAVITY = 0.2     # �d�͉����x
    
    def __init__(self):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.image = self.right_image
        self.rect = self.image.get_rect()
        self.rect.bottom = SCR_RECT.bottom
         
        # ���������_�̈ʒu�Ƒ��x
        self.fpx = float(self.rect.x)
        self.fpy = float(self.rect.y)
        self.fpvx = 0.0
        self.fpvy = 0.0
 
        self.on_floor = False
     
    def update(self):
        """�X�v���C�g�̍X�V"""
        # �L�[���͎擾
        pressed_keys = pygame.key.get_pressed()
 
        # ���E�ړ�
        if pressed_keys[K_RIGHT]:
            self.image = self.right_image
            self.fpvx = self.MOVE_SPEED
        elif pressed_keys[K_LEFT]:
            self.image = self.left_image
            self.fpvx = -self.MOVE_SPEED
        else:
            self.fpvx = 0.0
        if pressed_keys[K_UP]:
            if self.on_floor:
                self.fpvy = - self.JUMP_SPEED  # ������ɏ����x��^����
                self.on_floor = False
         
        # ���x���X�V
        if not self.on_floor:
            self.fpvy += self.GRAVITY  # �������ɏd�͂�������
         
        # ���������_�̈ʒu���X�V
        self.fpx += self.fpvx
        self.fpy += self.fpvy
         
        # ���n���������ׂ�
        if self.fpy > SCR_RECT.height - self.rect.height:
            self.fpy = SCR_RECT.height - self.rect.height  # ���ɂ߂荞�܂Ȃ��悤�Ɉʒu����
            self.fpvy = 0
            self.on_floor = True
         
        # ���������_�̈ʒu�𐮐����W�ɖ߂�
        # �X�v���C�g�𓮂����ɂ�self.rect�̍X�V���K�v�I
        self.rect.x = int(self.fpx)
        self.rect.y = int(self.fpy)
 
        global zibax
        zibax = self.rect.x
 
        global zibay
        zibay = self.rect.y
 
 
def load_image(filename, colorkey=None):
    filename = os.path.join("data", filename)
    try:
        image = pygame.image.load(filename)
    except pygame.error, message:
        print "Cannot load image:", filename
        raise SystemExit, message
    image = image.convert()
    if colorkey is not None:
        if colorkey is -1:
            colorkey = image.get_at((0,0))
        image.set_colorkey(colorkey, RLEACCEL)
    return image
 
if __name__ == "__main__":
    PyAction()

