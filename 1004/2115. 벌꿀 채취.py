TC = int(input())


def cal(list):
    global C
    max_result = 0
    list.sort()
    list.reverse()
    for i in range(len(list)):
        clone_C = C
        clone_C -= list[i]
        possibles = [list[i]]
        for j in range(len(list)):
            if i == j:
                continue
            if clone_C - list[j] >= 0:
                clone_C -= list[j]
                possibles.append(list[j])
        result = 0
        for i in possibles:
            result += i ** 2

        if max_result < result:
            max_result = result
    return max_result


def honey_choose(M):
    global max_reward
    for i in range(N):
        for j in range(N - M + 1):
            first = []
            for m in range(M):
                first += [data[i][j + m]]

            first_max = cal(first)

            for k in range(N):
                if k == i:
                    if j + M + M > N:
                        continue
                    for l in range(j + M, N - M + 1):

                        second = []
                        for m2 in range(M):
                            second += [data[k][l + m2]]

                        second_max = cal(second)
                        reward = first_max + second_max
                        if max_reward < reward:
                            max_reward = reward
                else:
                    for l in range(N - M + 1):
                        second = []
                        for m2 in range(M):
                            second += [data[k][l + m2]]

                        second_max = cal(second)
                        reward = first_max + second_max

                        if max_reward < reward:
                            max_reward = reward


for test_case in range(1, TC + 1):
    N, M, C = map(int, input().split())
    data = [list(map(int, input().split())) for _ in range(N)]
    max_reward = 0
    honey_choose(M)
    print("#{} {}".format(test_case, max_reward))