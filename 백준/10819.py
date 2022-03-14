# shuffle 재귀함수의 맨 밑 두줄이 핵심
import sys
n = int(sys.stdin.readline())
a = list(map(int,sys.stdin.readline().split()))
new = []
result_arr = []

def function(lst):
    rst = 0
    for x in range(1,len(lst)):
        rst+=abs(lst[x-1]-lst[x])
    return rst

def shuffle(a,new,used):
    if len(new) == n:
        result_arr.append(function(new))
    else:
        for x in range(len(a)):
            if used[x] != 1:
                used[x] = 1
                new.append(a[x])
                shuffle(a,new,used)
                used[x] = 0
                new.pop()
            
shuffle(a,new,[0]*n)          
print(max(result_arr))