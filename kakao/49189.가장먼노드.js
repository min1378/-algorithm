function solution(n, edges) {
  let queue = [1];
  let visited = Array(n + 1).fill(0)
  const adj = Array.from(Array(n + 1), () => Array(n + 1).fill(0))
  const minDistance = new Array(n + 1).fill(Number.MAX_SAFE_INTEGER);
  console.log(minDistance)
  minDistance[0] = 0;
  minDistance[1] = 0;
  for (const edge of edges) {
    const [start, end] = edge
    adj[start][end] = 1
    adj[end][start] = 1
  }
  visited[0] = 1
  while (visited.reduce((a, b) => a + b, 0) < n + 1) {
    const vertax = queue.shift()
    visited[vertax] = 1
    for (let i = 1; i < adj[vertax].length; i++) {
      if (adj[vertax][i] === 1 && !visited[i]) queue.push(i)
      minDistance[i] =
        minDistance[i] > minDistance[vertax] + 1 ?
        minDistance[vertax] + 1 :
        minDistance[i];
    }
  }
  console.log(minDistance)
  const max = Math.max(...minDistance);
  console.log(max)
  const answer = minDistance.filter((d) => d === max);
  console.log(answer)
  return answer.length;
}

solution(6, [
  [3, 6],
  [4, 3],
  [3, 2],
  [1, 3],
  [1, 2],
  [2, 4],
  [5, 2]
])