import random



def parametrage():
    if input("entrer des parametres personalisees?").lower() in ["oui", "ouai", "yep", "yes", "y"]:
        nbreCouleur = -1
        while nbreCouleur < 2:
            try:
                nbreCouleur = int(input("Saisir le nombre de couleurs : "))
            except ValueError:
                continue
        mbrePions = -1
        while mbrePions < 1:
            try:
                mbrePions = int(input("Saisire la longueur de la suite a deviner : "))
            except ValueError:
                continue
        nbreEssais = -1
        while nbreEssais < 0:
            try:
                nbreEssais = int(input("Saisire le nombre d'essais : "))
            except ValueError:
                continue
        return nbreCouleur, mbrePions, nbreEssais
    return 6, 4, 10


def listeAleatoire(nbreCouleur, mbrePions):
    # randint ne marche pas comme range et va jusqu'au parametre limiteur compris
    return [random.randint(1, nbreCouleur) for i in range(mbrePions)]
