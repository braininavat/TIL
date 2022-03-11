#boj.kr/10820
#VS CODE에서 EOF는 ctrl+z로 발생시킬수있다.
# strip() 을 쓸때 문자열이 끝나고 공백이 이어지는경우도 고려해야함
while True:
    try:
        line = input()

        ucase, dcase, num, blank = 0, 0, 0, 0
        for i in line:
            if ord("a") <= ord(i) <= ord("z"):
                dcase += 1
            elif ord("A") <= ord(i) <= ord("Z"):
                ucase += 1
            elif ord("0") <= ord(i) <= ord("9"):
                num += 1
            elif i == " ":
                blank += 1
        print(dcase, ucase, num, blank, sep=" ")
    except EOFError:
        break
