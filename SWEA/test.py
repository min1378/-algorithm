import math

balls = [[65, 65],[250, 10]]
HOLES = [ [0, 0], [130, 0], [260, 0], [0, 130], [130, 130], [260, 130] ]
my_x = balls[0][0]
my_y = balls[0][1]
def distance(x, y):
    return math.sqrt(x ** 2 + y ** 2)

def find_hole(other_x, other_y):
    min_dist = 99999
    for i in range(len(HOLES)):
        hole_x = HOLES[i][0]
        hole_y = HOLES[i][1]
        diff_x2 = other_x - hole_x
        diff_y2 = other_y - hole_y
        hole_dist = distance(diff_x2, diff_y2)
        if min_dist > hole_dist:
            min_dist = hole_dist
            check = i
    return check

def cal_angle(diff_x, diff_y):
    return round(math.degrees(math.atan2(diff_y, diff_x)), 3)

for i in range(1, 2):
    # 각도 계산
    other_x = balls[i][0]
    other_y = balls[i][1]
    diff_x = other_x - my_x
    diff_y = other_y - my_y
    angle1 = cal_angle(diff_x, diff_y)
    ad_angle1 = 90 - angle1
    dist1 = distance(diff_x, diff_y)
    find = find_hole(other_x, other_y)
    hole_x = HOLES[find][0]
    hole_y = HOLES[find][1]
    diff2_x = hole_x - other_x
    diff2_y = hole_y - other_y
    angle2 = cal_angle(diff2_x, diff2_y)
    dist2 = distance(diff2_x, diff2_y)
    print('각도 : ', angle1, angle2)
    print('거리 : ', dist1, dist2)
    print(dist1 * 0.1 + dist2 * 0.9)
    print(ad_angle1)