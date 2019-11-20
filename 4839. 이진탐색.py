import sys
sys.stdin = open("sample_input.txt", "r")

def bi_search(list_page):
    list_page[4] += 1
    if list_page[2] > list_page[3] :
        list_page[0] = list_page[3]
    else :
        list_page[1] = list_page[3]
    list_page[3] = int((list_page[0] + list_page[1])/2)    
    return list_page
T = int(input())
for test_case in range(1, T + 1):
    temp = list(map(int, input().split()))
    flag = 0
    A = [0]*5
    B = [0]*5
    A[0] = 1 #left
    B[0] = 1
    A[1] = temp[0] #right
    B[1] = temp[0]
    A[2] = temp[1] #page
    B[2] = temp[2]
    A[3] = int((A[0] + A[1])/2)
    B[3] = int((B[0] + B[1])/2)
    while flag != 1:
        if A[2] == A[3] :
            break
        else :
            bi_search(A)

    while flag != 1:
        if B[2] == B[3] :
            break
        else :
            bi_search(B)
    if A[4] > B[4] :
        end = 'B'
    elif A[4] == B[4] :
        end = 0
    else : 
        end = 'A'
    print('#{} {}'.format(test_case, end))