#dp[x] = x번째 집 도달시 money의 최적화
# #dp[x-1],dp[x-2]+money[x] 비교.
money = [1,2,3,1]
def solution(money):
    dp_y = [0]*len(money)
    dp_n = [0]*len(money)
    
    dp_y[0] += money[0]
    
    for x in range(2,len(money)-1):
        dp_y[x] = max(dp_y[x-1],dp_y[x-2]+money[x])
            
    for x in range(1,len(money)):
        dp_n[x] = max(dp_n[x-1],dp_n[x-2]+money[x])
    return max(max(dp_y),max(dp_n))    
print(solution(money))