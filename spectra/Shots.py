

import os, pygame, math, time, random
from pygame.locals import *
from Laser import Laser

class Shoot:

    def __init__(self):
        self.shotslist = []
        self.tears = 450 #tears is shot frequency
        self.damage = 3
        self.speed = 100
        self.width = 5
        self.Clock = pygame.time.Clock()
        self.shootTime = 0
        self.positionUpdate = 0
        self.fx = 1
        pathWork = os.getcwd()
        pathSound = os.path.join(pathWork, "sounds")
        self.sound1 = pygame.mixer.Sound(os.path.join(pathSound, "laser1.ogg"))
        self.sound2 = pygame.mixer.Sound(os.path.join(pathSound, "laser2.ogg"))
        self.sound3 = pygame.mixer.Sound(os.path.join(pathSound, "laser3.ogg"))
        
        
    
    def change_volume(self, volume): #change laser volume
        self.sound1.set_volume(float(volume) / 5) 
        self.sound2.set_volume(float(volume) / 5) 
        self.sound3.set_volume(float(volume) / 5) 


    def controller(self, shoot_from, mousePos, shoot=False, laser=0): #creates new lasers and plays their sfx
        tick = self.Clock.tick()
        self.shootTime += tick
        self.positionUpdate += tick
        if shoot and self.shootTime >= self.tears:
            new_laser = Laser(laser, shoot_from, mousePos, self.damage, self.speed, self.width)
            self.shotslist.append(new_laser)
            self.fx = random.randint(1,3)
            if self.fx == 1:
                self.sound1.play()
            elif self.fx == 2:
                self.sound2.play()
            elif self.fx == 3:
                self.sound3.play()
                    
            self.shootTime = 0
            shoot = False
        if self.positionUpdate > 10:
            self.update_pos(self.positionUpdate) 
            self.positionUpdate = 0
        return self.shotslist

    def update_pos(self, deltaTime): #update the coordinates of all lasers
        for laser in self.shotslist:
            laser.sx += laser.length * laser.direction[0] * deltaTime/laser.speed
            laser.sy += laser.length * laser.direction[1] * deltaTime/laser.speed
            laser.ex += laser.length * laser.direction[0] * deltaTime/laser.speed
            laser.ey += laser.length * laser.direction[1] * deltaTime/laser.speed
            
            








