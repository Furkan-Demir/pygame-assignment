import pygame
import random
import os
import math
from Entity.PlayerNormal import PlayerNormal
from Entity.PlayerEvil import PlayerEvil
from Entity.Camera import Camera
from Entity.Map import map_cozumle
from Entity.Grass import Grass
from Bolumler.bolum import bolum
from Entity.Dragon import Dragon
from Funcs.Player_Movement import Player_Movement
from Gereksizler.Cimen import Cimen
from Entity.Wall import Wall
from Entity.Tahta import Tahta
from Entity.Window import Window
from Entity.Jesus import Jesus
from Entity.Heart import Heart
from Entity.Mermi import Mermi
pygame.mixer.pre_init()
pygame.mixer.init()
pygame.init()

ekran_gen = 600
ekran_yuk = 800
ekran = pygame.display.set_mode((ekran_yuk,ekran_gen))
pygame.display.set_caption("Test")
FPS_ayar = pygame.time.Clock()

def oyun_olustur():
    global player
    global camera
    global grass_yerleri
    global wall_listem
    global Grass_liste
    global cimen_liste
    global window_liste
    global jesus
    global evil_mode
    cimen_liste = [ ]
    Grass_liste = [ ]
    wall_listem = [ ]
    grass_yerleri = []
    window_liste = [ ]
    objeler = map_cozumle(bolum(seviye))
    map_engel = 1000
    x_kor = objeler[1][0]+map_engel
    y_kor = objeler[1][1]+map_engel
    if evil_mode == True:
        player = PlayerEvil(x_kor,y_kor)
    else:
        player = PlayerNormal(x_kor,y_kor)
    camera = Camera(player)
    for iX in objeler[0]:
        wall_listem.append(Wall(iX[0]+map_engel,iX[1]+map_engel))
    for iX in objeler[2]:
        cimen_liste.append(Cimen(iX[0]+map_engel,iX[1]+map_engel+17))
    for iX in objeler[3]:
        Grass_liste.append(Grass(iX[0]+map_engel,iX[1]+map_engel))
    for i in Grass_liste:
        wall_yeri_x = set([t for t in range(i.x,i.x+32)])
        wall_yeri_y = set([t for t in range(i.y,i.y+32)])
        grass_yerleri.append([[i.x,i.x+32],wall_yeri_y,wall_yeri_x])
    for i in wall_listem:
        wall_yeri_x = set([t for t in range(i.x,i.x+32)])
        wall_yeri_y = set([t for t in range(i.y,i.y+32)])
        grass_yerleri.append([[i.x,i.x+32],wall_yeri_y,wall_yeri_x])    
    for iX in objeler[4]:
        window_liste.append(Window(iX[0]+map_engel,iX[1]+map_engel))
    jesus = Jesus(objeler[5][0]+map_engel,objeler[5][1]+map_engel)
    if seviye == 2:
        jesus.chat = ["Demek Yasak Elmayi Yedin","Seytani Formun Bile Beni Yenemez","Seni Zavalli","Goster Gucunu"]
    
    
    camera.update(player)

def Oyun():
    global evil_mode
    if seviye == 2:
        evil_mode = True
    if seviye == 1:
        global dragon
        dragon = Dragon()
    oyun_olustur()
    while True:
        if player.y > 1600:
            return Oyun()
        ekran.fill((209, 255, 252))
        if seviye == 1:
            dragon.ciz(ekran,camera)
        for i in cimen_liste:
            i.ciz(ekran,camera)
        for i in Grass_liste:
            i.ciz(ekran,camera)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        Player_Movement(player,grass_yerleri,ekran,camera)
        for i in window_liste:
            i.ciz(ekran,camera)
        for i in wall_listem:
            i.ciz(ekran,camera)
        camera.update(player)
        for i in Grass_liste:
            i.ciz(ekran,camera)
        if seviye == 1:
            Bolum_1()
            fightmi = jesus.ciz(ekran,player,camera)
            if fightmi == "fight":
                return Jesus_Ilk_Savas()
        if seviye == 2:
            fightmi = jesus.ciz(ekran,player,camera)
            if fightmi == "fight":
                return Jesus_Ikinci_Savas()
        pygame.display.update()
        FPS_ayar.tick(90)


