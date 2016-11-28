
import pygame, random, os
from pygame.locals import *

class Zagg:

    def __init__(self):
        self.name = 'Zagg'
        self.value = 3
        self.radius = 20
        self.speed = 2
        self.health = 8
        self.dodge = 100
        self.direction = -2
 
        self.x = random.randrange(125, 675)
        self.y = random.randrange(-250, -100)
        pathWork = os.getcwd()
        pathImg = os.path.join(pathWork, os.path.join("images", "zagg.png"))
        img = pygame.image.load(pathImg)
        self.img = pygame.transform.scale(img, (self.radius*2, self.radius*2))
        

