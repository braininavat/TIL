import sys
n, m = map(int,sys.stdin.readline().split())
t = list(map(int,sys.stdin.readline().split()))[1:]
know = []
parties = []
count = m
parent = [x for x in range(n+1)]

def find(n):
    if parent[n] != n:
        parent[n] = find(parent[n])
        return parent[n]
    else:
        return n
    
def union(x,y):
    x = find(x)
    y = find(y)
    if x < y:
        parent[y] = x
    else:
        parent[x] = y
        
for x in range(m): # 참여자 받고 참여자끼리 집합만듬
    party = list(map(int,sys.stdin.readline().split()))
    party = party[1:]
    parties.append(party)
    for x in range(1,len(party)):
        union(party[x-1],party[x])

for x in range(1,len(parent)):
    find(x)

for boy in t: #거짓말탐지기 집합들 추출
    par = find(boy)
    if par not in know:
        know.append(par)
        
for party_ in parties:
    for boy in party_:
        par = parent[boy]
        if par in know:
            count-=1
            break
print(count)
