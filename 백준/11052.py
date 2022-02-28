#boj.kr/11052
import sys
n = int(input())
packs = list(map(int,sys.stdin.readline().split()))
dp = [0]+[pack for pack in packs]

for x in range(n+1):
    maxval = 0
    for y in range(1,x//2+1):
        maxval = max(maxval,dp[x-y]+dp[y])
    dp[x] = max(maxval,dp[x])
    
print(dp[n]) 