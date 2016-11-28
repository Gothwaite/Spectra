
import pygame, sys, csv, os
from pygame.locals import *

class Scoreboard:
    
    def __init__(self):
        self.pathWork = os.getcwd()
        pathImg = os.path.join(self.pathWork, os.path.join("images", "Scoreboard.png"))
        self.background = pygame.image.load(pathImg)
        self.font = pygame.font.SysFont("Arial", 30)
        
    def controller(self, display):
        pathData = os.path.join(self.pathWork, os.path.join("data", "scoreboard.csv"))
        with open(pathData, 'r') as file:
            reader = csv.reader(file)
            score_list = list(reader)
        y = 0
        display.blit(self.background,(0, 0))
        score_list = sorted(score_list, key=lambda x: int(x[1]), reverse=True)
        for score in score_list: #draws the top scores, each one lower than the one before
            display.blit(self.font.render('%s   %s' % (score[0], score[1]), 0, (0,0,0)), (330, 250 + 40 * y))
            y+=1 
        pygame.display.update()
        
        while True:
            
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[0]: 
                    mouse = pygame.mouse.get_pos()
                    if mouse[0] < 465 and mouse[0] > 335 and mouse[1] < 520 and mouse[1] > 490:
                        return
        
        
