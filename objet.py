import random
from select import select

class labyrinthe :
    
    def __init__(self, X) :
        self.Matrice = []
        self.taille = X
        for x in range(self.taille) :
            M = [0 for y in range(self.taille)]
            self.Matrice.append(M)
        self.maze(0,self.taille,0,self.taille,)

    def affiche(self) :
        for x in range(len(self.Matrice)) :
            print(self.Matrice[x])

    def maze(self,X1,X2,Y1,Y2,N=0) :
        H = random.randint(X1,X2)
        V = random.randint(Y1,Y2)

        if N%2 == 0 :
            if X2//2 < 2 :
                return
            for x in range(X2):
                if x != V :
                    self.Matrice[x][H] = 1
        else :
            if Y2//2 < 2 :
                return
        for x in range(Y2):
            if x != H :
                self.Matrice[V][x] = 1






p = labyrinthe(20)

p.affiche()
        
