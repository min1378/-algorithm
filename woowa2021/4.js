const dx = [-1, 0, 1, 0]
const dy = [0, 1, 0, -1]
function BFS(start, board, endNumber) {
  const [startX, startY, count] = start
  const queue = [start]
  const n = board.length
  const visited = Array.from(Array(n), () => Array(n).fill(false))
  visited[startX][startY] = true
  while (queue.length > 0) {
    const [x, y, count] = queue.shift()
    if (board[x][y] === endNumber) return [[x, y, 0], count + 1]
    for (let mode = 0; mode < 4; mode++) {
      let xx = x + dx[mode]
      let yy = y + dy[mode]
      if (xx === -1) xx = n - 1
      else if (yy === -1) yy = n - 1
      else if (xx === n) xx = 0
      else if (yy === n) yy = 0
      if (visited[xx][yy]) continue
      visited[xx][yy] = true
      queue.push([xx, yy, count + 1])
    }
  }
}
function solution(n, board) {
  let answer = 0
  let start = [0, 0, 0]
  for (let i = 1; i < n * n + 1; i++) {
    const [newStart, count] = BFS(start, board, i)
    answer += count
    start = newStart
  }
  console.log(answer)
  return answer
}
solution(2, [
  [2, 3],
  [4, 1],
])
