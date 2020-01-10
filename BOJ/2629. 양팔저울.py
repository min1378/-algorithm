import sys
sys.stdin = open('2629.txt', 'r')
TC = 1
def binarySearch(answer):

    left = m_data[0]
    right = m_data[-1]

    if left == answer:
        return "Y"
    if right == answer:
        return "Y"
    mid = (left + right) // 2
    if mid < answer:
        




for test_case in range(1, TC+1):
    N = int(input())
    n_data = map(int, input().split())
    M = int(input())
    m_data = map(int, input().split())
    result = ""
    for i in range(M):
        answer = m_data[i]
        result += binarySearch(answer) + " "
    print(result)
