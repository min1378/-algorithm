function solution(n, start, end, roads, traps) {
  var answer = 0;
  const graph = Array.from(Array(n + 1), () => Array());
  for (const road of roads) {
    const [start, end, time] = road;
    graph[start].push(end);
  }
  return answer;
}
solution(
  3,
  1,
  3,
  [
    [1, 2, 2],
    [3, 2, 3],
  ],
  [2],
  5
);
