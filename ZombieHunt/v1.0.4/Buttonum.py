import pygame
from Player import Kare
from saveload import save_func, load_func

class GUIButton():
    def __init__(self,text,x_kor,y_kor,gen,yuk,renk,eventim,sayac,durum):
        self.eventim  = eventim
        self.sayac  = sayac
        self.durum  = durum
        self.x_kor  = x_kor
        self.y_kor  = y_kor
        self.gen    = gen
        self.yuk    = yuk
        self.renk   = renk
        self.text = text
    def ciz(self,ekran):
        fontum = pygame.font.SysFont("Arial", 30)
        
        pygame.draw.rect(ekran,self.renk,[self.x_kor,self.y_kor,self.gen,self.yuk])
        text, text_kare = text_objesi(self.text,fontum)
        text_kare.center=(self.x_kor+self.gen/2,self.y_kor+self.yuk/2)
        ekran.blit(text,text_kare)
    def durum_update(self):
        if self.durum == True:
            self.durum = False
        else:
            self.durum = True
    def buy_event(self,pos,mouse_click,player=None):
        if pos[0]>self.x_kor and pos[0]<self.x_kor+self.gen and pos[1]>self.y_kor and pos[1]<self.y_kor+self.yuk:
            if self.eventim != None and  mouse_click[0] == 1 and self.durum == True:
                if self.eventim == "sarjor" and player.para >= 100:
                    player.para -= 100
                    player.max_sarjor += 3
                    self.durum = False

                elif self.eventim == "can" and player.para >= 100:
                    player.can += 50
                    player.para -= 100
                    self.durum = False

                elif self.eventim == "hasar" and player.para >= 100:
                    player.hasar += 15
                    player.para -= 100
                    self.durum = False
                elif self.eventim == "baslat":
                    return True

                elif self.eventim == "save":
                    save_func(player)
                    self.durum = False
                    return True

                elif self.eventim == "load":
                    load_func(player)
                    self.durum = False
                    return True

    
    def sayac_arttir(self):
        self.sayac += 1

def text_objesi(text,font):
    renk = (0,0,0)
    text = font.render(text,True,renk)
    return text,text.get_rect()
