#boj.kr/2667
#bfs 사용
import sys
from collections import deque

n = int(sys.stdin.readline())
graph = [[]for _ in range (n)]
visited = [[0 for _ in range(n)] for _ in range (n)]
move = [[1,0],[-1,0],[0,1],[0,-1]]
count = []
for x in range(n):
    graph[x] = list(map(int,sys.stdin.readline().strip()))

def bfs(starty,startx):
    q = deque()
    q.append([starty,startx])
    counth = 1
    visited[starty][startx] = 1
    while q:
        prev = q.popleft()
        for i in range(4):
            nexty = prev[0]+move[i][0]
            nextx = prev[1]+move[i][1]
            if 0 <= nexty <= n-1 and 0 <= nextx <= n-1:
                if visited[nexty][nextx] == 0 and graph[nexty][nextx] == 1:
                    q.append([nexty,nextx])
                    visited[nexty][nextx] = 1
                    counth+=1
    return counth



for y in range(n):
    for x in range(n):
        if graph[y][x] == 1 and visited[y][x] == 0:
            count.append(bfs(y,x))

count.sort()
print(len(count))
for x in count:
    print(x)
