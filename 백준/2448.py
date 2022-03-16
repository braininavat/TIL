#크기 줄여가며 분할및 정복 사용
n = int(input())
stars = [[' ']*2*n for _ in range(n)]

def star(row, col, size):
    if size == 3:
        stars[row][col] = stars[row + 1][col - 1] = stars[row + 1][col + 1] = "*"
        for k in range(-2, 3):
            stars[row + 2][col - k] = "*"
    else:
        size = size//2
        star(row, col, size)
        star(row + size, col - size, size)
        star(row + size, col + size, size)
star(0,n-1,n)
for star in stars:
    print("".join(star))