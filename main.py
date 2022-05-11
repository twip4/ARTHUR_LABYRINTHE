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

def valid(maze,x,y):
  if (x>=0 and x<len(maze) and y>=0 and y<len(maze[0]) and maze[x][y]==1):
    return True
  else:
    return False
def walk(maze,x,y):
  if(x==0 and y==0):
    print("successful!")
    return True
  if valid(maze,x,y):
    # print(x,y)
    maze[x][y]=2 
    if not walk(maze,x-1,y):
      maze[x][y]=1
    elif not walk(maze,x,y-1):
      maze[x][y]=1
    elif not walk(maze,x+1,y):
      maze[x][y]=1
    elif not walk(maze,x,y+1):
      maze[x][y]=1
    else:
      return False 
  return True
walk(maze,3,3)