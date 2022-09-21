from dataclasses import replace
import random as rand

food=["김밥","떡볶이", "순대", "어묵", "국수", "튀김"]
print("분식 메뉴:", food)
a = list(rand.sample(range(0,6), 3))

print("선택 메뉴:", food[a[0]], food[a[1]], food[a[2]])