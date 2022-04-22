import sys
n = int(sys.stdin.readline())
dp = [[0,[]] for _ in range(n+1)]
dp[1][0] = 0
dp[1][1].append(1)  


for now in range(2,n+1):
    dp[now][0] = dp[now-1][0]+1
    dp[now][1] = dp[now-1][1]+[now]
    if now%3 == 0:
        if dp[now//3][0]<dp[now][0]:
            dp[now][0] = dp[now//3][0]+1
            dp[now][1] = list(dp[now//3][1])+[now]
    if now%2 == 0:
        if dp[now//2][0]<dp[now][0]:
            dp[now][0] = dp[now//2][0]+1
            dp[now][1] = list(dp[now//2][1])+[now]
    
print(dp[n][0])
for x in range(len(dp[n][1])-1,-1,-1):
    print(dp[n][1][x], end = " ")