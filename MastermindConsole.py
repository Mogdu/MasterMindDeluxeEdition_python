
import Initialisations
from TourDeJeu import *


def mastermindConsole():
    nbreCouleur, mbrePions, nbreEssais = Initialisations.parametrage()

    while True:  # boucle du programme
        aDeviner = Initialisations.listeAleatoire(nbreCouleur, mbrePions)
        i = 1
        print("\nessai 1")
        while not tourDeJeu(nbreCouleur, mbrePions, aDeviner):  # boucle d'une partie
            i += 1
            if i > nbreEssais:
                print("Perdu! il falait trouver : ", end="")
                affichage_proposition(aDeviner)
                print("")
                break
            print("\nessai", i)
        if input("Voulez vous rejouer?").lower() not in ["oui", "ouai", "certainement", "bien sur", "avec plaisir",
                                                         "yep", "yes", "yeah", "hell yeah"]:
            break


mastermindConsole()