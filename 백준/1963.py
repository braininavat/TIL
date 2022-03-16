#현재 소수에서 한자리만 다른 소수를 전부 찾아서 리스트로 리턴하려고 하니 시간초과 발생..
#한 자리만 바꿔서 소수인지 판별하는 방법으로 교체
#1~1000의 소수를 False 로 놓지 않으면 0xxx~9xxx의 BFS 실행시 3자리수의 잘못된 값을 큐에 넣는다.
import sys
from collections import deque
primes=[True for x in range(10000)]

def findprime():
    primes[0] = False
    primes[1] = False
    for x in range(2,101):
        now = x
        if primes[now] == True:
            now += x
            while now < 10000:
                primes[now]=False
                now +=x
    for x in range(1,1001):
        primes[x] = False                
findprime()

T = int(sys.stdin.readline())
while T:
    start, target = map(int,sys.stdin.readline().split())
    visited = [False]*10000
    result = "Impossible"
    q = deque()
    if primes[start] == True:
        q.append([start,0])
        visited[start]=True
    while q:
        q_tmp = q.popleft()
        now = q_tmp[0]
        count = q_tmp[1]
        if now == target:
            result = count
            break
        for i in range(4):
            tmp = (now//(10**i)%10)
            new_now = now-tmp*(10**i)
            for _ in range(10):
                if primes[new_now] == True:
                    if visited[new_now] == False:
                        visited[new_now] = True
                        q.append([new_now,count+1])
                new_now = new_now+(10**i)
    print(result)
    T-=1