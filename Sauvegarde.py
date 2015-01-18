
import TourDeJeu



def sauvegarder(aDeviner, oldPropositions):
    # on encode la partie dans un int
    # ce qui 1 prend moins de place. 2 cache la solution a l'utilisateur
    data = 0
    i = 0
    print("aDeviner:", aDeviner)
    for pion in aDeviner:
        data += pion*(8**i)
        i += 1
    for couple in oldPropositions:
        for pion in couple[0]:
            data += pion*(8**i)
            i += 1

    with open("mastermind.save", "w") as f:
        f.write(str(data))


#restitue la partie d'apres la sauvegarde
def reprendre():
    data = 0
    with open("mastermind.save") as f:
        data = int(f.read())

    aDeviner = []
    oldPropositions = []

    listeDesValeurs = []
    for c in oct(data)[2:]:  # on decoupe data serie de chifres de base 8
        listeDesValeurs.append(c)

    for i in range(4):
        aDeviner.append(int(listeDesValeurs.pop()))

    print("listeDesValeurs:", listeDesValeurs)
    while len(listeDesValeurs) >= 4:
        proposition = []
        for i in range(4):
            proposition.append(int(listeDesValeurs.pop()))
        oldPropositions.append((proposition, TourDeJeu.verification(proposition, aDeviner)))

    return aDeviner, oldPropositions