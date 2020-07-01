def solution(prices):
    end = len(prices)
    
    answer = [0]* len(prices)
    for i in range(end-1):
        for j in range(i, end-1):
            print(i, j, answer)
            if prices[i] > prices[j]: 
                break
            else: 
                answer[i] += 1
    return answer


print(solution([ 1, 2, 3, 2, 3, 1 ]))