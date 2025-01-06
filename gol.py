import math
import numpy
import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

rectCoords = []
rectSize = (20, 20)

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONUP:
            newCoordX, newCoordY = pygame.mouse.get_pos()
            newSnappedCoordX = math.floor(newCoordX / rectSize[0]) * rectSize[0]
            newSnappedCoordY = math.floor(newCoordY / rectSize[0]) * rectSize[0]
            rectCoords.append((newSnappedCoordX, newSnappedCoordY))
            
            for oldCoord in rectCoords[:-1]:
                if newSnappedCoordX == oldCoord[0] and newSnappedCoordY == oldCoord[1]:
                    rectCoords.remove(oldCoord)
                    rectCoords.pop()

    

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")

    for i in rectCoords:
        pygame.draw.rect(screen, "white", pygame.Rect(i, rectSize))



    # flip() the display to put your work on screen
    pygame.display.flip()
    clock.tick(10)

pygame.quit()