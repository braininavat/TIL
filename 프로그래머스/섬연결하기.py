#크루스칼 알고리즘 사용
def solution(n, costs):
    answer = 0
    count = 0
    parent = [x for x in range(n)]
    costs.sort(key = lambda x : x[2])
    
    def find(x): # 부모반환
        if parent[x] == x:
            return x
        parent[x] = find(parent[x])
        return parent[x]
    
    for cost in costs:
        parent_0 = find(parent[cost[0]])
        parent_1 = find(parent[cost[1]])
        if parent_0 != parent_1:
            answer+=cost[2]
            count+=1
            if count == n-1:
                return answer
            if parent_0 < parent_1:
                parent[parent_1] = parent_0
            else:
                parent[parent_0] = parent_1
    