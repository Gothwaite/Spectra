
import pygame, sys, os
from pygame.locals import *

class Settings:
    
    def __init__(self):
        pathWork = os.getcwd()
        pathImg = os.path.join(pathWork, os.path.join("images", "Settings.png"))
        self.background = self.background = pygame.image.load(pathImg)
        self.font = pygame.font.SysFont("Arial", 30)
        
    def controller(self, display, volume):
        while True:
            display.blit(self.background,(0, 0))
            display.blit(self.font.render('%d' % volume, 0, (0,0,0)), (388,240))
            pygame.display.update()
            events = pygame.event.get()
            pygame.mixer.music.set_volume(float(volume) / 100) ##temporary, .2
            for event in events:
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[0]: 
                    mouse = pygame.mouse.get_pos()
                    if mouse[0] < 375 and mouse[0] > 345 and mouse[1] < 275 and mouse[1] > 240:
                        if volume > 0:
                            volume -=1
                    if mouse[0] < 450 and mouse[0] > 420 and mouse[1] < 275 and mouse[1] > 240:
                        if volume < 10:
                            volume +=1
                    if mouse[0] < 465 and mouse[0] > 335 and mouse[1] < 520 and mouse[1] > 490:
                        return volume
        
        

        