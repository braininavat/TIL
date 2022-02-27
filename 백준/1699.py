n = int(input())
dp = [x for x in range(n+1)]

for x in range(2,n+1):
    for y in range(2,x):
        if y*y > x:
            break
        if dp[x] > dp[x-y*y]:
            dp[x] = dp[x-y*y]+1
        
print(dp[n])