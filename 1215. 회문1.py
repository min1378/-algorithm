# 가로로 회문 체크
def check(ls, M):
    result = 0
    
    for i in range(len(ls)):
        # M 길이의 회문을 체크한다.
        for j in range(len(ls)-M+1):
            count = 0
            # M 길이의 반만 체크한다. 가운데를 기준으로 앞 뒤를 비교하면 되기 때문 
            for k in range(M//2):
                # 만약에 회문이 아니라면 카운트를 증가시키지 않고 다음 반복문 실행                               
                if ls[i][j+k] != ls[i][M+j-1-k]:
                    break
                count += 1
                # count가 M//2만큼 같아지면 회문이기 때문에 result에 1을 추가한다.
                if count == M//2:
                    result +=1
    return result

# 세로 회문 체크
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
    #입력 받기
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