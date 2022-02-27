#boj.kr/2805

#내코드 : 이분탐색
import sys
n, m = map(int, sys.stdin.readline().split())
trees = list(map(int,sys.stdin.readline().split()))
start= 0
end = max(trees) 

while start <= end: 
    mid = (start+end) // 2
    total = 0
    
    for tree in trees:
        if tree >= mid:
            total += tree - mid
    
    if total >= m:
        start = mid + 1
    else:
        end = mid - 1        
print(end)

#다른사람코드 = Counter 사용
"""
import sys
input = sys.stdin.readline
from collections import Counter

def bs(target, start, end):
    res = 0
    while start <= end:
        mid = (start + end) // 2
        tmp = sum((h - mid) * c for h, c in tree_c.items() if h > mid)
        if tmp < target:
            end = mid - 1
        else:
            res = mid
            start = mid + 1
    return res

n, m = map(int, input().split())
tree_c = Counter(map(int, input().split()))
print(bs(m, 0, max(tree_c)))
"""
