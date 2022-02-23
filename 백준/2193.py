#https://www.acmicpc.net/problem/2193
n = int(input())

dp = [0]*91
dp[1] = 1
dp[2] = 1
if n > 2 :
    for x in range(4,n+1):
        dp[x] = dp[x-1]+dp[x-2]
print(dp[n])