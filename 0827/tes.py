# data = [[1,2], [3,4], [5,6], [7,8]]
# i = 0
# while True :
#     if i-1 > len(data) :
#         print("탈출")
#         break
#     del(data[i])
#     print(i, data)

# import sys
# from pprint import pprint
# sys.stdin = open('test.txt', 'r')
# TC = int(input())
# for test_case in range(1, TC+1):
#     N = int(input())
#     info = []
#     for _ in range(N):
#         temp = list(map(int, input().split()))
#         info.append(temp)
#     print("#{}".format(test_case))
#     pprint(info)
# check = [[1,2],[3,4],[5,6]]
# check.pop(2)
# print(check)
# temp = [i for i in range(N)]
#
# temp.remove(9)
# print(temp)
temp4 = {}
info = [[1, 2, 3, 4], [1, 2, 4, 5], [1, 3, 1, 1]]
for x, y, mode, count in info:
    if temp4.get((x, y)):
        temp4[(x, y)].append((mode, count))
    else:
        temp4[(x, y)] = [(mode, count)]

print(temp4)