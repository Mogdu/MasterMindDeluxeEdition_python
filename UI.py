
import pygame
from pygame.locals import*

class MainWindow:

    size = []
    screen = None

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
            for event in pygame.event.get():  # User did something
                if event.type == pygame.QUIT:  # If user clicked close
                    done = True  # Flag that we are done so we exit this loop
                elif event.type == VIDEORESIZE:
                    self.size = [event.w, event.h]
                    self.printScreen()
                    pygame.display.update()


        pygame.quit()


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