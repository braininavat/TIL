#boj.kr/2225
#내코드 : dp[n][k] += dp[n~0][k-1], 3중 for문 사용하게됨..
n, k = map(int,input().split())

dp = [[0 for _ in range (k+1)]for _ in range(n+1)] 

for x in range(n+1):
    dp[x][1] = 1
    if k > 1:
        dp[x][2] = x+1

for x in range(3,k+1):
    for y in range(n+1):
        for z in range(y+1):
            dp[y][x] += dp[z][x-1]
        dp[y][x] = dp[y][x]%1000000000

print(dp[n][k])

#다른사람코드 
# dp[n][k] += dp[n~0][k-1] 은 
# dp[n][k-1]+dp[n-1][k]와 동일함!
"""
N,K = input().split()
N = int(N)
K = int(K)

def fac(a):
    facto = 1
    for i in range(1,a+1):
        facto *= i
    return facto

ans = fac(N+K-1) // (fac(N)*fac(K-1))
print(ans%1000000000)
"""