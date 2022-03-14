# 문제 의도대로 다익스트라, 플로이드 워셜 등을 안쓰고 브루트포스로 풀려니 시간 초과가 계속 발생해서 고민했음
# 18번째 줄에서 cost가 val보다 작을때만 반복문을 시행한다는 조건을 걸어 시간단축 가능
import sys
n = int(sys.stdin.readline())
graph = []
for x in range(n):
    graph.append(list(map(int,sys.stdin.readline().split())))
visited = [0]*n
cost = int(1e9)

def travel(start,now,visited,val,cnt):
    global cost
    if cnt == n-1:
        if graph[now][start]!= 0:
            cost = min(cost, val+graph[now][start])
    else:
        for i in range(n):
            if visited[i] == 0 and graph[now][i] != 0 and cost > val:
                visited[i] = 1
                val+=graph[now][i]
                cnt+=1
                travel(start,i,visited,val,cnt)
                visited[i] = 0
                val-=graph[now][i]
                cnt-=1
            
for x in range(n):
    visited[x] = 1
    travel(x,x,visited,0,0)
    visited[x] = 0
    
print(cost)
    





