import sys
n = int(sys.stdin.readline())
budgets = list(map(int,sys.stdin.readline().split()))
target = int(sys.stdin.readline())

start = 0
end = max(budgets)

while start<=end:
    mid = (start+end)//2
    total = 0
    for budget in budgets:
        if budget <=mid:
            total+=budget
        else:
            total+=mid
    if target<total: # 금액이 더 크면 범위를 줄인다
        end = mid-1
    else:
        start = mid+1 #금액이 더 작거나 같으면 범위를 키워가며 최댓값 탐색
        result = mid
        
print(result)