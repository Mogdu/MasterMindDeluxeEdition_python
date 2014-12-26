


def tourDeJeu(nbreCouleur, mbrePions, aDeviner):
    proposition = None
    while proposition == None:
        try:
            proposition = saisie(nbreCouleur, mbrePions)
        except UserError:
            pass
    affichage_proposition(proposition)
    rougesEtNoirs = verification(proposition, aDeviner)
    affichage_rougesEtNoirs(rougesEtNoirs)
    ## debug
    affichage_proposition(aDeviner)
    if rougesEtNoirs[0] == mbrePions:
        print("Gagne!")
        return True
    return False


class UserError(Exception):
    pass

def saisie(nbreCouleur, mbrePions):
    characters = input("Entrer une suite de "+str(mbrePions)+" chiffres tous entre 1 et "+str(nbreCouleur))
    proposition = []
    possible = range(1, 7)
    for c in characters:
        i = int(c)
        try:
            if i in possible:
                proposition.append(i)
        except ValueError:  # c n'etait pas un nombre
            continue
    if len(possible) < 4:
        raise UserError("Seulement", len(possible), "valeurs sont correctes")
    return proposition


def affichage_proposition(proposition):
    print(proposition)


def verification(proposition, aDeviner):  # retourne un nombre de pion bon dans l'ordre et dans le desordre
        rouge = 0  # dans l'ordre
        noir = 0  # dans le desordre
        prop = dict(enumerate(proposition))  # on cree des listes independentes car on va suprimer des elements
        reponse = dict(enumerate(aDeviner))
        # test dans l'ordre
        for i in range(len(prop)):
            if prop[i] == reponse[i]:
                rouge += 1
                prop.pop(i)
                reponse.pop(i)
        # test dans le desordre
        for i in prop.keys():
            for ii in reponse.keys():
                if prop[i] == reponse[ii]:
                    noir += 1
                    reponse.pop(ii)
                    break
        return rouge, noir

def affichage_rougesEtNoirs(rougesEtNoirs):
    print(rougesEtNoirs[0], "bons dans l'ordre", rougesEtNoirs[1], "bons dans le desordre")