from libGrille import *
import time
import random
#on ouvre un objet graphique, version de la lib Grille
g = ouvrirFenetreGrille(80,16,12)


maxV = 11
maxH = 15

Matrice = []

for x in range(maxV) :
    M = [0 for y in range(maxH)]
    Matrice.append(M)

print(Matrice)

def Maze(Mat,MAXV,MAXH) :
    H = random.choice(MAXH)
    V = random.choice(MAXV)
    for x in range(MAXV):
        if x != V :
            Mat[H] = 1
    print(Mat)




Maze(Matrice,maxV,maxH)


#on place des murs
for i,j in [Matrice] :
    g.changerCarre(i,j,"black")


def exploration(i,j,oldi=None,oldj=None,F=None):
    """Démarre l'exploration de la case de coordonnées (i,j)
    Cette case est censée être valide et inexplorée (grise). L'exploration consiste en :
    - changer la case en bleu pour marquer le fait qu'elle est exklorée
    - déplacer pacman sur cette case
    - tester chacune des 4 cases voisines, et si cette case est valide et inexplorée, on appelle la fonction exploration dessus
    - quand une de ces explorations est terminée, on peut remettre pacman en i,j 
    - en dernière amélioration, on peut placer une flèche entre cette case et la case voisine si une exploration est lancée,
    et supprimer la flèche quand de la case voisine est est terminée
    """
    delay = 0.000005
    g.changerCarre(i,j,"blue")
    if oldi != None and oldj != None:
       F = g.dessinerFleche(oldi,oldj,i,j)
    g.placer_pacman(i,j)
    time.sleep(delay)
    L = [[1,0],[-1,0],[0,1],[0,-1]]
    random.shuffle(L)
    for x in L :
        posX,posY = i+x[0],j+x[1]
        if g.case_valide(posX,posY) and g.getCouleur(posX,posY) != "blue":
            if F != None :
                exploration(posX,posY,i,j,F)
            exploration(posX,posY,i,j)
    g.placer_pacman(i,j)
    if F != None :
        g.supprimer(F)
    time.sleep(delay)


g.attendreClic()
#exploration(7,5)


#fin du programme
g.attendreClic()
g.fermerFenetre()

