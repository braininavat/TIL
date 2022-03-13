#boj.kr/1107
#그리디로 접근했으나 쉽지않아서 포기.
#최대 반복수 백만->브루트포스이용
#chkrange 범위를 잘못잡으면 시간초과 발생. 
import sys
n = str(sys.stdin.readline().strip())#목표채널
m = int(sys.stdin.readline())#고장난버튼개수
broken = []
if m != 0:
    broken = list(map(str,sys.stdin.readline().split()))

def chk(num):
    for s in str(num):
        if s in broken:
            return -1
    return len(str(num))+abs(num-int(n))

result = abs(int(n)-100)

if m != 10: # 모두 사용불가
    cnt = 0
    chkrange = min((len(n)+1)**10,1000000)
    while cnt <= chkrange:
        chkresult = chk(cnt)
        if chkresult != -1:
            result = min(result,chkresult)
        cnt+=1
print(result)