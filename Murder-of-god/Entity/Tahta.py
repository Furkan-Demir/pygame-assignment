import pygame
import os
    
current_path = os.path.dirname(__file__) # Where your .py file is located
resource_path = os.path.join(current_path, '..',"Sprites","arka.png") # The resource folder path
resim = pygame.image.load(resource_path)
class Tahta():
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def ciz(self,ekran,camera):
        ekran.blit(resim,(self.x-camera.x,self.y-camera.y))   