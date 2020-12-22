import pygame
green = (0, 255, 0)
red = (255,0,0)
blue = (0, 0, 128)
white = (0, 0, 0)
class Kare():
    def __init__(self):
        self.para = 100
        self.sarjor_bekleme_sure = 0
        self.sarjor = 13
        self.max_sarjor = 13
        self.hasar = 35
        self.x_kor = 50
        self.y_kor = 300
        self.gen = 50
        self.yuk = 50
        self.speed = 5
        self.can = 100
    def ciz(self,ekran):
        if self.can > 75:
            pygame.draw.rect(ekran,blue,[self.x_kor,self.y_kor,self.gen,self.yuk])
        elif 75 >= self.can > 50:
            pygame.draw.rect(ekran,(40,40,128),[self.x_kor,self.y_kor,self.gen,self.yuk])
        elif self.can <= 50:
            pygame.draw.rect(ekran,(153,0,0),[self.x_kor,self.y_kor,self.gen,self.yuk])