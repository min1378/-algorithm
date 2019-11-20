import sys
sys.stdin = open("sample_input.txt", "r")


T = int(input())
for test_case in range(1, T + 1):
    info =[]
    count = int(input())
    sketch = []
    # sketch 10X10 2차원배열 생성
    for i in range(100) :
        temp=[]
        for j in range(100):
            temp.append(0)
        sketch.append(temp)
    # 색칠할 위치 input값 받기 
    for i in range(count) :
        line = list(map(int, input().split()))
        info.append(line) 
    
    for i in range(count) :
        
        if info[i][-1] == 1 :
            for j in range(abs(info[i][0]-info[i][2])+1):
                for k in range(abs(info[i][1]-info[i][3])+1):
                    sketch[info[i][0]+j][info[i][1]+k] += 1
        else :
            for j in range(abs(info[i][0]-info[i][2])+1):
                for k in range(abs(info[i][1]-info[i][3])+1):
                    sketch[info[i][0]+j][info[i][1]+k] += 2
    result = 0
    for i in range(10):
        for j in range(10):
            if sketch[i][j] == 3 :
                result += 1

    print('#{} {}'.format(test_case, result))