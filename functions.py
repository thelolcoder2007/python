from block import Block
import pygame


coordinates = [100, 175, 200, 275, 300, 375, 400, 475]
pygame.init()
screen = pygame.display.set_mode([600, 600])
font = pygame.font.SysFont("Calibri Regular.ttf", 100)

def generateNewBlock(blokje):
    blok = Block()
    if blokje[blok.posY][blok.posX] != None:
        generateNewBlock(blokje)
    else:
        blokje[blok.posY][blok.posX] = blok
    return blokje

def render(x, y, blokje):
    global font
    if blokje[y][x] != None:
        posx = coordinates[blokje[y][x].posX * 2 - 2]
        posy = coordinates[blokje[y][x].posY * 2 - 2]
        img = font.render(str(blokje[y][x].value), True, (255,255,0))
        screen.blit(img, (posx, posy))
    return blokje

def goup(blokje):
    for j in range(4):
        for i in range(4):
            if blokje[j][i] == None:
                blokje[j][3-i] = blokje[j][i]
                blokje[j][3-i] = None
    print('up')
    return blokje

def godown(blokje):
    print('down')
    return blokje

def goleft(blokje):
    print('left')
    return blokje

def goright(blokje):
    print('right')
    return blokje

def renderbg():
    global screen
    pygame.Surface.fill(screen, (255,255,255))
    for i in range(0,8,2):
        for j in range(0,8,2):
            pygame.draw.rect(screen, (0,0,0), (coordinates[i], coordinates[j], coordinates[i+1]-coordinates[i], coordinates[j+1]-coordinates[j]))