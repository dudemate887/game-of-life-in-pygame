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
                        rectCoords.remove((x, y))


                if isAlive == False:
                    totalAround = 0
                    for coord in rectCoords:
                        totalAround += countNeighbors(x, y, coord, rectSize)
                    if totalAround == 3:
                        rectCoords.append((x, y))
                        isAlive = True
                
                

                    

                    


    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")

    for i in rectCoords:
        pygame.draw.rect(screen, "white", pygame.Rect(i, (rectSize, rectSize)))



    # flip() the display to put your work on screen
    pygame.display.flip()
    clock.tick(10)

pygame.quit()