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

    # ""Sinon, elle calcule le maximum sur l’ensemble des éléments 'x’ de “possibles“,
    # du minimum sur l’ensemble des éléments ‘res’ de “résultats“
    # du nombre d’éléments de S dont l’évaluation (au sens du jeu Mastermind) avec ‘s‘ est différente de ‘res’.""
    # Nous prenons le partit d'interpreter librement ces ecritures

    return random.choice(list(S))



def reduireLesPossibles(S, choix, resultat):
    S = _reduireLesPossibles_casGeneral_ordre(S, choix, resultat[0])
    S = _reduireLesPossibles_casGeneral_desordre(S, choix, resultat[1])
    return S

def _reduireLesPossibles_casGeneral_ordre(S, choix, bons):
    # on peut enlever tout les resultats qui contiennent moins ou plus de pions dans l'ordre
    newS = set()
    for code in S:
        nb = 0
        for i, element in enumerate(code):
            if element == choix[i]:
                nb += 1
        if nb == bons:
            newS.update((code,))
    return newS


def _reduireLesPossibles_casGeneral_desordre(S, choix, bons):
    # on peut enlever tout les resultats qui contiennent au moins le non nombre de ces pions dans de desordre
    newS = set()
    for code in S:
        nb = 0
        for i, element in enumerate(code):
            for ii, chElement in enumerate(choix):
                if i != ii and element == chElement:
                    nb += 1
        if nb >= bons:
            newS.update((code,))
    print("plus que", len(newS), "possibles")
    return newS



def ensembleDesPossibles(mbrePions, nbreCouleur):
    ensemble = set()
    for i in range(1, nbreCouleur+1):
        sousEnsemble = (i,)   # la virgule dans (i,) en fait un tuple
        ensemble.update(_ensembleDesPossibles_iteration(sousEnsemble, nbreCouleur, mbrePions-1))
    return ensemble


def _ensembleDesPossibles_iteration(premiers, nbreCouleur, restants):
    sousEnsembles = set()
    for i in range(1, nbreCouleur+1):
        sousEnsemble = (premiers) + (i,)   # la virgule dans (i,) en fait un tuple et autorise a l'additioner
        #print(sousEnsemble)
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