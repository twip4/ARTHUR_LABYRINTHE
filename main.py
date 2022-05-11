import random

maxV = 16
maxH = 16

Matrice = []

for x in range(maxV) :
    M = [0 for y in range(maxH)]
    Matrice.append(M)

def Maze(Mat,MINV,MAXV,MINH,MAXH,N=0) :
    H = random.randint(MINH,MAXH)
    V = random.randint(MINV,MAXV)
    if N%2 == 0 :
        if MAXV//2 < 2 :
            return
        for x in range(MAXV):
            if x != V :
                Mat[x][H] = 1
    else :
        if MAXH//2 < 2 :
            return
        for x in range(MAXH):
            if x != H :
                Mat[V][x] = 1
    Printmat(Mat)
    Maze(Mat,0,V,0,H,N+1)
    Maze(Mat,V,16,H,16,N+1)



def Printmat(mat):
    for x in range(len(mat)) :
        print(mat[x])
    print()
    print()




Maze(Matrice,0,maxV,0,maxH)