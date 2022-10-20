n = int(input("정수 입력: "))
c = 0
while n > 0:
    if n % 2 == 1:
        c += 1
    n -= 1

print(f"홀수 개수: {c}")
