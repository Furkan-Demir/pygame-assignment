import pygame
import os
current_path = os.path.dirname(__file__) 
resource_path = os.path.join(current_path, '..',"Sprites","kalp.png")

class Heart:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.speed = 2
    def ciz(self,ekran):

        ekran.blit(pygame.image.load(resource_path), (self.x,self.y))