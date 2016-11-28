
import pygame,random, os

class Carrier:
    
    def __init__(self):
        self.health = 100
        self.value = 10
        self.y = random.randrange(-250, -100)
        self.x = random.randrange(100, 700)
        pathWork = os.getcwd()
        pathImg = os.path.join(pathWork, os.path.join("images", "carrier.png"))
        img = pygame.image.load(pathImg)
        self.img = pygame.transform.rotate(img, 180)
        self.speed = .5
        self.dodge = False
        self.radius = 80
        self.name = 'Carrier'
    