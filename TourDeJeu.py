


def tourDeJeu(nbreCouleur, n, aDeviner):
    proposition = None
    while proposition == None:
        try:
            proposition = saisie(nbreCouleur, n)
        except UserError:
            pass
    rougesEtBlancs = verification(proposition, aDeviner)
    affichage_rougesEtBlancs(rougesEtBlancs)
    if rougesEtBlancs[0] == n:
        print("Gagné! felicitations")
        return True
    return False


class UserError(Exception):
    pass

def saisie(nbreCouleur, nbrePions):
    characters = input("saisir votre proposition : ")
    proposition = []
    for c in characters:
        try:
            i = int(c)
            if i < 1 or i > nbreCouleur:
                proposition.append(i)
        except ValueError:  # c n'etait pas un nombre
            continue
    if len(proposition) < nbrePions:
        raise UserError("Seulement", len(proposition), "valeurs sont correctes")
    return proposition[:nbrePions]



def affichage_proposition(proposition):
    for c in proposition:
        print(c, end="")


def verification(proposition, aDeviner):  # retourne un nombre de pion bon dans l'ordre et dans le desordre
        rouge = 0  # dans l'ordre
        blanc = 0  # dans le desordre
        prop = dict(enumerate(proposition))  # on cree des dictionaires pour eliminer des element pendant les iterations
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
                    blanc += 1
                    reponse.pop(ii)
                    break
        return rouge, blanc

def affichage_rougesEtBlancs(rougesEtBlancs):
    print(rougesEtBlancs[0], "bien placé(s), et ", rougesEtBlancs[1], "mal placé(s)")