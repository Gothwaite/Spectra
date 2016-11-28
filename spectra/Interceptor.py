



import pygame, random, os
from pygame.locals import *

class Interceptor:

    def __init__(self, x=random.randrange(25, 775), y=random.randrange(-250, -100)):
        self.value = 1
        self.name = 'Interceptor'
        self.radius = 7
        self.speed = 1
        self.health = 5
        self.x = x
        self.y = y
        self.dodge = False
        pathWork = os.getcwd()
        pathImg = os.path.join(pathWork, os.path.join("images", "interceptor.png"))
        img = pygame.image.load(pathImg)
        self.img = pygame.transform.rotate(img, 180)

        
