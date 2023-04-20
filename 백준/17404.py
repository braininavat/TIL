import sys
n = int(sys.stdin.readline())
cost = [[0,0,0] for _ in range(n+1)]
dp = [0 for _ in range(n+1)]
for x in range(n):
    cost[x+1][0],cost[x][1],cost[x][2] = map(int(sys.stdin.readline().split()))
    
