n, m = map(int, input("정수 입력: ").split())
c1 = 1
c2 = 1

while c1 <= n:
    while c2 <= m:
        print(c1, c2)
        c2 += 1
    c2 = 1
    c1 += 1
