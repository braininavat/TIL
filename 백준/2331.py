import sys
a, p = map(int,sys.stdin.readline().split())
d = [a]
result = -1
while result ==-1:
    for x in range(len(d)-1):
        if d[-1] == d[x]:
            result = x
            break
    num = 0
    for x in str(d[-1]):
        num+=int(x)**p
    d.append(num)
print(result)