import sys
k,n = map(int,sys.stdin.readline().split())
cable = [0]*k
for x in range(k):
    cable[x] = int(sys.stdin.readline().strip())
start = 1
end = max(cable)

while start <= end:
    mid = (start+end)//2
    count = 0
    for x in range(k):
        count+=cable[x]//mid
    if count >= n:
        start = mid+1
        result = mid
    else:
        end = mid-1
print(result)