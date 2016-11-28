
import pygame, Zagg, Drone, random, Carrier, Interceptor, math, Dreadnought, Dreadnought_Laser
from pygame.locals import *


class Enemies:

    def __init__(self):
        self.enemieslist = []
        self.Clock = pygame.time.Clock()
        self.enemieslist = []
        self.spawnTime = 4000
        self.positionUpdate = 0
        self.wave_difficulty = 0

    def controller(self, level):
        tick = self.Clock.tick()
        self.spawnTime += tick
        self.positionUpdate += tick
        if self.spawnTime > 5000:
            for enemy in self.enemieslist: #check to see if ship should be firing right now
                if hasattr(enemy, 'firestatus'):
                    if enemy.firestatus == True:
                        self.enemy_fire(enemy)
            self.spawn_enemies(level)
        if self.positionUpdate > 10:
            self.update_pos(self.positionUpdate)
            self.positionUpdate = 0

                
        return self.enemieslist

    def enemy_fire(self, enemy): 
        new_laser = Dreadnought_Laser.Dreadnought_Laser(enemy.x, enemy.y)
        self.enemieslist.append(new_laser)
    
    def update_pos(self, deltaTime): #moves all the ships downwards
        for enemy in self.enemieslist:
            if enemy.name != 'Dreadnought' or enemy.y < 100:
                enemy.y += enemy.speed
                if enemy.dodge:
                    enemy.x += enemy.direction
                    enemy.dodge += enemy.direction
                    if enemy.dodge == 0 or enemy.dodge == 200:
                        enemy.direction = enemy.direction * -1
                        enemy.dodge = 100
            else:
                enemy.firestatus = True
                    
    def spawn_enemies(self, level): #spawn enemies at the top, and interceptors at the carriers
        self.wave_difficulty += random.randint(2,4) * level
        for enemy in self.enemieslist:
            if enemy.name == 'Carrier':
                new_enemy = Interceptor.Interceptor(enemy.x + 10, enemy.y + enemy.radius)
                self.enemieslist.append(new_enemy)
                new_enemy = Interceptor.Interceptor(enemy.x - 15, enemy.y + enemy.radius)
                self.enemieslist.append(new_enemy)
        for point in range(self.wave_difficulty // 40):
            new_enemy = Dreadnought.Dreadnought()
            self.enemieslist.append(new_enemy)      
            self.wave_difficulty = self.wave_difficulty % 40
        for point in range(self.wave_difficulty // 16):
            new_enemy = Carrier.Carrier()
            self.enemieslist.append(new_enemy)      
            self.wave_difficulty = self.wave_difficulty % 16
        for point in range(self.wave_difficulty // 3):
            new_enemy = Zagg.Zagg()
            self.enemieslist.append(new_enemy)
            self.wave_difficulty = self.wave_difficulty % 3
        for point in range(self.wave_difficulty // 1):
            new_enemy = Drone.Drone()
            self.enemieslist.append(new_enemy)
        self.wave_difficulty = 0
        self.spawnTime = 0
                    
            
    
