from block import Block
import pygame

coordinates = [100, 175, 200, 275, 300, 375, 400, 475]
pygame.init()
screen = pygame.display.set_mode([600, 600])
font = pygame.font.SysFont("Calibri Regular.ttf", 50)

def generateNewBlock(blokje):
    blok = Block()
    if blokje[blok.posX][blok.posY] != None:
        generateNewBlock()
    else:
        blokje[blok.posY][blok.posX] = blok
    return blokje

def render(x, y, blokje):
    global font
    if blokje[y][x] != None:
        posx = coordinates[blokje[y][x].posX * 2 - 2]
        posy = coordinates[blokje[y][x].posY * 2 - 2]
        img = font.render(str(blokje[y][x].value), True, (255,0,0))
        screen.blit(img, (posx, posy))
    return blokje

def goup(blokje):
    return blokje

def godown(blokje):
    print('down')
    return blokje

def goleft(blokje):
    print('left')
    return blokje

def goright(blokje):
    print('left')
    return blokje