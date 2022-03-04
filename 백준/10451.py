import sys
from collections import deque
t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    result = 0
    graph = [0] + list(map(int,sys.stdin.readline().split()))
    visited = [0]*(n+1)
    
    for x in range(1,n+1):
        if visited[x] == 0:
            visited[x] = 1
            result+=1
            nextnode = graph[x]
            while visited[nextnode] == 0:
                visited[nextnode] = 1
                nextnode = graph[nextnode]
    print(result)
