const minTime = (n, time, visited) => {
  let minValue = 99999999;
  let index = -1;
  for (let i = 0; i < n; i++) {
    if (!visited[i] && minValue > time[i]) {
      index = i;
      minValue = time[i];
    }
  }
  return index;
};

const dijkstra = (graph, start, n, maxCost) => {
  const INT_MAX = 99999999999;
  const time = Array.from({ length: n }, (v) => INT_MAX);
  const visited = Array.from({ length: n }, (v) => false);
  const cost = Array.from({ length: n }, (v) => 0);
  time[start] = 0;
  for (let count = 0; count < n - 1; count++) {
    const index = minTime(n, time, visited);
    for (let vertax = 0; vertax < n; vertax++) {
      if (graph[index][vertax] === -1) continue;
      if (cost[vertax] > maxCost) continue;
      if (visited[vertax]) continue;
      if (time[vertax] < time[index] + graph[index][vertax][0]) continue;
      if (maxCost < cost[index] + graph[index][vertax][1]) continue;
      time[vertax] = time[index] + graph[index][vertax][0];
      cost[vertax] = cost[index] + graph[index][vertax][1];
    }
    visited[index] = true;
  }
  return time;
};
const makeBlankGraph = (row, col) => Array.from(Array(row), () => Array(col).fill(-1));
function solution(n, m, paths) {
  const graph = makeBlankGraph(n, n);
  for (const path of paths) {
    const [start, end, time, cost] = path;
    const weight = [time, cost];
    graph[start - 1][end - 1] = weight;
    graph[end - 1][start - 1] = weight;
  }
  console.log(dijkstra(graph, 0, n, m));


solution(5, 4, [
  [1, 2, 3, 2],
  [1, 3, 2, 2],
  [2, 4, 1, 1],
  [2, 5, 4, 1],
  [3, 5, 2, 3],
  [4, 5, 2, 1],
]);
