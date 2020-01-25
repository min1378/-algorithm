import sys
sys.stdin = open('input.txt', 'r')

N = int(input())
number = []
for _ in range(N):
    temp = int(input())
    number.append(temp)

number.sort()

for i in range(N):
    print(number[i])