# Spectra, by Garrett St. Amand
#
#A lot of credit goes to Simon Hjortshoj, the author of the pygame "Zombie Shooter" http://www.pygame.org/project-Zombie+Shooter-2771-4485.html. I mirrored many aspects of his project's layout.
#
#Thanks to Timothy Downs for sharing his inputbox online, used for submitting high score initials.
#
#Credit to phobi, wubitog, Skorpio, Osmic and Naks Rifati from opengameart.org for the images and Kenney.nl and Szymon Matuszewski for sound fx. Even if their art isn't in the finalized version, it helped development immensely
#

import pygame, sys, PyHandler, math, PostScreen, MainMenu, Background, Settings, os

class Main:

    def __init__(self):
        pygame.display.set_caption('Spectra')
        self.Game = PyHandler.Main()
        self.Game.pathWork = os.getcwd()
        self.Game.display = pygame.display.set_mode((800, 600))
        self.Clock = pygame.time.Clock()
        self.framerate = 60
        self.Game.pathImg = os.path.join(self.Game.pathWork, "images")
        self.Game.pathSound = os.path.join(self.Game.pathWork, "sounds")
        background = os.path.join(self.Game.pathImg, "background.png")
        self.Game.screen = Background.Background(background, [0,0])
        self.Game.scene = 2
        self.PostScreen = PostScreen.PostScreen()
        self.MainMenu = MainMenu.MainMenu()
        self.Settings = Settings.Settings()
        self.Game.volume = .5
        backgroundmusic = os.path.join(self.Game.pathSound, "background.ogg")
        pygame.mixer.music.load(backgroundmusic)
        pygame.mixer.music.play(-1, 0)
        pygame.mixer.music.set_volume(float(self.Game.volume) / 10)


    def main_loop(self):
        while True:

            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            self.Clock.tick(self.framerate)
            fps = self.Clock.get_fps()

            if self.Game.scene == 1: #main game
                self.Game.display.fill([255, 255, 255])
                self.Game.display.blit(self.Game.screen.image, self.Game.screen.rect)
                self.Game.controller(fps, events) 
            if self.Game.scene == 0: #go to upgrade select screen, on return set wave health and player health
                self.Game.display.fill([255, 255, 255])
                self.Game.display.blit(self.Game.screen.image, self.Game.screen.rect)
                self.Game.upgrade.append(self.PostScreen.controller(self.Game.display, self.Game.level))
                self.Game.scene = 1
                self.Game.level += 1
                self.Game.wave_health = math.sqrt(self.Game.level * 2) * 20
                self.Game.health = 100
            if self.Game.scene == 2: #main menu
                self.Game.scene, self.Game.volume = self.MainMenu.controller(self.Game.display)
                self.Game.update_settings(self.Game.volume)
                pygame.mixer.music.set_volume(float(self.Game.volume) / 100)
                
                

            pygame.display.update()

            
 
        
            

if __name__=='__main__':
    main = Main()
    main.main_loop()
