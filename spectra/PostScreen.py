

import pygame, sys, Upgrades, os
from pygame.locals import *


class PostScreen:
    
    def __init__(self):
        pygame.font.init()
        self.font = pygame.font.SysFont("Comic Sans MS", 30)
        self.reg_text = pygame.font.SysFont("Arial", 14)
        self.pathWork = os.getcwd()
        pathImg = os.path.join(self.pathWork, os.path.join("images", "background.png"))
        self.background = pygame.image.load(pathImg)
        
        
    def controller(self, display, level): #draws the two random upgrade options and returns one when clicked on
        display.blit(self.font.render('Congratulations, you beat wave %d!' % level, 0, (255,255,255)), (0,0))
        option_1 = Upgrades.Upgrades()
        option_2 = Upgrades.Upgrades()
        pathImg = os.path.join(self.pathWork, os.path.join("images", "upgrade_select_bg.png"))
        display.blit(pygame.image.load(pathImg), (200, 150))
        display.blit(option_1.img,(240, 250))
        display.blit(option_2.img,(460, 250))
        display.blit(self.reg_text.render('%s' % option_1.name, 0, (0,0,0)), (235, 372))
        display.blit(self.reg_text.render('%s' % option_2.name, 0, (0,0,0)), (455, 372))
        pygame.display.update()
        while True:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[0]: 
                    mouse = pygame.mouse.get_pos()
                    if mouse[0] < 340 and mouse[0] > 240 and mouse[1] < 350 and mouse[1] > 250:
                        return option_1
                    if mouse[0] < 560 and mouse[0] > 460 and mouse[1] < 350 and mouse[1] > 250:
                        return option_2
                         
            
            
    