#백트래킹 말고 bfs이용

from collections import deque
target = int(input())
q = deque()
count = 0
result = -1

for x in range(10):
    q.append(x)
    count+=1
    if target == count:
        result = x
while q and result == -1:
    now = q.popleft()
    left = now%10
    for x in range(left):
        nxt = now*10+x
        count+=1
        if target == count:
            result = nxt
            break
        q.append(nxt)
        
    
print(result)
