def check(ls, M):
    result = 0
    for i in range(len(ls)):
        for j in range(len(ls)-M+1):
            count = 0
            for k in range(M//2):                                 
                if ls[i][j+k] != ls[i][M+j-1-k]:
                    break
                count += 1
                if count == M//2:
                    result +=1
    return result
def check2(ls, M):
    result = 0
    for i in range(len(ls)):
        for j in range(len(ls)-M+1):
            count = 0
            for k in range(M//2):                                 
                if ls[j+k][i] != ls[M+j-1-k][i]:
                    break
                count += 1
                if count == M//2:
                    result +=1
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
    result = check(info, M)
    num1 = check(info, M)
    num2 = check2(info, M)
    result = num1 + num2
     
 
     
    print('#{} {}'.format(test_case, result))