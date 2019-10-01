import sys
sys.stdin = open('1952.txt', 'r')
TC = int(input())
def cal():
    while continue_list:
        temp = continue_list.pop()
        for three_count in range(len(temp)//3):
            for one_count in range(len(temp), -3, len(temp)- (3 * three_count)):
                for day_count in range()
                    result = cost_info[1] * one_count + cost_info[2] * three_count
                    if min_cost < result:
                        min_cost = result


for test_case in range(1, TC+1):
    cost_info = list(map(int, input().split()))
    plan_info = list(map(int, input().split()))
    min_cost = min(cost_info[-1], cost_info[0] * sum(plan_info))
    print(min_cost)
    continue_list = []
    count = 0

    start = -1
    for i in range(len(plan_info)):
        if start == -1 and plan_info[i] > 0:
            start = i

        if start != -1 and plan_info[i] == 0:
            continue_list.append(plan_info[start:i])
            start = -1

        if i == len(plan_info) - 1 and start != -1:
            continue_list.append(plan_info[start:])

    print(continue_list)
    cal()



