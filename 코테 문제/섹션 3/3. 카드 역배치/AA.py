import sys

card = list(range(1, 21))

for i in range(10):
    a, b = map(int, input().split())
    x = card[a-1:b]
    x = x[::-1]
    card[a-1:b] = x
    # print(card)
for j in card:
    print(j, end=" ")
    