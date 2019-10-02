import sys
sys.stdin = open('1952.txt', 'r')
TC = int(input())

def compare(i, sum_min):
    global  min_cost_sum
    clone_sum = sum_min

    for j in range(i, 10):
        one_month_costs = month_min_cost[j] + month_min_cost[j+1] + month_min_cost[j+2]
        if one_month_costs > three_month_cost:
            sum_min = clone_sum - one_month_costs + three_month_cost

            if min_cost_sum > sum_min:
                min_cost_sum = sum_min

            if j + 3 <= 10:
                compare(j + 3, sum_min)
for test_case in range(1, TC+1):
    cost_info = list(map(int, input().split()))
    plan_info = list(map(int, input().split()))
    day_cost = cost_info[0]
    month_cost = cost_info[1]
    three_month_cost = cost_info[2]
    year_cost = cost_info[3]
    month_min_cost = [0] * 12

    for month in range(12):
        month_min_cost[month] = min(plan_info[month] * day_cost, month_cost)
    min_cost_sum = sum(month_min_cost)

    print(month_min_cost)
    compare(0, min_cost_sum)

    if min_cost_sum > year_cost:
        min_cost_sum = year_cost

    print("#{} {}".format(test_case, min_cost_sum))









