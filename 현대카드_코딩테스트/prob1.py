def solution(purchase):
    answer = [0,0,0,0,0]
    record = [0] * 366
    month_cal = [0, 0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334] # 누적 그냥 계산 내가 해줌! 어차피 노가다하는거
    for pur in purchase:
        pur_len = len(pur)
        print(pur)
        mon = int(pur[5] + pur[6])
        day = int(pur[8] + pur[9])
        price = ''
        for i in range(11, pur_len):
            price += pur[i]
        price = int(price)
        print(mon, day, price)

        pur_date = month_cal[mon] + day
        record[pur_date] += price
    
    # 30일까지는 +로 계산
    temp_sum = 0
    for i in range(1, 31):
        temp_sum += record[i]
        if 0 <= temp_sum < 10000:
            answer[0] += 1
        elif 10000 <= temp_sum < 20000:
            answer[1] += 1
        elif 20000 <= temp_sum < 50000:
            answer[2] += 1
        elif 50000 <= temp_sum < 100000:
            answer[3] += 1
        else:
            answer[4] += 1
    for j in range(31, 366):
        temp_sum -= record[j - 30]
        temp_sum += record[j]
        if 0 <= temp_sum < 10000:
            answer[0] += 1
        elif 10000 <= temp_sum < 20000:
            answer[1] += 1
        elif 20000 <= temp_sum < 50000:
            answer[2] += 1
        elif 50000 <= temp_sum < 100000:
            answer[3] += 1
        else:
            answer[4] += 1
    print(answer)
    return answer

solution(["2019/01/01 5000", "2019/01/20 15000", "2019/02/09 90000"])