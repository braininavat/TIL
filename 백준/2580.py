#백트래킹 사용
import sys
graph = []
empty = []
cnt = 0 
for x in range(9):
    graph.append(list(map(int,sys.stdin.readline().split())))
    for y in range(9):
        if graph[x][y] == 0:
            cnt+=1
            empty.append([x,y])
        
def chkx(posx,num):
    for y in range(9):
        if num == graph[posx][y]:
                return False
    return True

def chky(posy,num):
    for x in range(9):
        if num == graph[x][posy]:
                return False
    return True
                
def chksq(posx,posy,num):
    startx = 3*(posx//3)
    starty = 3*(posy//3)
    for x in range(startx,startx+3):
        for y in range(starty,starty+3):
            if num == graph[x][y]:
                return False
    return True

def backtrack(n):
    if cnt == n:
        for x in range(9):
            for y in range(9):
                print(graph[x][y], end = ' ')
            print()
        exit(0)
    posx,posy = empty[n]
    for i in range(1,10):
        if chkx(posx,i) and chky(posy,i) and chksq(posx,posy,i):
            graph[posx][posy] = i
            backtrack(n+1)
    graph[posx][posy] = 0
            
backtrack(0)