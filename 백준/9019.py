import sys
from collections import deque
T = int(sys.stdin.readline())

def DSLR(num,i):
    if i == 0: 
        if num*2 >= 10000:
            return (num*2)%10000
        else:
            return num*2
    elif i == 1:
        if num == 0 :
            return 9999
        else:
            return num-1
    elif i == 2:
        return num%1000*10+num//1000
    elif i == 3:
        return num%10*1000+num//10

def bfs(start,target):
    q = deque()
    q.append([start,""])
    visited[start] = True
    inst_list = ['D','S','L','R']
    while q:
        prev,inst_prev = q.popleft()
        if prev == target:
            return inst_prev
        for x in range(4):
            newnum = DSLR(prev,x)
            if visited[newnum] == False:
                visited[newnum] = True
                newinst = inst_prev
                q.append([newnum,newinst+inst_list[x]])
        
while T:
    visited = [False]*10000
    start,target = map(int,sys.stdin.readline().split())
    print(bfs(start,target))
    T-=1
    
    