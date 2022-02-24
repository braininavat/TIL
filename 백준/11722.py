#boj.kr/11722
import sys
n = int(sys.stdin.readline())
nlist = list(map(int,sys.stdin.readline().split()))
dp = [1]*1000

for x in range(len(nlist)):
    maxdp = 0
    for y in range(x):
        if nlist[x] < nlist[y]:
            maxdp = max(maxdp,dp[y])
    dp[x] += maxdp
print(max(dp))