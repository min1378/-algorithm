import sys
sys.stdin = open('13458.txt', 'r')
TC = int(input())
#for test_case in range(1, TC+1):
N = int(input())
data = list(map(int, input().split()))
B, C = map(int, input().split())

count = 0
for i in range(len(data)):
    if data[i] > B:
        data[i] -= B

        if data[i] % C == 0:
            count += data[i] // C
        else :
            count += data[i] // C + 1
    count += 1
print(count)


