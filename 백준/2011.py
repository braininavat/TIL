#boj.kr/2011
#내코드 = 점화식 세우는건 쉬웠는데 예외조건이 많아서 코드가 지저분해짐.
num = list(map(int,input()))
dp = [1]*len(num)
zcount = 0

if len(num) == 0 or num[0] == 0:
    print(0)
elif len(num) == 1:
    print(1)
elif num[0] > 2 and num[1] == 0:
    print(0)
else:
    if num[0]*10+num[1] < 27 and num[1] != 0:
        dp[1] = 2
    if num[1] == 0:
        zcount+=1

    for x in range(2,len(num)):
        if num[x] == 0:
            if num[x-1] > 2:
                print(0)
                zcount = 2 
                break
            zcount +=1
            dp[x] = dp[x-2]
            dp[x-1] = dp[x-2]
            if zcount == 2:
                print(0)
                break
        else:
            zcount = 0
            if num[x-1]*10+num[x] > 26 or num[x-1] == 0:
                dp[x] = dp[x-1]
            else:
                dp[x] = (dp[x-1]+dp[x-2])%1000000

    if zcount != 2:
        print(dp[len(num)-1])

#다른사람코드 : j = i+1로 dp를 1 크게 만들어서 코드 크기 줄임
#int로 변환하지 않고 바로 인덱스 슬라이싱
"""
mod = 1000000
s = input()
dp=[0]*5005
dp[0]=1
for i in range(len(s)):
    j=i+1 #dp
    a=int(s[i])
    b=int(s[i-1]+s[i])
    if 0<a and a<10:
        dp[j]=dp[j-1]%mod
    if 9<b and b<27:
        dp[j]=(dp[j]+dp[j-2])%mod
print(dp[len(s)])
"""