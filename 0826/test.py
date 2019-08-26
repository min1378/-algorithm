import sys
sys.stdin = open('input.txt', 'r')

def change(x):
    if x :
        x = 0
    else :
        x = 1
bulb_number = int(input())

bulb_info = list(map(int, input().split()))

student_number = int(input())

for _ in range(student_number):
student_info = list(map(int, input().split()))
if student_info[0] == 1:
for i in range(1, bulb_number):
if i % student_number[1] == 0:
change(bulb_info[i-1])
else:
symmetry_count = 0
if student_number[1] - 1 > bulb_number - student_number[1]:
count = bulb_number - student_number[1]
else:
count = student_number[1]
for j in range(1, count):
if bulb_info[student_number[1]-1-j] != bulb_info[student_number[1] - 1 + j]:
break
symmetry_count += 1
change(student_number[1]-1)
for k in range(1, symmetry_count):
    change(bulb_info[student_number[1]-1+k])
if bulb_info[student_number[1]-1+k] == 0:
bulb_info[student_number[1]-1+k] = 1
if bulb_info[student_number[1]-1-k] == 0:
bulb_info[student_number[1]-1-k] = 1

print(bulb_info)