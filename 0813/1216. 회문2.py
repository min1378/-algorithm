import sys
sys.stdin = open("input.txt", "r")




def check(ls):
    result = 0
    for M in range(len(ls), -1, -1): 
        for i in range(len(ls)):
            for j in range(len(ls)-M+1):
                count = 0
                for k in range(M//2):                                 
                    if ls[i][j+k] != ls[i][M+j-1-k]:
                        break
                    count += 1
                    if count == M//2:
                        return M
        
        
    return result
def check2(ls):
    result = 0
    for M in range(len(ls), -1, -1):
        for i in range(len(ls)):
            for j in range(len(ls)-M+1):
                count = 0
                for k in range(M//2):                                 
                    if ls[j+k][i] != ls[M+j-1-k][i]:
                        break
                    count += 1
                    if count == M//2:
                        return M
    return result

T = 10
for test_case in range(1, T + 1):
    M = int(input())
    temp=[0]
    temp[0]=str(input())
    info=[0]*len(temp[0])
    info[0]=temp[0]
    for i in range(1, len(info[0])):
        info[i] = str(input())

    num1 = check(info)
    num2 = check2(info)
    if num1 > num2 :
        result = num1
    else :
        result = num2
    

    
    print('#{} {}'.format(test_case, result))