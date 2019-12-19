import time

start = time.time()  # 시작 시간 저장

# 작업 코드

check = [i for i in range(1000000000)]
check.index(100-2)
print("time :", time.time() - start)  # 현재시각 - 시작시간 = 실행 시간