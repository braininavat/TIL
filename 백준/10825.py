import sys
n = int(sys.stdin.readline())
students = [[0]for _ in range(n)]

for x in range(n):
    students[x] = sys.stdin.readline().split()
    
students.sort(key= lambda x:x[0])#이름순
students.sort(key= lambda x : int(x[3]),reverse=True)#수학점수감소
students.sort(key= lambda x : int(x[2]))#영어점수증가
students.sort(key= lambda x : int(x[1]),reverse=True)#국어점수감소

#key=lambda x : -int(x[1])도 가능

for x in range(n):
    print(students[x][0])
