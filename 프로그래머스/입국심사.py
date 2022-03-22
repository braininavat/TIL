# 왜 end가 아니라 start를 반환해야 하는가?
# 이진 탐색을 해가며 n==total을 만족하는 최솟값에 도달시
# n<=total 구문에 진입하여 end가 1 감소되고, start>end값을 만족시켜 반환됨.
# 이때 반환되는 값은 최솟값-1인 end가 아닌 최솟값인 start값이 반환되어야 하기때문
n = 10
times =[6,8,10]
def solution(n, times):
    start = 1
    end = max(times)*n
    
    def bsearch(start,end):
        
        if start > end:
            return start
        mid = (start+end)//2
        total =0
        for time in times:
            total+=mid//time
        if n <= total:
            return bsearch(start,mid-1)
        else:
            return bsearch(mid+1,end)
        
    answer = bsearch(start,end)
    return answer
solution(n,times)