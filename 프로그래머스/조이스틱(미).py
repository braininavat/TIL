name = "JAN"
def solution(name):
    answer= 0
    name = list(name)
    visit = [False]*len(name)
    start = 0
    end= len(name)-1
    
    for x in range(len(name)):
        cost = ord(name[x])-ord('A')
        cost = min(cost,26-cost)
        if cost != 0:
            answer+=cost
            visit[x] = True
            
    def getdist(now,start,end,val):
        if not any(visit):
            return val
        for x in range(start,len(name)):
            if visit[x] == True:
                start = x
                break
        for x in range(end,-1,-1):
            if visit[x] == True:
                end = x
                break
        dist_start = min(abs(now-start),abs(len(name)-start+now))
        dist_end = min(abs(end-now),abs(len(name)-end+now))
        if dist_start < dist_end:
            visit[start] = False 
            return getdist(start,start,end,val+dist_start)
        else:
            visit[end] = False
            return getdist(end,start,end,val+dist_end)
        
    for x in range(len(name)):
        if visit[x] == True:
            visit[x] = False
            answer+=x
            answer+=getdist(x,start,end,0)
            break
    return answer
print(solution(name))