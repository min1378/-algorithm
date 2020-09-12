def isWall(x, y, N):
  if x < 0 or x > N - 1 or y < 0 or y > N - 1:
    return True
  return False

def cal_size(x, y, maps, p, r):
  for ran in range(r//2):
    maps[x][y]



def solution(maps, p, r):
  answer = 0
  width = len(maps)
  height = width
  for x in range(height):
    for y in range(width):
      print(maps[x][y])
      #answer = max(answer,cal_size(x, y, maps, p, r))
  return answer



solution([[1, 28, 41, 22, 25, 79, 4], [39, 20, 10, 17, 19, 18, 8], [21, 4, 13, 12, 9, 29, 19], [58, 1, 20, 5, 8, 16, 9], [5, 6, 15, 2, 39, 8, 29],[39, 7, 17, 5, 4, 49, 5], [74, 46, 8, 11, 25, 2, 11]], 19, 6)