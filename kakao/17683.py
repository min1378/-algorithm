def change(char):
    check = char.split("#")
    for i in range(len(check) - 1):
        temp = check[i][-1].lower()
        check[i] = check[i][:len(check[i]) - 1] + temp
    new_check = "".join(check)
    return new_check


def solution(m, musicinfos):
    new_m = change(m)
    answer = []
    for music in musicinfos:
        start_time, end_time, name, melody = music.split(',')
        start_hour, start_min = start_time.split(":")
        end_hour, end_min = end_time.split(":")
        end_minute = int(end_hour) * 60 + int(end_min)
        start_minute = int(start_hour) * 60 + int(start_min)
        diff_min = end_minute - start_minute
        count = diff_min // len(melody)
        progress = diff_min % len(melody)
        last = melody * count + melody[:progress + 1]
        new_last = change(last)
        if new_m in new_last:
            if answer == []:
                answer = [diff_min, name]
            else:
                if answer[0] < diff_min:
                    answer = [diff_min, name]

    if answer == []:
        return "(None)"
    else:
        return answer[1]


# print(
#     solution("ABC",
#              ["12:00,12:14,HELLO,C#DEFGAB", "13:00,13:05,WORLD,ABCDEF"]))
# print(
#     solution("ABCDEFG",
#              ["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"]))
# print(
#     solution("CC#BCC#BCC#BCC#B",
#              ["03:00,03:30,FOO,CC#B", "04:00,04:08,BAR,CC#BCC#BCC#B"]))
print(solution("cdcdf", ["12:00,12:11,HELLO,cdcdcdf"]))