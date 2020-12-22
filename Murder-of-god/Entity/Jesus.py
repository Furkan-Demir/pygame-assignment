import pygame
import os
pygame.font.init()
current_path = os.path.dirname(__file__) 
resource_path = os.path.join(current_path, '..',"Sprites","Jesus") 
font = pygame.font.Font(os.path.join(current_path, '..',"8bit.TTF")  , 16) 
class Jesus:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.durum = False
        self.img = ["1.png","2.png","3.png","4.png","5.png","6.png","7.png","8.png","9.png","10.png","11.png"]
        self.img_rate = 11
        self.chat =["Ben herseye gucu yeten Jesus.","Seni adi seytan.","Beni mi yok edeceksin Hahaha.","!!Savasalim!!"]
        self.chat_rate =0
        self.time = 0
        self.animation_bittimi = False
    def ciz(self,ekran,player,camera):
        if self.durum == False and abs(self.x-player.x) < 300 and abs(self.y-player.y) <300:
            self.durum = True
        if self.durum == True and self.img_rate == 0:
            self.animation_bittimi = True
        if self.durum == True and self.img_rate != 0:
            self.img_rate -= 0.1
        
        if self.animation_bittimi == True:
            try:
                self.chat_rate += 0.005
                player_animation = os.path.join(resource_path,"1.png") 
                player_animation = pygame.image.load(player_animation)
                player_animation = pygame.transform.flip(player_animation, True, False)
                ekran.blit(player_animation,(self.x-camera.x,self.y-camera.y))
                text = font.render(self.chat[int(self.chat_rate)], True, (254,0,0), (0,0,0)) 
                ekran.blit(text, (self.x-camera.x-200,self.y-camera.y-100))
            except:
                return "fight"

        if self.durum == True and self.animation_bittimi != True:
            try:
                player_animation = os.path.join(resource_path,self.img[int(self.img_rate)]) 
                player_animation = pygame.image.load(player_animation)
                player_animation = pygame.transform.flip(player_animation, True, False)
                ekran.blit(player_animation,(self.x-camera.x,self.y-camera.y))
            except:
                self.animation_bittimi = True
                player_animation = os.path.join(resource_path,"1.png") 
                player_animation = pygame.image.load(player_animation)
                player_animation = pygame.transform.flip(player_animation, True, False)
                ekran.blit(player_animation,(self.x-camera.x,self.y-camera.y))
    def draw(self,ekran):
        player_animation = os.path.join(resource_path,"1.png") 
        player_animation = pygame.image.load(player_animation)
        player_animation = pygame.transform.flip(player_animation, True, False)
        ekran.blit(player_animation,(self.x,self.y))