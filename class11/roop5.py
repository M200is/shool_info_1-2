n = int(input("정수 입력: "))

for i in range(1, n+1):
    if i % 3 == 0:
        continue
    print(i, end=' ')
