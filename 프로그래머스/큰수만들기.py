import sys
sys.setrecursionlimit(10**9)

#내코드(재귀이용, 시간초과. 최악의 경우 O(n^2))
def solution(number,k):
    if k == 0:
        return number
    for x in range(1,len(number)):
        if number[x-1]<number[x]:
            number = number[:x-1]+number[x:]
            return solution(number,k-1)
    number = number[:-k]
    return number

#다른사람코드(스택 이용, O(N))

def solution(number, k):
    stack = [number[0]]
    for num in number[1:]:
        while len(stack) > 0 and stack[-1] < num and k > 0:
            stack.pop()
            k -= 1
        stack.append(num)
    if k != 0:
        stack = stack[:-k]
    return ''.join(stack)