def Bolum_1():
    current_path = os.path.dirname(__file__) 
    resource_path = os.path.join("8bit.TTF") 
    font = pygame.font.Font(os.path.join(resource_path)  , 16) 
    if dragon:
        dragon.time += 1
        if dragon.time < 150:
            dragon.x -= 2
        if dragon.time > 150 and dragon.time < 300:
            dragon.geldimi = 1
        if dragon.time > 300 and dragon.time < 500:
            dragon.geldimi = 2
        if dragon.time > 500 and dragon.time < 750:
            dragon.geldimi = 3
        if dragon.time > 750 and dragon.time < 1000:
            dragon.geldimi = 4
        if dragon.time > 1000 and dragon.time < 1200:
            dragon.geldimi = 5
        if dragon.time > 1200:
            dragon.y -= 2

def Jesus_Ilk_Savas():
    current_path = os.path.dirname(__file__) 
    resource_path = os.path.join("8bit.TTF") 
    font = pygame.font.Font(os.path.join(resource_path)  , 16) 
    jesusum = Jesus(380,50)
    jesusum.animation_bittimi = True
    text = font.render("YOK EDICEM HAHAHA", True, (254,0,0), (0,0,0)) 
    efekt = 0
    kalp = Heart(300,300)
    mermi_listesi = [ ]
    timing = 0
    for i in range(400):
        if i % 10 == 0:
            mermi_listesi.append(Mermi(200,100+i,1,0))
    oldu_mu = 0
    while True:
        efekt += 1
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        ekran.fill((0,0,0))
        pygame.draw.rect(ekran,(250,250,250),[200,100,400,400])
        jesusum.draw(ekran)
        if efekt < 30:
            ekran.blit(text, (290,20))
        elif efekt > 60:
            efekt = 0
        keys = pygame.key.get_pressed()
        if keys[pygame.K_d] and kalp.x < 590:
            kalp.x += kalp.speed
        if keys[pygame.K_a] and kalp.x > 200:
            kalp.x -= kalp.speed
        if keys[pygame.K_w] and kalp.y > 100:
            kalp.y -= kalp.speed
        if keys[pygame.K_s] and kalp.y < 490:
            kalp.y += kalp.speed
        for i in mermi_listesi:
            i.ciz(ekran)
            if i.x <= kalp.x <= i.x+10 and i.y <= kalp.y <= i.y+10 and oldu_mu == 0:
                oldu_mu = 1
                efektim = os.path.join(os.path.dirname(__file__) ,"Sound","dead.wav") 
                pygame.mixer.Channel(0).play(pygame.mixer.Sound(efektim))
                for i in mermi_listesi:
                    i.x_speed = 0
        if oldu_mu == 1:
            timing += 1
        if timing > 120:
            return Animasyon()
        kalp.ciz(ekran)
        pygame.display.update()
        FPS_ayar.tick(90)

def Animasyon():
    _x = 400
    _y = 0
    bg =pygame.image.load(os.path.join( os.path.join(os.path.dirname(__file__),"Sprites","spacebg.png") ))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        bg = pygame.transform.scale(bg, (800, 600))
        ekran.blit(bg, (0,0))
        pygame.draw.circle(ekran,(254,254,254),[_x,_y],3)
        _y += 2
        if _y > 600:
            return Bolum_2()
        pygame.display.update()
        FPS_ayar.tick(90)

