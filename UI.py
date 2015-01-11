
import pygame
from pygame.locals import*


class Collidable:
    hitBox = []
    clickedFunction = None

    def __init__(self, hitBox, clickedFunction = None):
        self.hitBox = hitBox
        self.clickedFunction = clickedFunction

    def colideTest(self, coords):
        if coords[0] >= self.hitBox[0] and coords[0] <= self.hitBox[2] and \
           coords[1] >= self.hitBox[1] and coords[1] <= self.hitBox[3]:
            return True
        return False


class MainWindow:

    size = []
    screen = None
    colidables = []

    def __init__(self):
        # Define some colors
        BLACK    = (   0,   0,   0)
        WHITE    = ( 255, 255, 255)
        GREEN    = (   0, 255,   0)
        RED      = ( 255,   0,   0)

        pygame.init()

        self.size = (500, 700)
        self.screen = pygame.display.set_mode(self.size, RESIZABLE)

        pygame.display.set_caption("Mastermind")

        self.printScreen()
        done = False
        while not done:
            for e in pygame.event.get():  # User did something
                if e.type == pygame.QUIT:  # If user clicked close
                    done = True  # Flag that we are done so we exit this loop
                elif e.type == VIDEORESIZE:
                    self.size = [e.w, e.h]
                    self.printScreen()
                    pygame.display.update()
                elif e.type == MOUSEBUTTONUP:
                    self.clickColide(e.pos)


        pygame.quit()


    def clickColide(self, coords):
        for colidable in self.colidables:
            if colidable.colideTest(coords):
                colidable.clickedFunction()


    def printScreen(self):
        self.screen.fill((0, 0, 0))

        bordure = 100
        taillePions = 46
        pygame.draw.rect(self.screen, (255, 255, 255),
                         [(self.size[0]-4*taillePions)//2 - 2, 20, 4*taillePions + 5, taillePions + 5], 2)

        for i in range(10):
            pygame.draw.rect(self.screen, (255, 255, 255),
                             [(self.size[0]-4*taillePions)//2, 100 + i*taillePions, 4*taillePions, taillePions], 2)

        pygame.draw.rect(self.screen, (255, 255, 255),
                         [(self.size[0]-4*taillePions)//2, 650, 4*taillePions, taillePions], 2)

        for i in range(4):
            pygame.draw.rect(self.screen, (255, 255, 255),
                             [(self.size[0]-4*taillePions)//2 + taillePions*i, 560, taillePions, taillePions], 2)



        ## .get_rect()

        # --- Go ahead and update the screen with what we've drawn.
        pygame.display.flip()


window = MainWindow()