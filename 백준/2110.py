import sys
n,c = map(int,sys.stdin.readline().split())
houses = []
result = 0
for x in range(n):
    houses.append(int(sys.stdin.readline()))
houses.sort()

start = 0
end = houses[-1]-houses[0]

while start<=end:
    mid = (start+end)//2
    now = houses[0]
    count = 1
    for x in range(1,len(houses)):
        if houses[x]-now >= mid: #목표값보다 큰 거리에 공유기를 설치
            count+=1
            now = houses[x]           
    if count < c: #공유기개수가 목표보다낮으면 거리를 좁혀야함
        end = mid-1
    else:         #공유기 개수가 목표보다 많으면 거리를 늘리면됨.
        start = mid+1
        result = mid

print(result)
        