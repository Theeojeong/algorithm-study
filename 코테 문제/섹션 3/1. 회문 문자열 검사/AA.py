import sys

n = int(input())

for i in range(1, n+1):
    s = input()
    if s == 'q':
        break

    else:
        x = s.upper()
        # print(f"대문자로 변경: {x}") # level -> LEVEL

        y =[]

        for j in x:
            y.append(j)
        
        # print(y)

        if y == y[::-1]:
            print(f"#{i} YES")
        else:
            print(f"#{i} NO")