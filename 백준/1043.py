import sys
n, m = map(int,sys.stdin.readline().split())
t = list(map(int,sys.stdin.readline().split()))[1:]
parties = []
parents = [x for x in range(n+1)]
chk_parent = [False]*(n+1) #걸러내야되는parent를가진사람

count = m
for x in range(m):
    party = list(map(int,sys.stdin.readline().split()))
    parties.append(party)
    for y in range(party[0]):
        party_sort = party[1:]
        party_sort = sorted(party_sort)
        if parents[party_sort[y]] != party_sort[0]:
            for i in range(1,n+1):
                if parents[i] == parents[party_sort[y]]:
                    parents[i] = party_sort[0] 

for x in range(len(t)):
    t[x] = parents[t[x]]
for x in range(len(t)):
    chk_parent[t[x]] = True 
for party in parties:
    for man in party[1:]:
        if chk_parent[parents[man]] == True:
            count-=1
            break
        
    
print(count)
