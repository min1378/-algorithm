#import sys
#sys.stdin = open("sample_input.txt", "r")

T = int(input())
for test_case in range(1, T+1):    
    size = int(input())
    numbers = int(input())
    count = [0] * 10
    max_value = count[0]
    max_number = 0
    for i in range(size) :
        temp = numbers % 10
        numbers = numbers // 10
        count[temp] += 1
    for i in range(1,11) :

        if max_value < count[10-i] :
            max_value = count[10-i]
            max_number = 10-i
    print('#{} {} {}'.format(test_case, max_number, max_value))