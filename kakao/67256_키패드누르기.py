def solution(numbers, hand):
    answer = ''
    if hand == "left":
        hand_index = 0
    else :
        hand_index = 1
    new_hand = [[3, 0], [3, 2]]
    for number in numbers:
        if number == 1 or number == 4 or number == 7 :
            answer += "L"
            new_hand[0] = [number // 3, 0]
        elif number == 3 or number == 6 or number == 9:
            answer += "R"
            new_hand[1] = [number // 3 - 1, 2]
        else:
            if number == 0:
                diff_left = abs(3 - new_hand[0][0]) + abs(1 - new_hand[0][1])
                diff_right = abs(3 - new_hand[1][0]) + abs(1 - new_hand[1][1])
                if diff_left > diff_right :
                    answer += "R"
                    new_hand[1] = [3, 1]
                elif diff_left < diff_right:
                    answer += "L"
                    new_hand[0] = [3, 1]
                else:
                    temp = hand[0].upper()
                    answer += temp
                    new_hand[hand_index] = [3, 1]
            else: 
                diff_left = abs(number//3 - new_hand[0][0]) + abs(1 - new_hand[0][1])
                diff_right = abs(number//3 - new_hand[1][0]) + abs(1 - new_hand[1][1])
                if diff_left > diff_right :
                    answer += "R"
                    new_hand[1] = [number//3, 1]
                elif diff_left < diff_right:
                    answer += "L"
                    new_hand[0] = [number//3, 1]
                else:
                    temp = hand[0].upper()
                    answer += temp
                    new_hand[hand_index] = [number//3, 1]


    return answer


print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right"))