#집->파티장소 : 역방향 그래프를 만들어 파티장소로부터 다익스트라 사용한다
#파티장소->집 : 정방향 그래프로 다익스트라 사용
import sys,heapq
n,m,x = map(int,sys.stdin.readline().split())
costs = [[] for _ in range(n)]
costs_rev = [[] for _ in range(n)]
INF = int(1e9)
for _ in range(m):
    start,end,tmpcost = map(int,sys.stdin.readline().split())
    costs[start-1].append([end-1,tmpcost])
    costs_rev[end-1].append([start-1,tmpcost])
partyhouse = x-1

def dijkstra(start,costs):
    q = []
    distance = [INF]*n
    distance[start] = 0
    for cost in costs[start]:
        heapq.heappush(q,[cost[1],cost[0]]) # [cost, dest]
        distance[cost[0]] = cost[1]
    while q:
        dist,now =heapq.heappop(q)
        if distance[now] < dist:
            continue
        for cost in costs[now]:
            newdist = dist+cost[1]
            if newdist < distance[cost[0]]:
                distance[cost[0]] = newdist
                heapq.heappush(q,[newdist,cost[0]])
    return distance

go = dijkstra(partyhouse,costs_rev)
back = dijkstra(partyhouse,costs)
answer = 0
for x in range(n):
    answer = max(answer,go[x]+back[x])
   
print(answer)