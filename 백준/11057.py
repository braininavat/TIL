#https://www.acmicpc.net/problem/11057
import sys
n = int(sys.stdin.readline().strip())
dp = [1]*10
tmpdp = [0]*10
for x in range(n-1):
    for i in range(10):
        for j in range(i,10):
            tmpdp[i] += dp[j]
    for x in range(10):
        dp[x] = tmpdp[x]
        tmpdp[x] = 0
print(sum(dp)%10007)



