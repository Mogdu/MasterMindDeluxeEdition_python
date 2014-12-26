from Console import Initialisations
from Console.TourDeJeu import *


def mastermindConsole():
    nbreCouleur, mbrePions, nbreEssais = Initialisations.parametrage()
    aDeviner = Initialisations.listeAleatoire(nbreCouleur, mbrePions)

    while True:  # boucle du programme
        while tourDeJeu(nbreCouleur, mbrePions, aDeviner):  # boucle d'une partie
            nbreEssais -= 1
            if nbreEssais <= 0:
                print("Perdu! vous avez utilise tout vos essais")
                print("Vous cherchiez:")
                affichage_proposition(aDeviner)
                break
        if input("Voulez vous rejouer?").lower() not in ["oui", "ouai", "certainement", "bien sur", "avec plaisire",
                                                         "j'ai envie de te dire oui", "bien volontier",
                                                         "ha bas oui alors", "yes", "yeah", "hell yeah"]:
            break


mastermindConsole()