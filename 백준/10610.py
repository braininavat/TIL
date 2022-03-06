#30의 배수일 조건 : 각자리 숫자의합이 3이면서 0을포함
n = list(input())
n.sort(reverse=True)
result = 0
for x in n:
    result+=int(x)
if int(n[-1]) == 0 and result%3 == 0:
    print("".join(n))
else:
    print(-1)