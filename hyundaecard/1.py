from datetime import date


def solution(purchase):
    answer = [0, 0, 0, 0, 0]
    
    amount = 0
    grade = 0
    days = {}
    for purch in purchase:
        date, cost = purch.split(" ")
        year, month, day = date.split("/")
        print(year, month, day, cost)

        amount += int(cost)
        if 20000> amount >= 10000:
            grade = 1
        elif 50000> amount:
            grade = 2
        elif 100000> amount:
            grade = 3
        elif 100000 <= amount:
            grade = 4
        
    return answer


print(solution(["2019/01/01 5000", "2019/01/20 15000", "2019/02/09 90000"]))