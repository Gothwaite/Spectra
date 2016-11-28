
import pygame, random, os


class Dreadnought:
        
    def __init__(self):
        self.health = 350
        self.value = 15
        self.y = random.randrange(-300, -100)
        self.x = random.randrange(100, 700)
        pathWork = os.getcwd()
        pathImg = os.path.join(pathWork, os.path.join("images", "dreadnought.png"))
        self.img = pygame.image.load(pathImg)
        self.speed = .5
        self.dodge = False
        self.radius = 100
        self.name = 'Dreadnought'
        self.firestatus = False
    