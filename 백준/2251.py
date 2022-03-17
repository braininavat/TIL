#함수 만들때 순서 한번 더 생각해보고, 깊은 복사로 값 오염되는 것 주의해서 코드 짤것.
import sys
jar = tuple(map(int,sys.stdin.readline().split()))
from collections import deque
visited =[[[False for _ in range(201)]for _ in range(201)]for _ in range(201)]
volume = [0,0,jar[2]]
result = [False]*201
def change(start,target,vol):
    margin = jar[target]-vol[target]
    if vol[start] <= margin:
        vol[target] += vol[start]
        vol[start] = 0
    else:
        vol[start] -= margin
        vol[target] += margin
    return vol


q = deque()
q.append(volume)
result[volume[2]]=True
visited[volume[0]][volume[1]][volume[2]] = True
while q:
    volnew = q.popleft()
    if volnew[0] == 0:
        result[volnew[2]] = True
    for i in range(3):
        for j in range(3):
            if i != j:
                tmp = change(i,j,volnew[:]) # shallow copy
                if visited[tmp[0]][tmp[1]][tmp[2]] == False:
                    visited[tmp[0]][tmp[1]][tmp[2]] = True
                    q.append(tmp)

for x in range(201):
    if result[x] == True:
        print(x)


