import sys
sys.stdin = open("sample_input.txt", "r")

def selectionSort(a) :
    for i in range(0, len(a)-1):
        min = i
        for j in range(i+1, len(a)):
            if a[min] > a[j] :
                min = j
        a[i],a[min] = a[min],a[i]
           
T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    numbers = list(map(int, input().split()))
    big = []
    small = []
    selectionSort(numbers)
    for i in range(len(numbers)):
        small.append(numbers[i])
        big.append(numbers[len(numbers)-1-i])

    result = []
    
    for i in range(5) :
        result.append(big[i])
        result.append(small[i])
    
    print('#{}'.format(test_case), end=" ")
    for i in range(len(result)):print(result[i], end=" ")
    print()