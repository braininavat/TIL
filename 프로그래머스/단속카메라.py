https://programmers.co.kr/learn/courses/30/lessons/42884

def solution(routes):
    answer = 1
    routes.sort(key = lambda x : x[1])
    camera = routes[0][1]
    for route in routes:
        if camera < route[0]:
            camera = route[1]
            answer+=1
    return answer