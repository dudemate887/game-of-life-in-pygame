import math
import numpy as np
import pygame

# pygame setup
pygame.init()
screenSize = (1280, 720)
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
            if event.key == pygame.K_SPACE:
                playSim = True

    if playSim == True:
        for x in np.arange(0, screenSize[0], rectSize):
            for y in np.arange(0, screenSize[1], rectSize):
                for coord in rectCoords:
                    nAliveAround = 0
                    if x - rectSize == coord[0] and y == coord[1]:  #Left
                        nAliveAround += 1
                        print(f"{x} - {rectSize} is {coord[0]}")
                    if x + rectSize == coord[0] and y == coord[1]:  #Right
                        nAliveAround += 1
                        print("foun2d")
                    if x - rectSize == coord[0] and y - rectSize == coord[1]: #Top left
                        nAliveAround += 1
                        print("fou3nd")
                    if x == coord[0] and y - rectSize == coord[1]: #Top
                        nAliveAround += 1
                        print("f4ound")
                    if x + rectSize == coord[0] and y - rectSize == coord[1]: #Top right
                        nAliveAround += 1
                        print("fou5nd")
                    if x - rectSize == coord[0] and y + rectSize == coord[1]: #Bottom left
                        nAliveAround += 1
                        print("fou6nd")
                    if x == coord[0] and y + rectSize == coord[1]: #Bottom
                        nAliveAround += 1
                        print("fou7nd")
                    if x + rectSize == coord[0] and y + rectSize == coord[1]: #Bottom right
                        nAliveAround += 1
                        print("fou8nd")

                    if x == coord[0] and y == coord[1]: #Check if it's already a cell
                        if nAliveAround < 2: #Dies from underpopulation
                            rectCoords.remove(coord)
                            print(f"{coord} dies from under from check from block {x, y}")
                        if nAliveAround == 2 or nAliveAround == 3: #Lives
                            pass
                            print("survives")
                        if nAliveAround > 3: #Dies from overpopulation
                            rectCoords.remove(coord)
                            print("dies from over")
                    elif nAliveAround == 3: #Repopulates
                        rectCoords.append((x, y))
                        print("born")
                    


    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")

    for i in rectCoords:
        pygame.draw.rect(screen, "white", pygame.Rect(i, (rectSize, rectSize)))



    # flip() the display to put your work on screen
    pygame.display.flip()
    clock.tick(10)

pygame.quit()