def Bolum_2():
    oyuncum = ["1.png","2.png","3.png","4.png","5.png","6.png","7.png","8.png","9.png","10.png","11.png","12.png","13.png"]
    oyuncu_rate = 12.99
    oyuncu_konum =os.path.join(os.path.join(os.path.dirname(__file__),"Sprites","NormalPlayer","Dead"))
    bitti_mi = None
    apple_konum =pygame.image.load(os.path.join(os.path.join(os.path.dirname(__file__),"Sprites","apple.png")))
    _x = 400
    _y = 0
    apple_var = True
    zaman = 0
    while True:
        oyuncu_resim = pygame.image.load(os.path.join(oyuncu_konum,oyuncum[int(oyuncu_rate)]))
        if bitti_mi == False:
            oyuncu_rate -= 0.1
        if oyuncu_rate < 0.3:
            bitti_mi = True
            oyuncu_rate = 0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        ekran.fill((0,0,0))
        pygame.draw.rect(ekran,(250,250,250),[200,100,400,400])

        ekran.blit(oyuncu_resim,(400,450))
        if bitti_mi == True:
            zaman += 1
        if zaman > 50:
            global seviye
            seviye = 2
            
            return Oyun()
        if _y > 450-32:
            apple_var = False
            bitti_mi = False
        if apple_var == True:
            _y += +3
            ekran.blit(apple_konum,(_x,_y))
        pygame.display.update()
        FPS_ayar.tick(90)



def Jesus_Ikinci_Savas():
    current_path = os.path.dirname(__file__) 
    resource_path = os.path.join("8bit.TTF") 
    font = pygame.font.Font(os.path.join(resource_path)  , 16) 
    font2 = pygame.font.Font(os.path.join(resource_path)  , 32) 
    jesusum = Jesus(380,50)
    jesusum.animation_bittimi = True
    text = font.render("KACABILIRSIN AMA SAKLANAMAZSIN", True, (254,0,0), (0,0,0)) 
    kalp = Heart(300,300)
    mermi_listesi = [ ]
    efekt = 0
    zorluk = 0
    can = 3

    while True:
        stage_show = font2.render("Stage "+str(zorluk)+"/7", True, (254,0,0), (0,0,0))
        can_show = font2.render("Can "+str(can), True, (254,254,254), (0,0,0)) 
        if len(mermi_listesi) == 0:
            zorluk += 1
            mermi_listesi = mermi_olustur(mermi_listesi,zorluk)
            for i in mermi_listesi:
                i.evil = True
        efekt += 1
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        ekran.fill((0,0,0))
        pygame.draw.rect(ekran,(250,250,250),[200,100,400,400])
        jesusum.draw(ekran)
        if efekt < 30:
            ekran.blit(text, (190,20))
        elif efekt > 60:
            efekt = 0
        kalpmove(kalp)
        for i in mermi_listesi:
            i.ciz(ekran)
            try:
                if i.x < 0 or i.x > 800 or i.y < 0 or i.y>600:
                    mermi_listesi.remove(i)
            except:
                pass
            try:
                if i.x <= kalp.x <= i.x+10 and i.y <= kalp.y <= i.y+10:
                    efektim = os.path.join(os.path.dirname(__file__) ,"Sound","dead.wav") 
                    pygame.mixer.Channel(0).play(pygame.mixer.Sound(efektim))
                    mermi_listesi.remove(i)
                    can -= 1
            except:
                pass
        if can <= 0:
            zorluk = 0
            can = 3
            return Jesus_Ikinci_Savas()
        if zorluk == 7:
            pass
        ekran.blit(stage_show, (250,550))
        ekran.blit(can_show, (630,550))
        kalp.ciz(ekran)
        pygame.display.update()
        FPS_ayar.tick(90)

def mermi_olustur(mermi_listesi,zorluk):
    mermi_listesi = [ ]
    for i in range(zorluk*10):
        random_at = random.randint(1,4)
        if random_at == 1:
            # 200-600
            # 0-100
            # y neg degisken
            mermi_listesi.append(Mermi(random.randint(200,600),random.randint(0,100),0,random.randint(2,4)))
        elif random_at == 2:
            mermi_listesi.append(Mermi(random.randint(0,200),random.randint(100,500),random.randint(2,4),0))
        elif random_at == 3:
            mermi_listesi.append(Mermi(random.randint(600,800),random.randint(100,500),random.randint(-4,-2),
            random.randint(-1,1)))
        elif random_at == 4:
            mermi_listesi.append(Mermi(random.randint(200,600),random.randint(500,600),random.randint(-1,1),random.randint(2,4)))
    return mermi_listesi
