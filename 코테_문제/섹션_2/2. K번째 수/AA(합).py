import sys
# sys.stdin=open("input.txt", "rt")

T=int(input())

for i in range(T):
    n, s, e, k=map(int, input().split())
    x=list(map(int, input().split()))
    x=x[s-1:e]
    x=sorted(x)
    print(f"#{i+1}", x[k-1])    
