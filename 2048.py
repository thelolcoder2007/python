import pygame
import functions
pygame.init()

screen = pygame.display.set_mode([600, 600])

blokje = [[None,None,None,None],
[None,None,None,None],
[None,None,None,None],
[None,None,None,None]]


#main game loop
blokje = functions.generateNewBlock(blokje)
blokje = functions.generateNewBlock(blokje)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                blokje = functions.goup(blokje)
            elif event.key == pygame.K_DOWN:
                blokje = functions.godown(blokje)
            elif event.key == pygame.K_LEFT:
                print("left")
            elif event.key == pygame.K_RIGHT:
                print("right")
    screen.fill((255,255,255))
    for y in range(3):
        for x in range(3):
            blokje = functions.render(x, y, blokje)
    pygame.display.flip()


pygame.quit()