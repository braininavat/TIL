import sys
n = int(sys.stdin.readline())
members = [[0]for _ in range(n)]

for x in range(n):
    members[x]=sys.stdin.readline().split()
    
members.sort(key=lambda x : int(x[0]))

for member in members:
    print(" ".join(member))