import sys
# sys.stdin=open("input.txt", "rt")

n=int(input())
k=list(map(int, input().split()))

def digit_sum(x):
    z=[]
    j=list(map(int, str(x)))
    for i in j:
        z.append(i)
        q=sum(z)
    return q # 자릿수의 합

Max=float('-inf')
for i in range(n):
    if digit_sum(k[i])>Max:
        Max=digit_sum(k[i])
        max_number=k[i]
print(max_number)
        