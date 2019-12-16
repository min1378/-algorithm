import sys
sys.stdin = open("sample_input.txt", "r")

# def check(ls):
#     for i in range(len(ls)//2):
#         if ls[i] != ls[len(ls)-1-i]:
#             return False
#     return True

# T = int(input())
# for test_case in range(1, T + 1):
#     temp = list(map(int,input().split()))
#     N = temp[0]
#     M = temp[1]
#     info = [0]*N
#     transinfo = ['']*N
#     result = False
#     for i in range(N):
#         info[i] = str(input())
    
#     for i in range(N):
#         for j in range(N):
#             transinfo[i] += str(info[j][i])
     
#     print(test_case, len(transinfo), len(info))
#     for j in range(N):
#         check1 = check(info[j])
#         if check1 == True :
#             result = info[j]
#             break
#         check1 = check(transinfo[j])
#         if check1 == True :
#             result = transinfo[j]
#             break        
#     print('#{} {}'.format(test_case, result))


    #M의 길이 회문만 검색하는거임!!

def check(ls, M):
    result = ''
    for i in range(len(ls)):
        for j in range(len(ls)-M+1):
            count = 0
            for k in range(M//2):                                 
                if ls[i][j+k] != ls[i][M+j-1-k]:
                    break
                count += 1
                if count == M//2:
                    for m in range(M):
                        result += ls[i][j+m]
                    return result
def check2(ls, M):
    result = ''
    for i in range(len(ls)):
        for j in range(len(ls)-M+1):
            count = 0
            for k in range(M//2):                                 
                if ls[j+k][i] != ls[M+j-1-k][i]:
                    break
                count += 1
                if count == M//2:
                    for m in range(M):
                        result += ls[j+m][i]
                    return result

T = int(input())
for test_case in range(1, T + 1):
    temp = list(map(int,input().split()))
    N = temp[0]
    M = temp[1]
    info = [0]*N
    for i in range(N):
        info[i] = str(input())
    result = check(info, M)
    if result == None:
        result = check2(info,M)
    

    
    print('#{} {}'.format(test_case, result))