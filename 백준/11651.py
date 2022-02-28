import sys
n = int(sys.stdin.readline())
numbers  = [[0]for _ in range(n)]
for x in range(n):
    numbers[x] = list(map(int,sys.stdin.readline().split()))
    
numbers.sort(key= lambda x:x[0])
numbers.sort(key= lambda x:x[1])

for number in numbers:
    print(number[0],number[1],sep = " ")