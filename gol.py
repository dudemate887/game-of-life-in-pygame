import math
import numpy as np
import pygame

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

class Cell:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.isAlive = False
    


tileSize = 10
tiles = []

# initialize the tiles
for y in np.arange(0, screenSize[1], tileSize):
    for x in np.arange(0, screenSize[0], tileSize):
        tiles.append(Cell(x, y))


while running:

    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONUP:
            newCoordX, newCoordY = pygame.mouse.get_pos()
            newSnappedCoordX = math.floor(newCoordX / tileSize) * tileSize
            newSnappedCoordY = math.floor(newCoordY / tileSize) * tileSize
            for tile in tiles:
                if tile.x == newSnappedCoordX and tile.y == newSnappedCoordY:
                    tile.isAlive = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            if event.key == pygame.K_SPACE:
                playSim = True

    
    to_make = []
    to_kill = []

    if playSim == True:
        pass
                
    
    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")

    for tile in tiles:
        if tile.isAlive == True:
            pygame.draw.rect(screen, "white", pygame.Rect((tile.x, tile.y), (tileSize, tileSize)))

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