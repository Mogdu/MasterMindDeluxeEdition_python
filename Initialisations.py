import random



def parametrage():
    if input("entrer des parametres personalisees?").lower() in ["oui", "ouai", "yep", "yes", "y"]:
        nbreCouleur = -1
        while nbreCouleur < 2:
            nbreCouleur = input("Entrez le nombre de couleurs:")
        mbrePions = -1
        while mbrePions < 1:
         mbrePions = input("Entrez le nombre de poins avec lesquel vous allez jouer:")
        nbreEssais = -1
        while nbreEssais < 0:
            nbreEssais = input("Entrez le nombre d'essai possibles. Entrez 0 pour infinit:")
        return nbreCouleur, mbrePions, nbreEssais
    return 6, 4, 10


def listeAleatoire(nbreCouleur, mbrePions):
    # randint ne marche pas comme range et va jusqu'au parametre limiteur compris
    return [random.randint(1, nbreCouleur) for i in range(mbrePions)]
