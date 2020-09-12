function solution(n, s, a, b, fares) {
  // 정점, 시작, A도착, B도착, 경로
  let answer = 999999999999
  const endList = [a, b]
  const adjacencyList = {}
  const addVertex = (vertex) => {
    if (!adjacencyList[vertex]) adjacencyList[vertex] = []
  }
  const addEdge = (vertex1, vertex2, weight) => {
    adjacencyList[vertex1].push({ node: vertex2, weight })
    adjacencyList[vertex2].push({ node: vertex1, weight })
  }

  const dfs = (start, result, flag) => {
    console.log(answer)
    if (answer < result) return
    if (Object.values(flag).indexOf(false) === -1) {
      answer = Math.min(answer, result)
      return
    }
    const stack = start
    const visited = {}
    let currentVertex

    visited[start] = true
    while (stack.length) {
      currentVertex = stack.pop()

      adjacencyList[currentVertex].forEach((neighbor) => {
        if (!visited[neighbor.node]) {
          visited[neighbor.node] = true
          if (neighbor.node === a) flag[0] = true

          if (neighbor.node === b) flag[1] = true
          stack.push(neighbor.node)
          dfs(stack, result + neighbor.weight, flag)
        }
      })
    }
  }
  for (let i = 0; i < n; i++) addVertex(i + 1)
  for (const fare of fares) {
    addEdge(fare[0], fare[1], fare[2])
  }
  dfs([s], 0, [false, false])
  return answer
}

console.log(
  solution(6, 4, 6, 2, [
    [4, 1, 10],
    [3, 5, 24],
    [5, 6, 2],
    [3, 1, 41],
    [5, 1, 24],
    [4, 6, 50],
    [2, 4, 66],
    [2, 3, 22],
    [1, 6, 25],
  ])
)
// console.log(
//   solution(7, 3, 4, 1, [
//     [5, 7, 9],
//     [4, 6, 4],
//     [3, 6, 1],
//     [3, 2, 3],
//     [2, 1, 6],
//   ])
// )
