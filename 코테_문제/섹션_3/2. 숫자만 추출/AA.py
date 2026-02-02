import sys

x = input()

digits = [i for i in x if i.isdigit()]
number = int("".join(digits))
print(number)

count=0
for i in range(1, number+1):
    if number%i == 0:
        count = count + 1
print(count)