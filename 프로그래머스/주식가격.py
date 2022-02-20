#https://programmers.co.kr/learn/courses/30/lessons/42584

prices = [1,2,3,2,3]

def solution(prices):
    answer = [0]*len(prices)
    for x in range(len(prices)):
        for y in range(x+1,len(prices)):
            if prices[x]>prices[y]:
                answer[x] = y-x
                break
            answer[x] +=1
    return answer
print(solution(prices))