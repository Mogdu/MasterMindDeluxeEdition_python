import random
import Initialisations
from TourDeJeu import *


def tourDeJeuIA(S, essai, aDeviner, nbrePions):
    proposition = choisirIA(S, essai, nbrePions)
    print("proposition de l'ordinateur : ", end="")
    affichage_proposition(proposition)
    print("")
    rougesEtBlancs = verification(proposition, aDeviner)
    affichage_rougesEtBlancs(rougesEtBlancs)
    S = reduireLesPossibles(S, proposition, rougesEtBlancs)
    if rougesEtBlancs[0] == nbrePions:
        print("Gagné! felicitations")
        return True
    return S


def choisirIA(S, essai, nbrePions):
    if essai == 1 and nbrePions == 4:
        return [1, 1, 2, 2]

    return random.choice(list(S))



def reduireLesPossibles(S, choix, resultats):
    # on enleve de S toutes les solutions qui ne corespondent pas au couple essai/resultat que l'on vient de jouer
    # on peut supprimer tout ce qui a trop ou pas asse de bons dans l'ordre
    # et tout ce qui n'a pas asse de bons dans le desordre
    # par rapport a ce que l'on vient de jouer
    newS = set()
    for code in S:
        ordre = 0
        desordre = 0
        for i, element in enumerate(code):
            for ii, chElement in enumerate(choix):
                if element == chElement:
                    if i == ii:
                        ordre += 1
                    else:
                        desordre += 1

        if ordre == resultats[0] and desordre >= resultats[1]:
            newS.update((code,))
    print("plus que", len(newS), "possibles")
    return newS



def ensembleDesPossibles(nbrePions, nbreCouleur):
    ensemble = set()
    ensemble = _ensembleDesPossibles_iteration((), nbreCouleur, nbrePions)
    return ensemble


def _ensembleDesPossibles_iteration(premiers, nbreCouleur, restants):
    sousEnsembles = set()
    for i in range(1, nbreCouleur+1):
        sousEnsemble = (premiers) + (i,)   # la virgule dans (i,) en fait un tuple et autorise a l'additioner
        if restants > 1:
            sousEnsembles.update(_ensembleDesPossibles_iteration(sousEnsemble, nbreCouleur, restants-1))
        else:
            sousEnsembles.update((sousEnsemble,))
    return sousEnsembles


def ensembleDesResultats(nbrePions):
    ensemble = set()
    for i in range(1, nbrePions+1):
        for ii in range(1, nbrePions+1):
            ensemble.update(((i, ii),))  # la tonne de parentheses est obligatoire pour creer un set de tuples
    return ensemble




def mastermindConsole():
    nbreCouleur, nbrePions, nbreEssais = Initialisations.parametrage()

    while True:  # boucle du programme
        aDeviner = Initialisations.listeAleatoire(nbreCouleur, nbrePions)
        S = ensembleDesPossibles(nbrePions, nbreCouleur)
        i = 1
        print("\nessai 1")
        while True:  # boucle d'une partie
            S = tourDeJeuIA(S, i, aDeviner, nbrePions)
            if S == True:
                break
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