#boj.kr/2579
import sys
n = int(sys.stdin.readline())
dp_one = [0]*n#건너뛰어서 1개밟는경우
dp_two = [0]*n#이전꺼바로밟는경우

for x in range(n):
    dp_one[x] = int(sys.stdin.readline())

for x in range(n):
    dp_two[x] = dp_one[x]

if n!= 1:
    dp_two[1] = dp_one[0]+dp_one[1]

    for x in range(2,n):
        dp_one[x] += max(dp_two[x-2],dp_one[x-2])
        dp_two[x] += dp_one[x-1]
    
print(max(dp_one[n-1],dp_two[n-1]))