def Quicksort(nums):
    mid = nums[0]
    left = []
    right = []
    result_mid = []
    for num in nums:
        if mid < num: right.append(num)
        elif mid > num: left.append(num)
        else: result_mid.append(num)
    if len(left) > 1:
        left = Quicksort(left)
    if len(right) > 1:
        right = Quicksort(right)
    result = left[:] + result_mid[:] + right[:]
    return result
for tc in range(1, 1 + 1):
    N = 1000000
    num_list = [i for i in range(1,N+1)]
    num_list = list(reversed(num_list))
    print('#d', Quicksort(num_list)[N//2])