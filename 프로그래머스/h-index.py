citations= [3,0,6,1,5]
def solution(citations):
    citations.sort()
    answer = 0
    
    for h in range(1,citations[-1]): 
        overh = 0
        underh = 0
        for citation in citations: 
            if h > citation:
                underh +=1
            elif h < citation:
                overh+=1
            else:
                overh+=1
                underh+=1
        if overh >= h and underh <= h:
            answer = max(answer,h)
        
    return answer