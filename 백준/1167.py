# 임의 노드에서 출발해 가장 먼 노드를 찍으면 그 노드는 무조건 지름을 구성하는 노드임.
import sys
from collections import deque
n = int(sys.stdin.readline())
graph = [[] for _ in range(n+1)]

def bfs(start):
    cgraph = [-1]*(n+1) # -1 means visited[x] = False  
    q = deque()
    q.append(start)
    cgraph[start] = 0
    maxx = [-1,-1]
    while q:
        now = q.popleft()
        for to, cost in graph[now]:
            if cgraph[to] == -1:
                cgraph[to] = cgraph[now]+cost
                q.append(to)
                if maxx[1] < cgraph[to]:
                    maxx = [to, cgraph[to]]
    return maxx

for x in range(n):
    info = list(map(int, sys.stdin.readline().split()))
    now = info[0]
    for y in range(1,len(info)-2,2):
        graph[now].append([info[y],info[y+1]])

maxnode, maxval = bfs(1)
maxnode, maxval = bfs(maxnode)
print(maxval)