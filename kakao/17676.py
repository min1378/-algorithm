def solution(lines):
    times = []
    answer = 0
    for i in range(len(lines)):
        temp = lines[i].split(" ")
        time = temp[1].split(":")
        time_to_second_end = int(time[0]) * 3600 + int(time[1]) * 60 + float(
            time[2])
        time_to_second_start = time_to_second_end - float(temp[2][:-1]) + 0.001
        times.append([time_to_second_start, time_to_second_end, i])

    print(times)
    for time in times:
        start = time[0]
        end = time[1]
        index = time[2]
        count = 1
        count2 = 1
        for time2 in times:
            if index == time2[2]:
                continue
            if (start <= time2[0] < start + 1) or (start <= time2[1] <
                                                   start + 1):
                count += 1
            elif (time2[0] < start < time2[1]) and (time2[0] < start + 1 <
                                                    time2[1]):
                count += 1
        # for time3 in times:
        #     if index == time3[2]:
        #         continue
        #     if (end <= time3[0] < end + 1) or (end <= time3[1] < end + 1):
        #         count2 += 1
        #     elif (time3[0] < end < time3[1]) and (time3[0] < end + 1 <
        #                                           time3[1]):
        #         count2 += 1

        answer = max(answer, count)

    return answer


print(
    solution([
        "2016-09-15 20:59:57.421 0.351s", "2016-09-15 20:59:58.233 1.181s",
        "2016-09-15 20:59:58.299 0.8s", "2016-09-15 20:59:58.688 1.041s",
        "2016-09-15 20:59:59.591 1.412s", "2016-09-15 21:00:00.464 1.466s",
        "2016-09-15 21:00:00.741 1.581s", "2016-09-15 21:00:00.748 2.31s",
        "2016-09-15 21:00:00.966 0.381s", "2016-09-15 21:00:02.066 2.62s"
    ]))
