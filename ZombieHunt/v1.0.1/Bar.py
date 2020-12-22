import pygame
class Altbar():
    def __init__(self):
        self.x_kor = 0
        self.y_kor = 500
        self.gen = 800
        self.yuk = 100
    def ciz(self,ekran):
        pygame.draw.rect(ekran,(192,192,192),[self.x_kor,self.y_kor,self.gen,self.yuk])