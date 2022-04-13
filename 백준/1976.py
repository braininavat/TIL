import sys
n = int(sys.stdin.readline())#도시수
m = int(sys.stdin.readline())#여행할도시수
parent = [x for x in range(n+1)] #n개의 도시
stat = [0]*n 
plans = [0]*m
result = True
def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a,b):
    para = find(a)
    parb = find(b)
    if para < parb:
        parent[parb] = para #루트노드에대해
    else:
        parent[para] = parb
        
for x in range(1,n+1):
    stat = list(map(int,sys.stdin.readline().split()))
    for y in range(1,n):
        if stat[y]:
            union(x,y+1)

for x in range(1,n+1):
    find(x)


plans = list(map(int,sys.stdin.readline().split()))
for x in range(1,m):
    prev = parent[plans[x-1]]
    now = parent[plans[x]]
    if prev != now:
        print("NO")
        result = False
        break

if result == True:
    print("YES")