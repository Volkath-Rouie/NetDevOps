# minute = str(timedate.now())[11:13]
# miles = str(timedate.now())[14:16]

from datetime import datetime;from sleep import sleep;import random

class cat(object):
    def __init__(self):
        self.x = random.randint(0, 10)
        self.y = random.randint(0, 10)
        self.energy = 1000
    
    def action(self):
        self.x = validnize(self.x + random.randint(-2, 2))
        self.y = validnize(self.y + random.randint(-2, 2))
    
    def validnize(self,location):
        if location < 0:
            return abs(location)
        elif location > 10:
            return 20 - location
        else:
            return location
    
    def rewards(self):
        self.energy += 50


class mouse(object):
    def __init__(self):
        self.x = random.randint(0, 10)
        self.y = random.randint(0, 10)
    
    def action(self):
        self.x = validnize(self.x + random.randint(-1, 1))
        self.y = validnize(self.x + random.randint(-1, 1))

    def validnize(self,location):
        if location < 0:
            return abs(location)
        elif location > 10:
            return 20 - location
        else:
            return location

def experiment():
    Catcher = cat()
    Escaper = []
    for cycle0 in range(20):Escaper.append(mouse)
    while True:
        if len(Escaper) <= 0:
            print('Action ')
