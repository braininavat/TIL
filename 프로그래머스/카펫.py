https://programmers.co.kr/learn/courses/30/lessons/42842

def solution(brown, yellow):
    sqrt=int(yellow**(1/2))
    for x in range(1,sqrt+1):
        if yellow%x ==0:
            a = yellow//x
            b = x
            if 2*a+2*b+4 == brown:
                   return [a+2,b+2] 
    return -1