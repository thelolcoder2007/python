import functions
import pygame
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
                blokje = functions.goleft(blokje)
            elif event.key == pygame.K_RIGHT:
                blokje = functions.goright(blokje)
    functions.renderbg()
    for y in range(4):
        for x in range(4):
            blokje = functions.render(x, y, blokje)
    pygame.display.flip()


pygame.quit()