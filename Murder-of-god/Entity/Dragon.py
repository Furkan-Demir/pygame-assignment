import pygame
import os
pygame.font.init()
current_path = os.path.dirname(__file__) 
resource_path = os.path.join(current_path, '..',"Sprites","Dragon") 
font = pygame.font.Font(os.path.join(current_path, '..',"8bit.TTF")  , 16) 

class Dragon():
    def __init__(self):
        self.x = 1000+600
        self.y = 1000+300
        self.img = ["1.png","2.png","3.png"]
        self.img_rate = 0
        self.chat = "Seytan sana ihtiyacimiz var!"
        self.time = 0
        self.geldimi = 0
    
    def ciz(self,ekran,camera):

        
        
        self.img_rate += 0.08
        player_animation = self.img[int(self.img_rate) % len(self.img)]
        player_animation = os.path.join(resource_path,player_animation) 
        player_animation = pygame.image.load(player_animation)
        player_animation = pygame.transform.flip(player_animation, True, False)
        ekran.blit(player_animation,(self.x-camera.x,self.y-camera.y))
        if self.geldimi == 1:
            text = font.render(self.chat, True, (254,254,254), (0,0,0)) 
            ekran.blit(text, (self.x-camera.x-100,self.y-camera.y+100))
        elif self.geldimi == 2:
            text = font.render(self.chat, True, (254,254,254), (0,0,0)) 
            self.chat = "Yakinda hepimizi geberticekler."
            ekran.blit(text, (self.x-camera.x-100,self.y-camera.y+100))
        elif self.geldimi == 3:
            text = font.render(self.chat, True, (254,254,254), (0,0,0)) 
            self.chat = "Bizi kurtarmanin tek yolu..."
            ekran.blit(text, (self.x-camera.x-100,self.y-camera.y+100))
        elif self.geldimi == 4:
            text = font.render(self.chat, True, (254,0,0), (0,0,0)) 
            self.chat = "Tanriyi YOK ETMEK"
            ekran.blit(text, (self.x-camera.x-100,self.y-camera.y+100))
        elif self.geldimi == 5:
            text = font.render(self.chat, True, (200,200,200), (0,0,0)) 
            self.chat = "Yolun Sonuna ulasman gerek"
            ekran.blit(text, (self.x-camera.x-100,self.y-camera.y+100))