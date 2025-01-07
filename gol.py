import math
import numpy as np
import pygame

# pygame setup
pygame.init()
screenSize = (1920, 1080)
screen = pygame.display.set_mode(screenSize, display=1)
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

    def countNeighbors(self, tiles, x, y, tileSize):
        aliveNeighbors = 0
        neighbors = []

        for tile in tiles:
            if x - tileSize == tile.x and y == tile.y:
                neighbors.append(tile)
            if x + tileSize == tile.x and y == tile.y:
                neighbors.append(tile)
            if x - tileSize == tile.x and y - tileSize == tile.y:
                neighbors.append(tile)
            if x == tile.x and y - tileSize == tile.y:
                neighbors.append(tile)
            if x + tileSize == tile.x and y - tileSize == tile.y:
                neighbors.append(tile)
            if x - tileSize == tile.x and y + tileSize == tile.y:
                neighbors.append(tile)
            if x == tile.x and y + tileSize == tile.y:
                neighbors.append(tile)
            if x + tileSize == tile.x and y + tileSize == tile.y:
                neighbors.append(tile)

        for i in neighbors:
            if i.isAlive == True:
                aliveNeighbors += 1

        return (aliveNeighbors)


    


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
                    if tile.isAlive == False:
                        tile.isAlive = True
                    else:
                        tile.isAlive = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            if event.key == pygame.K_SPACE:
                playSim = True

    to_kill = []

    if playSim == True:
        for tile in tiles:
            aliveNeighbors = tile.countNeighbors(tiles, tile.x, tile.y, tileSize)
            print(f"{tile.x}, {tile.y} has found {aliveNeighbors} tiles")
            if tile.isAlive == True:
                if aliveNeighbors < 2 or aliveNeighbors > 3:
                    to_kill.append(tile)
            else: 
                if aliveNeighbors == 3:
                    to_kill.append(tile)
            
    for tileToMake in to_kill:
        for tile in tiles:
            if tileToMake == tile:
                if tile.isAlive == False:
                    tile.isAlive = True
                else:
                    tile.isAlive = False

    
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