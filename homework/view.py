# def min_v(a , b) :
#     if a < b :
#         return a
#     else : 
#         return b

# T = 10
# for test_case in range(1, T+1):
#     size = int(input())
#     view_high = [0]*size
#     view_high = list(map(int, input().split()))
#     result = 0
#     result_2 = 0
#     for i in range(2 , size-2) :

#         v_1 = view_high[i] - view_high[i-1] 
#         v_2 = view_high[i] - view_high[i-2]
#         v_3 = view_high[i] - view_high[i+1]
#         v_4 = view_high[i] - view_high[i+2]

#         if v_1 <= 0 or v_2 <= 0 or v_3 <= 0 or v_4 <= 0 :
#             result_2 = result_2

#         else :
#             result = min_v(min_v(v_1, v_2), min_v(v_3, v_4))
#             if result > 0 :
#                 result_2 += result
#     print('#{} {}'.format(test_case, result_2))

# T = 10
# for test_case in range(1, T+1):
#     size = int(input())
#     view_high = [0]*size
#     view_high = list(map(int, input().split()))
#     result = 0
#     for i in range(2, size-2) :
#         view = 0
#         maxvalue = view_high[i-2]
#         for s in range(i-2, i+3) :
#             if s == i:
#                 pass
#             elif maxvalue < view_high[s] :       
#                 maxvalue = view_high[s]
        
#         view = view_high[i] - maxvalue 

#         if view > 0 :
#             result += view
#     print('#{} {}'.format(test_case, result))     
