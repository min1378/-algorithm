import sys
sys.stdin = open('4880.txt', 'r')
# 1은 가위, 2는 바위, 3은 보

def divide_conquer(start, mid, end):
    if end - start == 0:
        return
    else:
        divide_conquer(start, (mid + start) // 2, mid)
        divide_conquer(mid + 1, (mid + 1 + end) // 2, end)

    first = second = -1
    for i in range(start, end + 1):
        if i in index_list:
            if first < 0:
                first = i
            else:
                second = i
    print(second)
    if rss_list[first] == 1:
        if rss_list[second] == 2:
            index_list.remove(first)
        else:
            index_list.remove(second)
    elif rss_list[first] == 2:
        if rss_list[second] == 3:
            index_list.remove(first)
        else:
            index_list.remove(second)
    else:
        if rss_list[second] == 1:
            index_list.remove(first)
        else:
            index_list.remove(second)
    # print(index_list)


for tc in range(1, int(input().strip()) + 1):
    n = int(input().strip())
    rss_list = list(map(int, input().strip().split()))
    index_list = list(a for a in range(n))
    print(n)
    print(rss_list)
    print(index_list)
    divide_conquer(0, (n - 1) // 2, n - 1)

    print('#%d %d' %(tc, index_list.pop() + 1))