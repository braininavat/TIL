import sys
n = int(sys.stdin.readline())
a, b = map(int,sys.stdin.readline().split())
m = int(sys.stdin.readline())
graph = [[0 for _ in range(n+1)]for _ in range(n+1)]
for _ in range(m):
    x, y = map(int,sys.stdin.readline().split())
    graph[x][y] = 1
    graph[y][x] = 1
    for i in range(n+1):
        if graph[i][x] != 0 and graph[i][y] == 0:
            graph[i][y] = graph[i][x]+1
            graph[y][i] = graph[i][x]+1
            
if graph[a][b] ==0:
    result= -1
else:
    result = graph[a][b]
if a == b:
    result = 0
print(result)

            
    
    


