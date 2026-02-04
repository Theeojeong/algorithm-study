import sys
import os

BASE = os.path.dirname(__file__)
sys.stdin = open(os.path.join(BASE, "in1.txt"), "rt")

x = input()

y = []

num = 0
        # g0en2T0s8eSoft
        # 1000
for i in x:
    if i.isdecimal():
        num = num * 10 + int(i)
print(num)


        















# x = input()

# digits = [i for i in x if i.isdigit()]
# number = int("".join(digits))
# print(number)

# count=0
# for i in range(1, number+1):
#     if number%i == 0:
#         count = count + 1
# print(count)