def kalpmove(kalp):
    keys = pygame.key.get_pressed()
    if keys[pygame.K_d] and kalp.x < 590:
        kalp.x += kalp.speed
    if keys[pygame.K_a] and kalp.x > 200:
        kalp.x -= kalp.speed
    if keys[pygame.K_w] and kalp.y > 100:
        kalp.y -= kalp.speed
    if keys[pygame.K_s] and kalp.y < 490:
        kalp.y += kalp.speed


def FinalAnimasyon():
    spr_player = ["1.png","2.png","3.png","4.png","5.png","6.png","7.png","8.png","9.png","10.png","11.png"
    ,"12.png","13.png","14.png","15.png","16.png" ]
    player_index = 0
    spr_jesus = ["1.png","2.png","3.png","4.png","5.png","6.png","7.png","8.png","9.png","10.png","11.png" ]
    jesus_index = 0
    timing = 0
    mesajlar = ["HAYIIRRRRRR","SENI LANET OLASII"]
    mesaj_index = 0
    player_konum =os.path.join(os.path.join(os.path.dirname(__file__),"Sprites","EvilAtak"))
    jesus_konum =os.path.join(os.path.join(os.path.dirname(__file__),"Sprites","Jesus"))
    mesaj_varmi = True
    resource_path = os.path.join("8bit.TTF") 
    font = pygame.font.Font(os.path.join(resource_path)  , 30) 

    while True:

        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        timing += 1
        if timing < 10:
            ekran.fill((250,250,250))
        elif 10 <= timing <=20:
            ekran.fill((70,0,0))
        else:
            timing = 0

        if mesaj_varmi == True and mesaj_index < 1.89:
            text = font.render(mesajlar[int(mesaj_index)], True, (254,0,0), (0,0,0))
            mesaj_index += 0.01
            ekran.blit(text,(330,200))
        if mesaj_index > 1.80:
            mesaj_varmi = False

        if mesaj_varmi == False:
            if player_index < len(spr_player) - 0.5:
                player_index += 0.1
            else:
                if jesus_index < len(spr_jesus) - 0.5:
                    jesus_index += 0.1
                else:
                    return oyun_bitti()
        jesus_resim = pygame.image.load(os.path.join(jesus_konum,spr_jesus[int(jesus_index)]))
        jesus_resim = pygame.transform.flip(jesus_resim, True, False)
        jesus_resim = pygame.transform.scale(jesus_resim, (140, 128))
        oyuncu_resim = pygame.image.load(os.path.join(player_konum,spr_player[int(player_index)]))
        oyuncu_resim = pygame.transform.scale(oyuncu_resim, (150, 128))
        ekran.blit(oyuncu_resim,(200,300))
        ekran.blit(jesus_resim,(400,300))
        pygame.display.update()
        FPS_ayar.tick(90)

def oyun_bitti():
    resource_path = os.path.join("8bit.TTF") 
    font = pygame.font.Font(os.path.join(resource_path)  , 20)
    text = "Oyun Bitti Cikis icin A ya basiniz"
    text2 = "Yeniden Oynamak icin X ye basiniz"
    while True:
        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT or keys[pygame.K_a]:
                pygame.quit()
            if keys[pygame.K_x]:
                return StartGame()
        ekran.fill((250,250,250))
        textim = font.render(text, True, (0,0,0), (250,0,0))
        text2im = font.render(text2, True, (0,0,0), (250,0,0))
        ekran.blit(textim,(150,200))
        ekran.blit(text2im,(150,300))
        pygame.display.update()
        FPS_ayar.tick(90)
def StartGame():
    sarkim = os.path.join(os.path.dirname(__file__) , "Sound","music1.mp3")
    pygame.mixer.music.load(sarkim)
    pygame.mixer.music.play(-1)
    return Oyun()
evil_mode = False
global seviye
seviye = 1
StartGame()