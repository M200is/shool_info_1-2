n = int(input("정수 입력: "))
c = 0

while c < n:
    c += 1
    if c % 3 == 0:
        continue
    print(c, end=' ')
