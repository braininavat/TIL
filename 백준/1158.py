import sys
n,k = map(int,sys.stdin.readline().split())
jp = []
circle = [x for x in range(1,n+1)]
now = 0


for _ in range(n):
    now +=k-1
    now %=len(circle)
    jp.append(circle.pop(now)) 
    
        
print("<", end = '')
print(", ".join((str(i) for i in jp)), end = '')
print(">")
                