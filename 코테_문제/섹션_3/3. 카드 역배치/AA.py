import sys
import os

# BASE = os.path.dirname(__file__)
# sys.stdin = open(os.path.join(BASE, "in1.txt"), "rt")

card = list(range(1, 21))

for i in range(10):
    x, y = map(int, input().split())
    # print(x, y)
    # 5, 10 card[4:10] 5678910
    z = card[x-1:y]
    z = z[::-1]

    card[x-1:y] = z

for i in card:
    print(i, sep=" ", end=" ")






























# card = list(range(1, 21))

# for i in range(10):
#     a, b = map(int, input().split())
#     x = card[a-1:b]
#     x = x[::-1]
#     card[a-1:b] = x
#     # print(card)
# for j in card:
#     print(j, end=" ")
