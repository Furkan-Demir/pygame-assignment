# Redhunter - Zombi Hunting Game
Redhunter 2D Topdown Shooter oyunudur.

```sh
$ Python 3.8.3
$ Pygame 1.9.6
```
# Oyun Yapısı

  - Oyunum 5 tane objeden oluşmaktadır. (Player, Alt bar, Zombi, Buton, Mermi)
  - Oyunumun display'i olan fonksiyonları: Oyun(), gameover(), startgame()

Oyun() Fonksiyonu Anlatımı:
# 1. Bölüm
```sh
def Oyun():
    mermi_id = 1
    mermi_listesi = [ ]
    zombi_listesi = [ ]
    zombi_id = 1
```

```sh
mermi_id = 1
zombi_id = 1
```
Oyunu başlatan ana fonksiyonumda while döngüsüne girmeden önce ayarlamalar yaptım. Mermi objelerimin birbirinden ayırt edilebilmesi için mermi_id = 1 dedikten sonra her mermimin id'sini +1'ledim. Aynı durum zombilerin id'sinde de geçerlidir.

```sh
mermi_listesi = [ ]
```
Ayrıca mermi objelerimi bir listede tuttum. Sebebi yarattığım mermi objem eğer zombiyle çarpışırsa ya da haritanın dışına çıkarsa silinmesini istiyordum. Yoksa oyun kapanana kadar yaratılan tüm mermiler gereksiz yere hesaplanacaktı.
___
# 2. Bölüm
```sh
gui_button_listesi = [GUIButton("Sarjor Arttır",10,505,170,40,red,"sarjor",0,True),
GUIButton("+50 Can",10,555,170,40,red,"can",0,True),
GUIButton("Mermi Hasarı",190,505,190,40,red,"hasar",0,True),
GUIButton("Oyunu Kaydet",600,0,200,40,green,"save",0,True)]
altbar = Altbar()
```
Oyunumunda kullandığım butonlarımı daha rahat şekilde kontrol edebilmek için hepsini bir listede topladım.
Altbar objemde, ekranın alt kısmında, butonlarımın bulunduğu yere çizgi çekmeye yarıyor.
___
# 3. Bölüm
```sh
for zombiler in range(stage*3):
    if len(zombi_listesi) < (stage*3):
        zombi_listesi.append(Zombie(zombi_id))
        zombi_id += 1
```
For döngüsü ile oyuncunun bölüm*3 kadar zombi yaratılmasını sağladım. Ve zombi_id değişkenimi 1 arttırdım.

___
# 4. Bölüm

```sh
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
```

```sh
if kare.can < 1:
    return gameover()
```
Eğer oyuncunun canı 1'den az ise gameover ekranına return'le.

```sh
ekran.fill((120,33,230))
kare.ciz(ekran)
altbar.ciz(ekran)
```
ekran.fill ile oyunun arkaplanını çizdim.
Kare ve altbarı çizdirdim.
```sh
if len(zombi_listesi) == 0:
    kare.stage += 1
    kare.can = kare.max_can
    return Oyun()
```
Eğer oyunda zombi kalmamışsa oyuncunun bölümünü (stage) 1 arttır ve canını 100 yap (max_can).
En son olarakta geri Oyun()'a yönlendir.
___
# 5. Bölüm
```sh
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
```
Butonlarımda durum değişkeni var. Bu değişken eğer butona tıklanılmışsa False'a dönüp butonun çizdirilmesini engelliyor. Böyle birşey yapma sebebim ise butona tıklanıldığında 100kere tıklanılmış gibi algılıyor, satın alma eventleride ister istemez 100 kere gerçekleşmiş oluyor (eğer 100 kere satın almayı karşılayacak para var ise). Kısacası True ise çizdir, False ise çizdirme işini yapıyor. False ise sayaç değişkenimi arttırıyor ve sayaç 100 olursa geri True'a dönüyor.
# 6. Bölüm
```sh
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
```
Bu kod dizisinde oyuncunun canını, mermisini, parasını, bölümünü yazdırıyorum. Canının seviyesine göre rengi değiştiyor.

# 7. Bölüm
```sh
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
```
Mouse sol click yapılınca trigonometrik hesaplarla ateş etmesini sağladım. Ve mermi_listesi'ne ekledim

# 8. Bölüm
```sh
for mermi in mermi_listesi:
    mermi.ciz(ekran)
    test = mermi.delete()           
    if test == True:
        try:
            mermi_listesi.remove(mermi)
        except:
            pass
```
Mermi listemdeki mermilerin yeni konumlarını hesaplayıp çizdirdim. Mermiler ekrandan dışarı çıkmasını kontrol ettim (.delete()) eğer çıkmışsa sildim.

# 9. Bölüm
```sh
for bulletim in mermi_listesi:
    for zombim in zombi_listesi:
        if zombim.x_kor  <= bulletim.x_kor <= zombim.x_kor + 2*zombim.r and zombim.y_kor <= bulletim.y_kor <= zombim.y_kor + 2*zombim.r:
            zombim.can -= kare.hasar
            try:
                mermi_listesi.remove(bulletim)
            except:
                pass
```
Mermilerin zombilerle çarpışmasını kontrol ettim. Eğer çarpışıyorsa mermiyi silip zombiye de hasar verilmesini sağladım.

# 10. Bölüm
```sh
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
```
Zombilerin trigonometri hesaplarıyla oyuncuya doğru hareket etmesini sağladım. Ayrıca eğer oyuncu ile çarpışıyorsa zombi kendini yok ediyor ve oyuncuya hasar veriyor.

# 11. Bölüm
```sh
reload_yapiyormu = reloadfunc()
if reload_yapiyormu == True:
    sarjorsayisi = fontum.render('Sarjor Yenileniyor', False, (51, 0, 0))
    ekran.blit(sarjorsayisi,(int(ekran_gen/2),int(ekran_yuk/2)))    
movementfunc()
```
reloadfunc() = Şarjordeki mermi sayısı eğer 0 ise True değeri döner.
Sonraki satırda da eğer true dönmüşse, "Sarjor Yenileniyor" yazdırıyor.
movementfunc() = Oyuncunun WASD hareketini sağlıyor.

# 12. Bölüm
```sh
def reloadfunc():
    if kare.sarjor == 0 and kare.sarjor_bekleme_sure <60:
        kare.sarjor_bekleme_sure += 1
        return True
    elif kare.sarjor == 0 and kare.sarjor_bekleme_sure >= 10:
        kare.sarjor = kare.max_sarjor
        kare.sarjor_bekleme_sure = 0
```
Reloadfunc(), eğer mermi kalmadıysa bekleme süresi ile gecikmeli şarjor yenilemeye yarıyor.
# 13. Bölüm
```sh
```