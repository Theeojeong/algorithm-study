import sys
# sys.stdin=open("input.txt", "rt")

# N의 약수들 중
# K번째로 작은 수

# 조건 1. N의 약수의 갯수>=K
# 2. 1<=K<=N<=10000
# 3. 

N, K=map(int, input().split())

x=[]
for i in range(1,N+1):
    if N%i==0:
        x.append(i)    
if len(x)<K:
    print("-1")
else:
    print(x[K-1])   


