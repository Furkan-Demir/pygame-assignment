import pygame
def Player_Movement(player,grass_yerleri,ekran,camera):
    engel_tespit = CheckMove(player,grass_yerleri)
    if player.block == False and player.jump == False:
        player.y += 2

    keys = pygame.key.get_pressed()
    if keys[pygame.K_d] and keys[pygame.K_a] == 0:
        player.run("+x",ekran,camera,engel_tespit)
    if keys[pygame.K_a] and keys[pygame.K_d] == 0:
        player.run("-x",ekran,camera,engel_tespit)
    if keys[pygame.K_w] and player.jump == False and player.block == True:
        player.jump_func(ekran,camera)
    if player.jump == True:
        player.jump_func(ekran,camera)
    if keys[pygame.K_a] == 0 and keys[pygame.K_d] == 0:
        player.stop(ekran,camera)
    if keys[pygame.K_a] == 1 and keys[pygame.K_d] == 1:
        player.stop(ekran,camera)


def CheckMove(player,grass_yerleri):
    player.alan[0] = set([t for t in range(player.x,player.x+34)])
    player.alan[1] = set([t for t in range(player.y,player.y+40)])
    checked = [ ]
    gravity_sayisi = 0
    
    for i in grass_yerleri:
        if Gravity_Check(i,player) == True:
            gravity_sayisi += 1
        if i[0][0] <= player.x <= i[0][-1]  and (player.alan[1] & i[1]):
            checked.append("-x")
        if i[0][0] <= player.x +33 <= i[0][-1] and player.alan[1] & i[1]:
            checked.append("+x")
        if player.alan[0] & i[2] and set(sorted(player.alan[1])[0:2]) & i[1]:
            player.jump = False
            player.jump_time = 0
            player.block = False
    if gravity_sayisi == 0:
        player.block = False
    else:
        player.block = True
        
    return checked
def Gravity_Check(i,player):
    playery = set([t for t in range(player.y-3,player.y+42)])
    if player.alan[0] & i[2] and playery & i[1]:
        return True