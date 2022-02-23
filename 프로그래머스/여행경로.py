#https://programmers.co.kr/learn/courses/30/lessons/43164

#내코드(DFS, 재귀함수 이용)
def solution(tickets):
    airport = ["ICN"]
    tickets.sort(key = lambda x : x[1])
    used = [0]*len(tickets)
    
    def dfs(airport):
        if len(airport) == len(tickets)+1:
            return airport
        for x in range(len(tickets)):
            if tickets[x][0] == airport[-1] and used[x] == 0:
                used[x] = 1
                dest = tickets[x][1]
                airport.append(dest)
                
                answer = dfs(airport)
                if answer: 
                    return answer
                else:
                    used[x] = 0
                    airport.pop()
    
    return dfs(airport)

#다른사람들의코드(DFS, defaultdict, 스택 이용)

from collections import defaultdict 

def dfs(graph, N, key, footprint):
    print(footprint)

    if len(footprint) == N + 1:
        return footprint

    for idx, country in enumerate(graph[key]):
        graph[key].pop(idx)

        tmp = footprint[:]
        tmp.append(country)

        ret = dfs(graph, N, country, tmp)

        graph[key].insert(idx, country)

        if ret:
            return ret


def solution(tickets):
    answer = []

    graph = defaultdict(list)

    N = len(tickets)
    for ticket in tickets:
        graph[ticket[0]].append(ticket[1])
        graph[ticket[0]].sort()

    answer = dfs(graph, N, "ICN", ["ICN"])

    return answer