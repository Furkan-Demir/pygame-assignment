import pygame
import os
 
class Mermi:
    def __init__(self,x,y,x_speed,y_speed):
        self.x = x
        self.y = y
        self.x_speed = x_speed
        self.y_speed = y_speed
        self.animation = ["1.png","2.png","3.png"]
        self.animation_rate = 0
        self.evil = False
    def ciz(self,ekran):
        current_path = os.path.dirname(__file__) 
        resource_path = os.path.join(current_path, '..',"Sprites","Mermi")
        if self.evil == True:
            resource_path = os.path.join(current_path, '..',"Sprites","EvilMermi") 
        self.animation_rate += 0.5
        player_animation = os.path.join(resource_path,self.animation[int(self.animation_rate)%len(self.animation)]) 
        player_animation = pygame.image.load(player_animation)
        self.x += self.x_speed
        self.y += self.y_speed
        ekran.blit(player_animation, (self.x,self.y))