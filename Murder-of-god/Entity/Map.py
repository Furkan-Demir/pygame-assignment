import pygame
import re


def map_cozumle(level):
    x_y_cimen_zemin = finda(level,"W")
    x_y_cimen = finda(level,"C")
    x_y_duvar = finda(level,"G")
    pencere = finda(level,"E")
    line_y = 0
    for i in level:
        indis = i.find("P")
        if indis != -1:
            player_yeri = [indis*32,line_y*32]
        line_y+=1
    line_y = 0  
    for i in level:
        indis = i.find("J")
        if indis != -1:
            jesus_yeri = [indis*32,line_y*32]
        line_y+=1
    
    return [x_y_cimen_zemin, player_yeri, x_y_cimen, x_y_duvar,pencere,jesus_yeri]

def map_cozumle2(level):
    x_y_cimen_zemin = finda(level,"W")
    x_y_cimen = finda(level,"C")
    x_y_duvar = finda(level,"G")
    pencere = finda(level,"E")
    line_y = 0
    for i in level:
        indis = i.find("P")
        if indis != -1:
            player_yeri = [indis*32,line_y*32]
        line_y+=1
    line_y = 0  
    for i in level:
        indis = i.find("J")
        if indis != -1:
            jesus_yeri = [indis*32,line_y*32]
        line_y+=1
    
    return [x_y_cimen_zemin, player_yeri, x_y_cimen, x_y_duvar,pencere,jesus_yeri]

def finda(level,element):
    line_y = 0
    x_y = [ ]
    for line in level:
        gecici = [ ]
        for match in re.finditer(element, line):
            gecici.append(match.start())
        for i in gecici:
            if [i*32,line_y*32] not in x_y:
                
                x_y.append([i*32,line_y*32])
        line_y+=1
    return x_y