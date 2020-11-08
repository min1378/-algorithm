function isWall(x, y, n) {
  if (x < 0 || x > n - 1 || y < 0 || y > n - 1) return true
  return false
}
function solution(n, horizontal) {
  const answer = Array.from(Array(n), () => Array(n).fill(0))
  const location = []
  const dx = [-1, 0, 1, 1]
  const dy = [1, 1, 0, -1]
  if (horizontal) {
    location.push([0, 1, 3])
    answer[0][1] = 1
  } else {
    location.push([1, 0, 0])
    answer[1][0] = 1
  }
  let vertical = false
  let spandTime = 1
  while (location) {
    let [x, y, mode] = location.pop()
    if (mode === 1 || mode === 2) vertical = true
    else vertical = false
    if (mode === 1) mode = 3
    if (mode === 2) mode = 0
    let xx = x + dx[mode]
    let yy = y + dy[mode]
    if (isWall(xx, yy, n)) {
      if (mode === 0) {
        if (vertical) {
          mode = 3
          xx = x + dx[mode]
          yy = y + dy[mode]
        } else {
          mode = 1
          xx = x + dx[mode]
          yy = y + dy[mode]
          if (isWall(xx, yy, n)) {
            mode = 2
            xx = x + dx[mode]
            yy = y + dy[mode]
          }
        }
      } else if (mode === 3) {
        if (vertical) {
          mode = 0
          xx = x + dx[mode]
          yy = y + dy[mode]
        } else {
          mode = 2
          xx = x + dx[mode]
          yy = y + dy[mode]
          if (isWall(xx, yy, n)) {
            mode = 1
            xx = x + dx[mode]
            yy = y + dy[mode]
          }
        }
      }
    }
    if (mode === 0 || mode === 3) spandTime += 2
    if (mode === 1 || mode === 2) spandTime += 1
    answer[xx][yy] = spandTime
    if (xx === n - 1 && yy === n - 1) break
    location.push([xx, yy, mode])
  }
  return answer
}
solution(4, true)
solution(5, false)
