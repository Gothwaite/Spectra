
import pygame,csv,random, os


class Upgrades:
    
    def __init__(self): #pulls the list of potential upgrades from a csv file
        pathWork = os.getcwd()
        pathData = os.path.join(pathWork, os.path.join("data", "upgrades.csv"))
        with open(pathData, 'rb') as file:
            reader = csv.reader(file)
            upgrade_list = list(reader)
        upgrade_list.pop(0) #first element gets popped, since it is just the key
        selected = random.randint(0, len(upgrade_list)-1)
        self.damage = upgrade_list[selected][1]
        pathImg = os.path.join(pathWork, os.path.join("images", upgrade_list[selected][5]))
        self.img = pygame.image.load(pathImg)
        self.tears = upgrade_list[selected][2]
        self.name = upgrade_list[selected][0]
        self.width = upgrade_list[selected][4]
        self.speed = upgrade_list[selected][3]
    
        