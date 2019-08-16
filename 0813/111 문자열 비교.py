import sys
sys.stdin = open("sample_input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    short = input()
    longs = input()
    count = 0
    jump = 0
    check = 0
    result = 2
    while True :
        jump = len(short)
        if result == 1 or result == 0:
            break 
        if count + jump >= len(longs):
            result = 0
            for j in range(len(longs)-count):
                for i in range(len(short)):
                    if short[len(short)-i-1] != longs[len(longs)-i-1-j]:
                        break
                    else :
                        check += 1
                if check == len(short):
                    result = 1 
                    break
                                        
        else:
            for i in range(len(short)):
                if short[len(short)-i-1] != longs[len(short)-i-1+count]:
                    count += jump
                    break
                else :
                    jump -= 1
                if jump == 0:
                    result = 1
                    break               
            
    print('#{} {}'.format(test_case, result))
