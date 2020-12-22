import pygame
import random
import math
from Player import Kare
from Bar import Altbar
from Enemy import Zombie
from Bullet import Mermi
from Buttonum import GUIButton
pygame.init()
ekran_gen = 600
ekran_yuk = 800
green = (0, 255, 0)
red = (255,0,0)
blue = (0, 0, 128)
white = (0, 0, 0)
ekran = pygame.display.set_mode((ekran_yuk,ekran_gen))
pygame.display.set_caption("Test")
fontum = pygame.font.SysFont("Arial", 30)
renk = (0,0,0)
saat = pygame.time.Clock()

def Oyun():
    mermi_id = 3
    mermi_listesi = [ ]
    zombi_listesi = [ ]
    zombi_id = 1
    
    stage = kare.stage
    hiz = 0
    gui_button_listesi = [GUIButton("Sarjor Arttır",10,505,170,40,red,"sarjor",0,True),
    GUIButton("+50 Can",10,555,170,40,red,"can",0,True),
    GUIButton("Mermi Hasarı",190,505,190,40,red,"hasar",0,True)]
    altbar = Altbar()

    for zombiler in range(stage*3):
        if len(zombi_listesi) < (stage*3):
            zombi_listesi.append(Zombie(zombi_id))
            zombi_id += 1
    while True:
        if kare.can < 1:
            return gameover()
        ekran.fill((120,33,230))
        kare.ciz(ekran)
        altbar.ciz(ekran)
        if len(zombi_listesi) == 0:
            kare.stage += 1
            kare.can = kare.max_can
            return Oyun()
        ## GUI start
        for i in gui_button_listesi:
            if i.durum == False:
                if i.sayac < 100:
                    i.sayac_arttir()
                else:
                    i.durum = True
                    i.sayac = 0
            elif i.durum == True:
                pos = pygame.mouse.get_pos()
                click = pygame.mouse.get_pressed()
                i.ciz(ekran)
                i.buy_event(pos,click,kare)
                

        if kare.can > 75:
            textsurface = fontum.render('Can: '+str(kare.can), False, (0, 0, 0))
        elif kare.can <= 75 and kare.can > 50:
            textsurface = fontum.render('Can: '+str(kare.can), False, (100, 0, 0))
        elif kare.can <= 50:
            textsurface = fontum.render('Can: '+str(kare.can), False, (255, 0, 0))
        
        ekran.blit(textsurface,(650,503))
        sarjorsayisi = fontum.render('Mermi: '+str(kare.sarjor), False, (51, 0, 0))
        ekran.blit(sarjorsayisi,(650,550))
        para_goster = fontum.render('Para: '+str(kare.para), False, (0, 0, 0))
        ekran.blit(para_goster,(490,550))
        stagegoster = fontum.render('Bölüm: '+str(kare.stage), False, (0, 0, 0))
        ekran.blit(stagegoster,((ekran_gen/2)+20,0))
        parago = fontum.render("Hepsi 100 Para", False, (0, 0, 0))
        ekran.blit(parago,(190,555))
        ## GUI end
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONUP:
                if kare.sarjor > 0:
                    kare.sarjor -= 1
                    pos = pygame.mouse.get_pos()
                    mermi_id += 1
                    sekme_sayisi = random.randint(-2,2)
                    mermi_x = int(pos[0] - kare.x_kor+16)
                    mermi_y = int(pos[1] - kare.y_kor+16)
                    angle = math.atan2(mermi_y,mermi_x)
                    speed = 15
                    
                    x_speed_mermi = int((speed*math.cos(angle)))+sekme_sayisi
                    y_speed_mermi = int((speed*math.sin(angle)))
                    mermi_listesi.append(Mermi(mermi_id,kare.x_kor+16,kare.y_kor+16,x_speed_mermi,y_speed_mermi))
                
        
        for mermi in mermi_listesi:
            mermi.ciz(ekran)
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
                    
                    



        for zmbi in zombi_listesi:
            zombi_x =   kare.x_kor-zmbi.x_kor+16
            zombi_y =  kare.y_kor-zmbi.y_kor+16
            anglex = math.atan2(zombi_y,zombi_x)
            
            zombi_speed = 2
            x_z = int((math.cos(anglex)*zombi_speed))
            y_z = int((math.sin(anglex)*zombi_speed))

            zmbi.ciz(x_z,y_z,ekran)
            print(zmbi.can)
            try:
                if kare.x_kor  <= zmbi.x_kor+zmbi.r <= kare.x_kor+32 and kare.y_kor  <= zmbi.y_kor+zmbi.r <= kare.y_kor+32:
                    kare.can -= 15
                    zombi_listesi.remove(zmbi)
                   
            except:
                pass
            try:
                if zmbi.x_kor <= kare.x_kor+16 <= zmbi.x_kor+zmbi.r*2 and zmbi.y_kor  <= kare.y_kor+16 <= zmbi.y_kor+zmbi.r*2:
                    kare.can -= 15
                    zombi_listesi.remove(zmbi)
                   
            except:
                pass
            try:
                if zmbi.can <= 0:
                    kare.para   += 100
                    zombi_listesi.remove(zmbi)
                    del zmbi
            except:
                pass
        reload_yapiyormu = reloadfunc()
        if reload_yapiyormu == True:
            sarjorsayisi = fontum.render('Sarjor Yenileniyor', False, (51, 0, 0))
            ekran.blit(sarjorsayisi,(int(ekran_gen/2),int(ekran_yuk/2)))    
        movementfunc()
        pygame.display.update()
        saat.tick(60)




def reloadfunc():
    if kare.sarjor == 0 and kare.sarjor_bekleme_sure <60:
        kare.sarjor_bekleme_sure += 1
        return True
    elif kare.sarjor == 0 and kare.sarjor_bekleme_sure >= 10:
        kare.sarjor = kare.max_sarjor
        kare.sarjor_bekleme_sure = 0

def movementfunc():
    keys = pygame.key.get_pressed()         
    if keys[pygame.K_a]:
        if kare.x_kor-1 < 0:
            kare.x_kor += 1

        else:
            kare.x_kor -= kare.speed

    if keys[pygame.K_d]:
        if kare.x_kor+1 > 750:
            kare.x_kor -= 1
        else:
            kare.x_kor += kare.speed
        

    if keys[pygame.K_w]:
        if kare.y_kor+1 < 0:
            kare.y_kor = kare.y_kor+1
        elif kare.y_kor+1 > 500:
            kare.y_kor -= 1
        else:
            kare.y_kor -= kare.speed
        

    if keys[pygame.K_s]:
        if kare.y_kor+1 < 0:
            kare.y_kor = kare.y_kor+1
        elif kare.y_kor+1 > 450:
            kare.y_kor -= 1
            
        else:
            kare.y_kor += kare.speed


def gameover():
    start = GUIButton("Yeniden Oyna",300,250,200,40,red,"baslat",0,True)
    FPS = pygame.time.Clock()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        start.ciz(ekran)
        pos = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if start.buy_event(pos,click) == True:
            kare.can = 100
            return Oyun()
        pygame.display.update()
        FPS.tick(60)

def startgame():
    start = GUIButton("Oyna!",300,250,200,40,red,"baslat",0,True)
    FPS = pygame.time.Clock()
    while True:
        ekran.fill((255,255,255))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        start.ciz(ekran)
        pos = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if start.buy_event(pos,click) == True:
            kare.can = 100
            return Oyun()
        pygame.display.update()
        FPS.tick(60)

kare = Kare()
startgame()