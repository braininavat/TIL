
#Counter 모듈: 결과값 정렬 X, sort() 시켜준 뒤에 결과값을 반환해야했음. 
import sys
from collections import Counter
n = int(input())
numbers = []
for x in range(n):
    numbers.append(int(sys.stdin.readline()))
numbers.sort()
result_list = Counter(numbers).most_common(1)
result = result_list[0][0]
print(result)