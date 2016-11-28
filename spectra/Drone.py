
import pygame, random, os


class Drone:

    def __init__(self):
        self.value = 1
        self.name = 'Drone'
        self.radius = 30
        self.speed = 1
        self.health = 8
        self.x = random.randrange(25, 775)
        self.y = random.randrange(-250, -100)
        self.dodge = False
        pathWork = os.getcwd()
        pathImg = os.path.join(pathWork, os.path.join("images", "drone.png"))
        img = pygame.image.load(pathImg)
        self.img = pygame.transform.scale(img, (self.radius*2, self.radius*2))
        
