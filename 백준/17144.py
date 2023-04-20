from doctest import NORMALIZE_WHITESPACE
import sys
from collections import deque
move = [[1,0],[-1,0],[0,1],[0,-1]] 
r,c,t = map(int,sys.stdin.readline().split()) # row, col, time
graph = []
dusts = []
for x in range(r):
    rownow = list(map(int,sys.stdin.readline().split()))
    graph.append(rownow)
    if rownow[0] == -1:
        ac = x # 공기청정기위치(아래쪽)

def diff(): # dust diffusion
    q = deque()
    for x in range(r):
        for y in range(c):
            if graph[x][y] > 0:
                q.append([x,y,graph[x][y]])
    while q:
        nowr, nowc, nowval = q.popleft()
        nextval = nowval//5
        cnt = 0 # diff counter
        for x in range(4): # mover 
            nextr = nowr+move[x][0]
            nextc = nowc+move[x][1]
            if 0<=nextr<r and 0<=nextc<c:
                if graph[nextr][nextc] == -1:
                    continue
                graph[nextr][nextc] += nextval
                cnt+=1
        graph[nowr][nowc] -= cnt*nextval
        
def cir(): #A/C
    nowr = ac-1
    nowc = 1
    prevval = graph[nowr][nowc]
    graph[nowr][nowc] = 0
    orderup = [2,1,3,0]
    for x in range(4):
        while(True):
            nextr = nowr + move[orderup[x]][0]
            nextc = nowc + move[orderup[x]][1]
            if nowr == ac-1 and nowc == 0:
                graph[nowr][nowc] = 0
                break
            if 0<= nextr < r and 0<= nextc <c:
                tmp = graph[nextr][nextc]
                graph[nextr][nextc] = prevval
                prevval = tmp 
                nowr, nowc = nextr, nextc
            else:
                break
            
    nowr = ac
    nowc = 1    
    prevval = graph[nowr][nowc]
    graph[nowr][nowc] = 0
    orderdown = [2,0,3,1]
    for x in range(4):
        while(True):
            nextr = nowr + move[orderdown[x]][0]
            nextc = nowc + move[orderdown[x]][1]
            if nowr == ac and nowc == 0:
                graph[nowr][nowc] = 0
                break
            if 0<= nextr < r and 0<= nextc <c:
                tmp = graph[nextr][nextc]
                graph[nextr][nextc] = prevval
                prevval = tmp 
                nowr,nowc = nextr,nextc
            else:
                break
    

for _ in range(t):
    diff()
    cir()
result = 0
for x in range(r):
    for y in range(c):
        result+=graph[x][y]
print(result)







