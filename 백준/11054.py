#boj.kr/11054
import sys 
n = int(sys.stdin.readline())
nlist = list(map(int,sys.stdin.readline().split()))

dp_inc = [1]*1000
dp_dec = [1]*1000

for x in range(len(nlist)):
    dp_inc_max = 0
    dp_dec_max = 0
    for y in range(x):
        if nlist[x] > nlist[y]:
            dp_inc_max = max(dp_inc_max,dp_inc[y])
        elif nlist[x] < nlist[y]:
            dp_dec_max = max(dp_dec_max,dp_inc[y],dp_dec[y])
    dp_inc[x] += dp_inc_max
    dp_dec[x] += dp_dec_max
    
print(max(max(dp_inc),max(dp_dec)))