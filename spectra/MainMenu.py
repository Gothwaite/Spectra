
import pygame, sys, Upgrades, Settings, Scoreboard, os
from pygame.locals import *


class MainMenu:
    
    def __init__(self):
        pygame.font.init()
        pathWork = os.getcwd()
        pathImg = os.path.join(pathWork, os.path.join("images", "MainMenu.png"))
        self.font = pygame.font.SysFont("Comic Sans MS", 30)
        self.reg_text = pygame.font.SysFont("Arial", 14)
        self.background = self.background = pygame.image.load(pathImg)
        self.Settings = Settings.Settings()
        self.Scoreboard = Scoreboard.Scoreboard()
        self.volume = 5
    def controller(self, display):
        display.blit(self.background,(0, 0))
        pygame.display.update()
        while True:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[0]: 
                    mouse = pygame.mouse.get_pos()
                    if mouse[0] < 575 and mouse[0] > 225 and mouse[1] < 235 and mouse[1] > 185: #play
                        return 1, self.volume
                    if mouse[0] < 560 and mouse[0] > 260 and mouse[1] < 320 and mouse[1] > 275: #scoreboard
                        self.Scoreboard.controller(display)
                        display.blit(self.background,(0, 0))
                        pygame.display.update()
                    if mouse[0] < 515 and mouse[0] > 290 and mouse[1] < 420 and mouse[1] > 380: #settings
                        self.volume = self.Settings.controller(display, self.volume)
                        display.blit(self.background,(0, 0))
                        pygame.display.update()
                        
                    if mouse[0] < 480 and mouse[0] > 315 and mouse[1] < 535 and mouse[1] > 470: #quit
                        pygame.quit()
                        sys.exit()
                         
            