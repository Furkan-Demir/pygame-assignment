import pygame
import random
class Zombie():
    def __init__(self,zombi_id):
        self.can = 100
        self.x_kor = random.randint(0,550)
        self.y_kor = random.randint(0,750)
        self.r = 20
        self.can = 100
        self.animation = True
        self.animation_sayac = 0
        self.animation_sayac2 = 0
    def ciz(self,x_sp,y_sp,ekran):
        
        pygame.draw.circle(ekran,(25,70,0),[self.x_kor,self.y_kor],self.r)
        if self.animation == True:
            if self.animation_sayac2 < 30:
                pygame.draw.circle(ekran,(160,0,0),[self.x_kor,self.y_kor],7)
                
                self.animation_sayac2 += 1
            else:
                self.animation_sayac2 = 0
                self.animation = False

        else:
            if self.animation_sayac < 15:
                self.animation_sayac += 1
            else:
                self.animation_sayac = 0
                self.animation = True


        self.x_kor += x_sp
        self.y_kor += y_sp
    def __del__(self):
        return  