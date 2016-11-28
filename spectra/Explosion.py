
import pygame, os
from pygame.locals import *
import SpriteSheet

class Explosion:

    def __init__(self, x, y):

        self.x = x - 16
        self.y = y - 16
        pathWork = os.getcwd()
        pathImg = os.path.join(pathWork, os.path.join("images", "explosion2.png"))
        img = pygame.image.load(pathImg)
        self.img = SpriteSheet.spritesheet(pathImg)
        frames = []
        for n in range(0,8): #this code handles spritesheets, turning them into a list of images that can be cycled through to create animations
            top = 32*n
            for i in range(0,3):
                left = 32*i
                width = 32
                height = 32
                frames.append(pygame.Rect(left, top, width, height))
        self.img = self.img.images_at(frames, (0,0,0))
