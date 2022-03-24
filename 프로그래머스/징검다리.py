#rocks[now]와 now 헷갈려서 시간 소요
#도착지점에서도 count를 증가시켜야 하는지 고민했는데 해도된다.
#어차피 더 큰 count 값을 가지면 그에 맞춰서 거리를 조절하고, dist보다 크면 고려하지 않아도 되기때문.
#최솟값을 찾는 것이기 때문에 이진 탐색에서 거리를 늘리는 함수에 
#<= 연산자를 사용해야 하고, answer=mid도 그 밑에서 연산해야함
def solution(distance, rocks, n):
    rocks.sort()
    rocks.append(distance)
    
    start = 0
    end = rocks[-1]-rocks[0]
    
    while start<=end:
        mid = (start+end)//2
        now = 0
        count = 0
        for x in range(len(rocks)):
            dist = rocks[x]-now
            if dist < mid: #바위 제거시
                count+=1
            else: #바위 제거 x시
                now = rocks[x]
        if count <= n: #목표보다 작으면 거리 늘려야됨
            start = mid+1
            answer = mid
        else:
            end = mid-1
    return answer