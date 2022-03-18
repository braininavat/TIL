import sys
n = int(sys.stdin.readline())
pos = [] 
neg = []
result = 0

for _ in range(n):
    num = int(sys.stdin.readline())
    if num > 0 :
        pos.append(num)
    else:
        neg.append(num)

pos.sort(reverse=True)
neg.sort()

def bond(nlist):
    global result 
    if len(nlist) == 0:
        return
    elif len(nlist) == 1:
        result += nlist[0]
        return
    else:
        mult = nlist[0]*nlist[1] 
        add = nlist[0]+nlist[1]
        if mult > add:
            result+=mult
        else:
            result+=add
        bond(nlist[2:])
        
bond(pos)
bond(neg)
print(result)