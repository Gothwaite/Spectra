
import pygame, Shots, Enemies, math, time, csv, inputbox, os
from pygame.locals import *
from Explosion import Explosion
from SpriteSheet import spritesheet
from pygame.examples.aliens import Score


pygame.mixer.pre_init(44100, -16, 2, 512)
pygame.mixer.init()
pygame.init()
    

class Main:

    def __init__(self):
        
        self.shoot_from = (400, 625)
        self.mouse = (0,0)
        self.shooting = False
        self.Shoot = Shots.Shoot()
        self.Enemies = Enemies.Enemies()
        self.shotsGroup = []
        self.enemiesGroup = []
        self.level = 1
        self.explosions = []
        self.health = 100
        self.score = 0
        self.upgrade = []
        self.total_score = 0
        self.wave_health = 20 * math.sqrt(self.level * 2)
        self.game_over_text = pygame.font.SysFont("Arial", 100)
        self.score_text = pygame.font.SysFont("Arial", 30)


    def controller(self, fps, events): #handles everything for gameplay
        self.check_wave_hp()
        self.applyUpgrades()
        self.collisionDetection()
        self.checkEvents(events)
        self.updateShoot(events)
        self.updateEnemies()
        self.draw_objects()
        self.updateUI()
        self.updateBarrel()
        
    def update_settings(self, volume):
        self.Shoot.change_volume(volume)

    def draw_objects(self): #draws lasers, enemies, and explosions
        for laser in self.shotsGroup:
            pygame.draw.line(self.display, laser.color, (laser.sx, laser.sy), (laser.ex, laser.ey), laser.width)      
        for enemy in self.enemiesGroup:
            if enemy.name == 'Laser':
                pygame.draw.line(self.display, (255, 0, 0,), (enemy.x, enemy.y), (enemy.x, enemy.y + 25), 5)  
            else:
                self.display.blit(enemy.img,((enemy.x-enemy.radius), (enemy.y-enemy.radius)))

                
        for explosion in self.explosions:
            if len(explosion.img) == 0: #removes explosion after last frame
                self.explosions.remove(explosion)
            else:
                self.display.blit(explosion.img[0],((explosion.x), (explosion.y)))
                explosion.img.remove(explosion.img[0])
        
    def updateUI(self): #updates the wave health bar and the player health bar
        health_bar_x = (((self.health) * (155 - 38)) / (100)) + 38
        wave_bar_x = (((self.wave_health) * (783 - 665)) / (math.sqrt(self.level * 2) * 20)) + 665
        pygame.draw.line(self.display, (255, 0, 0), (38, 570), (health_bar_x, 570), 19)
        pygame.draw.line(self.display, (255, 0, 0), (665, 570), (wave_bar_x, 570), 19)
        
    def check_wave_hp(self): #checks player health and wave health for 0
        if self.health <= 0:
            self.game_over()
        if self.wave_health <= 0:
            self.total_score += self.score
            self.score = 0
            self.scene = 0
            self.enemiesGroup[:] = []
            self.shotsGroup[:] = []
                
    def game_over(self): #game over sequence. checks score vs high score board and allows input if score is high enough. resets everything and goes back to menu afterwards.
        self.total_score += self.score
        self.score = 0
        self.enemiesGroup[:] = []
        self.shotsGroup[:] = []
        self.display.blit(self.game_over_text.render('GAME OVER', 0, (255,255,255)), (90,100))
        self.display.blit(self.score_text.render('SCORE: %d' % (self.total_score * 1000), 0, (255,255,255)), (90,250))
        pathData = os.path.join(self.pathWork, os.path.join("data", "scoreboard.csv"))
        with open(pathData, 'r') as file:
            reader = csv.reader(file)
            score_list = list(reader)
            score_list = sorted(score_list, key=lambda x: int(x[1]))
            if int(self.total_score * 1000) > int(score_list[0][1]):
                initials = inputbox.ask(self.display, "High Score! Enter Initials")
                score_list.pop(0)
                score_list.append([initials, self.total_score * 1000])
                file.close()
                with open(pathData, 'wb') as file:
                    writer = csv.writer(file)
                    writer.writerows(score_list)
                    file.close()
        pygame.display.update()
        self.total_score = 0
        self.level = 1
        self.Shoot.tears = 450 #tears is shot frequency
        self.Shoot.damage = 3
        self.Shoot.speed = 100
        self.Shoot.width = 5
        self.wave_health = 20
        self.health = 100
        self.scene = 2
    
    def applyUpgrades(self): #after postscreen this applies the upgrades to the players weapon
        for upgrade in self.upgrade:
            self.Shoot.damage += int(upgrade.damage)
            self.Shoot.speed -= int(upgrade.speed)
            self.Shoot.width += int(upgrade.width)
            self.Shoot.tears -= int(upgrade.tears)
            self.upgrade[:] = []
            if self.Shoot.speed < 20:
                self.Shoot.speed = 20
            if self.Shoot.damage < 1:
                self.Shoot.damage = 1
        

    def updateShoot(self, events):
        self.shotsGroup = self.Shoot.controller(self.shoot_from, pygame.mouse.get_pos(), self.shooting)

    def updateEnemies(self):
        self.enemiesGroup = self.Enemies.controller(self.level)
        
    def collisionDetection(self): #checks for collisions and kills stray lasers
        for enemy in self.enemiesGroup:
            if enemy.y > 525:
                self.explosions.append(Explosion(enemy.x, enemy.y))
                self.enemiesGroup.remove(enemy)
                self.health -= 10
            
        for laser in self.shotsGroup:
            if laser.ex < -100 or laser.ex > 900 or laser.ey < -100:
                self.shotsGroup.remove(laser) #kill strays
            for enemy in self.enemiesGroup:
                if abs(enemy.x - laser.ex) - laser.width/2 < enemy.radius and enemy.name != 'Laser':
                    if abs(enemy.y - laser.ey) < enemy.radius:
                        self.explosions.append(Explosion(laser.ex, laser.ey))
                        enemy.health -= laser.damage
                        try:
                            self.shotsGroup.remove(laser)
                        except ValueError:
                            continue
                        
                        if enemy.health <= 0:
                            self.explosions.append(Explosion(enemy.x, enemy.y))
                            self.enemiesGroup.remove(enemy)
                            self.wave_health -= enemy.value
                            self.total_score += enemy.value

    def updateBarrel(self): #makes the gun barrel follow the mouse and draws it
        self.mouse = pygame.mouse.get_pos()
        try:
            slope = float(self.shoot_from[1]-self.mouse[1]) / float(self.mouse[0]-self.shoot_from[0])
        except ZeroDivisionError:
            slope = float('Inf')
        angle = math.atan(slope)

        if self.mouse[0] >= self.shoot_from[0]:
            x = math.cos(angle)
            y = -math.sin(angle)
        if self.mouse[0] < self.shoot_from[0]:
            x = -math.cos(angle)
            y = math.sin(angle) #using pygame.draw.line() was inadequate since the ends of the line always had either 0 or 1 as the slope. the long polygon below is hard to read but works great
        pygame.draw.polygon(self.display, (122, 122, 122), ((self.shoot_from[0] - y * 15, self.shoot_from[1] + x * 15), (self.shoot_from[0] + y * 15, self.shoot_from[1] - x * 15), (self.shoot_from[0] + x*85 + y * 15, self.shoot_from[1] + y*85 - x * 15), (self.shoot_from[0] + x*85 - y * 15, self.shoot_from[1] + y*85 + x * 15)))
    
        
        

    def checkEvents(self, events):
        for event in events:
            if event.type == MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[0]:  
                self.shooting = True
            elif event.type == MOUSEBUTTONUP:
                self.shooting = False
                
