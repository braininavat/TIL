import sys
n,m = map(int,sys.stdin.readline().split()) #점개수, 횟수
completed = 0
parent = [x for x in range(n)]
def find(x):
    if parent[x] == x:
        return x
    parent[x] = find(parent[x])
    return parent[x]
        
def union(a,b):
    roota = find(a)
    rootb = find(b)
    if roota < rootb:
        parent[rootb] = roota
    else:
        parent[roota] = rootb

for x in range(m):
    a, b = map(int,sys.stdin.readline().split())
    if find(a) == find(b):
        completed = x+1
        break
    else:
        union(a,b)
        
print(completed)

