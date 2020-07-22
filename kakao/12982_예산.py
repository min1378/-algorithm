def solution(d, budget):
    answer = 0
    d.sort() # 제일 작은 것부터 체크하기 위해서... O(nlogn)
    for value in d:
        budget -= value
        if  budget < 0:
            return answer
        answer += 1       
    return answer