let q = []
let count = 0
let check = []
let adjs = [[]]

function makeAdjs(N, input, arr) {
  for (let k = 0; k < N; k++) {
    arr.push([])
  }
  console.log(arr)
  for (let i = 0; i < input.length; i++) {
    arr[input[i][0]].push(input[i][1])
  }
  console.log(arr)
  return arr
}

function bfs(n) {
  q.push(n)
  check[n] = true

  while (q.length) {
    const front = q.shift()
    const v = adjs[front]

    for (let i = 0; i < v.length; i++) {
      const node = v[i]
      if (!check[node]) {
        q.push(node)
        check[node] = true
        count++
      }
    }
  }
}
const input = [
  [0, 1],
  [0, 2],
  [0, 3],
  [1, 4],
  [1, 5],
  [2, 6],
  [3, 7],
  [3, 8],
  [3, 9],
  [4, 10],
  [4, 11],
  [5, 12],
  [5, 13],
  [6, 14],
  [6, 15],
  [6, 16],
  [8, 17],
  [8, 18],
]
const n = 19
adjs = makeAdjs(n, input, adjs)
bfs(0)

console.log(count)
