import sys
# sys.stdin=open("input.txt", "rt")

n=int(input())
p=list(map(int, input().split()))

average=round(sum(p)/n)
arrMin=float('inf')

for idx, x in enumerate(p):
    if abs(average-x)<arrMin:
        arrMin=abs(average-x)
        score=x
        q=idx
    elif abs(average-x)==arrMin:
        if x>score:
            score=x
            q=idx    

print(average, q+1)