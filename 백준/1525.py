#dict 에 키 있는지 검사 : if 검사할값 not in 딕셔너리: 로 검색한다.
import sys
from collections import deque
start = ""
for x in range(3):
    line = "".join(sys.stdin.readline().split())
    start += line
moveto = [[1,0],[-1,0],[0,1],[0,-1]]
target = "123456780"
visited = {}
result = -1

        
def move(puzzle,znow,znew):
    newpuzzle = list(puzzle)
    newpuzzle[znow] = list(puzzle)[znew]
    newpuzzle[znew] = '0'
    return "".join(newpuzzle)

def bfs():
    q = deque()
    znow = start.index('0')
    q.append([start,znow,0])
    visited[start] = True
    while q:
        puzzle,znow,cnt=q.popleft()
        if puzzle == target:
            return cnt
        for x in range(4):
            row = znow//3+moveto[x][0]
            col = znow%3+moveto[x][1]
            if 0 <= row <= 2 and 0 <= col <= 2:
                znew = row*3+col
                newpuzzle = move(puzzle,znow,znew)
                if newpuzzle not in visited:
                    visited[newpuzzle] = True
                    q.append([newpuzzle,znew,cnt+1])
    return -1

print(bfs())

        