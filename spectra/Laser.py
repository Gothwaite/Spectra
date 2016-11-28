

import math

class Laser:

    def __init__(self, laser, shoot_from, mousePos, damage, speed, width):
        
        try: # a lot of math to make the lasers travel at the correct angle
            slope = float(shoot_from[1]-mousePos[1]) / float(mousePos[0]-shoot_from[0])
        except ZeroDivisionError:
            slope = float('Inf')
        angle = math.atan(slope)
        
        if mousePos[0] >= shoot_from[0]:
            x = math.cos(angle)
            y = -math.sin(angle)
        if mousePos[0] < shoot_from[0]:
            x = -math.cos(angle)
            y = math.sin(angle)
            
        self.origin = shoot_from
        self.length = 50
        self.direction = (x, y)
        self.sx = shoot_from[0]
        self.sy = shoot_from[1]
        self.ex = shoot_from[0] + self.length * self.direction[0]
        self.ey = shoot_from[1] + self.length * self.direction[1]
        
        self.speed = speed
        self.damage = damage
        self.width = width
        
        if damage < 4: #color changes as damage increases
            self.color = (255,0,0)
        elif damage < 7:
            self.color = (255,125,0)
        elif damage < 10:
            self.color = (255,235,0)
        elif damage < 13:
            self.color = (0,255,0)
        elif damage < 16:
            self.color = (0,255,120)
        elif damage < 19:
            self.color = (0,0,255)
        elif damage < 22:
            self.color = (120,0,255)
        else:
            self.color = (255,255,255)
        
        
        

