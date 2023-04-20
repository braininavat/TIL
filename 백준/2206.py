import sys
from collections import deque
n,m = map(int,sys.stdin.readline().split())#n = col m = row
graph = []
move = [[0,1],[0,-1],[1,0],[-1,0]]
for _ in range(n):
    graph.append(sys.stdin.readline().strip())

def bfs():
    visited = [[False]*m for _ in range(n)]
    q = deque()
    q.append([0,0,0,1])
    visited[0][0] = True
    while q:
        col,row,br,cnt = q.popleft()
        for x in range(4):
            nextcol = col +move[x][0]
            nextrow = row + move[x][1]
            if 0<=nextcol<=n-1 and 0<=nextrow<=m-1: 
                if nextcol == n-1 and nextrow == m-1:
                    if graph[nextcol][nextrow] == '0' or br == 0:
                        return cnt+1
                if visited[nextcol][nextrow] == False:
                    if graph[nextcol][nextrow] == '0':
                        q.append([nextcol,nextrow,br,cnt+1])
                        visited[nextcol][nextrow] = True
                    else:
                        if br == 0:
                            q.append([nextcol,nextrow,1,cnt+1])
                            visited[nextcol][nextrow] = True
    return -1
                        
print(bfs())
