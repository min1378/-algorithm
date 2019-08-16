import sys
sys.stdin = open("input.txt", "r")

def amax(a, b) :
    if a > b :
        return a
    else :
        return b


T = 10
for test_case in range(1, T + 1):
    info = []
    count = 0
    sum_width = 0
    sum_height = 0
    sum_right = 0
    sum_left = 0
    c = int(input())
    for i in range(100) :
        line = list(map(int, input().split()))
        info.append(line)
        
    for x in range(len(info)) :
        temp = 0
        for y in range(len(info[x])):
            temp += info[x][y]
        if sum_width < temp :
            sum_width = temp

    for y in range(len(info[0])) :
        temp = 0
        for x in range(len(info)):
            temp += info[x][y]
        if sum_height < temp :
            sum_height = temp
    
    for x in range(len(info)) :
        for y in range(len(info[x])):
            if y == x :
                sum_right += info[x][y]

    for y in range(len(info[0])) :            
            for x in range(len(info)):
                if x + y == len(info) :
                    sum_left += info[x][y]

    result = amax(amax(sum_width, sum_height),amax(sum_left,sum_right))
    print('#{} {}'.format(test_case, result))