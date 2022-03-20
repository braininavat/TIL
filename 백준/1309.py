# 파이썬3의 int 형은 arbitary precision을 지원하기 때문에 
# 오버플로우가 발생하지 않는 대신, 저장되는 수의 크기에 비례해서 메모리 용량을 먹게된다.
# 그러므로 제때에 % 연산을 해주지 않으면 메모리 초과 발생
n = int(input())
dp_right=[0]*n
dp_left = [0]*n
dp_not = [0]*n

dp_right[0] = 1
dp_left[0] = 1
dp_not[0] = 1


for x in range(1,n):
    dp_right[x] = (dp_left[x-1] + dp_not[x-1])%9901
    dp_left[x] = (dp_right[x-1] + dp_not[x-1])%9901
    dp_not[x] = (dp_right[x-1] + dp_left[x-1]+dp_not[x-1])%9901
    
print((dp_right[n-1]+dp_left[n-1]+dp_not[n-1])%9901)
