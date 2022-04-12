#19, 21번줄에서 처음에 parent[x] = pary 로 놓아서 틀렸다. 자신의 부모가 아니라 루트노드의 부모를 최신화 해줘야한다.

import sys
sys.setrecursionlimit(10**9)
n,m = map(int,sys.stdin.readline().split())
parent = [x for x in range(n+1)]
result = []

def find(x):
    par = parent[x]
    if par != x:
        parent[x] = find(par)
    return parent[x]

def union(x,y):
    parx = find(x)
    pary = find(y)
    if parx > pary:
        parent[parx] = pary
    else:
        parent[pary] = parx
    
for x in range(m):
    d, a, b = map(int,sys.stdin.readline().split())
    if d == 0:
        union(a,b)
    else:
        if find(a) == find(b):
            print("YES")
        else:
            print("NO")