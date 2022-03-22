from collections import deque
n = 6
edge = 	[[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]

def solution(n, edge):
    count = 0
    q = deque()
    costmax = 1
    graph = [[] for _ in range(n)]
    visited = [False]*n
    for x in edge:
        graph[x[0]-1].append(x[1]-1)
        graph[x[1]-1].append(x[0]-1)
            
    for x in graph[0]:
            q.append([0,x,1])
            visited[x] = True
            
    visited[0] = True
    while q:
        _,nextnode,cost=q.popleft()
        for x in graph[nextnode]:
            if visited[x] == False:
                    visited[x] = True
                    q.append([nextnode,x,cost+1])
                    if costmax == cost+1:
                        count+=1
                    elif costmax > cost+1:
                        count = 0
                    else: 
                        costmax = cost+1;
                        count = 1
                        
    return count
print(solution(n,edge))