https://programmers.co.kr/learn/courses/30/lessons/42898


def solution(m, n, puddles):
    map_mn = [[-1 for _ in range(m)]for _ in range(n)]
    
    for x in range(1,m):
        map_mn[0][x] = 1
    for x in range(1,n):
        map_mn[x][0] = 1
        
    for puddle in puddles:
        if (puddle[0]-1) == 0:
            for x in range(puddle[1]-1,n):
                map_mn[x][0] = 0
        elif (puddle[1]-1) == 0:
            for x in range(puddle[0]-1,m):
                map_mn[0][x] = 0
        else:
            map_mn[puddle[1]-1][puddle[0]-1] = 0
        
    for x in range(1,n):
        for y in range(1,m):
            if map_mn[x][y] != 0:
                map_mn[x][y] = (map_mn[x-1][y] + map_mn[x][y-1])%1000000007
                
    answer = map_mn[n-1][m-1]
    return answer