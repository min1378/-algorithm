import sys
sys.stdin = open("input.txt", "r")
def Permutation(arr, r) :
    used = [0 for _ in range(len(arr))]
    result = []
    count = 0
    def generate(chosen, used) :
        
        if len(chosen) == r:
            result.append(chosen)   
            count += 1
        for i in range(len(arr)):
            if not used[i]:
                chosen.append(arr[i])
                used[i] = 1
                generate(chosen, used)
                used[i] = 0
                del chosen[-1]
        generate([], used)


T = int(input())
for test_case in range(1, T + 1):
    c = int(input())   
    info = []
    for i in range(100) :
        temp = list(map(int, input().split()))
        info.append(temp)
    
    #print('#{} {}'.format(test_case, result))