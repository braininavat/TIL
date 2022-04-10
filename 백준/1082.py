import sys
n = int(sys.stdin.readline())
p = list(map(int,sys.stdin.readline().split()))
m = int(sys.stdin.readline())

dp = [0]*51

for x in range(len(p)):
    dp[p[x]] = x
    
for x in range(p[n-1],m+1):
    maxnum = dp[x-1]
    dp[x] = dp[x-1]
    for y in range(0,n):
        maxnum = max(maxnum, dp[x-p[y]]*10+y)
    dp[x] = maxnum
        
    
print(dp[m])