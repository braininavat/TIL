#boj.kr/9466
#내코드 = 현재 사이클을 dict에 저장 후 읽어오는 방식 사용
import sys
t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    graph = [0]+ list(map(int,sys.stdin.readline().split()))
    visited = [0]*(n+1)
    visit_now = {}
    result = 0
    
    for x in range(1,n+1):
        if visited[x] == 0:
            visited[x] = 1
            cnt = 1
            visit_now[x] = cnt
            nxt = graph[x]
            while True:
                if visited[nxt] == 0:
                    if nxt == graph[nxt]:
                        result +=len(visit_now)
                        visited[nxt] = 1
                        break
                    else:
                        cnt+=1
                        visit_now[nxt] = cnt
                        visited[nxt] = 1
                        nxt = graph[nxt]
                else: #방문했던노드일때
                    if visit_now.get(nxt): #루프 성립시
                        visited[nxt] = 1
                        result += visit_now.get(nxt)-1
                    else: #루프성립X
                        result +=len(visit_now)
                    break
            visit_now.clear()
    print(result)
                        
                        
#다른사람코드 
#발상은 같지만 backtrack 변수로 풀어내는 방식이 더 세련된거같다..
    """def solution(n, students):
    visited = [False] * (n + 1)
    count = 0

    for i in range(1, n+1):
        if not visited[i]:
            
            # 사이클 발견시까지 진행
            current = i 
            while not visited[current]:
                visited[current] = True
                current = students[current]
            
            # current 는 사이클을 완성하는 학생
            #backrack 은 사이클의 최초 학생
            # 사이클 최초~ 마무리 학생까지는 팀을 이룰수없음
            backtrack = i
            while backtrack != current:
                backtrack = students[backtrack]
                count += 1
            
    return count

T = int(input())

for _ in range(T):
    n = int(input())
    students = [0] + list(map(int, input().split()))

    print(solution(n, students))
    """