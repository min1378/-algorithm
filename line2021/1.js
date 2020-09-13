function solution(boxes) {
  let answer = -1
  const itemMap = {}
  for (const box of boxes) {
    for (const b of box) {
      if (itemMap[b] >= 0) itemMap[b] += 1
      else itemMap[b] = 1
    }
  }
  let result = 0
  for (const count of Object.values(itemMap)) {
    if (count % 2 === 0) result += count
  }
  answer = boxes.length - result / 2
  return answer
}

solution([
  [1, 2],
  [2, 1],
  [3, 3],
  [4, 5],
  [5, 6],
  [7, 8],
])
