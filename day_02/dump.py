import sys
sys.stdin = open("dump_input.txt", "r")

# T = 10
# for test_case in range(1, T + 1):
#     dump = int(input())
#     count = dump
#     height = list(map(int, input().split()))
#     result = 2
#     for i in range(dump) :
#         d_max = height[0]
#         d_min = height[0]
#         d_max_index = 0
#         d_min_index = 0
#         for r in range(len(height)) : 
#             if d_max < height[r] :
#                 d_max = height[r]
#                 d_max_index = r
#             if d_min > height[r] :
#                 d_min = height[r]
#                 d_min_index = r
#         height[d_max_index] = height[d_max_index] - 1
#         height[d_min_index] = height[d_min_index] + 1
#         result = d_max - d_min
#         if result == 0 or result == 1 :
#             d_max = height[0]
#             d_min = height[0]
#             for r in range(len(height)):
#                 if d_max < height[r] :
#                     d_max = height[r]

#                 if d_min > height[r] :
#                     d_min = height[r]
#             result = d_max - d_min
#             break
#         if count == 0 :
#             d_max = height[0]
#             d_min = height[0]
#             for r in range(len(height)):
#                 if d_max < height[r] :
#                     d_max = height[r]

#                 if d_min > height[r] :
#                     d_min = height[r]
#             result = d_max - d_min
#             break
#         count -= 1
#         d_max = height[0]
#         d_min = height[0]
#         for r in range(len(height)):
#             if d_max < height[r] :
#                 d_max = height[r]

#             if d_min > height[r] :
#                 d_min = height[r]
#         result = d_max - d_min           
#     print('#{} {}'.format(test_case, result))







