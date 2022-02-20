import random

class Block():
    def __init__(self, startposX=None, startposY=None, value=None):
        if startposX == None:
            startposX = random.randint(1,4) - 1
        self.posX = startposX
        if startposY == None:
            startposY = random.randint(1,4) - 1
        self.posY = startposY
        if value == None:
            value = random.choice([2,2,2,2,2,2,4])
        self.value = value
    
    def move(self, x,y):
        self.posX = x
        self.posY = y

