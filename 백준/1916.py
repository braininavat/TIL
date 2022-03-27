import sys, heapq

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
INF = int(1e9)
graph = [[] for _ in range(n)]
for x in range(m): #버스정보
    start,end,cost = map(int,sys.stdin.readline().split())
    graph[start-1].append([end-1,cost])
start, end = map(int,sys.stdin.readline().split())

distance = [INF]*(n) #비용테이블

def dijkstra(start):
    q = [] 
    heapq.heappush(q,(0,start))
    distance[start] = 0
    while q: 
        dist, now = heapq.heappop(q)
        if distance[now] < dist: #이미 처리된적있으면 무시
            continue
        for i in graph[now]: #i = (노드,비용)
            cost = dist+i[1] 
            if cost < distance[i[0]]: #거리 더 짧으면
                distance[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))#힙에선 cost가 앞으로
                
dijkstra(start-1)
print(distance[end-1])
    



