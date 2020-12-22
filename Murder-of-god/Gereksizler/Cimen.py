import pygame
import random
import os
current_path = os.path.dirname(__file__)
resource_path = os.path.join(current_path, '..',"Sprites","Cimen") 
class Cimen():
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.image = str(random.randint(1,3))+ ".png"

    def ciz(self,ekran,camera):
        resmim = os.path.join(resource_path,self.image) 
        resmim = pygame.image.load(resmim)
        ekran.blit(resmim,(self.x-camera.x,self.y-camera.y)) 