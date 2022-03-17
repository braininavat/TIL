n, m = map(int,input().split())
num = 1
den = 1
for x in range(1,m+1):
    num *=n
    n-=1
    den *=x
print(num//den)