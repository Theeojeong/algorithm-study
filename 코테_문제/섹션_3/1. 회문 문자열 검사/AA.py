import os, sys

BASE = os.path.dirname(__file__)
sys.stdin = open(os.path.join(BASE, "in1.txt"), "rt")


N = int(input())

#             # 0 1 2 3 4
# for i in range(N):
#     x = input()
#     x = x.upper() # LEVEL
#                     # 0, 1
#     for j in range(len(x)//2):
#         if x[j] != x[-1-j]:
#             print(f"#{i+1} NO")
#             break
#     else:
#         print(f"#{i+1} YES")


for i in range(N):
    x = input()
    x = x.upper()

   #print(x[::-1])
    if x != x[::-1]:
        print(f"#{i+1} NO")
    else:
        print(f"#{i+1} YES")
