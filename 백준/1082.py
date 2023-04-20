import sys
n = int(sys.stdin.readline()) #0~n-1까지의숫자
p = list(map(int,sys.stdin.readline().split()))
m = int(sys.stdin.readline()) #m원,모두사용

dp = [0]*51

for x in range(len(p)):
    dp[p[x]] = x


for x in range(1,m+1):
    maxnum = max(dp[x],dp[x]-1)
    for y in range(0,n):
        checknum = x-p[y]
        if checknum>0:
            maxnum = max(maxnum, dp[checknum]*10+y)
    dp[x] = maxnum
        
    
print(dp[m])