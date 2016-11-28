
import pygame

class Dreadnought_Laser:
    
    def __init__(self, x, y):
        
        self.speed = 3
        self.value = 2
        self.x = x + 25
        self.y = y + 115
        self.name = 'Laser'
        self.dodge = False
        self.radius = 1
