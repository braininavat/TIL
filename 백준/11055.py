#boj.kr/11055
import sys
n = int(sys.stdin.readline())
nlist = list(map(int,sys.stdin.readline().split()))
dp = [0]*1000

for x in range(len(nlist)):
    dp[x] = nlist[x]
    cur_max = 0
    for i in range(x-1,-1,-1):
        if nlist[x] > nlist[i]:
            cur_max = max(cur_max,dp[i])
    dp[x] += cur_max
    
print(max(dp)) 