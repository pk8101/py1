def printPathHealper(x,y,maze,n,solution):
    if x==n-1 or y==n-1:
        solution[x][y]=1
        print(solution)
        return
    if x<0 or y<0 or x>=n or y>=n or solution[x][y]==1 or maze[x][y]==0:
        return 
    
    solution[x][y]=1
    printPathHealper(x+1,y,maze,n,solution)
    printPathHealper(x,y+1,maze,n,solution)
    printPathHealper(x-1,y,maze,n,solution)
    printPathHealper(x,y-1,maze,n,solution)
    solution[x][y]=0
    return

def printPath(maze):
    n=len(maze)
    solution=[[0 for j in range(n)] for i in range(n)]
    printPathHealper(0,0,maze,n,solution)
n=int(input())
maze=[]
for i in range(n):
    row=[int(i) for i in input().split()]
    maze.append(row)
    
printPath(maze)
    