import pygame
import os
    
current_path = os.path.dirname(__file__) # Where your .py file is located
resource_path = os.path.join(current_path, '..',"Sprites","wall.png") # The resource folder path
resim = pygame.image.load(resource_path)
grass = pygame.transform.scale(resim, (32, 32))
class Wall():
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def ciz(self,ekran,camera):
        ekran.blit(grass,(self.x-camera.x,self.y-camera.y))   
