n = int(input())
for _ in range(n):
    ps = list(input())
    result = "YES"
    if ps[0] == ")":
        result = "NO"
    else:
        count = 0
        for x in range(len(ps)):
            if count < 0:
                result = "NO"
                break
            if ps[x] == "(":
                count+=1
            else:
                count-=1
        if count != 0:
            result = "NO"
    print(result)
            