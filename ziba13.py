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
        pygame.display.set_caption("zibanyan game")
        
        p1 = Object()
    	x = p1.randx()
 
        y = p1.randy()
     
     
        sysfont = pygame.font.SysFont(None, 30)
        hello2 = sysfont.render("power", True, (0,0,0))
        hello3 = sysfont.render("clear", True, (0,0,0))
 
 
        # 画像のロード
    	Zibanyan.left_image = load_image("C:\Users\sakamoto\Desktop\pythongame\zibanyan.png", -1)                     # 左向き
    	Zibanyan.right_image = pygame.transform.flip(Zibanyan.left_image, 1, 0)  # 右向き
    	Tyokoboimage = load_image("C:\Users\sakamoto\Desktop\pythongame\yokobo.png", -1)  
    	Medal = load_image("C:\Users\sakamoto\Desktop\pythongame\medal.png", -1)
    	Uisu = load_image("C:\Users\sakamoto\Desktop\pythongame\uisu.png", -1)

	global jump_sound
	jump_sound = pygame.mixer.Sound("jump01.wav")
	
	global get_sound
	get_sound = pygame.mixer.Sound("get.wav")


	global get_level
	get_level = pygame.mixer.Sound("get_level.wav")
	
	self.all = pygame.sprite.RenderUpdates()
    	Zibanyan.containers = self.all
    	Zibanyan()
         
        # メインループ
    	clock = pygame.time.Clock()
    	add = 1
    	count = 0
    	add_point = 0;
    	tyokobo_count = 0;
    	
    	ran_mx = random.randint(300,500)

	ran = random.randint(1,100)
	
	tyoko_x_ran = random.randint(1,300)
    	
    	ran_u = random.randint(1,100)
 
	ran_x = random.randint(300,500)
	level_sound = 0
 
 
	count_m = 0
    	count_t = 0
    	count_u = 0

    	sound_m = 0
    	sound_t = 0
    	sound_u = 0
 
        while True:
            clock.tick(60)
            self.update()
            self.draw(screen)
            screen.blit(Tyokoboimage, (0,5))
            screen.blit(hello2, (20,5))
            pygame.draw.line(screen, (0,0,0), (85,15), (300 + add_point,15), 8)
            

            medal_x = x + ran_mx
            medal_y = y + ran + add

            tyoko_x = x + tyoko_x_ran
            tyoko_y = y + add

            uisu_x = x + ran_x
            uisu_y = y + ran_u + add
	    
            
     
            if math.fabs((medal_x / 6 )- zibax ) < 60  and math.fabs(medal_y  - zibay) < 60:
	    	    sound_m += 1
	    	    count_m = 1
                    add_point = 5
		    if sound_m == 1:
		    	    get_sound.play()
		    
 
            if math.fabs((tyoko_x/ 6) - zibax ) < 80  and math.fabs(tyoko_y  - zibay) < 70:
	    	    sound_t += 1
		    count_t = 1
                    add_point = 10
		    if sound_t == 1:
		    	    get_sound.play()
 
    #uisu
            if math.fabs(uisu_x - zibax) < 20  and math.fabs(uisu_y  - zibay) < 60:
	    	    sound_u += 1
	    	    count_u = 1
                    add_point = -50
                    if sound_u == 1:
                    	    get_sound.play()
         
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
                    level_sound += 1
		    if level_sound == 1:
                    	get_level.play()

                     
            pygame.display.update()
            self.key_handler()
            add += 0.5
 
    def update(self):
        """スプライトの更新"""
        self.all.update()
     
    def draw(self, screen):
        """スプライトの描画"""
        screen.fill((255,255,255))
        self.all.draw(screen)
     
    def key_handler(self):
        """キー入力処理"""
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN and event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
 
class Zibanyan(pygame.sprite.Sprite):
    MOVE_SPEED = 5.0  # 移動速度
    JUMP_SPEED = 8.0  # ジャンプの初速度
    GRAVITY = 0.2     # 重力加速度
    
    def __init__(self):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.image = self.right_image
        self.rect = self.image.get_rect()
        self.rect.bottom = SCR_RECT.bottom
         
        # 浮動小数点の位置と速度
        self.fpx = float(self.rect.x)
        self.fpy = float(self.rect.y)
        self.fpvx = 0.0
        self.fpvy = 0.0
 
        self.on_floor = False
     
    def update(self):
        """スプライトの更新"""
        # キー入力取得
        pressed_keys = pygame.key.get_pressed()
 
        # 左右移動
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
            	jump_sound.play()
                self.fpvy = - self.JUMP_SPEED  # 上向きに初速度を与える
                self.on_floor = False
         
        # 速度を更新
        if not self.on_floor:
            self.fpvy += self.GRAVITY  # 下向きに重力をかける
         
        # 浮動小数点の位置を更新
        self.fpx += self.fpvx
        self.fpy += self.fpvy
         
        # 着地したか調べる
        if self.fpy > SCR_RECT.height - self.rect.height:
            self.fpy = SCR_RECT.height - self.rect.height  # 床にめり込まないように位置調整
            self.fpvy = 0
            self.on_floor = True
         
        # 浮動小数点の位置を整数座標に戻す
        # スプライトを動かすにはself.rectの更新が必要！
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

