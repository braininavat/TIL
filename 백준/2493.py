import sys
n = int(sys.stdin.readline())
towers = list(map(int,sys.stdin.readline().split()))
stack = []
maxtower = -1
result = [0]*n

for i in range(n):
    if towers[i] > maxtower:    
        maxtower = towers[i]
        stack.clear()
        stack.append([towers[i],i])
    else:
        while towers[i] >= stack[-1][0]:
            tmp = stack.pop()
        tmp = stack[-1]
        stack.append([towers[i],i])
        result[i] = tmp[1]+1

for x in result:
    print(x, end = " ")

