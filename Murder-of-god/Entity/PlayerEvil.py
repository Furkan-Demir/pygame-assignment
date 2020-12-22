import pygame
import os
current_path = os.path.dirname(__file__) # Where your .py file is located
resource_path = os.path.join(current_path, '..',"Sprites","PlayerEvil") # The resource folder path
class PlayerEvil():
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.run_img = ["1.png","2.png","3.png","4.png","5.png","6.png","7.png","8.png" ]
        self.idle_img = ["1.png","2.png","3.png","4.png","5.png","6.png","7.png","8.png" ]
        self.jump_img = ["1.png","2.png","3.png","4.png","5.png","6.png","7.png","8.png" ]
        self.run_time = 0
        self.idle_time = 0
        self.jump = False
        self.jump_time = 0
        self.jump_max_time = 60
        self.yon = "sag"
        self.block = False
        self.alan =[[],[]]

    
    def run(self,yon,ekran,camera,engel_tespit):
        if yon == "+x":
            self.yon = "sag"
            self.run_time += 0.2
            if yon not in engel_tespit:
                self.x += 3
            if self.jump == False:
                player_animation = self.run_img[int(self.run_time) % len(self.run_img)]
                player_animation = os.path.join(resource_path, 'Walk',player_animation) 
                player_animation = pygame.image.load(player_animation)
                ekran.blit(player_animation,(self.x-camera.x,self.y-camera.y))
        if yon == "-x":
            self.yon = "sol"
            self.run_time += 0.2
            if yon not in engel_tespit:
                self.x -= 3
            if self.jump == False:
                player_animation = self.run_img[int(self.run_time) % len(self.run_img)]    
                player_animation = os.path.join(resource_path, 'Walk',player_animation)
                player_animation = pygame.image.load(player_animation)              
                player_animation = pygame.transform.flip(player_animation, True, False)
                ekran.blit(player_animation,(self.x-camera.x,self.y-camera.y))
    
    def stop(self,ekran,camera):
        if self.jump == False:
            self.idle_time += 0.2
            player_animation = self.idle_img[int(self.idle_time) % len(self.idle_img)]
            player_animation = os.path.join(resource_path, 'Idle',player_animation) 
            player_animation = pygame.image.load(player_animation)
            if self.yon == "sol":
                player_animation = pygame.transform.flip(player_animation, True, False)
            ekran.blit(player_animation,(self.x-camera.x,self.y-camera.y))       

    def jump_func(self,ekran,camera):
        if self.jump_time < self.jump_max_time:
            self.jump = True
            self.jump_time += 1
            self.y -= 2
            player_animation = self.jump_img[int(self.jump_time/5) % len(self.idle_img)]
            player_animation = os.path.join(resource_path, 'Jump',player_animation) 
            player_animation = pygame.image.load(player_animation)
            if self.yon == "sol":
                player_animation = pygame.transform.flip(player_animation, True, False)
            ekran.blit(player_animation,(self.x-camera.x,self.y-camera.y))  
        else:
            self.jump_time = 0
            self.jump = False

     