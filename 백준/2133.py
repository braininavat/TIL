#boj.kr/2133
n = int(input())

dp = [0]*31
dp[2] = 3

for x in range(4,31,2):
    dp[x] += dp[x-2]*3  #뒤에 3*2타일 붙이는경우(뒤에만 붙이면 중복 없음)
    for y in range(4,x+1,2): # 3*2n(n>2) 짜리 덩어리타일 붙이는경우
        dp[x] += dp[x-y]*2 # 스스로 덩어리를만드는경우
    dp[x] += 2

print(dp[n])