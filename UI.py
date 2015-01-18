
import pygame
from pygame.locals import*
import TourDeJeu
import Initialisations
import Sauvegarde




# variables globales
# ces variables sont appele par des fonctions declanche par l'utilisateur.
# en faire des variables global simplifient l'appele de ces fonctions
screen = None
proposition = []  # liste de nombres entiers
oldPropositions = []  # liste de couple enciennes proposition / resultat assoscie
aDeviner = []  # la proposition a deviner
secret = True
declancheurs = []
images = []

# constantes globales:
bordures = [60, 100]
taillePions = 45
# custom events prevu par pygames:
WINEVENT = USEREVENT+1
LOSEEVENT = USEREVENT+2
TOMENUEVENT = USEREVENT+3
NOUVELLEPARTIEEVENT = USEREVENT+4
CONTINUEPARTIEEVENT = USEREVENT+5








# fonction d'entree
def main():
    pygame.init()

    size = (500, 700)
    global screen
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Mastermind")

    creerMenu()
    boucleGenerale()

    pygame.quit()



def creerMenu():
    global declancheurs
    declancheurs = []  # un declancheur est un couple hitbox / fonction

    screen.fill((192, 192, 192))

    declancheurs.append(( [100, 100, 400, 150], lambda: pygame.event.post(pygame.event.Event(NOUVELLEPARTIEEVENT)) ))
    screen.blit(pygame.image.load("nouvellePartie.png"), [100, 100])

    declancheurs.append(( [100, 200, 400, 250], lambda: pygame.event.post(pygame.event.Event(CONTINUEPARTIEEVENT)) ))
    screen.blit(pygame.image.load("continuer.png"), [100, 200])

    declancheurs.append(( [100, 300, 400, 350], lambda: pygame.event.post(pygame.event.Event(QUIT)) ))
    screen.blit(pygame.image.load("quiter.png"), [100, 300])
    pygame.display.flip()


def partie():
    global images, declancheurs, proposition, secret
    secret = True
    images = []  # les couples url, coordones de toutes les images
    declancheurs = []  # un declancheur est un couple hitbox / fonction

    # on place les boutons pour choisire les pions
    for i in range(6):
        x = bordures[0]+i*taillePions
        y = bordures[1]
        p = i+1
        # un petit peut laid, mais permet de passer la valeur de p a cet instant
        declancheurs.append(( [x, y, x+taillePions, y+taillePions], eval("lambda: proposition.append("+str(p)+")") ))
        images.append(("pion"+str(p)+".png", [x, y]))

    # les autres boutons:
    declancheurs.append(( [350, 100, 450, 150], valideProposition ))
    images.append(("valider.jpg", [350, 100]))

    declancheurs.append(( [360, 145, 450, 180], corrigeProposition ))
    images.append(("corriger.png", [360, 145]))

    declancheurs.append(( [400, 0, 500, 48], sauvegarder ))
    images.append(("sauvegarderQuiter.png", [400, 0]))

    affichePartie()


def sauvegarder():
    Sauvegarde.sauvegarder(aDeviner, oldPropositions)
    pygame.event.post(pygame.event.Event(TOMENUEVENT))


def partieSauvegardee():
    global aDeviner, oldPropositions
    aDeviner, oldPropositions = Sauvegarde.reprendre()
    print(aDeviner)
    print(oldPropositions)
    partie()

def nouvellePartie():
    global aDeviner, oldPropositions
    aDeviner = Initialisations.listeAleatoire(6, 4)
    oldPropositions =[]
    partie()


# tout les events sont recuper ici. cette fonction boucle jusqu'a l'arret du programme
def boucleGenerale(partieEnCours = False):
    global secret, declancheurs, images
    boucle = True
    while boucle:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                boucle = False
            elif e.type == WINEVENT:
                secret = False
                images.append(("felicitations.png", [120, 50]))
                affichePartie()
                declancheurs = [[ [0, 0, 500, 700], lambda: pygame.event.post(pygame.event.Event(TOMENUEVENT)) ]]
            elif e.type == LOSEEVENT:
                secret = False
                images.append(("perdu.png", [120, 50]))
                affichePartie()
                declancheurs = [[ [0, 0, 500, 700], lambda: pygame.event.post(pygame.event.Event(TOMENUEVENT)) ]]
            elif e.type == TOMENUEVENT:
                secret = False
                partieEnCours = False
                creerMenu()
            elif e.type == NOUVELLEPARTIEEVENT:
                secret = True
                partieEnCours = True
                nouvellePartie()
            elif e.type == CONTINUEPARTIEEVENT:
                secret = True
                partieEnCours = True
                partieSauvegardee()
            elif e.type == MOUSEBUTTONUP:
                declancheurColision(e.pos)
                if partieEnCours:
                    affichePartie()


def affichePartie():
    screen.fill((192, 192, 192))

    for im in images:
        screen.blit(pygame.image.load(im[0]), im[1])

    # on dessine la solution a decouvrire
    if secret == True:
        dessineProposition((0,0,0,0), [bordures[0]+67, 0], screen)
    else:
        dessineProposition(aDeviner, [bordures[0]+67, 0], screen)

    # on dessine les enciennes propositions du joueur
    x = bordures[0]+taillePions
    y = bordures[1]+taillePions
    for oldPropo in oldPropositions:
        y += taillePions
        dessineProposition(oldPropo[0], [x, y], screen)
        dessineResultat(oldPropo[1], [x+200, y], screen)

    # on dessine la proposition actuel (pas forcement complete)
    y += taillePions
    for i, pion in enumerate(proposition[:4]):
        dessinePion(pion, [x+i*taillePions, y], screen)


    pygame.display.flip()




def collisionTest(coord, hitbox):
    return hitbox[0] <= coord[0] <= hitbox[2] and hitbox[1] <= coord[1] <= hitbox[3]


def declancheurColision(coords):

    for declancheur in declancheurs:
        if collisionTest(coords, declancheur[0]):
            print("collision")
            declancheur[1]()  # on execute la fonction assosciee


def dessinePion(nb, coord, screen):
     image = pygame.image.load("pion"+str(nb)+".png")
     screen.blit(image, coord)

def dessineProposition(proposition, coord, screen):
    for i, pion in enumerate(proposition):
        dessinePion(pion, [coord[0]+i*taillePions, coord[1]], screen)


def dessineResultat(resultat, coord, screen):
    resImages = []
    for i in range(resultat[0]):
        resImages.append(pygame.image.load("rouge.png"))
    for i in range(resultat[1]):
        resImages.append(pygame.image.load("blanc.png"))
    while len(resImages) < 4:
        resImages.append(pygame.image.load("noir.png"))

    for i, resImage in enumerate(resImages):
        screen.blit(resImage, [coord[0]+(i%2)*(taillePions//2), coord[1]+(i//2)*(taillePions//2)])



def valideProposition():
    global proposition  # pour faire l'assignement plus bas
    if len(proposition) < 4:
        return  # on empeche l'utilisateur de valider une proposition trop courte

    print("proposition:", proposition)
    print("a deviner:", aDeviner)
    print("verif:", TourDeJeu.verification(proposition[:4], aDeviner))
    result = TourDeJeu.verification(proposition[:4], aDeviner)
    oldPropositions.append([proposition[:4], result])
    proposition = []
    if result[0] == 4:  # 4 bons dans l'ordre
        print("Win")
        pygame.event.post(pygame.event.Event(WINEVENT))
    elif len(oldPropositions) >= 10:
        print("lose")
        pygame.event.post(pygame.event.Event(LOSEEVENT))


def corrigeProposition():
    if len(proposition) > 0:
        proposition.pop()






window = main()