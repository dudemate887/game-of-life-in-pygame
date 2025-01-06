import math
import numpy as np
import pygame

def countNeighbors(x, y, coord, rectSize):
    nAliveAround = 0
    if x - rectSize == coord[0] and y == coord[1]:  #Left
        nAliveAround += 1
    if x + rectSize == coord[0] and y == coord[1]:  #Right
        nAliveAround += 1
    if x - rectSize == coord[0] and y - rectSize == coord[1]: #Top left
        nAliveAround += 1
    if x == coord[0] and y - rectSize == coord[1]: #Top
        nAliveAround += 1
    if x + rectSize == coord[0] and y - rectSize == coord[1]: #Top right
        nAliveAround += 1
    if x - rectSize == coord[0] and y + rectSize == coord[1]: #Bottom left
        nAliveAround += 1
    if x == coord[0] and y + rectSize == coord[1]: #Bottom
        nAliveAround += 1
    if x + rectSize == coord[0] and y + rectSize == coord[1]: #Bottom right
        nAliveAround += 1
    
    return int(nAliveAround)


# pygame setup
pygame.init()
screenSize = (1920, 1080)
screen = pygame.display.set_mode(screenSize)
clock = pygame.time.Clock()
running = True
playSim = False
generation = 0

#Font stuff
genCountFont = pygame.font.SysFont('Arial', 30)

rectCoords = []
rectSize = 20

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONUP:
            newCoordX, newCoordY = pygame.mouse.get_pos()
            newSnappedCoordX = math.floor(newCoordX / rectSize) * rectSize
            newSnappedCoordY = math.floor(newCoordY / rectSize) * rectSize
            rectCoords.append((newSnappedCoordX, newSnappedCoordY))
            
            for oldCoord in rectCoords[:-1]:
                if newSnappedCoordX == oldCoord[0] and newSnappedCoordY == oldCoord[1]:
                    rectCoords.remove(oldCoord)
                    rectCoords.pop()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            if event.key == pygame.K_SPACE:
                playSim = True

    if playSim == True:
        cellsToKill = []
        cellsToBorn = []
        for y in np.arange(0, screenSize[1], rectSize):
            for x in np.arange(0, screenSize[0], rectSize):
                isAlive = False
                for coord in rectCoords:
                    if x == coord[0] and y == coord[1]:
                        isAlive = True
                if isAlive == True:
                    totalAround = 0
                    for coord in rectCoords:
                        totalAround += countNeighbors(x, y, coord, rectSize)
                    if totalAround < 2 or totalAround > 3:
                        cellsToKill.append((x, y))


                if isAlive == False:
                    totalAround = 0
                    for coord in rectCoords:
                        totalAround += countNeighbors(x, y, coord, rectSize)
                    if totalAround == 3:
                        cellsToBorn.append((x, y))
                        isAlive = True

        for cell in cellsToKill:
            rectCoords.remove(cell)
        for cell in cellsToBorn:
            rectCoords.append(cell)
                
    
    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")

    for i in rectCoords:
        pygame.draw.rect(screen, "white", pygame.Rect(i, (rectSize, rectSize)))

    genCount = genCountFont.render("Generation " + str(generation), False, (255, 255, 255))
    screen.blit(genCount, (0,0))

    # flip() the display to put your work on screen
    pygame.display.flip()
    if playSim:
        generation += 1
        clock.tick(3)
    else:
        clock.tick(60)

pygame.quit()