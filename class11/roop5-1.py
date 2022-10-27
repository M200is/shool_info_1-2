from re import I


n = int(input("정수 입력: "))
c = 1

while c <= n:
    if c % 3 == 0:
        c += 1
        continue
    print(c, end=' ')
    c += 1
