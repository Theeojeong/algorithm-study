import sys
# sys.stdin=open("input.txt", "rt")

n, k=map(int, input().split())
x=list(map(int, input().split()))
y=[]

for i in range(n):
    for p in range(i+1, n):
        for q in range(p+1, n):
            y.append(x[i] + x[p] + x[q])
z=list(set(y))
z.sort(reverse=True)
print(z[k-1])