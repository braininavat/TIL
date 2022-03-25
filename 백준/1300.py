n = int(input())
k = int(input())

start = 1
end = n**2

while start<=end:
    mid = (start+end)//2
    low = mid//n
    total =n*low
    for x in range(low+1,min(n,mid)+1):
        total += mid//x
    if k <= total:
        end = mid-1
        answer = mid
    elif total <k:
        start = mid+1

print(answer)
