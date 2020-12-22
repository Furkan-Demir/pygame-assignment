import pygame
import random
class Zombie():
    def __init__(self,zombi_id):
        self.can = 100
        self.x_kor = random.randint(0,550)
        self.y_kor = random.randint(0,750)
        self.r = 20
        self.can = 100
    def ciz(self,x_sp,y_sp,ekran):
        pygame.draw.circle(ekran,(25,51,0),[self.x_kor,self.y_kor],self.r)
        self.x_kor += x_sp
        self.y_kor += y_sp
    def __del__(self):
        return  