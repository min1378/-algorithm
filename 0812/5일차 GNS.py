import sys
sys.stdin = open("input.txt", "r")


# T = int(input())
# for test_case in range(1, T + 1):
#     info1 = list(input().split())
#     N=int(info1[1])
#     count = [0]*10
#     other = ['ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN']
#     info2 = list(map(str, input().split()))
#     result = ''
#     for i in info2:
#         if i == 'ZRO':
#             count[0] += 1
#         elif i == 'ONE':
#             count[1] += 1
#         elif i == 'TWO':
#             count[2] += 1
#         elif i == 'THR':
#             count[3] += 1
#         elif i == 'FOR':
#             count[4] += 1
#         elif i == 'FIV':
#             count[5] += 1
#         elif i == 'SIX':
#             count[6] += 1
#         elif i == 'SVN':
#             count[7] += 1
#         elif i == 'EGT':
#             count[8] += 1
#         elif i == 'NIN':
#             count[9] += 1
#     for i in range(len(count)):
#         for j in range(count[i]):
#             result +=' ' + other[i]             
#     print('#{} {}'.format(test_case, result))
code = ['ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN']
testcase = int(input())
for tc in range(1, testcase+1):
    n = input()
    s = input()
    ans = ''
    for i in range(len(code)):
        ans += (code[i] + ' ')*s.count(code[i])
    print("#%d\n%s" %(tc,ans))