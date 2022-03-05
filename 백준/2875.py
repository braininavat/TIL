import sys
n,m,k = map(int,sys.stdin.readline().split())

result = 0
for x in range(k+1):
    tmp = min((n-x)//2,m-k+x)
    result = max(result,tmp)
print(result)