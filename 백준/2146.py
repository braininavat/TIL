#함수로 안묶어주니까 코드가 난잡하고 보기싫어짐

import sys
from collections import deque
n = int(sys.stdin.readline())
graph = []
borders = []
answer= 100*100
num_isle = 0
for x in range(n):
    graph.append(list(map(int,sys.stdin.readline().split())))
visited = [[False]*n for _ in range(n)]
move = [[1,0],[-1,0],[0,1],[0,-1]]
q = deque()


for x in range(n):
    for y in range(n):
        if graph[x][y] == 1 and visited[x][y] == False:
            num_isle +=1
            graph[x][y] = num_isle
            q.append([x,y])
            visited[x][y] = True
            border = []
            while q:
                px,py = q.popleft()
                isborder = False
                for i in range(4):
                    nx = px+move[i][0]
                    ny = py+move[i][1]
                    if 0<=nx<=n-1 and 0<=ny<=n-1:
                        if graph[nx][ny] == 1:
                            if visited[nx][ny] ==False:
                                q.append([nx,ny])
                                visited[nx][ny] = True
                                graph[nx][ny] = num_isle
                        else:
                            isborder = True
                if isborder == True:
                    border.append([px,py])
            borders.append(border)

num_isle = 0

for border in borders:
    num_isle+=1
    visited = [[False]*n for _ in range(n)]
    for x in range(len(border)):
        q.append([border[x][0],border[x][1],0])
        visited[border[x][0]][border[x][1]] =True
    while q:
        px, py, cnt= q.popleft()
        for i in range(4):
            nx = px+move[i][0]
            ny = py+move[i][1]
            if 0<=nx<=n-1 and 0<=ny<=n-1:
                if graph[nx][ny] != num_isle  and visited[nx][ny] == False:
                    if graph[nx][ny] != 0:
                        answer=min(answer,cnt)
                        q.clear()
                        break
                    else:
                        visited[nx][ny] = True
                        q.append([nx,ny,cnt+1])

                
print(answer)