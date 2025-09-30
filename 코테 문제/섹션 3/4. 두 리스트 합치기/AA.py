import sys

N = int(input())
# print(N)

List1 = list(map(int, input().split()))
# print(List1)

M = int(input())
# print(M)

List2 = list(map(int, input().split()))
# print(List2)

List3 = List1 + List2
List3.sort()
for i in List3:
    print(i, end=" ")