import pygame
import random
import math
pygame.init()

ekran_gen = 600
ekran_yuk = 800

ekran = pygame.display.set_mode((ekran_yuk,ekran_gen))
pygame.display.set_caption("Test")

renk = (0,0,0)
saat = pygame.time.Clock()
class Kare():
    def __init__(self):
        self.hasar = 35
        self.x_kor = 50
        self.y_kor = 300
        self.gen = 50
        self.yuk = 50
        self.speed = 5
        self.can = 100
    def ciz(self):
        pygame.draw.rect(ekran,renk,[self.x_kor,self.y_kor,self.gen,self.yuk])

class Altbar():
    def __init__(self):
        self.x_kor = 0
        self.y_kor = 500
        self.gen = 800
        self.yuk = 100
    def ciz(self):
        pygame.draw.rect(ekran,(192,192,192),[self.x_kor,self.y_kor,self.gen,self.yuk])

class Zombie():
    def __init__(self,zombi_id):
        self.can = 100
        self.x_kor = random.randint(0,550)
        self.y_kor = random.randint(0,750)
        self.r = 20
        self.can = 100
    def ciz(self,x_sp,y_sp):
        pygame.draw.circle(ekran,(25,51,0),[self.x_kor,self.y_kor],self.r)
        self.x_kor += x_sp
        self.y_kor += y_sp
    def __del__(self):
        return  
class Mermi():
    def __init__(self,mermi_id,x_start,y_start,x_speed,y_speed):
        self.mermi_id = mermi_id
        self.x_kor = x_start
        self.y_kor = y_start
        self.x_speed = x_speed
        self.y_speed = y_speed
        self.r = 2
    def ciz(self):
        pygame.draw.circle(ekran,renk,[self.x_kor,self.y_kor],self.r)
        self.x_kor += self.x_speed
        self.y_kor += self.y_speed
    def delete(self):
        if self.x_kor > ekran_yuk or self.y_kor > ekran_gen or self.x_kor < 0 or self.y_kor <0:
            return True
    def __del__(self):
        return  




def Oyun():
    mermi_id = 3
    mermi_listesi = [ ]
    zombi_listesi = [ ]
    zombi_id = 1
    kare = Kare()
    stage = 1
    hiz = 0
    fontum = pygame.font.SysFont("Arial", 30)
    altbar = Altbar()
    while True:
        
        ekran.fill((120,33,230))
        green = (0, 255, 0) 
        blue = (0, 0, 128)
        white = (0, 0, 0) 
        if kare.can > 75:
            textsurface = fontum.render('Can: '+str(kare.can), False, (0, 0, 0))
        elif kare.can <= 75 and kare.can > 50:
            textsurface = fontum.render('Can: '+str(kare.can), False, (100, 0, 0))
        elif kare.can <= 50 :
            textsurface = fontum.render('Can: '+str(kare.can), False, (255, 0, 0)) 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                mermi_id += 1
                sekme_sayisi = random.randint(-2,2)
                mermi_x = int(pos[0] - kare.x_kor+25)
                mermi_y = int(pos[1] - kare.y_kor+25)
                angle = math.atan2(mermi_y,mermi_x)
                speed = 15
                
                x_speed_mermi = int((speed*math.cos(angle)))+sekme_sayisi
                y_speed_mermi = int((speed*math.sin(angle)))
                mermi_listesi.append(Mermi(mermi_id,kare.x_kor+25,kare.y_kor+25,x_speed_mermi,y_speed_mermi))
                
        
        for mermi in mermi_listesi:
            mermi.ciz()
            test = mermi.delete()           
            if test == True:
                try:
                    mermi_listesi.remove(mermi)
                except:
                    pass
                
        for bulletim in mermi_listesi:
            for zombim in zombi_listesi:
                if zombim.x_kor  <= bulletim.x_kor <= zombim.x_kor + 2*zombim.r and zombim.y_kor <= bulletim.y_kor <= zombim.y_kor + 2*zombim.r:
                    zombim.can -= kare.hasar
                    try:
                        mermi_listesi.remove(bulletim)
                    except:
                        pass
                    
                    

        kare.ciz()
        altbar.ciz()
        ekran.blit(textsurface,(0,500))
        for zombiler in range(stage*3):
            if len(zombi_listesi) < (stage*3):
                zombi_listesi.append(Zombie(zombi_id))
                zombi_id += 1
        for zmbi in zombi_listesi:
            zombi_x =   kare.x_kor-zmbi.x_kor
            zombi_y =  kare.y_kor-zmbi.y_kor
            anglex = math.atan2(zombi_y,zombi_x)
            
            zombi_speed = 3
            x_z = int((math.cos(anglex)*zombi_speed))
            y_z = int((math.sin(anglex)*zombi_speed))

            zmbi.ciz(x_z,y_z)
            print(zmbi.can)
            try:
                if zmbi.x_kor  <= kare.x_kor <= zmbi.x_kor + 2*zmbi.r and zmbi.y_kor <= kare.y_kor <= zmbi.y_kor + 2*zmbi.r:
                    kare.can -= 15
                    zombi_listesi.remove(zmbi)
            except:
                pass
            try:
                if zmbi.can <= 0:
                    zombi_listesi.remove(zmbi)
                    del zmbi
            except:
                pass
            


        keys = pygame.key.get_pressed()

            
        if keys[pygame.K_LEFT]:
            if kare.x_kor-1 < 0:
                kare.x_kor += 1

            else:
                kare.x_kor -= kare.speed

        if keys[pygame.K_RIGHT]:
            if kare.x_kor+1 > 750:
                kare.x_kor -= 1
            else:
                kare.x_kor += kare.speed
            

        if keys[pygame.K_UP]:
            if kare.y_kor+1 < 0:
                kare.y_kor = kare.y_kor+1
            elif kare.y_kor+1 > 500:
                kare.y_kor -= 1
            else:
                kare.y_kor -= kare.speed
            

        if keys[pygame.K_DOWN]:
            if kare.y_kor+1 < 0:
                kare.y_kor = kare.y_kor+1
            elif kare.y_kor+1 > 450:
                kare.y_kor -= 1
                
            else:
               kare.y_kor += kare.speed
            

        pygame.display.update()
        saat.tick(60)

Oyun()