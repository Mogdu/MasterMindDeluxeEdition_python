
import pygame
from pygame.locals import*

pygame.init()


def collisionTest(coord, hitbox):
    return hitbox[0] <= coord[0] <= hitbox[2] and hitbox[1] <= coord[1] <= hitbox[3]

spriteListe = []
def dessinePion(nb, coord):
     sprite = pygame.sprite()
     sprite.image = pygame.image.load("pion"+str(nb)+".jpg").convert()
     sprite.rect = sprite.image.get_rect()
     sprite.rect.topleft = coord
     spriteListe.append(sprite)




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
        #pygame.draw.rect(self.screen, (255, 255, 255),
        #                 [(self.size[0]-4*taillePions)//2 - 2, 20, 4*taillePions + 5, taillePions + 5], 2)

        y = 100
        for i in range(10):
            y += taillePions
            x = 100
            for ii in range(4):
                pygame.draw.rect(self.screen, (255, 255, 255),
                               [x, y, taillePions, taillePions], 2)

                x += taillePions



        ## .get_rect()

        # --- Go ahead and update the screen with what we've drawn.
        pygame.display.flip()


window = MainWindow()