import pygame
renk = (0,0,0)
ekran_gen = 600
ekran_yuk = 800
class Mermi():
    def __init__(self,mermi_id,x_start,y_start,x_speed,y_speed):
        self.mermi_id = mermi_id
        self.x_kor = x_start
        self.y_kor = y_start
        self.x_speed = x_speed
        self.y_speed = y_speed
        self.r = 2
    def ciz(self,ekran):
        pygame.draw.circle(ekran,renk,[self.x_kor,self.y_kor],self.r)
        self.x_kor += self.x_speed
        self.y_kor += self.y_speed
    def delete(self):
        if self.x_kor > ekran_yuk or self.y_kor > ekran_gen or self.x_kor < 0 or self.y_kor <0:
            return True
    def __del__(self):
        return  