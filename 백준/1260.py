import sys
from collections import deque

n,m,v = map(int,sys.stdin.readline().split())
graph= [[0 for x in range(n+1)]for x in range(n+1)]

visited = [0]*(n+1)

for x in range(m):
    a, b= map(int,sys.stdin.readline().split())
    graph[a][b] = graph[b][a] = 1
    
now = v
dfs_list = [now]
visited[now] = 1 

def Dfs(now):
    for x in range(1,n+1):
        if graph[now][x] == 1 and visited[x] == 0:
            visited[x] = 1
            dfs_list.append(x)
            Dfs(x)
        
Dfs(now)

visited = [0]*(n+1)
now = v
q = deque()
q.append(now)
visited[now] = 1
bfs_list= []

while q:
    now = q.popleft()
    bfs_list.append(now)
    for x in range(1,n+1):
        if graph[now][x] == 1 and visited[x] == 0:
            visited[x] = 1
            q.append(x)
            
for x in dfs_list:
    print(x, end = ' ')
print()
for x in bfs_list:
    print(x, end = ' ')