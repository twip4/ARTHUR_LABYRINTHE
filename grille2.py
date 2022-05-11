from libGrille import *
import time
import random
#on ouvre un objet graphique, version de la lib Grille
g = ouvrirFenetreGrille(80,16,12)


Matrice = [[1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1], [1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1], [1, 0, 0, 0, 1, 0, 1, 1, 0, 0, 1, 1], [1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 1], [1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1], [1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 1, 1], [1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 0, 1], [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1], [1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1], [1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 1], [1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1], [1, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 1], [1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1], [1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1]]

print(Matrice)

listpos = []

for x in range(len(Matrice)) :
    for y in range(len(Matrice[x])) :
        if Matrice[x][y] == 1 :
            listpos.append((x,y))

print(listpos)

#on place des mur
for i,j in listpos :
    g.changerCarre(i,j,"black")

posInit = (0,1)

g.placer_pacman(posInit[0],posInit[1])
g.changerCarre(15,10,"blue")


running = True

while running :
    n = g.attendreTouche()
    if n == "Up" :
        if g.case_valide(posInit[0],posInit[1]-1) :
            posInit = (posInit[0],posInit[1]-1)
    
    if n == "Down" :
        if g.case_valide(posInit[0],posInit[1]+1) :
            posInit = (posInit[0],posInit[1]+1)

    if n == "Right" :
        if g.case_valide(posInit[0]+1,posInit[1]) :
            posInit = (posInit[0]+1,posInit[1])
    
    if n == "Left" :
        if g.case_valide(posInit[0]-1,posInit[1]) :
            posInit = (posInit[0]-1,posInit[1])

    g.placer_pacman(posInit[0],posInit[1])

    if g.getCouleur(posInit[0],posInit[1]) == "blue" :
        running = False
        print("you win !!!!!!")

g.fermerFenetre()