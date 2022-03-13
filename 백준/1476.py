e,s,m = map(int,input().split())
n = 1
while True:
    if (n-e)%15 == (n-s)%28 == (n-m)%19 == 0:
        break
    else:
        n = n+1
print(n)