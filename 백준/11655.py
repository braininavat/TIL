s = list(input())
result = []
for alpha in s :
    if ord("a") <= ord(alpha) <= ord("z"):
        if ord(alpha)+13 > ord("z"):
            result.append(chr(ord("a")+ord(alpha)-ord("z")+12))
        else:
            result.append(chr(ord(alpha)+13))
    elif ord("A")<= ord(alpha) <= ord("Z"):
        if ord(alpha)+13 > ord("Z"):
            result.append(chr(ord("A")+ord(alpha)-ord("Z")+12))
        else:
            result.append(chr(ord(alpha)+13))
    else:
        result.append(alpha)
print("".join(result))