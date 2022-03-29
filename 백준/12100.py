import sys 
n = int(sys.stdin.readline())
graph = []
answer = 0
for x in range(n):
    graph.append(list(map(int,sys.stdin.readline().split())))

def up(graph):
    newgraph = [[0]*n for _ in range(n)]
    for y in range(n):
        prev = 0
        now = 0
        for x in range(n):
            if graph[x][y]!= 0:
                if prev == graph[x][y]:
                    newgraph[now][y] = (2*prev)
                    prev =0
                else:
                    newgraph[now][y] = graph[x][y]
                    prev = graph[x][y]
                    now+=1
    return newgraph
            
def down(graph):
    newgraph = [[0]*n for _ in range(n)]
    for y in range(n):
        prev = 0
        now = n-1
        for x in range(n-1,-1,-1):    
            if graph[x][y]!= 0:
                if prev == graph[x][y]:
                    newgraph[now][y] = (2*prev)
                    prev =0
                else:
                    newgraph[now][y] = graph[x][y]
                    prev = graph[x][y]
                    now-=1
    return newgraph
def left(graph):
    newgraph = [[0]*n for _ in range(n)]
    for x in range(n):
        prev = 0
        now = 0
        for y in range(n):
            if graph[x][y]!= 0:
                if prev == graph[x][y]:
                    newgraph[x][now] = (2*prev)
                    prev =0
                else:
                    newgraph[x][now] = graph[x][y]
                    prev = graph[x][y]
                    now+=1
    return newgraph

def right(graph):
    newgraph = [[0]*n for _ in range(n)]
    for x in range(n):
        prev = 0
        now = n-1
        for y in range(n-1,-1,-1):    
            if graph[x][y]!= 0:
                if prev == graph[x][y]:
                    newgraph[x][now] = (2*prev)
                    prev =0
                else:
                    newgraph[x][now] = graph[x][y]
                    prev = graph[x][y]
                    now-=1
    return newgraph

def dfs(cnt,graph):
    global answer
    if cnt == 5:
        answer = max(answer,max(max(graph)))
    else:
        dfs(cnt+1,up(graph))
        dfs(cnt+1,down(graph))
        dfs(cnt+1,left(graph))
        dfs(cnt+1,right(graph))
    
dfs(0,graph)
print(answer)