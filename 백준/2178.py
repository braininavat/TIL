# bfs에서 뺄때 체크하지 않고 넣을때 체크해야함

import sys
from collections import deque

n,m = map(int,sys.stdin.readline().split())
graph = []
answer = 1
visited = [[False]*m for _ in range(n)]
move = [[1,0],[-1,0],[0,1],[0,-1]]
for x in range(n):
    graph.append(list(sys.stdin.readline().strip()))

q = deque()
q.append([0,0,1]) # row, col, cnt
visited[0][0] = True
while q:
    rowprev, colprev, cntprev = q.popleft()
    if rowprev == n-1 and colprev == m-1:
        print(cntprev)
        break
    for x in range(4):
        rownow = rowprev+move[x][0]
        colnow = colprev+move[x][1]
        if 0<= rownow <= n-1 and 0<= colnow <= m-1:
            if graph[rownow][colnow] == '1' and visited[rownow][colnow] == False:
                visited[rownow][colnow] = True
                q.append([rownow,colnow,cntprev+1])



