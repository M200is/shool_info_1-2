n = int(input("정수 입력: "))
s = 0

for i in range(1, n+1):
    if i % 2 == 0:
        s += i

print(f"1에서 {n} 까지의 짝수의 합: {s}")
