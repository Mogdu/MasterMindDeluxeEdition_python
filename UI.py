
import pygame
from pygame.locals import*

pygame.init()


def collisionTest(coord, hitbox):
    return hitbox[0] <= coord[0] <= hitbox[2] and hitbox[1] <= coord[1] <= hitbox[3]


def dessinePion(nb, coord, screen):
     image = pygame.image.load("pion"+str(nb)+".jpg")
     screen.blit(image, coord)


def dessineProposition(proposition, coord, screen):
    for i, pion in enumerate(proposition):
        dessinePion(pion, [coord[0]+i*45, coord[1]], screen)

def jouePion(nb):
    pass

def main():
    # Define some colors
    BLACK    = (   0,   0,   0)
    WHITE    = ( 255, 255, 255)
    GREEN    = (   0, 255,   0)
    RED      = ( 255,   0,   0)

    pygame.init()

    size = (500, 700)
    screen = pygame.display.set_mode(size, RESIZABLE)

    pygame.display.set_caption("Mastermind")

    declancheurs = []  # un declancheur est un couple hitbox / fonction

    # on dessine les pions sur lesquels on clique pour jouer
    for i in range(6):
        p = i+1
        declancheurs.append(( [100, 50+i*45, 100+45, 50+p*45], lambda: jouePion(p) ))
        dessinePion(1, [100, 50+i*45], screen)

    printScreen(screen)
    done = False
    while not done:
        for e in pygame.event.get():  # User did something
            if e.type == pygame.QUIT:  # If user clicked close
                done = True  # Flag that we are done so we exit this loop
            elif e.type == VIDEORESIZE:
                size = [e.w, e.h]
                printScreen(screen)
                pygame.display.update()
            elif e.type == MOUSEBUTTONUP:
                declancheurColision(e.pos, declancheurs)


    pygame.quit()


def declancheurColision(coords, declancheurs):
    for declancheur in declancheurs:
        if collisionTest(coords, declancheur[0]):
            declancheur[1]()


def printScreen(screen):
    screen.fill((0, 0, 0))

    bordures = [100, 100]
    taillePions = 46
    #pygame.draw.rect(self.screen, (255, 255, 255),
    #                 [(self.size[0]-4*taillePions)//2 - 2, 20, 4*taillePions + 5, taillePions + 5], 2)

    y = bordures[1]
    for i in range(10):
        y += taillePions
        x = bordures[0]
        for ii in range(4):
            pygame.draw.rect(screen, (255, 255, 255),
                             [x, y, taillePions, taillePions], 2)

            x += taillePions


    dessineProposition((1,1,1,1), bordures, screen)

    ## .get_rect()

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()


window = main()