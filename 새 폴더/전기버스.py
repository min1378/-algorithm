import sys
sys.stdin = open("electric_input.txt", "r")


T = int(input())
for test_case in range(1, T + 1):
    count = 0
    info = list(map(int, input().split()))
    stop = list(map(int, input().split()))   
    K = info[0] 
    N = info[1]
    M = info[2]
    charge_gate = [0] * (N+1)
    charge_count = [0] * (N+1)
    for i in range(M) :
        charge_gate[stop[i]] += 1
    distance = 0
    charge = True
    while distance < N :
        if charge_count[distance] > 1 :
            count = 0 
            break
        if charge :
            distance += K
            charge = False
        elif charge_gate[distance] == 1 :
            charge = True
            charge_count[distance] += 1
            count += 1
                
        elif charge_gate[distance] != 1 :
            distance -= 1   
    print('#{} {}'.format(test_case, count))