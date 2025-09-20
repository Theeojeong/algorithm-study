import sys

N = int(input())
x = []

for i in list(range(1, N+1)):
    if i == 1:
        continue

    is_prime = True

    for j in list(range(2, i)):

        if i%j == 0:
            is_prime = False
            break

    if is_prime:
        x.append(i)

print(len(x))