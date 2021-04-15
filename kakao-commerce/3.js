let count = 0;
function solution(n, passenger, train) {
  let answer = [0, 0];

  const graph = Array.from(Array(n + 1), () => Array());
  for (const [start, end] of train) {
    graph[start].push(end);
  }
  function DFS(v, passengerCount, visited) {
    if (graph[v].length === 0) {
      const [station, maxCount] = answer;
      if (maxCount < passengerCount) {
        answer = [v, passengerCount];
      } else if (maxCount === passengerCount) {
        if (station < v) {
          answer = [v, passengerCount];
        }
      }
    } else {
      for (let i = 0; i < graph[v].length; i++) {
        if (!visited[graph[v][i]]) {
          visited[graph[v][i]] = 1;
          DFS(graph[v][i], passengerCount + passenger[graph[v][i] - 1], visited);
          visited[graph[v][i]] = 0;
        }
      }
    }
  }
  const visited = Array.from({ length: n + 1 }, () => 0);
  visited[1] = 1;
  DFS(1, passenger[0], visited);
  return answer;
}
// const n = 100000;
// const passenger = Array.from(Array(100000), (v, i) => i);
// const train = Array.from(Array(100000 - 1), (v, i) => [1, i + 2]);

// console.log(solution(n, passenger, train));
// solution(
//   6,
//   [1, 1, 1, 1, 1, 1],
//   [
//     [1, 2],
//     [1, 3],
//     [1, 4],
//     [3, 5],
//     [3, 6],
//   ]
// );
// solution(
//   4,
//   [2, 1, 2, 2],
//   [
//     [1, 2],
//     [1, 3],
//     [2, 4],
//   ]
// );
try {
  const n2 = 100000;
  const passenger2 = Array.from(Array(100000), (v, i) => i);
  const train2 = Array.from(Array(100000 - 1), (v, i) => [i + 1, i + 2]);
  console.log(solution(n2, passenger2, train2));
} catch (e) {
  console.log("Maximum stack size is", count, "in your current browser");
}
